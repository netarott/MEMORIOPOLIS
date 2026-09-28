# MEMORIOPOLIS / JANUS-13 完全版引き継ぎ書

更新日時：2026年9月26日 15:30 JST  
版：E0001 canonical・English Core20・自動化構想統合版  
次回作業日：2026年9月27日

---

## 1．本書の目的

本書は、2026年9月26日時点のMEMORIOPOLIS / JANUS-13について、Essay E0001、Core20、Concept画像、英語版Anki、共通UI、学習統計、次回の臺灣華語版作業、およびEssayからJANUS-13 Ankiまでの自動化構想を引き継ぐ完全版文書である。

---

## 2．本日の主要成果

1. `essay/E0001/`を経験単位の親フォルダとして採用した。
2. `E0001_ja.md`を現代日本語正本としてcanonical化した。
3. `E0001_en.md`を自然な英語Essayとしてcanonical化した。
4. Core20のConceptを正式決定した。
5. Core20のConcept画像10景を作成、分割、ZIP化した。
6. Englishノートタイプへ`ConceptScene`を追加した。
7. English Core10へConcept画像を配置した。
8. Englishカードを新しい共通UIへ改修した。
9. 3段プルダウンが正常に動作することを確認した。
10. AnkiDroidで解答面へ自動スクロールしない問題を修正した。
11. English Core20の17フィールドCSVを作成した。
12. 本日の学習で、カード総数140枚、定着35枚まで進んだ。
13. 次回は臺灣華語版のCore20まで進める方針を決定した。

---

## 3．日本語Novelと日本語Ankiの正

### Novel

```text
日本語Novel
├─ 現代日本語版
└─ 近代日本語版
```

### Anki

日本語系Ankiの唯一の正は次である。

```text
MEMORIOPOLIS::ModernJapanese
```

- 現代日本語専用Ankiデッキは作らない。
- ModernJapanese内で近代日本語表記、現代日本語表記、現代読み、四つの橋を保持する。
- 作品・Concept上は13言語・14観測面、Anki上は13言語デッキである。

---

## 4．Essayのディレクトリ構造

言語別フォルダではなく、経験単位であるEssay IDを親にする。

```text
essay/
└─ E0001/
   ├─ E0001_ja.md
   └─ E0001_en.md
```

今後ほかの言語版を作る場合も、同じE0001フォルダへ追加する。

```text
E0001/
├─ E0001_ja.md
├─ E0001_en.md
├─ E0001_zh-Hant-TW.md
├─ E0001_ko.md
├─ E0001_ru.md
└─ ...
```

設計原則：

> Essay IDが経験の中心であり、各言語は同じ経験を観測する面である。

---

## 5．E0001 canonical

### 日本語正本

```text
E0001_ja.md
status: canonical
```

タイトル：

```text
「ロマる」からロマへ
```

### 英語正式版

```text
E0001_en.md
status: canonical
canonical_source: E0001_ja.md
```

英語タイトル：

```text
From “Romaru” to the Roma
```

逐語訳ではなく、次の経験的な核を保つ自然な英語版とした。

```text
未知語を聞く
  ↓
意味を調べる
  ↓
ロマの記憶へ接続する
  ↓
土地と移動を考える
  ↓
SNS上の新しい地面へ至る
```

中心文：

```text
People do not lose the ground beneath them.
They change the ground to which they are connected.
```

結末：

```text
I never found the meaning of the word.
Even so, the word opened a path.
```

---

## 6．Core20正式決定

| ID | 日本語Concept | 英語 | 選定枠 |
|---|---|---|---|
| C0011 | ある | exist | 計画配分 |
| C0012 | する | do | 計画配分 |
| C0013 | 持つ | have | 計画配分 |
| C0014 | 送る | send | 計画配分 |
| C0015 | 受け取る | receive | 計画配分 |
| C0016 | 聞く | hear | E0001実出現 |
| C0017 | 調べる | look up | E0001実出現 |
| C0018 | 移る | move | E0001実出現 |
| C0019 | 結びつく | connect | 縁・発見 |
| C0020 | 縛られる | be bound | 縁・発見 |

配分：

```text
計画配分枠：5
E0001実出現枠：3
縁・発見枠：2
```

Core10が名詞中心だったため、Core20は動詞・状態・関係Conceptを中心とし、Core10の名詞を動かす。

---

## 7．Core20 Concept画像

完成ZIP：

```text
MEMORIOPOLIS_ConceptImages_C0011-C0020_2026-09-26.zip
```

配置先：

```text
MEMORIOPOLIS/
└─ language/
   └─ glossary/
      └─ MEMORIOPOLIS_ConceptImages_C0011-C0020_2026-09-26/
```

対応ファイル：

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

- WebP：Anki用
- PNG：GitHub保存用
- 同じConcept IDでは全言語が同じ画像を共有する。
- 画像内文字、人物、列車、都市、土地、星図、接続、制約を記憶入力として保持する。

---

## 8．English新UI

英語版UIをJANUS-13共通デザインの新基準とする。

### 表面

```text
Concept ID          ENGLISH
Concept画像
英単語
IPA
TTS
```

### 背面の初期表示

```text
日本語Concept
品詞
英語例文
例文TTS
日本語訳
```

### 3段プルダウン

```text
語の構造
例文解説
言語間ブリッジ
```

色：

- 金：Concept ID、区切り
- 紺：英語と主要情報
- 紫：語の構造
- 青：例文解説
- 緑：言語間ブリッジ

ダークモード、AnkiDroid、長文折り返しに対応済み。

---

## 9．解答面自動スクロールの修正

English新UIへの変更後、AnkiDroidで`Show answer`を押した際、解答面開始位置へ自動移動しなくなった。

原因は、従来の次のアンカーを外したことだった。

```html
<hr id="answer">
```

独自区切りへ次のIDを追加して修正した。

```html
<div id="answer" class="answer-divider">
  <span>CONCEPT BRIDGE</span>
</div>
```

今後、全言語の新UIで必ず`id="answer"`を保持する。

---

## 10．English Core20 CSV

完成ZIP：

```text
MEMORIOPOLIS_English_Core20_17fields_2026-09-26.zip
```

収録物：

```text
README.md
en_core20_anki_17fields.csv
en_core20_master_17fields.csv
```

17フィールド：

```text
1. ID
2. English
3. IPA
4. Japanese
5. PartOfSpeech
6. EnglishGrammar
7. ExampleEnglish
8. ExampleIPA
9. ExampleJapanese
10. Source
11. CourseTags
12. ExampleBreakdown
13. ExampleExplanation
14. ExamplePronunciationHint
15. UsageNote
16. ConceptContrast
17. ConceptScene
```

Source：

```text
E0001_en
```

Tag：

```text
memoriopolis::en::core20
```

ConceptSceneにはWebPへのHTML参照を保持する。

---

## 11．2026年9月26日のAnki統計

統計取得：2026年9月26日 15:13:50

### 本日

- 学習時間：18.09分
- 解答カード：50枚
- 1枚あたり：21.7秒
- `もう一度`：5回、10％
- 学習：12
- 復習：35
- 再学習：3
- 明日の復習期限：15回

### 過去31日

- 学習日数：18日、58.06％
- 合計復習：1,881回
- 期間平均：1日61回
- 学習日の平均：1日105回

### カード内訳

- 合計：140枚
- 定着前：105枚、75％
- 定着：35枚、25％
- 新規：0
- 学習中：0
- 再学習中：0
- 休止：0

### 記憶状態

- 復習間隔中央値：10日
- 安定性中央値：11日
- 難しさ中央値：12％
- 平均予測想起率：97％
- 現在覚えている推定数：136枚／136ノート

### 保持率

- 今日：85.7％、35回
- 昨日：75.7％、37回
- 過去1週間：78.2％、229回
- 過去1か月：82.2％、297回

カード総数と復習量が増えた一方、安定性と予測想起率も上昇している。現時点でFSRS設定は変更しない。

---

## 12．統計的カバー率と経験的カバー率

### 統計的カバー率

一般コーパスに対する既知語率。

### 経験的カバー率

篠原さんのNovel、Essay、読書記録、実務経験を、対象言語で認識・再構成・変換できる割合。

JANUS-13の主指標は経験的カバー率である。

外部コーパス：

```text
欠落と偏りを発見する監査表
```

自己コーパス：

```text
Conceptの発生源
```

例文：

```text
Conceptが記憶都市に住所を得た出生記録
```

---

## 13．EssayからJANUS-13 Ankiまでの自動化

### 結論

技術的には可能である。

現代日本語Essayがcanonicalになった時点から、次を自動生成できる。

```text
canonical日本語Essay
  ↓
Concept候補抽出
  ↓
既存Conceptとの重複・境界確認
  ↓
計画枠・実出現枠・発見枠への分類
  ↓
Core10候補表
  ↓
各Conceptの日本語定義・例文
  ↓
Concept画像10景
  ↓
対象言語Essay
  ↓
対象言語Ankiフィールド
  ↓
Master CSV
  ↓
Anki CSV
  ↓
ConceptScene参照
  ↓
ZIP
```

### 完全自動化にしない部分

JANUS-13の核を守るため、次の二つだけは人間の承認ゲートとして残す。

#### Gate 1：現代日本語Essayのcanonical化

篠原さんが経験の正本を確定する。

#### Gate 2：Concept選定と境界の確定

AIが候補と配分案を提示し、篠原さんが正式Concept IDを決定する。

この二段階の承認後は、画像、各言語版、Anki CSV、README、manifest、ZIP作成まで高度に自動化できる。

### なぜ完全自動選定を避けるか

- 一般頻度語へ偏る危険がある。
- 篠原さんにとっての経験的な重要度をAIだけでは決定できない。
- 「調べる／確認する／検証する」のようなConcept境界はプロジェクト思想に関わる。
- 例文を教科書的な文へ平板化する危険がある。
- 大量生成がNovel、Essay、読書時間を圧迫する可能性がある。

### 推奨する半自動パイプライン

```text
[人間]
E000n_ja.mdをcanonical化

[自動]
候補語、配分、重複、境界案を生成

[人間]
Core10を承認しConcept IDを固定

[自動]
日本語Anki
画像10景
英語Essay
英語Anki
臺灣華語Essay・Anki
韓国語Essay・Anki
その他言語
README
manifest
ZIP

[人間]
AnkiDroid実機確認

[自動]
GitHubコミット候補と引き継ぎ書を生成
```

### 自動化の入力

```text
essay/E000n/E000n_ja.md
concept_registry.csv
allocation_policy.md
language_profiles/
anki_templates/
concept_image_policy.md
```

### 自動化の出力

```text
essay/E000n/E000n_<language>.md
language/anki/<language>/coreXX_master.csv
language/anki/<language>/coreXX_anki.csv
language/glossary/MEMORIOPOLIS_ConceptImages_Cxxxx-Cxxxx_<date>/
manifest.csv
README.md
handoff.md
```

### 実装単位

将来的に、PowerShellまたはPythonの一つのオーケストレーターから実行できる。

```text
janus13-build E0002 --target English
janus13-build E0002 --target TaiwaneseMandarin
janus13-build E0002 --target all
```

ただし、`--target all`はConcept承認後だけ許可する。

### 最終的な目標

> 篠原さんは日記感覚で現代日本語Essayを書き、推敲してcanonical化する。JANUS-13は、その経験を壊さずにConcept、画像、言語間ブリッジ、各言語Ankiへ展開する。

---

## 14．NovelとEssayの役割差

### Novel

- 一本を作るのに時間がかかる。
- 世界観、制度、人物、物語を深く構築する。
- MEMORIOPOLIS固有Conceptを供給する。
- 長期的なConceptの背骨になる。

### Essay

- 日記感覚で書ける。
- 日常観測、読書、ニュース、実務をすぐ自己コーパスへ変換できる。
- 基本動詞、生活語、思考語、評価語、機能語を供給する。
- 経験的カバー率を継続的に高める。

したがって、Novelの完成を待たず、Essayを日常的なConcept供給経路として運用する。

```text
Novel ＝ 深い縦坑
Essay ＝ 日々増える街路
```

両方が記憶都市を成長させる。

---

## 15．次回：臺灣華語版Core20

次回の目標：

1. E0001の臺灣華語版ファイル名とメタデータを確定する。
2. 臺灣華語のCore10へConcept画像を展開する。
3. English新UIを基準に臺灣華語UIを改修する。
4. 臺灣華語固有の「語の構造」を設計する。
5. Core20の臺灣華語語形・注音・拼音・声調を作る。
6. Core20の例文をE0001の経験的な核から作る。
7. 例文解説を作る。
8. 言語間ブリッジを作る。
9. Core20画像参照を付ける。
10. Master CSVとAnki CSVを作成する。
11. Ankiへインポートする。
12. AnkiDroidで確認する。

### 臺灣華語の語の構造

```text
繁体字
注音
拼音
声調
字ごとの基本義
複合語としての意味
量詞
語順
日本語漢字との共通点・差
```

### UI

English新UIの外装を基準とする。

```text
Concept ID        臺灣華語
Concept画像
繁体字
注音・拼音
TTS
```

裏面：

```text
日本語Concept
品詞
例文
例文TTS
日本語訳
語の構造
例文解説
言語間ブリッジ
```

必ず解答開始位置へ次を置く。

```html
id="answer"
```

---

## 16．次回開始用プロンプト

```text
この引き継ぎ書を2026年9月26日の最新状態としてMEMORIOPOLIS / JANUS-13を再開します。

E0001_ja.mdとE0001_en.mdはcanonicalです。Core20は、C0011ある、C0012する、C0013持つ、C0014送る、C0015受け取る、C0016聞く、C0017調べる、C0018移る、C0019結びつく、C0020縛られるで正式決定済みです。

Core20画像10景は完成・分割・ZIP化済みです。EnglishはCore10画像、新共通UI、3段プルダウン、ダークモード、AnkiDroid対応まで完了しています。解答面の自動スクロールには、裏面開始区切りのid="answer"が必須です。

English Core20の17フィールドCSVも完成済みです。SourceはE0001_en、タグはmemoriopolis::en::core20です。

本日の目標は臺灣華語版のCore20まで完成させることです。まずCore10へConcept画像を追加し、English新UIを基準に臺灣華語の前面、背面、CSSを設計してください。ただし、語の構造は繁体字、注音、拼音、声調、字義、複合語、量詞、日本語漢字との差を扱う臺灣華語専用プロファイルにしてください。

次にE0001の臺灣華語版、Core20の語彙、自然な例文、例文解説、言語間ブリッジ、17フィールド以上のMaster CSVとAnki CSV、ConceptScene参照を作成し、AnkiDroidで確認します。

EssayからJANUS-13 Ankiまでの自動化は可能です。ただし、現代日本語Essayのcanonical化と、Concept選定・境界確定の二つを人間の承認ゲートとして残します。その後は画像、各言語版、Anki CSV、README、manifest、ZIP、引き継ぎ書まで自動化する方針です。
```

---

## 17．2026年9月26日の店じまい地点

- E0001日本語：canonical
- E0001英語：canonical
- Core20：正式決定
- Core20画像：完成
- English Core10画像：対応済み
- English新UI：完成
- English 3段プルダウン：動作確認済み
- Englishダークモード：対応済み
- 解答面自動スクロール：修正済み
- English Core20 CSV：完成
- Ankiカード総数：140
- 定着カード：35
- 安定性中央値：11日
- 平均予測想起率：97％
- 次回：臺灣華語版Core20まで
- 自動化：技術的に可能
- 人間の承認ゲート：日本語canonical化、Concept確定
- 自動化後工程：画像、多言語版、Anki CSV、ZIP、引き継ぎ書

本日の最終合意：

> Novelは記憶都市の深い縦坑であり、Essayは日々増える街路である。現代日本語Essayがcanonicalになり、Conceptが承認された後は、その経験を壊さずにJANUS-13の画像、多言語版、言語間ブリッジ、Ankiまで自動展開する。
