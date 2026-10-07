#!/usr/bin/env python3
"""Batch-generate MEMORIOPOLIS essay audio across per-essay directories.

Expected layout:
  essay/
    E0001/E0001_it.md
    E0002/E0002_en.md

Run from essay/ or pass --root <essay-folder>.
Requires: py -m pip install --upgrade edge-tts
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import re
import sys
import random
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

import edge_tts


@dataclass(frozen=True)
class VoiceConfig:
    locale: str
    preferred_voice: str
    rate: str


VOICE_CONFIGS = {
    "ja": VoiceConfig("ja-JP", "ja-JP-NanamiNeural", "-3%"),
    "en": VoiceConfig("en-US", "en-US-AndrewNeural", "-6%"),
    "zh-Hant-TW": VoiceConfig("zh-TW", "zh-TW-HsiaoChenNeural", "-8%"),
    "ko": VoiceConfig("ko-KR", "ko-KR-SunHiNeural", "-8%"),
    "ru": VoiceConfig("ru-RU", "ru-RU-SvetlanaNeural", "-8%"),
    "fil": VoiceConfig("fil-PH", "fil-PH-BlessicaNeural", "-8%"),
    "id": VoiceConfig("id-ID", "id-ID-GadisNeural", "-8%"),
    "vi": VoiceConfig("vi-VN", "vi-VN-HoaiMyNeural", "-10%"),
    "fr": VoiceConfig("fr-FR", "fr-FR-DeniseNeural", "-8%"),
    "de": VoiceConfig("de-DE", "de-DE-KatjaNeural", "-5%"),
    "it": VoiceConfig("it-IT", "it-IT-ElsaNeural", "-6%"),
}

STOP_HEADINGS = {
    "production notes", "working notes", "制作ノート", "note di lavorazione",
    "status", "状態",
}
FILE_RE = re.compile(r"^(E\d{4})_(.+)\.md$", re.I)
DIR_RE = re.compile(r"^E\d{4}$", re.I)


def parse_metadata_and_body(text: str) -> tuple[dict[str, str], str]:
    lines = text.replace("\r\n", "\n").split("\n")
    meta: dict[str, str] = {}
    body_start = None
    for i, line in enumerate(lines):
        if re.match(r"^#{1,6}\s+", line):
            body_start = i
            break
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if m:
            meta[m.group(1)] = m.group(2).strip().strip('"')
    if body_start is None:
        raise ValueError("No Markdown heading found")
    return meta, "\n".join(lines[body_start:])


def narration_from_markdown(text: str) -> tuple[str, dict[str, str]]:
    meta, body = parse_metadata_and_body(text)
    status = meta.get("status", "").lower()
    if status != "canonical":
        raise ValueError(f"status must be canonical, found: {status or '(missing)'}")

    kept: list[str] = []
    in_fence = False
    for raw in body.splitlines():
        line = raw.strip()
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        heading = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if heading:
            normalized = heading.group(2).strip().lower()
            if normalized in STOP_HEADINGS or normalized.startswith("production notes"):
                break
            continue

        if re.match(r"^\[\^[^]]+\]:", line):
            continue
        if re.match(r"^(Reference|Source|Riferimento|Referenz|Quelle)\s*:", line, re.I):
            continue
        if not line:
            kept.append("")
            continue

        line = re.sub(r"\[\^[^]]+\]", "", line)
        line = re.sub(r"!\[[^]]*\]\([^)]*\)", "", line)
        line = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", line)
        line = re.sub(r"^>\s?", "", line)
        line = re.sub(r"^[-*+]\s+", "", line)
        line = line.replace("**", "").replace("__", "").replace("*", "").replace("`", "")
        line = re.sub(r"<br\s*/?>", " ", line, flags=re.I)
        line = re.sub(r"\s+", " ", line).strip()
        if line:
            kept.append(line)

    paragraphs: list[str] = []
    current: list[str] = []
    for line in kept:
        if line:
            current.append(line)
        elif current:
            paragraphs.append(" ".join(current))
            current = []
    if current:
        paragraphs.append(" ".join(current))

    narration = "\n\n".join(paragraphs).strip()
    if len(narration) < 500:
        raise ValueError(f"Narration unexpectedly short: {len(narration)} characters")
    return narration, meta


def discover(root: Path, essays: set[str], languages: set[str]) -> list[tuple[Path, str, str]]:
    jobs: list[tuple[Path, str, str]] = []
    for essay_dir in sorted(p for p in root.iterdir() if p.is_dir() and DIR_RE.fullmatch(p.name)):
        essay_id = essay_dir.name.upper()
        if essays and essay_id not in essays:
            continue
        for source in sorted(essay_dir.glob(f"{essay_id}_*.md")):
            m = FILE_RE.fullmatch(source.name)
            if not m:
                continue
            language = m.group(2)
            if languages and language not in languages:
                continue
            if language not in VOICE_CONFIGS:
                print(f"[SKIP] No voice configuration: {source}")
                continue
            jobs.append((source, essay_id, language))
    return jobs


def discover_exact_jobs(root: Path, job_specs: list[str]) -> list[tuple[Path, str, str]]:
    jobs: list[tuple[Path, str, str]] = []
    for spec in job_specs:
        if ":" not in spec:
            raise ValueError(f"Invalid --job value: {spec}. Use E0001:it")
        essay_id, language = spec.split(":", 1)
        essay_id = essay_id.upper()
        if not DIR_RE.fullmatch(essay_id):
            raise ValueError(f"Invalid essay ID in --job: {essay_id}")
        if language not in VOICE_CONFIGS:
            raise ValueError(f"No voice configuration for language: {language}")
        source = root / essay_id / f"{essay_id}_{language}.md"
        if not source.is_file():
            raise FileNotFoundError(f"Source not found for --job {spec}: {source}")
        jobs.append((source, essay_id, language))
    return jobs


async def save_with_retry(communicate_factory, mp3: Path, srt: Path, retries: int = 4) -> None:
    for attempt in range(1, retries + 1):
        try:
            communicate = communicate_factory()
            await communicate.save(str(mp3), str(srt))
            return
        except Exception as exc:
            mp3.unlink(missing_ok=True)
            srt.unlink(missing_ok=True)
            if attempt >= retries:
                raise
            wait = min(20, (2 ** (attempt - 1)) + random.random())
            print(f"[WARN] TTS connection failed ({attempt}/{retries}): {exc}")
            print(f"[INFO] retrying in {wait:.1f} seconds...")
            await asyncio.sleep(wait)


def choose_voice(voices: list[dict], config: VoiceConfig) -> str:
    names = {v.get("ShortName") for v in voices}
    if config.preferred_voice in names:
        return config.preferred_voice
    candidates = sorted(
        [v for v in voices if v.get("Locale", "").lower() == config.locale.lower()],
        key=lambda v: (v.get("Gender") != "Female", v.get("ShortName", "")),
    )
    if not candidates:
        raise RuntimeError(f"No voice available for {config.locale}")
    replacement = candidates[0]["ShortName"]
    print(f"[WARN] {config.preferred_voice} unavailable; using {replacement}")
    return replacement


async def generate_one(source: Path, essay_id: str, language: str, voices: list[dict], overwrite: bool) -> dict:
    config = VOICE_CONFIGS[language]
    raw = source.read_text(encoding="utf-8-sig")
    narration, meta = narration_from_markdown(raw)
    if meta.get("essay_id", "").upper() != essay_id:
        raise ValueError(f"essay_id mismatch: folder={essay_id}, metadata={meta.get('essay_id')}")

    voice = choose_voice(voices, config)
    out_dir = source.parent / f"audio_{essay_id}_all"
    out_dir.mkdir(exist_ok=True)
    stem = source.stem
    mp3 = out_dir / f"{stem}.mp3"
    srt = out_dir / f"{stem}.srt"
    txt = out_dir / f"{stem}.narration.txt"
    info = out_dir / f"{stem}.audio.json"

    if mp3.exists() and not overwrite:
        return {"status": "skipped-existing", "source": str(source), "mp3": str(mp3)}

    tmp_mp3 = out_dir / f".{stem}.mp3.tmp"
    tmp_srt = out_dir / f".{stem}.srt.tmp"
    tmp_mp3.unlink(missing_ok=True)
    tmp_srt.unlink(missing_ok=True)

    await save_with_retry(lambda: edge_tts.Communicate(narration, voice=voice, rate=config.rate), tmp_mp3, tmp_srt, retries=4)
    if not tmp_mp3.exists() or tmp_mp3.stat().st_size < 1024:
        raise RuntimeError("Generated MP3 is missing or too small")
    tmp_mp3.replace(mp3)
    tmp_srt.replace(srt)
    txt.write_text(narration + "\n", encoding="utf-8")

    record = {
        "status": "generated",
        "essay_id": essay_id,
        "language": language,
        "source": str(source),
        "output_directory": str(out_dir),
        "locale": config.locale,
        "preferred_voice": config.preferred_voice,
        "voice": voice,
        "rate": config.rate,
        "source_sha256": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
        "narration_sha256": hashlib.sha256(narration.encode("utf-8")).hexdigest(),
        "narration_characters": len(narration),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "outputs": {"mp3": str(mp3), "srt": str(srt), "narration": str(txt)},
    }
    info.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[OK] {source.relative_to(source.parents[1])} -> {mp3.relative_to(source.parents[1])}")
    print(f"     locale={config.locale} voice={voice} rate={config.rate}")
    return record


async def main_async(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"[ERROR] essay root not found: {root}", file=sys.stderr)
        return 2

    essays = {x.upper() for x in args.essay}
    languages = set(args.language)
    try:
        jobs = discover_exact_jobs(root, args.job) if args.job else discover(root, essays, languages)
    except Exception as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 2
    if not jobs:
        print("[ERROR] No matching canonical Markdown candidates found", file=sys.stderr)
        return 2

    print(f"[INFO] root={root}")
    print(f"[INFO] discovered={len(jobs)}")
    voices = await edge_tts.list_voices()
    results, errors = [], []
    for source, essay_id, language in jobs:
        try:
            results.append(await generate_one(source, essay_id, language, voices, args.overwrite))
        except Exception as exc:
            error = {"source": str(source), "error": f"{type(exc).__name__}: {exc}"}
            errors.append(error)
            print(f"[ERROR] {source}: {exc}", file=sys.stderr)
            if not args.continue_on_error:
                break

    manifest = root / "MEMORIOPOLIS_essay_audio_manifest.json"
    manifest.write_text(json.dumps({"root": str(root), "results": results, "errors": errors}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[INFO] manifest={manifest}")
    return 1 if errors else 0


def parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Generate MP3s from canonical Markdown files stored in E#### subfolders.")
    p.add_argument("--root", default=".", help="Path to the essay directory containing E0001, E0002, ...")
    p.add_argument("--job", action="append", default=[], help="Exact Essay/language pair, e.g. --job E0001:it. Repeatable.")
    p.add_argument("--essay", action="append", default=[], help="Limit to an essay ID, e.g. --essay E0001. Repeatable.")
    p.add_argument("--language", action="append", default=[], help="Limit to a language suffix, e.g. --language it. Repeatable.")
    p.add_argument("--overwrite", action="store_true")
    p.add_argument("--continue-on-error", action="store_true")
    return p


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main_async(parser().parse_args())))
