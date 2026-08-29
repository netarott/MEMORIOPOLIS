#!/usr/bin/env python3
"""Combine the silent section 10 trailer with its generated soundtrack.

Run from any directory:
    py novel/chapter04/section10/trailer/mux_trailer_audio.py

Output:
    output/section10_trailer_prototype01.mp4
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

try:
    import imageio_ffmpeg
except ImportError as exc:
    raise SystemExit(
        "imageio-ffmpeg is not installed. Run:\n"
        "  py -m pip install imageio-ffmpeg"
    ) from exc


BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
DEFAULT_VIDEO = OUTPUT_DIR / "section10_trailer_silent_prototype01.mp4"
DEFAULT_AUDIO = OUTPUT_DIR / "section10_trailer_soundtrack_prototype01.wav"
DEFAULT_OUTPUT = OUTPUT_DIR / "section10_trailer_prototype01.mp4"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Mux the silent trailer and soundtrack into an MP4."
    )
    parser.add_argument("--video", type=Path, default=DEFAULT_VIDEO)
    parser.add_argument("--audio", type=Path, default=DEFAULT_AUDIO)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def require_file(path: Path, label: str) -> Path:
    resolved = path.resolve()
    if not resolved.is_file():
        raise FileNotFoundError(f"{label} not found: {resolved}")
    return resolved


def main() -> int:
    args = parse_args()
    try:
        video = require_file(args.video, "Silent video")
        audio = require_file(args.audio, "Soundtrack")
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()

    command = [
        ffmpeg,
        "-y",
        "-i", str(video),
        "-i", str(audio),
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "192k",
        "-ar", "48000",
        "-ac", "2",
        "-t", "21.0",
        "-movflags", "+faststart",
        str(output),
    ]

    print(f"Video:  {video}")
    print(f"Audio:  {audio}")
    print(f"Output: {output}")
    print("Combining without re-encoding the video stream...")

    completed = subprocess.run(command, check=False)
    if completed.returncode != 0:
        print(f"ERROR: ffmpeg exited with code {completed.returncode}", file=sys.stderr)
        return completed.returncode

    if not output.is_file() or output.stat().st_size == 0:
        print("ERROR: The output MP4 was not created.", file=sys.stderr)
        return 1

    print(f"Wrote: {output}")
    print(f"Size: {output.stat().st_size:,} bytes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
