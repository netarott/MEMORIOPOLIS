# MEMORIOPOLIS E0001 多言語MP3一括生成

## 対象

```text
E0001_ja.md
E0001_en.md
E0001_zh-Hant-TW.md
E0001_ko.md
E0001_ru.md
E0001_fil.md
E0001_id.md
E0001_vi.md
E0001_fr.md
```

原則は **1 Markdown = 1 MP3** です。

## 使い方

スクリプトを上記Markdownと同じフォルダーへ置きます。

```powershell
py -m pip install --upgrade edge-tts
py .\memoriopolis_e0001_audio_all.py --continue-on-error
```

既存MP3を上書きする場合:

```powershell
py .\memoriopolis_e0001_audio_all.py --continue-on-error --overwrite
```

## 出力

```text
audio_E0001_all/
├─ E0001_ja.mp3
├─ E0001_en.mp3
├─ E0001_zh-Hant-TW.mp3
├─ E0001_ko.mp3
├─ E0001_ru.mp3
├─ E0001_fil.mp3
├─ E0001_id.mp3
├─ E0001_vi.mp3
├─ E0001_fr.mp3
├─ 各言語の narration.txt
├─ 各言語の SRT
└─ E0001_audio_manifest.json
```

## 日本語とフランス語の確定設定

```text
日本語: ja-JP-NanamiNeural / -3%
フランス語: fr-FR-DeniseNeural / -8%
```

ほかの言語は、実行時にedge-ttsの実在音声一覧を取得し、優先候補が存在すれば採用します。候補が変わった場合は、対象ロケールから代替音声を選びます。

## 再生

例:

```powershell
Start-Process .\audio_E0001_all\E0001_ja.mp3
Start-Process .\audio_E0001_all\E0001_fr.mp3
```

## 確認

1. 各 `narration.txt` に制作メモやURLが入っていないこと
2. 冒頭、中央、末尾が欠けていないこと
3. 地域基準が正しいこと
   - 臺灣華語: zh-TW
   - スペイン語: 将来 es-ES
   - ポルトガル語: 将来 pt-BR
4. 繰り返し聞いて疲れにくい速度であること
5. 誤読が目立つ語は、後で音声用正規化辞書へ追加すること

## YouTube Musicへの次工程

全MP3を試聴後、PCからYouTube Musicへアップロードし、`MEMORIOPOLIS E0001 Random Circle`プレイリストを作成します。スマートフォンではシャッフルと全曲リピートを使用します。
