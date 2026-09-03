#!/usr/bin/env python3
"""Build the Section 11 silent Shorts storyboard.

Run from the MEMORIOPOLIS repository root:
    python scripts/build_section11_shorts_storyboard.py

Requires:
    Pillow
    ffmpeg available on PATH
"""
from __future__ import annotations

import math
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SECTION = ROOT / "experience" / "chapter04" / "section11"
IMAGES = SECTION / "assets" / "images"
TRAILER = SECTION / "trailer"
PREVIEW_DIR = TRAILER / "previews"
OUTPUT_DIR = TRAILER / "output"
FRAME_DIR = Path(tempfile.gettempdir()) / "memoriopolis_section11_frames"

WIDTH, HEIGHT = 1080, 1920
FPS = 30
DURATION = 20.5
TOTAL_FRAMES = round(FPS * DURATION)

# UI-safe region. Important text stays left of platform controls and above captions.
SAFE_LEFT = 92
SAFE_RIGHT = 880
SAFE_TOP = 190
SAFE_BOTTOM = 1530

@dataclass(frozen=True)
class Shot:
    start: float
    end: float
    image: str | None
    focus_x: float = 0.5
    focus_y: float = 0.5
    start_scale: float = 1.00
    end_scale: float = 1.015
    darkness: float = 0.22
    text: tuple[tuple[float, str, str], ...] = ()
    aki: bool = False

SHOTS = (
    Shot(0.0, 1.2, None, darkness=0.0),
    Shot(1.2, 4.2, "scene01_same_sender_1.png", 0.51, 0.46, 1.00, 1.015, .24,
         ((1.45, "同じ名前。", "large"), (2.25, "同じ言葉。", "large"))),
    Shot(4.2, 7.0, "scene02_old_application_2.png", 0.50, 0.57, 1.00, 1.012, .22,
         ((4.55, "けれど、", "medium"), (5.10, "通ってきた道は違う。", "large"))),
    Shot(7.0, 10.4, "scene02_old_application_1.png", 0.44, 0.62, 1.00, 1.010, .26,
         ((7.35, "記録はある。", "medium"), (8.35, "でも、説明がつながらない。", "large"))),
    Shot(10.4, 13.3, "scene03_inherited_system.png", 0.50, 0.61, 1.00, 1.008, .18,
         ((11.45, "A. K. I.", "aki"),), aki=True),
    Shot(13.3, 18.4, "scene06_two_forms_of_trust.png", 0.50, 0.55, 1.00, 1.018, .29,
         ((13.65, "正しい通知なのに、", "large"),
          (14.50, "正しいと証明できない。", "large"),
          (16.80, "同じ信じ方でよいのでしょうか。", "medium"))),
    Shot(18.4, 20.5, None, darkness=0.0, text=
         ((18.55, "記憶都市\n（メモリオポリス）", "title"),
          (19.05, "第四章 第十一節\n「説明の継ぎ目」", "medium"),
          (19.60, "本編は\n「記憶都市・中央駅」から。", "small"))),
)
FONT_CANDIDATES = (
    Path("C:/Windows/Fonts/BIZ-UDMinchoM.ttc"),
    Path("C:/Windows/Fonts/YuMincho.ttc"),
    Path("C:/Windows/Fonts/YuMincho.ttf"),
    Path("C:/Windows/Fonts/meiryo.ttc"),
    Path("/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"),
    Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"),
)
SERIF_CANDIDATES = (
    Path("C:/Windows/Fonts/georgia.ttf"),
    Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"),
)

def choose_font(candidates: Iterable[Path], size: int):
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


FONTS = {
    "small": choose_font(FONT_CANDIDATES, 40),
    "medium": choose_font(FONT_CANDIDATES, 52),
    "large": choose_font(FONT_CANDIDATES, 66),
    "title": choose_font(FONT_CANDIDATES, 50),
    "aki": choose_font(SERIF_CANDIDATES, 66),
}

def ease(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


def cover_crop(img: Image.Image, focus_x: float, focus_y: float, scale: float) -> Image.Image:
    source_ratio = img.width / img.height
    target_ratio = WIDTH / HEIGHT
    if source_ratio > target_ratio:
        crop_h = img.height / scale
        crop_w = crop_h * target_ratio
    else:
        crop_w = img.width / scale
        crop_h = crop_w / target_ratio
    cx, cy = img.width * focus_x, img.height * focus_y
    left = max(0, min(img.width - crop_w, cx - crop_w / 2))
    top = max(0, min(img.height - crop_h, cy - crop_h / 2))
    box = (round(left), round(top), round(left + crop_w), round(top + crop_h))
    return img.crop(box).resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)


def base_card() -> Image.Image:
    img = Image.new("RGB", (WIDTH, HEIGHT), "#02070b")
    draw = ImageDraw.Draw(img)
    y = round(HEIGHT * .53)
    draw.line((86, y, WIDTH - 86, y), fill=(126, 199, 205), width=2)
    draw.line((86, y + 15, WIDTH - 280, y + 15), fill=(194, 181, 137), width=1)
    return img


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font, max_width: int):
    lines, current = [], ""
    for ch in text:
        trial = current + ch
        if draw.textbbox((0, 0), trial, font=font)[2] <= max_width or not current:
            current = trial
        else:
            lines.append(current)
            current = ch
    if current:
        lines.append(current)
    return lines


def draw_text_layer(img: Image.Image, shot: Shot, time_s: float):
    draw = ImageDraw.Draw(img, "RGBA")
    visible = [(at, text, style) for at, text, style in shot.text if time_s >= at]
    if not visible:
        return
    y = SAFE_TOP + 100
    if shot.start >= 13.3 and shot.end <= 18.4:
        y = SAFE_TOP + 160
    if shot.start >= 18.4:
        y = 610
    for at, text, style in visible:
        age = min(1.0, max(0.0, (time_s - at) / .35))
        alpha = round(255 * ease(age))
        font = FONTS[style]
        max_w = SAFE_RIGHT - SAFE_LEFT
        lines = wrap_text(draw, text, font, max_w)
        line_h = font.size * 1.55 if hasattr(font, "size") else 60
        box_h = round(line_h * len(lines) + 34)
        draw.rounded_rectangle((SAFE_LEFT - 18, y - 12, SAFE_RIGHT + 18, y + box_h), radius=12,
                               fill=(2, 8, 12, round(160 * age)), outline=(151, 222, 226, round(55 * age)), width=1)
        for line in lines:
            draw.text((SAFE_LEFT, y), line, font=font, fill=(239, 243, 239, alpha),
                      stroke_width=1, stroke_fill=(0, 0, 0, round(170 * age)))
            y += round(line_h)
        if shot.start >= 18.4:
            y += 52
        else:
            y += 34


def render_frame(time_s: float, sources: dict[str, Image.Image]) -> Image.Image:
    shot = next(s for s in SHOTS if s.start <= time_s < s.end or (time_s == DURATION and s.end == DURATION))
    if shot.image is None:
        frame = base_card()
    else:
        local_t = (time_s - shot.start) / max(.001, shot.end - shot.start)
        scale = shot.start_scale + (shot.end_scale - shot.start_scale) * ease(local_t)
        frame = cover_crop(sources[shot.image], shot.focus_x, shot.focus_y, scale)
        frame = ImageEnhance.Color(frame).enhance(.84)
        frame = ImageEnhance.Contrast(frame).enhance(1.04)
        overlay = Image.new("RGBA", frame.size, (0, 5, 9, round(255 * shot.darkness)))
        frame = Image.alpha_composite(frame.convert("RGBA"), overlay).convert("RGB")
    # Very short crossfade from the prior shot.
    transition = .42
    if shot.start > 0 and time_s - shot.start < transition:
        prev = SHOTS[SHOTS.index(shot) - 1]
        if prev.image is None:
            prior = base_card()
        else:
            prior = cover_crop(sources[prev.image], prev.focus_x, prev.focus_y, prev.end_scale)
            prior = ImageEnhance.Color(prior).enhance(.84)
        blend = ease((time_s - shot.start) / transition)
        frame = Image.blend(prior.convert("RGB"), frame.convert("RGB"), blend)
    draw_text_layer(frame, shot, time_s)
    return frame


def check_sources():
    required = sorted({s.image for s in SHOTS if s.image})
    missing = [name for name in required if not (IMAGES / name).exists()]
    if missing:
        raise SystemExit("Missing source images:\n  " + "\n  ".join(missing))
    return required


def build_previews(sources):
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    preview_times = (1.8, 5.5, 8.8, 11.8, 15.2, 17.4, 19.5)
    for index, time_s in enumerate(preview_times, 1):
        render_frame(time_s, sources).save(PREVIEW_DIR / f"shot_{index:02d}_{time_s:04.1f}s.png")


def build_video(sources):
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        try:
            import imageio_ffmpeg
            ffmpeg = imageio_ffmpeg.get_ffmpeg_exe()
        except ImportError:
            raise SystemExit(
                "ffmpeg was not found on PATH, and imageio_ffmpeg is not installed. "
                "Previews were still generated."
            )
    if FRAME_DIR.exists():
        shutil.rmtree(FRAME_DIR)
    FRAME_DIR.mkdir(parents=True)
    for frame_no in range(TOTAL_FRAMES):
        time_s = frame_no / FPS
        render_frame(time_s, sources).save(FRAME_DIR / f"frame_{frame_no:05d}.jpg", quality=92, subsampling=0)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output = OUTPUT_DIR / "section11_trailer_ja_storyboard.mp4"
    command = [ffmpeg, "-y", "-framerate", str(FPS), "-i", str(FRAME_DIR / "frame_%05d.jpg"),
               "-c:v", "libx264", "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-r", str(FPS), str(output)]
    subprocess.run(command, check=True)
    shutil.rmtree(FRAME_DIR)
    return output


def main():
    required = check_sources()
    sources = {name: Image.open(IMAGES / name).convert("RGB") for name in required}
    build_previews(sources)
    output = build_video(sources)
    print(f"[OK] previews: {PREVIEW_DIR}")
    print(f"[OK] video: {output}")

if __name__ == "__main__":
    main()
