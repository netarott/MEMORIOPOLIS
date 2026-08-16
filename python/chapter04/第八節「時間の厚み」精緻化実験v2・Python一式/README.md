# 第八節「時間の厚み」精緻化実験 v2

## 目的

同じ3時間を、次の層へ分けて観測する。

- 時計上の滞在時間 \(\tau\)
- 最終回答を含む最初の可視応答 \(\rho_{\mathrm{any}}\)
- 最終回答前の最初の可視中間応答 \(\rho_{\mathrm{progress}}\)
- 最終回答前に可視中間応答が一度でもあったか \(I_{\mathrm{visible}}\)
- 内部履歴 \(H_t^{\mathrm{internal}}\)
- 可視履歴 \(H_t^{\mathrm{visible}}\)
- 依頼者から見た最長沈黙時間

## シナリオ

### A_silent_three_hours

最終回答まで途中の可視中間応答なし。

### B_checkpoint_three_hours

受領と中間状況を節目で共有。内部イベントも保存。

### C_frequent_updates_three_hours

途中報告をさらに増やす。ただし、Bより優れているとは判定しない。
可視イベント件数を増やす競争を防ぐための対照シナリオ。

## 実行

```powershell
python .\section8_time_model_v2.py `
    --input .\time_events_v2.csv `
    --output-dir .\results
```

## 重要な防衛線

- 件数を成績にしない。
- 応答回数を最大化しない。
- 人、チーム、リーダーを順位づけない。
- 心理状態や能力を推定しない。
- 最終回答までの思考時間を短縮する規則にしない。
- 途中状態がどの層で観測可能だったかだけを記録する。

この模型の `ranking` は常に「評価しない」である。
