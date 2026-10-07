# MEMORIOPOLIS Italian Core20

## ファイル

- `it_core20_master_19fields.csv`: ヘッダー付き確認用
- `it_core20_anki_19fields.csv`: ヘッダーなしAnkiインポート用
- `E0001_it.md`: イタリア語canonical版

## Core20

```text
C0011  esistere          ある／存在する
C0012  fare              する／作る
C0013  avere             持つ
C0014  inviare           送る
C0015  ricevere          受け取る
C0016  sentire           聞く／聞こえる／感じる
C0017  cercare           探す／調べる
C0018  spostarsi         移る／移動する
C0019  collegarsi        結びつく／接続する
C0020  essere vincolato  縛られる／制約されている
```

## フィールド

19フィールド。末尾は`ConceptScene`。

## 共通設定

```text
Source: E0001_it.md
CourseTags: memoriopolis::it::core20
TTS locale: it_IT
```

## Concept境界

- `sentire`: 音が耳に入る、または感じる。意識して耳を傾ける`ascoltare`とは区別。
- `cercare`: 探索過程。結果として見つける`trovare`とは区別。
- `spostarsi`: 人・物そのものが場所を移る。対象・状態を変える`cambiare`とは区別。
- `collegarsi`: 新しく接続関係へ入る。
- `essere vincolato`: すでに制約・依存関係の中にある。

## インポート

Ankiでは`it_core20_anki_19fields.csv`を使用し、既存の`MEMORIOPOLIS Italian Vocabulary`ノートタイプへ19フィールド順で割り当てる。
