# MEMORIOPOLIS / JANUS-18 完全版引き継ぎ書

**作成日:** 2026-10-07  
**対象:** E0002日本語・英語正本、English Core30、Italian Core20音源、Essay別フォルダー対応音声生成、JANUS-18 Audio Circle  
**次回予定:** Spanish Core20、臺灣華語 Core30

---

## 1. 本日の到達点

本日は、E0002を起点として、Essay、Anki、長文音声、YouTube Musicの運用を一つの循環へ接続した。

```text
E0002_ja.md canonical
        ↓
E0002_en.md canonical
        ↓
EnglishカードUI刷新
        ↓
English Core30 C0021-C0030
        ↓
E0002_en.mp3
        ↓
MEMORIOPOLIS | JANUS-18 Audio Circle
```

同時に、前段で完成していたItalian Core20に対応する`E0001_it.mp3`も生成し、YouTube Musicへのアップロードを完了した。

本日の重要な設計変更は、音声プレイリストをEssayごとに分けず、すべてのEssayと言語を一つの横断プレイリストへ集約する方針を確定したことである。

---

## 2. E0002日本語版

### 2.1 ファイル

```text
essay/E0002/E0002_ja.md
```

### 2.2 状態

```yaml
essay_id: E0002
language: ja
status: canonical
```

### 2.3 タイトル

```text
もう一本の線路
```

### 2.4 中心命題

男女が同じ盤上で競争できるようになっても、その盤面がケアを担わない人間を前提としているなら、社会はまだ十分には変わっていない。

### 2.5 主題

- 結婚
- 子育て
- ケア
- 労働
- 引き継ぎ
- 復帰経路
- 競争の盤面
- 性別役割
- 消費空間
- 観察対象を断定的に評価しない姿勢

### 2.6 結末の比喩

```text
電車は有楽町線を走っていた。
しかし、私が見ていたのは、競争とケアの間に敷かれた、もう一本の線路だった。
```

---

## 3. E0002英語版

### 3.1 ファイル

```text
essay/E0002/E0002_en.md
```

### 3.2 状態

```yaml
essay_id: E0002
language: en
status: canonical
```

ファイル末尾も次の表記へ統一済みであり、`draft`表記は残していない。

```text
English canonical version.
```

### 3.3 英語タイトル

```text
Another Track
```

### 3.4 翻訳方針

- 逐語訳ではなく、日本語正本と骨子・中心命題を一致させる
- 英語話者がEssayとして自然に読める段落運動を優先する
- 観察対象の人物像を断定しない
- 個人批判ではなく、制度、労働、ケア、競争の構造へ焦点を置く
- 日本語正本の線路、盤面、社会OSの比喩を維持する

### 3.5 主要表現

```text
It takes about twenty years to raise one human being.
```

```text
Installing the social operating system takes a long time.
```

```text
There are more pieces to choose from now.
But the rules of the board may still be old.
```

```text
The train was running on the Yurakucho Line.
But what I was looking at was another track, laid between competition and care.
```

### 3.6 okama barの処理

車内で実際に使われた語を引用として保持し、英語圏の読者向けに脚注を付けた。

本文:

```markdown
“Money is there to be spent. Let's go to an *okama* bar next time.”[^okama]
```

脚注:

```markdown
[^okama]: *Okama bar* is a Japanese nightlife term without a precise English equivalent. Here it refers broadly to a venue where gender-nonconforming performance and conversation may form part of the entertainment. The word *okama* can be derogatory when applied to a person, although some performers and venues use it as a self-description.
```

MP3生成時には、本文中の`okama bar`は読み上げるが、脚注定義は読み上げない。

---

## 4. EnglishカードUIの刷新

### 4.1 UIファイル

```text
ENGLISH_CARD_UI_17FIELDS_AUDIO_FIRST_CONCEPTSCENE_3PANELS_2026-10-07.md
```

### 4.2 更新理由

旧英語UIは2026-09-26版で、17フィールドと3段パネルには対応していたが、現在の音優先型ではなかった。

旧順序:

```text
ID
↓
ConceptScene
↓
English
↓
IPA
↓
単語TTS
```

更新後:

```text
単語の音
↓
心の中でConcept候補を探す
↓
ConceptScene
↓
英語の綴り
↓
IPA
↓
日本語Concept
↓
例文の音
↓
例文と日本語訳
↓
3段パネル
```

### 4.3 正式17フィールド

```text
01 ID
02 English
03 IPA
04 Japanese
05 PartOfSpeech
06 EnglishGrammar
07 ExampleEnglish
08 ExampleIPA
09 ExampleJapanese
10 Source
11 CourseTags
12 ExampleBreakdown
13 ExampleExplanation
14 ExamplePronunciationHint
15 UsageNote
16 ConceptContrast
17 ConceptScene
```

### 4.4 UIの特徴

- `LISTEN FIRST`の単語音声ゲート
- ConceptSceneを共通の記憶住所として表示
- 英語見出し語とIPAを音声確認後に表示
- 例文側にも`LISTEN TO THE SENTENCE`を配置
- `id="answer"`による回答開始位置への移動
- Anki DesktopとAnkiDroidに対応
- ライトモード、ダークモード対応
- 長い句動詞と例文の折り返し対応
- 英語用のネイビー、ブルー、赤、金の配色

### 4.5 裏面の3段パネル

```text
1. WORD STRUCTURE
2. SENTENCE GUIDE
3. CONCEPT BRIDGE
```

### 4.6 TTS

```html
{{tts en_US:English}}
{{tts en_US:ExampleEnglish}}
```

---

## 5. English Core30

### 5.1 完了状態

English Core30、C0021からC0030までをAnkiへ登録済み。

```text
C0021 marry      結婚する
C0022 raise      育てる
C0023 work       働く
C0024 hand over  引き継ぐ／引き渡す
C0025 return     戻る
C0026 protect    守る／保護する
C0027 balance    両立させる／釣り合わせる
C0028 compete    競争する
C0029 perform    演じる／遂行する
C0030 evaluate   評価する
```

### 5.2 Core30ファイル

```text
en_core30_master_17fields.csv
en_core30_anki_17fields.csv
README_EN_CORE30_17FIELDS.md
MEMORIOPOLIS_English_E0002_Core30_17fields_2026-10-07.zip
```

### 5.3 共通設定

```text
Source: E0002_en.md
CourseTags: memoriopolis::en::core30
TTS locale: en_US
Note type: MEMORIOPOLIS English Vocabulary
Field count: 17
```

### 5.4 Concept境界

```text
marry / be married / get married / marriage
raise / bring up / rear / rise
work / job / labor / care work
hand over / take over / delegate / pass on
return / go back / come back / resume
balance / reconcile / juggle / combine
compete / contest / struggle / cooperate
perform / act / play a role / pretend
evaluate / assess / judge / criticize
```

### 5.5 特に重要な境界

C0030は、人物を断定的に「裁く」方向へ寄せず、基準に照らして検討する`evaluate`を採用した。

```text
evaluate = 基準に照らして検討する
assess   = 状態や程度を見積もる
judge    = 判断する。文脈によって人物批評の含みが強くなる
```

### 5.6 ConceptScene名

```text
C0021 memoriopolis_c0021_marry.webp
C0022 memoriopolis_c0022_raise.webp
C0023 memoriopolis_c0023_work.webp
C0024 memoriopolis_c0024_hand_over.webp
C0025 memoriopolis_c0025_return.webp
C0026 memoriopolis_c0026_protect.webp
C0027 memoriopolis_c0027_balance.webp
C0028 memoriopolis_c0028_compete.webp
C0029 memoriopolis_c0029_perform.webp
C0030 memoriopolis_c0030_evaluate.webp
```

### 5.7 実機確認項目

後日、Anki DesktopおよびAnkiDroidで次を確認する。

- C0021からC0030のConceptScene
- 単語TTSが最初に再生されるか
- `hand over`のTTS
- IPAと見出し語の配置
- 例文TTS
- 回答位置への自動スクロール
- 3段パネル
- ダークモード
- C0030の長い例文の折り返し

---

## 6. Ankiの日次上限

English Core30の10枚とItalian Core20の10枚を同日に出すため、親デッキの日次新規上限を20枚へ変更した。

```text
JANUS-13 Daily Training
新規: 20
```

当日の新規内訳:

```text
English Core30: 10枚
Italian Core20: 10枚
合計: 20枚
```

親デッキ側に新規20枚が集約され、子デッキ側が0と表示される場合があるが、カードが消えたわけではない。

今後、新しい2言語を同日に10枚ずつ追加する場合も、親側の新規上限20枚を基本とする。ただし、既存の復習負荷を見ながら調整する。

---

## 7. Italian Core20音源

### 7.1 入力

```text
essay/E0001/E0001_it.md
```

### 7.2 出力

```text
essay/E0001/audio_E0001_all/E0001_it.mp3
```

付随ファイル:

```text
E0001_it.srt
E0001_it.narration.txt
E0001_it.audio.json
```

### 7.3 音声設定

```text
locale: it-IT
voice: it-IT-ElsaNeural
rate: -6%
```

### 7.4 状態

- MP3生成成功
- YouTube Musicへのアップロード完了
- JANUS-18 Audio Circleへ追加済み

---

## 8. E0002英語音源

### 8.1 入力

```text
essay/E0002/E0002_en.md
```

### 8.2 出力

```text
essay/E0002/audio_E0002_all/E0002_en.mp3
```

付随ファイル:

```text
E0002_en.srt
E0002_en.narration.txt
E0002_en.audio.json
```

### 8.3 音声設定

```text
locale: en-US
voice: en-US-AndrewNeural
rate: -6%
```

### 8.4 生成履歴

初回はEdge TTSへの接続中に一時的なネットワーク切断が発生した。

```text
speech.platform.bing.com:443
WinError 1231
WinError 1236
```

入力Markdownやcanonical設定の問題ではなく、通信途中の切断だった。

再試行対応版に差し替えた後、正常生成した。

```text
[OK] E0002\E0002_en.md
-> E0002\audio_E0002_all\E0002_en.mp3
locale=en-US voice=en-US-AndrewNeural rate=-6%
```

### 8.5 試聴確認項目

- Andrew Neural、速度-6%の自然さ
- `Yurakucho Line`
- `Ginza-itchome Station`
- `okama bar`
- 制度設計部分の速度
- `There are more pieces to choose from now.`の抑揚
- 結末`another track, laid between competition and care`の着地

---

## 9. Essay別フォルダー対応の音声生成スクリプト

### 9.1 正式スクリプト

```text
essay/memoriopolis_essay_audio_batch.py
essay/run_memoriopolis_essay_audio.ps1
```

### 9.2 フォルダー構成

```text
MEMORIOPOLIS/
└─ essay/
   ├─ E0001/
   │  ├─ E0001_ja.md
   │  ├─ E0001_en.md
   │  ├─ E0001_it.md
   │  └─ audio_E0001_all/
   ├─ E0002/
   │  ├─ E0002_ja.md
   │  ├─ E0002_en.md
   │  └─ audio_E0002_all/
   ├─ memoriopolis_essay_audio_batch.py
   └─ run_memoriopolis_essay_audio.ps1
```

### 9.3 正確なジョブ指定

旧版の次の指定は使わない。

```powershell
--essay E0001 --essay E0002 --language it --language en
```

この指定ではEssayと言語の組合せが展開され、不要な`E0001_en.md`も候補になる。

正式版では、Essayと言語をペアで指定する。

```powershell
--job E0001:it
--job E0002:en
```

### 9.4 実行

```powershell
py .\memoriopolis_essay_audio_batch.py `
  --root . `
  --job E0001:it `
  --job E0002:en `
  --continue-on-error
```

英語だけ:

```powershell
py .\memoriopolis_essay_audio_batch.py `
  --root . `
  --job E0002:en
```

上書き:

```powershell
py .\memoriopolis_essay_audio_batch.py `
  --root . `
  --job E0001:it `
  --job E0002:en `
  --overwrite `
  --continue-on-error
```

### 9.5 安全策

- Essayフォルダー名、ファイル名、`essay_id`を照合
- `status: canonical`以外は拒否
- 実行時にEdge TTS音声一覧を確認
- 優先Voiceがなければ同一ロケール内で代替
- 既存MP3は`--overwrite`なしでは再生成しない
- 一時ファイル生成後に完成ファイルへ置換
- 接続切断時に最大4回、自動再試行
- `Production Notes`、`制作ノート`以降を除外
- 脚注定義、URL、コードブロックを除外
- `essay/MEMORIOPOLIS_essay_audio_manifest.json`へ結果を記録

### 9.6 1 Markdown = 1 MP3

この原則を維持する。

```text
E0001_it.md -> E0001_it.mp3
E0002_en.md -> E0002_en.mp3
```

Ankiカードの単語・例文TTSと、Essay全体の長文MP3は役割が異なる。

```text
Anki
→ 短い音、綴り、ConceptScene、例文

Essay MP3
→ 長文、談話展開、経験、文脈予測
```

---

## 10. YouTube Musicの運用変更

### 10.1 Essay別プレイリストを廃止

Essayごとにプレイリストを作る運用は採用しない。

理由:

- E0100まで進むとプレイリスト管理自体が仕事になる
- 再生前にEssay内容が分かり、音からEssayを特定する訓練が弱くなる
- ファイル名にEssay IDと言語コードが残るため、別途分類を重ねる必要がない
- 日常トレーニングではEssayと言語を横断したランダム再生が有効

### 10.2 正式プレイリスト名

```text
MEMORIOPOLIS | JANUS-18 Audio Circle
```

E0001限定表記を外し、E0002以降も同一プレイリストへ追加できる状態にした。

### 10.3 最終説明文

```text
『記憶都市（メモリオポリス）』の多言語ナレーション。

複数言語でランダム再生し、
音、リズム、Concept、記憶の経路を反復するためのJANUS-18音声環。

Source: canonical multilingual editions
https://github.com/netarott/MEMORIOPOLIS
```

### 10.4 プライバシー

```text
非公開
```

### 10.5 音声環の目的

横断シャッフルでは、再生開始後に次を音から予測する。

```text
何語か
↓
どのEssayか
↓
どの経験・Conceptか
↓
文章のどの位置か
↓
次に何が語られるか
```

認識対象を次へ広げる。

```text
言語
↓
言語 × Essay × Concept × 経験 × 談話位置
```

### 10.6 ファイル名を索引として使う

```text
E0001_it.mp3
E0001_de.mp3
E0002_en.mp3
```

曲名だけで次を識別できる。

- Essay ID
- 言語コード
- 音源形式

---

## 11. 本日時点のAudio Circle

E0001の既存多言語音源に、E0001イタリア語とE0002英語を加えた。

代表的な音源:

```text
E0001_ja.mp3
E0001_en.mp3
E0001_zh-Hant-TW.mp3
E0001_ko.mp3
E0001_ru.mp3
E0001_fil.mp3
E0001_id.mp3
E0001_vi.mp3
E0001_fr.mp3
E0001_de.mp3
E0001_it.mp3
E0002_en.mp3
```

今後もEssay IDにかかわらず、canonical Markdownから生成した音源を同じAudio Circleへ追加する。

---

## 12. GitHubを正本とする運用

正本の保存先はGitHubである。

```text
https://github.com/netarott/MEMORIOPOLIS
```

音声生成はGitHub上のcanonical Markdownを入力とする。

```text
GitHub canonical Markdown
↓
Edge TTS
↓
Essay別 audio_E####_all
↓
YouTube Musicへアップロード
↓
JANUS-18 Audio Circle
```

YouTube Musicは正本ではなく、反復聴取のための再生環境である。

---

## 13. 明日の予定

明日、2026-10-08は次の二本立てで進める。

```text
Core20側: スペイン語 es-ES
Core30側: 臺灣華語 zh-Hant-TW
```

---

## 14. Spanish Core20の制作順

スペイン語は、確定済みの方針どおりスペイン本国のスペイン語`es-ES`を基準にする。

### 14.1 制作順

```text
1. Spanish Core10の実フィールドマスター確認
2. ConceptSceneフィールドが末尾に存在するか確認
3. SpanishカードUIの現状確認
4. 必要なら音優先・ConceptScene・3段パネル版へ更新
5. E0001_es.mdを作成
6. 内容確認後にstatus: canonicalへ確定
7. Spanish Core20 C0011-C0020を作成
8. master CSVとAnki CSVを作成
9. Ankiへインポート
10. E0001_es.mp3を生成
11. JANUS-18 Audio Circleへ追加
```

### 14.2 Core20共通Concept

```text
C0011 ある／存在する
C0012 する／作る
C0013 持つ
C0014 送る
C0015 受け取る
C0016 聞く／耳に入る
C0017 調べる／探す
C0018 移る／変える
C0019 結びつく／接続する
C0020 縛られる／結び付けられている
```

### 14.3 重要な境界

- C0016は、意識的に傾聴するだけでなく、未知語が偶然耳に入るConcept
- C0017は、意味や答えを探す過程と、資料で特定項目を引く行為を区別
- C0018は、単なる身体移動ではなく、場所・状態・接続先を別のものへ変えるConcept
- C0019は接続を作る側
- C0020は接続・拘束された状態

### 14.4 ファイル識別子

候補:

```text
E0001_es.md
es_core20_master_19fields.csv
es_core20_anki_19fields.csv
```

実フィールド数はSpanish Core10のマスター確認後に確定する。既存フィールド名へ完全一致させ、推測で新規フィールド名を作らない。

---

## 15. 臺灣華語 Core30の制作順

言語・ファイル識別子は次へ統一する。

```text
zh-Hant-TW
```

### 15.1 制作順

```text
1. 臺灣華語Core10/Core20の実フィールドマスター確認
2. 現在のカードUIが音優先型か確認
3. ConceptSceneと3段パネルの状態確認
4. 必要ならカードUIを最新版へ更新
5. E0002_zh-Hant-TW.mdを作成
6. 内容確認後にstatus: canonicalへ確定
7. 臺灣華語Core30 C0021-C0030を作成
8. master CSVとAnki CSVを作成
9. Ankiへインポート
10. E0002_zh-Hant-TW.mp3を生成
11. JANUS-18 Audio Circleへ追加
```

### 15.2 Core30共通Concept

```text
C0021 結婚する
C0022 育てる
C0023 働く
C0024 引き継ぐ
C0025 戻る
C0026 守る
C0027 両立する
C0028 競争する
C0029 演じる
C0030 評価する
```

### 15.3 翻訳方針

- 英語Core30の見出し語を機械的に訳さない
- 日本語正本`E0002_ja.md`のConceptを基準にする
- `E0002_zh-Hant-TW.md`で自然に現れる語を優先する
- 臺灣で自然な繁體字、語彙、語調を採用する
- 中国大陸向け簡体字や用語へ寄せない
- `zh-Hant-TW`を全ファイル、メタデータ、CourseTagsで維持する

### 15.4 特に検討するConcept境界

```text
結婚する
→ 結婚という行為、婚姻状態、制度としての結婚を区別

育てる
→ 養育、教育、成長を支えることを区別

引き継ぐ
→ 仕事を渡す側、受け取る側、継承することを区別

戻る
→ 場所へ戻る、職場復帰、活動再開を区別

両立する
→ 常時五対五ではなく、時期によって配分が変わるConcept

演じる
→ 舞台上の演技、社会的役割の遂行、事実でないふりを区別

評価する
→ 分析的評価と、人物を裁く判断を区別
```

---

## 16. 明日の音声生成への追加

Spanish E0001と臺灣華語E0002がcanonicalになった後、正式バッチスクリプトへ次のジョブを渡す。

```powershell
py .\memoriopolis_essay_audio_batch.py `
  --root . `
  --job E0001:es `
  --job E0002:zh-Hant-TW `
  --continue-on-error
```

ただし、現在のバッチスクリプト内にスペイン語Voice設定がまだない場合は、先に`VOICE_CONFIGS`へ`es`を追加する。

候補設定:

```text
Spanish
locale: es-ES
voice: 実行時のEdge TTS音声一覧を確認して確定
rate: 初回は-6%前後から試聴
```

臺灣華語は既存設定を使用する。

```text
locale: zh-TW
voice: zh-TW-HsiaoChenNeural
rate: -8%
```

スペイン語Voiceは、実際の音声一覧と試聴後に正式決定し、推測のみで固定しない。

---

## 17. 次回開始時に最初に確認するもの

### 17.1 Spanish

アップロードまたは確認対象:

```text
Spanish Core10 master CSV
Spanish Core10 Anki CSV
既存SpanishカードUI
ConceptSceneフィールドの実名と順序
```

### 17.2 臺灣華語

アップロードまたは確認対象:

```text
zh-Hant-TW Core10/Core20 master CSV
zh-Hant-TWの既存カードUI
既存フィールド順
ConceptSceneフィールド
E0002_ja.md
E0002_en.md
```

既存の実フィールド名を確認してからUIとCSVを作る。フィールド名の推定や、他言語仕様の機械的な流用は行わない。

---

## 18. 現在の設計原則

### 18.1 正本

```text
GitHub上のcanonical Markdownが正本
```

### 18.2 Essay

```text
経験単位 = Essay ID
1 Markdown = 1 MP3
```

### 18.3 Anki

```text
Concept ID = 記憶都市の住所
音 → ConceptScene → 綴り → 日本語Concept → 例文 → 解説
```

### 18.4 Audio Circle

```text
Essayと言語を横断
ランダム再生
音から言語、Essay、Concept、経験、談話位置を予測
```

### 18.5 ConceptScene

```text
言語ごとに別画像を作らず、同じConcept IDでは同じ画像を共有
```

### 18.6 日本語系Anki

```text
日本語系Ankiの正はMEMORIOPOLIS::ModernJapaneseのみ
現代日本語の独立Ankiデッキは作成しない
```

### 18.7 言語基準

```text
Spanish: es-ES
Portuguese: pt-BR
Taiwanese Mandarin: zh-Hant-TW
```

---

## 19. 本日の完了事項チェックリスト

```text
[x] E0002_ja.md canonical
[x] E0002_en.md canonical
[x] 英語版のokama bar脚注
[x] 英語カードUIを音優先型へ刷新
[x] English Core30 C0021-C0030作成
[x] English Core30をAnkiへ登録
[x] Anki新規上限を20枚へ変更
[x] E0001_it.mp3生成
[x] E0001_it.mp3をYouTube Musicへアップロード
[x] E0002_en.mp3生成
[x] Essay別フォルダー対応バッチスクリプト作成
[x] Essayと言語の正確な--job指定へ修正
[x] Edge TTS接続切断時の再試行を追加
[x] Essay別プレイリスト方針を廃止
[x] 横断Audio Circleへ統合
[x] プレイリスト名をMEMORIOPOLIS | JANUS-18 Audio Circleへ変更
[x] Source表記をcanonical multilingual editionsへ変更
[x] GitHub URLを説明へ追加
```

---

## 20. 未確認・次回以降の確認事項

```text
[ ] English Core30のAnki Desktop表示確認
[ ] English Core30のAnkiDroid表示確認
[ ] hand overの単語TTS確認
[ ] C0030の長文折り返し確認
[ ] English UIのダークモード確認
[ ] E0002_en.mp3のスマートフォン再生確認
[ ] E0002_en.mp3のAudio Circle追加状態確認
[ ] Spanish Core10実フィールド確認
[ ] Spanish UI更新
[ ] E0001_es.md作成とcanonical化
[ ] Spanish Core20作成
[ ] zh-Hant-TW実フィールド確認
[ ] E0002_zh-Hant-TW.md作成とcanonical化
[ ] 臺灣華語Core30作成
```

---

## 21. 次回開始用プロンプト

```text
前回の引き継ぎに従い、今日は二本立てで進めます。

Core20側はスペイン語es-ESです。
まずSpanish Core10の実フィールドマスターと既存UIを確認し、ConceptSceneを末尾フィールドとして維持した音優先型UIを整えます。その後、E0001_es.mdを自然なスペイン語で作成し、canonical確認後にC0011-C0020のSpanish Core20を作成してください。

Core30側は臺灣華語zh-Hant-TWです。
既存フィールドマスターとUIを確認した後、E0002_ja.mdの骨子を基準にE0002_zh-Hant-TW.mdを自然な臺灣華語で作成します。canonical確認後、C0021-C0030の臺灣華語Core30を作成してください。

既存の実フィールド名へ完全一致させ、他言語のフィールド名を推測で流用しないでください。カードの順序は音、ConceptScene、綴り、日本語Concept、例文、3段パネルです。音源はEssay別フォルダーに出力し、YouTube MusicではMEMORIOPOLIS | JANUS-18 Audio Circleへ集約します。
```

---

## 22. 一行サマリー

> E0002を日本語と英語で正本化し、English Core30と長文MP3へ接続したことで、JANUS-18 Audio Circleは言語だけでなく、Essayと経験を横断して音から記憶の住所を探す環へ移行した。
