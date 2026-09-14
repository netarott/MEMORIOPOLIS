# MEMORIOPOLIS 臺灣華語 Core10 draft01

## 位置づけ

第四章第十二節の臺灣繁體中文正本を読むためのCore10です。C0003「城市」だけは、対象語が第十二節本文に直接現れないため、読解コース用例文として`MEMORIOPOLIS core`をSourceにしています。それ以外は`section12_zh-TW`に基づきます。

## 16フィールド

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

## 設計原則

- 繁體字を主表示にする。
- 注音符號を臺灣華語の主要な音韻座標として扱う。
- 拼音は他言語との横断学習と入力補助の橋として併記する。
- カタカナは正しい発音の代用ではなく、日本人の耳が音を発見するための一時的な橋として使う。
- 声調、軽声、そり舌音、ü系母音、鼻音韻尾を必要に応じて説明する。

## 収録ファイル

- `zh_tw_core10_master_draft01.csv`：ヘッダーあり
- `zh_tw_core10_anki_draft01.csv`：ヘッダーなし、Anki取込用
- `ZH_TW_NOTE_TYPE_DRAFT01.md`：ノートタイプとTTS設計

Windowsの`zh-TW`音声環境は別会話で導入作業中です。TTSが未導入でもカード表示とCSVインポートは先に実施できます。
