# MEMORIOPOLIS / JANUS-18 完全版引き継ぎ書

更新日時：2026年10月1日 14:08 JST  
版：音優先型UI・Filipino Core20・Indonesian Core20・CLASSICA-5 Bridge/Depth統合版  
次回作業日：2026年10月2日

---

## 36．2026年9月29日の主要成果

本日はLIVING-13のロシア語面を整備した。

1. `ru_core10_master.csv`と`ru_core10_anki.csv`を確認した。
2. ロシア語Core10の既存16フィールドと列順を正式なフィールドマスターとして確定した。
3. ロシア語ノートタイプには`ConceptScene`がすでに追加済みであることを確認した。
4. ロシア語ノートタイプを正式17フィールド構成として確定した。
5. 英語版、臺灣華語版、韓国語版と共通する新UIへ更新した。
6. ロシア語固有の強勢、ラテン文字転写、格変化、動詞の体を観測しやすいカード構造を作成した。
7. `E0001_ru.md`を逐語訳ではなく、自然なロシア語Essayとして作成した。
8. 内容確認後、ロシア語版を正本として承認した。
9. `E0001_ru_canonical.md`をCore20パッケージへ同梱した。
10. ロシア語Core20の17フィールドCSV一式を作成した。
11. C0011からC0020まで、強勢、転写、文法、例文、解説、発音ヒント、画像参照を整備した。
12. 帰り道と就寝前に、AnkiDroidでロシア語Core20を確認する予定とした。
13. 本日の制作作業は完了し、ここで店じまいとした。

---

## 37．E0001正本状況

2026年9月29日時点の正本状況：

```text
E0001_ja.md          canonical
E0001_en.md          canonical
E0001_zh-Hant-TW.md  canonical
E0001_ko.md          canonical
E0001_ru.md          canonical
```

ロシア語版の正本ファイル名：

```text
E0001_ru.md
```

ロシア語Core20パッケージには、正本状態を明示した次のファイルも同梱した。

```text
E0001_ru_canonical.md
```

Source表記：

```text
E0001_ru
```

---

## 38．E0001ロシア語版

タイトル：

```text
От «ромару» к рома
```

「ロマる」は、意味が確定していない聞き取り語であるため、既存のロシア語へ意味変換せず、音を写した`ромару`として保持した。

### 38.1 中心命題

```text
Человек не теряет землю под ногами.
Он лишь меняет землю, с которой связан.
```

対応する日本語Concept：

```text
人は、地面を失うのではない。
接続する地面を変える。
```

ロシア語版では、`земля под ногами`が物理的な地面だけでなく、生活や存在の足場も連想できる表現になっている。

### 38.2 結末

```text
Значения слова я так и не нашёл.
И всё же оно открыло новый путь.
```

意味：

```text
言葉の意味は、結局見つからなかった。
それでも、その言葉は新しい道を開いた。
```

### 38.3 語彙上の重要な選択

```text
земля
＝ 土地、大地、足元の地面、帰属する場所

почва
＝ 土壌、物質としての土、比喩的な基盤

быть связанным
＝ 構造的・関係的につながっている

быть привязанным
＝ 何かに結び付けられ、依存または拘束されている

быть скованным
＝ より強く拘束・束縛されている
```

ロシア語版では、接続と拘束を一語へまとめず、意味の濃淡を分けて表現した。

### 38.4 翻訳方針

- 日本語の語順をそのまま移さない。
- ロシア語の論理展開と段落のリズムを優先する。
- 未知語、記憶、土地、移動、プラットフォームへ進む経験的な核を維持する。
- 個人的観測、記憶、資料上の情報、仮説を区別する。
- ロシア語独自の土地、接続、拘束の語感を活かす。
- 語の意味が不明なままでも、思考の経路が開かれる結末を維持する。

---

## 39．ロシア語ノートタイプの正式17フィールド

```text
1. ID
2. Russian
3. Stress
4. Transliteration
5. Japanese
6. PartOfSpeech
7. RussianGrammar
8. ExampleRussian
9. ExampleStress
10. ExampleTransliteration
11. ExampleJapanese
12. Source
13. Tags
14. ExampleBreakdown
15. ExampleExplanation
16. ExamplePronunciationHint
17. ConceptScene
```

`ConceptScene`は追加済みである。

既存フィールドの順序は変更しない。

---

## 40．ロシア語Anki UI

完成ファイル：

```text
RUSSIAN_CARD_UI_17FIELDS_CONCEPTSCENE_3PANELS_2026-09-29.md
```

### 40.1 表面

```text
Concept ID                 РУССКИЙ
Concept画像
通常のキリル文字
強勢付き表記
ラテン文字転写
ru_RU単語TTS
```

例：

```text
запись
за́пись
zapisʹ
```

### 40.2 背面の初期表示

```text
CONCEPT BRIDGE
日本語Concept
品詞
ロシア語例文
強勢付き例文
ru_RU例文TTS
日本語訳
```

### 40.3 3段プルダウン

```text
語の構造
例文解説
言語間ブリッジ
```

#### 語の構造

- キリル文字
- 強勢付き表記
- ラテン文字転写
- 文法・語形変化

#### 例文解説

- 例文転写
- 文の組み立て
- なぜこの意味になるか

#### 言語間ブリッジ

- 音の橋
- キリル文字、強勢、転写、日本語Concept、Concept画像の接続

### 40.4 TTS

単語：

```html
{{tts ru_RU:Russian}}
```

例文：

```html
{{tts ru_RU:ExampleRussian}}
```

強勢記号付きフィールドは視覚学習用とし、TTSには通常表記を渡す。

### 40.5 自動スクロール

```html
<div id="answer" class="answer-divider">
  <span>CONCEPT BRIDGE</span>
</div>
```

`id="answer"`は削除しない。

### 40.6 UI整合性

- 正式17フィールド以外を参照していない。
- `ConceptScene`参照あり。
- `ru_RU`単語TTSあり。
- `ru_RU`例文TTSあり。
- `id="answer"`あり。
- ライトモード対応。
- ダークモード対応。
- AnkiDroidの画面幅に対応。
- 長い見出し語と例文の折り返しに対応。

---

## 41．ロシア語Core20

完成パッケージ：

```text
MEMORIOPOLIS_Russian_Core20_17fields_2026-09-29.zip
```

収録ファイル：

```text
README.md
ru_core20_master_17fields.csv
ru_core20_anki_17fields.csv
E0001_ru_canonical.md
```

Source：

```text
E0001_ru
```

Tags：

```text
memoriopolis::ru::core20
```

### 41.1 見出し語

```text
C0011 существовать       существова́ть
C0012 делать             де́лать
C0013 иметь              име́ть
C0014 отправлять         отправля́ть
C0015 получать           получа́ть
C0016 слышать            слы́шать
C0017 искать             иска́ть
C0018 переходить         переходи́ть
C0019 связываться        свя́зываться
C0020 быть привязанным   быть привя́занным
```

### 41.2 ロシア語固有の観測点

```text
動詞の不完了体・完了体
格支配
強勢位置
無強勢母音の弱化
硬音・軟音
再帰動詞の-ся / -сь
形動詞
副動詞
見出し語と活用形での強勢移動
過程と結果のConcept境界
```

### 41.3 重要なConcept境界

```text
существовать
＝ 抽象的・論理的に存在する
≠ есть / быть の所在・所有

делать
＝ 基本的な「する・作る」
≠ 日本語の「する」と完全な一対一ではない

иметь
＝ 明示的・抽象的所有
≠ 日常所有でよく使う у ... есть

слышать
＝ 耳に入る・聞こえる
≠ слушать の意識して聞く

искать
＝ 探す過程
↔ найти の見つける結果

переходить
＝ 場所、状態、話題、思考の焦点が移る

связываться
＝ 結びつく・関係を作る

быть привязанным
＝ 物理的、制度的、関係的に拘束される
```

### 41.4 整合性確認

- 10行すべて17列。
- C0011からC0020まで連番。
- 全行のSourceが`E0001_ru`。
- 全行のTagsが`memoriopolis::ru::core20`。
- 強勢付き見出し語を収録。
- Concept IDと画像ファイル名が一致。
- master版とAnki版の列順が一致。
- Core20画像参照を17列目に設定。

---

## 42．ロシア語Core20のインポート

1. Core20のWebP画像10枚をAnkiメディアへ配置する。
2. 次をインポートする。

```text
ru_core20_anki_17fields.csv
```

3. ロシア語ノートタイプを選択する。
4. デッキを選択する。

```text
MEMORIOPOLIS::Russian
```

5. 17列を順番どおり割り当てる。
6. フィールド内HTMLを許可する。
7. C0011、C0016、C0019、C0020をプレビューする。
8. PC版で画像、強勢、転写、TTS、3段プルダウンを確認する。
9. AnkiDroidへ同期する。

---

## 43．帰り道と就寝前のAnkiDroid確認

### 表面

- C0001からC0020までConcept画像が表示される。
- `РУССКИЙ`バッジが表示される。
- キリル文字が明瞭に表示される。
- 強勢記号が文字化けしない。
- ラテン文字転写が表示される。
- `ru_RU`単語TTSが動作する。

### 背面

- `Show answer`で`CONCEPT BRIDGE`へ移動する。
- 日本語Conceptと品詞が表示される。
- 通常例文と強勢付き例文が表示される。
- `ru_RU`例文TTSが動作する。
- 日本語訳が表示される。
- 3段プルダウンが開閉できる。
- 長文解説が自然に折り返される。
- Sourceが`E0001_ru`になっている。

### ダークモード

- キリル文字が背景へ沈まない。
- ルビー色の強勢付き表記が読める。
- 転写文字が十分に明るい。
- 紫、青、緑のプルダウン見出しを区別できる。
- 詳細欄の日本語解説が読める。

### 重点カード

```text
C0011 существовать
C0016 слышать
C0019 связываться
C0020 быть привязанным
```

C0019では再帰動詞と強勢移動を確認する。

C0020では、長い見出し語、強勢付き表記、転写、折り返し、TTSを重点確認する。

---

## 44．記憶術の読書とJANUS-18

就寝前に読んでいる例の2冊の記憶術関連書籍が、MEMORIOPOLISとAnki設計に継続的な刺激を与えている。

現時点で重要な気づき：

- 人間は土地、建物、部屋、経路について無意識に多くの情報を取り込む。
- 想起アンカーは、美しさ、奇想天外さ、強い違和感など、印象の強さによって競争力を持つ。
- 場所法は、記憶対象を空間上の住所へ配置し、再訪可能な経路を作る。
- 実在する場所だけでなく、写真、建築資料、想像上の都市も記憶宮殿になりうる。
- Concept画像は単なる装飾ではなく、想起を始動する視覚的アンカーである。
- Concept IDは、同じConceptへ戻るための不変の住所である。

JANUS-18での対応関係：

```text
Concept ID
＝ 記憶宮殿の住所

ConceptScene
＝ 住所に置かれた強いアンカー

Essay
＝ 住所どうしを結ぶ街路

LIVING-13
＝ 同じ住所へ向かう現代13言語の経路

CLASSICA-5
＝ 同じ住所の地下にある古典文明の地層

近代日本語
＝ 地表と地下をつなぐ階段

FSRS
＝ 各住所と経路を再訪する時刻表
```

この読書は余暇ではあるが、JANUS-18の設計思想と創作活動の重要な入力源として扱う。

書名や内容の詳細は、次回ユーザーから明示された場合に正確に追記する。現段階では推測で書名を固定しない。

---

## 45．JANUS-18の現在地

```text
JANUS-18
├─ LIVING-13
│  ├─ ModernJapanese
│  ├─ English       E0001 / Core20進行済み
│  ├─ zh-Hant-TW    E0001 / Core20進行済み
│  ├─ Korean        E0001 / Core20進行済み
│  ├─ Russian       E0001 / Core20進行済み
│  └─ 残りの現代語
│
└─ CLASSICA-5
   ├─ Classical Latin
   ├─ Ancient Greek
   ├─ Classical Sanskrit
   ├─ Biblical Hebrew
   └─ Classical Arabic
```

現在はLIVING-13のE0001円環を進めている。

CLASSICA-5の開始条件：

```text
E0001の現代語展開をドイツ語まで完成
  ↓
近代日本語で現代と過去を橋渡し
  ↓
C0001からC0020の古典語適合性を審査
  ↓
CLASSICA-5を各言語で一挙にCore20まで整備
```

---

## 46．次回作業

次回は、ロシア語AnkiDroid確認結果を最初に反映する。

問題がなければ、LIVING-13の次の現代語へ進む。

次の言語で必ず守る手順：

```text
Core10フィールドマスターを取得
  ↓
実在フィールド名と順序を確定
  ↓
ConceptSceneの有無を確認
  ↓
UIを共通外装へ更新
  ↓
フィールド参照を機械検査
  ↓
E0001対象言語版を自然な文章で作成
  ↓
canonical化
  ↓
Core20 CSVを作成
  ↓
列数、ID、Source、Tags、画像参照を確認
  ↓
PC版・AnkiDroidで確認
```

---

## 47．次回開始用プロンプト

```text
この引き継ぎ書を2026年9月29日の最新状態としてMEMORIOPOLIS / JANUS-18を再開します。

E0001_ja.md、E0001_en.md、E0001_zh-Hant-TW.md、E0001_ko.md、E0001_ru.mdはcanonicalです。

ロシア語ノートタイプは17フィールド構成です。正式フィールドは、ID、Russian、Stress、Transliteration、Japanese、PartOfSpeech、RussianGrammar、ExampleRussian、ExampleStress、ExampleTransliteration、ExampleJapanese、Source、Tags、ExampleBreakdown、ExampleExplanation、ExamplePronunciationHint、ConceptSceneです。

ロシア語UIはRUSSIAN_CARD_UI_17FIELDS_CONCEPTSCENE_3PANELS_2026-09-29.mdです。ロシア語Core20はMEMORIOPOLIS_Russian_Core20_17fields_2026-09-29.zipとして完成済みです。

帰り道と就寝前に、AnkiDroidで画像、強勢、転写、ru_RU TTS、3段プルダウン、id=answerによる自動スクロール、C0019とC0020の長い表示を確認します。問題があれば次言語へ進む前に修正します。

JANUS-18は、現代13言語のLIVING-13と古典5言語のCLASSICA-5からなる二重環です。CLASSICA-5は、E0001の現代語円環をドイツ語まで完成し、近代日本語で現代と過去を橋渡しした後に開始します。現代技術用語や法律用語を無理に古典語へ翻訳せず、近縁Concept、文明固有の再定義、直接対応なしを正式な観測結果として扱います。C0001だけの試験は行わず、各古典語を一挙にCore20まで整備します。

記憶術関連の例の2冊を就寝前に読み、場所法、強い想起アンカー、建築的な記憶宮殿の考え方を、Concept IDとConceptSceneの設計へ還流させています。
```

---

## 48．2026年9月29日の店じまい地点

- E0001ロシア語版：canonical。
- ロシア語Core10フィールドマスター：確認済み。
- ロシア語`ConceptScene`：追加済み。
- ロシア語正式フィールド：17個。
- ロシア語UI：新共通UIへ更新済み。
- ロシア語UIフィールド参照：整合性確認済み。
- ロシア語TTS：`ru_RU`。
- ロシア語Core20：完成。
- ロシア語Core20 Source：`E0001_ru`。
- ロシア語Core20 Tags：`memoriopolis::ru::core20`。
- ロシア語Core20画像参照：設定済み。
- AnkiDroid確認：帰り道と就寝前に実施予定。
- FSRS設定：変更なし。
- 学習方針：Daily Trainingを本線とし、Coreを充実させる。
- 記憶術読書：創作とAnki設計への重要な刺激として継続。
- JANUS-18：LIVING-13とCLASSICA-5の二重環。
- CLASSICA-5：ドイツ語までのE0001展開と近代日本語ブリッジ後に開始。
- 古典語方針：無理な直訳を避け、近縁Conceptと意味のずれを記録する。

本日の最終合意：

> ロシア語の街路とCore20を記憶都市へ接続した。帰り道と就寝前に実機上の経路を歩き、問題がなければLIVING-13の次の言語へ進む。記憶術の読書から得た場所法とアンカーの知見は、Concept IDとConceptSceneを核とするJANUS-18の記憶宮殿へ継続的に還流させる。

---

## 49．2026年9月30日から10月1日までの主要成果

この期間は、フィリピン語とインドネシア語のE0001・Core20を整備すると同時に、JANUS-18全体の学習方式を「音優先型」へ更新した。

### 49.1 フィリピン語

- `E0001_fil.md`を作成した。
- 内容確認後、`E0001_fil.md`を`canonical`として確定した。
- 既存18フィールドの末尾へ`ConceptScene`を追加した。
- フィリピン語ノートタイプを正式19フィールド構成とした。
- 共通外装と3段プルダウンを維持しながら、音優先型UIを初めて実装した。
- Windows版Ankiでは`fil_PH`のTTS音声がなくエラーになった。
- 実際の学習環境であるAnkiDroidでは、`fil_PH`の単語音声・例文音声とも正常に再生できた。
- 音を先に聞いてから「Conceptは何だったか」と想起する練習が成立した。
- フィリピン語Core20の19フィールドCSV一式を作成した。

完成ファイル：

```text
E0001_fil.md
FILIPINO_CARD_UI_19FIELDS_AUDIO_FIRST_CONCEPTSCENE_3PANELS_2026-09-30.md
MEMORIOPOLIS_Filipino_Core20_19fields_2026-09-30.zip
```

### 49.2 インドネシア語

- `id_core10_master.csv`と`id_core10_anki.csv`を確認した。
- 既存18フィールドと列順を正式なフィールドマスターとして確定した。
- 末尾へ`ConceptScene`を追加し、正式19フィールド構成とした。
- フィリピン語で確認できた音優先型UIを標準として適用した。
- `E0001_id.md`を自然なインドネシア語Essayとして作成した。
- 内容確認後、`E0001_id.md`を`canonical`として確定した。
- インドネシア語Core20の19フィールドCSV一式を作成した。
- Core20をAnkiDroidへ同期し、夜に実機確認する予定とした。

完成ファイル：

```text
E0001_id.md
INDONESIAN_CARD_UI_19FIELDS_AUDIO_FIRST_CONCEPTSCENE_3PANELS_2026-10-01.md
MEMORIOPOLIS_Indonesian_Core20_19fields_2026-10-01.zip
```

---

## 50．E0001のcanonical状況

2026年10月1日時点：

```text
E0001_ja.md          canonical
E0001_en.md          canonical
E0001_zh-Hant-TW.md  canonical
E0001_ko.md          canonical
E0001_ru.md          canonical
E0001_fil.md         canonical
E0001_id.md          canonical
```

E0001は日本語正本から各言語へ逐語的に置換せず、各言語で自然に読めるEssayとして再構成する。

正本化後の変更は、誤字修正、事実修正、明示的な改訂としてGitHub上で管理する。

---

## 51．音優先型UIをLIVING-13の標準とする

フィリピン語をAnkiDroidで確認した結果、音声を最初に提示すると、文字や画像を見て「分かった気になる」のではなく、音から記憶を検索する短い時間が生まれた。

実際の内的反応：

```text
音を聞く
  ↓
「えっと、このConceptは何だったっけ？」
  ↓
ConceptSceneまたは日本語Conceptを探す
  ↓
画像で住所を確認する
  ↓
見出し語、発音、語根、接辞へ入る
```

この確認をもって、今後のLIVING-13では音優先型UIを標準採用する。

### 51.1 表面

```text
見出し語の音
  ↓
Conceptを想起
  ↓
ConceptScene
  ↓
見出し語の文字
  ↓
発音・音の切れ目
```

表面の音声は、Conceptの住所を探す入口である。

### 51.2 裏面

```text
日本語Concept
  ↓
例文の音
  ↓
見出し語と文意を想起
  ↓
対象言語の例文
  ↓
日本語訳
  ↓
語根・接辞・語形・文法・Concept境界
```

裏面の例文音声は、そのConceptの住所の周囲を対象言語で歩く経路である。

### 51.3 内的評価の三段階

```text
第1段階：既知感
この音を以前に聞いたことがあるか

第2段階：Concept想起
どのConcept ID、どのConceptSceneにつながるか

第3段階：言語想起
見出し語、語形、用法を回収できるか
```

Conceptを思い出せても対象言語が出ない場合は、住所には到達したが、その言語の道路がまだ弱いと解釈する。

---

## 52．音、場所、画像、Conceptの関係

MEMORIOPOLISの新しい記憶経路：

```text
音
×
場所
×
イメージ
×
Concept
×
言語
×
自分の経験
```

各要素の役割：

```text
音声
＝ 都市の入口を開く合図・駅名アナウンス

Concept ID
＝ 記憶都市の住所・駅番号

ConceptScene
＝ 住所の風景・駅周辺の景観

見出し語
＝ 言語別の道路・路線名

例文
＝ その道路を実際に歩く経路

Essay
＝ 複数の住所を結ぶ物語上の街路

FSRS
＝ 各住所と各道路を再訪する時刻表
```

ConceptSceneは答えそのものではなく、複数言語が集まる交通結節点である。

同じConcept IDには、LIVING-13とCLASSICA-5を通して同じConceptSceneを使う。

---

## 53．学校的な正確さと記憶都市的な連想

学校の試験では正確な再現が評価される。一方、古い記憶術では、語呂合わせ、奇妙な像、場所、身体感覚、共感覚的な連想を総動員して、まず情報を記憶へ定着させる。

MEMORIOPOLISでは、連想と正確さを対立させない。

```text
入口
＝ 語呂、音の類似、画像、場所、個人的経験

奥行き
＝ 正確な語義、発音、語根、接辞、文法、出典
```

例：

```text
フィリピン語 tungo
  ↓
日本語の「単語」に似た音をアンカーにする
  ↓
正しい意味は「〜へ向かって」
  ↓
音からConceptへ向かう学習そのものを連想する
```

語呂合わせは誤義を固定するためではなく、正しい意味へ戻るための一時的な橋として使う。

---

## 54．フィリピン語の正式19フィールド

```text
1. ID
2. Filipino
3. Pronunciation
4. Japanese
5. PartOfSpeech
6. UsageNote
7. ExampleFilipino
8. ExampleJapanese
9. Root
10. Affixes
11. PerceptualSegmentation
12. MorphologicalBreakdown
13. ExampleBreakdown
14. ExampleExplanation
15. MeaningBridge
16. SoundBridge
17. Source
18. CourseTags
19. ConceptScene
```

TTS：

```html
{{tts fil_PH:Filipino}}
{{tts fil_PH:ExampleFilipino}}
```

Windows版でフィリピン語TTSが再生できなくても、本番環境のAnkiDroidで再生できれば運用上問題なしとする。

### 54.1 Filipino Core20

```text
C0011 umiral       ある
C0012 gawin        する
C0013 magkaroon    持つ
C0014 magpadala    送る
C0015 tumanggap    受け取る
C0016 makarinig    聞く
C0017 maghanap     調べる
C0018 lumipat      移る
C0019 maiugnay     結びつく
C0020 matali       縛られる
```

Source：

```text
E0001_fil
```

CourseTags：

```text
memoriopolis::fil::core20
```

---

## 55．インドネシア語の正式19フィールド

```text
1. ID
2. Indonesian
3. Pronunciation
4. Japanese
5. PartOfSpeech
6. UsageNote
7. ExampleIndonesian
8. ExampleJapanese
9. Root
10. Affixes
11. PerceptualSegmentation
12. MorphologicalBreakdown
13. ExampleBreakdown
14. ExampleExplanation
15. MeaningBridge
16. SoundBridge
17. Source
18. CourseTags
19. ConceptScene
```

TTS：

```html
{{tts id_ID:Indonesian}}
{{tts id_ID:ExampleIndonesian}}
```

### 55.1 Indonesian Core20

```text
C0011 ada          ある
C0012 melakukan    する
C0013 memiliki     持つ
C0014 mengirim     送る
C0015 menerima     受け取る
C0016 mendengar    聞く
C0017 mencari      調べる
C0018 berpindah    移る
C0019 terhubung    結びつく
C0020 terikat      縛られる
```

語根・接辞の主要観測点：

```text
melakukan
＝ meN- + laku + -kan

memiliki
＝ meN- + milik + -i

mengirim
＝ meN- + kirim
語頭kが消失

menerima
＝ meN- + terima
語頭tが消失

mendengar
＝ meN- + dengar
語頭dは保持

mencari
＝ meN- + cari

berpindah
＝ ber- + pindah

terhubung
＝ ter- + hubung

terikat
＝ ter- + ikat
```

Source：

```text
E0001_id
```

CourseTags：

```text
memoriopolis::id::core20
```

---

## 56．インドネシア語E0001の中心表現

タイトル：

```text
Dari “Romaru” Menuju Orang Roma
```

中心命題：

```text
Manusia tidak kehilangan tanah tempat berpijak.
Manusia hanya mengganti tanah yang menjadi tempatnya terhubung.
```

結末：

```text
Saya tidak menemukan arti kata itu.
Meskipun demikian, kata tersebut telah membuka sebuah jalan.
```

主要Concept：

```text
tanah
＝ 土地、土、生活の基盤

tempat berpijak
＝ 足場、立脚点

berpindah
＝ 場所・状態・焦点が移る

terhubung
＝ 接続された状態

terikat
＝ 物理的・制度的・関係的に縛られた状態
```

---

## 57．CLASSICA-5の音声設計を二層化する

近代日本語は次の基準で確定する。

```text
表記
＝ 歴史的仮名遣い＋旧字体

文法・文体
＝ 明治から戦前まで

音
＝ 現代日本語話者が「古い文章」として理解できる読み

役割
＝ 現代日本語と古典語をつなぐ時間方向の橋
```

CLASSICA-5では、近代日本語と同じように「現代の耳から入れる入口」を用意する。ただし、古典語を近代文語へ置き換えず、二層構造にする。

```text
CLASSICA-5
├─ BRIDGE
│  └─ 現代の耳から入りやすい短い音声経路
│
└─ DEPTH
   └─ 古典語本来の語形、文法、発音伝統、出典
```

### 57.1 Listening Bridge

条件：

- 古典語に実在する語彙を使う。
- 古典語として妥当な文法を使う。
- 現代技術・法律用語を無理に造語しない。
- 近縁Conceptへ降ろす。
- 構文を短く単純にする。
- 音からConceptを特定しやすくする。

原則：

> 現代語へ寄せるのではなく、古典語の中で簡単にする。

### 57.2 Classical Depth

収録内容：

- 古典語Lemma
- 採用した歴史層
- 語形変化・形態論
- 統語・文法
- ConceptMatchType
- 古典文献の用例
- 出典
- 発音伝統
- 現代語との意味差

### 57.3 CLASSICA-5のカード経路

```text
表面のBridge Audio
  ↓
Conceptを想起
  ↓
ConceptScene
  ↓
Lemmaと転写

裏面のBridge Example Audio
  ↓
文意を想起
  ↓
短い古典語学習文
  ↓
日本語訳
  ↓
Classical Depth
  ↓
古典文法・歴史的用法・出典
```

### 57.4 言語別の橋

```text
Classical Latin
＝ 平明な古典ラテン語散文 → 古典文献 → 必要に応じて中世・新ラテン語

Ancient Greek
＝ 単純なAtticまたはConceptに応じたKoine → 古典文献

Classical Sanskrit
＝ 古典文法を保つ短い散文 → 連声・格変化・複合語 → 必要ConceptのみVedic

Biblical Hebrew
＝ 基本語根と短い構文 → ティベリア式母音・聖書語法・出典

Classical Arabic
＝ 明瞭な古典文語の短文 → 格語尾・派生形 → 必要に応じてQuranic Arabic
```

---

## 58．記憶術の師匠筋Ed Cookeについての調査

ジョシュア・フォアの著書に登場する「エド」は、英国の記憶競技者・著者・起業家Ed Cookeである。

重要な経歴：

- 心理学と哲学を学んだ。
- 認知科学の修士課程を修了した。
- 23歳でGrand Master of Memoryとなった。
- Joshua Foerの記憶術コーチを務めた。
- 約1年の指導後、Joshua Foerは2006年の全米記憶選手権で優勝した。
- 記憶術を語学学習へ応用するMemriseを共同創業した。

本人の代表的著書：

```text
Remember, Remember:
Learn the Stuff You Thought You Never Could
```

主なオンライン資料：

```text
Penguin Booksの公式書籍ページ
Google Booksの書誌・プレビュー
Ed.blog
Memrise創業者紹介
記憶競技・注意・忘却についてのインタビュー
現在の学習・AI・空間芸術に関する講演と活動
```

MEMORIOPOLISとの接点：

```text
Ed Cooke
＝ 裸の情報を奇妙な像と場所へ変換する

MEMORIOPOLIS
＝ 音、ConceptScene、Concept ID、Essay、多言語を一つの住所へ接続する
```

違い：

```text
記憶競技
＝ 任意情報を高速・正確に再現する

JANUS-18
＝ 自分の経験から生まれたConceptを、多言語と歴史の中で長期的に育てる
```

今後、Ed Cookeの著書や公開講演を読む場合は、競技技法だけでなく、想像力、遊び、場所、音、学習環境の設計という観点からJANUS-18へ接続する。

---

## 59．Anki統計の現在地

2026年9月30日の統計では、カード状態が次のように分化した。

```text
新規       10枚
学習中      0枚
再学習中    0枚
定着前    130枚
定着       40枚
合計      180枚
```

重要な観測：

```text
安定性の中央値      11日
復習間隔の中央値    10日
平均想起確率        約94%
```

円グラフの変化は不具合ではなく、FSRSがカードを「新規・定着前・定着」に分け始めた結果と解釈する。

音優先型UI導入後は、次を継続観測する。

```text
もう一度率
保持率
難易度の中央値
安定性の中央値
1枚あたりの解答時間
音だけでConceptを想起できた割合の体感
```

導入直後に解答時間が伸びても、音から記憶を検索する深い課題へ変わった影響として観察し、すぐに失敗と判断しない。

---

## 60．次回作業

次回は最初に、インドネシア語Core20のAnkiDroid実機確認結果を反映する。

確認項目：

```text
表面のid_ID単語音声
音の後にConceptを検索する間が生まれるか
ConceptScene
見出し語・発音
裏面の例文音声
日本語訳
語根・接辞・形態素分解
3段プルダウン
id="answer"による自動スクロール
ダークモード
```

問題がなければ、LIVING-13の次言語へ進む。現在の進行順では、次候補はベトナム語とする。

次言語でも必ず守る手順：

```text
Core10フィールドマスターを取得
  ↓
実フィールド名と順序を確定
  ↓
ConceptSceneを末尾へ追加
  ↓
音優先型UIを作成
  ↓
AnkiDroidでTTS確認
  ↓
E0001対象言語版を自然な文章で作成
  ↓
canonical化
  ↓
Core20の正本CSV・Anki CSVを作成
  ↓
実機確認
```

---

## 61．次回開始用プロンプト

```text
この引き継ぎ書を2026年10月1日の最新状態として、MEMORIOPOLIS / JANUS-18を再開します。

E0001_ja.md、E0001_en.md、E0001_zh-Hant-TW.md、E0001_ko.md、E0001_ru.md、E0001_fil.md、E0001_id.mdはcanonicalです。

音優先型UIをLIVING-13の標準とします。表面では見出し語の音を先に聞き、Conceptを想起してからConceptSceneと文字を確認します。裏面では例文音声を先に聞き、見出し語と文意を想起してから例文、日本語訳、語根・接辞・文法へ進みます。

フィリピン語はAnkiDroidでfil_PHの単語音声と例文音声が正常に再生され、音からConceptを検索する練習が成立しました。Windows版のフィリピン語TTSエラーは許容します。

インドネシア語Core20はMEMORIOPOLIS_Indonesian_Core20_19fields_2026-10-01.zipとして完成済みです。次回最初にAnkiDroidの実機確認結果を反映してください。

CLASSICA-5はBRIDGEとDEPTHの二層にします。Bridge AudioとBridge Example Audioを現代の耳から入る経路とし、古典語の正規語彙と妥当な文法を保ちながら短く単純な文にします。Classical Depthでは歴史層、語形、文法、発音伝統、古典文献、出典へ降ります。現代語に寄せるのではなく、古典語の中で簡単にします。

問題がなければ、次候補のベトナム語Core10フィールドマスター確認から開始します。
```

---

## 62．2026年10月1日の店じまい地点

- 音優先型UI：LIVING-13の標準として正式採用。
- フィリピン語E0001：canonical。
- フィリピン語ノートタイプ：正式19フィールド。
- フィリピン語Core20：完成。
- フィリピン語AnkiDroid TTS：単語・例文とも正常。
- インドネシア語E0001：canonical。
- インドネシア語ノートタイプ：正式19フィールド。
- インドネシア語UI：音優先型へ更新済み。
- インドネシア語Core20：完成。
- インドネシア語Core20実機確認：夜にAnkiDroidで実施予定。
- ConceptScene：全言語共通のConcept住所として維持。
- FSRS：再訪時刻表として継続利用。
- 連想：語呂、音、画像、場所を入口として許容。
- 正確さ：語義、発音、語根、接辞、文法、出典で奥行きを担保。
- 近代日本語：歴史的仮名遣い＋旧字体、明治から戦前の文法・文体。
- CLASSICA-5：Listening BridgeとClassical Depthの二層構造。
- 次言語候補：ベトナム語。

本日の最終整理：

> MEMORIOPOLISは、文字を見て意味を当てる単語帳から、音を聞いてConceptの住所を探す記憶都市へ移行した。ConceptSceneで場所を確かめ、見出し語、語根、接辞、例文へ降りる。LIVING-13ではこの経路を標準化し、CLASSICA-5では現代の耳から入るBridge Audioと、古典語本来の地層へ降りるClassical Depthを組み合わせる。
