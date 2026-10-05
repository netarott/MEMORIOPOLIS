# E0001 Audio PoC

## 目的

- `E0001_ja.md` から `E0001_ja.mp3` を生成
- `E0001_fr.md` から `E0001_fr.mp3` を生成
- 1 Markdown = 1 MP3
- YAML風メタデータ、参照URL、制作メモは読み上げない
- 確認用に narration.txt と SRT も生成

## 1. 同じフォルダーへ置く

```text
E0001_ja.md
E0001_fr.md
memoriopolis_e0001_audio_poc.py
```

## 2. PowerShellでインストール

```powershell
py -m pip install --upgrade edge-tts
```

## 3. MP3生成

```powershell
py .\memoriopolis_e0001_audio_poc.py
```

## 4. 出力

```text
audio_E0001_poc/
├─ E0001_ja.mp3
├─ E0001_ja.srt
├─ E0001_ja.narration.txt
├─ E0001_fr.mp3
├─ E0001_fr.srt
└─ E0001_fr.narration.txt
```

## 5. 試聴

最初に各MP3の冒頭、中央、末尾を確認します。

- 日本語: タイトル、列車の場面、中心命題、結末
- フランス語: 固有名詞、Roms、SNS周辺、中心命題、結末
- 制作メモやURLが読まれていないこと
- 速度が疲れにくいこと

## 6. 次工程

試聴結果が良ければ、canonical済みの全E0001へ同じ処理を展開し、MP3へ言語・アルバム情報を付与してYouTube Musicへアップロードします。
