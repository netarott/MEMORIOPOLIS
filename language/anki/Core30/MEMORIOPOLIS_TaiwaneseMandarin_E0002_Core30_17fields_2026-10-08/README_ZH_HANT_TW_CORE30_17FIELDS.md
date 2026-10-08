# MEMORIOPOLIS 臺灣華語 Core30

## 基本仕様

- 言語識別子: `zh-Hant-TW`
- TTSロケール: `zh_TW`
- Essay正本: `E0002_zh-Hant-TW.md`
- 対象Concept: C0021-C0030
- ノートタイプ: `MEMORIOPOLIS Taiwanese Mandarin Vocabulary`
- フィールド数: 17
- Tags: `memoriopolis::zh-Hant-TW::core30`

## ファイル

- `zh_tw_core30_master_17fields.csv`: ヘッダー付き正本
- `zh_tw_core30_anki_17fields.csv`: ヘッダーなしAnkiインポート用

## 正式フィールド順

```text
01 ID
02 TraditionalChinese
03 Zhuyin
04 Pinyin
05 Japanese
06 PartOfSpeech
07 TaiwanMandarinGrammar
08 ExampleTraditionalChinese
09 ExampleZhuyin
10 ExamplePinyin
11 ExampleJapanese
12 Source
13 Tags
14 ExampleBreakdown
15 ExampleExplanation
16 ExamplePronunciationHint
17 ConceptScene
```

## Ankiインポート

1. ノートタイプを `MEMORIOPOLIS Taiwanese Mandarin Vocabulary` にする。
2. 文字コードはUTF-8、区切り文字はカンマ。
3. `zh_tw_core30_anki_17fields.csv`はヘッダーなしとして読み込む。
4. HTMLを許可する。
5. フィールド順を17フィールドへ一致させる。
6. `ConceptScene`は17番目。
7. Core30共通画像がAnkiメディアに存在することを確認する。

## ConceptScene

```text
C0021 memoriopolis_c0021_marry.webp
C0022 memoriopolis_c0022_raise.webp
C0023 memoriopolis_c0023_work.webp
C0024 memoriopolis_c0024_hand_over.webp
C0025 memoriopolis_c0025_return.webp
C0026 memoriopolis_c0026_protect.webp
C0027 memoriopolis_c0027_balance.webp
C0028 memoriopolis_c0028_compete.webp
C0029 memoriopolis_c0029_perform.webp
C0030 memoriopolis_c0030_evaluate.webp
```

`ConceptScene`列にはAnki画像フィールド用の`<img src="...">`を格納している。

## 主なConcept境界

- `結婚` / `婚姻` / `已婚`
- `養育` / `撫養` / `教育`
- `工作` / `勞動`
- `交接` / `接手` / `交出`
- `回來` / `復職` / `恢復`
- `保障` / `保護`
- `兼顧` / `平衡`
- `競爭` / `合作`
- `扮演` / `假裝`
- `評價` / `評估` / `判定`
