# MEMORIOPOLIS / JANUS-13 完璧版引き継ぎ書

**更新日：2026年9月20日**  
**次の制作言語：ブラジル・ポルトガル語**  
**基準：Português do Brasil / Windows `pt-BR` / Anki `pt_BR`**

---

## 0．プロジェクトの現在地

```text
正式名称：JANUS-13
言語数：13言語
観測面：14面
日本語：一言語として数え、近代面と現代面を持つ
現在完了：スペイン語、第9言語・第10観測面
次工程：ブラジル・ポルトガル語、第10言語・第11観測面
```

13言語：

```text
1. 日本語
2. 韓国語
3. ロシア語
4. 臺灣華語
5. 英語
6. フィリピン語
7. インドネシア語
8. ベトナム語
9. スペイン語
10. ポルトガル語
11. イタリア語
12. フランス語
13. ドイツ語
```

14観測面：

```text
日本語・近代面
日本語・現代面
韓国語
ロシア語
臺灣華語
英語
フィリピン語
インドネシア語
ベトナム語
スペイン語
ブラジル・ポルトガル語
イタリア語
フランス語
ドイツ語
```

---

## 1．正本と制作循環

```text
日本語正本
↓
各言語のNovel
↓
新出Conceptを抽出
↓
JANUS-13型Ankiカード
↓
親デッキMEMORIOPOLISで横断学習
↓
文字・音・文法・知覚上の発見
↓
制作ノート
↓
カードと次のNovelを改修
```

```text
歴史は、制作ノートに残す。
座標は、Concept Registryで守る。
縁は、Ankiで反復する。
交配は、Novelで起こす。
```

---

## 2．Core番号と共通Concept

```text
Core10：第四章第十二節、C0001～C0010
Core20：第四章第十三節、C0011～C0020
Core30：序章、C0021～C0030
```

```text
C0001  記録
C0002  記憶
C0003  都市
C0004  通知
C0005  返信
C0006  宛先
C0007  署名
C0008  検証
C0009  権限
C0010  役割
```

---

## 3．現在のデッキと次のデッキ

```text
MEMORIOPOLIS
├─ English
├─ Filipino
├─ Indonesian
├─ Korean
├─ ModernJapanese
├─ Russian
├─ Spanish
├─ TaiwaneseMandarin
└─ Vietnamese
```

次に追加：

```text
MEMORIOPOLIS::Portuguese
```

```text
ノートタイプ：MEMORIOPOLIS Portuguese Vocabulary
タグ：memoriopolis::pt_br::core10
```

---

## 4．18フィールド標準

```text
1  ID
2  TargetLanguage
3  Pronunciation
4  Japanese
5  PartOfSpeech
6  UsageNote
7  ExampleTargetLanguage
8  ExampleJapanese
9  Root
10 Affixes
11 PerceptualSegmentation
12 MorphologicalBreakdown
13 ExampleBreakdown
14 ExampleExplanation
15 MeaningBridge
16 SoundBridge
17 Source
18 CourseTags
```

ブラジル・ポルトガル語：

```text
2  Portuguese
7  ExamplePortuguese
```

例文解説は、初学者が「なぜこの日本語訳になるのか」を理解できる長さと平易さを優先する。

---

## 5．Daily Training最終設定

```text
名前：MEMORIOPOLIS Daily Training
```

第1フィルター：

```text
deck:MEMORIOPOLIS is:due
上限：50
順序：忘れている可能性が高い順
```

第2フィルター：

```text
deck:MEMORIOPOLIS is:new
上限：10
順序：追加順
```

```text
回答に基づいて復習予定を組み直す：オン
2つ目の絞り込み：オン
空でも作成・更新：オフ
```

スペイン語導入時に10枚だけ収集された理由：

```text
他言語の新規カードはすでに学習済み
他言語の本日期限カードは親デッキで先に復習済み
スペイン語10枚だけがis:new
```

したがって正常動作。

---

## 6．FSRSと通常デッキ

```text
FSRS：オン
目標保持率：90%
一括再スケジュール：オフ
最適化：まだ実行しない
```

```text
新規カード上限：10
復習上限：200
学習ステップ：1m 10m
再学習ステップ：10m
定着しにくいカード：忘却8回、タグのみ
関連カード分離：3項目オン
音声自動再生：有効
```

回答基準：

```text
もう一度：思い出せなかった
難しい：正解したが大きく迷った
普通：適度な負荷で正解した
簡単：文字・音・意味が即座につながった
```

---

## 7．スペイン語の確定記録

```text
基準：スペインのスペイン語
Windows：es-ES
Anki：es_ES
デッキ：MEMORIOPOLIS::Spanish
ノートタイプ：MEMORIOPOLIS Spanish Vocabulary
```

```text
ZIP：MEMORIOPOLIS_Spanish_Core10_draft01_18fields_2026-09-20.zip
Novel：section12_es_draft01.md
Core10：完成・導入・学習完了
```

```text
C0001 registro
C0002 memoria
C0003 ciudad
C0004 notificación
C0005 respuesta
C0006 destinatario
C0007 firma
C0008 verificación
C0009 permiso
C0010 rol
```

利用者の観測：スペイン語は英語と音が似ている部分があり、比較的すんなり学習を完了できた。

---

## 8．ブラジル・ポルトガル語の確定方針

```text
基準変種：Português do Brasil
Windows：pt-BR
Anki：pt_BR
```

採用理由：

```text
日本からブラジルへの移民
ブラジルの日系社会
日本への還流
日本国内のポルトガル語との接触
現在の日伯関係
BRICS
```

ポルトガルとの次の歴史は捨てず、制作ノートの歴史層へ置く。

```text
種子島への火縄銃伝来
南蛮貿易
キリスト教
ポルトガル語由来の外来語
```

```text
正面：ブラジル・ポルトガル語
比較層：ヨーロッパ・ポルトガル語
歴史層：日本とポルトガルの接触史
```

TTS：

```html
{{tts pt_BR:Portuguese}}
```

```html
{{tts pt_BR:ExamplePortuguese}}
```

---

## 9．Windows pt-BR環境

2026年9月20日夕方：

```text
Language.Basic~~~pt-BR~0.0.1.0
→ 導入処理を実施

Language.TextToSpeech~~~pt-BR~0.0.1.0
→ インストール中
```

PowerShellプロンプト復帰後に確認：

```powershell
Get-WindowsCapability -Online |
Where-Object {
    $_.Name -match '^Language\..*~~~pt-BR~'
} |
Select-Object Name, State
```

期待値：

```text
Language.Basic~~~pt-BR~0.0.1.0          Installed
Language.TextToSpeech~~~pt-BR~0.0.1.0   Installed
```

インストール中は再実行しない。Ctrl+Cを押さず、管理者VS Codeを閉じず、スリープ・Wi-Fi切断を避ける。

---

## 10．明日の制作物

```text
section12_pt_br_draft01.md
pt_br_core10_master_draft01_18fields.csv
pt_br_core10_anki_draft01_18fields.csv
README_pt_br_core10_draft01.md
PORTUGUESE_BR_NOTE_TYPE_DRAFT01_18FIELDS.md
PORTUGUESE_BR_CARD_TEMPLATE_DRAFT01.md
section12_ja_source_for_pt_br.md
```

```text
ZIP：MEMORIOPOLIS_Portuguese_BR_Core10_draft01_18fields_2026-09-21.zip
```

重点観測：

```text
鼻母音
開母音・閉母音
強勢
r
lh / nh
名詞の性数
冠詞
動詞活用
você
nós / a gente
estar＋動名詞
```

---


---

# 特別追補：絵巻10景による場所法の実装

## 18．本追補の位置づけ

2026年9月20日、学習法の構造を再検討し、現在のMEMORIOPOLISには次の三要素がすでに存在することを確認した。

```text
NovelからConceptを抽出する
→ ストーリー法

Ankiで答えを自力で取り出す
→ アクティブリコール

FSRSが再訪時期を決める
→ 分散学習
```

一方、伝統的な「場所法」に相当する固定空間座標が、作品内には存在しながら、Conceptと一対一で制度化されていなかった。

この不足を補うため、次の方針を正式な構想として採用する。

> 絵巻を6景から10景へ拡張し、各景をCore10のConcept IDと一対一で対応させる。

絵巻、予告編、Novel、Anki、FSRSを別々の制作物ではなく、同じ記憶経路の異なる層として統合する。

---

## 19．MEMORIOPOLISの四つの記憶軸

```text
絵巻10景
→ 空間の固定座標
→ 場所法

予告編
→ 同じ10地点を順番に巡回
→ 視覚的な時間連鎖

Novel
→ 各地点へ出来事・因果関係・対話を与える
→ ストーリー法

Anki
→ Conceptを自力で取り出す
→ アクティブリコール

FSRS
→ その地点を再訪する時刻を決める
→ 分散学習
```

構造を一文で表すと、次のようになる。

> Novelが時間の道を作り、絵巻が空間の住所を作り、Ankiが取り出す行為を作り、FSRSが再訪の時刻を決める。

---

## 20．閲覧者の体験経路

公開側では学習法を明示しない。

```text
ホーム
↓
列車に乗る
↓
都市へ移動する
↓
絵巻または予告編を見る
↓
Novelをクリックして読む
↓
格納庫を見つける
↓
Ankiデータを見つける
↓
自分でインポートして学習する
↓
FSRSの時刻表に従って再訪する
```

体験の深さに応じて、記憶機能が段階的に増える。

```text
絵巻・予告編を見た人
→ 視覚的な場所と経路を手掛かりにできる

Novelを読んだ人
→ 出来事と因果関係を手掛かりにできる

格納庫でAnkiを見つけた人
→ 能動的な想起訓練へ進める

Ankiを継続する人
→ FSRSによって適切な時期に都市を再訪する
```

「場所法」という名称は公開画面で説明しなくてもよい。ただし、制作側では各景とConcept IDの対応を厳密に固定する。

---

## 21．Concept IDの再定義

Concept IDは単なるカード番号ではない。

> Concept IDは、物語、画像、映像、言語、制作ノート、記憶履歴を結ぶ都市の住所コードである。

例：

```text
C0007
├─ Concept：署名
├─ Novel内の署名場面
├─ 絵巻第7景
├─ 予告編第7地点
├─ 日本語：署名
├─ 英語：signature
├─ 韓国語：서명
├─ ロシア語：подпись
├─ 臺灣華語：簽名
├─ フィリピン語：lagda
├─ インドネシア語：tanda tangan
├─ ベトナム語：chữ ký
├─ スペイン語：firma
├─ ブラジル・ポルトガル語：assinatura（予定）
├─ Ankiの回答履歴
└─ 制作ノートの観測記録
```

言語ごとに別の場所を作らない。

```text
Concept
→ 一つの固定場所

言語
→ 同じ場所を異なる方向から見る面
```

これにより、JANUS-13の多言語面が一つのConcept座標へ集約される。

---

## 22．第四章第十二節の絵巻10景案

### 第1景：C0001 記録

```text
場所：運用局へ入る前の記録台
中心物：自動的にページをめくる巨大な記録簿
主要Concept：記録
```

### 第2景：C0002 記憶

```text
場所：記憶展示壁
中心物：触れたものの過去を映す半透明の壁
主要Concept：記憶
```

### 第3景：C0003 都市

```text
場所：穏息市を見下ろす展望台
中心物：複数の層が重なる都市模型
主要Concept：都市
```

### 第4景：C0004 通知

```text
場所：通知受付ホール
中心物：同じ画面に並ぶ二つの通知
主要Concept：通知
```

### 第5景：C0005 返信

```text
場所：返信窓口
中心物：本文が空白の返信欄
主要Concept：返信
```

### 第6景：C0006 宛先

```text
場所：宛先案内板
中心物：行き先が消え、Iだけが残る案内板
主要Concept：宛先
```

### 第7景：C0007 署名

```text
場所：署名検査台
中心物：銀白色に光る署名と検査線
主要Concept：署名
```

### 第8景：C0008 検証

```text
場所：外部検証室
中心物：複数の経路を照合する検証装置
主要Concept：検証
```

### 第9景：C0009 権限

```text
場所：権限ゲート
中心物：「権限がありません」と表示された閉鎖扉
主要Concept：権限
```

### 第10景：C0010 役割

```text
場所：役割管理室
中心物：人のいない椅子と、役割名だけが浮かぶ名札
終端：入力候補として残るI
主要Concept：役割
```

---

## 23．絵巻と予告編の整合ルール

絵巻と予告編は同じ10地点を共有する。

```text
絵巻第7景
→ 署名検査台

予告編第7地点
→ 同じ署名検査台

Novelの対応場面
→ 署名の検証

Anki C0007
→ 署名
```

固定する要素：

```text
背景の基本構造
中心物
主要色
視線または移動方向
Concept IDとの対応
```

変更可能な要素：

```text
カメラ距離
登場人物の配置
光の強さ
動き
時間帯
```

予告編では、第1景から第10景まで同じ方向へ進む。

```text
C0001
↓
C0002
↓
C0003
↓
...
↓
C0010
```

初期段階では逆方向の予告編を作らない。経路が定着した後、復習用の逆方向短編を検討できる。

---

## 24．公開層と管理層

### 視聴者に見える層

```text
第一景
第二景
第三景
...
第十景
```

### 制作者が管理する層

```text
scene-01 → C0001
scene-02 → C0002
scene-03 → C0003
...
scene-10 → C0010
```

### 内部ファイル名の例

```text
ch04-s12-c0001-record.webp
ch04-s12-c0002-memory.webp
ch04-s12-c0003-city.webp
ch04-s12-c0004-notification.webp
ch04-s12-c0005-reply.webp
ch04-s12-c0006-destination.webp
ch04-s12-c0007-signature.webp
ch04-s12-c0008-verification.webp
ch04-s12-c0009-permission.webp
ch04-s12-c0010-role.webp
```

公開画面へ`C0001`などを表示する必要はない。GitHub、メタデータ、制作ノート、AnkiではConcept IDを保持する。

---

## 25．Concept Atlas構想

場所法の正本は、Ankiの19番目のフィールドとして追加せず、まず外部のConcept Atlasとして管理する。

推奨構成：

```text
docs/
└─ concept-atlas/
   ├─ core10_map.md
   ├─ core20_map.md
   ├─ core30_map.md
   └─ scene_registry.csv
```

`core10_map.md`の例：

```markdown
# Core10 Memory Route

## Route

C0001 -> C0002 -> C0003 -> C0004 -> C0005
-> C0006 -> C0007 -> C0008 -> C0009 -> C0010

## C0001 記録

- District: 穏息市
- Building: 運用局
- Locus: 正門の記録台
- Visual Anchor: 自動的にページをめくる巨大な記録簿
- Scene: 01

## C0002 記憶

- District: 穏息市
- Building: 運用局
- Locus: 記憶展示壁
- Visual Anchor: 触れたものの過去を映す壁
- Scene: 02
```

Ankiの既存`ID`フィールドを、Concept Atlasへの住所コードとして利用する。

```text
Anki ID
↓
Concept Atlas
↓
絵巻の固定地点
↓
予告編の対応地点
↓
Novelの対応場面
```

18フィールド標準は当面維持する。

---

## 26．都市の階層構造

長期構造：

```text
MEMORIOPOLIS
└─ 地区
   └─ 建物
      └─ 経路・階
         └─ 固定地点
            └─ Concept ID
```

第四章第十二節の例：

```text
章：第四章「翻訳者」
→ 地区：穏息市

節：第十二節「宛先のない返信」
→ 建物：運用局

Core10
→ 運用局内の10地点
```

将来案：

```text
Core10
→ 運用局・第1経路

Core20
→ 運用局・第2経路
または外部接続棟

Core30
→ 別地区または序章地区
```

一つの絵巻は10景、一つの巡回単位とする。何十景も一巻へ詰め込まない。

---

## 27．場所法を機能させる制作条件

```text
各景が明確に異なる
各景の主要Conceptは一つ
主要物体は一つ
景の順番を固定する
絵巻と予告編で同じ場所を使う
Novelの出来事と対応づける
AnkiでConcept IDから場所を再想起できる
```

一景へ複数Conceptを詰め込まない。

```text
第7景
→ 署名

第8景
→ 検証

第9景
→ 権限
```

場所は意味そのものではなく、意味へ到達する索引である。

```text
意味理解
→ Novel
→ ExampleExplanation
→ MeaningBridge

住所と順序
→ 絵巻
→ Concept Atlas

想起
→ Anki

再訪時期
→ FSRS
```

---

## 28．利用者への最小限の誘導

「場所法」という用語を見せず、格納庫のREADMEなどに次の一文を置く案がある。

> カードのIDを見たら、絵巻の同じ地点を一度だけ思い出してください。

英語版の例：

> When you see a card ID, briefly recall the corresponding place in the scroll.

これにより、作品性を損なわず、希望する利用者は自然に空間手掛かりを使える。

---

## 29．本日のスペイン語Anki観測

```text
基準変種：スペインのスペイン語
ロケール：es-ES / es_ES
新規カード：10枚
Daily Trainingへの収集：成功
学習完了：成功
```

利用者の観測：

```text
スペイン語の音は英語と似ている部分があり、比較的すんなり学習を完了できた。
```

今後の注意：

```text
英語と似た語形は意味の橋として有効
ただし発音を英語化しない
スペイン標準のc / z、r、母音、強勢をSoundBridgeで維持する
```

スペイン語面は現行の`es-ES`基準を維持し、メキシコ・中南米変種は比較層へ置く。

---

## 30．ブラジル・ポルトガル語Windows環境の現状

2026年9月20日現在：

```text
Language.Basic~~~pt-BR~0.0.1.0
→ インストール処理を実施

Language.TextToSpeech~~~pt-BR~0.0.1.0
→ インストール中
```

完了判定はまだ行わない。

PowerShellプロンプトが戻った後、次を実行する。

```powershell
Get-WindowsCapability -Online |
Where-Object {
    $_.Name -match '^Language\..*~~~pt-BR~'
} |
Select-Object Name, State
```

期待する結果：

```text
Language.Basic~~~pt-BR~0.0.1.0          Installed
Language.TextToSpeech~~~pt-BR~0.0.1.0   Installed
```

処理中は次を守る。

```text
同じコマンドを再実行しない
Ctrl+Cを押さない
VS Codeを閉じない
PCをスリープさせない
Wi-Fiを切断しない
```

完了後：

```text
RestartNeededを確認
必要な場合だけ再起動
OneDrive同期を再開
管理者VS Codeを終了
通常権限のVS Codeへ戻す
```

---

## 31．明日のブラジル・ポルトガル語制作

```text
言語：ポルトガル語
基準：Português do Brasil
Windows：pt-BR
Anki：pt_BR
言語番号：第10言語
観測面：第11観測面
```

デッキ：

```text
MEMORIOPOLIS::Portuguese
```

ノートタイプ：

```text
MEMORIOPOLIS Portuguese Vocabulary
```

タグ：

```text
memoriopolis::pt_br::core10
```

TTS：

```html
{{tts pt_BR:Portuguese}}
```

```html
{{tts pt_BR:ExamplePortuguese}}
```

予定ZIP：

```text
MEMORIOPOLIS_Portuguese_BR_Core10_draft01_18fields_2026-09-21.zip
```

重点観測：

```text
鼻母音
開母音・閉母音
強勢
r / rr相当の発音差
lh / nh
名詞の性数
冠詞
動詞活用
você
nós / a gente
estar＋動名詞
ブラジルとポルトガルの差
```

日本との縁：

```text
日系移民
日系社会
日本への還流
日本国内のポルトガル語
日伯関係
BRICS
```

ポルトガルとの歴史的接続は、別の時間層として制作ノートへ保持する。

---

## 32．更新版の次回開始用プロンプト

```text
この引き継ぎ書を2026年9月20日の最終・特別追補版として、MEMORIOPOLIS / JANUS-13を再開します。

次の制作言語は第10言語、第11観測面のブラジル・ポルトガル語です。Português do Brasil、Windows pt-BR、Anki pt_BRを基準にします。日本からブラジルへの移民、日系社会、日本への還流、日伯関係、BRICSとの接続を優先します。ポルトガルとの種子島、南蛮貿易、キリスト教、外来語の歴史は制作ノートの歴史層として保持します。

最初にWindows Capabilityを確認し、Language.Basic~~~pt-BR~0.0.1.0とLanguage.TextToSpeech~~~pt-BR~0.0.1.0がInstalledであることを確認してください。TextToSpeechは2026年9月20日夕方にインストール中でした。Installedなら再導入しません。

その後、日本語正本section12_ja.mdを基に、第四章第十二節のブラジル・ポルトガル語版Novel全文第一稿と18フィールド版Anki Core10を作成してください。デッキ名はMEMORIOPOLIS::Portuguese、ノートタイプ名はMEMORIOPOLIS Portuguese Vocabulary、タグはmemoriopolis::pt_br::core10です。

単語TTSは{{tts pt_BR:Portuguese}}、例文TTSは{{tts pt_BR:ExamplePortuguese}}を使います。AnkiDroidでエラーが出た場合は、{{tts-voices:}}で端末がコピーしたロケールと音声識別子をそのまま使います。

新しい重要構想として、絵巻を6景から10景へ拡張し、Core10のC0001からC0010までを一景ずつ対応させます。Concept IDはカード番号ではなく、物語、絵巻、予告編、Anki、多言語、制作ノートを結ぶ都市の住所コードです。

第四章第十二節の10景は、C0001記録＝記録台、C0002記憶＝記憶展示壁、C0003都市＝都市展望台、C0004通知＝通知受付、C0005返信＝返信窓口、C0006宛先＝宛先案内板、C0007署名＝署名検査台、C0008検証＝外部検証室、C0009権限＝権限ゲート、C0010役割＝役割管理室を基本案とします。

絵巻は場所法、予告編は同じ地点の時間巡回、Novelはストーリー法、Ankiはアクティブリコール、FSRSは分散学習を担当します。公開画面でConcept IDや場所法を明示する必要はありませんが、制作側では各景とConcept IDを固定してください。

まずConcept Atlasを外部文書として作り、Ankiの19番目のフィールドはまだ追加しません。既存のIDフィールドを住所コードとして利用します。

MEMORIOPOLIS Daily Trainingは、第1フィルターがdeck:MEMORIOPOLIS is:due、上限50、忘れている可能性が高い順です。第2フィルターはdeck:MEMORIOPOLIS is:new、上限10、追加順です。FSRSは有効、目標保持率90%、一括再スケジュールはオフです。
```

---

## 33．2026年9月20日の最終店じまい地点

```text
JANUS-13                              13言語・14観測面
スペイン語                            第9言語・第10観測面
スペイン語基準                        es-ES
スペイン語Novel/Core10                完成・導入・学習完了
スペイン語の学習感触                  英語との音の類似が助けになった
次言語                                ブラジル・ポルトガル語
ポルトガル語                          第10言語・第11観測面
ポルトガル語基準                      pt-BR
pt-BR Basic                           導入処理実施
pt-BR TextToSpeech                    インストール中
場所法                                新規導入方針を確定
絵巻                                  6景から10景へ拡張方針
絵巻10景                              C0001～C0010と一対一対応
予告編                                同じ10地点を順番に巡回
Concept ID                            都市の住所コードとして再定義
Concept Atlas                         外部文書として作成予定
Anki 19番目のフィールド               当面追加しない
Novel                                 ストーリー法を担当
Anki                                  アクティブリコールを担当
FSRS                                  分散学習を担当
```

本日の最終到達点：

> MEMORIOPOLISは、物語を読む都市から、実際に歩いて記憶を検索できる都市へ進む。絵巻10景が空間の住所を作り、予告編が巡回路を作り、Novelが出来事を結び、AnkiがConceptを取り出し、FSRSが再訪の時刻を決める。Concept IDは、そのすべてを結ぶ住所コードである。
