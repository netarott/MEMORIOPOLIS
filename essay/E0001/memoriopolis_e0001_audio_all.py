from __future__ import annotations

import argparse
import asyncio
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import edge_tts

# 1 Markdown = 1 MP3
# Voice IDs are checked against the live edge-tts voice list before synthesis.
PROFILES = {
    "ja": {
        "file": "E0001_ja.md",
        "locale": "ja-JP",
        "preferred": ["ja-JP-NanamiNeural", "ja-JP-KeitaNeural"],
        "rate": "-3%",
    },
    "en": {
        "file": "E0001_en.md",
        "locale": "en-US",
        "preferred": ["en-US-AndrewNeural", "en-US-EmmaNeural", "en-US-AriaNeural"],
        "rate": "-6%",
    },
    "zh-Hant-TW": {
        "file": "E0001_zh-Hant-TW.md",
        "locale": "zh-TW",
        "preferred": ["zh-TW-HsiaoChenNeural", "zh-TW-YunJheNeural", "zh-TW-HsiaoYuNeural"],
        "rate": "-8%",
    },
    "ko": {
        "file": "E0001_ko.md",
        "locale": "ko-KR",
        "preferred": ["ko-KR-SunHiNeural", "ko-KR-InJoonNeural"],
        "rate": "-8%",
    },
    "ru": {
        "file": "E0001_ru.md",
        "locale": "ru-RU",
        "preferred": ["ru-RU-SvetlanaNeural", "ru-RU-DmitryNeural"],
        "rate": "-8%",
    },
    "fil": {
        "file": "E0001_fil.md",
        "locale": "fil-PH",
        "preferred": ["fil-PH-BlessicaNeural", "fil-PH-AngeloNeural"],
        "rate": "-8%",
    },
    "id": {
        "file": "E0001_id.md",
        "locale": "id-ID",
        "preferred": ["id-ID-GadisNeural", "id-ID-ArdiNeural"],
        "rate": "-8%",
    },
    "vi": {
        "file": "E0001_vi.md",
        "locale": "vi-VN",
        "preferred": ["vi-VN-HoaiMyNeural", "vi-VN-NamMinhNeural"],
        "rate": "-10%",
    },
    "fr": {
        "file": "E0001_fr.md",
        "locale": "fr-FR",
        "preferred": ["fr-FR-DeniseNeural", "fr-FR-HenriNeural"],
        "rate": "-8%",
    },
}

# Stop before non-Essay production notes. Add a marker here if a future language
# uses another heading. Matching is intentionally multilingual and conservative.
STOP_HEADING_PATTERNS = [
    r"^#{1,6}\s*制作メモ\s*$",
    r"^#{1,6}\s*Production Notes?\s*$",
    r"^#{1,6}\s*Note de rédaction\s*$",
    r"^#{1,6}\s*Notas? de (?:producción|redacción)\s*$",
    r"^#{1,6}\s*Nota de produção\s*$",
    r"^#{1,6}\s*Note di (?:produzione|redazione)\s*$",
    r"^#{1,6}\s*Produktionsnotiz(?:en)?\s*$",
    r"^#{1,6}\s*제작 메모\s*$",
    r"^#{1,6}\s*Примечани[ея] (?:к|по) (?:тексту|созданию)\s*$",
    r"^#{1,6}\s*Mga Tala sa Pagbuo\s*$",
    r"^#{1,6}\s*Catatan (?:Produksi|Penyusunan)\s*$",
    r"^#{1,6}\s*Ghi chú (?:biên soạn|sản xuất)\s*$",
]


def strip_front_matter(text: str) -> str:
    """Remove YAML front matter or pre-title metadata, keeping the Essay title."""
    # Standard YAML front matter.
    text = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", text, flags=re.DOTALL)

    # Existing E0001 files may contain metadata before a level-2 E0001 heading.
    match = re.search(r"(?m)^##\s+E0001\b.*$", text)
    return text[match.start():] if match else text


def cut_production_notes(text: str) -> str:
    earliest = None
    for pattern in STOP_HEADING_PATTERNS:
        match = re.search(pattern, text, flags=re.MULTILINE | re.IGNORECASE)
        if match and (earliest is None or match.start() < earliest):
            earliest = match.start()
    return text[:earliest] if earliest is not None else text


def markdown_to_narration(text: str) -> str:
    text = strip_front_matter(text)
    text = cut_production_notes(text)

    # Remove code, images, HTML, reference-only lines, and raw URLs.
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"~~~.*?~~~", "", text, flags=re.DOTALL)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    text = re.sub(
        r"(?mi)^\s*(参照|参考|reference|référence|fuente|fonte|quelle|источник|출처|sanggunian|sumber|nguồn)\s*[:：].*$",
        "",
        text,
    )
    text = re.sub(r"https?://\S+", "", text)

    # Keep Markdown link labels but remove markup.
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"(?m)^#{1,6}\s+", "", text)
    text = re.sub(r"(?m)^\s*>\s?", "", text)
    text = re.sub(r"(?m)^\s*[-*+]\s+", "", text)
    text = text.replace("**", "").replace("__", "").replace("`", "")
    text = re.sub(r"<[^>]+>", "", text)

    # Remove simple footnote definitions and horizontal rules.
    text = re.sub(r"(?m)^\[\^[^\]]+\]:.*$", "", text)
    text = re.sub(r"(?m)^\s*[-*_]{3,}\s*$", "", text)

    # Normalize spacing while preserving paragraph boundaries.
    text = text.replace("\u00a0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n[ \t]+", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def source_says_canonical(text: str) -> bool:
    """Return True if metadata explicitly says canonical; False if draft; else True."""
    status = re.search(r"(?mi)^\s*status\s*:\s*([\w-]+)\s*$", text)
    if not status:
        return True
    return status.group(1).lower() == "canonical"


async def get_voice_catalog() -> list[dict]:
    print("[INFO] edge-tts voice listを取得しています...")
    return await edge_tts.list_voices()


def choose_voice(profile: dict, voices: list[dict]) -> str:
    available_names = {v["ShortName"] for v in voices}
    for candidate in profile["preferred"]:
        if candidate in available_names:
            return candidate

    locale_matches = [
        v["ShortName"] for v in voices if v.get("Locale", "").lower() == profile["locale"].lower()
    ]
    if locale_matches:
        return sorted(locale_matches)[0]

    raise RuntimeError(
        f"音声が見つかりません: locale={profile['locale']}。"
        " edge-tts --list-voices の結果を確認してください。"
    )


async def synthesize_one(
    language: str,
    profile: dict,
    voice: str,
    input_dir: Path,
    output_dir: Path,
    overwrite: bool,
) -> dict:
    md_path = input_dir / profile["file"]
    if not md_path.exists():
        raise FileNotFoundError(f"入力ファイルがありません: {md_path}")

    source = md_path.read_text(encoding="utf-8-sig")
    if not source_says_canonical(source):
        raise RuntimeError(f"canonicalではありません: {md_path.name}")

    narration = markdown_to_narration(source)
    if len(narration) < 100:
        raise RuntimeError(f"本文抽出結果が短すぎます: {md_path.name}")

    output_dir.mkdir(parents=True, exist_ok=True)
    txt_path = output_dir / f"{md_path.stem}.narration.txt"
    mp3_path = output_dir / f"{md_path.stem}.mp3"
    srt_path = output_dir / f"{md_path.stem}.srt"

    if mp3_path.exists() and not overwrite:
        print(f"[SKIP] 既存MP3: {mp3_path.name}")
        return {
            "language": language,
            "source": md_path.name,
            "status": "skipped",
            "voice": voice,
            "rate": profile["rate"],
        }

    txt_path.write_text(narration, encoding="utf-8")

    communicator = edge_tts.Communicate(
        narration,
        voice,
        rate=profile["rate"],
    )
    submaker = edge_tts.SubMaker()

    # Write to temporary files first to avoid leaving a broken final MP3.
    temp_mp3 = mp3_path.with_suffix(".mp3.part")
    try:
        with temp_mp3.open("wb") as audio_file:
            async for chunk in communicator.stream():
                if chunk["type"] == "audio":
                    audio_file.write(chunk["data"])
                elif chunk["type"] in ("WordBoundary", "SentenceBoundary"):
                    submaker.feed(chunk)
        temp_mp3.replace(mp3_path)
    finally:
        if temp_mp3.exists():
            temp_mp3.unlink()

    srt_path.write_text(submaker.get_srt(), encoding="utf-8")

    print(f"[OK] {md_path.name} -> {mp3_path.name}")
    print(f"     locale={profile['locale']} voice={voice} rate={profile['rate']}")

    return {
        "language": language,
        "source": md_path.name,
        "status": "generated",
        "voice": voice,
        "locale": profile["locale"],
        "rate": profile["rate"],
        "mp3": mp3_path.name,
        "narration": txt_path.name,
        "srt": srt_path.name,
        "characters": len(narration),
    }


async def async_main(args: argparse.Namespace) -> None:
    voices = await get_voice_catalog()
    selected = {lang: choose_voice(profile, voices) for lang, profile in PROFILES.items()}

    print("[INFO] 使用する音声")
    for lang, profile in PROFILES.items():
        print(f"  {lang:10s} {selected[lang]}  rate={profile['rate']}")

    results = []
    failures = []

    # Sequential generation is slower but more stable and easier to diagnose.
    for language, profile in PROFILES.items():
        try:
            result = await synthesize_one(
                language=language,
                profile=profile,
                voice=selected[language],
                input_dir=args.input,
                output_dir=args.output,
                overwrite=args.overwrite,
            )
            results.append(result)
        except Exception as exc:
            failures.append({"language": language, "file": profile["file"], "error": str(exc)})
            print(f"[ERROR] {profile['file']}: {exc}")
            if not args.continue_on_error:
                break

    manifest = {
        "work": "E0001",
        "rule": "1 Markdown = 1 MP3",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "engine": "edge-tts",
        "results": results,
        "failures": failures,
    }
    args.output.mkdir(parents=True, exist_ok=True)
    manifest_path = args.output / "E0001_audio_manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print()
    print(f"[DONE] 成功/スキップ: {len(results)}  失敗: {len(failures)}")
    print(f"[INFO] manifest: {manifest_path}")
    if failures:
        raise SystemExit(1)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate one MP3 for each canonical multilingual E0001 Markdown file."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("."),
        help="E0001_*.md files directory (default: current directory)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("audio_E0001_all"),
        help="Output directory (default: audio_E0001_all)",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing MP3 files",
    )
    parser.add_argument(
        "--continue-on-error",
        action="store_true",
        help="Continue processing the remaining languages after an error",
    )
    args = parser.parse_args()
    asyncio.run(async_main(args))


if __name__ == "__main__":
    main()
