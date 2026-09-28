# MEMORIOPOLIS / JANUS-18 完全版引き継ぎ書

更新日時：2026年9月28日 10:50 JST  
版：E0001韓国語版・Korean Core20・FSRS理解・CLASSICA-5方針統合版  
次回作業日：2026年9月29日

---

## 1．本書の目的

本書は、2026年9月28日時点のMEMORIOPOLIS / JANUS-13について、E0001韓国語版、韓国語Core10へのConcept画像追加、韓国語専用Anki UI、韓国語Core20 CSV、FSRSとDue Dateへの理解、記憶術との接続、現在のカード状況、および次回のロシア語作業を引き継ぐ完全版文書である。

---

## 2．本日の主要成果

1. AnkiDroidのCard Viewerで、MEMORIOPOLIS配下の全150カードにDue Dateが割り当てられていることを確認した。
2. スケジューラー名はERSではなくFSRSであることを再確認した。
3. 初期に同じカードが多く出ていたのは、苦手なカードが短い間隔で重なったためと理解した。
4. Daily Trainingは、FSRSが設定したDue Dateを迎えたカードを収集していたと整理した。
5. `E0001_ko.md`を、逐語訳ではなく自然な韓国語Essayとして作成した。
6. 韓国語版の中心命題と結末に、韓国語独自の自然な響きがあることを確認した。
7. 韓国語ノートタイプの既存13フィールド末尾へ`ConceptScene`を追加した。
8. 韓国語Core10のC0001～C0010へConcept画像を追加した。
9. 韓国語Core20の14フィールドCSV一式を作成した。
10. 韓国語専用の表面、裏面、CSSを作成した。
11. 韓国語UIはアップロード済みCore10フィールドマスターだけを参照することを機械的に検査した。
12. 帰りの電車でAnkiDroid上の画像、TTS、ダークモード、プルダウン、自動スクロールを確認する予定とした。
13. 次回はロシア語Core20へ進む方針を確認した。

---

## 3．JANUS-13の基本構造

```text
経験・読書・実務・日常観測
  ↓
現代日本語Essayを作成
  ↓
canonical化
  ↓
Concept候補を抽出
  ↓
人間がConcept境界を承認
  ↓
Concept画像
  ↓
各言語版Essay
  ↓
各言語Anki
  ↓
FSRSによる変換訓練
  ↓
次の読書・創作へ還流
```

GitHubを正本とする。

- Novel：記憶都市の深い縦坑
- Essay：日々増える街路
- Concept ID：言語間で共有する住所
- Concept画像：想起を起動するアンカー
- Anki：多言語間の変換訓練
- FSRS：記憶状態に応じた復習日の配分

---

## 4．日本語Novelと日本語Ankiの正

### Novel

```text
日本語Novel
├─ 現代日本語版
└─ 近代日本語版
```

### Anki

日本語系Ankiの唯一の正：

```text
MEMORIOPOLIS::ModernJapanese
```

- 現代日本語専用Ankiデッキは作らない。
- 作品・Concept上は13言語・14観測面。
- Anki上は13言語デッキ。
- `ModernJapanese`は近代日本語版Ankiを指す。

---

## 5．Essayのcanonical状況

```text
E0001_ja.md          canonical
E0001_en.md          canonical
E0001_zh-Hant-TW.md  canonical
E0001_ko.md          canonical
```

Essay配置：

```text
essay/
└─ E0001/
   ├─ E0001_ja.md
   ├─ E0001_en.md
   ├─ E0001_zh-Hant-TW.md
   └─ E0001_ko.md
```

---

## 6．E0001韓国語版

ファイル：

```text
E0001_ko.md
```

タイトル：

```text
‘로마루’에서 로마인으로
```

「ロマる」は意味未確定の聞き取り語であるため、韓国語の意味へ置き換えず、音を反映した`로마루`として保持した。

### 中心命題

```text
사람은 발밑의 땅을 잃는 것이 아니다.
자신이 연결되는 땅을 바꿀 뿐이다.
```

対応する日本語：

```text
人は、地面を失うのではない。
接続する地面を変える。
```

### 結末

```text
끝내 그 말의 뜻은 찾지 못했다.
그럼에도 그 말은 하나의 길을 열었다.
```

### 翻訳方針

- 日本語の語順をそのまま追わない。
- 韓国語の段落リズムと論理展開を優先する。
- 未知語、記憶、土地、移動、プラットフォームへ進む経験的な核を維持する。
- ロマ人に関する観察、記憶、資料、仮説を区別する。
- 「地面」「接続」「制約」の中心比喩を維持する。
- 結末を説明し切らず、思考経路が開かれた余韻を残す。

---

## 7．Core20正式Concept

| ID | 日本語 | 英語 | 臺灣華語 | 韓国語 |
|---|---|---|---|---|
| C0011 | ある | exist | 存在 | 존재하다 |
| C0012 | する | do | 做 | 하다 |
| C0013 | 持つ | have | 擁有 | 가지다 |
| C0014 | 送る | send | 傳送 | 보내다 |
| C0015 | 受け取る | receive | 接收 | 받다 |
| C0016 | 聞く | hear | 聽見 | 듣다 |
| C0017 | 調べる | look up | 查詢 | 찾아보다 |
| C0018 | 移る | move | 轉移 | 옮겨 가다 |
| C0019 | 結びつく | connect | 連結 | 연결되다 |
| C0020 | 縛られる | be bound | 受到束縛 | 얽매이다 |

配分：

```text
計画配分枠：5
E0001実出現枠：3
縁・発見枠：2
```

---

## 8．記憶術とConcept画像

ジョセフ・フォアの記憶術に関する読書から、次の観点を確認した。

- 場所法では、土地、建物、部屋に対して人間が自然に取り込む空間情報を利用する。
- 美しさ、奇想天外さ、強い違和感など、印象の強い対象が想起アンカーになる。
- 記憶対象を空間上の住所へ配置することで、想起経路を作る。
- 実在する建物だけでなく、建築資料から得た場所も記憶宮殿に利用できる。

JANUS-13では次の対応関係になる。

```text
Concept ID
＝ 記憶宮殿の住所

Concept画像
＝ 住所で遭遇する強いアンカー

言語別カード
＝ 同じ住所へ至る複数の経路

Essay
＝ 住所どうしを結ぶ街路

FSRS
＝ それぞれの経路を再訪する時刻表
```

同じConcept画像を13言語で共有することで、一つの記憶風景から複数言語を呼び出す。

---

## 9．Concept画像

### Core10

```text
MEMORIOPOLIS_ConceptImages_C0001-C0010_2026-09-25.zip
```

### Core20

```text
MEMORIOPOLIS_ConceptImages_C0011-C0020_2026-09-26.zip
```

全言語共通フィールド：

```text
ConceptScene
```

Core20対応：

```text
C0011 memoriopolis_c0011_exist.webp
C0012 memoriopolis_c0012_do.webp
C0013 memoriopolis_c0013_have.webp
C0014 memoriopolis_c0014_send.webp
C0015 memoriopolis_c0015_receive.webp
C0016 memoriopolis_c0016_hear.webp
C0017 memoriopolis_c0017_look_up.webp
C0018 memoriopolis_c0018_move.webp
C0019 memoriopolis_c0019_connect.webp
C0020 memoriopolis_c0020_be_bound.webp
```

---

## 10．韓国語ノートタイプの正式14フィールド

韓国語Core10フィールドマスターから確定した構造：

```text
1. ID
2. Korean
3. Romanization
4. Japanese
5. PartOfSpeech
6. ExampleKorean
7. ExampleRomanization
8. ExampleJapanese
9. Source
10. Tags
11. ExampleBreakdown
12. ExampleExplanation
13. ExamplePronunciationHint
14. ConceptScene
```

既存13フィールドの順序は変更せず、末尾に`ConceptScene`を追加した。

---

## 11．韓国語Anki UI

完成ファイル：

```text
KOREAN_CARD_UI_14FIELDS_CONCEPTSCENE_3PANELS_2026-09-28.md
```

### 表面

```text
Concept ID                 한국어
Concept画像
ハングル見出し語
ローマ字
ko_KR TTS
```

### 背面の初期表示

```text
CONCEPT BRIDGE
日本語Concept
品詞
韓国語例文
例文TTS
日本語訳
```

### 3段プルダウン

```text
語の構造
例文解説
言語間ブリッジ
```

#### 語の構造

- ハングル
- ローマ字
- 品詞・語の働き
- 実際の聞こえ方・音韻変化

#### 例文解説

- 例文ローマ字
- 文の組み立て
- なぜこの意味になるか

#### 言語間ブリッジ

- 音の橋
- ハングル、ローマ字、日本語Concept、Concept画像の接続

### TTS

単語：

```html
{{tts ko_KR:Korean}}
```

例文：

```html
{{tts ko_KR:ExampleKorean}}
```

### 自動スクロール

裏面の次を必ず保持する。

```html
<div id="answer" class="answer-divider">
  <span>CONCEPT BRIDGE</span>
</div>
```

`id="answer"`がAnkiDroidでの解答開始位置となる。

### 整合性検査

- 正式14フィールド以外を参照していない。
- 未存在フィールドはない。
- `ko_KR` TTSを単語と例文の双方に設定した。
- `id="answer"`を確認した。
- CSSはライトモード、ダークモード、モバイル幅へ対応した。

---

## 12．韓国語Core20 CSV

完成ZIP：

```text
MEMORIOPOLIS_Korean_Core20_14fields_2026-09-28.zip
```

収録：

```text
README.md
ko_core20_master_14fields.csv
ko_core20_anki_14fields.csv
```

Source：

```text
E0001_ko
```

Tags：

```text
memoriopolis::ko::core20
```

検査済み：

- 10行すべて14列
- C0011～C0020の連番
- SourceとTagsの統一
- Concept画像名とIDの一致
- master版とAnki版の内容一致
- ZIP内部の破損なし

---

## 13．韓国語Core20の言語固有ポイント

### C0011 존재하다

抽象的・論理的な存在を表す。所在・所有の`있다`とは区別する。

### C0012 하다

日本語の「する」に近い基本動詞だが、使用範囲は完全には一致しない。

### C0013 가지다

物だけでなく、権限、役割、性質、関係を持つ場合にも使う。

### C0015 받다

単独では`받따`に近く、`받아야`では連音により`바다야`に近づく。

### C0016 듣다

音・話を聞く。質問する`묻다`とは別Concept。過去形はㄷ不規則活用で`들었다`となる。

### C0017 찾아보다

`찾다`と`보다`が結び付き、「探してみる」「調べてみる」を表す。検証する`검증하다`とは区別する。

### C0018 옮겨 가다

位置、焦点、状態が別の側へ移っていくことを表す。

### C0019 연결되다

`연결하다`に`되다`が付き、関係が成立してつながることを表す。

### C0020 얽매이다

物理的拘束だけでなく、規則、制度、関係、考えなどに縛られることを表す。

---

## 14．フィールドマスター先行ルール

臺灣華語版の手戻りを踏まえ、次の順序を固定する。

```text
Core10フィールドマスターを取得
  ↓
実在フィールド名と順序を確定
  ↓
ConceptScene追加後の列数を確定
  ↓
表面・裏面・CSSを生成
  ↓
参照フィールドを機械検査
  ↓
Core20 CSVを同一順序で生成
  ↓
列数、ID、Source、Tags、画像参照を検査
  ↓
ZIP化
```

原則：

> 共通UIの外装は再利用するが、データ参照は必ずその言語の実フィールドマスターから組み立てる。

---

## 15．FSRSとDue Dateへの理解

AnkiDroidのCard Viewerで、MEMORIOPOLISの全150カードにDue Dateが設定されていることを確認した。

名称：

```text
FSRS
Free Spaced Repetition Scheduler
```

FSRSはカードごとに記憶状態を推定し、次の復習日を設定する。

```text
Stability
＝ 記憶がどれくらい保たれるか

Difficulty
＝ そのカードの覚えにくさ

Retrievability
＝ 現在思い出せる見込み

Due Date
＝ 次に復習する日
```

### 初期に同じカードが見えた理由

```text
学習履歴が少ない
  ↓
苦手カードでAgainが発生
  ↓
短い間隔で再表示
  ↓
同じカードが重なって見える
```

履歴が蓄積すると、容易なカードは先の日付へ、難しいカードは近い日付へ分散する。

### Daily Trainingとの役割分担

```text
FSRS
＝ 各カードのDue Dateを決める

JANUS-13 Daily Training
＝ 今日が期限のカードと新規カードを集める
```

Daily Trainingが独自に特定の語を偏って選んでいたのではない。

### Forgottenカスタム

```text
rated:7:1 deck:MEMORIOPOLIS
```

直近7日以内に`Again`を押したカードを観測する補助フィルター。

- Daily Training：通常学習の本線
- Custom Study Session：直近の失敗を観測する窓

今後も新しい訓練メニューを増やしすぎず、Coreを充実させ、FSRSへ復習配分を任せる。

---

## 16．2026年9月28日店じまい時点のカード状況

画像で確認したAnkiWeb表示：

```text
Custom Study Session
新規：0
学習中：0
復習：7

JANUS-13 Daily Training
新規：10
学習中：0
復習：21

MEMORIOPOLIS各言語デッキ
新規：0
学習中：0
復習：0
```

解釈：

- Daily Trainingに新規10枚と復習21枚が集約されている。
- Custom Study Sessionには直近のForgottenカード7枚がある。
- 元デッキ側が0なのは、対象カードがフィルターデッキへ一時的に移動しているためと考えられる。
- Daily Trainingを日々の本線として継続する。
- Custom Study Sessionは必要時の補助観測として扱う。

---

## 17．帰りの電車での韓国語AnkiDroid確認

### 表面

- C0001～C0020の画像が表示される
- ハングルが明瞭に表示される
- ローマ字が表示される
- `한국어`バッジが表示される
- `ko_KR`単語TTSが動作する

### 背面

- `Show answer`後に`CONCEPT BRIDGE`へ移動する
- 日本語Conceptと品詞が表示される
- 韓国語例文と日本語訳が表示される
- `ko_KR`例文TTSが動作する
- 3段プルダウンが開閉できる
- 長文解説が自然に折り返される

### ダークモード

- ハングル見出し語が背景へ沈まない
- ローマ字が読める
- 珊瑚色の韓国語バッジが読める
- 紫、青、緑のプルダウン見出しを区別できる
- プルダウン内部の日本語解説が読める

### 重点カード

```text
C0011 존재하다
C0016 듣다
C0020 얽매이다
```

C0020では、長い見出し、ローマ字、画像、TTS、折り返しを重点確認する。

---

## 18．設計書と引き継ぎ書

JANUS-13は現在も仕様を改善中であるため、恒常的な設計書の固定は保留する。

当面の管理方法：

```text
完全版引き継ぎ書
＋
言語別Core10フィールドマスター
＋
生成前後チェックリスト
```

仕様が安定した段階で、以下の設計書構成を再検討する。

```text
docs/design/
├─ JANUS13_ARCHITECTURE.md
├─ ANKI_COMMON_UI.md
├─ FIELD_MASTER_POLICY.md
├─ LANGUAGE_PROFILES.md
├─ CONCEPT_IMAGE_POLICY.md
└─ AUTOMATION_PIPELINE.md
```

---

## 19．次回：ロシア語Core20

次回作業日：2026年9月29日

### 最初にアップロードするファイル

```text
ru_core10_master.csv
ru_core10_anki.csv
```

名称が異なる場合も、ヘッダー付きCore10マスターを優先する。

### 固定手順

```text
ロシア語Core10フィールドマスターを取得
  ↓
実在フィールド名と順序を確定
  ↓
ConceptSceneを末尾へ追加
  ↓
Core10画像を登録
  ↓
E0001ロシア語版を自然な文章で作成
  ↓
ロシア語専用UIを作成
  ↓
参照フィールドを機械検査
  ↓
ロシア語Core20 CSVを作成
  ↓
列数、ID、Source、Tags、画像参照を検査
  ↓
Ankiへインポート
  ↓
PC版・AnkiDroidで確認
```

### ロシア語で観測したい要素

既存フィールドに存在する範囲で扱う。

```text
キリル文字
アクセント位置
ローマ字または発音補助
品詞
語形変化
格支配
完了体・不完了体
動詞の再帰形
例文の構造
日本語とのConcept境界
```

理想フィールドを先に仮定しない。

---

## 20．EssayからAnkiまでの半自動化

人間の承認ゲート：

```text
Gate 1：現代日本語Essayのcanonical化
Gate 2：Concept選定と境界確定
```

承認後に自動化できる工程：

```text
Concept画像
対象言語Essay
語彙・発音情報
例文
例文解説
言語間ブリッジ
Master CSV
Anki CSV
ConceptScene参照
README
manifest
ZIP
引き継ぎ書
```

各言語のAnki生成前に必ず次を入力する。

```text
field_masters/<language>_core10_master.csv
```

---

## 21．次回開始用プロンプト

```text
この引き継ぎ書を2026年9月28日の最新状態としてMEMORIOPOLIS / JANUS-13を再開します。

E0001_ja.md、E0001_en.md、E0001_zh-Hant-TW.mdはcanonicalです。E0001_ko.mdは自然な韓国語Essayとして作成済みで、status: canonicalです。

韓国語ノートタイプは、既存13フィールドの末尾へConceptSceneを追加した14フィールド構成です。正式フィールドは、ID、Korean、Romanization、Japanese、PartOfSpeech、ExampleKorean、ExampleRomanization、ExampleJapanese、Source、Tags、ExampleBreakdown、ExampleExplanation、ExamplePronunciationHint、ConceptSceneです。

韓国語Core10にはConcept画像を追加済みです。韓国語Core20はMEMORIOPOLIS_Korean_Core20_14fields_2026-09-28.zipとして完成済みです。韓国語UIはKOREAN_CARD_UI_14FIELDS_CONCEPTSCENE_3PANELS_2026-09-28.mdです。

帰りの電車でAnkiDroid上の画像、ko_KR TTS、ダークモード、3段プルダウン、id=answerによる自動スクロール、C0020の表示を確認します。問題があればロシア語作業前に修正します。

FSRSが全150カードへDue Dateを割り当てていることをCard Viewerで確認しました。初期に同じカードが多く見えたのは、苦手カードの短い間隔が重なったためです。Daily TrainingはFSRSが設定したDue Dateを迎えたカードを集めています。設定は変更せず、Coreを充実させます。

店じまい時点で、Custom Study Sessionは復習7枚、JANUS-13 Daily Trainingは新規10枚・復習21枚です。

本日はロシア語Core20を進めます。最初にロシア語Core10のmaster CSVとAnki CSVをアップロードします。必ずフィールドマスターを先に読み、実在フィールド名と順序を確定してから、E0001ロシア語版、UI、Core20 CSVを生成してください。理想フィールドを先に仮定しないでください。
```

---

## 22．2026年9月28日の店じまい地点

- MEMORIOPOLIS全カード：150枚
- FSRS Due Date：Card Viewerで確認済み
- FSRSへの理解：苦手カード優先と将来日への分散を確認
- Daily Training：新規10枚、復習21枚
- Custom Study Session：復習7枚
- E0001韓国語版：canonical
- 韓国語Core10画像：追加済み
- 韓国語正式フィールド：14個
- 韓国語Core20 CSV：完成
- 韓国語UI：完成
- 韓国語UIフィールド参照：機械検査済み
- 韓国語TTS：`ko_KR`
- 韓国語AnkiDroid確認：帰りの電車で実施予定
- 記憶術上の整理：Concept IDが住所、Concept画像がアンカー
- 再発防止：フィールドマスター先行
- 設計書：仕様安定後に再考
- FSRS設定：変更なし
- 学習方針：訓練メニューを増やしすぎずCoreを充実
- 次回：ロシア語Core20
- 次回必須入力：ロシア語Core10フィールドマスター

本日の最終合意：

> Concept IDを記憶宮殿の住所、Concept画像を強い想起アンカー、各言語を同じ住所へ至る経路として育てる。カードの再訪時期はFSRSへ任せ、JANUS-13は経験から生まれるCoreと経路を増やしていく。


---

## 23．JANUS-18とCLASSICA-5の採用決定

JANUS-13の現代13言語に、次の古典5言語を加え、プロジェクトを`JANUS-18`へ発展させる方針を採用した。

```text
JANUS-18
├─ LIVING-13
│  └─ 現代世界を横断する13言語
│
└─ CLASSICA-5
   ├─ Classical Latin
   ├─ Ancient Greek
   ├─ Classical Sanskrit
   ├─ Biblical Hebrew
   └─ Classical Arabic
```

これは18言語を同じ平面に並べる拡張ではない。

```text
LIVING-13
＝ 現代の経験を水平方向に観測する円環

CLASSICA-5
＝ 言葉とConceptの歴史的地層へ垂直方向に降りる円環
```

JANUS-18は、現代語による地表の街路と、古典語による時間方向の縦坑を持つ二重環構造とする。

---

## 24．CLASSICA-5の目的

CLASSICA-5は、現代技術用語や法律用語を古典語へ機械的に翻訳するための仕組みではない。

目的は次のとおり。

1. 現代Conceptの歴史的な根を探る。
2. 古典文明で近縁Conceptがどのように切り分けられていたかを観測する。
3. 現代語の直系祖先、または後世の諸言語・思想・学問へ大きな影響を与えた言語層へ接続する。
4. 直接対応語がない場合も、その不在や意味のずれを記録する。
5. 同じConcept画像を共有しながら、文明ごとに異なる意味の地層を観測する。

基本原則：

> 現代の語を無理に古典語化せず、古典世界に存在する近縁Conceptまで降りて接続する。

例：

```text
プラットフォーム規約
  ↓
規則・法・命令・慣習への拘束

フォロワー数
  ↓
名声・評判・群衆の注意

推薦アルゴリズム
  ↓
選別・順序・判断・配分

システム権限
  ↓
力・資格・許可・委任・支配権
```

---

## 25．CLASSICA-5の基準言語層

各古典語は、単純に最古の形を選ぶのではなく、次の基準で採用する。

> 現代語の直系祖先となった、または後世の他言語・思想・宗教・学術へ強い影響を与えた時期の言語層を正とする。

### 25.1 Classical Latin

```text
正：Classical Latin
橋：Medieval Latin
```

- 古典ラテン語を語彙・文法の基準とする。
- ロマンス諸語の祖先として観測する。
- 中世ラテン語は、宗教、法、哲学、学術への橋として必要に応じて参照する。

### 25.2 Ancient Greek

```text
正：Classical Attic Greek
橋：Koine Greek
```

- 哲学、政治、都市、文学、歴史記述では古典期アッティカ語を基準とする。
- 地中海世界への拡大、初期キリスト教文献、後代のギリシャ語への接続ではコイネーを参照する。
- ConceptによってClassical AtticとKoineのどちらが適切かを明示する。

### 25.3 Classical Sanskrit

```text
正：Classical Sanskrit
橋：Vedic Sanskrit
```

- パーニニ以降の古典サンスクリット語を文法上の基準とする。
- 言葉、記憶、存在、道、束縛など、ヴェーダ的な思想層との接続が重要なConceptではVedic Sanskritを注記する。

### 25.4 Biblical Hebrew

```text
正：Biblical Hebrew
橋：Mishnaic / Rabbinic Hebrew
```

- 土地、記憶、名、道、契約、共同体などのConceptを観測する基準とする。
- 後代の意味変化や現代ヘブライ語への連続性が重要な場合は、ミシュナ・ラビ文学のヘブライ語を橋として参照する。

### 25.5 Classical Arabic

```text
正：Classical Arabic
橋：Quranic Arabic
```

- 古典アラビア語を文法・語彙の基準とする。
- クルアーン固有の語法や意味が重要な場合のみ、Quranic Arabicとして明示する。
- 現代標準アラビア語への単純な置換ではなく、古典文語の意味世界を観測する。

---

## 26．CLASSICA-5のConcept対応方針

C0001～C0020を、そのまま一対一で翻訳することは前提としない。

各Conceptの対応関係を次のいずれかで記録する。

```text
Exact
＝ かなり直接的に対応する

Near
＝ 近縁Conceptとして対応する

Partial
＝ 意味の一部だけが重なる

Civilizational Reframing
＝ その文明固有の切り分けへ組み替える

No Direct Equivalent
＝ 直接対応する語がない
```

`No Direct Equivalent`は欠損ではない。

> そのConceptが、その文明では別の境界で切り分けられていたことを示す重要な観測結果である。

### 直接接続しやすい候補

```text
記録
記憶
都市
応答
署名
存在する
する
持つ
送る
受け取る
聞く
調べる
移る
結びつく
縛られる
```

### 近縁Conceptへ降ろす候補

```text
通知
→ 知らせ・告知・伝令・徴

検証
→ 試す・吟味する・確かめる・証明する

受取人
→ 受ける者・宛てられた者・使者から受け取る者

権限
→ 力・資格・許可・支配権・委任

役割
→ 務め・職分・身分・配役
```

### 無理に直接対応させない現代Concept

```text
SNS
フォロワー
プラットフォーム規約
推薦アルゴリズム
デジタル通知
電子署名
システム権限
```

これらは、古典世界にも存在する注意、名声、規則、市場、共同体、拘束、証し、委任などのConceptへ降ろして接続する。

---

## 27．CLASSICA-5の作業開始条件と順序

CLASSICA-5は直ちに着手せず、次の順序で進める。

```text
E0001のLIVING-13展開を継続
  ↓
ドイツ語版まで完成
  ↓
近代日本語で現代と過去を橋渡し
  ↓
C0001～C0020の古典語適合性を審査
  ↓
CLASSICA-5を一挙にCore20まで整備
  ↓
JANUS-18としてFSRS学習へ投入
```

近代日本語は、次の時間方向の翻訳者として位置づける。

```text
現代日本語
  ↓
近代日本語
  ↓
CLASSICA-5
```

E0001の現代語円環は、ドイツ語まで完成させる。途中でCLASSICA-5へ分岐しない。

---

## 28．CLASSICA-5はCore20を一挙に整備する

C0001だけを使った小規模PoCは実施しない。

理由：

- Ankiノートタイプの作成方法が確立している。
- CSV生成、画像参照、TTS、FSRS学習の基本手順が確認できている。
- フィールドマスター先行と機械的な整合性検査により、制作上の主要リスクを抑えられる。
- 古典語ではConcept相互の関係をCore20全体で比較する方が有益である。

方針：

> Core10～20から古典語化に適したConceptを選別し、各古典語をCore20までまとめて整備する。

20枚を揃える際、直接対応しないConceptは近縁Concept、文明固有の再定義、または直接対応なしとして記録する。

---

## 29．CLASSICA-5の制作単位

5言語すべてを同時並行で作るのではなく、一言語ずつCore20一式を完成させる。

推奨順序：

```text
1. Classical Latin Core20
2. Ancient Greek Core20
3. Classical Sanskrit Core20
4. Biblical Hebrew Core20
5. Classical Arabic Core20
```

各言語で完成させる一式：

```text
言語層定義
言語別フィールドマスター
Ankiノートタイプ
Core20見出し語
語形・形態論
文法情報
古典語例文または学習文
出典
Concept対応種別
現代Conceptとの境界
発音伝統
ConceptScene
Master CSV
Anki CSV
README
AnkiDroid確認
```

5言語完成後、横断的にConcept ID、対応種別、画像、Source、Tagsの統一性を再確認する。

---

## 30．CLASSICA-5のAnki設計原則

CLASSICA-5でも次は共通とする。

```text
Concept ID
ConceptScene
日本語Concept
Core番号
GitHub正本
FSRS
フィールドマスター先行
生成後整合性検査
```

一方、LIVING-13と評価軸を分ける。

```text
LIVING-13
＝ 自然な現代文・現代用法・現代TTS

CLASSICA-5
＝ 時代層・語形・文法・出典・発音伝統・Concept対応距離
```

古典語では「ネイティブらしい現代文」を評価基準にしない。

評価基準：

```text
時代層に整合する
文法的に妥当である
語義が出典と整合する
後世の意味を古代へ投影しすぎない
語形変化を明示する
発音伝統を明示する
再建発音と宗教的・伝統的読法を混同しない
```

仮の共通フィールド候補：

```text
ID
Lemma
Script
Romanization
JapaneseConcept
PartOfSpeech
HistoricalLayer
ConceptMatchType
Morphology
Grammar
ClassicalExample
ExampleTransliteration
ExampleJapanese
Source
ClassicalCitation
ConceptBridge
PronunciationTradition
Tags
ConceptScene
```

ただし、この候補を5言語へ機械的に固定しない。各言語の特性を整理した後、言語別フィールドマスターを確定する。

---

## 31．CLASSICA-5の例文と出典

CLASSICA-5では、現代Essayの全文翻訳を必須としない。

基本構造：

```text
現代日本語Essay
  ↓
古典語へ接続できる中核Conceptを抽出
  ↓
同じConceptまたは近縁Conceptがあるかを調べる
  ↓
古典語の短い学習文を作る
  ↓
古典文献上の用例・語法・出典へ接続
  ↓
現代Conceptとの距離と境界を記録
```

例文層は二つを想定する。

```text
Concept Bridge
＝ JANUS-18学習用の短い古典語文

Classical Citation
＝ 古典文献における実例または出典情報
```

毎回のEssayを古典5言語へ全文翻訳する必要はない。古典語との縁があるConceptだけを接続する。

---

## 32．CLASSICA-5の発音方針

古典語では唯一のネイティブ標準発音を前提にしない。

各カードまたはノートタイプに`PronunciationTradition`を明示する。

暫定方針：

```text
Classical Latin
＝ Classical Restored

Ancient Greek
＝ Reconstructed Attic
必要に応じてKoineの再建発音を別記

Classical Sanskrit
＝ Scholarly / Traditional readingを明示

Biblical Hebrew
＝ Tiberian-oriented reconstruction

Classical Arabic
＝ Classical / Quranic recitation traditionを明示
```

音声は必須条件としない。

優先順位：

```text
文字
語形
文法
出典
Concept境界
発音伝統
音声
```

現代語向けTTSを古典語へ無理に流用しない。

---

## 33．JANUS-18における記憶宮殿の拡張

JANUS-18では、場所法の構造も二層になる。

```text
Concept ID
＝ 時代を越えて共有する住所

ConceptScene
＝ 現代語と古典語をつなぐ共通アンカー

LIVING-13
＝ 同じ住所へ向かう現代の街路

CLASSICA-5
＝ 同じ住所の地下にある文明史的地層

近代日本語
＝ 地表と地下をつなぐ階段

FSRS
＝ 各経路と各地層を再訪する時刻表
```

最終的なJANUS-18の理念：

```text
現代語は世界を横断する。
近代日本語は時代を橋渡しする。
古典語は思考の海底へ降りる。
```

---

## 34．更新後の次回開始用プロンプトへの追記

次回以降の開始用プロンプトには、次を追加する。

```text
JANUS-13は、現代13言語のLIVING-13と古典5言語のCLASSICA-5からなるJANUS-18へ発展させる方針です。

CLASSICA-5はClassical Latin、Ancient Greek、Classical Sanskrit、Biblical Hebrew、Classical Arabicです。各言語は最古層ではなく、現代語の直系祖先となった、または後世の諸言語・思想・学術・宗教へ大きな影響を与えた時期の言語層を基準とします。

現代技術用語や法律用語は古典語へ無理に直訳しません。C0001～C0020から古典語化に適したConceptを選び、直接対応、近縁、部分対応、文明固有の再定義、直接対応なしのいずれかを記録します。

作業開始はE0001の現代語円環をドイツ語まで完成させ、近代日本語で現代と過去を橋渡しした後です。C0001だけのPoCは行わず、CLASSICA-5を各言語ごとに一挙にCore20まで整備します。
```

---

## 35．2026年9月28日追記後の最終合意

- プロジェクト名は将来的に`JANUS-18`へ発展させる。
- 現代13言語を`LIVING-13`とする。
- 古典5言語を`CLASSICA-5`とする。
- CLASSICA-5はClassical Latin、Ancient Greek、Classical Sanskrit、Biblical Hebrew、Classical Arabic。
- 古典語は、現代語の直系祖先または後世に強い影響を与えた時期の言語層を正とする。
- 現代技術・法律用語は無理に古典語化しない。
- 近縁Concept、文明固有の再定義、直接対応なしを正式な観測結果として認める。
- E0001のLIVING-13円環をドイツ語まで完成させる。
- その後、近代日本語を現代と過去の橋として整備する。
- C0001～C0020から古典語化に適したConceptを選ぶ。
- C0001だけの試験は行わない。
- CLASSICA-5は一言語ずつCore20まで一挙に整備する。
- Concept IDとConceptSceneはLIVING-13とCLASSICA-5で共有する。
- 古典語では時代層、語形、文法、出典、発音伝統、Concept対応距離を重視する。
- Anki制作では、CLASSICA-5でも言語別フィールドマスター先行を守る。

追記後の最終理念：

> JANUS-18は、現代13言語で世界を横断し、近代日本語を階段として、古典5言語で思考の歴史的地層へ降りる。現代語を古典語へ無理に置換せず、Conceptの近縁性、ずれ、不在そのものを記憶都市の測量結果として残す。
