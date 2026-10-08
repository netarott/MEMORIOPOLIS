#!/usr/bin/env python3
"""Synchronize missing MEMORIOPOLIS Essay MP3 files.

Default behavior:
- scan essay/E####/E####_*.md
- skip when the corresponding MP3 already exists
- generate only missing MP3s from canonical Markdown
- keep output inside each Essay directory: audio_E####_all/

Requires:
    py -m pip install --upgrade edge-tts
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import random
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

try:
    import edge_tts
except ImportError:
    print("[ERROR] edge-tts is not installed.", file=sys.stderr)
    print("Run: py -m pip install --upgrade edge-tts", file=sys.stderr)
    raise SystemExit(2)


@dataclass(frozen=True)
class VoiceConfig:
    locale: str
    preferred_voice: str
    rate: str


# Language suffix used in E####_<suffix>.md -> Edge TTS settings.
VOICE_CONFIGS: dict[str, VoiceConfig] = {
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
    "es": VoiceConfig("es-ES", "es-ES-ElviraNeural", "-6%"),
    "pt-BR": VoiceConfig("pt-BR", "pt-BR-FranciscaNeural", "-7%"),
}

DIR_RE = re.compile(r"^E\d{4}$", re.I)
FILE_RE = re.compile(r"^(E\d{4})_(.+)\.md$", re.I)
STOP_HEADINGS = {
    "production notes", "working notes", "制作ノート", "制作メモ", "状態", "status",
    "note di lavorazione", "notas de producción", "notas de produccion",
    "notas de produção", "notas de producao", "produktiosnotizen", "produktionsnotizen",
    "製作筆記", "제작 노트",
}


def parse_metadata_and_body(text: str) -> tuple[dict[str, str], str]:
    lines = text.replace("\r\n", "\n").split("\n")
    metadata: dict[str, str] = {}
    body_start: int | None = None
    for index, line in enumerate(lines):
        if re.match(r"^#{1,6}\s+", line):
            body_start = index
            break
        match = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if match:
            metadata[match.group(1)] = match.group(2).strip().strip('"')
    if body_start is None:
        raise ValueError("No Markdown heading was found")
    return metadata, "\n".join(lines[body_start:])


def markdown_to_narration(text: str) -> tuple[str, dict[str, str]]:
    metadata, body = parse_metadata_and_body(text)
    status = metadata.get("status", "").strip().lower()
    if status != "canonical":
        raise ValueError(f"status must be canonical, found: {status or '(missing)'}")

    lines: list[str] = []
    in_code_fence = False
    for raw in body.splitlines():
        line = raw.strip()
        if line.startswith("```"):
            in_code_fence = not in_code_fence
            continue
        if in_code_fence:
            continue

        heading = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if heading:
            normalized = heading.group(2).strip().lower()
            if normalized in STOP_HEADINGS or normalized.startswith("production notes"):
                break
            # Do not narrate title or intermediate headings.
            continue

        if re.match(r"^\[\^[^]]+\]:", line):
            continue
        if re.match(r"^(Reference|Source|Riferimento|Referenz|Quelle|Fuente|Fonte)\s*:", line, re.I):
            continue
        if not line:
            lines.append("")
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
            lines.append(line)

    paragraphs: list[str] = []
    current: list[str] = []
    for line in lines:
        if line:
            current.append(line)
        elif current:
            paragraphs.append(" ".join(current))
            current = []
    if current:
        paragraphs.append(" ".join(current))

    narration = "\n\n".join(paragraphs).strip()
    if len(narration) < 300:
        raise ValueError(f"Narration is unexpectedly short: {len(narration)} characters")
    return narration, metadata


def discover_markdown(root: Path) -> list[tuple[Path, str, str]]:
    jobs: list[tuple[Path, str, str]] = []
    for essay_dir in sorted(p for p in root.iterdir() if p.is_dir() and DIR_RE.fullmatch(p.name)):
        essay_id = essay_dir.name.upper()
        for source in sorted(essay_dir.glob(f"{essay_id}_*.md")):
            match = FILE_RE.fullmatch(source.name)
            if not match:
                continue
            jobs.append((source, essay_id, match.group(2)))
    return jobs


def selected(source: Path, essay_id: str, language: str, args: argparse.Namespace) -> bool:
    if args.essay and essay_id not in {value.upper() for value in args.essay}:
        return False
    if args.language and language not in set(args.language):
        return False
    if args.job and f"{essay_id}:{language}" not in set(args.job):
        return False
    return True


def output_paths(source: Path, essay_id: str) -> dict[str, Path]:
    output_dir = source.parent / f"audio_{essay_id}_all"
    stem = source.stem
    return {
        "dir": output_dir,
        "mp3": output_dir / f"{stem}.mp3",
        "srt": output_dir / f"{stem}.srt",
        "txt": output_dir / f"{stem}.narration.txt",
        "json": output_dir / f"{stem}.audio.json",
    }


def choose_voice(voices: list[dict], config: VoiceConfig) -> str:
    names = {voice.get("ShortName") for voice in voices}
    if config.preferred_voice in names:
        return config.preferred_voice
    alternatives = sorted(
        [voice for voice in voices if voice.get("Locale", "").lower() == config.locale.lower()],
        key=lambda voice: (voice.get("Gender") != "Female", voice.get("ShortName", "")),
    )
    if not alternatives:
        raise RuntimeError(f"No voice is available for locale {config.locale}")
    replacement = alternatives[0]["ShortName"]
    print(f"[WARN] {config.preferred_voice} unavailable; using {replacement}")
    return replacement


async def save_with_retry(factory, mp3: Path, srt: Path, retries: int) -> None:
    for attempt in range(1, retries + 1):
        try:
            await factory().save(str(mp3), str(srt))
            return
        except Exception as exc:
            mp3.unlink(missing_ok=True)
            srt.unlink(missing_ok=True)
            if attempt >= retries:
                raise
            wait = min(30.0, (2 ** (attempt - 1)) + random.random())
            print(f"[WARN] TTS connection failed ({attempt}/{retries}): {exc}")
            print(f"[INFO] retrying in {wait:.1f} seconds")
            await asyncio.sleep(wait)


async def generate(
    source: Path,
    essay_id: str,
    language: str,
    voices: list[dict],
    args: argparse.Namespace,
) -> dict:
    paths = output_paths(source, essay_id)

    # The primary synchronization rule: existing MP3 means no work.
    if paths["mp3"].exists() and not args.overwrite:
        print(f"[SKIP] exists: {paths['mp3'].relative_to(args.root_path)}")
        return {"status": "skipped-existing", "source": str(source), "mp3": str(paths["mp3"])}

    if language not in VOICE_CONFIGS:
        print(f"[SKIP] unsupported language suffix: {source.name}")
        return {"status": "skipped-unsupported-language", "source": str(source), "language": language}

    raw = source.read_text(encoding="utf-8-sig")
    narration, metadata = markdown_to_narration(raw)
    if metadata.get("essay_id", "").upper() != essay_id:
        raise ValueError(
            f"essay_id mismatch: folder={essay_id}, metadata={metadata.get('essay_id', '(missing)')}"
        )

    config = VOICE_CONFIGS[language]
    voice = choose_voice(voices, config)
    if args.dry_run:
        print(f"[CREATE] {source.relative_to(args.root_path)} -> {paths['mp3'].relative_to(args.root_path)}")
        return {"status": "dry-run-create", "source": str(source), "mp3": str(paths["mp3"])}

    paths["dir"].mkdir(exist_ok=True)
    temp_mp3 = paths["dir"] / f".{source.stem}.mp3.tmp"
    temp_srt = paths["dir"] / f".{source.stem}.srt.tmp"
    temp_mp3.unlink(missing_ok=True)
    temp_srt.unlink(missing_ok=True)

    await save_with_retry(
        lambda: edge_tts.Communicate(narration, voice=voice, rate=config.rate),
        temp_mp3,
        temp_srt,
        args.retries,
    )
    if not temp_mp3.exists() or temp_mp3.stat().st_size < 1024:
        raise RuntimeError("Generated MP3 is missing or too small")

    temp_mp3.replace(paths["mp3"])
    temp_srt.replace(paths["srt"])
    paths["txt"].write_text(narration + "\n", encoding="utf-8")

    record = {
        "status": "generated",
        "essay_id": essay_id,
        "language": language,
        "source": str(source),
        "locale": config.locale,
        "preferred_voice": config.preferred_voice,
        "voice": voice,
        "rate": config.rate,
        "source_sha256": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
        "narration_sha256": hashlib.sha256(narration.encode("utf-8")).hexdigest(),
        "narration_characters": len(narration),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "outputs": {key: str(value) for key, value in paths.items() if key != "dir"},
    }
    paths["json"].write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"[OK] {source.relative_to(args.root_path)} -> {paths['mp3'].relative_to(args.root_path)}")
    print(f"     locale={config.locale} voice={voice} rate={config.rate}")
    return record


async def main_async(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve()
    args.root_path = root
    if not root.is_dir():
        print(f"[ERROR] Essay root not found: {root}", file=sys.stderr)
        return 2

    discovered = [job for job in discover_markdown(root) if selected(*job, args)]
    if not discovered:
        print("[INFO] No matching Markdown files were found")
        return 0

    existing = []
    missing_supported = []
    unsupported = []
    for source, essay_id, language in discovered:
        paths = output_paths(source, essay_id)
        if paths["mp3"].exists() and not args.overwrite:
            existing.append((source, essay_id, language))
        elif language in VOICE_CONFIGS:
            missing_supported.append((source, essay_id, language))
        else:
            unsupported.append((source, essay_id, language))

    print(f"[INFO] root={root}")
    print(f"[INFO] Markdown discovered={len(discovered)}")
    print(f"[INFO] MP3 already exists={len(existing)}")
    print(f"[INFO] MP3 to create={len(missing_supported)}")
    print(f"[INFO] unsupported language={len(unsupported)}")

    # Avoid any network call when everything is already synchronized.
    voices: list[dict] = []
    if missing_supported and not args.dry_run:
        voices = await edge_tts.list_voices()

    results: list[dict] = []
    errors: list[dict] = []
    for source, essay_id, language in discovered:
        try:
            results.append(await generate(source, essay_id, language, voices, args))
        except Exception as exc:
            errors.append({"source": str(source), "error": f"{type(exc).__name__}: {exc}"})
            print(f"[ERROR] {source.relative_to(root)}: {exc}", file=sys.stderr)
            if not args.continue_on_error:
                break

    manifest = root / "MEMORIOPOLIS_essay_audio_manifest.json"
    if not args.dry_run:
        manifest.write_text(
            json.dumps(
                {
                    "root": str(root),
                    "run_at_utc": datetime.now(timezone.utc).isoformat(),
                    "results": results,
                    "errors": errors,
                },
                ensure_ascii=False,
                indent=2,
            ) + "\n",
            encoding="utf-8",
        )
        print(f"[INFO] manifest={manifest}")

    generated_count = sum(item.get("status") == "generated" for item in results)
    skipped_count = sum(item.get("status", "").startswith("skipped") for item in results)
    print(f"[SUMMARY] generated={generated_count} skipped={skipped_count} errors={len(errors)}")
    return 1 if errors else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create only missing MP3 files from canonical Markdown stored in E#### directories."
    )
    parser.add_argument("--root", default=".", help="essay directory containing E0001, E0002, ...")
    parser.add_argument("--essay", action="append", default=[], help="limit to Essay ID; repeatable")
    parser.add_argument("--language", action="append", default=[], help="limit to language suffix; repeatable")
    parser.add_argument("--job", action="append", default=[], help="exact pair such as E0002:ja; repeatable")
    parser.add_argument("--overwrite", action="store_true", help="regenerate MP3 even if it already exists")
    parser.add_argument("--dry-run", action="store_true", help="show create/skip decisions without TTS calls")
    parser.add_argument("--retries", type=int, default=4, help="TTS retry count; default 4")
    parser.add_argument("--continue-on-error", action="store_true")
    return parser


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main_async(build_parser().parse_args())))
