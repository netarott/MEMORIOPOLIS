# 第七節「矢印を動かす」最小状態機械

## 目的

第六節の式 `X_(t+1) = T(X_t, e_t)` を、決定論的な小さなPython模型として実行する。
正解率を競うモデルではなく、何が届き、どの条件で状態が動いたかを監査可能にする。

## 必要環境

- Python 3.10以上
- 外部ライブラリ不要

## 実行方法

同じフォルダで次を実行する。

```bash
python section7_state_machine.py --input test_events.csv --output-dir results
```

## 合成シナリオ

1. `01_expected_order`: 日報、問い合わせ、予定、レビュー、確認の順に到着する。
2. `02_reordered`: 同じ5件が別順序で到着する。終点は同じでも途中経路が異なる。
3. `03_mismatched_work`: レビューと確認が別作業 `WU-999` に属し、未確定に保持される。

## 出力

- `results/summary.csv`: シナリオごとの最終状態と件数
- `results/audit_log.csv`: 入力ごとの状態、判定、理由
- `sample_console_output.txt`: 実行例

## 防衛線

- すべて合成データである。
- 実名、顧客名、実在ID、認証情報を含まない。
- 個人評価、処遇判断、犯人捜しには使用しない。
- この最小模型は自然言語の意味を理解しない。
