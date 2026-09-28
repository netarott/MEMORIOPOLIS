# MEMORIOPOLIS Korean Core20

更新日：2026-09-28

## ファイル

- `ko_core20_master_14fields.csv`：ヘッダー付き正本
- `ko_core20_anki_14fields.csv`：ヘッダーなしAnkiインポート用

## 正式14フィールド

1. ID
2. Korean
3. Romanization
4. Japanese
5. PartOfSpeech
6. ExampleKorean
7. ExampleRomanization
8. ExampleJapanese
9. Source
10. Tags
11. ExampleBreakdown
12. ExampleExplanation
13. ExamplePronunciationHint
14. ConceptScene

## Sourceとタグ

- Source：`E0001_ko`
- Tags：`memoriopolis::ko::core20`

## 画像

`ConceptScene`はC0011-C0020のWebP画像を参照するHTMLを含む。
`MEMORIOPOLIS_ConceptImages_C0011-C0020_2026-09-26.zip`の`webp/`をAnkiメディアへ配置する。

## インポート

1. 韓国語ノートタイプの末尾に`ConceptScene`があることを確認する。
2. Core20 WebP 10枚をAnkiメディアへ配置する。
3. `ko_core20_anki_14fields.csv`をUTF-8として読み込む。
4. 韓国語ノートタイプと`MEMORIOPOLIS::Korean`を選択する。
5. 14列を順番どおり割り当てる。
6. フィールド内HTMLを許可する。
7. C0011、C0016、C0020をプレビューする。
8. 同期後にAnkiDroidで画像、TTS、ダークモード、プルダウン、自動スクロールを確認する。

## Concept境界

- C0011 `존재하다`：抽象的・論理的な存在。所在・所有の`있다`とは区別する。
- C0012 `하다`：基本動詞。ただし日本語の「する」と一対一ではない。
- C0013 `가지다`：物理的所有だけでなく、権限・関係・性質にも使う。
- C0016 `듣다`：音・話を聞く。質問する`묻다`とは別Concept。
- C0017 `찾아보다`：情報を探して調べてみる。検証する`검증하다`とは区別する。
- C0018 `옮겨 가다`：位置・焦点・状態が別の側へ移る。
- C0019 `연결되다`：関係が成立する自動詞的Concept。
- C0020 `얽매이다`：制度・関係・規則などに拘束される状態。
