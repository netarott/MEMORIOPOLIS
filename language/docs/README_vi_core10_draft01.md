# MEMORIOPOLIS Vietnamese Core10 draft01

## Deck
`MEMORIOPOLIS::Vietnamese`

## Note type
`MEMORIOPOLIS Vietnamese Vocabulary`

## Import
Import `vi_core10_anki_draft01_18fields.csv` as UTF-8, no header, 18 columns.

## TTS
```html
{{tts vi_VN:Vietnamese}}
{{tts vi_VN:ExampleVietnamese}}
```

Windows `Language.Basic~~~vi-VN~0.0.1.0` and `Language.TextToSpeech~~~vi-VN~0.0.1.0` are installed.

On AnkiDroid, try `vi_VN` first. If `APP_MISSING_VOICE` appears, temporarily add `{{tts-voices:}}`, open the voice settings, copy the exact Vietnamese locale and voice identifier supplied by the device, and use those exact values. Do not guess the Android locale.

## Design
The standard 18 fields are retained. Vietnamese tone and orthographic information are recorded inside `Pronunciation`, `PerceptualSegmentation`, and `SoundBridge` for Core10, without adding a nineteenth field yet.
