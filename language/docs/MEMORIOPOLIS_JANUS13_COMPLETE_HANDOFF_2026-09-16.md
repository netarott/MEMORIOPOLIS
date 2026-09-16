# MEMORIOPOLIS / JANUS-13 完全版引き継ぎ書

**更新日：2026年9月16日**  
**本日の店じまい地点：近代日本語版Anki Core10の実装完了、ロシア語カードの音声ボタン中央配置完了、フィリピン語版Novel 第四章第十二節 draft01作成完了。**  
**次回の制作地点：フィリピン語版Novelの確認後、フィリピン語版Anki Core10を作成する。**  
**本日夜の作業予定：フィリピン語の言語機能・合成音声データを自宅Wi-Fi環境で導入する。**

---

## 0．今回の最重要サマリー

- プロジェクト名は`JANUS-13`で統一する。
- 第四章第十二節は`Core10`である。
- 第四章第十三節は、新出Conceptを10個追加して`Core20`とする。
- 序章は、その次の新出Conceptを10個追加して`Core30`とする。
- Core番号は物語の章順ではなく、JANUS-13型Ankiへ投入した新出Conceptの累積数を表す。
- 対象本文から既知Conceptを除外し、新出Conceptを重要度と頻度で評価して10個ずつ採用する。
- 既知Conceptは新規採番しないが、新しい用例・出現箇所はConcept Registryへ記録する。
- 日本語正本を起点として、各言語のNovelを制作する。
- NovelからJANUS-13型Ankiカードを作る。
- Ankiでトレーニングし、文字・音・文法・知覚について発見したことを制作ノートへ記録する。
- 旧note作品は、現在の正本としてではなく、過去の運行記録として記憶機関庫へアーカイブする。
- GitHub Pagesの中央駅には作品リンクを積み上げない。
- 中央駅には発車掲示板を置き、先発・次発・後発の三本だけをランダムに表示する。
- 読者は三本から自分で列車を選ぶ。
- Novelをすべての人に読ませることを目標にしない。縁のある読者が自分で乗車する設計とする。
- Novelを読んで何かを感じた読者は、機関庫の制作ノートを経由して作者やGitHubリポジトリへたどり着ける。
- Ankiの音声は移植性を優先し、音声名を固定せず言語コードだけを指定する。
- 予告編では、人工知性の声と「私」の声を話者別に制作する。
- 予告編の基本演出は、人工知性を女性音声、「私」を男性音声とする。
- 予告編用の音声はAnkiとは分離し、話者別の音声ファイルを生成してMP4へ統合する。

---

## 1．現在のMEMORIOPOLIS親デッキ

```text
MEMORIOPOLIS
├─ Korean
├─ Russian
├─ TaiwaneseMandarin
├─ English
└─ ModernJapanese
```

次に追加する予定のデッキ：

```text
MEMORIOPOLIS::Filipino
```

現在の共通Conceptは次の10個である。

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

## 2．Core番号の運用規則

### 採用済みの順序

```text
Core10
→ 第四章第十二節
→ C0001～C0010

Core20
→ 第四章第十三節
→ C0011～C0020を追加

Core30
→ 序章
→ C0021～C0030を追加
```

### Core番号の意味

> Core番号は物語の時系列や章番号ではなく、JANUS-13型Ankiへ新規Conceptを投入した累積数を表す。

そのため、物語順とAnki化順は一致しなくてよい。

```text
物語順
序章 → 第一章 → … → 第四章第十二節 → 第十三節

Anki化順
第四章第十二節 → 第十三節 → 序章 → 以降の対象文章
```

これは次の二つの時間を保存する。

```text
NarrativeOrder
→ 物語内部の順序

AnkiOrder
→ 作者が再観測・再整備した順序
```

---

## 3．新出Conceptの選定規則

対象文章から候補語を抽出し、既存Conceptと照合する。

```text
1. 対象本文を読む
2. Concept候補を抽出する
3. Concept Registryと照合する
4. 既知Conceptを新規候補から外す
5. 新出Conceptを重要度と頻度で評価する
6. 上位10個を次のCoreへ採用する
7. 残りの候補は次のCore候補として保存する
```

推奨する評価順は次のとおり。

```text
第一基準
→ その文章の判断や進行を動かしているか

第二基準
→ 作品全体で再登場する可能性があるか

第三基準
→ 複数言語で観測差が出るか

第四基準
→ 本文内の頻度が高いか

第五基準
→ 意味の橋・音の橋・分節の橋を作る価値があるか
```

原則：

> 重要度で選び、頻度で補強する。

### 既知Conceptの扱い

既知Conceptは、新しいCoreの10語には含めない。ただし、新しい文章で異なる用法が現れた場合は、その出現を保存する。

```text
C0002 記憶
├─ 第四章第十二節での用法
├─ 序章での用法
└─ 将来のEssayでの用法
```

```text
Concept ID
→ 作品全体を横断する意味の座標

Occurrence
→ そのConceptが実際に走った文章・用例
```

---

## 4．制作循環

JANUS-13の制作は、Novelを公開して終わりではない。

```text
日本語正本
↓
各言語のNovel
↓
Novelから新出Conceptを10個抽出
↓
JANUS-13型Ankiカード
↓
親デッキMEMORIOPOLISでトレーニング
↓
文字・音・文法・知覚上の発見
↓
制作ノート
↓
次のNovel・Essay・Commentary・Technical Reflectionへ還流
```

短く表すと、次の循環になる。

```text
Novel
→ Anki
→ トレーニング
→ 発見
→ 制作ノート
→ 次の文章
```

Ankiは完成作品の副教材ではない。

> Ankiは、書いた文章を13の言語面へ通し、作者内部に差異を蓄積し、次の文章を変える中間工程である。

---

## 5．旧noteの位置づけ

旧noteは削除せず、機関庫に保存する。

```text
旧note
→ 最初の公開運行記録

GitHub日本語正本
→ 現在の正本

JANUS-13 Anki
→ 現在の再観測・反復装置

制作ノート
→ トレーニング中に生じた発見の記録
```

旧noteと現在の正本に差があっても、それは誤差ではなく地層である。

> 旧noteは廃車ではなく、最初に記憶都市を走った保存編成である。

機関庫の旧noteアーカイブには、最低限、次を記録する。

```text
公開日
記事タイトル
元URL
対応する章・節
当時の本文
現在のGitHub正本
対応するCore
```

---

## 6．制作ノート

制作ノートは、完成済み理論の説明書ではなく、観測日誌として始める。

### 記録するもの

```text
観測した事実
思いついた仮説
既存知識による修正
カードへの反映
次に確認すること
```

### IDの分離

```text
C0001
→ Concept ID

O-0001
→ Observation ID

M-0001
→ Maintenance ID
```

Conceptと観測記録と整備記録は混ぜない。

### 制作ノートの例

```markdown
# 観測記録 O-0001

## 観測日

2026年9月16日

## 使用した編成

- Korean Core10
- Russian Core10
- Taiwanese Mandarin Core10
- English Core10
- Modern Japanese Core10

## 起きたこと

ロシア語のキリル文字だけでは単語の輪郭をつかみにくかった。
ラテン転写を見ると音価が分かり、子音の配置が文字列を
分節する標識として見え始めた。

## 暫定的な名前

子音標識仮説
Consonantal Landmark Hypothesis

## 留保

人類言語の起源を説明する仮説ではない。
現時点では、個人的な多言語読解過程についての知覚仮説である。

## 次に見ること

- 別のロシア語Conceptでも同じ知覚が起きるか
- 韓国語の終声でも類似した標識が働くか
- ドイツ語の子音連続でも同じ現象が見えるか
- ベトナム語では母音記号と声調がどう補完するか
- フランス語では子音が語境界を越えて接続するか
```

---

## 7．JANUS-13の三軸

### 7.1 垂直軸：日本語内部の時間

```text
近代日本語
歴史的仮名遣い・旧字体
        ⇅
現代日本語
現代仮名遣い・新字体
```

近代日本語は、外国語と並ぶ14番目の言語ではない。

> 近代日本語は、現代日本語の下にある時間地層である。

### 7.2 水平軸：日本語と外国語の関係

```text
韓国語
ロシア語
臺灣華語
英語
フィリピン語
インドネシア語
ベトナム語
スペイン語
ポルトガル語
イタリア語
フランス語
ドイツ語
        ⇄
現代日本語
```

各言語を重要度ランキングとして並べない。

```text
古層接続
南蛮接続
近代化接続
現代・未来接続
```

という歴史的・関係的座標を内部メタデータとして持たせる。

### 7.3 分節軸：文字列が音と単語として見えるまで

```text
文字列
↓
音価
↓
音節核
↓
子音の輪郭
↓
知覚上の区切り
↓
形態素
↓
文法関係
```

分節軸では、次を観測する。

```text
文字列はどこで単語として見えるか
音はどこで音節として聞こえるか
子音はどこで輪郭を作るか
母音はどこで音節核を作るか
強勢や声調はどこでまとまりを示すか
空白や文字ブロックはどの程度分節を助けるか
```

### 子音標識仮説

> 未知文字を読む初期段階では、母音が音節の核として発声可能性を与え、子音の配置が語の輪郭を認識する標識として働く可能性がある。

短く表すと次のとおり。

```text
母音は、声を通す。
子音は、輪郭をつくる。
転写は、その二つを未知文字へ戻す。
```

これは人類言語の起源を断定する説ではなく、現段階では読解知覚に関する観測仮説である。

---

## 8．第十三節からのフィールド負荷試験順

第四章第十二節は、実際に制作した順序を維持する特例とする。

第四章第十三節のCore20からは、次の順でNovelとAnkiのフィールド設計を検査する。

```text
1  現代日本語 ⇄ 近代日本語
   時間・字体・読み分離

2  臺灣華語
   表意文字・注音符号・拼音・声調

3  韓国語
   音節ブロック・初声・中声・終声・音変化

4  ロシア語
   未知文字・転写・強勢・子音標識

5  英語
   既知語・IPA・強勢・用法・概念境界

6  フィリピン語
   語根・接辞・形態的分節

7  インドネシア語
   接辞・重複・語根

8  ベトナム語
   母音記号・声調・音節

9  スペイン語
   比較的規則的な綴りと母音核

10 ポルトガル語
   南蛮接触・鼻母音・音の弱化

11 イタリア語
   明瞭な音節・子音の長短

12 フランス語
   語境界を越える接続・綴りと音の距離

13 ドイツ語
   子音連続・複合語・格・語順
```

この順番は、言語の重要度や優劣ではない。

> JANUS-13型Ankiの観測フィールドを段階的に負荷試験する順番である。

---

## 9．分節関連フィールドの区別

今後のロシア語Core20などでは、次の三つを分離して扱う。

### PerceptualSegmentation

```text
学習者が音を捉えるための仮設的な区切り
```

### ConsonantLandmarks

```text
語の輪郭として知覚された子音配置
```

### MorphologicalBreakdown

```text
語根・接辞・語尾などの文法的な分解
```

重要な原則：

```text
知覚上の区切り
≠
音節
≠
形態素
```

最初から子音標識仮説を全言語に当てはめない。

```text
ロシア語で発見
↓
韓国語・ドイツ語で再検査
↓
ベトナム語で母音・声調との相補性を確認
↓
フランス語で語境界を越える子音接続を確認
↓
仮説を修正
```

---

## 10．近代日本語版Anki Core10

### デッキ

```text
MEMORIOPOLIS::ModernJapanese
```

### ノートタイプ

```text
MEMORIOPOLIS Modern Japanese Vocabulary
```

### ZIP

```text
MEMORIOPOLIS_Modern_Japanese_Core10_draft01_2026-09-16.zip
```

### 収録ファイル

```text
ja_modern_core10_master_draft01.csv
ja_modern_core10_anki_draft01.csv
README_ja_modern_core10_draft01.md
MODERN_JAPANESE_NOTE_TYPE_DRAFT01.md
section12_ja_modern_japanese_core10_excerpt_draft01.md
```

### 16フィールド

```text
1  ID
2  ModernJapanese
3  HistoricalReading
4  ContemporaryJapanese
5  ContemporaryReading
6  PartOfSpeech
7  ModernUsage
8  ExampleModernJapanese
9  ExampleContemporaryJapanese
10 ExampleReading
11 Source
12 CourseTags
13 GlyphBridge
14 KanaBridge
15 MeaningBridge
16 SoundBridge
```

### 四つの橋

```text
GlyphBridge
→ 字体の橋

KanaBridge
→ 仮名遣いの橋

MeaningBridge
→ 意味の橋

SoundBridge
→ 音の橋
```

### TTS

```html
{{tts ja_JP:ContemporaryReading}}
```

```html
{{tts ja_JP:ExampleReading}}
```

旧字体・歴史的仮名遣いを表示し、TTSには現代読みを渡す。

### 現在の状態

```text
デッキ作成             完了
ノートタイプ作成       完了
16フィールド設定       完了
CSVインポート          完了
表面テンプレート       完了
裏面テンプレート       完了
CSS                    完了
PC版プレビュー         完了
AnkiWeb同期            実施対象
AnkiDroid確認          実施対象
```

AnkiDroidでは、最低限、次を確認する。

```text
C0001 記錄
C0008 檢證
C0009 權限
C0002 記憶またはC0010 役割
```

---

## 11．ロシア語カードのCSS修正

ロシア語の音声再生ボタンが左寄せになっていたため、表面・裏面のTTSを`tts-audio`で囲み、CSSで中央寄せにした。

### 表面

```html
<div class="tts-audio">
  {{tts ru_RU:Russian}}
</div>
```

### 裏面

```html
<div class="tts-audio">
  {{tts ru_RU:ExampleRussian}}
</div>
```

### CSS

```css
.tts-audio {
  text-align: center;
  margin: 14px 0;
}
```

PC版プレビューで、単語音声と例文音声の両方が中央に表示されることを確認済み。

```text
表面の単語音声
→ 中央寄せ成功

裏面の例文音声
→ 中央寄せ成功

既存レイアウト
→ 崩れなし
```

同期後、AnkiDroidでも中央配置を確認する。

---

## 12．次の言語：フィリピン語

### 観測面の名称

```text
日本語表示：フィリピン語
現地語表示：Filipino
補足：タガログ語を基盤とする標準フィリピン語
```

名称は`Filipino`で統一する。

### ファイル・デッキ案

```text
Novel：
section12_fil_draft01.md

デッキ：
MEMORIOPOLIS::Filipino

ノートタイプ：
MEMORIOPOLIS Filipino Vocabulary

タグ：
memoriopolis::fil::core10
```

### Novelの現在地

第四章第十二節のフィリピン語版Novelを作成済み。

```text
section12_fil_draft01.md
```

章題：

```text
Ikaapat na Kabanata: “Ang Tagasalin”
```

節題：

```text
Ikalabindalawang Seksiyon:
“Isang Tugon na Walang Patutunguhan”
```

核心文：

```text
Ang pagkakaroon mo ng awtoridad at ang pagtatangka
ng screen na ituring kang mayhawak ng awtoridad
ay hindi iisa.
```

### Novel確認時の重点

```text
artipisyal na talino
→ 人工知性の統一表現

abiso
→ 通知

tugon
→ 返信・応答

rekord
→ 記録

ruta
→ 経路

beripikasyon
→ 検証

awtoridad
→ 権限

tungkulin
→ 役割

patutunguhan
→ 宛先・行き先
```

小説としての自然さと、AnkiでConceptを固定できる用語一貫性の両方を確認する。

### フィリピン語で検査するもの

```text
ラテン文字と実際の音
語根
接頭辞
接尾辞
接中辞
語の反復
焦点・ヴォイスに関係する形
機能語
スペイン語・英語由来要素
知覚上の区切りと形態素境界の違い
```

フィリピン語では、次を分離する。

```text
PerceptualSegmentation
→ 発音を捉えるための知覚上の区切り

MorphologicalBreakdown
→ 語根や接辞による文法的な分解
```

---

## 13．今夜のフィリピン語音声導入

本日夜、自宅Wi-Fi環境でフィリピン語の言語機能・合成音声を導入する。

### 運用方針

```text
自宅Wi-Fi
↓
お守り程度にOneDrive同期を一時停止
↓
フィリピン語のBasic機能を確認・導入
↓
必要なら再起動
↓
TextToSpeechを確認・導入
↓
導入結果を確認
↓
OneDriveを再開
```

開始前に、実際のWindows上で利用可能な言語タグとCapability名を確認する。

候補としては`fil-PH`が想定されるが、実行前にWindowsの表示・利用可能Capabilityを確認し、推測だけでコマンドを確定しない。

### 確認事項

```text
BasicTypingが利用可能か
TextToSpeechが利用可能か
フィリピン語音声がWindows標準で提供されているか
導入後にAnki PC版から認識できるか
AnkiDroid側でどのTTS言語へ対応するか
```

今夜、篠原さんから声がかかった時点で、状態確認から一緒に進める。

---

## 14．Anki音声の基本方針

### Anki

Ankiでは音声名を固定せず、言語コードだけを指定する。

```html
{{tts ru_RU:Russian}}
```

```html
{{tts ja_JP:ContemporaryReading}}
```

フィリピン語も、端末で認識される言語タグを確認した後、同じ方針にする。

目的：

```text
PC版Anki
AnkiWeb
AnkiDroid
```

の移植性を優先する。

### 音声名を固定しない理由

```text
利点
→ 各端末で利用可能な音声を使用できる
→ PCとAndroid間の互換性が高い

制約
→ 端末によって声質が変わる
→ 男性音声・女性音声を統一できない場合がある
```

学習装置としては、移植性を優先する。

---

## 15．予告編音声の方針

Anki音声と予告編音声を分離する。

### 役割

```text
Anki音声
→ 学習・反復・移植性

予告編音声
→ 登場人物・演出・シリーズ内の一貫性
```

### 話者設定

```text
人工知性
→ 女性音声

「私」
→ 男性音声
```

必要に応じて担当者など第三の話者を追加する。

### 制作工程

```text
人工知性の台詞
→ 選定した音声
→ ai_voice.wav

「私」の台詞
→ 選定した音声
→ narrator_voice.wav

必要な第三話者
→ operator_voice.wav

環境音・音楽
→ background.wav

画像・映像
→ 絵巻素材

最終工程
→ 音声と映像を統合してMP4
```

予告編はPCの既定音声へ全面的に従う必要はない。話者ごとに別々の音声を生成してからMP4へ統合する。

### 論理名で管理する

台本に実際の音声名を直接埋め込まず、設定側で論理名を使う。

```text
AI_VOICE
NARRATOR_VOICE
OPERATOR_VOICE
```

言語ごとの実音声名は、別の設定で割り当てる。

```text
Japanese:
  AI_VOICE       → 選定した日本語音声A
  NARRATOR_VOICE → 選定した日本語音声B

Russian:
  AI_VOICE       → 選定したロシア語音声A
  NARRATOR_VOICE → 選定したロシア語音声B
```

### 最初の試験素材

第四章第十二節の次の往復が適する。

```text
「私」
これは、私に返信しろと言っているんですか。

人工知性
この画面は、そう読ませようとしています。

「私」
同じことでは？

人工知性
違います。
```

最初は日本語版で30秒前後のMP4を試作し、人物識別として声の切り替えが機能するか確認する。

---

## 16．GitHub Pagesの中央駅

中央駅は作品リンクを積み上げない。

### 発車掲示板

```text
記憶都市中央駅

発車標
├─ 先発
├─ 次発
└─ 後発
```

表示するのは常に三本だけ。

```text
先発
次発
後発
```

各列車には、最低限、次を表示する。

```text
発車区分
ホーム名
列車種別
文章タイトル
乗車リンク
```

例：

```text
先発
翻訳と権限ホーム
NOVEL
第四章 第十二節「宛先のない返信」
［乗車する］
```

### 抽選規則

```text
1. 公開可能な文章だけを候補にする
2. 同じ文章を三枠へ重複表示しない
3. 可能なら異なるホームから選ぶ
4. 可能なら異なる列車種別を混ぜる
5. 新規公開列車には一時的に少し高い配車率を与える
6. 同一端末では短時間に同じ三本を繰り返さない
7. 一定時間または次回訪問時に更新する
```

中央駅に履歴を追加しない。

```text
中央駅
→ 現在接続できる三本だけ

機関庫
→ 過去に走った列車の保存
```

---

## 17．GitHub Pagesの公開導線

```text
記憶都市中央駅
↓
発車掲示板
↓
読者が三本から一本を選ぶ
↓
テーマのホーム
↓
絵巻
↓
任意のショート予告編
↓
その文章を動かした一文
↓
読者がクリックした場合だけ本文へ
↓
Novel / Essay / Commentary / Technical Reflection
↓
夜の帰還線
↓
記憶機関庫
```

中央駅からNovelへ強制的に誘導しない。

```text
列車は来ている。
乗るかどうかは読者が決める。
```

### ランダム表示

ランダムに選ばれるのはNovelに限定しない。

```text
Novel
Essay
Commentary
Technical Reflection
Research Paper
PoC
```

文章形式に応じて、JANUS-13が表示する一文の性格を変える。

```text
Novel
→ 物語の判断を動かしたセリフ

Essay
→ 思考を動かす問い・主張

Commentary
→ 観測を開始した事実・コメント

Technical Reflection
→ 技術と制度を接続する命題

Research Paper
→ 中心仮説・定義・数式
```

---

## 18．ホーム・絵巻・文章に登場する二者

ホーム、絵巻、Novelには「私」と人工知性が登場する。

### ホーム

```text
「私」
→ 問いを持ってホームへ来る

人工知性
→ 経路や候補を開くが、答えを確定しない
```

### 絵巻

```text
「私」
→ 車窓を経験や記憶として見る

人工知性
→ 同じ車窓を文字・分類・関係として観測する
```

### Novel

```text
「私」と人工知性
→ 登場人物として判断に関わる
```

原則：

> 同じ車窓を見ている。しかし、同じ風景を見ているとは限らない。

Essayや技術考察では、必ずしも同じ形の登場人物にしない。

```text
Essay
→ 対話・視点差

Commentary
→ 同じニュースへの異なる読み

Technical Reflection
→ 仮説・検証・修正の往復

Research Paper
→ 著者・支援・方法を明確に分離
```

---

## 19．記憶機関庫

記憶機関庫には、過去の保存と現在の整備が共存する。

```text
記憶機関庫
├─ 旧noteアーカイブ
├─ 制作ノート
├─ JANUS-13 Anki
├─ Core10 / Core20 / Core30
├─ Concept Registry
├─ 意味の橋
├─ 音の橋
├─ 字体の橋
├─ 仮名遣いの橋
├─ 分節の橋
├─ カードテンプレート
├─ CSV
├─ 整備記録
└─ GitHubリポジトリへの入口
```

Novel末尾には大きな宣伝リンクを置かない。

候補：

```text
この列車の整備記録を見る
```

または、

```text
この言葉が夜に戻る場所
```

読者は次の順に作者へたどり着く。

```text
作品
↓
夜の帰還線
↓
記憶機関庫
↓
制作ノート
↓
GitHubリポジトリ
↓
作者
```

> 作品から作者へ直行するのではなく、作品から制作過程を通って作者へ至る。

GitHubリポジトリは公開状態を維持する。アクセス可能だが、中央駅正面では誘導しすぎない。

---

## 20．読者との関係

アクセス記録から、多くの読者が多言語そのものには強い関心を持たないことが観測された。

そのことを問題とはしない。

```text
すべての人に多言語構造を説明しない
すべての人をNovelへ誘導しない
すべての人を機関庫へ招かない
```

読者に、次の効果を一般的な効能として約束しない。

```text
言語野が鍛えられる
母語が磨かれる
知覚が静止する
悟りに至る
```

これらは制作・トレーニング上の仮説や観測として、制作ノートに記録する。

公開面では、静かな表現にする。

```text
異なる言葉を通ったあと、
同じ風景が同じように見えるとは限りません。
```

```text
列車を降りたあと、
何が変わったのかは記録されません。
```

原則：

> すべての人に読ませるために列車を走らせるのではない。三本のうち一つの行き先に引かれた人が、自分で乗車する。

---

## 21．推奨するGitHub構造

```text
MEMORIOPOLIS/
├─ canon/
│  ├─ prologue/
│  ├─ chapter01/
│  └─ chapter04/
│
├─ archive/
│  └─ note/
│     ├─ index.md
│     ├─ prologue/
│     └─ chapter01/
│
├─ anki/
│  ├─ concepts/
│  │  └─ concept_registry.csv
│  ├─ core/
│  │  ├─ core010/
│  │  ├─ core020/
│  │  └─ core030/
│  ├─ languages/
│  │  ├─ ko/
│  │  ├─ ru/
│  │  ├─ zh-TW/
│  │  ├─ en/
│  │  ├─ ja-modern/
│  │  └─ fil/
│  └─ templates/
│
├─ observation-notes/
│  ├─ index.md
│  ├─ O-0001_consonantal-landmarks.md
│  └─ O-0002_concept-anchored-randomness.md
│
├─ maintenance-log/
│  ├─ index.md
│  ├─ M-0001_english-tts.md
│  └─ M-0002_russian-audio-alignment.md
│
└─ web/
   ├─ station-board/
   ├─ platforms/
   ├─ scroll/
   ├─ trailers/
   ├─ janus-13/
   └─ roundhouse/
```

---

## 22．次回の制作手順

### 今夜

```text
1. 自宅Wi-Fiへ接続
2. OneDriveを一時停止
3. Windows上のフィリピン語Capabilityを確認
4. Basic機能を確認・導入
5. 必要なら再起動
6. TextToSpeechを確認・導入
7. 導入結果を確認
8. OneDriveを再開
```

### 次回のAnki制作

```text
1. section12_fil_draft01.mdを再読
2. 用語の自然さと一貫性を確認
3. C0001～C0010の対応語を確定
4. Filipino側の品詞・用法を確認
5. 語根と接辞を確認
6. PerceptualSegmentationを検討
7. MorphologicalBreakdownを作成
8. 意味の橋を作成
9. 音の橋を作成
10. フィリピン語版Core10の16フィールドを確定
11. マスターCSVを作成
12. Anki取込用CSVを作成
13. READMEを作成
14. ノートタイプ仕様を作成
15. ZIP化
16. PC版Ankiへインポート
17. TTSを確認
18. AnkiWebへ同期
19. AnkiDroidで確認
20. 親デッキで六つの観測面を混合
```

六つの観測面：

```text
Korean
Russian
TaiwaneseMandarin
English
ModernJapanese
Filipino
```

---

## 23．次回開始用プロンプト

```text
この引き継ぎ書を2026年9月16日の最新状態として、MEMORIOPOLIS / JANUS-13の制作を再開します。

第四章第十二節はCore10です。第四章第十三節は新出Conceptを10個追加してCore20、序章はその次の新出Conceptを10個追加してCore30とします。既知Conceptは新規採番せず、出現用例だけConcept Registryへ追加します。新出Conceptは重要度を第一基準、頻度を補強基準として10個ずつ採用します。

近代日本語版Anki Core10は、MEMORIOPOLIS::ModernJapaneseへ導入済みです。ロシア語カードの単語・例文TTSボタンも、tts-audioクラスによって中央配置へ修正済みです。

次の言語はフィリピン語Filipinoです。タガログ語を基盤とする標準フィリピン語として扱います。第四章第十二節のフィリピン語版Novel draft01、section12_fil_draft01.mdは作成済みです。

まず、今夜導入したWindowsのフィリピン語Basic機能とTextToSpeechの確認結果を整理してください。その後、section12_fil_draft01.mdを基に、C0001～C0010の対応語、用法、語根、接辞、知覚上の分節、形態素分解、意味の橋、音の橋を設計し、フィリピン語版Anki Core10のZIPを作成してください。

JANUS-13には、時間の垂直軸、日本語と外国語の関係を示す水平軸、文字列が音と単語として見えるまでの分節軸があります。子音標識仮説は普遍原理として断定せず、観測仮説として各言語で再検査します。

Ankiは音声名を固定せず、言語コードだけを指定して移植性を優先します。予告編では、人工知性を女性音声、「私」を男性音声として、話者別音声を生成してMP4へ統合します。
```

---

## 24．2026年9月16日の店じまい地点

```text
MEMORIOPOLIS親デッキ                 五観測面が開通
韓国語Core10                         運用中
ロシア語Core10                       運用中
ロシア語TTSボタン中央配置            完了
臺灣華語Core10                       運用中
英語Core10                           運用中
近代日本語版Novel 第十二節            作成済み
近代日本語版Anki Core10              PC版実装・プレビュー完了
近代日本語版AnkiWeb同期              実施対象
近代日本語版AnkiDroid確認            実施対象
フィリピン語版Novel 第十二節          draft01作成済み
フィリピン語言語機能                  今夜導入予定
フィリピン語Anki Core10              次回作成
Core20                              第四章第十三節
Core30                              序章
Concept Registry                    導入予定
制作ノート                           導入予定
旧note機関庫アーカイブ                方針確定
中央駅発車掲示板                     先発・次発・後発の三本
予告編音声                           AI=女性、「私」=男性
Anki音声                             音声名を固定せず移植性優先
```

本日の到達点を一文に集約すると、次のとおり。

> JANUS-13は、現代日本語と近代日本語を結ぶ時間の垂直軸、日本語と外国語を結ぶ関係の水平軸、そして文字列が音と単語として見えるまでの分節軸を持ち始めた。NovelはAnkiへ、Ankiは発見へ、発見は制作ノートへ、制作ノートは次の文章へ戻る。中央駅には三本の列車だけが現れ、縁のある読者が自分で乗車する。
