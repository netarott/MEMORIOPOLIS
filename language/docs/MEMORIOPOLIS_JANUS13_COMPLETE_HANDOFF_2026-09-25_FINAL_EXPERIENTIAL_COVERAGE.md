# MEMORIOPOLIS / JANUS-13 完全版引き継ぎ書

更新日時：2026年9月25日 13:25 JST  
版：本当の店じまい・経験的カバー率統合版  
次回作業日：2026年9月26日

---

## 1．本書の目的

本書は、『記憶都市（メモリオポリス）』およびJANUS-13について、2026年9月25日時点の制作、Anki実装、Concept画像、カードUI、カバー率、例文、語彙選定、GitHub運用の方針を次回へ引き継ぐ完全版文書である。

本日の主要成果：

1. C0001～C0010のConcept画像10景を作成した。
2. 一枚絵を10枚へ分割し、WebP・PNGをZIP化した。
3. ModernJapaneseとRussianへConceptSceneを追加した。
4. 両言語のC0001へ同じ画像を登録した。
5. Russianの裏面を3段プルダウンUIへ改修した。
6. ドイツ語版をJANUS-13共通UIの基盤とする方針を確定した。
7. 統計的カバー率と経験的カバー率を区別した。
8. 外部コーパスを正本ではなく監査表として使う方針を確定した。
9. JANUS-13の例文をConceptの出生記録として位置づけた。

---

## 2．基本構造

正式タイトル：『記憶都市（メモリオポリス）』  
英字表記：MEMORIOPOLIS  
多言語創作・学習体系：JANUS-13

GitHubを正本とする。

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
次の読書・創作へ還流する
```

Note、YouTube、GitHub Pagesは当面の必須工程にしない。縁のある人がGitHubの記録へ到達すればよい。

---

## 3．13言語・14観測面

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
9. スペイン語（es-ES）
10. ポルトガル語（pt-BR）
11. イタリア語
12. フランス語（fr-FR）
13. ドイツ語（de-DE）

日本語だけが二つの時間面を持つため、13言語・14観測面となる。

---

## 4．最重要：日本語Novelと日本語Anki

### Novel

```text
日本語Novel
├─ 現代日本語版
└─ 近代日本語版
```

### Anki

日本語系Ankiの正は一つだけである。

```text
MEMORIOPOLIS::ModernJapanese
```

- 近代日本語表記を主表示にする。
- 同じノート内に現代日本語表記、現代読み、例文読み、字体・仮名遣い・意味・音の橋を持つ。
- 現代日本語専用の独立Ankiデッキは作成しない。

```text
作品・Concept上：13言語・14観測面
Anki上：13言語デッキ
日本語Ankiの正：MEMORIOPOLIS::ModernJapanese
```

---

## 5．Ankiデッキ

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

横断学習：`JANUS-13 Daily Training`

全13言語デッキは開通済み。

---

## 6．Core10

| ID | Concept |
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

---

## 7．Concept画像の思想

Concept画像は、学校試験のように空欄から答えを100％再生するための問題画像ではない。

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

重視するもの：

- 美しさ
- 印象の強さ
- 反復しても再訪したくなること
- 人物、視線、手の動き、物の配置
- 衣食住、自然、光、時間帯
- 八卦、星図、方位、兆候、象徴、儀礼的配置
- 漫画的な魔法ではなく、民俗学的な観測・記録・解釈

文字なしを絶対的な正としない。Concept ID、日本語見出し、短文、帳面や標識の文字が記憶風景を豊かにするなら、入力情報として許容する。

---

## 8．Concept画像10景

完成ZIP：

```text
MEMORIOPOLIS_ConceptImages_C0001-C0010_2026-09-25.zip
```

構成：

```text
README.md
manifest.csv
png/
webp/
```

対応：

```text
C0001 memoriopolis_c0001_record.webp
C0002 memoriopolis_c0002_memory.webp
C0003 memoriopolis_c0003_city.webp
C0004 memoriopolis_c0004_notification.webp
C0005 memoriopolis_c0005_reply.webp
C0006 memoriopolis_c0006_recipient.webp
C0007 memoriopolis_c0007_signature.webp
C0008 memoriopolis_c0008_verification.webp
C0009 memoriopolis_c0009_authorization.webp
C0010 memoriopolis_c0010_role.webp
```

- Anki用：WebP
- GitHub保存用：PNG
- 分割後：約248～250×625～626px
- WebP：約60～81KB／枚

同じConcept IDでは全言語が同じ画像ファイルを共有する。

---

## 9．ConceptScene共通仕様

フィールド名：`ConceptScene`

既存フィールドの末尾へ追加し、既存順序は変更しない。

表面：

```html
<div class="concept-id">{{ID}}</div>

{{#ConceptScene}}
<div class="concept-scene">
  {{ConceptScene}}
</div>
{{/ConceptScene}}
```

CSS：

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

原則：

- カード数を増やさない。
- 独立画像カードを作らない。
- 画像が空欄なら空枠を出さない。
- 画像を装飾ではなく変換の入力信号として使う。

---

## 10．ModernJapanese導入状況

- 17番目に`ConceptScene`を追加済み。
- C0001「記錄／記録」へ`memoriopolis_c0001_record.webp`を登録済み。
- 同期済み。
- 2026年9月25日のDaily Trainingでは期限対象外のため表示されなかった。
- フィールド変更・画像追加では復習期限は変化しないため、表示されないことは同期失敗を意味しない。

C0001確認成功後、C0001～C0010へ展開する。

---

## 11．Russian導入状況

- Russianノートタイプへ`ConceptScene`を追加済み。
- C0001へ同じ画像を登録済み。
- 表面は正常表示。

```text
C0001
Concept画像
запись
強勢付き語形
単語TTS
```

Concept IDがHTMLと画像内で二重に見えるが、現段階では入力情報の重複として許容し、実運用で観測する。

---

## 12．Russian UI改修

裏面を次の3段プルダウンへ改修した。

```text
▶ 語の構造
▶ 例文解説
▶ 言語間ブリッジ
```

初期表示：

- Transliteration
- 日本語
- 品詞
- ロシア語例文
- 例文TTS
- 例文日本語訳

語の構造：

- 性・数・格・語形
- 強勢付き語形
- 必要に応じて転写

例文解説：

- 強勢付き例文
- 例文転写
- 文の組み立て
- なぜこの意味・語形になるか

言語間ブリッジ：

- 現時点では`ExamplePronunciationHint`を音の橋として利用
- 日本語との接続
- 将来の専用フィールド候補：`LanguageBridge`

---

## 13．共通UI方針

ドイツ語版をJANUS-13共通UIの基盤とする。

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
- 語の構造
- 例文解説
- 言語間ブリッジ
- Source
- ダークモード
- モバイル対応

### 言語プロファイル層

- Russian：格、性、数、強勢、硬音・軟音、動詞の体
- German：語幹、接辞、複合語、性、格、語順
- Romance：語幹、接辞、性・数、活用、ラテン語系対応
- Filipino：語根、接辞、重複、焦点・ヴォイス
- Indonesian：語根、接頭辞、接尾辞、接周辞、重複
- Vietnamese：音節、声調、複合語、漢越語、類別詞
- TaiwaneseMandarin：繁体字、注音、拼音、声調、字義、量詞
- Korean：音節ブロック、語幹、語尾、助詞、終声、音韻変化、漢字語
- ModernJapanese：旧字体、歴史的仮名遣い、現代読み、四つの橋

UIの位置と操作は統一し、言語固有性はプルダウン内部で保持する。

---

## 14．Source正規化

Russian Source：

```text
section12_ru_draft01
```

を、論理的出典IDへ変更する。

```text
section12_ru
```

`draft01`はテンプレートではなくSourceフィールド値である。Russian 10件を対象にSourceフィールドだけ一括置換する。

今後、他言語も改修時に`draft01`を順次外す。

---

## 15．統計的カバー率と経験的カバー率

JANUS-13ではカバー率を一つの指標として扱わない。

### 統計的カバー率

一般コーパスに対して既知語が占める割合。

```text
大規模コーパス
  ↓
頻度語彙
  ↓
高頻度語を学ぶ
  ↓
一般文章の既知語率を高める
```

価値：

- 外部ニュースや会話を効率よく読む
- 機能語、生活語、基本動詞の欠落を見つける
- 社会一般との距離を監査する

### 経験的カバー率

篠原さんが経験し、考え、日本語で書いた内容を、対象言語の既習Conceptでどこまで認識・再構成・変換できるか。

```text
篠原さんの経験
  ↓
Novel・Essay・読書記録
  ↓
Conceptを発見
  ↓
Concept ID
  ↓
13言語・14観測面
  ↓
Ankiで変換訓練
```

JANUS-13が主として高めるのは経験的カバー率である。

---

## 16．例文はConceptの出生記録

JANUS-13の例文は、単なる文法・語義の使用例ではない。

> 例文は、そのConceptがなぜ必要になり、なぜ記憶都市に住所を与えられたのかを保存する出生記録である。

例文が保持するもの：

- 誰が何を観測したか
- 何を確認でき、何を確認できなかったか
- 存在と機能の差
- 権限を持つことと権限者として扱われることの差
- 記録があることと、その記録で説明できることの差
- 分類に見つからないことと、存在しないことの差
- Novelの出来事とConcept境界

作成順：

```text
日本語で経験・観測を書く
  ↓
Conceptを切り出す
  ↓
Concept境界を定義する
  ↓
対象言語で自然な場面へ再構成する
  ↓
なぜその日本語訳になるかを説明する
```

各言語の例文は逐語訳でなくてよいが、同じ経験的な核を共有する。

---

## 17．自己コーパスと外部コーパス

### 自己コーパス

Conceptの発生源。

- 『記憶都市』
- 現代日本語Essay
- 読書記録
- ニュースへの感想
- 実務経験
- 日々のMarkdown
- Concept選定記録
- 篠原さんが実際に使用した日本語

```text
自己コーパス ＝ Conceptの発生源
```

### 外部コーパス

欠落、偏り、世間一般との距離を確かめる監査資料。

- 頻度語彙表
- 市販教材
- 公開単語帳
- ニュース
- 書籍・会話コーパス
- 外部のNovelやEssay

```text
外部コーパス ＝ 欠落を発見する監査表
```

---

## 18．既製単語帳・大量語彙投入

市販・公開単語帳を流し込めば、技術的には1万語規模の13言語Ankiを作れる。しかし、これを中央に置かない。

避ける流れ：

```text
既製単語を大量投入
  ↓
カード数と復習負荷が増える
  ↓
Novel・Essay・読書時間が減る
  ↓
JANUS-13本来の入力源が弱くなる
```

外部語彙の推奨利用：

```text
自己コーパスからConceptを選ぶ
  ↓
配分表を確認
  ↓
外部頻度表で欠落を監査
  ↓
不足語について自分の日本語の場面を書く
  ↓
Concept境界を確認
  ↓
JANUS-13へ採用
```

外から見つけた語でも、篠原さんの日本語を一度通過すればJANUS-13の住民になれる。

採用条件：

- Novelで必要になった
- Essay・読書記録で実際に使った
- 複数回遭遇した
- 日常行動に欠かせない
- 文章骨格を読む機能語である
- 既存Concept間の関係を表す
- カバー率測定で繰り返し不足した
- 篠原さん自身が意味ある例文を書ける
- 画像・場所へ接続できる
- 14観測面で比較価値がある

---

## 19．今後測る二つのカバー率

### 外部カバー率

未知のニュース、書籍、会話などに対する既知語・既知Conceptの割合。

### 自己経験カバー率

Novel、Essay、読書記録、実務経験を対象言語でどこまで認識・再構成・変換できるか。

分解指標：

```text
Conceptカバー率
語形カバー率
構文カバー率
音声認識率
画像からの起動率
日本語からの産出率
別言語への切替率
```

JANUS-13の北極星：

> 一般語学は、社会の言語コーパスに対するカバー率を高める。JANUS-13はそれに加えて、一人の経験、思考、創作に対する変換可能率を高める。

---

## 20．1,200 Conceptの配分

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

選定経路：

```text
計画配分枠 50％
実出現枠 30％
縁・発見枠 20％
```

Core50単位で累積配分を調整する。

---

## 21．Core20暫定候補

```text
C0011 ある
C0012 する
C0013 持つ
C0014 作る
C0015 送る
C0016 受け取る
C0017 見る
C0018 確認する
C0019 ここ
C0020 誰
```

> 名詞を10個置いたら、次の10個で名詞を動かす。さらに次の10個で、時間・否定・疑問・比較を加える。

---

## 22．Daily TrainingとFSRS

第1フィルター：

```text
deck:MEMORIOPOLIS is:due
```

第2フィルター：

```text
deck:MEMORIOPOLIS is:new
```

- due上限50
- new上限10
- FSRS有効
- 目標保持率90％
- 一括再スケジュールはオフ
- 復習上限200
- 学習ステップ1m 10m
- 再学習10m

---

## 23．2026年9月26日の確認

1. JANUS-13 Daily Trainingを通常どおり実施する。
2. ModernJapaneseまたはRussianのC0001が出た場合、画像を実運用で確認する。
3. 出ない場合は期限対象外なので、カード管理のプレビューで確認する。
4. PC版・AnkiDroidで画像、TTS、中央表示、ダークモード、プルダウンを確認する。
5. Russian Sourceを`section12_ru`へ正規化する。
6. 画像から何が最初に起動したかを観測する。
7. C0001が成功したら、その他の言語へ図の対応を進める。
8. 共通UIをさらに「かっちょよく」磨く。

観測項目：

- 画像内文字
- 人物
- 帳面
- 都市
- Novelの場面
- Concept
- 近代日本語の記錄
- Russianのзапись
- Concept IDの二重表示
- スクロール量
- 反復して再訪したいか

---

## 24．Concept画像展開順

```text
ModernJapanese C0001 / Russian C0001で確認
  ↓
ModernJapanese C0001～C0010
  ↓
Russian C0001～C0010
  ↓
他言語へ順次展開
```

ユーザーの最新方針として、ロシア語またはModernJapaneseで該当箇所を確認できたら、その他の言語の図対応を進めてよい。

---

## 25．次回開始用プロンプト

```text
この引き継ぎ書を2026年9月25日の本当の最終状態として、MEMORIOPOLIS / JANUS-13を再開します。

全13言語Ankiデッキは開通済みです。日本語Novelには現代日本語版と近代日本語版がありますが、日本語系Ankiの正はMEMORIOPOLIS::ModernJapaneseのみで、現代日本語の独立Ankiデッキは作りません。

C0001～C0010のConcept画像10景は完成・分割・ZIP化済みです。ModernJapaneseとRussianにはConceptSceneを追加し、両方のC0001へmemoriopolis_c0001_record.webpを登録済みです。Russian表面は正常表示し、裏面は「語の構造」「例文解説」「言語間ブリッジ」の3段プルダウンへ改修済みです。

最初にJANUS-13 Daily Trainingを実施し、ModernJapaneseまたはRussianのC0001が出たらConcept画像を確認してください。出ない場合はカード管理のプレビューで確認してください。Russian Sourceはsection12_ru_draft01からsection12_ruへ正規化します。

ロシア語またはModernJapaneseで画像が正常に確認できたら、その他の言語へConceptSceneとC0001～C0010の共通画像を順次対応します。カード数は増やしません。同じConcept IDは同じ画像を共有します。

UIはドイツ語版を共通基盤とし、Concept画像、対象語、TTS、例文、「語の構造」「例文解説」「言語間ブリッジ」を共通配置にします。ただし、各プルダウン内部は言語固有プロファイルとして設計します。次回はUIをさらに美しく、一貫性があり、AnkiDroidのダークモードでも読みやすい形へ磨きます。

JANUS-13では統計的カバー率と経験的カバー率を区別します。一般コーパスの語彙数を増やすだけでなく、篠原さんのNovel、Essay、読書記録、実務経験を対象言語へ変換できる自己経験カバー率を主指標とします。

市販単語帳、公開語彙、頻度表は一括投入しません。外部コーパスは生活語・機能語などの欠落を発見する監査表です。外部から見つけた語も、篠原さん自身の日本語の場面と例文を経由し、Concept境界を確認してから採用します。

JANUS-13の例文は単なる文法例ではありません。そのConceptがなぜ必要になり、なぜ記憶都市に住所を与えられたのかを保存する出生記録です。大量カード生成によってNovel、Essay、読書、経験記録の時間を圧迫しないでください。
```

---

## 26．2026年9月25日の本当の店じまい地点

- JANUS-13：13言語・14観測面
- 全13言語Ankiデッキ：開通済み
- Concept画像10景：完成
- Concept画像ZIP：完成
- ModernJapanese C0001：画像登録・同期済み
- Russian C0001：画像登録済み
- Russian表面：正常表示
- Russian裏面：3段プルダウン化済み
- Russianダークモード：対応済み
- Russian Source：`section12_ru`へ正規化
- 明日：Daily Trainingまたはプレビューで画像確認
- 確認成功後：その他の言語へ画像対応
- 明日：共通UIをさらに美しくする
- 共通UI基盤：German
- 言語固有性：各プルダウン内部で保持
- 自己コーパス：Conceptの発生源
- 外部コーパス：欠落を発見する監査表
- 統計的カバー率：外部世界を読む指標
- 経験的カバー率：篠原さんの経験世界を多言語へ変換する指標
- JANUS-13の主指標：経験的カバー率
- 既製単語帳：一括投入しない
- 例文：Conceptの出生記録
- GitHub：正本と活動記録

本日の最終合意：

> Concept画像は、人物、文字、衣食住、自然、星図、方位、象徴、儀礼的配置を含む美しい記憶風景として、Novel、Concept、語形、音声、各言語を相互に起動する入力信号である。

> JANUS-13は、一般コーパスから大量の語を移植する多言語単語帳ではない。篠原さんの経験を起点に日本語の場面が生まれ、その場面からConcept、例文、画像、音声、13言語・14観測面が発生する。外部コーパスは監査表として使い、例文をConceptの出生記録として保持する。
