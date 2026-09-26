# MEMORIOPOLIS / JANUS-13 完全版引き継ぎ書

**更新日：2026年9月17日**  
**店じまい地点：フィリピン語版Anki Core10を導入し、AnkiDroidへの同期まで完了。インドネシア語のWindows言語機能とTTSパックの提供状況を確認済み。**  
**次回開始地点：自宅Wi-Fi環境でインドネシア語のBasicおよびTextToSpeechを導入し、その後、第四章第十二節のインドネシア語版NovelとAnki Core10を制作する。**

---

## 0．今回の最重要サマリー

- プロジェクト名は`JANUS-13`で統一する。
- 第四章第十二節は`Core10`である。
- 第四章第十三節は新出Conceptを10個追加して`Core20`とする。
- 序章はその次の新出Conceptを10個追加して`Core30`とする。
- Core番号は物語の章順ではなく、JANUS-13型Ankiへ投入した新出Conceptの累積数を表す。
- 既知Conceptは新規採番せず、新しい用例・出現箇所をConcept Registryへ追加する。
- 日本語正本から各言語のNovelを制作し、NovelからAnkiカードを作る。
- Ankiでトレーニングし、文字・音・文法・知覚についての発見を制作ノートへ記録する。
- JANUS-13には、時間の垂直軸、言語間関係の水平軸、文字から音・語構造を捉える分節軸がある。
- 学問的な系統・語源史はカードへ詰め込みすぎず、制作ノートと内部台帳で保持する。
- Ankiでは現代語時点の「縁」に櫛を通し、創作のための余白を残す。
- 現代で一般に使われない歴史文字は、通常のAnkiカードから外す。
- 現代の読解・発音・語形認識に働く文字だけを学習アンカーとして残す。
- ハングルは音節構造とパッチムを視覚化する。
- 繁體字・旧字体は、意味領域と音価の手掛かり、漢字文化圏の接続を可視化する。
- ラテン文字は語根・語幹・接辞・活用・派生・重複を横方向に比較しやすい。
- AnkiのTTSは音声名を固定せず、言語コードだけを指定して移植性を優先する。
- 予告編はAnkiと分離し、人工知性を女性音声、「私」を男性音声として話者別に生成する。
- GitHub Pagesの中央駅には、先発・次発・後発の三本だけをランダム表示する。

---

## 1．現在のMEMORIOPOLIS親デッキ

```text
MEMORIOPOLIS
├─ Korean
├─ Russian
├─ TaiwaneseMandarin
├─ English
├─ ModernJapanese
└─ Filipino
```

次に追加する予定のデッキ：

```text
MEMORIOPOLIS::Indonesian
```

現在の共通Conceptは次の10個。

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

## 2．制作とCore番号の規則

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

原則：

> Core番号は、物語の時系列ではなく、JANUS-13型Ankiへ追加した新出Conceptの累積数を表す。

```text
NarrativeOrder
→ 物語内部の章・節の順序

AnkiOrder
→ 作者が再観測・再整備した順序
```

新出Conceptの選定順：

```text
1. 対象本文を読む
2. Concept候補を抽出する
3. Concept Registryと照合する
4. 既知Conceptを新規候補から除外する
5. 新出Conceptを重要度と頻度で評価する
6. 上位10個を次のCoreへ採用する
7. 残りの候補を次回候補として保存する
```

評価基準：

```text
第一基準
→ その文章の判断や進行を動かしているか

第二基準
→ 作品全体で再登場する可能性があるか

第三基準
→ 複数言語で観測差が出るか

第四基準
→ 本文内での頻度が高いか

第五基準
→ 意味・音・分節の橋を作る価値があるか
```

> 重要度で選び、頻度で補強する。

---

## 3．制作循環

```text
日本語正本
↓
各言語のNovel
↓
新出Conceptを10個抽出
↓
JANUS-13型Ankiカード
↓
親デッキMEMORIOPOLISでトレーニング
↓
文字・音・文法・知覚上の発見
↓
制作ノート
↓
次のNovel・Essay・Commentary・Technical Reflection
```

短縮形：

```text
Novel
→ Anki
→ トレーニング
→ 発見
→ 制作ノート
→ 次の文章
```

> Ankiは完成作品の副教材ではなく、書いた文章を複数の言語面へ通し、作者内部に差異を蓄積して次の文章を変える中間工程である。

---

## 4．JANUS-13の三軸

### 4.1 時間の垂直軸

```text
近代日本語
歴史的仮名遣い・旧字体
        ⇅
現代日本語
現代仮名遣い・新字体
```

近代日本語は14番目の外国語ではない。

> 近代日本語は、現代日本語の下にある時間地層である。

### 4.2 言語間関係の水平軸

```text
現代日本語
⇄ 韓国語
⇄ ロシア語
⇄ 臺灣華語
⇄ 英語
⇄ フィリピン語
⇄ インドネシア語
⇄ ベトナム語
⇄ スペイン語
⇄ ポルトガル語
⇄ イタリア語
⇄ フランス語
⇄ ドイツ語
```

この軸は言語の重要度ランキングではない。

```text
古層接続
南蛮接続
近代化接続
現代・未来接続
```

などの関係座標を内部に保持する。

### 4.3 分節軸

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

観測項目：

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

```text
母音は、声を通す。
子音は、輪郭をつくる。
転写は、その二つを未知文字へ戻す。
```

これは普遍的な言語起源説ではなく、読解知覚についての観測仮説として扱う。

---

## 5．文字アンカーの採用原則

### 基本原則

> 現代で生きている文字は学習アンカーとしてAnkiへ置く。現代の日常使用から退いた文字は歴史的地層として制作ノートへ置く。

### Ankiへ残す情報

```text
現代の標準表記である
現代の読者が実際に使用する
発音の理解を助ける
語根・語幹・接辞・活用の認識を助ける
意味の推測を助ける
他のJANUS-13面との現代的な縁を作る
```

### 制作ノートへ送る情報

```text
現在は一般に使用されない歴史文字
語源史だけに必要な表記
学習対象語の理解へ直接寄与しない古形
複数の学説を長く説明しなければならない情報
創作上の連想には有効だが、反復を重くする情報
```

### 文字体系ごとの観測

```text
ハングル
→ 初声・中声・終声
→ 音節ブロック
→ パッチム
→ 音変化の起点

繁體字・旧字体
→ 意味領域
→ 形声文字の音の手掛かり
→ 漢字文化圏の共有層
→ 近代日本語と臺灣華語の視覚的接続

ラテン文字
→ 語根・語幹
→ 接辞
→ 活用語尾
→ 派生
→ 重複
→ 語形の横方向の比較

キリル文字
→ 転写で音価を確認
→ 子音配置を観測
→ 語幹と語尾を観測
```

中心命題：

> ハングルは音節を組み立てて見せ、漢字は意味を圧縮して見せ、ラテン文字は語の伸縮を並べて見せる。

---

## 6．「疎な精密さ」

JANUS-13では、学術上の正確さを放棄しない。ただし、すべてをカードへ詰め込まない。

```text
悪い緩さ
→ 不確かな系統関係を断定する
→ 音が似るだけで語源を結ぶ
→ 歴史的事実と創作上の連想を混同する

良い緩さ
→ すべてをカード上で説明しない
→ 現代語同士の響き・用法・構造の縁を観測する
→ 仮説を結論にせず、次の連想を開く
→ 学習者と創作者の余白を残す
```

目標：

> 正確だが、説明しすぎない。緩やかだが、虚偽ではない。

役割分担：

```text
Concept Registry
→ 座標と整合性を厳密に守る

Ankiカード
→ 現代語の意味・音・用法を軽く反復する

制作ノート
→ 学術上の留保と創作上の連想を接続する

Novel
→ 新しい交配を起こす
```

短く表現すると：

```text
歴史は、制作ノートに残す。
座標は、台帳で守る。
縁は、Ankiで反復する。
交配は、Novelで起こす。
```

---

## 7．第十三節からのフィールド負荷試験順

第四章第十二節は、実際に制作した順序を維持する特例とする。

第四章第十三節のCore20からは次の順で進める。

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
   語根・接辞・重複・派生語

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

これは重要度順ではなく、Ankiフィールドの負荷試験順である。

---

## 8．分節関連フィールド

```text
PerceptualSegmentation
→ 学習者が音を捉えるための仮設的な区切り

ConsonantLandmarks
→ 語の輪郭として知覚された子音配置

MorphologicalBreakdown
→ 語根・接辞・語尾などの形態上の分解
```

重要：

```text
知覚上の区切り
≠
音節
≠
形態素
```

検証順：

```text
ロシア語で子音標識を発見
↓
韓国語・ドイツ語で再検査
↓
ベトナム語で母音・声調との相補性を確認
↓
フランス語で語境界を越える接続を確認
↓
仮説を修正
```

---

## 9．近代日本語版Anki Core10

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

### 現在地

```text
デッキ作成             完了
ノートタイプ作成       完了
16フィールド設定       完了
CSVインポート          完了
表面テンプレート       完了
裏面テンプレート       完了
CSS                    完了
PC版プレビュー         完了
AnkiWeb同期            完了
AnkiDroid追加          完了
```

近代日本語の旧字体と臺灣華語の繁體字には、視覚的な親和性がある。

```text
記錄 ⇄ 記錄
檢證 ⇄ 檢證
權限 ⇄ 權限
經路 ⇄ 經路
```

この接続は系統の同一性ではなく、日本語内部の時間軸と漢字文化圏の関係軸の交差として扱う。

---

## 10．ロシア語カードのCSS修正

音声ボタンを中央配置済み。

### テンプレート

```html
<div class="tts-audio">
  {{tts ru_RU:Russian}}
</div>
```

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

PC版プレビューで、単語音声と例文音声の中央配置を確認済み。

---

## 11．フィリピン語版Novel

### 観測面

```text
日本語表示：フィリピン語
現地語表示：Filipino
補足：タガログ語を基盤とする標準フィリピン語
```

### 本文

```text
section12_fil.md
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

---

## 12．フィリピン語版Anki Core10

### ZIP

```text
MEMORIOPOLIS_Filipino_Core10_draft01_2026-09-17.zip
```

### デッキ

```text
MEMORIOPOLIS::Filipino
```

### ノートタイプ

```text
MEMORIOPOLIS Filipino Vocabulary
```

### Core10

```text
C0001  rekord          記録
C0002  alaala          記憶
C0003  lungsod         都市
C0004  abiso           通知
C0005  tugon           返信／応答
C0006  patutunguhan    宛先／行き先
C0007  lagda           署名
C0008  beripikasyon    検証
C0009  awtoridad       権限／権威
C0010  tungkulin       役割／職務
```

### 16フィールド

```text
1  ID
2  Filipino
3  Pronunciation
4  Japanese
5  PartOfSpeech
6  UsageNote
7  ExampleFilipino
8  ExampleJapanese
9  Root
10 Affixes
11 PerceptualSegmentation
12 MorphologicalBreakdown
13 MeaningBridge
14 SoundBridge
15 Source
16 CourseTags
```

### ZIP収録物

```text
fil_core10_master_draft01.csv
fil_core10_anki_draft01.csv
README_fil_core10_draft01.md
FILIPINO_NOTE_TYPE_DRAFT01.md
FILIPINO_CARD_TEMPLATE_DRAFT01.md
section12_fil_core10_excerpt_draft01.md
section12_fil_source.md
```

### カードCSS

最初のZIPには差分CSSのみが入っていたため、カード全体の完成版CSSへ差し替えた。

現在の設計：

```text
表面
→ Concept ID
→ Filipino
→ 単語
→ 発音・IPA
→ TTSボタン

裏面
→ 日本語
→ 品詞
→ 意味と用法
→ Filipino例文
→ 例文TTS
→ 日本語訳
→ 語根
→ 接辞
→ 知覚上の区切り
→ 形態の橋
→ 意味の橋
→ 音の橋
→ Source
```

色分け：

```text
日本語
→ 青灰

例文・Filipino
→ 緑

語根
→ 茶

接辞
→ 黄土

知覚上の区切り
→ 青

形態の橋
→ 紫

意味の橋
→ 緑

音の橋
→ 黄
```

### TTS

```html
{{tts fil_PH:Filipino}}
```

```html
{{tts fil_PH:ExampleFilipino}}
```

音声名は固定しない。

### 現在地

```text
Novel作成                  完了
Core10 ZIP                 完了
デッキ作成                 完了
ノートタイプ作成           完了
16フィールド作成           完了
テンプレート設定           完了
完成版CSS設定              完了
CSVインポート              完了
PC版プレビュー             完了
AnkiWeb同期                完了
AnkiDroidへデッキ到着      完了
AnkiDroid音声確認          後日実施
```

音声確認に適したカード：

```text
C0002 alaala
→ 母音の連続

C0003 lungsod
→ ng /ŋ/ と語末子音

C0006 patutunguhan
→ 長い語と語根・接辞

C0010 tungkulin
→ ng /ŋ/ と三音節の輪郭
```

### Windows言語機能

```text
Language.Basic~~~fil-PH~0.0.1.0
→ Installed

Language.Handwriting~~~fil-PH~0.0.1.0
→ NotPresent、不要

Language.TextToSpeech~~~fil-PH~0.0.1.0
→ Windows側で提供を確認できず
```

運用：

```text
PC版Anki
→ 音声なしの素振り

AnkiDroid
→ Android側のTTSで実機確認
```

---

## 13．フィリピン語とインドネシア語の文字方針

現代の標準フィリピン語と標準インドネシア語は、ラテン文字を基本表記とする。

歴史的には、フィリピンにはバイバインなど、インドネシア各地にはカウィ・ジャワ・バリ・スンダ・バタック・ロンタラ・ジャウィなどの文字層がある。

ただし、JANUS-13の通常カードでは、現代の日常読解に使わない歴史文字は扱わない。

```text
Anki
→ 現代のラテン文字
→ 語根・語幹・接辞・活用・派生・重複

制作ノート
→ 歴史的な文字地層
```

> 同じラテン文字が見えることは、同じ音・文法・文字史を意味しない。

---

## 14．次の言語：インドネシア語

### 言語名

```text
日本語：インドネシア語
現地語：Bahasa Indonesia
```

### デッキ案

```text
MEMORIOPOLIS::Indonesian
```

### ノートタイプ案

```text
MEMORIOPOLIS Indonesian Vocabulary
```

### タグ案

```text
memoriopolis::id::core10
```

### TTS予定

```html
<div class="tts-audio">
  {{tts id_ID:Indonesian}}
</div>
```

```html
<div class="tts-audio">
  {{tts id_ID:ExampleIndonesian}}
</div>
```

音声名`Andika`をカードへ固定せず、言語コードのみ指定する。

### フィリピン語との比較軸

```text
フィリピン語
→ 語根の前後・内部に接辞が現れる
→ 接中辞も観測対象

インドネシア語
→ 語根に接頭辞・接尾辞が付く
→ 重複が意味・文法機能を担う
→ 派生語族を横方向に比較しやすい
```

明日の中心的な問い：

> 同じオーストロネシア語族でも、フィリピン語とインドネシア語は、語根の輪郭をどのように違って見せるのか。

---

## 15．インドネシア語Windows言語パックの確認結果

管理者PowerShellで、次の確認を実施済み。

```powershell
Get-WindowsCapability -Online |
Where-Object {
    $_.Name -match '^Language\..*~~~id-ID~'
} |
Select-Object Name, State
```

実機で確認された結果：

```text
Language.Basic~~~id-ID~0.0.1.0          NotPresent
Language.Handwriting~~~id-ID~0.0.1.0    NotPresent
Language.TextToSpeech~~~id-ID~0.0.1.0   NotPresent
```

結論：

```text
Basic
→ 提供あり、未導入

Handwriting
→ 提供あり、未導入
→ 今回は不要

TextToSpeech
→ 提供あり、未導入
→ 今夜導入する
```

フィリピン語と異なり、インドネシア語はPC版Ankiでも音声再生できる見込みがある。

---

## 16．次回夜のPowerShell作業

### 事前準備

```text
1. 自宅Wi-Fiへ接続
2. OneDrive同期を一時停止
3. 管理者モードでPowerShellを起動
```

### Step 1：Basicを導入

```powershell
Add-WindowsCapability -Online -Name "Language.Basic~~~id-ID~0.0.1.0"
```

処理中は次を守る。

```text
PowerShellを閉じない
同じコマンドを再実行しない
PCをスリープさせない
Wi-Fiを切断しない
```

プロンプトへ戻ったら、結果の`RestartNeeded`を確認する。

### Step 2：TextToSpeechを導入

Basicの処理完了後に実行する。

```powershell
Add-WindowsCapability -Online -Name "Language.TextToSpeech~~~id-ID~0.0.1.0"
```

BasicとTextToSpeechを同時実行しない。

### Step 3：状態確認

```powershell
Get-WindowsCapability -Online |
Where-Object {
    $_.Name -match '^Language\..*~~~id-ID~'
} |
Select-Object Name, State
```

期待する最終状態：

```text
Language.Basic~~~id-ID~0.0.1.0          Installed
Language.Handwriting~~~id-ID~0.0.1.0    NotPresent
Language.TextToSpeech~~~id-ID~0.0.1.0   Installed
```

### Step 4：終了

```text
必要な場合のみ再起動
↓
OneDrive同期を再開
```

---

## 17．インドネシア語版の制作予定

```text
1. 第四章第十二節のインドネシア語版Novelを作成
2. 小説としての自然さと用語の一貫性を確認
3. C0001～C0010の対応語を確定
4. 品詞と現代用法を整理
5. 語根を確認
6. 接頭辞・接尾辞を確認
7. 重複形を確認
8. PerceptualSegmentationを設計
9. MorphologicalBreakdownを設計
10. MeaningBridgeを作成
11. SoundBridgeを作成
12. 16フィールドを確定
13. マスターCSVを作成
14. Anki取込用CSVを作成
15. READMEを作成
16. ノートタイプ仕様を作成
17. 完成版カードテンプレートとCSSを作成
18. ZIP化
19. PC版Ankiへ導入
20. PC版でTTSを確認
21. AnkiWebへ同期
22. AnkiDroidで確認
23. 親デッキMEMORIOPOLISで七言語面を混合
```

七言語面：

```text
Korean
Russian
TaiwaneseMandarin
English
ModernJapanese
Filipino
Indonesian
```

---

## 18．Anki音声と予告編音声

### Anki

```text
目的
→ 学習・反復・移植性

指定
→ 言語コードのみ

音声名
→ 固定しない
```

### 予告編

```text
人工知性
→ 女性音声

「私」
→ 男性音声

担当者など
→ 必要に応じて第三の音声
```

制作工程：

```text
人工知性の台詞
→ ai_voice.wav

「私」の台詞
→ narrator_voice.wav

第三話者
→ operator_voice.wav

環境音・音楽
→ background.wav

絵巻素材
→ images / video

最終工程
→ 音声と映像を統合してMP4
```

論理名：

```text
AI_VOICE
NARRATOR_VOICE
OPERATOR_VOICE
```

実際の音声名は言語別設定で管理し、台本やAnkiカードへ直接埋め込まない。

---

## 19．制作ノートへ加える言語地層の観測

### 台湾からフィリピン語への縁

```text
臺灣華語
→ 中国語系の現代の観測面

台湾語
→ 閩南語系

台湾原住民族諸語
→ オーストロネシア語族

フィリピン語
→ タガログ語を基盤とするオーストロネシア語族
```

正確な接続：

```text
臺灣華語 → 台湾語 → フィリピン語
```

という直接系譜ではない。

制作ノート向け表現：

> 近代日本語版を親デッキへ加えると、旧字体が臺灣華語の繁體字と視覚的に接続した。その臺灣華語の背後にある台湾という場所には、中国語系の臺灣華語・台湾語とは別に、オーストロネシア語族の台湾原住民族諸語という古い地層がある。フィリピン語はタガログ語を基盤とするオーストロネシア語族の言語である。文字の縁から島々の言語史へ、JANUS-13の関係軸が伸びた。

短縮形：

```text
旧字体から繁體字へ。
繁體字から台湾へ。
台湾から島々の言語へ。
島々の言語からフィリピン語へ。
```

### 現代語の地層

英語も日本語も、一つの純粋な成分ではなく、系統的な基層と接触層を持つ。

```text
英語
→ ゲルマン語の系統的基層
→ 古ノルド語との接触
→ ノルマン・フランス語
→ ラテン語・ギリシャ語の宗教・学術層

日本語
→ 日琉語族の系統的基盤
→ 朝鮮半島を経由した移動と接触
→ 中国語・漢字・漢文の巨大な接触層
→ アイヌ語など列島内の異系統言語との接触
→ 南蛮・蘭学・近代西洋語
```

重要な留保：

```text
共通祖語からの継承
借用語
言語接触
文字体系
翻訳語
類型的類似
```

を同一視しない。

JANUS-13では、語族の正統性を争うのではなく、古層の上に接触・制度・侵略・交易・文化輸入・翻訳の層が積み重なり、現代語が日常語から抽象概念まで扱える奥行きを獲得したことに注目する。

中心命題：

> 母語そのものが、すでに複数の時間と接触を内蔵した多言語的な地層である。

---

## 20．中央駅と公開導線

中央駅には作品リンクを積み上げない。

```text
記憶都市中央駅

発車標
├─ 先発
├─ 次発
└─ 後発
```

三本だけをランダム表示する。

```text
中央駅
→ 現在接続できる三本だけ

記憶機関庫
→ 過去に走った列車の保存
```

公開導線：

```text
中央駅
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
文章を動かした一文
↓
本文
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

原則：

> 列車は来ている。乗るかどうかは読者が決める。

> 作品から作者へ直行するのではなく、作品から制作過程を通って作者へ至る。

---

## 21．次回開始用プロンプト

```text
この引き継ぎ書を2026年9月17日の最新状態として、MEMORIOPOLIS / JANUS-13の制作を再開します。

フィリピン語版Anki Core10は、MEMORIOPOLIS::Filipinoへ導入し、AnkiWebを経由してAnkiDroidへ同期済みです。AnkiDroidでのフィリピン語TTS確認は後日行います。

次の言語はインドネシア語、Bahasa Indonesiaです。デッキ名はMEMORIOPOLIS::Indonesian、ノートタイプ名はMEMORIOPOLIS Indonesian Vocabularyとします。

Windows実機では、Language.Basic~~~id-ID~0.0.1.0、Language.Handwriting~~~id-ID~0.0.1.0、Language.TextToSpeech~~~id-ID~0.0.1.0が存在し、すべてNotPresentであることを確認済みです。Handwritingは不要です。

まず管理者PowerShellで、Basicを導入し、完了後にTextToSpeechを導入してください。両方の状態がInstalledになったことを確認した後、必要な場合だけ再起動し、OneDriveを再開します。

その後、第四章第十二節のインドネシア語版Novelを作成してください。Novelを基に、C0001～C0010の対応語、現代用法、語根、接辞、重複、知覚上の区切り、形態の橋、意味の橋、音の橋を設計し、インドネシア語版Anki Core10をZIPへまとめてください。

JANUS-13では、現代で使われない歴史文字は通常のAnkiカードから外します。文字は文化財として収集するのではなく、現代語の内部構造を透視する学習アンカーとして採用します。ハングルは音節とパッチム、繁體字・旧字体は意味と音価の手掛かり、ラテン文字は語根・語幹・接辞・活用・派生・重複を可視化します。

学問的な系統・語源史はConcept Registryと制作ノートで保持し、Ankiカードでは現代語時点の縁に櫛を通します。正確だが説明しすぎない、疎な精密さを維持してください。

AnkiのTTSは音声名を固定せず、id_IDの言語コードだけを指定して移植性を優先します。
```

---

## 22．2026年9月17日の店じまい地点

```text
MEMORIOPOLIS親デッキ                  六言語面が開通
韓国語Core10                          運用中
ロシア語Core10                        運用中
ロシア語TTSボタン中央配置             完了
臺灣華語Core10                        運用中
英語Core10                            運用中
近代日本語Core10                      AnkiDroidへ追加完了
フィリピン語Novel 第十二節             完了
フィリピン語Core10 ZIP                完了
フィリピン語Ankiデッキ                完了
フィリピン語完成版CSS                 完了
フィリピン語AnkiWeb同期               完了
フィリピン語AnkiDroid到着             完了
フィリピン語AnkiDroid音声             後日確認
フィリピン語Windows Basic             Installed
フィリピン語Windows TTS               提供確認できず
インドネシア語Capability確認           完了
インドネシア語Basic                   提供あり、NotPresent
インドネシア語TextToSpeech            提供あり、NotPresent
インドネシア語Handwriting             提供あり、不要
インドネシア語言語パック導入           次回夜
インドネシア語Novel                   次回作成
インドネシア語Core10                  次回作成
Core20                               第四章第十三節
Core30                               序章
Concept Registry                     導入予定
制作ノート                            継続整備
旧note機関庫アーカイブ                 方針確定
中央駅発車掲示板                      先発・次発・後発の三本
Anki音声                              音声名を固定せず移植性優先
予告編音声                            AI=女性、「私」=男性
文字採用原則                          現代の学習アンカーを優先
```

本日の到達点：

> JANUS-13の六番目の言語面としてフィリピン語が開通した。フィリピン語カードでは、ラテン文字を通して語根・接辞・知覚上の区切り・形態上の分解を分離した。次のインドネシア語では、同じオーストロネシア語族に属しながら異なる語形成、特に接辞・重複・派生語を観測する。歴史文字は制作ノートへ、現代の読解に働く文字はAnkiへ置き、疎な精密さによって創作の余白を保つ。
