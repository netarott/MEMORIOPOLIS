# MEMORIOPOLIS / JANUS-13 完全版引き継ぎ書

更新日時：2026年9月24日 12:53 JST  
版：Concept画像試験開始前・完全統合版  
次回作業日：2026年9月25日

---

## 1. 本書の目的

本書は、『記憶都市（メモリオポリス）』およびJANUS-13について、2026年9月24日時点の制作、学習、Anki、Concept画像、語彙配分、読書記録、GitHub運用の全方針を、次回以降の会話へ正確に引き継ぐための文書である。

今回の最重要更新は次のとおり。

1. ドイツ語版Novel全文第一稿と18フィールド版Anki Core10が完成した。
2. JANUS-13の全13言語Ankiデッキがそろった。
3. ドイツ語カードの左寄せはCSSの `text-align: left;` が原因で、`center` へ修正済み。
4. C0001「記録」のConcept画像試作が完成した。
5. 2026年9月25日に、まず `MEMORIOPOLIS::ModernJapanese` のC0001だけで画像表示、同期、学習テストを行う。
6. 試験成功後、ModernJapaneseのC0001からC0010へConcept画像を展開する。
7. 他言語は、その後、同じConcept画像へ順次差し替える。
8. Novelの日本語系とAnkiの日本語系は構造が異なるため、本書で明確に区別する。

---

## 2. 正式名称と基本方針

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

## 3. JANUS-13の13言語・14観測面

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

日本語だけが現代日本語と近代日本語の二つの時間面を持つため、13言語・14観測面となる。

---

## 4. 最重要：日本語Novelと日本語Ankiの構造

この部分は入り組んでいるため、以後、必ず次のように区別する。

### 4.1 Novelの日本語系

Novelには、日本語の二つの本文がある。

```text
日本語Novel
├─ 現代日本語版
└─ 近代日本語版
```

- 現代日本語版：創作・意味・推敲の日本語正本
- 近代日本語版：旧字体、歴史的仮名遣いなどを観測する時間面

### 4.2 Ankiの日本語系

日本語の独立Ankiデッキは一つだけである。

```text
MEMORIOPOLIS::ModernJapanese
```

これが日本語系Ankiの唯一の正である。

- 近代日本語表記を主表示にする
- 同じノート内に現代日本語表記、現代読み、例文読み、字体・仮名遣い・意味・音の橋を持つ
- 現代日本語専用の独立Ankiデッキは作成しない
- `ModernJapanese` というデッキ名は、JANUS-13内では近代日本語版Ankiを指す

### 4.3 数え方

```text
作品・Concept上：13言語・14観測面
Anki上：13言語デッキ
日本語Ankiの正：MEMORIOPOLIS::ModernJapanese
```

この構造を今後の引き継ぎ書、カード設計、Concept画像展開で取り違えない。

---

## 5. 現在のAnkiデッキ構成

`MEMORIOPOLIS`配下に、次の13言語デッキがある。

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

ドイツ語の追加により、JANUS-13の13言語デッキがすべてそろった。

---

## 6. Core10

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

Core10は第四章第十二節の中核Conceptであり、名詞中心である。導入段階として、この名詞中心性は問題ない。

---

## 7. ドイツ語版の完成状況

基準変種：ドイツの標準ドイツ語  
Windowsロケール：de-DE  
Ankiロケール：de_DE

### デッキ・ノートタイプ

```text
デッキ：MEMORIOPOLIS::German
ノートタイプ：MEMORIOPOLIS German Vocabulary
タグ：memoriopolis::de::core10
```

### TTS

```text
{{tts de_DE:German}}
{{tts de_DE:ExampleGerman}}
```

### 完成ZIP

```text
MEMORIOPOLIS_German_Core10_draft01_18fields_2026-09-24.zip
```

### 収録ファイル

```text
section12_de_draft01.md
de_core10_master_draft01_18fields.csv
de_core10_anki_draft01_18fields.csv
README_de_core10_draft01.md
GERMAN_NOTE_TYPE_DRAFT01_18FIELDS.md
GERMAN_CARD_TEMPLATE_DRAFT01.md
section12_ja_source_for_de.md
```

### 品質検査

- German Novel：431行
- 日本語正本：437行
- Ankiデータ：10件
- Concept ID：C0001からC0010
- Master CSV：ヘッダー付き、データ10件
- Anki CSV：ヘッダーなし、データ10件
- 全行：18フィールド
- CSV：UTF-8 BOM付き
- ZIP：7ファイル
- ZIP破損検査：問題なし

### ドイツ語Core10

| ID | ドイツ語 | 日本語 | 性 |
|---|---|---|---|
| C0001 | Aufzeichnung | 記録 | 女性 |
| C0002 | Gedächtnis | 記憶 | 中性 |
| C0003 | Stadt | 都市 | 女性 |
| C0004 | Benachrichtigung | 通知 | 女性 |
| C0005 | Antwort | 返信／応答 | 女性 |
| C0006 | Empfänger | 宛先／受取人 | 男性 |
| C0007 | Signatur | 署名 | 女性 |
| C0008 | Überprüfung | 検証 | 女性 |
| C0009 | Berechtigung | 権限／許可 | 女性 |
| C0010 | Rolle | 役割／ロール | 女性 |

### CSS修正

初版テンプレートでは、次の指定により左寄せになっていた。

```css
.card {
  text-align: left;
}
```

次のように修正済み。

```css
.card {
  text-align: center;
}
```

ノートタイプ単位の修正であるため、ドイツ語カード全体へ反映済み。CSVの再インポートは不要。

---

## 8. 2026年9月24日時点のAnki統計

統計取得時刻：2026年9月24日 12:26ごろ  
状態：当日の学習開始前、ドイツ語新規10枚を含む。

### カード構成

- 合計：35枚
- 新規：10枚、28.57％
- 定着前：25枚、71.43％
- 学習中：0枚
- 再学習中：0枚
- 定着：0枚
- 休止：0枚
- 今日の学習から除外：0枚
- 現在覚えている推定数：20枚／20件のノート

### 学習実績

- 過去31日中の学習日数：11日、35.48％
- 解答回数：367回
- 期間内平均：1日12回
- 学習した日の平均：1日33回
- 追加カード：35枚
- 追加ペース：平均1日1枚

### 記憶状態

- 今後の復習予定：25回
- 明日が復習期限：0回
- 復習間隔の中央値：2日
- 安定性の中央値：1日
- 難しさの中央値：71％
- 今日思い出せる予測確率の平均：79％

### 保持率

復習間隔が1日以上のカードで、`もう一度`以外を選んだ割合：

- 昨日：0.0％、2回
- 過去1週間：46.7％、30回
- 過去1か月：54.8％、42回
- 過去1年：54.8％、42回

導入初期で定着カードが0枚、評価回数も少ないため、現時点では設定を変更しない。正答率だけでなく、Concept ID、語形、音声、意味のどこで失敗したかを観測する。

---

## 9. Daily TrainingとFSRS

### フィルター

第1フィルター：

```text
deck:MEMORIOPOLIS is:due
```

- 上限50
- 忘れている可能性が高い順

第2フィルター：

```text
deck:MEMORIOPOLIS is:new
```

- 上限10
- 追加順

### FSRS

- FSRS：有効
- 目標保持率：90％
- 一括再スケジュール：オフ
- 新規上限：10
- 復習上限：200
- 学習ステップ：1m 10m
- 再学習：10m

---

## 10. Concept IDの役割

Concept IDは翻訳語の番号ではない。異なる記憶表象が合流する共通座標である。

```text
Concept ID
  ├─ 固定された場所
  ├─ Concept画像
  ├─ Novelの出来事
  ├─ 現代日本語の説明
  ├─ 近代日本語の表現
  ├─ 各言語の語形
  ├─ 各言語の音声
  └─ 各言語固有の意味範囲
```

Concept IDは、場所法、ストーリー法、画像、音声、文字、Ankiを結ぶ都市の住所コードである。

---

## 11. 伝統的記憶術とIT

### 伝統的記憶術

- 固定地点：場所法
- Novelの出来事：ストーリー法
- 視覚像：想起の入口
- 場所と物語：抽象Conceptを具体的経験へ接続

### IT

- Anki：アクティブリコール
- FSRS：分散学習
- TTS：音声反復
- GitHub：変更履歴と正本管理
- AI：翻訳、例文、説明、比較の初稿コストを下げる
- Concept ID：多言語データを整列する

JANUS-13は、古来の記憶術をAIで置き換えるものではない。記憶術が意味の構造を作り、ITが多言語展開と反復を支える。

---

## 12. C0001 Concept画像の試作

### 対象Concept

```text
C0001：記録
```

### 試作画像のテイスト

- 正方形
- 記憶都市を見渡す机上の場面
- 古い革装丁の記録帳
- 都市の景観
- 過去・現在・未来を想起させる層
- デジタル記録と物理的記録の共存
- 暖色を基調とした写実的・幻想的表現

### 注意

現在の試作画像には英語文字が含まれている。テイスト確認と初期表示試験には使用できるが、14観測面へ正式展開する段階では、文字なし版へ差し替えるか再生成する余地がある。

正式画像では、画像内の文字に依存せず、場所、出来事、物体、光、構図からConceptを起動できることが望ましい。

---

## 13. Concept画像の推奨仕様

### 元画像

- 形式：WebPを第一候補
- 代替：PNG
- サイズ：1024 × 1024 px
- 縦横比：1:1
- カラーモード：RGB
- 目標容量：150～500 KB
- 上限目安：1 MB未満
- 透過背景：不要
- アニメーション：不要
- 画像内テキスト：原則なし

### ファイル名

ASCII小文字、数字、アンダースコアを使う。

```text
memoriopolis_c0001_record.webp
memoriopolis_c0002_memory.webp
memoriopolis_c0003_city.webp
memoriopolis_c0004_notification.webp
memoriopolis_c0005_response.webp
memoriopolis_c0006_recipient.webp
memoriopolis_c0007_signature.webp
memoriopolis_c0008_verification.webp
memoriopolis_c0009_authorization.webp
memoriopolis_c0010_role.webp
```

同一Conceptでは、全言語が同じ画像ファイルを参照する。言語別に画像を複製しない。

```text
10 Concept × 1画像 = 10画像
```

14観測面だから140画像になるわけではない。

---

## 14. Concept画像のAnki表示CSS

推奨CSS：

```css
.concept-scene img {
  display: block;
  width: 100%;
  max-width: 420px;
  max-height: 420px;
  height: auto;
  object-fit: contain;
  margin: 12px auto 16px auto;
  border-radius: 10px;
}
```

カード全体は中央揃えを維持する。

```css
.card {
  text-align: center;
}
```

画像がないカードで空領域を表示させないため、テンプレートでは条件付き表示を使う。

```html
{{#ConceptScene}}
<div class="concept-scene">
  {{ConceptScene}}
</div>
{{/ConceptScene}}
```

---

## 15. ModernJapaneseの現行16フィールド

ノートタイプ：

```text
MEMORIOPOLIS Modern Japanese Vocabulary
```

現行フィールド順：

1. ID
2. ModernJapanese
3. HistoricalReading
4. ContemporaryJapanese
5. ContemporaryReading
6. PartOfSpeech
7. ModernUsage
8. ExampleModernJapanese
9. ExampleContemporaryJapanese
10. ExampleReading
11. Source
12. CourseTags
13. GlyphBridge
14. KanaBridge
15. MeaningBridge
16. SoundBridge

TTS：

```text
{{tts ja_JP:ContemporaryReading}}
{{tts ja_JP:ExampleReading}}
```

表示は近代日本語表記だが、TTSは現代読み専用フィールドを読む。

---

## 16. 2026年9月25日のConcept画像テスト

### 試験対象

```text
デッキ：MEMORIOPOLIS::ModernJapanese
ノートタイプ：MEMORIOPOLIS Modern Japanese Vocabulary
対象ノート：C0001
近代日本語表記：記錄
現代日本語表記：記録
Concept：記録
```

### フィールド追加

現行16フィールドの末尾へ、17番目として追加する。

```text
17. ConceptScene
```

既存16フィールドの順序は変更しない。

### 試験版の状態

- C0001だけConceptSceneへ画像を登録
- C0002からC0010のConceptSceneは空欄
- カード数は増やさない
- 独立した画像カードは作らない
- 既存ノートの表面へ入力信号として画像を追加する

### 表面の推奨順

```text
Concept ID
Concept画像
近代日本語表記
現代読み
TTS
```

初回は、既存カードへ画像を追加するだけとし、産出カードは作らない。

### PC版Ankiでの確認

- 画像が中央表示される
- 縦横比が崩れない
- 画像が大きすぎない
- `記錄`と読みが正しく表示される
- 既存TTSが動作する
- カード全体が左寄せへ戻らない
- 既存の字体・仮名・意味・音の橋が表示される
- C0002からC0010には空枠が出ない

### AnkiDroidでの確認

- メディアが同期される
- 画像が欠落しない
- 中央表示される
- 横幅からはみ出さない
- Night Modeで視認できる
- TTSが画像追加後も動作する
- スクロール量が過大にならない

### 学習上の確認

- 画像から「記録」というConceptが起動するか
- `記錄`と`記録`の両方へ到達できるか
- Novelの場面を想起できるか
- 画像が答えを直接読ませるだけになっていないか
- 従来の文字のみのカードより想起が速いか
- 画像が記憶を妨げず、固定地点として機能するか

### メディア確認

テスト後、Ankiの次の機能を実行する。

```text
ツール > メディアをチェック
```

欠落ファイル、未使用ファイル、同期不適合のファイル名がないことを確認する。

---

## 17. Concept画像の展開順

この順序を必ず守る。

### 第1段階

```text
ModernJapanese C0001
```

表示、同期、TTS、学習感をテストする。

### 第2段階

テスト成功後：

```text
ModernJapanese C0001～C0010
```

C0001を正式版へ差し替える場合は、この段階で文字なし版も検討する。

### 第3段階

他言語へ順次展開する。

```text
ModernJapaneseで確立
  ↓
他言語のノートタイプへConceptSceneを追加
  ↓
各言語のC0001～C0010へ同一画像を割り当て
  ↓
各言語でTTS、画像、長い語形、モバイル表示を確認
```

他言語を一括で変更せず、言語ごとに順次差し替える。

### 重要原則

- 同じConcept IDには同じ画像
- カード数を増やさない
- 画像を答えの装飾にしない
- 画像を固定地点から言語を起動する入力信号にする
- ModernJapaneseを最初の実験場にする

---

## 18. C0001～C0010 Concept Atlasの設計項目

各Conceptについて、画像生成前に次を確定する。

```markdown
## Cxxxx Concept名

- 固定場所：
- Novel内の出来事：
- 画面の中心物：
- 人物を入れるか：
- 動き：
- 色のアンカー：
- 他Conceptと区別する要素：
- 画像に入れてはいけない要素：
- 想起したい機能：
- 推奨ファイル名：
```

10枚は別々の画像でありながら、同じ都市、同じ画風、同じ光、同じ世界観の絵巻として連続することが望ましい。

---

## 19. 活動方針

### GitHub

- 正本
- 変更履歴
- Markdownによる日々の航海日誌
- 設計判断の記録
- 縁のある人がアクセスできる静かな公開場所

### Note、YouTube、Pages

当面の必須工程ではない。

- 更新頻度を守るための制作をしない
- 閲覧数を主目的にしない
- 多言語クリエイターという肩書きを先に説明しない
- 体系と成果が育った後に必要部分を切り出せる状態を作る

---

## 20. NovelとEssay

### Novel

物語内の出来事、場所、制度、人物、Conceptを供給する。

### Essay・読書記録

ニュース、読書、日常の観測から、Novelだけでは不足しやすい次の語を供給する。

- 日常語
- 基本動詞
- 指示語
- 機能語
- 接続語
- 思考語
- 感情・評価語
- 留保表現
- 比較表現
- ニュースや社会制度の語

### 書くことがある日

```text
読書・ニュース
  ↓
現代日本語の感想
  ↓
専門語と日常語を発見
  ↓
Concept候補を選定
  ↓
JANUS-13化
```

### 特段書くことがない日

```text
既存NovelをJANUS-13化
  ↓
Ankiで学習
  ↓
気づきをMarkdownへ記録
```

---

## 21. 未知語の扱い

未知語をすべてAnkiへ入れない。

```text
未知語に遭遇
  ├─ その場で調べて終了
  ├─ 発見語としてMarkdownへ記録
  ├─ 再出現待ち
  └─ Core採用候補
```

Core採用候補への昇格基準：

- 複数回出現した
- 文意を決める重要語だった
- 日常でも使える
- NovelとEssayの両方で使える
- 14観測面で比較する価値がある
- 既存Conceptと強く結びつく
- 場所や物語として記憶できる
- 頻出するが毎回検索している

一度しか出ない高度な専門用語は、その場で調べて終えてよい。

---

## 22. 1,200 Conceptの目標

1,200 Conceptは少なくない。

```text
1,200 Concept × 14観測面
= 16,800カード相当の対応関係
```

完全に独立した16,800項目ではないが、語形、音声、意味範囲、例文、表記を長期維持するため、相当な学習量となる。

目標は、辞書なしで完全に読むことではない。

> なんとなく読める。なんとなく意味がつかめる。核心語だけ必要に応じて調べられる。

未知語が残っていてよい。文章の骨格が見えれば検索できる。検索した語が何度も戻ってくれば、そのとき都市に新しい住所を与える。

---

## 23. 読解レベル

### Level 0：不明

話題も出来事も分からない。

### Level 1：話題認識

何について書かれているか分かる。

### Level 2：骨格理解

誰が何をしたか、肯定か否定か、時間関係、原因と結果がおおよそ分かる。

### Level 3：要旨理解

辞書や検索を少し使えば、要旨を日本語で説明できる。

### Level 4：詳細理解

態度、留保、含意、細部まで説明できる。

1,200 Conceptの第一目標は、多くの一般文章をLevel 1～2で受け止め、少数の検索によってLevel 3へ進めることである。

---

## 24. 1,200 Conceptの目標配分

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

1回のCore10で厳密に一致させず、Core50、Core100、Core200などの累積単位で偏りを補正する。

---

## 25. Concept選定の三つの入口

### 50％：計画配分枠

- 基本動詞
- 機能語
- 指示語
- 時間・空間語
- 数量語
- 接続機能
- 評価・判断
- 日常生活の基礎語

### 30％：実出現枠

- Novel
- Essay
- 読書記録
- 日々のMarkdown
- GitHubの技術文書

### 20％：縁・発見枠

- 読書やニュースで発見した語
- 日本との歴史的・文化的な縁がある語
- 言語間比較で興味深い語
- 一対一翻訳が難しい語
- MEMORIOPOLIS固有Concept

Core10単位の概算：

```text
5 Concept：計画枠
3 Concept：実出現枠
2 Concept：縁・発見枠
```

---

## 26. Core20以降の原則

> 名詞を10個置いたら、次の10個で名詞を動かす。さらに次の10個で、時間・否定・疑問・比較を加える。

```text
対象を置く：名詞
対象を動かす：動詞
対象を特定する：指示語・疑問語
時間と位置を与える：時間語・空間語
関係を作る：機能語・接続語
評価する：性質・判断・感情
考えを組み立てる：原因・結果・条件・留保
```

### Core20暫定候補

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

「確認」と「検証」はConcept境界を分ける。

- 確認：状態、内容、存在を確かめる一般的行為
- 検証：証拠や手順に基づき、正しさや妥当性を調べる行為

---

## 27. 定期観測

### 14日ごと

- 各観測面の学習完了状況
- Again率
- 平均想起時間
- 音声エラー
- 例文説明が弱いカード
- 語形だけ覚えて意味構造が弱いカード
- 言語切り替え時の混同

### 28日ごと

- 未学習の短文を読む
- 辞書なしで話題と骨格を推定する
- 読解Levelを記録する
- Concept画像から対象語を出す
- 同じConceptを複数言語で切り替える
- 既習語で短文を作る
- Core50累積配分を確認する

### 3か月ごと

- 未学習の記事またはEssayを読む
- 語形カバー率を測る
- Conceptカバー率を測る
- 内容理解を日本語で記述する
- 未知Conceptを次期候補へ登録する
- Novel偏重、制度語偏重、名詞偏重を見直す
- 1,200 Concept目標に対する累積配分を補正する

---

## 28. 五年計画

```text
14観測面 × 1日1観測面
= 14日で一巡
```

一巡で各言語へ10 Conceptを追加する。

- 約28日：各言語へ約20 Concept
- 1年：240 Concept／言語
- 4年：960 Concept／言語
- 5年：1,200 Concept／言語

### 段階

1年目：240 Concept  
都市の住所体系と基本語。

2年目：480 Concept  
短文の関係構造、時間、否定、比較、日常生活。

3年目：720 Concept  
抽象語、制度語、読書・ニュース・思考語。

4年目：960 Concept  
約1,000 Conceptの都市骨格。未知文章の骨格理解を強化。

5年目：1,200 Concept  
一般文章をLevel 1～2で受け止め、検索によりLevel 3へ進む。

最後の300 Concept程度は、初期900 Conceptを運用した結果から不足領域を補う。

---

## 29. 次回開始用プロンプト

以下を次回の会話へ貼り付けて再開する。

```text
この引き継ぎ書を2026年9月24日の最新状態として、MEMORIOPOLIS / JANUS-13を再開します。

JANUS-13の全13言語Ankiデッキは開通済みです。ドイツ語版Novel全文第一稿と18フィールド版Core10も完成・導入済みです。ドイツ語カードの左寄せはCSSのtext-alignをleftからcenterへ変更して修正済みです。

日本語の構造を厳密に区別してください。Novelには現代日本語版と近代日本語版の二面があります。一方、日本語系Ankiの正は近代日本語版であるMEMORIOPOLIS::ModernJapaneseのみです。現代日本語の独立Ankiデッキは作成しません。ModernJapaneseの同一ノート内に、近代日本語表記、現代日本語表記、現代読み、四つの橋を保持します。

本日の作業は、Concept画像の初期実験です。まずMEMORIOPOLIS::ModernJapaneseのC0001「記錄／記録」だけで試験します。現行ノートタイプは16フィールドです。既存フィールドの末尾へ17番目のConceptSceneを追加します。C0001だけConceptSceneへ画像を登録し、C0002からC0010は空欄にします。カード数は増やしません。

表面テンプレートでは、ConceptSceneを条件付き表示にしてください。画像は中央表示、最大幅・高さ420px、縦横比維持、object-fit: containとします。カード全体のtext-align: centerを維持します。

C0001で、Windows版Anki、AnkiDroid、メディア同期、TTS、中央表示、Night Mode、スクロール量、画像から記錄／記録とNovelの場面が起動するかを確認します。試験後、ツール > メディアをチェックを実行します。

C0001の試験が成功したら、ModernJapaneseのC0001からC0010までConcept画像を展開します。その後、他言語へ同じConcept画像を順次差し替えます。他言語を一括変更せず、言語ごとに確認します。同じConcept IDには同じ画像ファイルを使用し、言語別に画像を複製しません。

現在のC0001試作画像はテイスト確認用として良好ですが、英語文字が含まれています。正式な全言語展開前に、文字なし画像へ差し替えるかを検討してください。正式画像は1024×1024px、正方形、WebP、RGB、原則文字なし、目標150～500KB、上限1MB未満を基準にします。

Concept画像の役割は装飾ではありません。Concept ID、固定場所、Novelの出来事、対象言語の語形、音声を結び、固定地点から対象言語を起動する入力信号として使用します。

GitHubを正本、Markdownを活動記録、Novelと現代日本語Essayを入力源、Concept IDを共通座標、Ankiを変換訓練装置とします。Note、YouTube、Pagesは当面の必須工程ではありません。

Core20以降は1,200 Concept全体の配分を管理します。Concept選定は計画配分枠50％、実出現枠30％、縁・発見枠20％を基本にし、Core50単位で累積配分を確認します。未知語はすべてAnkiへ入れず、その場で調べて終了、Markdownへ記録、再出現待ち、Core採用候補の四段階で扱います。
```

---

## 30. 2026年9月24日の店じまい地点

- JANUS-13：13言語・14観測面
- Anki：13言語デッキ開通済み
- ドイツ語Novel：完成
- ドイツ語Core10：完成・導入済み
- ドイツ語CSS：中央揃えへ修正済み
- 日本語Novel：現代日本語版と近代日本語版の二面
- 日本語Ankiの正：`MEMORIOPOLIS::ModernJapanese`のみ
- 現代日本語の独立Ankiデッキ：作成しない
- C0001 Concept画像：試作済み
- 次回：ModernJapanese C0001でConceptScene試験
- 現行ModernJapanese：16フィールド
- 試験版ModernJapanese：17番目にConceptSceneを追加
- C0001成功後：ModernJapanese C0001～C0010へ展開
- その後：他言語へ順次展開
- 同一Concept：全言語で同一画像を共有
- カード数：増やさない
- GitHub：正本と活動記録
- 日常の入力：読書記録、ニュース感想、現代日本語Essay
- 書くことがない日：NovelのJANUS-13化
- 1,200 Concept：五年計画
- Core20以降：配分管理

本日の最終合意：

> Novelの日本語系は現代日本語版と近代日本語版の二面を持つ。一方、Ankiの日本語系は近代日本語版であるMEMORIOPOLIS::ModernJapaneseのみを正とし、現代日本語の独立Ankiデッキは作成しない。Concept画像は、まずModernJapaneseのC0001で試験し、成功後にC0001～C0010へ展開する。その後、他言語へ順次適用する。
