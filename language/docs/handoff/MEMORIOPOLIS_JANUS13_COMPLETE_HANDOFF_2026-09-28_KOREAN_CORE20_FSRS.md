# MEMORIOPOLIS / JANUS-13 完全版引き継ぎ書

更新日時：2026年9月28日 10:50 JST  
版：E0001韓国語版・Korean Core20・FSRS理解統合版  
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
E0001_ko.md          draft
```

韓国語版を正式採用する場合は、YAMLを次へ変更する。

```yaml
status: canonical
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

E0001_ja.md、E0001_en.md、E0001_zh-Hant-TW.mdはcanonicalです。E0001_ko.mdは自然な韓国語Essayとして作成済みで、現在status: draftです。正式採用する場合はcanonicalへ変更します。

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
- E0001韓国語版：作成済み、draft
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
