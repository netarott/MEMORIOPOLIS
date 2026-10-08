$ErrorActionPreference = "Stop"

# Place this file and memoriopolis_audio_sync.py in MEMORIOPOLIS\essay\
# Existing MP3s are skipped. Only missing MP3s are generated.
py .\memoriopolis_audio_sync.py --root . --continue-on-error
