# MEMORIOPOLIS Taiwanese Mandarin Vocabulary draft01

## デッキ

`MEMORIOPOLIS::TaiwaneseMandarin`

## ノートタイプ

`MEMORIOPOLIS Taiwanese Mandarin Vocabulary`

## フィールド順

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

## TTS方針

音声専用フィールドは作らず、OSの`zh_TW` TTSが利用可能になった後、通常表記を読み上げる。

```html
{{tts zh_TW:TraditionalChinese}}
```

```html
{{tts zh_TW:ExampleTraditionalChinese}}
```

注音符號と拼音は表示用で、TTSには繁體字の通常表記を渡す。

## 表面

ID、TraditionalChinese、Zhuyin、Pinyin、単語TTS。

## 裏面

日本語、品詞、臺灣華語文法、例文、例文注音、例文拼音、例文TTS、例文日本語訳、文の組み立て、意味の橋、音の橋、Source。
