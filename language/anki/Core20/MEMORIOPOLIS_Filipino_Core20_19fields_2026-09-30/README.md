# MEMORIOPOLIS Filipino Core20

更新日：2026-09-30

## 収録ファイル

- `fil_core20_master_19fields.csv`：ヘッダー付き正本
- `fil_core20_anki_19fields.csv`：ヘッダーなしAnkiインポート用
- `E0001_fil_canonical.md`：フィリピン語版Essay正本

## 正式19フィールド

1. ID
2. Filipino
3. Pronunciation
4. Japanese
5. PartOfSpeech
6. UsageNote
7. ExampleFilipino
8. ExampleJapanese
9. Root
10. Affixes
11. PerceptualSegmentation
12. MorphologicalBreakdown
13. ExampleBreakdown
14. ExampleExplanation
15. MeaningBridge
16. SoundBridge
17. Source
18. CourseTags
19. ConceptScene

## Sourceとタグ

- Source：`E0001_fil`
- CourseTags：`memoriopolis::fil::core20`

## 音声

カードテンプレートは次を使用する。

- 単語：`{{tts fil_PH:Filipino}}`
- 例文：`{{tts fil_PH:ExampleFilipino}}`

Windows版Ankiでフィリピン語音声がない場合はエラーを許容し、学習本番のAnkiDroidで確認する。

## Concept境界

- C0011 `umiral`：抽象的存在・効力。所在の`may / mayroon / nasa`と区別。
- C0012 `gawin`：対象フォーカスの「する」。行為者フォーカス`gumawa`と区別。
- C0013 `magkaroon`：獲得・成立を伴う「持つ」。静的所有`may / mayroon`と区別。
- C0016 `makarinig`：耳に入る。意識して聞く`makinig`と区別。
- C0017 `maghanap`：情報や意味を探す。研究する`magsaliksik`、検査する`suriin`と区別。
- C0019 `maiugnay`：関係づけられる・結びつく。文脈により`iugnay`等とフォーカスを使い分ける。
- C0020 `matali`：物理的・制度的・関係的に縛られる。

## インポート

1. Core20 WebP 10枚をAnkiメディアへ配置する。
2. `fil_core20_anki_19fields.csv`をUTF-8として読み込む。
3. フィリピン語ノートタイプと`MEMORIOPOLIS::Filipino`を選択する。
4. 19列を順番どおり割り当てる。
5. フィールド内HTMLを許可する。
6. C0011、C0012、C0016、C0019、C0020をプレビューする。
7. AnkiDroidで画像、`fil_PH` TTS、語根、接辞、音の切れ目、3段プルダウン、自動スクロールを確認する。
