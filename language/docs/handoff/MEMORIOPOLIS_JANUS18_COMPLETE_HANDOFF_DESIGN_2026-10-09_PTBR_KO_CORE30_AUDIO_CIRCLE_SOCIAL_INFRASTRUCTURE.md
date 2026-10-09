# MEMORIOPOLIS / JANUS-18 完全版引き継ぎ書・設計書

更新日時：2026年10月9日 17:07 JST  
版：E0001 LIVING-13完結・E0002韓国語Core30・統合Audio Circle・社会基盤設計統合版  
次回開始時点：自宅でAnkiDroidと音源を実機確認後、E0002の次言語へ進む

---

## 1. 本書の目的

本書は、2026年10月9日時点のMEMORIOPOLIS / JANUS-18について、以下を一冊へ統合する完全版の引き継ぎ書・設計書である。

- E0001ブラジル・ポルトガル語版とPortuguese Core20
- E0002韓国語版とKorean Core30
- 韓国語ノートタイプの音優先型UI刷新
- ConceptScene破損と修正方針
- MarkdownからMP3を作る汎用音声パイプライン
- YouTube Music上の統合JANUS-18 Audio Circle
- 公開カバー画像と公開運用
- 音、文字、画像、Concept、Essayを循環させる訓練設計
- MEMORIOPOLISを社会基盤の変化へ接続する北極星
- Novel、Essay、Paper、Anki、Audio、街歩き、読書を横断する制作原則

---

## 2. 本日の主要成果

1. `E0001_pt-BR.md`をブラジル・ポルトガル語正本としてcanonical化した。
2. ブラジル・ポルトガル語Core10へ`ConceptScene`を追加し、画像を登録した。
3. ブラジル・ポルトガル語ノートタイプを、音優先、ConceptScene、3段パネル対応の現行UIへ更新した。
4. Portuguese Core20の19フィールドCSVを作成し、Ankiへインポートした。
5. `Source`から旧`draft`表記を削除し、`E0001_pt-BR.md`へ統一した。
6. 汎用スクリプト`memoriopolis_audio_sync.py`で`E0001_pt-BR.mp3`を生成した。
7. `E0002_ko.md`を作成し、canonical正本として確定した。
8. 韓国語Core30用のC0021からC0030を14フィールドCSVとして作成した。
9. 韓国語ノートタイプを、Core10、Core20、Core30共通の音優先型UIへ刷新した。
10. Korean Core30の一部ConceptSceneが、CSV内の推測画像名とAnkiメディアの実在名の不一致により破損した。
11. 破損したConceptSceneをAnki上で手動修正した。
12. Korean Core30をAnkiWebへ同期した。
13. `memoriopolis_audio_sync.py`で`E0002_ko.mp3`を生成した。
14. `E0001_pt-BR.mp3`と`E0002_ko.mp3`を、Essay別に分けず、統合Audio Circleへ追加した。
15. YouTube Musicの統合プレイリストは17トラック、合計1時間40分になった。
16. Audio Circleの公開範囲は「公開」とした。
17. Audio Circleのカスタムカバー画像を、個別Essayに依存しない統合版へ更新した。
18. 画面上では18回の視聴が確認された。
19. MEMORIOPOLISが社会基盤の変化に資する経路を、設計上の正式な評価軸として整理した。

---

## 3. 現在のプロジェクト構造

```text
MEMORIOPOLIS / JANUS-18
├─ Novel
│  ├─ 現代日本語版
│  └─ 近代日本語版
│
├─ Essay
│  ├─ E0001
│  ├─ E0002
│  └─ 以後、継続的に追加
│
├─ Paper
│  ├─ 記憶術
│  ├─ 多言語勘
│  ├─ 人格場・制度場
│  └─ 実装結果の理論化
│
├─ Anki
│  ├─ 音優先型カード
│  ├─ ConceptScene
│  ├─ 語彙・例文・解説
│  └─ FSRS
│
├─ Audio
│  ├─ 1 Markdown = 1 MP3
│  ├─ edge-tts
│  ├─ 汎用同期スクリプト
│  └─ YouTube Music Audio Circle
│
└─ Languages
   ├─ LIVING-13
   └─ CLASSICA-5
```

---

## 4. JANUS-18

### 4.1 LIVING-13

```text
1. ModernJapanese
2. English
3. zh-Hant-TW
4. Korean
5. Russian
6. Filipino
7. Indonesian
8. Vietnamese
9. French
10. German
11. Italian
12. Spanish es-ES
13. Portuguese pt-BR
```

### 4.2 CLASSICA-5

```text
1. Classical Latin
2. Ancient Greek
3. Classical Sanskrit
4. Biblical Hebrew
5. Classical Arabic
```

### 4.3 基本構造

```text
LIVING-13
＝ 現代世界を横断する水平の円環

ModernJapanese
＝ 現代と過去をつなぐ階段

CLASSICA-5
＝ 文明史の深層へ降りる垂直の円環
```

---

## 5. E0001の現在地

E0001は、LIVING-13の現代語円環を一周した状態である。

```text
E0001_ja.md          canonical
E0001_en.md          canonical
E0001_zh-Hant-TW.md  canonical
E0001_ko.md          canonical
E0001_ru.md          canonical
E0001_fil.md         canonical
E0001_id.md          canonical
E0001_vi.md          canonical
E0001_fr.md          canonical
E0001_de.md          canonical
E0001_it.md          canonical
E0001_es.md          canonical
E0001_pt-BR.md       canonical
```

### 5.1 E0001ブラジル・ポルトガル語版

```yaml
essay_id: E0001
language: pt-BR
locale: pt-BR
status: canonical
canonical_source: E0001_ja.md
core_range: C0011-C0020
```

中心命題：

```text
As pessoas não perdem o chão.
Apenas mudam o chão ao qual estão conectadas.
```

結末：

```text
Não encontrei o significado da palavra.
Mesmo assim, aquela palavra abriu um caminho.
```

### 5.2 Portuguese Core20

```text
C0011 existir
C0012 fazer
C0013 ter
C0014 enviar
C0015 receber
C0016 ouvir
C0017 procurar
C0018 mudar
C0019 conectar-se
C0020 estar preso
```

重要なConcept境界：

```text
ouvir
＝ 音や言葉が自然に耳へ入る

escutar
＝ 意識して耳を傾ける
```

```text
procurar
＝ 探す過程

encontrar
＝ 見つけた結果
```

```text
conectar-se
＝ 新しい接続関係へ入る

estar preso
＝ 拘束・依存関係の中にある
```

Source：

```text
E0001_pt-BR.md
```

CourseTags：

```text
memoriopolis::pt-BR::core20
```

---

## 6. E0002の現在地

```text
E0002_ja.md          canonical
E0002_en.md          canonical
E0002_zh-Hant-TW.md  canonical
E0002_ko.md          canonical
```

### 6.1 E0002韓国語版

```yaml
essay_id: E0002
title: "또 하나의 선로"
language: ko
locale: ko-KR
status: canonical
canonical_source: E0002_ja.md
core_range: C0021-C0030
```

中心となる結末：

```text
사람을 지킨다는 것은,
같은 자리에 묶어 두는 일이 아닐지도 모른다.

잠시 다른 길로 갔다가도 다시 돌아올 수 있도록,
또 하나의 선로를 놓는 일일지도 모른다.
```

意味：

```text
人を守るということは、同じ場所に縛りつけることではないのかもしれない。
しばらく別の道へ進んでも再び戻れるように、もう一本の線路を敷くことなのかもしれない。
```

### 6.2 Korean Core30

```text
C0021 결혼하다
C0022 키우다
C0023 일하다
C0024 인계하다
C0025 돌아오다
C0026 보장하다
C0027 양립하다
C0028 경쟁하다
C0029 역할을 맡다
C0030 평가하다
```

Source：

```text
E0002_ko.md
```

Tags：

```text
memoriopolis::ko::core30
```

### 6.3 Concept境界

```text
키우다
＝ 日常的な「育てる」

양육하다
＝ 制度的・説明的な「養育する」
```

```text
인계하다
＝ 業務や責任を正式に引き渡す

인계받다
＝ 引き継ぐ側として受け取る
```

```text
보장하다
＝ 権利や条件を制度的に保障する

지키다
＝ 人、場所、約束、権利などを守る
```

```text
역할을 맡다
＝ 社会や組織の役割を担う

역할을 연기하다
＝ 役を演じる
```

---

## 7. 韓国語ノートタイプの正式設計

### 7.1 正式14フィールド

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

### 7.2 現行UI

```text
KOREAN_CARD_UI_14FIELDS_AUDIO_FIRST_CONCEPTSCENE_3PANELS_2026-10-09.md
```

対象：

```text
Core10
Core20
Core30
```

### 7.3 表面

```text
Concept ID・韓国語チップ
  ↓
単語音声
  ↓
Conceptを心の中で想起
  ↓
ConceptScene
  ↓
ハングル見出し語
  ↓
ローマ字
```

単語TTS：

```html
{{tts ko_KR:Korean}}
```

表示：

```text
먼저 들어 보세요
まず音を聞き、心の中でConceptを探す
```

### 7.4 裏面

```text
CONCEPT BRIDGE
  ↓
日本語Concept・品詞
  ↓
例文音声
  ↓
韓国語例文
  ↓
日本語訳
  ↓
3段パネル
```

例文TTS：

```html
{{tts ko_KR:ExampleKorean}}
```

### 7.5 3段パネル

```text
낱말의 구조 · 語の構造
예문 해설 · 例文解説
언어의 다리 · 言語間ブリッジ
```

### 7.6 AnkiDroid自動スクロール

裏面の次を削除しない。

```html
<div id="answer" class="answer-divider">
```

---

## 8. ConceptScene破損と再発防止

### 8.1 本日の事象

Korean Core30では、正常表示されるカードと、壊れた画像アイコンになるカードが混在した。

原因：

```text
CSV内の推測画像ファイル名
≠
Ankiメディア内の実在画像ファイル名
```

### 8.2 対応

```text
正常カード
＝ そのまま維持

破損カード
＝ Anki上で実在する画像へ手動差し替え
```

全体再インポートは行わなかった。

### 8.3 今後の必須ルール

```text
Concept画像フォルダーを確認
  ↓
実在ファイル名一覧を取得
  ↓
C番号と対応を確定
  ↓
CSVのConceptSceneへ転記
  ↓
インポート
```

**Concept画像ファイル名を英訳から推測してはならない。**

フィールドマスター先行と同様に、画像も実在ファイル名先行とする。

---

## 9. 音声生成パイプライン

### 9.1 原則

```text
1 canonical Markdown
＝
1 MP3
```

### 9.2 正式スクリプト

```text
memoriopolis_audio_sync.py
```

動作：

```text
Markdownを探索
  ↓
status: canonicalを確認
  ↓
言語・Voice・速度を選択
  ↓
既存MP3があればスキップ
  ↓
未生成MP3だけ作る
```

### 9.3 本日の生成

```text
E0001_pt-BR.md
  ↓
E0001_pt-BR.mp3
```

設定：

```text
locale：pt-BR
voice：pt-BR-FranciscaNeural
rate：-7%
```

```text
E0002_ko.md
  ↓
E0002_ko.mp3
```

設定：

```text
locale：ko-KR
voice：ko-KR-SunHiNeural
rate：-8%
```

### 9.4 実行例

```powershell
py .\memoriopolis_audio_sync.py --root . --job E0001:pt-BR
```

```powershell
py .\memoriopolis_audio_sync.py --root . --job E0002:ko
```

成功条件：

```text
[SUMMARY] generated=1 skipped=0 errors=0
```

---

## 10. Audio Circle正式設計

### 10.1 プレイリスト名

```text
MEMORIOPOLIS｜JANUS-18 Audio Circle
```

### 10.2 統合原則

Essayごとにプレイリストを分けない。

```text
E0001
E0002
E0003以降
```

のすべてのcanonical多言語MP3を、一つの統合プレイリストへ追加する。

### 10.3 現在の状態

```text
17トラック
合計1時間40分
公開
18回視聴
```

本日追加：

```text
E0001_pt-BR.mp3  4:04
E0002_ko.mp3     6:13
```

### 10.4 公開方針

Audio Circleは公開でよい。

目的：

```text
自分の反復トレーニング
＋
インターネット上で観測可能な公開実験
```

ただし、公開回数や再生数を競争指標にしない。

```text
視聴回数
＝ 発見された痕跡
≠ 成果の中心指標
```

### 10.5 カスタムカバー

個別Essayに依存しない統合カバーへ変更済み。

主要表示：

```text
MEMORIOPOLIS
JANUS-18 Audio Circle
More Languages, A Wider World
```

構図：

- ヘッドフォン
- 都市
- 鉄道
- 本とノート
- 多言語
- 複数方向の標識
- 記憶都市を俯瞰する視点

小さい文字はサムネイルで読めなくても問題なし。

優先順位：

```text
1. MEMORIOPOLIS
2. JANUS-18 Audio Circle
3. 音、都市、多言語の世界観
```

### 10.6 再生

```text
シャッフル
＋
全曲リピート
```

第一曲が固定される場合があるが、現時点ではYouTube Music側の挙動として許容する。

---

## 11. AnkiとAudio Circleの役割

```text
AnkiDroid
＝ 短い音からConceptを能動的に検索する

Audio Circle
＝ Essay全体の音、息、間、リズム、談話構造へ大量反復で馴染む
```

### 11.1 Anki

```text
単語音声
  ↓
Conceptを想起
  ↓
ConceptScene
  ↓
文字・語形・例文
```

### 11.2 Audio Circle

```text
音声が始まる
  ↓
言語を識別する
  ↓
Essay IDと場面を識別する
  ↓
次の談話展開を予測する
  ↓
Ankiで学んだ音と長文中で再会する
```

### 11.3 GitHubアプリとの併用

```text
YouTube Music
＝ 時間に沿って流れる音

GitHubアプリ
＝ canonical Markdownの地図
```

両者を同時に使うことで、次を観測する。

```text
音と文字の対応
語境界
息継ぎ
段落構造
意味のまとまり
談話の転換
次の展開の予測
```

---

## 12. 多言語勘と談話航法

### 12.1 多言語勘

> 多言語勘とは、Conceptと場面を手掛かりに、複数言語の候補を立ち上げ、その言語らしい候補を選択・変形する能力である。

```text
候補生成
  ↓
候補評価
  ↓
候補調整
```

### 12.2 談話航法

> 談話航法とは、一語ずつの完全理解を待たず、文章の場面、因果、転換、回収、結末のパターンから、次の意味候補を予測する読み方・聞き方である。

```text
場面設定
  ↓
問題提示
  ↓
予想外の要素
  ↓
探索
  ↓
視点転換
  ↓
中心命題
  ↓
結末
```

文法と対立しない。

```text
文法
＝ 局所的な道路規則

談話航法
＝ 地区から地区へ移る経路の把握
```

---

## 13. 忘却、記憶、判断

### 13.1 彫刻モデル

```text
経験の総体
  ↓
注意
  ↓
忘却による削減
  ↓
意味の輪郭
  ↓
記憶
```

```text
場所法
＝ のこぎり

奇抜なイメージ
＝ のみ

語呂合わせ
＝ 彫刻刀

FSRS
＝ 次に手を入れる工程表
```

目的は道具の性能競争ではない。

```text
何を残すか
なぜ残すか
現実へどう戻すか
```

が中心である。

### 13.2 チェスのグランドマスターとの接続

```text
初心者
＝ 全候補を個別に検討する

熟達者
＝ 局面パターンから有力候補を絞る
```

語学でも、単語と文法だけでなく、文章の局面と表現候補を読む能力を育てる。

---

## 14. MEMORIOPOLISの社会的な北極星

> MEMORIOPOLISは、記憶量、言語数、学習速度を競うための仕組みではない。音、文字、画像、経験、物語、学問を再訪可能な経路として結び、分業と階級化によって狭くなりやすい人間の知性に、複数の窓と移動可能性を取り戻すための試みである。

### 14.1 社会基盤へ資する設計表

| 領域 | 現在の実装 | 個人に生じる変化 | 社会基盤へ拡張できる可能性 | 注意すべき危険 | 今後の観測 |
|---|---|---|---|---|---|
| 記憶 | 音、ConceptScene、Concept ID、Essay、FSRS | 複数経路から意味へ戻れる | 成人の再学習、生涯学習 | 記憶量・速度競争 | 長期保持、再訪時の変化 |
| 語学 | JANUS-18、音優先Anki、Audio Circle | 外国語が文字列ではなく音と流れになる | 多言語情報への入口を増やす | 言語数を成果にする | 語境界、言語識別、談話予測 |
| 読解 | GitHub Markdown＋YouTube Music | 局所文法と談話全体を往復できる | 成人教育、外国語読解支援 | TTSを聞くだけで理解した錯覚 | 音のみ・文字のみ・併用の比較 |
| 多言語勘 | 同一Conceptの多言語観測 | 表現候補を立ち上げやすくなる | 翻訳、異文化協働 | 一対一翻訳 | 候補と選択理由の記録 |
| 談話航法 | Essay全体の反復聴取 | 分からない語があっても流れを読める | 学術・行政・報道の構造読解 | パターンの押し付け | 予測と実際の差 |
| 創作 | Novel、Essay、Paperの横断 | 経験、物語、理論、実装が循環する | 文学と研究を結ぶ学習文化 | 全作品の理論従属 | 実装が生んだ新しい着想 |
| 音声文化 | 1 Markdown = 1 MP3 | 原文がカードの材料として埋もれない | 読む時間が少ない人への入口 | 聞き流しによる理解錯覚 | 聞こえるようになった単位 |
| 教育 | 自己コーパス | 学習が生活と切り離されない | 経験起点の個別学習 | 閉鎖的な個人世界 | 共有可能部分と固有部分の分離 |
| AI | 翻訳、画像、TTS、CSV生成を人が統合 | AIを思考の足場として使う | 主体的AI学習のモデル | 無検証の大量生成 | canonical承認、修正履歴 |
| 階級移動 | 多言語、学術、技術への低コスト接続 | 所属職務を越えて学び直せる | 知的移動可能性の支援 | 時間・所得条件の無視 | 継続可能な時間・費用・端末 |
| 労働と分業 | Ankiで分解し、EssayとAudioで全体へ戻す | 部品知識と全体像を往復できる | 仕事の意味回復 | 人間判断の更なる細分化 | 分解の利点と損失 |
| 公共性 | GitHub正本、公開Audio Circle | 学習履歴を検証・再利用できる | オープン教材と研究 | 公開自体が目的化 | 著作権、個人情報、公開範囲 |
| 古典語 | CLASSICA-5 | 現代Conceptの起源と限界が見える | 歴史的時間幅の回復 | 無理な古典語化 | Exact、Near、Partial、不在 |
| 社会観察 | 電車、街歩き、読書からEssay | 日常を構造的な問いへ変える | 見落とされた問題の発見 | 人物の断定 | 観察、推論、仮説の分離 |
| 市場形成 | 学問、観察、実装の循環 | 未命名の価値をConcept化する | 新しい教育・文化・技術領域 | 儲けだけへの縮小 | 誰が便益・費用を負うか |

### 14.2 実装上の三方良し

| 観点 | 提供したいもの | 避けたい状態 |
|---|---|---|
| 学ぶ人 | 経験から始まり、音と多言語で世界へ接続できる環境 | 点数・カード数・言語数だけを追う |
| 作る人 | AIを使いながら正本と判断を人間が保持する制作基盤 | AI生成物の大量生産へ埋没する |
| 社会 | 学び直し、異文化理解、知的移動を支える仕組み | 学習機会が時間と資本を持つ人だけに集中する |

### 14.3 機能追加時の評価質問

```text
1. この機能は、人の知性を広げるか。
2. 原文や経験へ戻る経路を残すか。
3. 学ぶ人を一つの正解へ閉じ込めないか。
4. 時間や資本の少ない人も使えるか。
5. 生まれた価値が再び人の学習環境へ還流するか。
```

---

## 15. アダム・スミス、分業、MEMORIOPOLIS

分業は生産力を上げるが、人が全体像と判断力を失う危険を生む。

MEMORIOPOLISにも同じ構造がある。

```text
Essay
  ↓
Conceptへ分解
  ↓
単語・例文カードへ分解
  ↓
効率的に反復
```

Ankiだけで終わると、原文、息、時間、経験が失われる可能性がある。

そこで、次の回復経路を作る。

```text
Anki
＝ 分業

ConceptScene
＝ 共有される意味の住所

Essay
＝ 全体性

MP3
＝ 時間と息の回復

Audio Circle
＝ 分解された学習成果を生活へ戻す場
```

> 効率を上げるために分解する。しかし、分解された人間や知識を、どのように全体へ戻すのか。

この問いを設計の中心に置く。

---

## 16. 運用ルール

### 16.1 正本

```text
GitHub上のcanonical Markdown
＝ 文章正本
```

### 16.2 Anki

```text
フィールドマスター先行
画像実在名先行
音優先UI
AnkiWebで復習メニュー再構築
AnkiDroidで学習・実機確認
```

### 16.3 Audio

```text
canonical Markdownのみ音声化
1 Markdown = 1 MP3
既存MP3はスキップ
統合Audio Circleへ追加
```

### 16.4 公開

```text
Audio Circleは公開
正本と生成条件を追跡可能にする
視聴回数を競争指標にしない
```

---

## 17. 帰宅後の確認

### 17.1 AnkiDroid

重点カード：

```text
C0021 結婚하다
C0027 양립하다
C0029 역할을 맡다
C0030 평가하다
```

確認項目：

- 単語音声
- 音からConceptを探す間
- ConceptScene
- ハングルとローマ字
- `CONCEPT BRIDGE`への移動
- 例文音声
- 3段パネル
- ダークモード

### 17.2 MP3

```text
E0001_pt-BR.mp3
E0002_ko.mp3
```

確認項目：

- ブラジル・ポルトガル語の自然さ
- 韓国語の速度`-8%`
- `오카마 바`の読み
- E0002の結末の余韻
- トラック間の音量差

### 17.3 YouTube Music

- 17トラックすべてが再生対象になっている
- シャッフル＋全曲リピート
- バックグラウンド再生
- 新カバーがスマートフォンでも読める

---

## 18. 次回の候補作業

帰宅後確認に問題がなければ、次の順で進む。

```text
1. AnkiDroid確認結果の反映
2. Audio Circle試聴結果の反映
3. E0002の次言語版を作成
4. 対応するCore30を作成
5. Anki同期
6. 汎用スクリプトでMP3生成
7. 統合Audio Circleへ追加
```

E0002の展開順をLIVING-13の既定順へ合わせる場合、次の候補はロシア語である。

```text
E0002_ja
E0002_en
E0002_zh-Hant-TW
E0002_ko
E0002_ru ← 次候補
```

ただし、CLASSICA-5開始条件との優先順位は次回開始時に引き継ぎ書を見て判断する。

---

## 19. 次回開始用プロンプト

```text
この引き継ぎ書を2026年10月9日の最新状態として、MEMORIOPOLIS / JANUS-18を再開します。

本日はE0001ブラジル・ポルトガル語版をcanonical化し、Portuguese Core20を作成・インポートし、E0001_pt-BR.mp3を生成しました。またE0002韓国語版をcanonical化し、韓国語ノートタイプを音優先型UIへ更新し、Korean Core30を作成・インポートしました。Core30のConceptSceneでは推測画像名と実在ファイル名の不一致があり、破損箇所だけをAnki上で手動修正しました。今後は画像の実在ファイル名を確認してからCSVを作成してください。

E0002_ko.mp3も汎用スクリプトmemoriopolis_audio_sync.pyで生成済みです。AnkiWebへの同期も完了しています。帰宅後にAnkiDroidでC0021、C0027、C0029、C0030を確認し、E0001_pt-BR.mp3とE0002_ko.mp3を試聴します。

YouTube Musicの正式プレイリストはMEMORIOPOLIS｜JANUS-18 Audio Circleです。Essayごとに分割せず、すべてのcanonical多言語MP3を一つの統合プレイリストへ追加します。現在は公開、17トラック、1時間40分、画面上では18回視聴です。カバーは個別Essayに依存しない統合版へ更新済みです。

社会設計上、MEMORIOPOLISは記憶量や学習速度を競うものではなく、音、文字、画像、経験、物語、学問を再訪可能な経路として結び、人間の知性へ複数の窓と移動可能性を戻すことを北極星とします。

帰宅後確認に問題がなければ、E0002の次言語版と対応Core30へ進みます。既定順ならE0002_ru.mdが次候補です。
```

---

## 20. 2026年10月9日の店じまい地点

```text
[x] E0001_pt-BR.md canonical
[x] Brazilian Portuguese Core10 ConceptScene
[x] Brazilian Portuguese音優先型UI
[x] Portuguese Core20
[x] E0001_pt-BR.mp3
[x] E0002_ko.md canonical
[x] 韓国語音優先型UI
[x] Korean Core30
[x] ConceptScene破損箇所の手動修正
[x] E0002_ko.mp3
[x] AnkiWeb同期
[x] 統合Audio Circleへ2本追加
[x] Audio Circleを17トラック・1時間40分へ更新
[x] Audio Circle公開運用
[x] 統合カスタムカバーへ更新
[x] 社会基盤への接続表を設計へ統合
[ ] 自宅でAnkiDroid確認
[ ] 自宅でMP3確認
[ ] 次回、E0002の次言語へ進む
```

本日の最終合意：

> MEMORIOPOLISは、知識を分解して効率的に学ぶためだけの仕組みではない。Ankiで分解した音とConceptを、Essay、MP3、Audio Circle、Novel、Paper、街歩き、読書へ戻すことで、知識の全体性と人間の知性を回復する循環を作る。公開Audio Circleは、その循環をインターネット上で観測可能にする最初の小さな社会基盤である。
