# MEMORIOPOLIS Audio Sync

## 目的

毎回スクリプトを作り直さず、`essay`配下を走査して不足しているMP3だけを作成する。

```text
MP3がある   -> SKIP
MP3がない   -> canonical Markdownから生成
```

## 配置

```text
MEMORIOPOLIS/
└─ essay/
   ├─ E0001/
   ├─ E0002/
   ├─ memoriopolis_audio_sync.py
   └─ run_memoriopolis_audio_sync.ps1
```

## 初回だけ

```powershell
py -m pip install --upgrade edge-tts
```

## 通常運用

```powershell
.\run_memoriopolis_audio_sync.ps1
```

または:

```powershell
py .\memoriopolis_audio_sync.py --root . --continue-on-error
```

## 今日の不足分だけ事前確認

```powershell
py .\memoriopolis_audio_sync.py --root . --dry-run
```

## 特定ジョブだけ

```powershell
py .\memoriopolis_audio_sync.py --root . --job E0002:ja
```

複数指定:

```powershell
py .\memoriopolis_audio_sync.py `
  --root . `
  --job E0001:es `
  --job E0002:ja `
  --job E0002:zh-Hant-TW `
  --continue-on-error
```

## 強制再生成

通常は使わない。

```powershell
py .\memoriopolis_audio_sync.py --root . --job E0002:ja --overwrite
```

## 出力規則

```text
E0002/E0002_ja.md
-> E0002/audio_E0002_all/E0002_ja.mp3
```

付随ファイル:

```text
E0002_ja.srt
E0002_ja.narration.txt
E0002_ja.audio.json
```

## 安全策

- `status: canonical`以外は生成しない
- Essayフォルダー名、ファイル名、`essay_id`を照合
- 既存MP3は先に検出し、Markdown解析やTTS通信もせずスキップ
- 不足MP3がゼロなら音声一覧のネットワーク取得も行わない
- 一時ファイルから完成ファイルへ置換
- 接続切断時は既定4回まで再試行
- 制作ノート、脚注定義、URL、コードブロックを読み上げない
- 実行結果を`MEMORIOPOLIS_essay_audio_manifest.json`へ記録

## 現在の音声設定

```text
ja           ja-JP-NanamiNeural       -3%
en           en-US-AndrewNeural        -6%
zh-Hant-TW   zh-TW-HsiaoChenNeural     -8%
ko           ko-KR-SunHiNeural         -8%
ru           ru-RU-SvetlanaNeural      -8%
fil          fil-PH-BlessicaNeural     -8%
id           id-ID-GadisNeural         -8%
vi           vi-VN-HoaiMyNeural        -10%
fr           fr-FR-DeniseNeural        -8%
de           de-DE-KatjaNeural         -5%
it           it-IT-ElsaNeural          -6%
es           es-ES-ElviraNeural        -6%
pt-BR        pt-BR-FranciscaNeural     -7%
```

利用時には現在の音声一覧を取得し、優先Voiceが使えない場合は同じロケールの代替Voiceを選ぶ。
