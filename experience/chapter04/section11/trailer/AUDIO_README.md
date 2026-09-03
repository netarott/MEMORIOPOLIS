# Section 11 Audio Builder

## 音響FIX仕様

- 通知A：乾いた2音．
- 通知B：通知Aとほぼ同じ2音＋短い銀白色の余韻．
- 古地層：地下鉄そのものではなく，都市の下を走り続ける低い振動と不規則な継ぎ目．
- 同一性：所在を持たない微かな風と，似ているが同一ではない二滴の雫．
- 16.46秒付近：多関節の指が止まる前の短い音響上の空白．
- 終端：解決和音を置かず，細い経路音を画面外へ残す．

すべてコードで生成するオリジナル音響であり，既存OSの通知音や録音素材は使用しません．

## 配置

```text
scripts/build_section11_shorts_audio.py
```

## 前提

無音絵コンテが生成済みであること．

```text
experience/chapter04/section11/trailer/output/
└─ section11_trailer_ja_storyboard.mp4
```

## 実行

リポジトリのルートで実行します．

```powershell
python scripts/build_section11_shorts_audio.py
```

## 出力

```text
experience/chapter04/section11/trailer/output/
├─ section11_trailer_ja_soundscape.wav
└─ section11_trailer_ja_fix_candidate.mp4
```

## FIX判定

スピーカーとイヤホンで一度ずつ通して確認します．次のみ修正対象とします．

- 文字が切れている．
- CTAが読めない．
- 通知Aまたは通知Bが聞こえない．
- 音割れ，急激な音量跳躍，無音欠落がある．
- 動画が途中で停止する．

わずかな画面のズレ，周期の不一致，クロスフェードの癖は，意味を壊さない限り記憶に残る継ぎ目として許容します．
