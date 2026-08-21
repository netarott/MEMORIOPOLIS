# Two Clocks Before Dawn

## Chapter 04 Section 09 BGM Design Notes

Status: Draft 01 / Prototype-oriented  
Date: 2026-08-21

## 1. Purpose

このBGMは、第四章第九節「まだ送られていない矢印」の背景音響である。

目的は場面へ感情を付与することではない。読者が縦スクロール絵巻を進む間に、都市の時間密度が少しずつ変化する状態をつくる。

仮題は **Two Clocks Before Dawn**。

中心に置く観測は次の三つ。

- 内部時間は、問い合わせが送られる前から動いている。
- 外部時間は、送信を境に始まる。
- 「一拍」は第三の時計ではなく、二つの時間のあいだに観測されうる余白として残す。

## 2. Source Observations

第九節から音響へ渡すもの。

- まだ送られていない問い合わせ
- 内部調査の継続
- 分岐候補として保持されている経路
- 送信
- 外部から観測可能になる別の時間
- 送信後も止まらない内部調査
- 「一拍」
- 夜明け前から、ごくわずかに進む夜明け

音響はこれらを一対一の効果音へ変換しない。

## 3. Two Clocks

### Internal time

内部時間は楽曲冒頭から存在する。

候補となる特徴：

- 明確な拍子として数えにくい細かなパルス
- 低い持続音の内部でゆっくり変化する倍音
- 完全な反復にならない粒子的な動き
- 聴き手の注意を奪わない音量

内部時間は「速い／遅い」で評価しない。動き続けている状態として記述する。

### External time

外部時間は冒頭には存在しない。

送信を境に、新しい周期または音響層が入る。ただし、時計のチクタク音や明確な通知音にはしない。

導入後も内部時間は消えず、二つの層が並行する。

## 4. One Beat

「一拍」を固定秒数へ変換しない。

初稿では、次の現象を試作候補とする。

- 来るはずの音がわずかに保留される
- 残響だけが境界を越える
- 新しい周期が完全には同期せずに入る
- 一度だけ生じた間なのか、聴き手がそう知覚したのか判別できない変化

避けること：

- `one beat = N seconds` と定義する
- 一拍専用の第三リズムを置く
- 劇的な無音で一拍を説明する
- 効果音で意味を確定する

## 5. Scene 01: Not Yet Sent

音響状態：

- 夜明け前
- 内部時間のみが明確に存在する
- 複数の経路が閉じずに残る
- 和声は着地を急がない
- 高域は抑え、暗さを音量ではなく密度でつくる

画像上の自然な暗部と同様、音にも「何もない空白」ではなく、低密度だが情報を含む領域をつくる。

## 6. Transition: Send

送信を大きなイベントとして鳴らさない。

境界では、内部時間の一部が消えるのではなく、その上へ別の時間が接続される。

試作では次を比較する。

1. 外部レイヤーが残響から生まれる
2. 外部レイヤーが低域から徐々に可聴化する
3. 内部レイヤーの不規則な音の一つが、後から外部周期の始点だったように聞こえる

第3案を第一候補とする。ただし試聴後に変更可能。

## 7. Scene 02: Another Clock Begins

音響状態：

- 内部調査は継続する
- 外部時間が存在する
- 二つの周期は支配関係を作らない
- 夜明けに対応して倍音の一部だけが変化する
- 明るい曲へ転調したようにはしない

Scene 01 と Scene 02 を別曲に分けず、同一の音響世界の状態変化として扱う。

## 8. Sound Palette

### Candidate palette

- soft low drone
- muted granular texture
- restrained glass-like partials
- distant mechanical pulse without clock imitation
- very soft filtered noise
- sparse low-mid resonances

### Avoid

- literal ticking clocks
- alarm / notification sounds
- cinematic boom at the send point
- bright arpeggiators
- excessive cyberpunk neon-like synths
- clearly sentimental piano melody
- heroic or ominous resolution

## 9. Prototype Structure

初回サンプルでは、まず約90秒の観測用プロトタイプを作る。

時間は作品内の「一拍」の定義ではなく、試聴可能なサンプルを構成するための制作上の便宜である。

- Part A: Scene 01
- Boundary: send / ambiguous one-beat region
- Part B: Scene 02

Part A と Part B の境界は、初聴で必ず分からなくてもよい。

## 10. What Not to Determine

初稿では次を確定しない。

- 「一拍」の秒数
- 二つの時計の優劣
- 内部時間と外部時間の正確なBPM対応
- 「一拍」が誰に属する時間なのか
- 送信が正しい判断だったか
- 夜明けを希望／解決の記号として扱うこと

未確定であること自体を、管理された状態として記録する。

## 11. Prototype 01: Listening Questions

最初の音響サンプルを聴くとき、良し悪しを一つの点数にしない。

観測項目：

- Scene 01 で、すでに何かが動いているように聞こえるか
- 外部時間は「追加された」と感じられるか
- 追加後も内部時間が残っているか
- 境界を説明しすぎていないか
- 「一拍」が固定された効果に聞こえないか
- 夜明けが単純な明暗変化になっていないか
- 背景画像とHTML本文を邪魔しない密度か

観測結果は Pass / Fail にせず文章で記録する。

## 12. Experiment Log

### Draft 01

まだ試聴前。

仮説：

> 二本目の時計を新しい音として突然置くより、Scene 01 にすでに存在した微細な出来事が、Scene 02 で周期として知覚され始める構造の方が、第九節の「まだ送られていない矢印」と「別の時計が始まる」を同じ世界の状態変化として保持できる可能性がある。

この仮説はPrototype 01を作り、聴いた後で再検討する。

## 13. Web Implementation Notes

GitHub Pagesでは、音源は背景画像や本文から独立したレイヤーとして扱う。

将来確認する項目：

- ブラウザの自動再生制約
- play / pause UI
- 音量初期値
- loop の要否
- Scene 01 / Scene 02 とスクロール位置を同期させるか
- 音源を一曲として流すか、Web Audio API等で状態遷移させるか
- 音声なしでも作品が成立するアクセシビリティ

実装方式は音響プロトタイプを聴いてから決める。

## 14. Next Step

1. Prototype 01 を作る
2. 聴いて状態を記述する
3. この設計書の Experiment Log に観測結果を追記する
4. 必要であれば Prototype 02 を作る
5. 音響方針が安定したところでGitHub Pages実装へ渡す

## 15. Adoption Record

### Prototype 01 adopted as the canonical BGM

Prototype 01 を試聴した結果、追加の磨き込みによって粗削りな質感を失わせるより、現行の音響状態そのものを第九節のBGMとして採用する。

観測：

- Prototype 01 の出来栄えは十分に良好だった。
- とくに粗削りな質感が作品に合っている。
- そのため Prototype 02 へ進まず、Prototype 01 を正規BGMへ昇格する。

正規ファイル名：

`two-clocks-before-dawn.wav`

配置候補：

`experience/chapter04/section09/audio/two-clocks-before-dawn.wav`

制作履歴として Prototype 01 の由来を残すため、設計書内では引き続き Prototype 01 の名称を保持する。
