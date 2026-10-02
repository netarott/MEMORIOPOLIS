# MEMORIOPOLIS / JANUS-18 完全版引き継ぎ書

更新日時：2026年10月2日 11:40 JST  
版：完全版・Vietnamese Core20・多言語勘・記憶哲学・音優先型UI統合版  
次回作業日：2026年10月3日

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

---

# 2026年10月2日追補：Vietnamese Core20・多言語勘・記憶哲学

## 60．本日の到達点

2026年10月2日は、ベトナム語版の実装を進める一方で、MEMORIOPOLISを単なる「記憶の宮殿の都市版」にしないための思想的整理を行った。

本日の成果は、大きく次の四群に分かれる。

```text
1. インドネシア語TTS例外の復旧
2. ベトナム語E0001・Core10・Core20の整備
3. 忘却、抽象化、専門家判断、多言語勘の理論整理
4. Novel・Essay・Paper・実装結果を自由に横断する制作方針の再確認
```

本日、MEMORIOPOLISは次の段階へ進んだ。

> 情報を保管する巨大な記憶宮殿ではなく、音、画像、場所、言語、経験、忘却を通じて、現実を見る窓と良い候補を生み出す外部足場として育てる。

---

## 61．インドネシア語TTS例外の復旧

### 61.1 問題

2026年10月1日夜、AnkiDroidでインドネシア語の音声が再生されなかった。

昨日作成したテンプレートでは、一般的なISO言語コードを用いていた。

```html
{{tts id_ID:Indonesian}}
{{tts id_ID:ExampleIndonesian}}
```

しかし、2026年9月19日の引き継ぎ書には、インドネシア語だけはAnkiDroid実機上で一般指定が動作せず、旧JavaロケールとGoogle TTSの音声識別子を明示する必要があると記録されていた。

### 61.2 正式指定

単語：

```html
{{tts in_ID voices=com.google.android.tts-id-id-x-dfz-local:Indonesian}}
```

例文：

```html
{{tts in_ID voices=com.google.android.tts-id-id-x-dfz-local:ExampleIndonesian}}
```

組み合わせ：

```text
ロケール
＝ in_ID

Google TTS音声識別子
＝ com.google.android.tts-id-id-x-dfz-local
```

### 61.3 再発防止

- 現在のISOコード`id`へ正規化しない。
- 端末が返した`in_ID`をそのまま正本として使う。
- voice IDも省略しない。
- TTSが動かない場合は、推測でコードを書き換えない。
- 一時的に`{{tts-voices:}}`を表示し、AnkiDroidが返した値をそのまま採用する。
- フィールド名、CSV、CSS、ConceptSceneは変更しない。

この修正は画像で確認済みであり、表面と裏面のTTSタグは正しく更新された。

---

## 62．ベトナム語ノートタイプとCore10

### 62.1 正式19フィールド

```text
1. ID
2. Vietnamese
3. Pronunciation
4. Japanese
5. PartOfSpeech
6. UsageNote
7. ExampleVietnamese
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

アップロードされた元CSVは、次の状態だった。

```text
vi_core10_master.csv
＝ ヘッダー付き18列

vi_core10_anki.csv
＝ ヘッダーなし18列
```

Ankiノートタイプへ`ConceptScene`を19番目として追加した後、Core10用CSVも正式19列へ更新した。

作成済み：

```text
vi_core10_master_19fields.csv
vi_core10_anki_19fields.csv
```

C0001からC0010まで、共通ConceptScene参照を19列目へ追加した。

### 62.2 ベトナム語音優先型UI

完成ファイル：

```text
VIETNAMESE_CARD_UI_19FIELDS_AUDIO_TONE_FIRST_CONCEPTSCENE_3PANELS_2026-10-02.md
```

設計：

```text
音と声調
  ↓
Conceptを想起
  ↓
ConceptSceneで住所を確認
  ↓
綴りと声調記号
  ↓
例文音声
  ↓
語構成と文法
```

表面：

```text
NGHE TRƯỚC
まず音と声調を聞き、心の中でConceptを探す
```

単語TTS：

```html
{{tts vi_VN:Vietnamese}}
```

裏面：

```text
NGHE CÂU VÍ DỤ
例文の音と声調から、見出し語と文意を探す
```

例文TTS：

```html
{{tts vi_VN:ExampleVietnamese}}
```

2026年9月19日の記録では、ベトナム語にインドネシア語のような例外voice IDはない。AnkiDroidでエラーが出た場合のみ、`{{tts-voices:}}`で端末の実値を取得する。

### 62.3 画面確認

PC版Ankiのプレビューでは、次が正常に表示された。

- C0001
- `TIẾNG VIỆT`言語チップ
- `NGHE TRƯỚC`音声領域
- 再生ボタン
- ConceptScene
- ベトナム語見出し語・発音領域
- 裏面構造に対応するCSS

夜にAnkiDroidで、単語TTS、例文TTS、声調、画像、3段プルダウン、自動スクロール、ダークモードを確認する。

---

## 63．E0001ベトナム語版

完成ファイル：

```text
E0001_vi.md
```

タイトル：

```text
Từ “Romaru” đến người Roma
```

現在の状態：

```yaml
language: vi
status: draft
canonical_source: E0001_ja.md
core_range: C0011-C0020
```

中心命題：

```text
Con người không đánh mất mặt đất dưới chân mình.
Họ chỉ thay đổi vùng đất mà mình kết nối tới.
```

結末：

```text
Tôi đã không tìm thấy nghĩa của từ ấy.
Dẫu vậy, từ ấy vẫn mở ra một con đường.
```

翻訳方針：

- 日本語の語順を機械的に追わない。
- ベトナム語として自然な段落の流れを優先する。
- 未知語から記憶、土地、移動、SNS・プラットフォームへ進む思考経路を保持する。
- 個人的観察、記憶、参照情報、仮説を分ける。
- 「romaru」の意味は未確定のまま残す。
- 結末を説明で閉じず、「一つの道を開いた」という余韻を保持する。

内容確認後、問題がなければ次へ変更する。

```yaml
status: canonical
```

---

## 64．Vietnamese Core20

完成パッケージ：

```text
MEMORIOPOLIS_Vietnamese_E0001_Core10_Core20_19fields_2026-10-02.zip
```

収録ファイル：

```text
E0001_vi.md
vi_core10_master_19fields.csv
vi_core10_anki_19fields.csv
vi_core20_master_19fields.csv
vi_core20_anki_19fields.csv
README.md
```

### 64.1 Core20見出し語

```text
C0011 tồn tại        ある
C0012 làm            する
C0013 có             持つ
C0014 gửi            送る
C0015 nhận           受け取る
C0016 nghe           聞く
C0017 tìm kiếm       調べる
C0018 chuyển         移る
C0019 kết nối        結びつく
C0020 bị ràng buộc   縛られる
```

Source：

```text
E0001_vi
```

CourseTags：

```text
memoriopolis::vi::core20
```

### 64.2 候補空間

C0011：

```text
có
＝ ある、いる

tồn tại
＝ 存在する、存続する
```

C0012：

```text
làm
＝ する、作る

thực hiện
＝ 実行する、実施する
```

C0013：

```text
có
＝ 持つ、ある

sở hữu
＝ 所有する
```

C0016：

```text
nghe
＝ 聞く

nghe thấy
＝ 聞こえる、耳にする

lắng nghe
＝ 耳を傾ける
```

C0017：

```text
tìm
＝ 探す

tìm kiếm
＝ 探索・検索する

kiểm tra
＝ 検査・確認する

nghiên cứu
＝ 研究する
```

C0019：

```text
kết nối
＝ 接続する、結びつく

liên kết
＝ 連結する、相互に関連づける

mối liên hệ
＝ 関係、つながり
```

C0020：

```text
bị
＝ 不利益を受ける受け身

ràng buộc
＝ 拘束する

bị ràng buộc
＝ 拘束される、縛られる
```

ベトナム語では、単語だけでなく、音節数と声調の並びもチャンクとして観測する。

```text
tồn tại
＝ 低く重い二音節

tìm kiếm
＝ 下降＋上昇

kết nối
＝ 上昇＋上昇

bị ràng buộc
＝ 短く重い音＋下降＋短く重い音
```

---

## 65．忘却とは記憶である

本日の思想的な中心は、次の比喩だった。

> 大理石や木を削ることが忘却であり、削られて現れる像が記憶である。

```text
経験の総体
  ↓
注意による選択
  ↓
忘却による削減
  ↓
意味の輪郭
  ↓
記憶として再構成
```

完全保存は、石材をそのまま倉庫へ置くことに近い。

人間の記憶は、細部を選び、不要な部分を背景へ退かせ、現在の目的に応じて像を再構成する。

```text
忘却
＝ 削ること

記憶
＝ 残った像

想起
＝ 現在の光で像を見ること

再解釈
＝ 別の角度から彫り直すこと

学習
＝ 情報量を増やすだけでなく、輪郭を育てること
```

Ankiの`Again`は失敗ではない。

```text
今の像では、この角度から輪郭が見えなかった
```

という観測である。

---

## 66．記憶術は道具である

場所法、奇抜なイメージ、語呂合わせ、間隔反復は、作品そのものではない。

```text
場所法
＝ のこぎり

奇抜なイメージ
＝ のみ

語呂合わせ
＝ 彫刻刀

間隔反復
＝ 時間を置いた研磨

検索練習
＝ 輪郭を手で確かめる作業

FSRS
＝ 次に手を入れる時期を知らせる工程表
```

競技化すると、道具の性能が目的になりやすい。

```text
より速く
より大量に
より正確に
他者の記録を超える
```

MEMORIOPOLISは、この軍拡競争へ入らない。

借りるもの：

- 抽象情報を像へ変換する方法。
- 像を場所へ安定して置く方法。
- 同じ刺激へ一貫したアンカーを与える方法。
- 失敗地点を分析する習慣。
- 検索経路を反復する方法。
- 遊び、奇妙さ、ユーモア。

最終目的にしないもの：

- 速度。
- 記憶量。
- 順位。
- 意味のない情報の短期再現。

記憶都市の目的は、世界との関係を増やすことにある。

---

## 67．驚異的記憶と生活に使える記憶

Sさん型の極端な記憶について、次の仮説を整理した。

「像を作れない」というより、刺激から像が大量かつ自動的に発生し、どの像を背景として削るかが難しい可能性がある。

```text
一般的な記憶
大量の細部
  ↓
忘却・選択・圧縮
  ↓
Concept

極端な細部保持
刺激
  ↓
多数の像が強く発生
  ↓
細部が長く残る
  ↓
背景を削りにくい
  ↓
抽象化やカテゴリー化に負荷がかかる場合がある
```

ただし、サヴァン症候群、HSAM、共感覚、Sさんの単一症例は区別する。

サヴァン的能力を持つ人々を一様に「抽象化できない」「生活できない」と解釈しない。

より慎重な表現：

> 一部の人では、細部の保持やパターン処理が非常に強い一方、統合、抽象化、実行機能、社会的文脈への適用などに大きな支援が必要なことがある。

適応的な記憶に必要なのは、完全保存ではなく、具体と抽象の往復である。

```text
必要なときは細部へ戻る
必要なときはConceptへ上がる
```

---

## 68．チェスのグランドマスターと専門家判断

チェスのグランドマスターは、盤面の駒を一個ずつ同じ重みで処理するのではない。

```text
初心者
細部 → 一個ずつ検討 → 全体像を推測

熟練者
局面パターンを認識
  ↓
重要な細部だけを選ぶ
  ↓
候補手を絞る
  ↓
必要な変化だけを読む
```

意味のある局面では、駒の配置がチャンクやテンプレートとして認識される。

ランダム配置では熟練者の記憶優位が縮むため、これは万能な写真記憶ではなく、意味によって構造化された領域固有の記憶と考えられる。

```text
完全な保存
≠
優れた判断

適切な圧縮
＋
必要な細部への再アクセス
＝
専門的な判断
```

忘却は記憶の像を作るだけでなく、判断可能な世界を作る。

---

## 69．多言語勘を候補生成能力として実装する

多言語勘の定義：

> Conceptと場面を手掛かりに、複数言語の蓄積から妥当な表現候補を立ち上げ、その言語らしい候補を選択・変形する能力。

三段階：

```text
1. 候補生成
今の場面では何を言えるか

2. 候補評価
どの表現が自然か
何を前景化するか
口語か文章語か

3. 候補調整
時制、相、主語、フォーカス、語尾、接辞、語順
```

文法と単語は必要だが、それだけでは運用にならない。

```text
単語
＝ 部品

文法
＝ 組立規則

チャンク
＝ よく使われる意味のまとまり

候補選択
＝ 場面に合うまとまりを立ち上げる力

運用
＝ 候補を選び、必要部分だけ変形して使うこと
```

### 69.1 記憶都市の五層

```text
第1層：Concept
何を意味するか

第2層：Lexeme
各言語で何というか

第3層：Family
語根と派生形

第4層：Pattern
どの語とまとまり、どの構文に入るか

第5層：Situation
どの場面なら、どの候補を選ぶか
```

Core20は第1層から第3層までを整備している。

次の実験対象は、第4層と第5層である。

### 69.2 候補手カードPoC

最初の候補：

```text
C0016 聞く
mendengar / mendengarkan / terdengar

C0019 結びつく
terhubung / berhubungan / menghubungkan / hubungan

C0020 縛られる
terikat / mengikat / ikatan / keterikatan
```

一場面につき候補は最大三つ程度とする。候補過多は全探索へ戻るため、グランドマスター型の訓練にならない。

例：

```text
場面：
列車内で、意識して聞こうとしていない言葉が耳に入った。

候補：
mendengar
mendengarkan
terdengar

語り手を主語にして「私は聞いた」
→ mendengar

言葉が聞こえた事実を前景化
→ terdengar

注意して耳を傾ける
→ mendengarkan
```

この選択過程が多言語勘である。

### 69.3 良い候補の評価軸

```text
1. Concept適合
2. 場面適合
3. 焦点適合
4. レジスター適合
5. 語のまとまり・共起
6. 音としての取り出しやすさ
7. 誤解の少なさ
```

正解／不正解だけでなく、候補順位を学習する。

```text
第1候補
自然だが焦点が異なる候補
文法的だが場面に合わない候補
意味がずれる候補
```

---

## 70．パレイドリアと候補生成

木目が顔に見える、柳の下に人影や幽霊が見えるといった現象は、脳が曖昧な入力から既知のパターンを高速に当てはめる副産物として理解できる。

```text
曖昧な入力
  ↓
有力候補を高速生成
  ↓
追加情報と比較
  ↓
合わない候補を修正
```

多言語勘にもこの機能を借りる。

```text
不完全な外国語音声
＋
文脈
＋
既知の語形
＋
話題
  ↓
意味候補を立てる
```

目指すのは、誤認しないことだけではない。

```text
早く仮説を立てる
仮説を保留する
文脈で順位を変える
誤りに気づいて更新する
```

> 大胆に候補を出し、穏やかに修正できる知性を育てる。

誤答は、現在どのテンプレートを使っているかを示す足跡である。

---

## 71．神経ネットワークと記憶都市

脳は一つの中央装置が順番に計算するのではなく、多数の神経細胞が相互接続したネットワークとして働く。

重要なのは、次の組み合わせである。

```text
神経細胞の数
＋
結び付き方
＋
結び付きの強さが経験で変わること
```

記憶は一つの場所に完成画像として置かれるのではなく、再び起動できる活動パターンとして分散していると考える。

```text
音
色
形
意味
過去の場面
文字
文化的物語
```

これらが同時に再活動することで、一つのまとまりが再構成される。

多言語勘は、中央辞書の検索ではなく、複数の弱い手掛かりによる分散投票として捉えられる。

```text
音の形
→ この語族らしい

接辞
→ 状態形らしい

場面
→ 能動的行為ではない

Essay
→ 接続状態を述べていた

他言語
→ connect系Conceptと対応する
```

複数の手掛かりが同じ候補を支持すると、その候補の活動が最も強くなる。

MEMORIOPOLISは脳そのものではなく、意味のあるネットワークを作りやすくする外部足場である。

```text
Concept ID
＝ 接続先を固定する

ConceptScene
＝ 視覚的な共通ノード

音声
＝ 聴覚からの起動信号

Essay
＝ 時間と経験の文脈

語根・接辞
＝ 言語内部の構造

FSRS
＝ 接続が弱くなる前の再起動
```

---

## 72．MEMORIOPOLISを巨大な記憶宮殿にしない

単純な拡張：

```text
記憶の宮殿
  ↓
部屋を増やす
  ↓
建物を増やす
  ↓
都市にする
```

これでは巨大な記憶倉庫になる。

MEMORIOPOLIS：

```text
音
  ↓
Concept候補
  ↓
画像と場所
  ↓
複数言語による異なる見方
  ↓
Essayと個人的経験
  ↓
現実の知覚と判断の変化
```

目的は、情報を大量に収納することではない。

> 世界から受け取れる信号を増やすこと。

記憶都市は現実から逃げ込む閉鎖空間ではない。

```text
現実
  ↓
記憶都市で多言語・多時代へ接続
  ↓
別の視点を得る
  ↓
再び現実へ戻る
```

戻った現実では、外国語の音が雑音ではなくなり、文字に構造が見え、一つの日本語訳に複数の候補が見える。

---

## 73．JANUS-18の北極星

ユーザーの思想：

- 競争で何かを必死に追い求めることを人生の目標としない。
- JANUS-18で多言語に触れることは、思考の翼を広げることである。
- 多言語は、意識に複数の窓を持つことである。
- 外国語の文章や街中の会話が部分的に分かるだけでも、知識と経験の間に化学反応が起こる。
- その化学反応によって、意識がポジティブな意味で変容する。

正式な北極星：

> JANUS-18は、記憶量や言語数を競う計画ではない。多言語の音、文字、Concept、物語、歴史に触れることで、思考に翼を与え、意識に複数の窓を開き、現実から受け取れる意味を増やす試みである。

各要素：

```text
Concept ID
＝ 戻れる住所

ConceptScene
＝ 意味を確認する風景

音声
＝ 窓を開ける合図

各言語
＝ 異なる方向を向いた窓

Essay
＝ 経験とConceptを結ぶ街路

忘却
＝ 景色の輪郭を整える編集

FSRS
＝ 再び窓を開く時刻表

多言語勘
＝ 複数の窓から得た情報で良い候補を立ち上げる力
```

MEMORIOPOLISは、記憶を保管する都市ではなく、意識が変容し続けるための都市である。

---

## 74．Novel・Essay・Paper・実装を横断する制作方法

今後も、次の四領域を分断しない。

```text
Novel
＝ 研究成果を直接説明せず、物語として経験させる

Essay
＝ 個人的経験からConceptを抽出する

Paper
＝ 仮説、既存研究、実装結果を検証可能な形へ整理する

JANUS-18実装
＝ Anki、音声、ConceptScene、FSRS、多言語展開で仮説を試す
```

循環：

```text
日常の経験
  ↓
Essay
  ↓
Concept抽出
  ↓
多言語カード実装
  ↓
AnkiDroidでの身体的・聴覚的な確認
  ↓
統計と内省
  ↓
Paperの仮説
  ↓
Novelで別の形に変換
  ↓
新しい経験と解釈
```

この自由な横断をMEMORIOPOLISの正式な制作方法とする。

特定の媒体だけを正解とせず、媒体ごとに異なる役割を持たせる。

---

## 75．次回作業：2026年10月3日 フランス語

### 75.1 最初の確認

夜のAnkiDroid確認結果を反映する。

ベトナム語：

```text
単語TTS
例文TTS
声調の輪郭
ConceptScene
声調記号
IPA
3段プルダウン
id="answer"による自動スクロール
ダークモード
```

インドネシア語：

```text
in_ID
voices=com.google.android.tts-id-id-x-dfz-local
```

修正後の単語・例文音声を確認する。

### 75.2 ベトナム語canonical

`E0001_vi.md`の内容を確認し、採用する場合：

```yaml
status: canonical
```

### 75.3 フランス語の進行順

```text
1. French Core10の実フィールドマスターを取得
2. 実フィールド名と順序を確認
3. ConceptSceneを末尾に追加
4. 音優先型UIを作成
5. AnkiDroidでfr_FR TTSを確認
6. E0001フランス語版を自然な文章で作成
7. 内容確認後にcanonical化
8. French Core20の正本CSVとAnki CSVを作成
9. 実機確認
```

フランス語の音優先経路：

```text
音
  ↓
Concept候補
  ↓
ConceptScene
  ↓
綴り
  ↓
リエゾン、アンシェヌマン、語末子音
  ↓
例文
```

既定の展開順：

```text
フィリピン語
  ↓
インドネシア語
  ↓
ベトナム語
  ↓
フランス語
  ↓
ドイツ語
  ↓
イタリア語
  ↓
スペイン語 es-ES
  ↓
ポルトガル語 pt-BR
```

---

## 76．次回開始用プロンプト

```text
この引き継ぎ書を2026年10月2日の最新状態として、MEMORIOPOLIS / JANUS-18を再開します。

最初に、ベトナム語Core10/Core20とインドネシア語TTS修正版のAnkiDroid実機確認結果を反映してください。

E0001_vi.mdはdraftです。内容確認後にcanonical化します。

インドネシア語TTSの正本は次です。
{{tts in_ID voices=com.google.android.tts-id-id-x-dfz-local:Indonesian}}
{{tts in_ID voices=com.google.android.tts-id-id-x-dfz-local:ExampleIndonesian}}

ベトナム語TTSの現在の標準指定は次です。
{{tts vi_VN:Vietnamese}}
{{tts vi_VN:ExampleVietnamese}}
エラー時は{{tts-voices:}}で端末の実値を取得し、推測で変更しません。

音優先型UIをLIVING-13の標準とします。

MEMORIOPOLISは、巨大な記憶の宮殿や競技記憶の軍拡競争を目指しません。忘却によって像の輪郭を作り、複数の言語を意識の窓として、現実から受け取れる意味を増やします。

多言語勘は、Conceptと場面から少数の良い表現候補を立ち上げ、文脈で順位付けし、必要な部分だけ文法的に変形する能力として育てます。将来、C0016、C0019、C0020を候補手カードPoCに使います。

Novel、Essay、Paper、JANUS-18の実装結果を自由に横断しながら、MEMORIOPOLISを整備します。

問題がなければ、2026年10月3日の対象言語であるフランス語へ進みます。最初にFrench Core10の実フィールドマスターを確認してください。
```

---

## 77．2026年10月2日の店じまい地点

- インドネシア語TTS例外：過去の実機値へ復旧。
- ベトナム語ノートタイプ：正式19フィールド。
- ベトナム語音優先型UI：完成。
- ベトナム語Core10 19列CSV：完成。
- `E0001_vi.md`：draft完成。
- Vietnamese Core20：完成。
- AnkiDroid実機確認：夜に実施予定。
- 次言語：フランス語。
- 忘却：記憶の像を削り出す編集として位置づける。
- 場所法・奇抜な像・FSRS：作品ではなく道具。
- 記憶競技：技術は借りるが、速度・記憶量・順位を目的にしない。
- 専門家判断：細部の完全保持ではなく、意味あるパターンから良い候補を選ぶ能力。
- 多言語勘：場面から表現候補を立て、文脈で削り、最適な候補を使う能力。
- MEMORIOPOLIS：巨大な記憶宮殿ではなく、現実へ戻る窓を増やす都市。
- JANUS-18：思考の翼を広げ、意識に複数の窓を開く実践。
- 制作方式：Novel、Essay、Paper、実装、統計、内省を自由に横断する。

本日の最終整理：

> 記憶都市は、すべてを保存するための都市ではない。忘却によって意味の輪郭を作り、音からConceptの住所へ入り、複数言語の窓から同じ世界を別の方向に見る。そこで生まれた良い候補を現実の理解と判断へ持ち帰る。Novel、Essay、Paper、JANUS-18の実装を横断することで、MEMORIOPOLISそのものもまた、固定された建築物ではなく、意識とともに変容する都市として育てる。
