# MEMORIOPOLIS Filipino Core10 draft02, 18 fields

## 改修目的

初学者が「なぜこの日本語訳になるのか」を、例文の語句と文法関係から追えるようにする。

## 追加フィールド

13. `ExampleBreakdown`：例文を意味のまとまりごとに分解
14. `ExampleExplanation`：標識・リンカー・語順・動詞形が日本語訳を作る過程を説明

既存の音韻・語形成フィールドは削除しない。

## 更新方法

既存ノートタイプ `MEMORIOPOLIS Filipino Vocabulary` に、`ExampleBreakdown` と `ExampleExplanation` を `MorphologicalBreakdown` の直後へ追加する。

その後、`fil_core10_anki_draft02_18fields.csv`をインポートし、1列目の`ID`を既存ノート照合用フィールドとして更新する。事前にAnkiのバックアップを取る。

## TTS

```html
{{tts fil_PH:Filipino}}
{{tts fil_PH:ExampleFilipino}}
```

音声名は固定しない。
