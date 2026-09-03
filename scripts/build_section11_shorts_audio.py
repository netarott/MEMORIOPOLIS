#!/usr/bin/env python3
"""Build the Section 11 music-attached Shorts FIX candidate.

Run from the MEMORIOPOLIS repository root:
    python scripts/build_section11_shorts_audio.py

Input:
    experience/chapter04/section11/trailer/output/
        section11_trailer_ja_storyboard.mp4

Outputs:
    experience/chapter04/section11/trailer/output/
        section11_trailer_ja_soundscape.wav
        section11_trailer_ja_fix_candidate.mp4

The soundscape is original and generated entirely in code.
"""
from __future__ import annotations

import math
import random
import shutil
import subprocess
import wave
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SECTION = ROOT / "experience" / "chapter04" / "section11"
TRAILER = SECTION / "trailer"
OUTPUT_DIR = TRAILER / "output"
INPUT_VIDEO = OUTPUT_DIR / "section11_trailer_ja_storyboard.mp4"
OUTPUT_WAV = OUTPUT_DIR / "section11_trailer_ja_soundscape.wav"
OUTPUT_VIDEO = OUTPUT_DIR / "section11_trailer_ja_fix_candidate.mp4"

SAMPLE_RATE = 48_000
DURATION = 20.5
CHANNELS = 2
SAMPLES = round(SAMPLE_RATE * DURATION)
MASTER_PEAK = 0.84
SEED = 1104


def seconds(value: float) -> int:
    return round(value * SAMPLE_RATE)


def smoothstep(x: np.ndarray) -> np.ndarray:
    x = np.clip(x, 0.0, 1.0)
    return x * x * (3.0 - 2.0 * x)


def envelope(length: int, attack: float, release: float) -> np.ndarray:
    result = np.ones(length, dtype=np.float64)
    a = min(length, max(1, seconds(attack)))
    r = min(length, max(1, seconds(release)))
    result[:a] *= smoothstep(np.linspace(0.0, 1.0, a, endpoint=False))
    result[-r:] *= smoothstep(np.linspace(1.0, 0.0, r, endpoint=False))
    return result


def equal_power_pan(signal: np.ndarray, pan: float) -> np.ndarray:
    pan = float(np.clip(pan, -1.0, 1.0))
    angle = (pan + 1.0) * math.pi / 4.0
    return np.column_stack((signal * math.cos(angle), signal * math.sin(angle)))


def add(track: np.ndarray, signal: np.ndarray, start: float, gain: float = 1.0,
        pan: float = 0.0) -> None:
    begin = seconds(start)
    if signal.ndim == 1:
        signal = equal_power_pan(signal, pan)
    end = min(len(track), begin + len(signal))
    if end > begin:
        track[begin:end] += signal[:end - begin] * gain


def lowpass_noise(duration: float, cutoff_hz: float, rng: np.random.Generator) -> np.ndarray:
    n = seconds(duration)
    noise = rng.normal(0.0, 1.0, n)
    # One-pole low-pass filter. Stable and dependency-free beyond NumPy.
    alpha = 1.0 - math.exp(-2.0 * math.pi * cutoff_hz / SAMPLE_RATE)
    out = np.empty(n, dtype=np.float64)
    state = 0.0
    for index, value in enumerate(noise):
        state += alpha * (value - state)
        out[index] = state
    peak = np.max(np.abs(out)) or 1.0
    return out / peak


def wind_layer(rng: np.random.Generator) -> np.ndarray:
    """A locationless field, present almost everywhere but never foregrounded."""
    noise = lowpass_noise(DURATION, 820.0, rng)
    t = np.arange(SAMPLES) / SAMPLE_RATE
    breath = 0.55 + 0.18 * np.sin(2 * math.pi * 0.071 * t + 0.6)
    breath += 0.10 * np.sin(2 * math.pi * 0.113 * t + 2.2)
    high_air = rng.normal(0.0, 1.0, SAMPLES) * 0.025
    mono = (noise * breath + high_air) * envelope(SAMPLES, 1.3, 1.6)
    # Slightly different movement on each side. The field has no fixed source.
    left = mono * (0.91 + 0.05 * np.sin(2 * math.pi * 0.047 * t))
    right = mono * (0.89 + 0.06 * np.sin(2 * math.pi * 0.053 * t + 1.3))
    return np.column_stack((left, right))


def ambient_bed(rng: np.random.Generator) -> np.ndarray:
    """Two unsynchronised institutional time layers, without a resolved chord."""
    t = np.arange(SAMPLES) / SAMPLE_RATE
    fundamental_a = 55.0
    fundamental_b = 55.0 * 2 ** (7 / 1200)  # Seven cents apart, almost the same.
    a = np.sin(2 * math.pi * fundamental_a * t) * 0.55
    a += np.sin(2 * math.pi * fundamental_a * 2.01 * t + 0.5) * 0.19
    b = np.sin(2 * math.pi * fundamental_b * t + 1.1) * 0.48
    b += np.sin(2 * math.pi * fundamental_b * 1.997 * t + 1.8) * 0.16
    movement_a = 0.52 + 0.12 * np.sin(2 * math.pi * 0.083 * t)
    movement_b = 0.47 + 0.13 * np.sin(2 * math.pi * 0.067 * t + 1.4)
    bed = np.column_stack((a * movement_a + b * 0.34, b * movement_b + a * 0.31))
    return bed * envelope(SAMPLES, 1.8, 2.0)[:, None]


def soft_tone(freq: float, duration: float, overtone: float = 0.18) -> np.ndarray:
    n = seconds(duration)
    t = np.arange(n) / SAMPLE_RATE
    signal = np.sin(2 * math.pi * freq * t)
    signal += overtone * np.sin(2 * math.pi * freq * 2.01 * t + 0.3)
    signal += 0.07 * np.sin(2 * math.pi * freq * 3.02 * t + 0.8)
    return signal * envelope(n, 0.008, duration * 0.72)


def notification_a() -> np.ndarray:
    """Dry two-note arrival. Familiar, ordinary, neither warning nor success."""
    length = seconds(0.58)
    result = np.zeros((length, 2), dtype=np.float64)
    add(result, soft_tone(659.25, 0.17, 0.14), 0.00, 0.74, -0.05)
    add(result, soft_tone(783.99, 0.19, 0.12), 0.21, 0.66, 0.04)
    return result


def silver_tail(freq: float = 1174.66) -> np.ndarray:
    """A short silver-white tail, audible as a different route rather than a reward."""
    duration = 0.58
    n = seconds(duration)
    t = np.arange(n) / SAMPLE_RATE
    signal = np.sin(2 * math.pi * freq * t + 0.2)
    signal += 0.31 * np.sin(2 * math.pi * freq * 1.502 * t + 1.1)
    signal += 0.14 * np.sin(2 * math.pi * freq * 2.006 * t + 0.4)
    shimmer = 0.74 + 0.26 * np.sin(2 * math.pi * 7.4 * t)
    decay = np.exp(-6.4 * t)
    return signal * shimmer * decay * envelope(n, 0.012, 0.24)


def notification_b() -> np.ndarray:
    """Almost the same two notes, followed by a brief silver-white trace."""
    length = seconds(0.92)
    result = np.zeros((length, 2), dtype=np.float64)
    add(result, soft_tone(659.25, 0.17, 0.14), 0.00, 0.70, -0.04)
    add(result, soft_tone(783.99, 0.19, 0.12), 0.21, 0.63, 0.03)
    add(result, silver_tail(), 0.38, 0.26, 0.16)
    return result


def application_scroll(rng: np.random.Generator) -> np.ndarray:
    duration = 1.9
    n = seconds(duration)
    t = np.arange(n) / SAMPLE_RATE
    texture = lowpass_noise(duration, 1600.0, rng) * 0.15
    pulses = np.zeros(n)
    for when, level in ((0.08, .48), (.49, .34), (1.03, .31), (1.57, .23)):
        start = seconds(when)
        length = min(seconds(.075), n - start)
        if length > 0:
            click_t = np.arange(length) / SAMPLE_RATE
            pulses[start:start + length] += np.sin(2 * math.pi * 310 * click_t) * np.exp(-46 * click_t) * level
    return (texture + pulses) * envelope(n, .06, .35)


def subway_strata(rng: np.random.Generator) -> np.ndarray:
    """The memory of a train below the city, never explicit enough to become a scene."""
    duration = 6.1
    n = seconds(duration)
    t = np.arange(n) / SAMPLE_RATE
    approach = smoothstep(t / 2.4) * smoothstep((duration - t) / 2.1)
    rumble = lowpass_noise(duration, 95.0, rng) * 0.72
    rumble += np.sin(2 * math.pi * (31.0 + 0.35 * np.sin(2 * math.pi * .09 * t)) * t) * 0.27
    air = lowpass_noise(duration, 390.0, rng) * 0.12
    mono = (rumble + air) * approach
    stereo = equal_power_pan(mono, -0.12)
    # Irregular rail-joint memories, not a beat.
    for when, level, pan in ((1.05, .15, -.20), (1.79, .12, -.08), (2.66, .16, .02),
                             (3.58, .11, .08), (4.31, .13, .16)):
        n_click = seconds(.24)
        ct = np.arange(n_click) / SAMPLE_RATE
        click = (np.sin(2 * math.pi * 73 * ct) + .35 * np.sin(2 * math.pi * 146 * ct))
        click *= np.exp(-17 * ct)
        add(stereo, click, when, level, pan)
    return stereo


def droplet(freq: float, duration: float, decay: float, pan: float) -> np.ndarray:
    n = seconds(duration)
    t = np.arange(n) / SAMPLE_RATE
    body = np.sin(2 * math.pi * (freq + 22 * np.exp(-10 * t)) * t)
    body += .28 * np.sin(2 * math.pi * freq * 2.18 * t + .5)
    body *= np.exp(-decay * t)
    # A small diffuse ripple, intentionally not a realistic water Foley sample.
    ripple = np.sin(2 * math.pi * 4.7 * t) * np.exp(-4.8 * t) * .10
    return equal_power_pan((body + ripple) * envelope(n, .004, duration * .45), pan)


def apply_identity_silence(track: np.ndarray) -> None:
    """A short seam before the hand stops. Never a hard digital mute."""
    start, lowest, end = seconds(16.46), seconds(16.62), seconds(16.84)
    fade_out = np.linspace(1.0, 0.06, lowest - start, endpoint=False)
    valley = np.full(end - lowest, 0.06)
    track[start:lowest] *= fade_out[:, None]
    track[lowest:end] *= valley[:, None]
    recovery_end = min(len(track), end + seconds(.34))
    recovery = np.linspace(0.06, 1.0, recovery_end - end)
    track[end:recovery_end] *= recovery[:, None]


def high_frequency_soften(track: np.ndarray, start_s: float, end_s: float) -> None:
    """The old-strata interval loses some high-frequency detail."""
    start, end = seconds(start_s), seconds(end_s)
    segment = track[start:end].copy()
    alpha = 1.0 - math.exp(-2.0 * math.pi * 1450.0 / SAMPLE_RATE)
    state = np.zeros(2)
    for i in range(len(segment)):
        state += alpha * (segment[i] - state)
        segment[i] = state
    track[start:end] = segment


def soft_limit(track: np.ndarray) -> np.ndarray:
    track = np.tanh(track * 1.12)
    peak = np.max(np.abs(track)) or 1.0
    return track * (MASTER_PEAK / peak)


def build_soundscape() -> np.ndarray:
    rng = np.random.default_rng(SEED)
    track = np.zeros((SAMPLES, CHANNELS), dtype=np.float64)

    # Field and two institutional time layers.
    track += wind_layer(rng) * 0.035
    track += ambient_bed(rng) * 0.030

    # Two arrivals. B shares the grammar of A but carries a separate route-tail.
    add(track, notification_a(), 1.35, 0.34)
    add(track, notification_b(), 4.40, 0.34)

    # Work-body and old strata.
    add(track, application_scroll(rng), 7.18, 0.15, -0.08)
    add(track, subway_strata(rng), 8.55, 0.105)

    # Two droplets: recognisably related, never sample-identical.
    add(track, droplet(918.0, 1.05, 5.8, -0.16), 10.92, 0.13)
    add(track, droplet(889.0, 1.14, 5.15, 0.11), 16.36, 0.12)

    high_frequency_soften(track, 10.35, 13.45)
    apply_identity_silence(track)

    # The route continues beyond the title card. No resolving cadence.
    tail = soft_tone(110.7, 2.1, 0.08)
    add(track, tail, 18.35, 0.035, 0.10)
    return soft_limit(track)


def write_wav(track: np.ndarray, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    pcm = np.clip(track, -1.0, 1.0)
    pcm = (pcm * 32767.0).astype('<i2')
    with wave.open(str(destination), 'wb') as wav:
        wav.setnchannels(CHANNELS)
        wav.setsampwidth(2)
        wav.setframerate(SAMPLE_RATE)
        wav.writeframes(pcm.tobytes())


def find_ffmpeg() -> str:
    executable = shutil.which('ffmpeg')
    if executable:
        return executable
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError as error:
        raise SystemExit(
            'ffmpeg was not found on PATH, and imageio_ffmpeg is not installed.'
        ) from error


def mux(ffmpeg: str) -> None:
    if not INPUT_VIDEO.exists():
        raise SystemExit(f'Missing silent storyboard: {INPUT_VIDEO}')
    command = [
        ffmpeg, '-y',
        '-i', str(INPUT_VIDEO),
        '-i', str(OUTPUT_WAV),
        '-map', '0:v:0', '-map', '1:a:0',
        '-c:v', 'copy',
        '-c:a', 'aac', '-b:a', '192k',
        '-ar', str(SAMPLE_RATE),
        '-shortest',
        '-movflags', '+faststart',
        str(OUTPUT_VIDEO),
    ]
    subprocess.run(command, check=True)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    track = build_soundscape()
    write_wav(track, OUTPUT_WAV)
    ffmpeg = find_ffmpeg()
    mux(ffmpeg)
    print(f'[OK] soundscape: {OUTPUT_WAV}')
    print(f'[OK] FIX candidate: {OUTPUT_VIDEO}')
    print('[CHECK] Listen once on speakers and once on headphones.')
    print('[CHECK] Fix only clipped text, broken audio, missing notifications, or an unreadable CTA.')


if __name__ == '__main__':
    main()
