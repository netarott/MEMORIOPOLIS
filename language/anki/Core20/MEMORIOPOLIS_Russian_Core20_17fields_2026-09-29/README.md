# MEMORIOPOLIS Russian Core20

更新日：2026-09-29

## 収録ファイル

- `ru_core20_master_17fields.csv`：ヘッダー付き正本
- `ru_core20_anki_17fields.csv`：ヘッダーなしAnkiインポート用

## 正式17フィールド

1. ID
2. Russian
3. Stress
4. Transliteration
5. Japanese
6. PartOfSpeech
7. RussianGrammar
8. ExampleRussian
9. ExampleStress
10. ExampleTransliteration
11. ExampleJapanese
12. Source
13. Tags
14. ExampleBreakdown
15. ExampleExplanation
16. ExamplePronunciationHint
17. ConceptScene

## Sourceとタグ

- Source：`E0001_ru`
- Tags：`memoriopolis::ru::core20`

## Concept境界

- C0011 `существовать`：抽象的・論理的存在。所在・所有の`есть / быть`とは区別する。
- C0012 `делать`：基本的な「する・作る」。日本語の「する」と完全には一致しない。
- C0013 `иметь`：明示的・抽象的所有。日常所有では`у ... есть`も重要。
- C0014 `отправлять`：送る過程。完了体は`отправить`。
- C0015 `получать`：受け取る過程。完了体は`получить`。
- C0016 `слышать`：耳に入る。意識して聞く`слушать`と区別する。
- C0017 `искать`：探す・意味を調べる過程。結果として見つける`найти`と対になる。
- C0018 `переходить`：場所・状態・話題・思考の焦点が移る。
- C0019 `связываться`：結びつく・関係を作る。文脈により`быть связанным`も用いる。
- C0020 `быть привязанным`：物理的・制度的・関係的に結び付けられ、拘束される。

## インポート

1. ロシア語ノートタイプが17フィールド構成であることを確認する。
2. Core20のWebP画像10枚をAnkiメディアへ配置する。
3. `ru_core20_anki_17fields.csv`をUTF-8として読み込む。
4. ロシア語ノートタイプと`MEMORIOPOLIS::Russian`を選択する。
5. 17列を順番どおり割り当てる。
6. フィールド内HTMLを許可する。
7. C0011、C0016、C0019、C0020をプレビューする。
8. 強勢記号、転写、画像、`ru_RU` TTS、3段プルダウン、自動スクロールを確認する。
