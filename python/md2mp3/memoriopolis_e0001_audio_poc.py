from __future__ import annotations

import argparse
import asyncio
import re
from pathlib import Path

import edge_tts

PROFILES = {
    "ja": {
        "voice": "ja-JP-NanamiNeural",
        "rate": "-8%",
        "stop_heading": "### 制作メモ",
    },
    "fr": {
        "voice": "fr-FR-DeniseNeural",
        "rate": "-8%",
        "stop_heading": "### Note de rédaction",
    },
}


def strip_front_matter(text: str) -> str:
    # Current E0001 files use YAML-like metadata without an opening --- marker.
    match = re.search(r"(?m)^##\s+E0001\b.*$", text)
    return text[match.start():] if match else text


def markdown_to_narration(text: str, stop_heading: str) -> str:
    text = strip_front_matter(text)

    if stop_heading in text:
        text = text.split(stop_heading, 1)[0]

    # Remove fenced code, images, standalone reference lines, and raw URLs.
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    text = re.sub(r"(?m)^\s*(参照|Référence)\s*：?.*$", "", text)
    text = re.sub(r"https?://\S+", "", text)

    # Keep link labels, remove Markdown syntax.
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"(?m)^#{1,6}\s+", "", text)
    text = re.sub(r"(?m)^\s*>\s?", "", text)
    text = re.sub(r"(?m)^\s*[-*+]\s+", "", text)
    text = text.replace("**", "").replace("__", "").replace("`", "")
    text = re.sub(r"<[^>]+>", "", text)

    # Normalize whitespace while keeping paragraph boundaries.
    text = text.replace("\u00a0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n[ \t]+", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


async def synthesize(md_path: Path, language: str, output_dir: Path) -> None:
    profile = PROFILES[language]
    source = md_path.read_text(encoding="utf-8-sig")
    narration = markdown_to_narration(source, profile["stop_heading"])

    output_dir.mkdir(parents=True, exist_ok=True)
    txt_path = output_dir / f"{md_path.stem}.narration.txt"
    mp3_path = output_dir / f"{md_path.stem}.mp3"
    srt_path = output_dir / f"{md_path.stem}.srt"

    txt_path.write_text(narration, encoding="utf-8")

    communicate = edge_tts.Communicate(
        narration,
        profile["voice"],
        rate=profile["rate"],
    )
    submaker = edge_tts.SubMaker()

    with mp3_path.open("wb") as audio_file:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_file.write(chunk["data"])
            elif chunk["type"] in ("WordBoundary", "SentenceBoundary"):
                submaker.feed(chunk)

    srt_path.write_text(submaker.get_srt(), encoding="utf-8")
    print(f"[OK] {md_path.name} -> {mp3_path.name}")
    print(f"     voice={profile['voice']} rate={profile['rate']}")


async def async_main(args: argparse.Namespace) -> None:
    await synthesize(args.ja, "ja", args.output)
    await synthesize(args.fr, "fr", args.output)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create one MP3 per canonical E0001 Markdown file."
    )
    parser.add_argument("--ja", type=Path, default=Path("E0001_ja.md"))
    parser.add_argument("--fr", type=Path, default=Path("E0001_fr.md"))
    parser.add_argument("--output", type=Path, default=Path("audio_E0001_poc"))
    args = parser.parse_args()
    asyncio.run(async_main(args))


if __name__ == "__main__":
    main()
