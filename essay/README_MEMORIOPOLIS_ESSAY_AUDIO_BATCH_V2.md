# MEMORIOPOLIS Essay Audio Batch v2

## 修正点

1. `--job E0001:it`の形式でEssayと言語を正確なペアとして指定します。
2. `--essay E0001 --essay E0002 --language it --language en`による組合せ展開は使いません。
3. Edge TTSの一時的な接続切断に対して最大4回、自動再試行します。
4. 既に生成済みのMP3は`--overwrite`なしでは再生成しません。

## 配置

```text
MEMORIOPOLIS/
└─ essay/
   ├─ E0001/
   │  └─ E0001_it.md
   ├─ E0002/
   │  └─ E0002_en.md
   ├─ memoriopolis_essay_audio_batch.py
   └─ run_memoriopolis_essay_audio.ps1
```

## 実行

```powershell
.\run_memoriopolis_essay_audio.ps1
```

実行内容は次と同じです。

```powershell
py .\memoriopolis_essay_audio_batch.py `
  --root . `
  --job E0001:it `
  --job E0002:en `
  --continue-on-error
```

## 今回のエラー後に英語だけ再実行する場合

イタリア語MP3は既に成功しています。英語だけを再実行できます。

```powershell
py .\memoriopolis_essay_audio_batch.py `
  --root . `
  --job E0002:en
```

接続が再度切れた場合は、スクリプトが最大4回まで待機して再試行します。

## 出力

```text
E0001/audio_E0001_all/E0001_it.mp3
E0002/audio_E0002_all/E0002_en.mp3
```

## 上書き

```powershell
py .\memoriopolis_essay_audio_batch.py `
  --root . `
  --job E0001:it `
  --job E0002:en `
  --overwrite `
  --continue-on-error
```
