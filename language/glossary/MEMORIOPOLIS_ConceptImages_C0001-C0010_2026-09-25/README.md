# MEMORIOPOLIS Concept Images C0001-C0010

## Contents
- `webp/`: Anki用推奨版。画質95で容量を抑えたWebP。
- `png/`: 分割後の可逆PNG原本。
- `manifest.csv`: Concept ID、ファイル名、画像寸法、WebP容量。

## Ankiへの登録
1. `webp/` 内の対応画像を各ノートの `ConceptScene` フィールドへ貼り付ける。
2. まず `MEMORIOPOLIS::ModernJapanese` の C0001 だけで表示・同期テストする。
3. 成功後、ModernJapaneseのC0001-C0010へ展開する。
4. 他言語は同じ画像ファイルを順次共有する。

## Notes
- 元の5列x2行の1枚絵を、各Conceptの縦長画像へ分割した。
- 各画像は約250x625px。AnkiDroidでの初期試験には十分だが、将来大きく表示する場合は、各Conceptを個別生成した高解像度版へ更新できる。
- 画像内のConcept ID、日本語見出し、短い文は、記憶風景を構成する入力情報として保持した。
