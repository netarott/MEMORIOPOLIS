# 韓国語版Anki Core10 FIX候補

更新日：2026-09-11

## 収録ファイル

- `ko_core10_master.csv`：正本。ヘッダーあり、13フィールド。
- `ko_core10_anki.csv`：Anki取込用。ヘッダーなし、13フィールド。

## 今回の更新

- `ExamplePronunciationHint`を13番目のフィールドとして追加。
- C0001はAnkiDroid確認済みの内容を収録。
- C0002～C0010へ、ハングル、Romanization、日本人の耳に聞こえるカタカナ、音の説明を追加。
- C0002の`Source`は、正本からの直接引用ではないため`MEMORIOPOLIS core`を維持。

## Ankiへの取込

1. ノートタイプに`ExamplePronunciationHint`を含む13フィールドがあることを確認する。
2. `ko_core10_anki.csv`をインポートする。
3. 1列目を`ID`、13列目を`ExamplePronunciationHint`へ対応させる。
4. 既存ノートを更新する設定を使う。ノートを削除して再登録しない。
5. Windows版AnkiでC0001～C0010をプレビューする。
6. 同期後、AnkiDroidで表示と音声を確認する。
7. 問題がなければ韓国語版Anki Core10をFIXする。

## 方針

カタカナは正しい発音の代用ではない。日本人の耳が音声の中から対象語を見つけ、ハングルへ戻るための一時的な「音の橋」として、`ExamplePronunciationHint`内だけで使用する。
