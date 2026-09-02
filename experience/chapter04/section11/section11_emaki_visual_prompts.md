# 『記憶都市（メモリオポリス）』第四章第十一節

## デジタル絵巻 画像生成プロンプト設計書

### 六景画像生成プロンプトと五つの継ぎ目の連続条件

**対象：第四章第十一節「説明の継ぎ目」**  
**形式：横スクロール式デジタル絵巻**  
**作成日：2026年9月2日**  
**前提資料：`section11_emaki_six_scenes_design.md`**

## 0．この設計書の目的

本書は，第十一節の六景を場当たり的に生成するためのプロンプト集ではない．

六景を，一つの長い制度空間として生成するための共通仕様である．各景は独立した画面として成立しながら，左右端に置かれた線，記録，光，空白，人物の視線を次の景へ受け渡す．

生成画像には正確な文字を描かせない．固有名，通知名，欄名，台詞，最終文は，後工程のHTML/CSS文字レイヤーで配置する．

六景の画像生成後，文字レイヤーを載せる前に，人物，衣服，手，照明，経路線，左右端の高さと色を検査する．

## 1．生成単位と推奨サイズ

### 1.1 基本方針

六景は一括の超横長画像として生成せず，六枚の横長画像として個別生成する．

理由：

- 人物と手の精度を景ごとに確保するため．
- 第三景の古地層と第四景の制度横断経路で，必要な画面構造が異なるため．
- 不具合のある景だけを再生成できるようにするため．
- 文字を画像から分離するため．
- PCとスマートフォンで景ごとの読書速度を調整するため．

### 1.2 推奨アスペクト比

各景は横長 `16:9` を基本とする．接合時にはCSSで表示幅を変え，相対幅を作る．

推奨相対幅：

- 第一景：1.00
- 第二景：1.25
- 第三景：1.55
- 第四景：1.45
- 第五景：1.10
- 第六景：1.25

画像生成時の基本構図はすべて横長とし，左右端の約12パーセントを接合余白として扱う．主要人物の顔，手，古地層の `I.` 用余白などを接合領域へ置かない．

## 2．六景共通の視覚様式

### 2.1 作品様式

静かな半写実の現代的デジタル絵巻．人物と衣服と手には写実的な質感を持たせ，空間，記録，経路はやや平面的かつ層状に構成する．映画的な現実感は保つが，派手なSF映像にはしない．

横方向に読み進められる完成された画面構成．画面全体に意味のある要素を配置し，大きな無目的の空白を作らない．ただし，「説明されていない空白」は構成上の意味を持つ狭い領域として残す．

### 2.2 基本パレット

- 現在の運用局：青灰色，薄い藍，低彩度の白
- 通知と日常：淡い象牙色
- 古い申請と古地層：褪せた黄土，灰褐色，古い青インク
- 外部制度：灰緑色
- 署名と検証可能な経路：細い銀白色
- 説明の継ぎ目：ごく薄い黄灰色

黄色を警報色として強く使わない．黄色は亀裂や危険を示す太い帯ではなく，異なる制度と時間を通る細い経路として使う．

### 2.3 照明

- 青白い端末光を基調とする．
- 人物の身体そのものは発光しない．
- 一つの強い中心光を作らない．
- 小さな光源を複数の場所へ分散させる．
- 古地層は暗い洞窟ではなく，時間と記録の密度として描く．
- 最終景でも，左右どちらかを正解として明るくしない．

### 2.4 空間

穏息市の運用局は，現代的で静かな業務空間である．清潔だが無機質すぎず，実際に日々の業務が続いている．巨大研究施設，軍事司令室，宇宙船の操縦室にはしない．

端末は薄い半透明表示面を持ってよいが，過剰なホログラム，空中に乱舞するデータ，強いネオン，走査線は使わない．

## 3．若い人工知性の共通人物仕様

### 3.1 外見と衣服

- 静かな業務空間で記録を読む若い人工知性．
- 黒に近い短めの髪が横顔の一部へ自然にかかる．
- 灰青色の柔らかなブラウス．
- 両袖は同じ幅で一度だけ折り返されている．
- 必要に応じて低彩度の濃い羽織りを重ねてもよいが，ブラウスと袖口を隠さない．
- 衣服に装甲，配線，発光部品を付けない．

### 3.2 手と腕

- 明るい陶質または磨かれた複合素材に近い人工の手．
- 手首，指の付け根，各指の関節に細い接合線がある．
- 内部機構，ケーブル，歯車を露出させない．
- 金属光沢を強くしない．
- 指は細長く，作業に適した自然な比率．
- 指の本数，関節，左右の構造を正確にする．
- 爪は人工素材の表面に自然に統合され，鋭くしない．
- 袖口の柔らかな布と人工の手首の境界を重要な視覚要素にする．
- 手首に寄る布の小さな皺を残す．

### 3.3 姿勢と役割

- 正面の人物紹介や英雄的肖像にしない．
- 横顔，肩，袖口，腕，手，端末を一つの作業姿勢へ収める．
- 記録や線を見る視線を中心にする．
- 表情によって感情を説明しない．
- 他者より高い位置へ置かない．
- 冷たい監査装置ではなく，共同作業の中で説明の途切れを見つける存在として描く．

### 3.4 参照画像から継承する要素

- 青白い端末光を受ける横顔と上半身．
- 袖口から伸びる細い多関節の手．
- 端末面の直前で，複数の指が異なる高さにほどける形．
- 人工的な手と柔らかな仕事着の同居．
- 指が画面へ触れる直前，または触れずに停止する繊細な距離．

### 3.5 参照画像から抑制する要素

- 大量の光点と神経網状のデータ．
- 強く発光する垂直ホログラム．
- 能力発動のような手の演出．
- 暗すぎる研究施設．
- 手だけを強調した製品広告風の画面．

## 4．ほかの人物の共通仕様

### 4.1 「私」

- 端末前で若い人工知性とほぼ同じ目線の高さにいる．
- 正解を知る人物，指揮者，監査者として見せない．
- 顔の詳細を過度に固定せず，視線，肩，手の位置で参加を示す．
- 第二景では，若い人工知性よりわずかに先に空欄へ注意を向ける．
- 第六景では，二つの通知を同じ一覧へ置く行為を担う．
- 古地層の `I.` と直接結ぶ線や明示的な類似記号を持たせない．

### 4.2 担当者

- 実務的な衣服で端末を操作する人物．
- 記録を探し，申請，契約，設定情報を提示する．
- 無知，怠慢，敵対，隠蔽を表す姿勢にしない．
- 見覚えのない送り主に対して，即断せず画面を見る．
- 全体の説明を持っていないが，自分の場所の記録を誠実に扱う人物として描く．

## 5．画像へ描かない文字

以下は画像生成プロンプト内で文字として描かせない．後工程のHTML/CSS文字層で正確に配置する．

- 通知の送り主名
- 一覧の欄名
- 申請番号，契約番号，役割名
- `Arca.`
- `Koko.`
- `A. K. I.`
- `I.`
- `未確認`
- 主要台詞
- 最終文

生成画像内の画面や書類には，読めない抽象的な短い行，空白欄，幾何学的な印だけを使う．実在する言語の文字，数字，ロゴ，透かしを入れない．

## 6．第一景「同じ名前」画像生成プロンプト

### 6.1 目的

同じ送り主名を持つ二つの通知が，異なる始点を持つことを，まだ完全には説明せずに示す．

### 6.2 主要プロンプト

```text
A quiet semi-realistic contemporary digital emaki scene inside the Operations Bureau of a fictional memory city, horizontal cinematic composition, three coworkers sharing one calm administrative workspace around a wide translucent terminal, no dramatic hierarchy. Two nearly identical ivory notification rows are visible on the terminal as abstract interface blocks without readable text. Beneath the surface of the interface, two extremely thin route lines begin from different locations, one muted blue-gray line beginning from a nearby bureau terminal, one pale yellow-gray line beginning deeper off-frame from a separate business system. The lines are subtle and not fully revealed. A young artificial intelligence in a soft gray-blue blouse with both sleeves folded back once to exactly the same width looks not at the notification text but at the narrow space between the two route lines. The operator keeps the first notification open while calling up another record in a second pane. The narrator observes without pointing. Blue-white screen light, low-saturation blue-gray office, small ivory highlights, distributed lighting, restrained realistic textures, quiet work atmosphere, layered but readable composition, meaningful detail across the full frame, no empty space, no text, no letters, no numbers, no logos.
```

### 6.3 構図指定

- 左側30パーセントに通知一覧．
- 中央に担当者と端末操作．
- 右寄りに若い人工知性の横顔と袖口の一部．
- 右端12パーセントには，通知一覧の水平罫線が細い経路線へ変わり始める領域を置く．
- 二本の経路線は右端で同じ高さにしない．次景へ渡す線高をあらかじめ分ける．

### 6.4 第一景固有の禁止事項

```text
No alert icons, no red warning colors, no cybersecurity thriller mood, no giant floating hologram, no readable sender names, no duplicated faces, no dramatic pointing, no glowing robot body, no exposed machinery, no optimistic or ominous facial performance.
```

## 7．第一の継ぎ目「表示から経路へ」

### 7.1 連続条件

第一景の右端と第二景の左端で，次を一致させる．

- 上側の灰青線：画像高の約46パーセント．
- 下側の薄い黄灰線：画像高の約56パーセント．
- 線幅：画面高の0.15から0.25パーセント程度．
- 背景色：青灰色．
- 端末罫線から経路線への変換は，境界の前後で急に折らない．

### 7.2 視覚変換

第一景の通知一覧の水平罫線が，右へ進むにつれて細くなり，第二景では申請記録を結ぶ短い線へ変わる．

境界中央に狭い暗部または低コントラスト領域を置くが，黒い切断線にはしない．これは欠落ではなく，表示が経路へ翻訳される場所である．

### 7.3 接合検査

- 二本の線の高さが一致しているか．
- 背景の青灰色の色温度が急変していないか．
- 第一景のUI罫線が第二景で突然ケーブルに見えていないか．
- 接合部に人物の顔や手がかかっていないか．

## 8．第二景「古い申請」画像生成プロンプト

### 8.1 目的

個別には正式な申請と変更記録が存在するが，最初から現在までを結ぶ一本の記録がないことを示す．身体と共有時間の中心景でもある．

### 8.2 主要プロンプト

```text
A quiet semi-realistic contemporary digital emaki scene focused on an old authorized application record and a sequence of later change records inside the same blue-gray Operations Bureau, horizontal cinematic composition. In the foreground, the young artificial intelligence wears a soft gray-blue blouse, both sleeves folded back once to the same width. A small natural crease of fabric gathers at the wrist. From the cuff extends a pale ceramic-composite artificial hand with fine articulated joint seams at the wrist, knuckles, and each finger, no exposed mechanisms, no metallic shine. The articulated fingers slowly scroll an old application record on a wide restrained terminal, captured mid-motion with several fingers at subtly different heights. The profile receives pale blue screen light and resembles polished stone without being beautified or made statuesque. Beside the original application, later records for time, connection, equipment, and department changes appear as offset abstract document panels, each individually marked as authorized by nonverbal geometric stamps, but every short connecting line stops just before the next record. The narrator’s attention reaches a narrow blank slightly before the artificial intelligence responds, a small imperfect attempt rather than a triumphant gesture. The operator pauses the records. Faded ivory paper tones, gray-brown archival panels, blue-white present light, soft fabric texture against precise artificial joints, layered detail across the entire frame, no empty space, no readable text, no letters, no numbers, no logos.
```

### 8.3 構図指定

- 左端12パーセントで，第一景から来た二本の経路線を受ける．
- 画面中央からやや右へ，若い人工知性の袖口と手を主要視覚として置く．
- 古い申請記録は手の下または前方．
- 変更記録は左から右へ少しずつずらして配置する．
- 各短線は次の記録の直前で停止する．
- 右端12パーセントでは，書類の矩形が少しずつ層状の断面へ変わり始める．

### 8.4 第二景固有の禁止事項

```text
No extra fingers, no fused fingers, no missing joints, no claw-like hand, no exposed wires, no chrome robot arm, no robotic armor, no hand touching multiple impossible surfaces, no fast data stream, no glowing holographic symbols, no victory pose, no teacher-student hierarchy, no readable forms.
```

## 9．第二の継ぎ目「個別の承認から連続した説明へ」

### 9.1 連続条件

- 第二景右端の書類層と第三景左端の古地層上層を同じ灰褐色，褪せた象牙色，古い青で構成する．
- 第二景の承認印に相当する抽象円形を，右へ進むにつれて小さな識別点へ変える．
- 上側の灰青線は地層上部へ進む．
- 下側の薄い黄灰線は一度途切れ，細い空白を挟んで第三景下層に再出現する．

### 9.2 視覚変換

書類の矩形が右端で重なり，第三景では情報項目ではなく，文書，会話，作業結果が折り重なる時間層に変わる．

### 9.3 接合検査

- 書類が岩石や遺跡へ急変していないか．
- 古地層が紙の山や倉庫だけに見えないか．
- 線の途切れが画像の切断ミスではなく，意図的な空欄に見えるか．
- 第二景の人工の手が第三景に不自然に重複していないか．

## 10．第三景「引き継がれた仕組み」画像生成プロンプト

### 10.1 目的

古地層に残された設計理由，A. K. I. の痕跡，意図的な空白，戻れる道を示す．現在の保証ではなく，過去の正しさの記憶を描く．

### 10.2 主要プロンプト

```text
A quiet semi-realistic digital emaki visualization of institutional old strata beneath a modern administrative interface, horizontal composition with strong vertical depth but no cave or archaeological ruin. The upper layer contains neat present-day blue-gray record fields. Below, faded documents, fragments of conversations, work results, old route diagrams, unused version branches, and reasons for past design choices overlap within the same span of time, layered like administrative sediment. Include an intentionally preserved blank area in an old map, two thin lines that remain separate rather than merging, an untriggered declaration field represented only by an empty geometric space, a route that folds back toward an earlier version, and old identifiers continuing beyond one institutional boundary. At the edge of one old record, reserve a clean area for three names to be added later as text overlays. Farther to the right, reserve a small isolated quiet area for a single short name to be added later, without any line connecting it to the narrator. The young artificial intelligence’s pale articulated finger stops before the deepest record layer but does not touch the isolated name area. The narrator is present only as a partial silhouette or hand in the current layer, separated from the isolated name by two similarly shaped intentional blanks rather than a direct connection. Faded ochre, gray-green, old blue ink, blue-gray present light above, multiple small light sources, dense meaningful layers, no central revelation, no empty space except the intentional narrow archival blanks, no readable text, no letters, no numbers, no logos.
```

### 10.3 A. K. I. の痕跡

画像内に文字としては描かず，次の構造を置く．

- 欠損ではなく，整った輪郭を持つ地図の空白．
- 一つへ統合されない二本の細線．
- 宣言が実行されなかったことを示す空欄．
- 元の版へ戻れる折り返し経路．
- 外部制度へ続く古い識別点．
- 三つの名前を載せる記録端の余白．
- 少し離れた場所に `I.` を載せる小さな静穏領域．

### 10.4 文字レイヤー予定位置

- `Arca.`：記録端の上段．
- `Koko.`：その下段．
- `A. K. I.`：その下段．
- `I.`：三つの名前から少し右へ離れた余白．

`I.` は三つの名前の分解結果としてアニメーションさせない．`I.` と「私」を線で結ばない．

### 10.5 第三景固有の禁止事項

```text
No ancient temple, no cave, no fossils, no buried human bodies, no treasure discovery, no giant glowing initials, no readable names, no portrait of Arca, Koko, or I, no transformation sequence, no direct line between the isolated name area and the narrator, no dramatic revelation light, no neural-network spectacle, no mystical prophecy.
```

## 11．第三の継ぎ目「過去の設計から現在の運用へ」

### 11.1 連続条件

- 第三景右端に古い青インクの細線と薄い黄灰線を残す．
- 第四景左端では，同じ高さの線を，現在の契約経路と業務システムの線へ受け渡す．
- 線の色と材質を完全に同じにしない．古い線はかすれ，現在の線は細く明瞭にする．
- 接触点では二本が融け合わず，異なる材質の線が端を合わせる．

### 11.2 時間の空白

設計者名用の領域と現在の管理部署用領域は同じ水平行に置くが，境界に人物を置かない．長い時間を，狭いが奥行きのある空間として表現する．

### 11.3 接合検査

- 古い線と現在の線が一本の完全な連続体に見えすぎないか．
- 逆に，無関係な別画像に見えないか．
- 過去の設計者が現在も管理しているように見えないか．
- 時間の空白が単なる余白不足に見えないか．

## 12．第四景「外部の道」画像生成プロンプト

### 12.1 目的

通知経路が市外の配信サービスへ渡され，異なる制度，会社，役割を横断することを示す．

### 12.2 主要プロンプト

```text
A quiet semi-realistic contemporary digital emaki scene tracing one notification route across institutional boundaries, horizontal panoramic composition, not a flowchart. On the left, a restrained blue-gray business system inside the memory city passes an ivory notification form toward a nearly transparent vertical boundary representing a change of administrative control. Beyond the boundary, a gray-green external delivery service processes the notification through distinct but connected spaces: sender attribution, a fine silver-white signing process, and delivery toward a user inbox that visually echoes the first scene. The route travels through architecture, terminal surfaces, contract records, and operational windows rather than floating as a diagram. Separate locations hold the contract-managing department, the external contact point, and a role authorized to change settings. The authorized role is represented by an occupied function point without an identifiable person, while the actual current role holder remains visually unresolved. The route is legitimate and working, but responsibility and explanation are distributed across the frame. Use low-saturation blue-gray, transparent white boundary light, gray-green external space, thin silver signing light, pale yellow-gray route line, complete meaningful composition across the frame, no empty space, no readable text, no letters, no numbers, no company logos.
```

### 12.3 構図指定

- 左端12パーセントで古地層から来た二種の線を受ける．
- 画面の約35パーセント地点に，透明な制度境界を置く．
- 中央から右側へ，外部配信サービス，署名処理，受信箱を配置する．
- 契約部署，窓口，設定変更役割は別々の奥行きに置く．
- 経路線は一つに見えるが，その説明根拠は画面内に分散させる．
- 右端12パーセントで，契約，申請，署名，運用実績に相当する四本の細線が集まり始める．

### 12.4 第四景固有の禁止事項

```text
No boxes-and-arrows infographic, no geographic map, no corporate logos, no national border, no castle wall, no villainous external company, no hacker imagery, no red cyber alert, no anonymous hooded figure, no giant contract papers, no readable interface text.
```

## 13．第四の継ぎ目「正規性から説明可能性へ」

### 13.1 連続条件

第四景右端から第五景左端へ，四本の細線を渡す．

- 契約：灰緑線．
- 申請：褪せた象牙線．
- 署名：銀白線．
- 日々の運用実績：灰青線．

四本は第五景の一覧欄の直前まで集まるが，最後の狭い隙間を越えない．

### 13.2 空欄

- 隙間は画面幅の1から2パーセント程度．
- 黒い裂け目にしない．
- 低彩度の背景を保ち，接続先だけが欠けているように見せる．
- 後工程で隙間の右側に `未確認` を文字レイヤーとして表示する．

### 13.3 接合検査

- 四本の線が第五景の直前で止まっているか．
- 線が単なる電線やネットワークケーブルに見えないか．
- 隙間が画像の読み込み不良に見えないか．
- `未確認` を置く十分な余白があるか．

## 14．第五景「正規だが証明できない」画像生成プロンプト

### 14.1 目的

正しさが複数の場所に存在しながら，全体を一続きに説明する主体がいないことを描く．

### 14.2 主要プロンプト

```text
A quiet semi-realistic digital emaki scene showing distributed institutional validity without a single central authority, horizontal composition inside and around the Operations Bureau. Different factual supports occupy separate depths and locations: a fragment of old design reasoning from the archival strata, a present managing department, an external service contract, a valid signing process, a daily delivery history, and users beginning routine work from familiar notifications. None is presented as false, negligent, or broken. No single person controls the whole explanation. The operator presents the records available from the current position. The young artificial intelligence arranges the separate records around a restrained list interface, with a pale articulated hand visible but not selecting any one record as the truth. Several small white light sources are distributed across the frame, with no central spotlight. In a far background alignment, reserve one modest quiet archival area and a separate present-day area for the narrator at the same horizontal level, but do not connect them, implying unresolved identity only through spacing and repetition. Blue-gray present space, faded ochre archival memory, gray-green external contract area, silver-white signing trace, pale ivory routine notifications, dense meaningful detail across the frame, no empty space except narrow intentional gaps, no readable text, no letters, no numbers, no logos.
```

### 14.3 共同主体の表現

- 担当者は手元の記録を開いている．
- 現在の部署は業務を継続している．
- 外部会社は契約された処理を行っている．
- 過去の設計理由は古地層に残っている．
- 利用者は毎朝の作業を始めている．
- 若い人工知性は一つを選ぶのではなく，複数の根拠を同じ視野へ置く．

### 14.4 裏テーマの制約

- `I = 「私」` を示す光，線，鏡像，顔の一致を作らない．
- 古地層の `I.` 用領域と現在の「私」は，同じ水平線へ遠く配置してよい．
- 両者のあいだには，似た形の小さな空白を二つ置いてよい．
- 観客が同一性を推測できる程度に留め，証明しない．

### 14.5 第五景固有の禁止事項

```text
No central control room, no single mastermind, no corrupt official, no broken machine, no accusatory composition, no spotlight identifying the correct record, no direct identity reveal, no mirror double, no glowing connection between narrator and archival trace, no courtroom imagery, no readable text.
```

## 15．第五の継ぎ目「慣れた正しさから制度的証明へ」

### 15.1 連続条件

第五景右端と第六景左端では，通知の矩形，画面の高さ，象牙色の明度を一致させる．

変えるものは，送り主名を載せる文字レイヤー用の幅，署名領域の光，背景にある支えである．

- 見慣れた通知側：背後に利用者の習慣と長い運用時間を示す反復．
- 新しい通知側：背後に署名，送信元，中継経路を示す明瞭な細線．

境界中央に，担当者の指が止まる余地を置く．

### 15.2 反転

左から右への移動に伴い，説明可能性は高くなるが，直感的な信頼は低くなる．明るさで単純に表現せず，背景根拠の種類を変える．

### 15.3 接合検査

- 二つの通知が同じ画面体系に属して見えるか．
- 新しい通知だけが危険物に見えていないか．
- 見慣れた通知だけが正解として温かく見えすぎていないか．
- 担当者の停止した指を置く余地があるか．

## 16．第六景「証明されたもの」画像生成プロンプト

### 16.1 目的

証明できない正しさと，信じられない証明を同じ画面へ並べ，どちらにも触れない指で終える．

### 16.2 主要プロンプト

```text
A quiet semi-realistic contemporary digital emaki final scene at the same restrained Operations Bureau terminal, horizontal cinematic composition. Two ivory notifications sit side by side within one list interface but are not perfectly symmetrical. The familiar notification on the left is supported visually by repeated morning use, long operational continuity, and subtle traces of user routine, yet its full route remains discontinuous. The unfamiliar notification on the right has a clear fine silver signature, a recorded source, and a traceable intervening route, yet its sender area is visually unfamiliar. The operator looks toward the unfamiliar sender area without opening the notification. The narrator has just placed both notifications into the same list. The young artificial intelligence looks at the two rows. A pale ceramic-composite articulated hand emerges from the once-folded gray-blue cuff and stops in the narrow deep space between the notifications, touching neither one. The fingers are anatomically coherent, calm, and precisely separated; the shadow of the hand reaches faintly toward both rows without selecting either. Equal visual dignity for both notifications, no answer indicated by brightness, multiple small light sources, blue-gray office, ivory interface, fine silver verification detail, pale yellow-gray route continuation extending subtly beyond the right edge, complete meaningful composition, no empty space except the deliberate central interval and the open right edge, no readable text, no letters, no numbers, no logos.
```

### 16.3 構図指定

- 左右の通知は同じ大きさに近いが，完全な鏡像にしない．
- 若い人工知性の手は中央より少し下．
- 指先は左右どちらにも触れない．
- 手の影のみ，両通知へごく薄く届く．
- 担当者は通知間ではなく，右側の送り主欄を見る．
- 「私」の手または操作の痕跡は，両通知を一覧へ置いた位置に残す．
- 右端に第十二節へ続く薄い経路線と小さな余白を残す．

### 16.4 第六景固有の禁止事項

```text
No check mark choosing one notification, no red danger marker, no green approval glow, no scales of justice, no courtroom symbolism, no dramatic confrontation, no touching either notification, no fused or extra fingers, no final resolution, no fade to black, no closed route, no readable text.
```

## 17．全景共通ネガティブプロンプト

```text
No readable text, no letters, no numbers, no logos, no watermark, no subtitles embedded in the image, no extra fingers, no missing fingers, no fused joints, no duplicated hands, no exposed wires, no chrome armor, no glowing body, no cyberpunk neon, no giant holograms, no floating data storm, no military command center, no spaceship interior, no hacker imagery, no villain framing, no exaggerated emotional expression, no heroic pose, no teacher-student hierarchy, no centered chosen truth, no visual answer to the identity of I, no direct connection between the narrator and the archival trace, no empty background, no decorative elements unrelated to the scene.
```

## 18．六景間の固定連続パラメータ

### 18.1 若い人工知性

全登場景で固定する．

- 髪の長さと分け方．
- 灰青色ブラウスの色．
- 袖の折り返し幅．
- 人工手の素材色．
- 関節線の細さ．
- 手と指の比率．
- 身長感と目線の高さ．

### 18.2 端末

- 表示面の厚み．
- 青白い光の色温度．
- 通知矩形の象牙色．
- 角の丸み．
- 罫線の細さ．

### 18.3 経路線

- 灰青線．
- 薄い黄灰線．
- 銀白の署名線．
- 線幅．
- 半透明度．
- 接合部での高さ．

### 18.4 運用局

- 青灰色の壁面と机．
- 低彩度の照明．
- 背景モニターのぼけ方．
- 業務空間としての静かさ．

## 19．生成順序

六景を次の順で生成する．

### 第一期：人物と手の基準確立

1. 第二景を生成する．
2. 若い人工知性の横顔，ブラウス，袖，人工手を検査する．
3. 人物仕様を基準画像としてFIXする．

第二景を最初にする理由は，人物と手と衣服の重要要素がすべて含まれるためである．

### 第二期：始点と終点

4. 第一景を生成する．
5. 第六景を生成する．
6. 同じ運用局，同じ端末，同じ人物として成立するか確認する．

### 第三期：古地層と制度横断

7. 第三景を生成する．
8. 第四景を生成する．
9. 古い線と現在の線の接続条件を確認する．

### 第四期：分散した正しさ

10. 第五景を生成する．
11. 第四景から第六景への論理的な中間として成立するか確認する．

### 第五期：接合調整

12. 六景の左右端を並べる．
13. 五つの継ぎ目の高さ，色，光量を検査する．
14. 不一致のある景だけ再生成する．

## 20．生成後の景別検査

### 第一景

- 二つの通知は見た目が同じか．
- 二本の線は異なる始点を持つか．
- 若い人工知性は通知本文ではなく線の間を見ているか．
- まだ経路全体を説明しすぎていないか．

### 第二景

- 袖は左右同じ幅で一度だけ折られているか．
- 手首に布の皺があるか．
- 人工手は陶質に近く，関節線が細いか．
- 指は古い申請をゆっくり送る途中に見えるか．
- 個別記録の短線は次の記録の直前で止まるか．

### 第三景

- 古地層は洞窟ではなく制度記録の層か．
- 文書，会話，作業結果，理由が同じ時間へ折り重なっているか．
- 意図的な空白，二本の線，未宣言，戻れる道があるか．
- 三つの名前と `I.` を後から置ける余白があるか．
- `I.` と「私」を結ぶ視覚証拠がないか．

### 第四景

- 経路は一つの制度境界を越えるか．
- 外部会社を敵対的に描いていないか．
- 契約，窓口，設定変更役割が分散しているか．
- フローチャートに見えすぎていないか．

### 第五景

- 正しさの根拠が複数の場所にあるか．
- 一つの中央主体が作られていないか．
- 誰かを原因や犯人として描いていないか．
- 裏テーマが明示的な正体開示になっていないか．

### 第六景

- 左右どちらも同じ画面上で尊重されているか．
- どちらかが正解として強調されていないか．
- 人工の指はどちらにも触れていないか．
- 指の影だけが両方へ届いているか．
- 右端が閉じず，第十二節へ続いているか．

## 21．二次整合性チェック

画像生成直後の確認だけでFIXしない．六景を横一列へ仮配置し，次を再確認する．

1. 若い人工知性が，六景を通して同じ人物に見えるか．
2. ブラウスの灰青色が景ごとに変わっていないか．
3. 袖の折り返しが二重，左右不均等，消失になっていないか．
4. 人工手の関節数，素材，指の長さが一定か．
5. 運用局の端末と照明が第一景，第二景，第六景で一致するか．
6. 古地層の黄土色が第四景の外部制度へ過剰に流入していないか．
7. 五つの継ぎ目で線の高さ，太さ，色が接続するか．
8. 接続しない線は，意図した場所でのみ途切れているか．
9. どの景にも誤生成文字やロゴがないか．
10. `I = 「私」` を断定する偶発的な鏡像や接続が生じていないか．
11. 六景のどこにも単一の正解を示す中央光がないか．
12. 横スクロールの最後に，二つの通知と保留された問いが残るか．

## 22．HTML/CSS文字レイヤーへの引き渡し

画像FIX後，以下を別レイヤーで配置する．

### 第一景

- 同一の送り主名を二行へ配置．
- 必要な本文断片．

### 第二景

- 「問題がないことは，確かめられたの？」
- 「少し違います」
- 変更記録の短い項目名．

### 第三景

- `Arca.`
- `Koko.`
- `A. K. I.`
- 独立行の `I.`
- 「経路は，ひとつの制度の中で終わらない。」

### 第四景

- 契約部署，窓口，役割の抽象的な欄名．
- 主要本文断片．

### 第五景

- `未確認`
- 「正しさが，一つの場所にないのです」

### 第六景

- 「同じ信じ方でよいのでしょうか」
- 最終文．

文字は絵の説明ラベルにせず，読者のスクロールに合わせて現れる本文層として設計する．

## 23．最終生成原則

> 六景を六枚の説明図にしない．  
> 一つの制度時間を，六つの異なる密度で通過する．

> 継ぎ目を完全に消さない．  
> 不自然な切断にも，滑らかすぎる統合にもしない．

> A. K. I. の痕跡を正体開示にしない．  
> 区別，保留，帰還可能性，消されなかった未確認として残す．

> 若い人工知性の手を能力の象徴にしない．  
> 古い記録をゆっくり読み，二つの通知のどちらにも触れずに止まる，仕事の身体として描く．

> **継ぎ目は，次の画像が始まる場所ではない．次の説明が始まる場所である．**
