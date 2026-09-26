# MEMORIOPOLIS / JANUS-13 完全版引き継ぎ書

更新日時：2026年9月25日 12:46 JST  
版：Concept画像10景作成・ロシア語UI改修完了版  
次回作業日：2026年9月26日

---

## 1．本書の目的

本書は、『記憶都市（メモリオポリス）』およびJANUS-13について、2026年9月25日時点の制作、Anki実装、Concept画像、カードUI、学習運用、語彙配分、GitHub運用の全方針を、次回以降へ正確に引き継ぐための完全版文書である。

本日の主要な到達点は次のとおり。

1. C0001～C0010のConcept画像10景を一つの連続した絵巻として作成した。
2. 5列×2行の一枚絵から、各Conceptの縦長画像10枚へ分割した。
3. Anki用WebPと保存用PNGをZIP化した。
4. ModernJapaneseへ`ConceptScene`フィールドを追加し、C0001へ画像を登録・同期した。
5. ModernJapaneseのC0001は当日のDaily Training対象外だったため、通常学習画面での確認は翌日以降へ持ち越した。
6. ロシア語ノートタイプにも`ConceptScene`を追加し、C0001へ同じ画像を登録した。
7. ロシア語カード表面で、Concept ID、Concept画像、ロシア語語形の順に正常表示できた。
8. ロシア語カード裏面を、ドイツ語版を基準とする3つのプルダウンUIへ改修した。
9. ロシア語版のSourceに含まれる`draft01`を外し、論理的出典IDへ正規化する方針を確定した。
10. 2026年9月26日のJANUS-13 Daily Trainingで、画像、同期、TTS、ダークモード、プルダウンの実運用確認を行う。

---

## 2．正式名称と活動の中心線

正式な小説タイトル：『記憶都市（メモリオポリス）』  
英字表記：MEMORIOPOLIS  
多言語創作・学習体系：JANUS-13

GitHubを正本とする。

- Novel、Essay、設計、日々の記録：Markdown
- 多言語変換訓練：Anki
- 復習制御：FSRS
- 言語間の共通座標：Concept ID
- 公開姿勢：縁のある人がGitHubへアクセスすればよい
- Note、YouTube、GitHub Pages：当面の必須工程にしない

中心となる循環：

```text
読む
  ↓
現代日本語で考える・書く
  ↓
Concept候補を発見する
  ↓
JANUS-13へ展開する
  ↓
Ankiで変換訓練する
  ↓
カバー率と想起状態を観測する
  ↓
次の読書・創作へ戻す
```

---

## 3．JANUS-13の13言語・14観測面

### 対象言語

1. 日本語
   - 現代日本語面
   - 近代日本語面
2. 韓国語
3. ロシア語
4. 臺灣華語
5. 英語
6. フィリピン語
7. インドネシア語
8. ベトナム語
9. スペイン語（スペイン、es-ES）
10. ポルトガル語（ブラジル、pt-BR）
11. イタリア語
12. フランス語（フランス、fr-FR）
13. ドイツ語（ドイツ、de-DE）

日本語だけが二つの時間面を持つため、13言語・14観測面となる。

---

## 4．最重要：日本語Novelと日本語Ankiの構造

### Novel

```text
日本語Novel
├─ 現代日本語版
└─ 近代日本語版
```

- 現代日本語版：創作・意味・推敲の日本語正本
- 近代日本語版：旧字体、歴史的仮名遣いなどを観測する時間面

### Anki

日本語の独立Ankiデッキは一つだけである。

```text
MEMORIOPOLIS::ModernJapanese
```

これが日本語系Ankiの唯一の正である。

- 近代日本語表記を主表示にする
- 同じノート内に現代日本語表記、現代読み、例文読み、字体・仮名遣い・意味・音の橋を持つ
- 現代日本語専用の独立Ankiデッキは作成しない
- `ModernJapanese`はJANUS-13内では近代日本語版Ankiを指す

### 数え方

```text
作品・Concept上：13言語・14観測面
Anki上：13言語デッキ
日本語Ankiの正：MEMORIOPOLIS::ModernJapanese
```

---

## 5．現在のAnkiデッキ構成

```text
MEMORIOPOLIS::English
MEMORIOPOLIS::Filipino
MEMORIOPOLIS::French
MEMORIOPOLIS::German
MEMORIOPOLIS::Indonesian
MEMORIOPOLIS::Italian
MEMORIOPOLIS::Korean
MEMORIOPOLIS::ModernJapanese
MEMORIOPOLIS::Portuguese
MEMORIOPOLIS::Russian
MEMORIOPOLIS::Spanish
MEMORIOPOLIS::TaiwaneseMandarin
MEMORIOPOLIS::Vietnamese
```

横断学習デッキ：

```text
JANUS-13 Daily Training
```

全13言語Ankiデッキは開通済み。

---

## 6．Core10

| Concept ID | 日本語Concept |
|---|---|
| C0001 | 記録 |
| C0002 | 記憶 |
| C0003 | 都市 |
| C0004 | 通知 |
| C0005 | 返信／応答 |
| C0006 | 宛先／受取人 |
| C0007 | 署名 |
| C0008 | 検証 |
| C0009 | 権限／許可 |
| C0010 | 役割／ロール |

Core10は第四章第十二節の中核Conceptであり、名詞中心である。

---

## 7．Concept画像の思想

Concept画像は、空欄から答えを100％再生するための問題画像ではない。

```text
画像・人物・文字・自然・場所
  ↓
Novelの場面
  ↓
Concept
  ↓
各言語の語形・音声・意味
  ↓
次の読解・発話・創作
```

Concept画像は、入力から出力への変換経路へ追加する情報の一つである。

### 優先する性質

- 美しいこと
- 印象に残ること
- 何度見ても再訪できること
- 場面として固有であること
- 人物、視線、手の動き、物の配置から物語が立ち上がること
- 衣食住、自然、光、時間帯を含むこと
- 八卦、星図、方位、兆候、儀礼的配置などの象徴層を含み得ること
- 漫画的な魔法表現ではなく、民俗学的な観測・記録・解釈の雰囲気を保つこと

### 文字について

文字なしを絶対的な正としない。

画像内の文字は、辞書的な答え表示ではなく、記憶風景を構成する入力情報として許容する。

- Concept ID
- 日本語見出し
- 短い文
- 帳面や標識の文字
- 都市内の記録・署名・通知

これらが美しさ、印象、物語性を高めるなら採用してよい。

---

## 8．Concept画像10景

C0001～C0010を、同じ記憶都市の世界観を持つ連続した絵巻として作成した。

### 画像の内容

- C0001 記録：帳面、砂時計、都市、書き残す人物
- C0002 記憶：星図、過去の断片、時間層を見上げる人物
- C0003 都市：塔、橋、水路、住民、空と水
- C0004 通知：梟、封書、灯火、光の信号
- C0005 返信：封書、返送、窓外の都市、猫
- C0006 宛先：分岐する道標、都市、旅装の人物、鳥
- C0007 署名：筆記する手、紙、封印、署名
- C0008 検証：拡大鏡、星図、観測具、比較と確認
- C0009 権限：門、守る人物、秤、境界
- C0010 役割：共同作業、道具、異なる担当、都市を支える人々

### ZIP

```text
MEMORIOPOLIS_ConceptImages_C0001-C0010_2026-09-25.zip
```

### ZIPの内容

```text
README.md
manifest.csv

png/
  memoriopolis_c0001_record.png
  memoriopolis_c0002_memory.png
  memoriopolis_c0003_city.png
  memoriopolis_c0004_notification.png
  memoriopolis_c0005_reply.png
  memoriopolis_c0006_recipient.png
  memoriopolis_c0007_signature.png
  memoriopolis_c0008_verification.png
  memoriopolis_c0009_authorization.png
  memoriopolis_c0010_role.png

webp/
  memoriopolis_c0001_record.webp
  memoriopolis_c0002_memory.webp
  memoriopolis_c0003_city.webp
  memoriopolis_c0004_notification.webp
  memoriopolis_c0005_reply.webp
  memoriopolis_c0006_recipient.webp
  memoriopolis_c0007_signature.webp
  memoriopolis_c0008_verification.webp
  memoriopolis_c0009_authorization.webp
  memoriopolis_c0010_role.webp
```

### 使い分け

- Anki：WebP
- GitHub原本：PNG
- 対応表：manifest.csv

### 分割後の寸法

- 横幅：約248～250px
- 高さ：約625～626px
- WebP容量：約60～81KB／枚

初期AnkiDroid試験には十分。将来、大きな表示や高解像度が必要になった場合は、同じ構図を保ちながら個別高解像度版へ更新できる。

---

## 9．ConceptScene共通仕様

フィールド名：

```text
ConceptScene
```

原則として既存フィールドの末尾へ追加する。既存フィールドの順序は変更しない。

### 表面テンプレート

Concept IDの直後、対象語の前へ配置する。

```html
<div class="concept-id">{{ID}}</div>

{{#ConceptScene}}
<div class="concept-scene">
  {{ConceptScene}}
</div>
{{/ConceptScene}}
```

### CSS

```css
.concept-scene {
  width: 100%;
  margin: 12px auto 16px auto;
  text-align: center;
}

.concept-scene img {
  display: block;
  width: auto;
  max-width: 100%;
  max-height: 420px;
  height: auto;
  object-fit: contain;
  margin: 0 auto;
  border-radius: 10px;
}

@media (max-width: 600px) {
  .concept-scene img {
    max-height: 320px;
  }
}
```

画面を占有しすぎる場合は、モバイル用`max-height`を280pxへ下げる。

### 原則

- 同じConcept IDには同じ画像
- 言語別に画像を複製しない
- カード数を増やさない
- 独立した画像カードは作らない
- 既存カードの表面へ入力信号として追加する
- 画像が空欄のカードでは空白領域を表示しない

---

## 10．ModernJapaneseへの導入状況

ノートタイプ：

```text
MEMORIOPOLIS Modern Japanese Vocabulary
```

現行16フィールドの末尾へ、17番目として追加した。

```text
17. ConceptScene
```

### 試験対象

```text
デッキ：MEMORIOPOLIS::ModernJapanese
対象：C0001
近代日本語：記錄
現代日本語：記録
画像：memoriopolis_c0001_record.webp
```

### 状況

- C0001へ画像を登録済み
- PC版Ankiでのテンプレート構造を設定済み
- Anki同期済み
- 当日のDaily TrainingではC0001が抽出されなかった
- 画像追加やフィールド変更では、カードの復習期限は変化しない
- Daily Trainingに出なかったことは同期失敗を意味しない

### 今後

2026年9月26日以降、Daily Trainingに抽出された場合は通常学習内で確認する。抽出されない場合は、カード管理のプレビューで直接確認する。

ModernJapanese C0001で成功後、C0001～C0010へ展開する。その後、他言語へ順次適用する。

---

## 11．ロシア語への導入状況

デッキ：

```text
MEMORIOPOLIS::Russian
```

ノートタイプ：

```text
MEMORIOPOLIS Russian Vocabulary
```

### ConceptScene

既存フィールドの末尾へ`ConceptScene`を追加した。

C0001へ次の画像を登録した。

```text
memoriopolis_c0001_record.webp
```

### 表面

正常表示を確認済み。

```text
C0001
Concept画像
запись
強勢付き語形
単語TTS
```

画像は中央表示され、縦横比を維持し、ロシア語見出し語も十分に目立つ。

画像内にもC0001と「記録」があるため、Concept IDが二重に見えるが、現段階では入力情報の重複として許容する。数日使用後に気になるかを観測する。

---

## 12．ロシア語UIの改修

ロシア語版は、従来、情報が個別の箱として縦に並び、他言語と比べて少し寂しい印象があった。

ドイツ語版を基準として、次の3段プルダウンへ集約した。

```text
▶ 語の構造
▶ 例文解説
▶ 言語間ブリッジ
```

### 初期表示に残す情報

- Transliteration
- 日本語
- 品詞
- ロシア語例文
- 例文TTS
- 例文の日本語訳

### 語の構造

- 性・数・格・語形
- 強勢付き語形
- 必要に応じて転写

### 例文解説

- 例文・強勢付き
- 例文・転写
- 文の組み立て
- なぜこの意味・語形になるか

### 言語間ブリッジ

現段階では、次を暫定利用する。

- `ExamplePronunciationHint`：音の橋
- `Japanese`：日本語との接続

将来、専用フィールドを追加する候補：

```text
LanguageBridge
```

### UI評価

- Concept画像と語形の関係が明確になった
- 例文とTTSは初期表示に残り、学習直後に確認できる
- 詳細説明は必要なときだけ開ける
- ドイツ語版と同じ操作感になった
- ロシア語固有の屈折、強勢、発音情報を「語の構造」に保持できる

---

## 13．3段プルダウンの共通CSS

```css
.detail-block {
  margin-top: 0.8rem;
  border: 1px solid #d6d3d1;
  border-radius: 9px;
  overflow: hidden;
  text-align: left;
}

.detail-block summary {
  cursor: pointer;
  padding: 0.85rem 1rem;
  font-weight: 700;
  text-align: center;
  list-style-position: inside;
}

.detail-block summary:hover {
  background: rgba(31, 58, 95, 0.06);
}

.detail-content {
  padding: 0.4rem 1rem 1rem 1rem;
  line-height: 1.7;
}

.detail-label {
  margin-top: 0.8rem;
  margin-bottom: 0.25rem;
  font-size: 0.85rem;
  font-weight: 700;
  color: #526176;
}

.structure-block summary {
  background: #f2edf8;
  color: #4c365f;
}

.explanation-block summary {
  background: #e9f2f9;
  color: #294e68;
}

.bridge-block summary {
  background: #edf5ee;
  color: #36583d;
}
```

### ダークモード

```css
.nightMode .detail-block,
.night_mode .detail-block {
  color: #f2f4f7;
  background: #303030;
  border-color: #6b7280;
}

.nightMode .detail-label,
.night_mode .detail-label {
  color: #c4d0df;
}

.nightMode .structure-block summary,
.night_mode .structure-block summary {
  color: #f1e7ff;
  background: #453752;
}

.nightMode .explanation-block summary,
.night_mode .explanation-block summary {
  color: #e2f3ff;
  background: #29475c;
}

.nightMode .bridge-block summary,
.night_mode .bridge-block summary {
  color: #e6f6e9;
  background: #34503a;
}

.nightMode .detail-content,
.night_mode .detail-content {
  color: #f2f4f7;
}
```

色の意味：

- 語の構造：紫系
- 例文解説：青系
- 言語間ブリッジ：緑系

---

## 14．ドイツ語版UIから得た共通原則

ドイツ語版の良い点：

- `details`と`summary`によるプルダウン
- 初期表示が過密にならない
- 「語の構造」「例文解説」「言語間ブリッジ」の3区分
- PC版とAnkiDroidの双方で操作しやすい
- ダークモード対応

今後は、ドイツ語版をJANUS-13共通UIの基盤とする。

ただし、各プルダウン内部は言語固有プロファイルとして設計する。

### 共通UI層

- Concept ID
- Concept画像
- 対象語
- 発音・読み
- TTS
- 日本語Concept
- 品詞
- 用法
- 例文
- 例文TTS
- 日本語訳
- 3つのプルダウン
- Source
- ダークモード
- モバイル対応

### 言語プロファイル層

- ロシア語：格、性、数、強勢、硬音・軟音、動詞の体
- ドイツ語：語幹、接辞、複合語、性、格、語順
- ロマンス諸語：語幹、接辞、性・数、活用、ラテン語系対応
- フィリピン語：語根、接辞、重複、焦点・ヴォイス
- インドネシア語：語根、接頭辞、接尾辞、接周辞、重複
- ベトナム語：音節、声調、複合語、漢越語、類別詞
- 臺灣華語：繁体字、注音、拼音、声調、字義、量詞、日本語漢字との差
- 韓国語：音節ブロック、語幹、語尾、助詞、終声、音韻変化、漢字語・固有語
- ModernJapanese：旧字体、歴史的仮名遣い、現代読み、四つの橋

---

## 15．Source正規化

ロシア語カードのSourceには次の値が入っていた。

```text
section12_ru_draft01
```

`draft01`はテンプレートに直接書かれているのではなく、各ノートの`Source`フィールドの値である。

版番号を外し、論理的な出典IDへ統一する。

推奨値：

```text
section12_ru
```

### 理由

- `draft02`や改訂版が生まれてもカード側のSourceを変更せずに済む
- GitHub上の正本を指す論理的識別子として機能する
- カードへ制作途中の版番号を表示しない

### 一括置換

対象：

```text
deck:MEMORIOPOLIS::Russian
```

検索文字列：

```text
section12_ru_draft01
```

置換後：

```text
section12_ru
```

対象フィールド：

```text
Source
```

表示ラベルは当面、次のままでよい。

```html
<div class="source">
  Source: {{Source}}
</div>
```

将来、日本語化する場合：

```html
{{#Source}}
<div class="source">
  出典：{{Source}}
</div>
{{/Source}}
```

今後、他言語のSourceに含まれる`draft01`も、各言語の改修時に順次外す。

---

## 16．2026年9月26日の確認項目

### JANUS-13 Daily Training

Daily Trainingを通常どおり再構築する。

第1フィルター：

```text
deck:MEMORIOPOLIS is:due
```

第2フィルター：

```text
deck:MEMORIOPOLIS is:new
```

ModernJapaneseまたはロシア語のC0001が抽出された場合は、通常学習の中でConcept画像を確認する。

抽出されない場合は、期限対象ではないだけであり、同期失敗ではない。カード管理のプレビューで直接確認する。

### PC版Anki

- ModernJapanese C0001に画像が表示される
- Russian C0001に画像が表示される
- 画像が中央にある
- 縦横比が崩れない
- 横スクロールが出ない
- TTSが動作する
- C0002以降に空枠が出ない
- ロシア語裏面に3つのプルダウンが表示される
- プルダウンが開閉できる
- Sourceが`section12_ru`になっている

### AnkiDroid

- 画像メディアが同期される
- 画像が欠落しない
- 画像が大きすぎない
- ダークモードで対象語と例文が読める
- TTSが動作する
- 3つのプルダウンが開閉できる
- プルダウン内部の文字色が読める
- スクロール量が過大でない

### 学習上の観測

- 画像を見た瞬間に何が起動したか
- 画像内文字を先に読んだか
- 人物、帳面、都市を先に見たか
- Novelの場面が起動したか
- 「記録」というConceptへ自然に到達したか
- ロシア語`запись`へ到達しやすくなったか
- 画像を数回見ても再訪したいと感じるか
- Concept IDの二重表示が気になるか

---

## 17．今後のConcept画像展開順

### 第1段階

```text
ModernJapanese C0001
Russian C0001
```

表示、同期、TTS、ダークモード、学習感を確認する。

### 第2段階

成功後：

```text
ModernJapanese C0001～C0010
```

日本語系Ankiの正であるModernJapaneseを最初に完成させる。

### 第3段階

```text
Russian C0001～C0010
```

ロシア語は、共通UIとConcept画像の最初の他言語展開例とする。

### 第4段階

他言語へ順次展開する。

- ヨーロッパ系言語
- ASEAN系言語
- 臺灣華語
- 韓国語

一括変更せず、言語ごとにテンプレート、TTS、ダークモード、長い語形、言語固有情報を確認する。

---

## 18．Anki統計と運用

2026年9月24日12:26ごろの基準統計：

- 合計：35枚
- 新規：10枚
- 定着前：25枚
- 定着：0枚
- 解答回数：367回
- 学習日数：31日中11日
- 学習日の平均：33回
- 復習間隔中央値：2日
- 安定性中央値：1日
- 難しさ中央値：71％
- 予測想起率平均：79％

導入初期のため、設定は変更しない。

FSRS：

- 有効
- 目標保持率90％
- 一括再スケジュールはオフ
- 新規上限10
- 復習上限200
- 学習ステップ1m 10m
- 再学習10m

---

## 19．未知語と1,200 Concept

未知語をすべてAnkiへ入れない。

```text
未知語に遭遇
  ├─ その場で調べて終了
  ├─ Markdownへ記録
  ├─ 再出現待ち
  └─ Core採用候補
```

目標：

> なんとなく読める。なんとなく意味がつかめる。核心語だけ必要に応じて調べられる。

1,200 Conceptは少なくない。

```text
1,200 Concept × 14観測面
= 16,800カード相当の対応関係
```

未知語をなくすのではなく、文章の骨格を捉え、必要な語だけ検索できる変換体系を作る。

---

## 20．1,200 Conceptの目標配分

| 領域 | 目標数 | 比率 |
|---|---:|---:|
| 機能語・文法機能 | 150 | 12.5％ |
| 基本動詞・状態変化 | 180 | 15.0％ |
| 日常名詞 | 220 | 18.3％ |
| 性質・状態 | 130 | 10.8％ |
| 時間・空間・数量 | 100 | 8.3％ |
| 思考・感情・判断 | 100 | 8.3％ |
| 社会・人間関係・制度 | 100 | 8.3％ |
| 読書・ニュース・議論 | 80 | 6.7％ |
| MEMORIOPOLIS固有Concept | 90 | 7.5％ |
| 可変枠 | 50 | 4.2％ |
| **合計** | **1,200** | **100％** |

Concept選定：

```text
計画配分枠：50％
実出現枠：30％
縁・発見枠：20％
```

Core10単位で厳密に合わせず、Core50単位で累積配分を調整する。

---

## 21．Core20暫定候補

| ID | 日本語Concept | 主な役割 |
|---|---|---|
| C0011 | ある | 存在 |
| C0012 | する | 実行 |
| C0013 | 持つ | 所有・保持 |
| C0014 | 作る | 生成 |
| C0015 | 送る | 移動・伝達 |
| C0016 | 受け取る | 授受 |
| C0017 | 見る | 知覚 |
| C0018 | 確認する | 一般的な確認行為 |
| C0019 | ここ | 場所指示 |
| C0020 | 誰 | 主体への疑問 |

基本原則：

> 名詞を10個置いたら、次の10個で名詞を動かす。さらに次の10個で、時間・否定・疑問・比較を加える。

---

## 22．次回開始用プロンプト

```text
この引き継ぎ書を2026年9月25日の最新状態として、MEMORIOPOLIS / JANUS-13を再開します。

JANUS-13の全13言語Ankiデッキは開通済みです。Novelの日本語系は現代日本語版と近代日本語版の二面を持ちますが、日本語系Ankiの正は近代日本語版であるMEMORIOPOLIS::ModernJapaneseのみです。現代日本語の独立Ankiデッキは作成しません。

C0001～C0010のConcept画像10景は完成済みです。一枚絵を各Conceptの縦長画像へ分割し、Anki用WebPと保存用PNGをMEMORIOPOLIS_ConceptImages_C0001-C0010_2026-09-25.zipへまとめています。同一Concept IDでは、全言語が同じ画像ファイルを共有します。

ModernJapaneseには17番目のフィールドとしてConceptSceneを追加し、C0001へmemoriopolis_c0001_record.webpを登録・同期済みです。2026年9月25日のDaily TrainingではC0001が期限対象ではなかったため、通常学習画面では表示されませんでした。これは同期失敗ではありません。

ロシア語ノートタイプにもConceptSceneを追加し、C0001へ同じ画像を登録しました。表面ではC0001、Concept画像、запись、強勢付き語形、TTSの順で正常表示されています。

ロシア語裏面は、ドイツ語版を基準として、語の構造、例文解説、言語間ブリッジの3つのプルダウンへ改修済みです。基本情報、例文、例文TTS、日本語訳は初期表示に残しています。ダークモードCSSも追加済みです。

ロシア語のSourceはsection12_ru_draft01からsection12_ruへ正規化してください。draft01はテンプレートではなくSourceフィールドの値です。deck:MEMORIOPOLIS::Russianを対象に、Sourceフィールドだけを一括置換します。

本日の最初の作業は、JANUS-13 Daily Trainingの通常学習です。ModernJapaneseまたはロシア語のC0001が抽出された場合は、PC版AnkiとAnkiDroidで、画像、TTS、中央表示、ダークモード、3つのプルダウンを確認してください。抽出されない場合はカード管理のプレビューで直接確認してください。

学習時には、画像からNovelの場面、記録というConcept、近代日本語の記錄、ロシア語のзаписьへ自然に到達するかを観測します。画像内の文字、人物、帳面、都市のどれが最初に入力として働くかも記録してください。

C0001試験が成功したら、まずModernJapaneseのC0001～C0010へConcept画像を展開します。その後、RussianのC0001～C0010へ展開し、他言語は順次改修します。カード数は増やしません。

ドイツ語版をJANUS-13共通UIの基盤としますが、各プルダウン内部は言語固有プロファイルとして設計します。ASEAN系、臺灣華語、韓国語は、欧州語の形態分析をそのまま移植せず、それぞれの語根、接辞、声調、文字、音節、終声、漢字語層などを語の構造へ収めます。
```

---

## 23．2026年9月25日の店じまい地点

- JANUS-13：13言語・14観測面
- Anki：13言語デッキ開通済み
- Concept画像：C0001～C0010の10景完成
- Concept画像ZIP：作成済み
- WebP：Anki用
- PNG：GitHub保存用
- ModernJapanese：ConceptScene追加済み
- ModernJapanese C0001：画像登録・同期済み
- Russian：ConceptScene追加済み
- Russian C0001：画像登録済み
- Russian表面：正常表示
- Russian裏面：3段プルダウン化済み
- Russianダークモード：CSS追加済み
- Russian Source：`section12_ru`へ正規化する方針
- 明日：JANUS-13 Daily Trainingで実運用確認
- 抽出されない場合：カード管理プレビューで確認
- 次の画像展開：ModernJapanese C0001～C0010
- その次：Russian C0001～C0010
- 他言語：順次展開
- カード数：増やさない
- 同一Concept：全言語で同一画像を共有
- 共通UI：ドイツ語版を基盤にする
- 言語固有性：各プルダウン内部で保持する
- GitHub：正本と活動記録

本日の最終合意：

> Concept画像は、試験のために答えを隠す図ではない。人物、文字、衣食住、自然、星図、方位、象徴、儀礼的配置を含む美しい記憶風景として、Novel、Concept、語形、音声、各言語を相互に起動する入力信号である。ドイツ語版の3段プルダウンをJANUS-13共通UIの基盤とし、各言語固有の構造はプルダウン内部で保持する。
