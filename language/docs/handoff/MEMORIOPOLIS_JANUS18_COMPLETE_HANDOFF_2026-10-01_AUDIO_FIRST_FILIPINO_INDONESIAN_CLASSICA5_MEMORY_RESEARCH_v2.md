# MEMORIOPOLIS / JANUS-18 完全版引き継ぎ書

更新日時：2026年10月1日 15:53 JST  
版：v2・音優先型UI・Filipino/Indonesian Core20・CLASSICA-5・記憶術探索統合版  
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

## 49．2026年9月30日から10月1日までの更新

### 49.1 canonical

```text
E0001_ja.md          canonical
E0001_en.md          canonical
E0001_zh-Hant-TW.md  canonical
E0001_ko.md          canonical
E0001_ru.md          canonical
E0001_fil.md         canonical
E0001_id.md          canonical
```

### 49.2 フィリピン語

- 既存18フィールドの末尾へ`ConceptScene`を追加し、正式19フィールドとした。
- `E0001_fil.md`を作成し、canonical化した。
- 音優先型UIを初めて実装した。
- Windows版では`fil_PH`音声がなくTTSエラーとなったが、学習本番のAnkiDroidでは単語・例文とも正常に再生した。
- 音を先に聞き、「Conceptは何だったか」と想起する練習が実機で成立した。
- Filipino Core20を作成した。

```text
E0001_fil.md
FILIPINO_CARD_UI_19FIELDS_AUDIO_FIRST_CONCEPTSCENE_3PANELS_2026-09-30.md
MEMORIOPOLIS_Filipino_Core20_19fields_2026-09-30.zip
```

Core20：

```text
C0011 umiral
C0012 gawin
C0013 magkaroon
C0014 magpadala
C0015 tumanggap
C0016 makarinig
C0017 maghanap
C0018 lumipat
C0019 maiugnay
C0020 matali
```

### 49.3 インドネシア語

- `id_core10_master.csv`と`id_core10_anki.csv`の既存18フィールドと列順を確認した。
- 末尾へ`ConceptScene`を追加し、正式19フィールドとした。
- 音優先型UIを適用した。
- `E0001_id.md`を作成し、canonical化した。
- Indonesian Core20を作成し、AnkiDroidへ同期した。夜に実機確認する。

```text
E0001_id.md
INDONESIAN_CARD_UI_19FIELDS_AUDIO_FIRST_CONCEPTSCENE_3PANELS_2026-10-01.md
MEMORIOPOLIS_Indonesian_Core20_19fields_2026-10-01.zip
```

Core20：

```text
C0011 ada
C0012 melakukan
C0013 memiliki
C0014 mengirim
C0015 menerima
C0016 mendengar
C0017 mencari
C0018 berpindah
C0019 terhubung
C0020 terikat
```

---

## 50．音優先型UIをLIVING-13の標準とする

```text
表面
見出し語の音
  ↓
Conceptを想起
  ↓
ConceptSceneで住所を確認
  ↓
文字・発音・音の切れ目

裏面
例文の音
  ↓
見出し語と文意を想起
  ↓
例文・日本語訳
  ↓
語根・接辞・語形・文法・Concept境界
```

内的評価：

```text
第1段階：音の既知感
第2段階：Concept・ConceptSceneの想起
第3段階：対象言語の見出し語・語形・用法の回収
```

Conceptだけ出た場合は、住所には到達したが対象言語の道路が弱いと解釈する。

```text
音声       ＝ 都市の入口を開く合図
Concept ID ＝ 住所
ConceptScene＝ 住所の風景
見出し語   ＝ 言語別の道路
例文       ＝ 道路を歩く経路
Essay      ＝ 住所間を結ぶ街路
FSRS       ＝ 再訪の時刻表
```

---

## 51．連想と正確さ

学校的な正確さだけでなく、語呂、音の類似、奇妙な像、場所、身体感覚を記憶の入口として許容する。ただし、連想は誤義を固定するためではなく、正しい意味へ戻る橋として使う。

```text
入口
＝ 語呂、音、画像、場所、個人的経験

奥行き
＝ 正確な語義、発音、語根、接辞、文法、出典
```

フィリピン語`tungo`は日本語の「単語」と似るが、正しい意味は「〜へ向かって」。この偶然を「音からConceptへ向かう」アンカーとして利用する。

---

## 52．CLASSICA-5：BRIDGEとDEPTH

近代日本語：

```text
表記：歴史的仮名遣い＋旧字体
文法・文体：明治から戦前まで
音：現代話者が古い文章として理解できる読み
```

CLASSICA-5：

```text
CLASSICA-5
├─ BRIDGE
│  └─ 現代の耳から入りやすい短い音声経路
└─ DEPTH
   └─ 古典語本来の語形、文法、発音伝統、出典
```

原則：

> 現代語へ寄せるのではなく、古典語の中で簡単にする。

現代技術・法律用語を無理に古典語化せず、近縁Conceptへ降ろす。Bridge Exampleは古典語として妥当な語彙・文法を保ち、短く単純にする。Classical Depthでは歴史層、形態論、統語、ConceptMatchType、古典文献、出典、発音伝統、現代語との差へ降りる。

---

## 53．店じまい後のマスターとの会話：記憶術の情報探索

店じまい後、記憶術をJANUS-18の正式な研究軸として探索する方針を話し合った。

### 53.1 探索地図

```text
1. 場所法の科学的根拠と限界
2. 強いイメージと意味的一致
3. 音声から場所・画像・Conceptを想起する経路
4. 記憶競技者の符号化技術
5. 語学学習への応用
6. 忘却、抽象化、一般化
7. 古代からルネサンスまでの記憶術史
8. デジタル記憶宮殿、VR、AI
```

当面の中心課題：

> 音声を手掛かりとして、空間、画像、Concept、対象言語をどのように起動できるか。

### 53.2 場所法の科学と限界

近年の系統的レビューでは、場所法は単純反復より高い想起効果を示す一方、研究の偏りや方法上の制約から、証拠の質には慎重な評価が必要とされている。

```text
場所法は強力
  ↓
しかし万能ではない
  ↓
対象、訓練時間、場所設計、意味的一致、認知負荷を観測する
```

強烈さだけでなく、Conceptとの意味的一致を重視する。

```text
Conceptと無関係な強い像
＜
Conceptと説明可能に結びつき、少し奇妙で印象的な像
```

同じConcept IDに同じConceptSceneを固定する現在の設計は、共通住所の安定性を狙うものである。

### 53.3 記憶術訓練と脳ネットワーク

記憶競技者と初心者を比較した研究では、卓越した記憶は単一の脳部位より、視覚系、内側側頭葉、デフォルトモードなどを含むネットワークの結び付きと関連した。初心者でも場所法を含む訓練によって成績と機能的結合が変化し、効果が数か月後まで関連した研究がある。

MEMORIOPOLISで観測する変化：

```text
初期
音 → 混乱 → 画像 → 日本語Concept

中期
音 → ConceptScene → Concept

熟達期
音 → Concept・画像・対象言語が近い時間で起動

深化
音 → 語根・接辞・例文・他言語が階層的に展開
```

速度だけでなく、複数経路からの到達と長期的な再構成を評価する。

### 53.4 音と場所のMEMORIOPOLIS仮説

古典的な場所法：

```text
場所 → イメージ → 記憶対象
```

MEMORIOPOLIS：

```text
音
  ↓
Conceptを検索
  ↓
場所と画像を想起・確認
  ↓
対象言語の文字・語形・例文へ降りる
```

統合要素：

```text
場所法
＋検索練習
＋聴覚認識
＋視覚的フィードバック
＋意味ネットワーク
＋間隔反復
```

英語検索語：

```text
auditory cues method of loci
sound-triggered spatial memory
cross-modal retrieval auditory visual
memory palace language learning audio
semantic congruence method of loci
multimodal vocabulary learning spaced repetition
auditory cue visual imagery recall
sound symbolism second language memory
```

既存研究による支持と、MEMORIOPOLIS独自仮説を分離する。

```text
比較的支持される部分
＝ 場所法、検索練習、意味的一致、間隔反復、多重符号化

独自仮説
＝ 多言語共通ConceptSceneを固定し、音から共通Concept住所へ入る
```

### 53.5 語学学習への応用

一般的な語彙記憶宮殿：

```text
外国語単語 → 語呂画像 → 場所
```

MEMORIOPOLIS：

```text
外国語音声
  ↓
共通Concept
  ↓
共通ConceptScene
  ↓
言語固有の見出し語・語根・接辞・文法
  ↓
自作Essayの経験
```

固定するもの：

```text
Concept ID、ConceptScene、中心Concept
```

言語ごとに変わるもの：

```text
音、文字、語形、語根、接辞、例文、文法
```

### 53.6 記憶競技から借りるもの

借りる：

- 音を聞いた瞬間に像や意味を起動する訓練。
- 同じ刺激へ同じアンカーを割り当てる一貫性。
- 失敗地点を記録する習慣。
- 符号化と想起を分ける観測法。
- 画像、場所、言語道路のどこが弱いかを分析する視点。
- 奇妙さ、動き、誇張、ユーモア、遊び心。

そのまま採らない：

- 速度のみを最終目標にすること。
- 無意味情報の短期再現を中心にすること。
- 一度の競技成績だけで長期学習を評価すること。

MEMORIOPOLISの目的：

> 自分の経験から生まれたConceptを、音、画像、場所、多言語、歴史の中で長期的に育てる。

---

## 54．今後の観測項目

```text
A. 音だけでConceptが出た
B. ConceptSceneだけ浮かんだ
C. 日本語Conceptだけ出た
D. 別言語が先に出た
E. 語根だけ聞き取れた
F. Conceptは出たが対象言語が出なかった
G. 例文のリズムだけ分かった
H. 何も浮かばなかった
```

毎カード記録せず、週に一度、印象的なカードのみ研究ノートへ残す。

長期観測：

```text
音優先と文字優先の解答時間差
音からConceptSceneが浮かぶ割合
別言語が先に浮かぶ頻度
同一ConceptSceneによる言語間促進と干渉
Core10からCore20への安定性変化
例文音声による用法想起の変化
現代語と古典語のBridge Audio間の距離
睡眠前後の想起感覚
```

---

## 55．オンライン探索資源

### 研究

```text
The Method of Loci in the Context of Psychological Research:
A Systematic Review and Meta-analysis

Mnemonic Training Reshapes Brain Networks to Support Superior Memory

Durable Memories and Efficient Neural Coding Through Mnemonic Training Using the Method of Loci

Method of Loci and Semantic Link:
Assessment of Memory Benefits in Healthy Aging
```

### 実践コミュニティ

```text
Art of Memory Wiki
https://artofmemory.com/wiki/Main_Page/

Art of Memory Getting Started Guide
https://artofmemory.com/start/

Art of Memory Forum
https://forum.artofmemory.com/

MemorySports
https://memorysports.app/
```

```text
査読研究
＝ 科学的根拠として読む

フォーラム・ブログ
＝ 実践アイデアと仮説の発見源として読む
```

両者を混同しない。

今後読む項目：

```text
Method of Loci
Memory Town System for Languages
Synesthesia and Memory
Spaced Repetition
Story Method
PAO System
Semantic Congruence
Memorizing Books and Texts
Auditory Memory
Cross-modal Retrieval
Forgetting and Abstraction
```

---

## 56．Ed Cooke調査の要点

ジョシュア・フォアの師匠筋「エド」は、英国の記憶競技者、著者、起業家Ed Cooke。

- 23歳でGrand Master of Memoryとなった。
- Joshua Foerを指導し、約1年後の全米記憶選手権優勝へつなげた。
- 代表的著書は`Remember, Remember: Learn the Stuff You Thought You Never Could`。
- Memrise共同創業者として、記憶術を大規模な語学学習へ接続した。
- 現在は学習、AI、音響空間、共同体的プロジェクトにも関心を広げている。

```text
Ed Cooke
＝ 裸の情報を奇妙な像と場所へ変換する

MEMORIOPOLIS
＝ 音、ConceptScene、Concept ID、Essay、多言語を一つの住所へ接続する
```

---

## 57．探索の優先順位

```text
1. 場所法の科学と限界
2. 音声手掛かりと視覚・空間記憶
3. 語学学習と記憶宮殿
4. 忘却と抽象化
5. Ed Cooke以外の記憶競技者
6. 共感覚と後天的連想
7. 古代からルネサンスまでの記憶術史
8. デジタル記憶宮殿、VR、AI
```

最初の研究テーマ案：

```text
音声手掛かりから空間・画像・Conceptを想起する学習設計

副題：
Anki、ConceptScene、FSRS、多言語共通Conceptを用いた
後天的な交差感覚的記憶ネットワークの試行
```

---

## 58．次回作業

1. インドネシア語Core20のAnkiDroid実機確認結果を反映する。
2. `id_ID`単語音声、例文音声、Concept想起、ConceptScene、語根・接辞、3段プルダウン、自動スクロール、ダークモードを確認する。
3. 問題がなければ次候補のベトナム語へ進む。
4. ベトナム語Core10フィールドマスターを先に確認する。
5. `ConceptScene`を末尾へ追加する。
6. 音優先型UI、E0001ベトナム語版、Core20の順で進める。

---

## 59．店じまい後の最終合意

- 記憶術の探索をJANUS-18の正式な研究軸にする。
- 場所法を万能視せず、効果と限界を読む。
- 強烈さだけでなく、Conceptとの意味的一致を重視する。
- 音からConcept住所へ入る方式を独自実験として継続する。
- ConceptSceneを全言語共通の意味住所とする。
- 記憶競技から符号化、一貫性、失敗分析、遊び心を借りる。
- 速度至上主義は採用しない。
- 科学論文、歴史資料、実践コミュニティ、Ankiログを別種の資料として扱う。
- プロジェクト思想に関わる店じまい後の会話も、引き継ぎ書へ追記する。

> MEMORIOPOLISは、古代の場所法をそのまま再現するのではない。音を入口にし、ConceptSceneを共通住所とし、Essayを街路とし、FSRSを再訪の時刻表とする。記憶術の歴史と科学を探索しながら、現代13言語と古典5言語を歩ける、多言語・多時代の記憶都市を実験的に構築する。
