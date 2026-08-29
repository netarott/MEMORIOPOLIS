#!/usr/bin/env python3
"""Build the 21-second soundtrack prototype for the section 10 trailer.

The soundtrack follows storyboard.md:

00.0-03.0  Low operations-bureau ambience
03.0-07.0  Small notification tone and a thin stopping sound
07.0-11.0  Reduced ambience and a transparent boundary tone
11.0-15.0  Low resonance opening into an unnamed space
15.0-18.0  Four equal reflection tones
18.0-21.0  Convergence chord and final fade

No external audio assets are required. The output is a stereo 48 kHz WAV file.

Run from any directory:
    py novel/chapter04/section10/trailer/build_soundtrack.py

Optional:
    py novel/chapter04/section10/trailer/build_soundtrack.py --seed 10
    py novel/chapter04/section10/trailer/build_soundtrack.py --output path/to/file.wav
"""

from __future__ import annotations

import argparse
import math
import wave
from pathlib import Path

import numpy as np


SAMPLE_RATE = 48_000
DURATION = 21.0
CHANNELS = 2
DEFAULT_SEED = 10

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
DEFAULT_OUTPUT = OUTPUT_DIR / "section10_trailer_soundtrack_prototype01.wav"


# ---------------------------------------------------------------------------
# Basic signal helpers
# ---------------------------------------------------------------------------


def seconds_to_samples(seconds: float) -> int:
    return int(round(seconds * SAMPLE_RATE))


def time_axis(duration: float) -> np.ndarray:
    return np.arange(seconds_to_samples(duration), dtype=np.float64) / SAMPLE_RATE


def smoothstep01(x: np.ndarray) -> np.ndarray:
    x = np.clip(x, 0.0, 1.0)
    return x * x * (3.0 - 2.0 * x)


def envelope(
    duration: float,
    attack: float = 0.02,
    release: float = 0.15,
    sustain: float = 1.0,
) -> np.ndarray:
    """Return a smooth attack-sustain-release envelope."""
    t = time_axis(duration)
    env = np.full_like(t, sustain)
    if attack > 0:
        env *= smoothstep01(t / attack)
    if release > 0:
        env *= smoothstep01((duration - t) / release)
    return np.clip(env, 0.0, 1.0)


def equal_power_pan(mono: np.ndarray, pan: float) -> np.ndarray:
    """Pan mono audio to stereo. pan=-1 is left, +1 is right."""
    pan = float(np.clip(pan, -1.0, 1.0))
    angle = (pan + 1.0) * math.pi / 4.0
    left = mono * math.cos(angle)
    right = mono * math.sin(angle)
    return np.column_stack((left, right))


def add_at(master: np.ndarray, stereo: np.ndarray, start: float, gain: float = 1.0) -> None:
    start_sample = seconds_to_samples(start)
    if start_sample >= len(master):
        return
    end_sample = min(len(master), start_sample + len(stereo))
    usable = end_sample - start_sample
    if usable > 0:
        master[start_sample:end_sample] += stereo[:usable] * gain


def one_pole_lowpass(signal: np.ndarray, cutoff_hz: float) -> np.ndarray:
    """Simple low-pass filter implemented without SciPy."""
    cutoff_hz = max(1.0, float(cutoff_hz))
    alpha = 1.0 - math.exp(-2.0 * math.pi * cutoff_hz / SAMPLE_RATE)
    output = np.empty_like(signal)
    state = 0.0
    for index, value in enumerate(signal):
        state += alpha * (value - state)
        output[index] = state
    return output


def highpass_from_lowpass(signal: np.ndarray, cutoff_hz: float) -> np.ndarray:
    return signal - one_pole_lowpass(signal, cutoff_hz)


def soft_limit(stereo: np.ndarray, drive: float = 1.25) -> np.ndarray:
    return np.tanh(stereo * drive) / np.tanh(drive)


# ---------------------------------------------------------------------------
# Sound generators
# ---------------------------------------------------------------------------


def sine_tone(
    frequency: float,
    duration: float,
    *,
    amplitude: float = 1.0,
    phase: float = 0.0,
    vibrato_hz: float = 0.0,
    vibrato_depth: float = 0.0,
) -> np.ndarray:
    t = time_axis(duration)
    if vibrato_hz > 0 and vibrato_depth > 0:
        phase_curve = (
            2.0 * math.pi * frequency * t
            + vibrato_depth * np.sin(2.0 * math.pi * vibrato_hz * t)
            + phase
        )
    else:
        phase_curve = 2.0 * math.pi * frequency * t + phase
    return amplitude * np.sin(phase_curve)


def partial_tone(
    base_frequency: float,
    duration: float,
    partials: tuple[tuple[float, float], ...],
    *,
    attack: float,
    release: float,
) -> np.ndarray:
    signal = np.zeros(seconds_to_samples(duration), dtype=np.float64)
    for ratio, gain in partials:
        signal += sine_tone(base_frequency * ratio, duration, amplitude=gain)
    signal *= envelope(duration, attack=attack, release=release)
    peak = np.max(np.abs(signal)) or 1.0
    return signal / peak


def shimmer_tone(frequency: float, duration: float) -> np.ndarray:
    """Transparent glass-like tone with non-harsh upper partials."""
    mono = partial_tone(
        frequency,
        duration,
        partials=((1.0, 1.0), (2.01, 0.32), (3.98, 0.13), (6.02, 0.05)),
        attack=0.018,
        release=max(0.20, duration * 0.72),
    )
    return mono


def notification_tone(duration: float = 0.72) -> np.ndarray:
    """Original two-part notification-like sound, not modeled on a service."""
    t = time_axis(duration)
    first = sine_tone(587.33, duration, amplitude=0.70)
    second = sine_tone(783.99, duration, amplitude=0.32, phase=0.25)
    bell = first + second
    bell *= np.exp(-4.4 * t)
    bell *= envelope(duration, attack=0.008, release=0.12)
    return bell


def stopping_tick(duration: float = 0.35) -> np.ndarray:
    """A restrained high-frequency stop cue."""
    t = time_axis(duration)
    carrier = sine_tone(1760.0, duration, amplitude=0.65)
    overtone = sine_tone(2637.0, duration, amplitude=0.22, phase=0.7)
    click = (carrier + overtone) * np.exp(-12.0 * t)
    click *= envelope(duration, attack=0.002, release=0.17)
    return click


def boundary_tone(duration: float = 2.15) -> np.ndarray:
    t = time_axis(duration)
    start_hz = 720.0
    end_hz = 1320.0
    frequency = start_hz * np.power(end_hz / start_hz, t / duration)
    phase = 2.0 * math.pi * np.cumsum(frequency) / SAMPLE_RATE
    line = np.sin(phase)
    line += 0.16 * np.sin(phase * 2.004 + 0.4)
    line *= envelope(duration, attack=0.42, release=0.76)
    return line / (np.max(np.abs(line)) or 1.0)


def low_resonance(duration: float = 4.6) -> np.ndarray:
    """Low, non-horror resonance suggesting an opening space."""
    t = time_axis(duration)
    root = sine_tone(73.42, duration, amplitude=0.72, vibrato_hz=0.11, vibrato_depth=0.06)
    fifth = sine_tone(110.00, duration, amplitude=0.28, phase=0.3)
    upper = sine_tone(220.00, duration, amplitude=0.08, phase=1.1)
    signal = root + fifth + upper
    swell = smoothstep01(t / 1.35) * smoothstep01((duration - t) / 1.10)
    return signal * swell


def reflection_tone(frequency: float, duration: float = 0.86) -> np.ndarray:
    mono = shimmer_tone(frequency, duration)
    t = time_axis(duration)
    return mono * np.exp(-1.5 * t)


def convergence_chord(duration: float = 3.2) -> np.ndarray:
    """A restrained open chord that converges rather than triumphs."""
    frequencies = (146.83, 220.00, 293.66, 440.00)
    gains = (0.58, 0.42, 0.27, 0.12)
    signal = np.zeros(seconds_to_samples(duration), dtype=np.float64)
    for index, (frequency, gain) in enumerate(zip(frequencies, gains)):
        signal += sine_tone(
            frequency,
            duration,
            amplitude=gain,
            phase=index * 0.31,
            vibrato_hz=0.09 + index * 0.012,
            vibrato_depth=0.025,
        )
    signal *= envelope(duration, attack=0.75, release=0.72)
    return signal / (np.max(np.abs(signal)) or 1.0)


def filtered_ambience(duration: float, rng: np.random.Generator) -> np.ndarray:
    """Low mechanical room tone with slow movement."""
    sample_count = seconds_to_samples(duration)
    noise = rng.normal(0.0, 1.0, sample_count)
    low_noise = one_pole_lowpass(noise, 145.0)
    low_noise = highpass_from_lowpass(low_noise, 24.0)
    peak = np.max(np.abs(low_noise)) or 1.0
    low_noise /= peak

    t = time_axis(duration)
    hum = 0.55 * np.sin(2.0 * math.pi * 48.0 * t)
    hum += 0.20 * np.sin(2.0 * math.pi * 96.0 * t + 0.3)
    hum += 0.08 * np.sin(2.0 * math.pi * 144.0 * t + 1.0)

    slow_motion = 0.78 + 0.12 * np.sin(2.0 * math.pi * 0.08 * t + 0.6)
    slow_motion += 0.07 * np.sin(2.0 * math.pi * 0.031 * t + 2.0)

    ambience = (0.50 * low_noise + 0.22 * hum) * slow_motion
    ambience *= envelope(duration, attack=1.0, release=1.25)
    return ambience


def quiet_reverb(stereo: np.ndarray, delays: tuple[float, ...], gains: tuple[float, ...]) -> np.ndarray:
    """Add a small deterministic echo field to a stereo signal."""
    result = stereo.copy()
    for delay, gain in zip(delays, gains):
        offset = seconds_to_samples(delay)
        if offset < len(stereo):
            # Swap channels on alternating reflections for a subtle widening.
            reflected = stereo[:-offset, ::-1]
            result[offset:] += reflected * gain
    return result


# ---------------------------------------------------------------------------
# Timeline assembly
# ---------------------------------------------------------------------------


def build_soundtrack(seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    master = np.zeros((seconds_to_samples(DURATION), CHANNELS), dtype=np.float64)

    # 00.0-21.0: quiet operations-bureau ambience, reduced around the boundary.
    ambience = filtered_ambience(DURATION, rng)
    ambience_stereo = equal_power_pan(ambience, 0.0)
    timeline = time_axis(DURATION)
    reduction = 1.0 - 0.39 * (
        smoothstep01((timeline - 6.75) / 0.90)
        * smoothstep01((11.25 - timeline) / 0.90)
    )
    ambience_stereo *= reduction[:, None]
    master += ambience_stereo * 0.095

    # 03.35: original notification-like cue.
    notification = equal_power_pan(notification_tone(), -0.18)
    notification = quiet_reverb(notification, (0.105, 0.205), (0.18, 0.09))
    add_at(master, notification, 3.35, gain=0.22)

    # 04.10: the hand stops before touching the display.
    stop = equal_power_pan(stopping_tick(), 0.26)
    add_at(master, stop, 4.10, gain=0.14)

    # 08.55: the thin boundary appears and brightens.
    boundary = equal_power_pan(boundary_tone(), 0.0)
    boundary = quiet_reverb(boundary, (0.072, 0.141, 0.285), (0.19, 0.11, 0.055))
    add_at(master, boundary, 8.55, gain=0.14)

    # 10.85-15.0: the line reveals an unnamed space.
    resonance = equal_power_pan(low_resonance(), 0.0)
    resonance = quiet_reverb(resonance, (0.23, 0.49, 0.92), (0.16, 0.09, 0.045))
    add_at(master, resonance, 10.75, gain=0.18)

    # 15.0-18.0: four equal reflections. Frequencies form a suspended shape.
    reflection_starts = (15.00, 15.70, 16.40, 17.10)
    reflection_frequencies = (523.25, 587.33, 659.25, 739.99)
    reflection_pans = (-0.48, -0.16, 0.16, 0.48)
    for start, frequency, pan in zip(
        reflection_starts, reflection_frequencies, reflection_pans
    ):
        tone = equal_power_pan(reflection_tone(frequency), pan)
        tone = quiet_reverb(tone, (0.095, 0.19), (0.18, 0.08))
        add_at(master, tone, start, gain=0.115)

    # 18.0-21.0: four reflections resolve into one restrained chord.
    chord = equal_power_pan(convergence_chord(), 0.0)
    chord = quiet_reverb(chord, (0.16, 0.34, 0.68), (0.15, 0.08, 0.035))
    add_at(master, chord, 17.85, gain=0.19)

    # Very subtle high air in the final title, fading with the image.
    air_duration = 3.15
    air_noise = rng.normal(0.0, 1.0, seconds_to_samples(air_duration))
    air_noise = highpass_from_lowpass(air_noise, 4800.0)
    air_noise /= np.max(np.abs(air_noise)) or 1.0
    air_noise *= envelope(air_duration, attack=0.85, release=0.60)
    add_at(master, equal_power_pan(air_noise, 0.0), 17.85, gain=0.012)

    # Match the visual fade from 20.65 to 21.00.
    fade_start = seconds_to_samples(20.65)
    if fade_start < len(master):
        fade = np.linspace(1.0, 0.0, len(master) - fade_start, dtype=np.float64)
        fade = fade * fade
        master[fade_start:] *= fade[:, None]

    # Remove DC and apply a restrained limiter.
    master -= np.mean(master, axis=0, keepdims=True)
    master = soft_limit(master, drive=1.15)

    # Normalize to a conservative peak, leaving headroom for later video muxing.
    peak = float(np.max(np.abs(master))) or 1.0
    target_peak = 10.0 ** (-3.0 / 20.0)  # -3 dBFS peak
    master *= target_peak / peak
    return np.clip(master, -1.0, 1.0)


# ---------------------------------------------------------------------------
# WAV output and validation
# ---------------------------------------------------------------------------


def write_wav(path: Path, stereo: np.ndarray) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    pcm = np.round(stereo * 32767.0).astype("<i2")
    with wave.open(str(path), "wb") as stream:
        stream.setnchannels(CHANNELS)
        stream.setsampwidth(2)
        stream.setframerate(SAMPLE_RATE)
        stream.writeframes(pcm.tobytes())


def inspect_wav(path: Path) -> dict[str, float | int]:
    with wave.open(str(path), "rb") as stream:
        frames = stream.getnframes()
        sample_rate = stream.getframerate()
        channels = stream.getnchannels()
        sample_width = stream.getsampwidth()
    return {
        "channels": channels,
        "sample_rate": sample_rate,
        "sample_width": sample_width,
        "frames": frames,
        "duration": frames / sample_rate,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Build the 21-second MEMORIOPOLIS section 10 soundtrack."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output WAV path. Default: {DEFAULT_OUTPUT}",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=DEFAULT_SEED,
        help=f"Seed for deterministic ambience. Default: {DEFAULT_SEED}",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output_path = args.output.resolve()

    soundtrack = build_soundtrack(args.seed)
    write_wav(output_path, soundtrack)
    info = inspect_wav(output_path)

    expected_frames = seconds_to_samples(DURATION)
    if info["channels"] != CHANNELS:
        raise RuntimeError(f"Unexpected channel count: {info['channels']}")
    if info["sample_rate"] != SAMPLE_RATE:
        raise RuntimeError(f"Unexpected sample rate: {info['sample_rate']}")
    if info["frames"] != expected_frames:
        raise RuntimeError(f"Unexpected frame count: {info['frames']}")

    peak = float(np.max(np.abs(soundtrack)))
    rms = float(np.sqrt(np.mean(np.square(soundtrack))))
    print(f"Wrote: {output_path}")
    print(f"Duration: {info['duration']:.3f} seconds")
    print(f"Format: {info['sample_rate']} Hz, {info['channels']} channels, 16-bit PCM")
    print(f"Peak: {20.0 * math.log10(max(peak, 1e-12)):.2f} dBFS")
    print(f"RMS: {20.0 * math.log10(max(rms, 1e-12)):.2f} dBFS")
    print(f"Seed: {args.seed}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
