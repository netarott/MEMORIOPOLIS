# MEMORIOPOLIS zh-Hant-TW Core20

更新日：2026-09-27

## ファイル

- `zh-Hant-TW_core20_master_17fields.csv`：ヘッダー付き正本
- `zh-Hant-TW_core20_anki_17fields.csv`：ヘッダーなしAnkiインポート用

## ノートタイプとデッキ

- ノートタイプ：`MEMORIOPOLIS Taiwanese Mandarin Vocabulary`
- デッキ：`MEMORIOPOLIS::TaiwaneseMandarin`

## 17フィールド

1. ID
2. TraditionalChinese
3. Zhuyin
4. Pinyin
5. Japanese
6. PartOfSpeech
7. TaiwanMandarinGrammar
8. ExampleTraditionalChinese
9. ExampleZhuyin
10. ExamplePinyin
11. ExampleJapanese
12. Source
13. Tags
14. ExampleBreakdown
15. ExampleExplanation
16. ExamplePronunciationHint
17. ConceptScene

## Sourceとタグ

- Source：`E0001_zh-Hant-TW`
- Tags：`memoriopolis::zh_hant_tw::core20`

## 画像

`ConceptScene`はC0011-C0020のWebPファイルを参照するHTMLを含む。
先に `MEMORIOPOLIS_ConceptImages_C0011-C0020_2026-09-26.zip` の `webp/` 10枚をAnkiメディアへ配置する。

## インポート

1. AnkiメディアへCore20 WebP 10枚を配置する。
2. `zh-Hant-TW_core20_anki_17fields.csv`をUTF-8で読み込む。
3. ノートタイプとデッキを上記どおり選択する。
4. 17列を順番どおり割り当てる。
5. フィールド内HTMLを許可する。
6. インポート後、C0011とC0020をプレビューする。
7. 同期し、AnkiDroidでTTS、ダークモード、プルダウン、自動スクロールを確認する。

## 設計方針

- 臺灣で自然な繁體字語彙を採用する。
- 注音を第一の発音観測面、拼音を補助観測面とする。
- 例文はE0001の経験的な核から作る。
- 「有／存在」「聽／聽見」「查詢／確認／驗證」などのConcept境界を説明する。
