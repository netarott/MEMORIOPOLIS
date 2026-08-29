#!/usr/bin/env python3
"""Build the silent vertical trailer for MEMORIOPOLIS section 10.

Expected layout:

trailer/
    build_trailer.py
    storyboard.md
    assets/
        01_operations_bureau.png
        02_artificial_hand.png
        03_boundary_line.png
        04_unnamed_space.png
        05_four_reflections.png
        06_title_background.png
    output/

Install dependencies:
    py -m pip install "moviepy>=2,<3" pillow numpy imageio-ffmpeg

Run from any directory:
    py novel/chapter04/section10/trailer/build_trailer.py
"""

from __future__ import annotations

import argparse
import math
import os
import sys
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Sequence

import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

try:
    from moviepy import VideoClip
except ImportError as exc:
    raise SystemExit(
        "MoviePy is not installed. Run:\n"
        '  py -m pip install "moviepy>=2,<3" pillow numpy imageio-ffmpeg'
    ) from exc


# ---------------------------------------------------------------------------
# Output specification
# ---------------------------------------------------------------------------

WIDTH = 1080
HEIGHT = 1920
FPS = 30
DURATION = 21.0
BACKGROUND = (2, 8, 13)
TEXT_COLOR = (232, 238, 240, 255)
ACCENT_COLOR = (159, 232, 238, 255)
OUTLINE_COLOR = (2, 8, 13, 235)

BASE_DIR = Path(__file__).resolve().parent
ASSET_DIR = BASE_DIR / "assets"
OUTPUT_DIR = BASE_DIR / "output"
DEFAULT_OUTPUT = OUTPUT_DIR / "section10_trailer_silent_prototype01.mp4"

ASSET_NAMES = (
    "01_operations_bureau.png",
    "02_artificial_hand.png",
    "03_boundary_line.png",
    "04_unnamed_space.png",
    "05_four_reflections.png",
    "06_title_background.png",
)


@dataclass(frozen=True)
class Shot:
    start: float
    end: float
    asset_name: str
    zoom_start: float
    zoom_end: float
    darken: float = 1.0
    focus_x: float = 0.5
    focus_y: float = 0.5

    @property
    def duration(self) -> float:
        return self.end - self.start


SHOTS = (
    Shot(0.0, 3.0, ASSET_NAMES[0], 1.00, 1.05, 0.78, 0.50, 0.48),
    Shot(3.0, 7.0, ASSET_NAMES[1], 1.00, 1.07, 0.90, 0.55, 0.53),
    Shot(7.0, 11.0, ASSET_NAMES[2], 1.00, 1.035, 0.88, 0.50, 0.50),
    Shot(11.0, 15.0, ASSET_NAMES[3], 1.00, 1.06, 0.88, 0.57, 0.51),
    Shot(15.0, 18.0, ASSET_NAMES[4], 1.00, 1.05, 0.88, 0.50, 0.50),
    Shot(18.0, 21.0, ASSET_NAMES[5], 1.00, 1.025, 0.72, 0.50, 0.50),
)

# Fade duration used at the start of each shot except the first.
CROSSFADE = {
    1: 0.25,
    2: 0.25,
    3: 0.40,
    4: 0.25,
    5: 0.35,
}


# ---------------------------------------------------------------------------
# Font selection
# ---------------------------------------------------------------------------

FONT_CANDIDATES = {
    "cjk": (
        "C:/Windows/Fonts/NotoSansCJK-Regular.ttc",
        "C:/Windows/Fonts/NotoSansJP-Regular.otf",
        "C:/Windows/Fonts/meiryo.ttc",
        "C:/Windows/Fonts/YuGothR.ttc",
        "C:/Windows/Fonts/msgothic.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
        "/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc",
    ),
    "korean": (
        "C:/Windows/Fonts/NotoSansCJK-Regular.ttc",
        "C:/Windows/Fonts/malgun.ttf",
        "C:/Windows/Fonts/malgunbd.ttf",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/System/Library/Fonts/AppleSDGothicNeo.ttc",
    ),
    "latin": (
        "C:/Windows/Fonts/NotoSans-Regular.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeui.ttf",
        "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf",
    ),
}


def _candidate_paths(kind: str) -> Sequence[Path]:
    env_font = os.environ.get("MEMORIOPOLIS_FONT")
    paths: list[Path] = []
    if env_font:
        paths.append(Path(env_font))
    paths.extend(Path(item) for item in FONT_CANDIDATES[kind])
    return paths


@lru_cache(maxsize=None)
def font_path(kind: str) -> Path:
    for path in _candidate_paths(kind):
        if path.is_file():
            return path
    raise FileNotFoundError(
        f"No suitable {kind} font was found. "
        "Install Noto Sans CJK or set MEMORIOPOLIS_FONT to a font file path."
    )


@lru_cache(maxsize=64)
def get_font(kind: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(font_path(kind)), size=size)


# ---------------------------------------------------------------------------
# Image preparation and camera movement
# ---------------------------------------------------------------------------


def smoothstep(value: float) -> float:
    value = min(1.0, max(0.0, value))
    return value * value * (3.0 - 2.0 * value)


def fade_window(t: float, start: float, fade_in: float, end: float, fade_out: float) -> float:
    if t < start or t >= end:
        return 0.0
    alpha = 1.0
    if fade_in > 0 and t < start + fade_in:
        alpha *= smoothstep((t - start) / fade_in)
    if fade_out > 0 and t > end - fade_out:
        alpha *= smoothstep((end - t) / fade_out)
    return min(1.0, max(0.0, alpha))


@lru_cache(maxsize=12)
def load_asset(asset_name: str) -> Image.Image:
    path = ASSET_DIR / asset_name
    if not path.is_file():
        raise FileNotFoundError(f"Missing asset: {path}")
    return Image.open(path).convert("RGB")


def cover_crop(image: Image.Image, scale: float, focus_x: float, focus_y: float) -> Image.Image:
    source_w, source_h = image.size
    base_scale = max(WIDTH / source_w, HEIGHT / source_h)
    final_scale = base_scale * scale
    resized_w = max(WIDTH, int(round(source_w * final_scale)))
    resized_h = max(HEIGHT, int(round(source_h * final_scale)))
    resized = image.resize((resized_w, resized_h), Image.Resampling.LANCZOS)

    overflow_x = resized_w - WIDTH
    overflow_y = resized_h - HEIGHT
    left = int(round(overflow_x * min(1.0, max(0.0, focus_x))))
    top = int(round(overflow_y * min(1.0, max(0.0, focus_y))))
    left = min(max(left, 0), overflow_x)
    top = min(max(top, 0), overflow_y)
    return resized.crop((left, top, left + WIDTH, top + HEIGHT))


def shot_frame(shot_index: int, global_t: float) -> Image.Image:
    shot = SHOTS[shot_index]
    local_t = min(shot.duration, max(0.0, global_t - shot.start))
    progress = smoothstep(local_t / shot.duration)
    zoom = shot.zoom_start + (shot.zoom_end - shot.zoom_start) * progress
    frame = cover_crop(load_asset(shot.asset_name), zoom, shot.focus_x, shot.focus_y)
    if shot.darken != 1.0:
        frame = ImageEnhance.Brightness(frame).enhance(shot.darken)
    return frame


def current_shot_index(t: float) -> int:
    for index, shot in enumerate(SHOTS):
        if shot.start <= t < shot.end:
            return index
    return len(SHOTS) - 1


def base_frame(t: float) -> Image.Image:
    index = current_shot_index(t)
    frame = shot_frame(index, t)

    if index > 0:
        fade_duration = CROSSFADE[index]
        local_t = t - SHOTS[index].start
        if 0.0 <= local_t < fade_duration:
            previous = shot_frame(index - 1, t)
            alpha = smoothstep(local_t / fade_duration)
            frame = Image.blend(previous, frame, alpha)

    return frame


# ---------------------------------------------------------------------------
# Subtitle rendering
# ---------------------------------------------------------------------------


def text_bbox(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, stroke_width: int) -> tuple[int, int, int, int]:
    return draw.textbbox((0, 0), text, font=font, stroke_width=stroke_width)


def draw_text(
    canvas: Image.Image,
    text: str,
    xy: tuple[int, int],
    *,
    kind: str = "cjk",
    size: int = 60,
    color: tuple[int, int, int, int] = TEXT_COLOR,
    anchor: str = "mm",
    align: str = "center",
    stroke_width: int = 3,
    alpha: float = 1.0,
    shadow: bool = True,
) -> None:
    if alpha <= 0:
        return

    overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    font = get_font(kind, size)
    final_color = color[:3] + (int(color[3] * alpha),)
    final_outline = OUTLINE_COLOR[:3] + (int(OUTLINE_COLOR[3] * alpha),)

    if shadow:
        draw.multiline_text(
            (xy[0] + 3, xy[1] + 4),
            text,
            font=font,
            fill=(0, 0, 0, int(150 * alpha)),
            anchor=anchor,
            align=align,
            spacing=int(size * 0.24),
            stroke_width=stroke_width + 1,
            stroke_fill=(0, 0, 0, int(120 * alpha)),
        )

    draw.multiline_text(
        xy,
        text,
        font=font,
        fill=final_color,
        anchor=anchor,
        align=align,
        spacing=int(size * 0.24),
        stroke_width=stroke_width,
        stroke_fill=final_outline,
    )
    canvas.alpha_composite(overlay)


def draw_caption_block(
    canvas: Image.Image,
    t: float,
    lines: Sequence[tuple[str, float]],
    *,
    end: float,
    x: int,
    first_y: int,
    line_gap: int,
    size: int,
    align: str = "center",
    anchor: str = "mm",
) -> None:
    for index, (text, start) in enumerate(lines):
        alpha = fade_window(t, start, 0.22, end, 0.20)
        draw_text(
            canvas,
            text,
            (x, first_y + index * line_gap),
            size=size,
            alpha=alpha,
            align=align,
            anchor=anchor,
        )


def render_subtitles(frame: Image.Image, t: float) -> Image.Image:
    canvas = frame.convert("RGBA")

    # Cut 1: sequential lines.
    draw_caption_block(
        canvas,
        t,
        (
            ("いつもの名前。", 0.25),
            ("いつもの言葉。", 1.05),
            ("いつもの朝。", 1.85),
        ),
        end=2.95,
        x=WIDTH // 2,
        first_y=1195,
        line_gap=92,
        size=62,
    )

    # Cut 2: the young artificial intelligence's question.
    alpha = fade_window(t, 3.55, 0.28, 6.82, 0.25)
    draw_text(
        canvas,
        "これが本人のメッセージだという\n根拠は？",
        (WIDTH // 2, 1450),
        size=56,
        alpha=alpha,
    )

    # Cut 3: equal weight on both concepts.
    alpha_left = fade_window(t, 7.35, 0.24, 10.80, 0.22)
    alpha_right = fade_window(t, 8.45, 0.24, 10.80, 0.22)
    draw_text(canvas, "疑うこと。", (280, 980), size=68, alpha=alpha_left)
    draw_text(canvas, "確かめること。", (795, 980), size=68, alpha=alpha_right)

    # Cut 4: two-line thought, positioned away from the face and hand.
    alpha_line1 = fade_window(t, 11.45, 0.24, 14.82, 0.22)
    alpha_line2 = fade_window(t, 12.75, 0.24, 14.82, 0.22)
    draw_text(canvas, "二つの答えのあいだに、", (WIDTH // 2, 1435), size=52, alpha=alpha_line1)
    draw_text(canvas, "まだ名前のない空間ができた。", (WIDTH // 2, 1525), size=52, alpha=alpha_line2)

    # Cut 5: four reflections, equal duration and visual weight.
    reflections = (
        ("To verify.", 15.00, "latin"),
        ("不急著決定。", 15.70, "cjk"),
        ("확인할 수 있는지", 16.40, "korean"),
        ("как мы доверяем", 17.10, "latin"),
    )
    for text, start, kind in reflections:
        alpha = fade_window(t, start, 0.16, min(18.0, start + 0.90), 0.18)
        draw_text(canvas, text, (WIDTH // 2, 1425), kind=kind, size=54, color=ACCENT_COLOR, alpha=alpha)

    # Cut 6: title elements appear sequentially and remain together.
    title_alpha = fade_window(t, 18.00, 0.28, 20.68, 0.15)
    chapter_alpha = fade_window(t, 18.65, 0.28, 20.68, 0.15)
    section_alpha = fade_window(t, 19.25, 0.28, 20.68, 0.15)
    draw_text(canvas, "記憶都市（メモリオポリス）", (WIDTH // 2, 760), size=66, alpha=title_alpha)
    draw_text(canvas, "第四章　第十節", (WIDTH // 2, 900), size=48, color=ACCENT_COLOR, alpha=chapter_alpha)
    draw_text(canvas, "「二つの信頼」", (WIDTH // 2, 1035), size=72, alpha=section_alpha)

    # Final fade to black.
    if t >= 20.65:
        black_alpha = smoothstep((t - 20.65) / 0.35)
        black = Image.new("RGBA", canvas.size, (0, 0, 0, int(255 * black_alpha)))
        canvas.alpha_composite(black)

    return canvas.convert("RGB")


# ---------------------------------------------------------------------------
# Validation and build
# ---------------------------------------------------------------------------


def validate_assets() -> None:
    missing = [str(ASSET_DIR / name) for name in ASSET_NAMES if not (ASSET_DIR / name).is_file()]
    if missing:
        raise FileNotFoundError("Missing trailer assets:\n  " + "\n  ".join(missing))

    for name in ASSET_NAMES:
        path = ASSET_DIR / name
        with Image.open(path) as image:
            if image.width < 720 or image.height < 1280:
                raise ValueError(f"Asset is too small for vertical video: {path} ({image.size})")
            if image.height <= image.width:
                raise ValueError(f"Asset is not portrait-oriented: {path} ({image.size})")


def validate_fonts() -> None:
    required = ("cjk", "korean", "latin")
    selected = {kind: font_path(kind) for kind in required}
    print("Fonts:")
    for kind, path in selected.items():
        print(f"  {kind:7s} {path}")


def make_frame(t: float) -> np.ndarray:
    frame = base_frame(float(t))
    composed = render_subtitles(frame, float(t))
    return np.asarray(composed, dtype=np.uint8)


def build(output_path: Path, preview_only: bool = False) -> None:
    validate_assets()
    validate_fonts()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if preview_only:
        preview_dir = OUTPUT_DIR / "preview_frames"
        preview_dir.mkdir(parents=True, exist_ok=True)
        moments = (0.5, 2.4, 4.8, 8.9, 13.4, 16.7, 19.8)
        for moment in moments:
            image = Image.fromarray(make_frame(moment))
            target = preview_dir / f"frame_{moment:05.2f}s.png"
            image.save(target)
            print(f"Wrote {target}")
        return

    output_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"Building {output_path}")
    print(f"Specification: {WIDTH}x{HEIGHT}, {FPS} fps, {DURATION:.1f} seconds, silent")

    clip = VideoClip(frame_function=make_frame, duration=DURATION)
    try:
        clip.write_videofile(
            str(output_path),
            fps=FPS,
            codec="libx264",
            audio=False,
            pixel_format="yuv420p",
            preset="medium",
            threads=max(1, min(8, os.cpu_count() or 1)),
            logger="bar",
        )
    finally:
        clip.close()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the silent MEMORIOPOLIS section 10 trailer.")
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output MP4 path. Default: {DEFAULT_OUTPUT}",
    )
    parser.add_argument(
        "--preview-frames",
        action="store_true",
        help="Render representative PNG frames instead of the full MP4.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        build(args.output.resolve(), preview_only=args.preview_frames)
    except (FileNotFoundError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
