# MEMORIOPOLIS Anki Templates

このフォルダは、『記憶都市（メモリオポリス）』韓国語読解コースで使用するAnkiカードテンプレートの正本です。

## 対象ノートタイプ

```text
MEMORIOPOLIS Korean Vocabulary
```

## ファイル

- `korean_vocabulary_front.html`: 表面テンプレート
- `korean_vocabulary_back.html`: 裏面テンプレート
- `korean_vocabulary_style.css`: カード共通スタイル

## 必要なフィールド

次の10フィールドを、この順序で作成します。

```text
ID
Korean
Romanization
Japanese
PartOfSpeech
ExampleKorean
ExampleRomanization
ExampleJapanese
Source
Tags
```

## Ankiへの設定方法

1. Ankiで「ツール」→「ノートタイプを管理」を開く。
2. `MEMORIOPOLIS Korean Vocabulary` を選択する。
3. 「カード」を開く。
4. 表面へ `korean_vocabulary_front.html` の内容を貼り付ける。
5. 裏面へ `korean_vocabulary_back.html` の内容を貼り付ける。
6. スタイルへ `korean_vocabulary_style.css` の内容を貼り付ける。
7. 保存する。

## 音声

韓国語の単語と例文は、AnkiのTTS機能を使用します。

```html
{{tts ko_KR:Korean}}
{{tts ko_KR:ExampleKorean}}
```

Windows版Ankiでは、Windowsに韓国語の音声合成機能がインストールされている必要があります。

## データの位置づけ

- `ko_core10_master.csv`: 見出し付きの編集用正本
- `ko_core10_anki.csv`: 見出しなしのAnki投入用データ
- `templates/`: Anki上の表示設定を再現するための正本
