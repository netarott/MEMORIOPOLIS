from __future__ import annotations

import argparse
import asyncio
import json
import re
from datetime import datetime, timezone
from pathlib import Path

import edge_tts

VOICE = "de-DE-KatjaNeural"
RATE = "-5%"
LOCALE = "de-DE"


def strip_front_matter(text: str) -> str:
    text = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", text, flags=re.DOTALL)
    match = re.search(r"(?m)^##\s+E0001\b.*$", text)
    return text[match.start():] if match else text


def markdown_to_narration(text: str) -> str:
    text = strip_front_matter(text)

    # Stop before production notes.
    marker = re.search(r"(?mi)^#{1,6}\s*Produktionsnotizen\s*$", text)
    if marker:
        text = text[:marker.start()]

    # Remove non-narrative Markdown structures.
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"~~~.*?~~~", "", text, flags=re.DOTALL)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    text = re.sub(r"(?mi)^\s*(Referenz|Quelle)\s*[:：].*$", "", text)
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"(?m)^#{1,6}\s+", "", text)
    text = re.sub(r"(?m)^\s*>\s?", "", text)
    text = re.sub(r"(?m)^\s*[-*+]\s+", "", text)
    text = text.replace("**", "").replace("__", "").replace("`", "")
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"(?m)^\s*[-*_]{3,}\s*$", "", text)

    text = text.replace("\u00a0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n[ \t]+", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


async def choose_voice() -> str:
    voices = await edge_tts.list_voices()
    names = {v["ShortName"] for v in voices}
    if VOICE in names:
        return VOICE

    alternatives = sorted(
        v["ShortName"] for v in voices if v.get("Locale", "").lower() == LOCALE.lower()
    )
    if not alternatives:
        raise RuntimeError(f"No edge-tts voice found for {LOCALE}")
    return alternatives[0]


async def synthesize(source_path: Path, output_dir: Path, overwrite: bool) -> None:
    source = source_path.read_text(encoding="utf-8-sig")
    if not re.search(r"(?mi)^status\s*:\s*canonical\s*$", source):
        raise RuntimeError("E0001_de.md is not marked status: canonical")

    narration = markdown_to_narration(source)
    if len(narration) < 100:
        raise RuntimeError("Narration text is unexpectedly short")

    output_dir.mkdir(parents=True, exist_ok=True)
    txt_path = output_dir / "E0001_de.narration.txt"
    srt_path = output_dir / "E0001_de.srt"
    mp3_path = output_dir / "E0001_de.mp3"
    manifest_path = output_dir / "E0001_de.audio.json"

    if mp3_path.exists() and not overwrite:
        print(f"[SKIP] {mp3_path} already exists. Use --overwrite to regenerate.")
        return

    voice = await choose_voice()
    txt_path.write_text(narration, encoding="utf-8")

    communicator = edge_tts.Communicate(narration, voice, rate=RATE)
    submaker = edge_tts.SubMaker()
    temp_path = mp3_path.with_suffix(".mp3.part")

    try:
        with temp_path.open("wb") as audio_file:
            async for chunk in communicator.stream():
                if chunk["type"] == "audio":
                    audio_file.write(chunk["data"])
                elif chunk["type"] in ("WordBoundary", "SentenceBoundary"):
                    submaker.feed(chunk)
        temp_path.replace(mp3_path)
    finally:
        if temp_path.exists():
            temp_path.unlink()

    srt_path.write_text(submaker.get_srt(), encoding="utf-8")
    manifest = {
        "work": "E0001",
        "language": "de",
        "source": source_path.name,
        "source_status": "canonical",
        "engine": "edge-tts",
        "locale": LOCALE,
        "voice": voice,
        "rate": RATE,
        "rule": "1 Markdown = 1 MP3",
        "characters": len(narration),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[OK] {source_path.name} -> {mp3_path.name}")
    print(f"     locale={LOCALE} voice={voice} rate={RATE}")
    print(f"     narration={txt_path.name}")
    print(f"     subtitles={srt_path.name}")
    print(f"     manifest={manifest_path.name}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate E0001_de.mp3 from canonical E0001_de.md")
    parser.add_argument("--input", type=Path, default=Path("E0001_de.md"))
    parser.add_argument("--output", type=Path, default=Path("audio_E0001_all"))
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    asyncio.run(synthesize(args.input, args.output, args.overwrite))


if __name__ == "__main__":
    main()
