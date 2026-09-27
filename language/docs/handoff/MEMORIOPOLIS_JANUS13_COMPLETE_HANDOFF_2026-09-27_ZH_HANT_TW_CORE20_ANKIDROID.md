# MEMORIOPOLIS / JANUS-13 完全版引き継ぎ書

更新日時：2026年9月27日 17:10 JST  
版：E0001 zh-Hant-TW canonical・臺灣華語Core20・AnkiDroid運用統合版  
次回作業日：2026年9月28日

---

## 1．本書の目的

本書は、2026年9月27日時点のMEMORIOPOLIS / JANUS-13について、E0001臺灣華語版、臺灣華語Ankiの新UI、Core10画像、Core20 CSV、フィールド不一致による手戻りと再発防止、Daily TrainingとForgottenカスタム、AnkiDroidのフィルターデッキ問題、および次回の韓国語作業を引き継ぐ完全版文書である。

---

## 2．本日の主要成果

1. `E0001_zh-Hant-TW.md`を作成した。
2. 臺灣華語版を内容確認後、`status: canonical`へ変更した。
3. 今後の臺灣華語関連ファイル・メタデータを`zh-Hant-TW`へ統一した。
4. 臺灣華語ノートタイプへ`ConceptScene`を追加した。
5. Core10へConcept画像を登録した。
6. 英語版新UIを基礎に、臺灣華語専用UIを作成した。
7. 最初のUI案に存在しないフィールド名が含まれ、裏面テンプレートでエラーが発生した。
8. `zh_tw_core10_master.csv`と`zh_tw_core10_anki.csv`を読み、実在するフィールド名と順序を確定した。
9. 正式17フィールドだけを使う修正版UIを作成し、テンプレートエラーを解消した。
10. 臺灣華語Core20の17フィールドCSV一式を作成した。
11. C0011～C0020の画像、繁體字、注音、拼音、TTSがPC版プレビューで正常表示された。
12. 今夜、AnkiDroidへ同期し、ダークモード、TTS、プルダウン、自動スクロールを確認する。
13. Forgottenカードを抽出するカスタム学習をAnkiDroid上で作成した。
14. Daily Trainingの設定画面をAnkiDroidで開くとアプリが終了する問題を確認した。
15. 設定は変更せず、AnkiDroidからAnkiWebへ同期し、当面様子を見る方針とした。
16. 次回は韓国語Core10フィールドマスターを最初に読み、韓国語Core20まで進める。

---

## 3．JANUS-13の基本構造

```text
経験・読書・実務・日常観測
  ↓
現代日本語で書く
  ↓
canonical化
  ↓
Concept候補を抽出
  ↓
Concept境界を人間が承認
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

- Novel：深い縦坑
- Essay：日々増える街路
- Concept ID：言語間の共通住所
- Concept画像：記憶風景としての入力信号
- Anki：多言語変換訓練
- FSRS：忘れやすさに応じた復習配分

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

## 5．Essayのディレクトリ構造

Essayは言語別に分割せず、経験単位のEssay IDを親にする。

```text
essay/
└─ E0001/
   ├─ E0001_ja.md
   ├─ E0001_en.md
   └─ E0001_zh-Hant-TW.md
```

設計原則：

> Essay IDが経験の中心であり、各言語は同じ経験を観測する面である。

---

## 6．E0001のcanonical状況

```text
E0001_ja.md          canonical
E0001_en.md          canonical
E0001_zh-Hant-TW.md  canonical
```

### 日本語タイトル

```text
「ロマる」からロマへ
```

### 英語タイトル

```text
From “Romaru” to the Roma
```

### 臺灣華語タイトル

```text
從「romaru」到羅姆人
```

三言語とも逐語対応ではなく、次の経験的な核を共有する。

```text
未知語を聞く
  ↓
意味を調べる
  ↓
過去の記憶へ接続する
  ↓
土地と移動を考える
  ↓
SNS上の新しい地面へ至る
```

臺灣華語版の中心文：

```text
人並不會失去腳下的地面。
人只是改變自己所連接的地面。
```

結末：

```text
我終究沒有找到那個詞的意思。
即使如此，那個詞仍然打開了一條路。
```

---

## 7．臺灣華語の言語識別子

今後のMEMORIOPOLIS / JANUS-13では、臺灣華語版を次へ統一する。

```text
zh-Hant-TW
```

内訳：

```text
zh   = 中国語
Hant = 繁體字
TW   = 臺灣
```

使用例：

```text
E0001_zh-Hant-TW.md
zh-Hant-TW_core20_master_17fields.csv
zh-Hant-TW_core20_anki_17fields.csv
```

YAML：

```yaml
language: zh-Hant-TW
```

基準：

- 繁體字
- 臺灣で自然な語彙
- 注音を第一の発音観測面とする
- 拼音を補助観測面とする
- TTSは`zh_TW`

---

## 8．Core20正式Concept

| ID | 日本語Concept | 英語 | 臺灣華語 |
|---|---|---|---|
| C0011 | ある | exist | 存在 |
| C0012 | する | do | 做 |
| C0013 | 持つ | have | 擁有 |
| C0014 | 送る | send | 傳送 |
| C0015 | 受け取る | receive | 接收 |
| C0016 | 聞く | hear | 聽見 |
| C0017 | 調べる | look up | 查詢 |
| C0018 | 移る | move | 轉移 |
| C0019 | 結びつく | connect | 連結 |
| C0020 | 縛られる | be bound | 受到束縛 |

配分：

```text
計画配分枠：5
E0001実出現枠：3
縁・発見枠：2
```

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

全言語共通画像フィールド：

```text
ConceptScene
```

同じConcept IDでは全言語が同じWebP画像を共有する。

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

## 10．臺灣華語ノートタイプの正式17フィールド

Core10フィールドマスターから確定した正式構造：

```text
1. ID
2. TraditionalChinese
3. Zhuyin
4. Pinyin
5. Japanese
6. PartOfSpeech
7. TaiwanMandarinGrammar
8. ExampleTraditionalChinese
9. ExampleZhuyin
10. ExamplePinyin
11. ExampleJapanese
12. Source
13. Tags
14. ExampleBreakdown
15. ExampleExplanation
16. ExamplePronunciationHint
17. ConceptScene
```

既存16フィールドの順番は変更せず、`ConceptScene`を末尾へ追加した。

---

## 11．臺灣華語新UI

正式修正版：

```text
TAIWANESE_MANDARIN_UI_zh-Hant-TW_17FIELDS_CORRECTED_2026-09-27.md
```

### 表面

```text
Concept ID            臺灣華語
Concept画像
繁體字
注音
拼音
TTS
```

### 背面の初期表示

```text
日本語Concept
品詞
臺灣華語例文
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

- 繁體字
- 注音
- 拼音・声調
- TaiwanMandarinGrammar

#### 例文解説

- 例文注音
- 例文拼音
- 文の組み立て
- なぜこの意味になるか

#### 言語間ブリッジ

- ExamplePronunciationHint
- 繁體字、日本語漢字、注音、拼音を一つのConceptへ接続する橋

### 解答開始位置

必ず保持する。

```html
<div id="answer" class="answer-divider">
  <span>CONCEPT BRIDGE</span>
</div>
```

`id="answer"`が、AnkiDroidで`Show answer`を押した際の自動スクロール位置になる。

---

## 12．本日の手戻りと原因

最初の臺灣華語UI案では、実データを確認する前に理想的なフィールド構成を仮定した。

存在しなかった例：

```text
ExampleChinese
ChineseGrammar
CharacterStructure
LanguageBridge
ConceptContrast
CourseTags
```

実際のフィールド：

```text
ExampleTraditionalChinese
TaiwanMandarinGrammar
Tags
```

Ankiは裏面テンプレート内の次を検出し、エラーを表示した。

```text
{{#ExampleChinese}}
```

原因：

> 共通UIの概念設計を、既存ノートタイプの実フィールド確認より先に行った。

---

## 13．再発防止ルール

今後、Anki UIまたはCore CSVを作る際は、必ず次の順序を守る。

```text
Core10フィールドマスターを取得
  ↓
ヘッダーを読み、実在フィールド名を確定
  ↓
大文字・小文字を含め完全一致を確認
  ↓
フィールド順と既存列数を確定
  ↓
ConceptScene追加後の列数を確定
  ↓
表面・裏面・CSSを生成
  ↓
Core20 CSVを同じ順序で生成
  ↓
全行の列数を確認
  ↓
Concept IDの連番を確認
  ↓
画像参照を確認
  ↓
SourceとTagsを確認
  ↓
ZIP化
```

### 生成前チェック

```text
1. 実在フィールド名
2. 大文字・小文字
3. フィールド順
4. 既存列数
5. 追加後列数
6. TTS対象フィールド
7. 例文フィールド
8. Sourceフィールド
9. Tagsフィールド
10. ConceptScene位置
```

### 生成後チェック

```text
1. 全行の列数が同一
2. IDがCxxxxの連番
3. 見出し語、注音、拼音の対応
4. ConceptScene画像名の一致
5. テンプレート内に未存在フィールドがない
6. 裏面にid="answer"がある
7. Sourceに不要なdraft表記がない
8. ZIP内部ファイルが想定どおり
```

### 次回からの運用

> テンプレートを先に設計せず、フィールドマスターを先に読む。

共通UIの外装は再利用するが、データ参照は必ず言語ごとの実フィールドマスターから組み立てる。

---

## 14．設計書と引き継ぎ書

本日、手戻りの再発防止策として、完全版引き継ぎ書だけでなく、恒常的な設計書を作成・保守する案が出た。

ただし、JANUS-13は現在も次の仕様を改善中である。

- 共通UI
- 言語別フィールド
- Concept画像
- 3段プルダウン
- Source命名
- EssayからAnkiへの自動化
- TTS
- 言語間ブリッジ

現段階で設計書を固定すると、変更追随の負荷が大きくなる可能性がある。

当面：

```text
完全版引き継ぎ書
＋
言語別フィールドマスター
＋
再発防止チェックリスト
```

仕様が安定した段階で再考する。

将来候補：

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

## 15．臺灣華語Core20 CSV

完成ZIP：

```text
MEMORIOPOLIS_zh-Hant-TW_Core20_17fields_2026-09-27.zip
```

収録：

```text
README.md
zh-Hant-TW_core20_master_17fields.csv
zh-Hant-TW_core20_anki_17fields.csv
```

Source：

```text
E0001_zh-Hant-TW
```

Tags：

```text
memoriopolis::zh_hant_tw::core20
```

インポート後、PC版でC0011の正常表示を確認した。

確認済み：

- Concept画像
- `存在`
- `ㄘㄨㄣˊ ㄗㄞˋ`
- `cúnzài`
- TTSボタン
- C0011～C0020の新規カード登録

今夜はC0020も含めてAnkiDroidで確認する。

---

## 16．今夜のAnkiDroid確認項目

### 表面

- Core10・Core20画像が欠落しない
- 画像の縦横比が維持される
- `臺灣華語`バッジが表示される
- 繁體字が明瞭
- 注音の声調記号が表示される
- 拼音のアクセント記号が文字化けしない
- `zh_TW` TTSが動作する

### 背面

- `Show answer`で`CONCEPT BRIDGE`へ移動する
- 日本語Conceptと品詞が表示される
- 臺灣華語例文が表示される
- 例文TTSが動作する
- 日本語訳が表示される
- 3段プルダウンが開閉できる
- 注音・拼音が枠からはみ出さない
- Sourceが`E0001_zh-Hant-TW`になっている

### ダークモード

- 繁體字が背景へ沈まない
- 翡翠色の注音が読める
- 拼音が十分に明るい
- 紫・青・緑の見出しが区別できる
- プルダウン内部の日本語解説が読める

### 長いカード

C0020：

```text
受到束縛
ㄕㄡˋ ㄉㄠˋ ㄕㄨˋ ㄈㄨˊ
shòudào shùfú
```

長い見出し語、4音節の注音、拼音、長文例文を重点確認する。

---

## 17．Daily TrainingとForgottenカスタム

### JANUS-13 Daily Training

従来構成：

```text
第1フィルター
デッキ：MEMORIOPOLIS
期限：is:due

第2フィルター
デッキ：MEMORIOPOLIS
新規：is:new
```

現在のAnkiWeb表示：

```text
JANUS-13 Daily Training
新規 10
学習中 0
復習 15
```

### Forgottenカスタム

AnkiDroid上で作成し、再構築に成功した。

検索式：

```text
rated:7:1 deck:MEMORIOPOLIS
```

意味：

```text
過去7日以内にAgainで解答した
かつ
MEMORIOPOLIS配下のカード
```

現在のAnkiWeb表示：

```text
Custom Study Session
新規 0
学習中 0
復習 17
```

これはFSRSの予測上忘れそうなカードではなく、実際に直近7日で`Again`になったカードを集める補助フィルターである。

---

## 18．AnkiDroidのDaily Training問題

### 現象

- ForgottenカスタムはAnkiDroidで再構築できる。
- Daily TrainingのオプションをAnkiDroidで開こうとすると、エラーポップアップ後にAnkiDroidが終了する。
- Daily TrainingはPC版で再構築できる。
- Daily TrainingはAnkiWebへ同期され、カード数も表示される。

### 現時点の見立て

PC版で作成したこと自体が原因とは限らない。

可能性：

1. AnkiDroidのフィルターデッキオプション画面の不具合
2. Daily Trainingの二段フィルターとの組み合わせ
3. 過去バージョンで保存された設定との互換性
4. WebViewや端末環境
5. 特定設定データの破損

### 本日の方針

設定は変更しない。

```text
AnkiDroid
  ↓
AnkiWebへ同期
  ↓
しばらく現状を観測
```

当面：

- Daily Trainingの設定編集・再構築はPC版Ankiで行う。
- AnkiDroidでDaily Trainingのオプションを無理に開かない。
- Forgottenカスタムは補助観測として扱う。
- FSRS設定は変更しない。
- Daily Trainingの削除・再作成は、必要性が明確になるまで行わない。

---

## 19．FSRSと同じカードが出る感覚

Daily Trainingで同じ語が多く出るように感じた理由：

- 難しいカードはFSRSで間隔が短くなる。
- `Again`になったカードはForgottenにも入る。
- 容易なカードは数週間から1か月先へ送られる。
- 言語ごとに均等な枚数は出ない。

韓国語の「検証」が多く出ていたのは、そのカードが実際に弱かった可能性が高い。

今後の方針：

> 新しいトレーニングメニューを増やすより、Coreを充実させる。

新Coreの例文で既存Conceptが再登場し、別の経路から再会できる。

```text
カード単体の復習
＋
新例文での再登場
＋
Concept画像での再認
＋
他言語からの再接続
```

---

## 20．次回：韓国語Core20

次回は、作業開始時に韓国語Core10フィールドマスターをアップロードする。

推奨ファイル：

```text
ko_core10_master.csv
ko_core10_anki.csv
```

### 固定手順

```text
韓国語Core10フィールドマスターを取得
  ↓
実在フィールド名と順序を確定
  ↓
ConceptSceneを末尾へ追加
  ↓
正式フィールドだけでUIを作成
  ↓
Core10画像を登録
  ↓
PC版プレビュー
  ↓
E0001韓国語版を作成
  ↓
韓国語Core20 CSVを作成
  ↓
画像参照・列数・IDを確認
  ↓
Ankiインポート
  ↓
AnkiDroid確認
```

### 韓国語で観測したい要素

既存フィールドに存在する範囲で次を扱う。

```text
ハングル表記
音節ブロック
発音
語幹
語尾
助詞
終声
音韻変化
活用
漢字語／固有語
日本語との意味差
```

理想フィールドを先に仮定しない。

---

## 21．EssayからAnkiまでの半自動化

技術的には可能。

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

ただし、各言語のAnki生成前に、その言語のCore10フィールドマスターを必須入力とする。

自動化入力へ追加：

```text
field_masters/<language>_core10_master.csv
```

これにより、実ノートタイプと生成物の不一致を防ぐ。

---

## 22．次回開始用プロンプト

```text
この引き継ぎ書を2026年9月27日の最新状態としてMEMORIOPOLIS / JANUS-13を再開します。

E0001_ja.md、E0001_en.md、E0001_zh-Hant-TW.mdはcanonicalです。臺灣華語関連の言語識別子は今後zh-Hant-TWへ統一します。

臺灣華語ノートタイプは、既存16フィールドの末尾へConceptSceneを追加した17フィールド構成です。正式フィールド名は、ID、TraditionalChinese、Zhuyin、Pinyin、Japanese、PartOfSpeech、TaiwanMandarinGrammar、ExampleTraditionalChinese、ExampleZhuyin、ExamplePinyin、ExampleJapanese、Source、Tags、ExampleBreakdown、ExampleExplanation、ExamplePronunciationHint、ConceptSceneです。

臺灣華語Core10にはConcept画像を導入済みです。修正版UIはTAIWANESE_MANDARIN_UI_zh-Hant-TW_17FIELDS_CORRECTED_2026-09-27.mdです。臺灣華語Core20 CSVはMEMORIOPOLIS_zh-Hant-TW_Core20_17fields_2026-09-27.zipに収録されています。PC版ではC0011の画像、存在、注音、拼音、TTSが正常表示されています。

今夜、AnkiDroidで臺灣華語Core20の画像、zh_TW TTS、ダークモード、3段プルダウン、id=answerによる自動スクロール、C0020の長い見出しを確認します。

明日は韓国語Core20を作成します。作業開始時に韓国語Core10のmaster CSVとAnki CSVをアップロードします。必ずフィールドマスターを先に読み、実在フィールド名と順序を確定してから、UIとCSVを生成してください。理想フィールドを先に仮定しないでください。

AnkiDroidではForgottenカスタムの再構築は成功しています。検索式はrated:7:1 deck:MEMORIOPOLISです。一方、JANUS-13 Daily TrainingのオプションをAnkiDroidで開くとアプリが終了します。当面は設定を変更せず、AnkiDroidからAnkiWebへ同期して観測します。Daily Trainingの編集・再構築はPC版Ankiで行い、削除・再作成は行いません。

新しいトレーニングメニューを増やすより、Coreを充実させ、FSRSに弱いカードを選ばせます。
```

---

## 23．2026年9月27日の店じまい地点

- E0001日本語：canonical
- E0001英語：canonical
- E0001臺灣華語：canonical
- 臺灣華語識別子：`zh-Hant-TW`へ統一
- 臺灣華語Core10画像：対応済み
- 臺灣華語新UI：修正版完成
- 臺灣華語正式フィールド：17個
- 臺灣華語Core20 CSV：完成
- 臺灣華語Core20画像参照：設定済み
- PC版C0011：正常表示
- 今夜：AnkiDroidで実機確認
- UI手戻り原因：実フィールド確認前の理想フィールド仮定
- 再発防止：フィールドマスター先行
- 設計書：仕様安定後に再考
- Forgottenカスタム：AnkiDroidで再構築可能
- Forgotten検索：`rated:7:1 deck:MEMORIOPOLIS`
- Daily Training：AnkiDroidのオプションでアプリ終了
- Daily Training：設定変更せず同期して観測
- FSRS：設定変更なし
- 学習方針：メニューを増やさずCoreを充実
- 次回：韓国語Core20
- 次回必須入力：韓国語Core10フィールドマスター

本日の最終合意：

> JANUS-13の共通UIは再利用するが、各言語のデータ構造は必ず実在するCore10フィールドマスターから組み立てる。仕様が安定するまでは完全版引き継ぎ書とチェックリストを維持し、恒常的な設計書は安定後に再考する。
