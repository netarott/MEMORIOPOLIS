$ErrorActionPreference = "Stop"

# Place this file and memoriopolis_essay_audio_batch.py in MEMORIOPOLIS\essay\
py -m pip install --upgrade edge-tts

# Exact pairs only. This does NOT include E0001_en.md.
py .\memoriopolis_essay_audio_batch.py `
  --root . `
  --job E0001:it `
  --job E0002:en `
  --continue-on-error
