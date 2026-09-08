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

次の12フィールドを、この順序で作成します。

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
ExampleBreakdown
ExampleExplanation
```
## 例文解説フィールド

### ExampleBreakdown

例文を意味のまとまりに分け、日本語との対応を示す。

例：

```text
도시의 ＝ 都市の
기록을 ＝ 記録を
확인했다 ＝ 確認した

### ExampleExplanation

例文がなぜその日本語訳になるのかを、初学者向けに説明する。

説明では、助詞や語尾、動詞の辞書形と例文中の形をつなぎ、最後に文全体の訳へ戻る。専門用語の羅列を避け、一度読んで文の組み立てが腹落ちする長さを目指す。

### 執筆方針

- 初出の文法は丁寧に説明する。
- 再登場した文法は、以前の説明とのつながりを示す。
- 単なる逐語訳にせず、語と語の関係を説明する。
- 必要以上に長い文法講義にしない。
- 日本語との対応は「同じ」と断定せず、「近い働き」「この文では」のように説明する。
- 自然な日本語訳と直訳に違いがある場合は、その理由を短く説明する。

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
