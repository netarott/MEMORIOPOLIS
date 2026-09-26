# MEMORIOPOLIS 多言語小説読解コース 完全版引き継ぎ書

- 更新日：2026年9月8日
- 対象リポジトリ：`MEMORIOPOLIS`
- 対象企画：『記憶都市（メモリオポリス）』多言語小説読解コース
- 現在の起点：第4章「翻訳者」第12節「受信人のない回信」
- 現在の実装言語：韓国語
- 現在の到達点：韓国語Core 10、例文解説、TTS、Windows版Anki、AnkiWeb、AnkiDroidの連携確認済み

---

## 1. 企画の目的

『記憶都市（メモリオポリス）』を、読者が日本語以外の言語でも読めるようになるための専用読解コースを構築する。

一般的な語学教材の順序をそのまま採用するのではなく、読者がすでに物語や概念を知っている強みを生かし、作品本文から語彙、文法、発音、例文を回収する。

```text
小説本文
  ↓
作品内の概念
  ↓
語彙と発音
  ↓
例文
  ↓
文の組み立て
  ↓
なぜその訳になるのかという解説
  ↓
Ankiによる反復学習
  ↓
原文読解
```

このコースは単なる単語帳ではなく、第4章「翻訳者」の読者が、作中で起きている翻訳を自ら追体験するスピンオフ作品として位置づける。

---

## 2. この教材が埋める学習上の空白

一般的な初級教材には、次の情報が用意されていることが多い。

- 単語
- 読み方
- 音声
- 例文
- 日本語訳

しかし、初学者が本当に立ち止まりやすいのは、次の区間である。

```text
単語の意味は分かる
  ↓
例文も日本語訳も見える
  ↓
しかし、なぜその韓国語がその日本語訳になるのか分からない
```

この説明されていない区間を自力で埋めるには、多くの時間、複数の文法書、検索力、試行錯誤への余裕が必要になる。結果として、人生の大きな時間を投資できる人だけが初級と中級の間を越えやすい構造が生まれる。

『記憶都市読解コース』では、この区間を次の二つのフィールドで明示的に橋渡しする。

### `ExampleBreakdown`

例文を意味のまとまりに分け、日本語との対応を見せる。

```text
도시의 ＝ 都市の
기록을 ＝ 記録を
확인했다 ＝ 確認した
```

### `ExampleExplanation`

助詞、語尾、辞書形と例文中の形、直訳と自然訳の関係を、初学者にも理解できる言葉で説明する。

```text
도시의は「都市の」という意味です。의は、日本語の「の」に近い働きをします。
기록을の을は「を」に近く、確認する対象が기록であることを示します。
확인했다は「確認する」という意味の확인하다が過去形になった形です。
文全体をつなぐと、「都市の記録を確認した」となります。
```

この二つのフィールドは補足情報ではなく、本コースの中核機能とする。

---

## 3. 例文解説の執筆原則

### 3.1 基本構造

各例文解説は、原則として次の順序で書く。

1. 文を2から4個程度の意味のまとまりに分ける
2. 助詞や語尾が、この文で何をしているか説明する
3. 動詞や形容詞の辞書形と、例文中の形をつなぐ
4. 必要に応じて、直訳と自然な日本語訳の差を説明する
5. 最後に文全体の訳へ戻る

### 3.2 文体

- 専門用語の羅列を避ける
- 正確さを失わない範囲で、日常的な日本語を使う
- 「日本語と同じ」と断定せず、「近い働き」「この文では」と説明する
- 一度読んで文の組み立てが腹落ちする長さを目指す
- 単なる逐語訳で終わらせない
- 必要以上に長い文法講義にしない

### 3.3 初出と再登場

同じ文法を毎回同じ長さで説明しない。

```text
初出
丁寧に説明する

再登場
以前の説明とのつながりを示す

定着後
分解表示を中心にし、説明を短くする
```

例：目的語を示す`을/를`

```text
初出：
을は、日本語の「を」に近く、動作の対象を示します。

再登場：
경로를の를は、前に学んだ을と同じ働きです。
前の語にパッチムがないため、ここでは를になります。

定着後：
경로를 ＝ 経路を
```

---

## 4. 五言語展開の基本設計

最終成果物は五言語対照とし、学習コースは言語別にする。

対象言語は次の五つ。

1. 日本語
2. English
3. 한국어
4. 臺灣繁體中文
5. Русский

### 4.1 概念中心の設計

単語帳の中心は個別言語ではなく、言語に依存しないConcept IDとする。

```text
C0001 Record
C0002 Memory
C0003 City
C0004 Notification
...
```

各言語は同じConcept IDへぶら下げる。

```text
C0009 Authority

日本語：権限
English：authority
한국어：권한
臺灣繁體中文：權限
Русский：полномочие
```

言語ごとに別のConcept IDを作らない。

### 4.2 最終成果物と学習導線

```text
概念辞典
五言語を同じ概念IDで管理

学習コース
韓国語、ロシア語、臺灣華語、英語を別々のAnkiデッキで提供
```

---

## 5. 臺灣華語版の確定方針

臺灣華語版では、拼音と注音符号を両方とも残す。

標準構成は次のとおり。

```text
繁體字
声調記号付き漢語拼音
声調付き注音符号
日本語
品詞
作中例文
例文の拼音
例文の注音
例文の日本語訳
臺灣華語TTS
例文の組み立て
初学者向け例文解説
出典
```

表面では原則として繁體字のみを見せ、拼音と注音は解答面に表示する。

例：

```text
權限

quánxiàn

ㄑㄩㄢˊ ㄒㄧㄢˋ

権限
```

想定フィールド：

```text
ID
TraditionalChinese
Pinyin
Bopomofo
Japanese
PartOfSpeech
ExampleTraditionalChinese
ExamplePinyin
ExampleBopomofo
ExampleJapanese
ExampleBreakdown
ExampleExplanation
Source
Tags
```

TTSは臺灣華語向けの`zh_TW`を使用する。

```html
{{tts zh_TW:TraditionalChinese}}
{{tts zh_TW:ExampleTraditionalChinese}}
```

---

## 6. ロシア語版の確定方針

ロシア語では、単語の辞書形だけでは小説読解に足りない。格変化、数、強勢、作中で実際に現れた語形をつなぐ必要がある。

想定フィールド：

```text
ID
Russian
StressMarked
Transliteration
Japanese
PartOfSpeech
FormInExample
GrammarInfo
ExampleRussian
ExampleTransliteration
ExampleJapanese
ExampleBreakdown
ExampleExplanation
Source
Tags
```

特に重視する項目：

- 辞書形
- 強勢付き表記
- ラテン文字転写
- 例文中の実際の語形
- 格
- 数
- 必要に応じて性
- 動詞の完了体・不完了体
- なぜ名詞や形容詞の形が変わるのかという説明

専門用語だけで終わらせず、たとえば次のように説明する。

```text
この文では、前後の語との関係を表すため、名詞が辞書形とは違う形になっています。
日本語では助詞で示す関係を、ロシア語では名詞の形の変化でも表します。
```

ロシア語Coreを先に作るのではなく、ロシア語版Novelを作り、本文で実際に採用した語と語形をAnkiへ収録する。

---

## 7. 英語版の方針

英語ではRomanizationに相当する欄は設けない。

代わりに次を重視する。

- 発音
- 品詞
- 冠詞
- 前置詞
- 時制
- 句動詞
- 語法
- コロケーション
- 日本語では省略されやすい主語や所有関係
- 直訳と自然訳の差

想定フィールド：

```text
ID
English
Pronunciation
Japanese
PartOfSpeech
Collocation
ExampleEnglish
ExampleJapanese
ExampleBreakdown
ExampleExplanation
Source
Tags
```

---

## 8. 韓国語Core 10

| ID | 한국어 | Romanization | 日本語 |
|---|---|---|---|
| C0001 | 기록 | girok | 記録 |
| C0002 | 기억 | gieok | 記憶 |
| C0003 | 도시 | dosi | 都市 |
| C0004 | 알림 | allim | 通知 |
| C0005 | 회신 | hoesin | 回信／返信 |
| C0006 | 수신인 | susinin | 受信人／宛先 |
| C0007 | 서명 | seomyeong | 署名 |
| C0008 | 검증 | geomjeung | 検証 |
| C0009 | 권한 | gwonhan | 権限 |
| C0010 | 역할 | yeokhal | 役割／ロール |

Core 10の全カードに次を収録済み。

- 韓国語単語
- 改訂ローマ字表記
- 日本語
- 品詞
- 韓国語例文
- 例文のローマ字表記
- 例文の日本語訳
- 文の組み立て
- なぜその意味になるのかという解説
- 出典
- TTSによる単語音声
- TTSによる例文音声

---

## 9. 韓国語Ankiノートタイプ

ノートタイプ名：

```text
MEMORIOPOLIS Korean Vocabulary
```

フィールドは次の12個。

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
```

現時点では、既存の10フィールドの末尾へ解説用2フィールドを追加したため、`Source`と`Tags`が9番目と10番目、解説欄が11番目と12番目になっている。この順番をCSVとノートタイプで一致させる。

---

## 10. 韓国語Ankiカード仕様

### 10.1 表面

```text
Concept ID
韓国語単語
韓国語単語TTS
```

表面では、Romanizationと日本語を表示しない。まずハングルを直接認識する。

表面テンプレート：

```html
<div class="concept-id">{{ID}}</div>
<div class="korean-word">{{Korean}}</div>

{{tts ko_KR:Korean}}
```

### 10.2 裏面

表示順：

```text
表面の再掲
Romanization
日本語
品詞
韓国語例文
例文TTS
例文Romanization
例文日本語訳
文の組み立て
なぜこの意味になる？
出典
```

解説用テンプレート：

```html
{{#ExampleBreakdown}}
<div class="explanation-block">
  <div class="explanation-title">文の組み立て</div>
  <div class="example-breakdown">{{ExampleBreakdown}}</div>
</div>
{{/ExampleBreakdown}}

{{#ExampleExplanation}}
<div class="explanation-block">
  <div class="explanation-title">なぜこの意味になる？</div>
  <div class="example-explanation">{{ExampleExplanation}}</div>
</div>
{{/ExampleExplanation}}
```

### 10.3 解説ブロックのCSS

```css
.explanation-block {
  margin-top: 18px;
  padding: 18px 16px;
  border-radius: 12px;
  background-color: #fff8e8;
  text-align: left;
}

.explanation-title {
  margin-bottom: 10px;
  color: #8a5a00;
  font-size: 15px;
  font-weight: 700;
  text-align: center;
}

.example-breakdown {
  font-size: 17px;
  line-height: 1.8;
  white-space: pre-line;
}

.example-explanation {
  font-size: 17px;
  line-height: 1.8;
}

.nightMode .explanation-block {
  background-color: #3b3528;
}

.nightMode .explanation-title {
  color: #f0c979;
}
```

---

## 11. CSV運用

### `ko_core10_master.csv`

- 見出し付き
- GitHub上で編集する正本
- 人間が内容を確認するためのファイル

現在の見出し：

```text
ID
Korean
Romanization
Japanese
PartOfSpeech
ExampleKorean
ExampleRomanization
ExampleJapanese
Source
Tags
ExampleBreakdown
ExampleExplanation
```

### `ko_core10_anki.csv`

- 見出しなし
- Ankiを再構築するときの全件投入用
- 10行が10枚のノートになる

### 差分更新ファイル

Coreを追加するときは、既存カードの重複を避けるため差分CSVを作る。

例：

```text
ko_core11-20_anki.csv
```

既存カードの解説だけを更新するときも、見出しなしの更新用CSVを一時的に使用できる。ただし一時ファイルは原則としてリポジトリへ残さず、masterと全件Anki版を正本・派生版として維持する。

インポート時は、最初のフィールド`ID`を照合キーとして、既存ノートを「更新」に設定する。

期待する結果：

```text
既存ノートを更新：対象件数
新規追加：0件
```

---

## 12. リポジトリ構成

現在の主要構造：

```text
MEMORIOPOLIS/
└─ language/
   ├─ anki/
   │  ├─ ko_core10_master.csv
   │  ├─ ko_core10_anki.csv
   │  └─ templates/
   │     ├─ README.md
   │     ├─ korean_vocabulary_front.html
   │     ├─ korean_vocabulary_back.html
   │     └─ korean_vocabulary_style.css
   ├─ audio/
   ├─ docs/
   ├─ glossary/
   │  └─ concept/
   │     ├─ README.md
   │     ├─ C0001_Record.md
   │     ├─ C0002_Memory.md
   │     ├─ C0003_City.md
   │     ├─ C0004_Notification.md
   │     ├─ C0005_Reply.md
   │     ├─ C0006_Recipient.md
   │     ├─ C0007_Signature.md
   │     ├─ C0008_Verification.md
   │     ├─ C0009_Authority.md
   │     └─ C0010_Role.md
   └─ lessons/
```

### 正本と派生物の関係

```text
Concept Markdown
言語横断の概念正本

master CSV
言語別教材データの正本

Anki CSV
Anki投入用の派生物

Ankiテンプレート
表示仕様の正本

Anki内コレクション
学習用の実行環境

AnkiWeb
端末間同期
```

---

## 13. バックアップ

Ankiのコレクションバックアップを作成済み。

```text
MEMORIOPOLIS_Core10_before_explanations_2026-09-08.colpkg
```

このファイルはGitHubへコミットしない。リポジトリ外の個人用バックアップとして保管する。

推奨保存先例：

```text
C:\AnkiBackups\
```

または、OneDrive上でもGitリポジトリ外の専用フォルダーを使用する。

---

## 14. Git反映状況

Core 10の例文解説対応はコミットおよびpush済み。

コミット：

```text
2d24d7a feat(language): add beginner-friendly example explanations to Korean Core 10
```

反映内容：

- 韓国語Core 10全件へ`ExampleBreakdown`を追加
- 韓国語Core 10全件へ`ExampleExplanation`を追加
- master CSVを12列へ更新
- Anki投入用CSVを12列へ更新
- 裏面テンプレートへ解説欄を追加
- 解説欄のCSSと夜間モードを追加
- テンプレートREADMEを12フィールドへ更新
- 例文解説の執筆方針をREADMEへ追加

GitHubの`main`ブランチへpush済み。

### Git自動整理の注意

リポジトリがOneDrive配下にあるため、Gitの自動整理で次のような表示が出た。

```text
Deletion of directory '.git/objects/xx' failed.
Should I try again? (y/n)
```

これはOneDriveなどが`.git/objects`を一時的にロックしている可能性がある。処理が終わらない場合は`Ctrl + C`で中断し、次を確認する。

```powershell
git status
git log -1 --oneline
```

コミットが作成済みで作業ツリーがcleanなら、そのままpushできる。

今後も頻発する場合は、将来的にGitリポジトリをOneDrive同期対象外へ移すことを検討する。

```text
C:\GitHub\MEMORIOPOLIS
```

ただし、移動は別作業として慎重に行う。

---

## 15. Anki実行環境

### 15.1 Windows版Anki

確認済み：

- Core 10の10件を読み込み済み
- ノートタイプの12フィールド化済み
- 単語TTSが再生可能
- 例文TTSが再生可能
- 例文分解と例文解説が表示可能
- C0010の長い例文・解説も横スクロールなし
- 夜間モード用CSSを実装済み

韓国語TTS：

```html
{{tts ko_KR:Korean}}
{{tts ko_KR:ExampleKorean}}
```

Windowsへ韓国語の音声合成機能を追加済み。

### 15.2 AnkiWeb

AnkiWebアカウントを作成し、認証済み。

Windows版AnkiからAnkiWebへ初回アップロード済み。

確認済み：

- Core 10がAnkiWebへ同期される
- カードテンプレートが反映される
- 例文分解が表示される
- 例文解説が表示される
- 学習ボタンが利用できる

既知の制約：

AnkiWebのブラウザー版では、TTSタグが音声プレイヤーとして処理されず、次のような文字列として表示された。

```text
[anki:tts lang=ko_KR]기록[/anki:tts]
```

したがって、AnkiWebブラウザー版は次の用途に使う。

- データ同期の確認
- 音声を必要としない学習
- カードと解説の閲覧

音声付きの主なスマートフォン学習にはAnkiDroidを使用する。

### 15.3 AnkiDroid

インストール済み。

AnkiWebと同期済み。

確認済み：

- Core 10が表示される
- 韓国語単語TTSが再生される
- 韓国語例文TTSが再生される
- 例文分解と例文解説が表示される

日常の主な学習環境として、通勤時間にAnkiDroidを使用する。

---

## 16. 現在の端末運用

```text
GitHub
教材データ、概念、テンプレートの正本

Windows版Anki
CSVのインポート、フィールドとテンプレートの管理、PC学習

AnkiWeb
WindowsとAndroid間の同期中継、Web閲覧

AnkiDroid
通勤時間の日常トレーニング、韓国語TTS再生
```

### 同期の基本ルール

```text
PCでカードやテンプレートを更新
  ↓
Windows版AnkiからAnkiWebへ同期
  ↓
AnkiDroidで同期
  ↓
AnkiDroidで学習
  ↓
AnkiDroidで同期
  ↓
Windows版Ankiで同期
```

ノートタイプへのフィールド追加やカードテンプレート変更は、単純にマージできない場合がある。そのため、構造変更は原則としてWindows版Ankiで行い、完了後にAnkiWebへ同期してから、AnkiDroidへ反映する。

---

## 17. 通勤学習で確認すること

Core 10を実際に通勤中に使い、次を観察する。

### 学習負荷

- 10枚を一巡する時間
- 一日に無理なく追加できる新規カード数
- 解説を毎回読む負担
- 音声を聞く回数
- 復習量の増え方

### 表示

- 文字サイズ
- 解説ブロックの幅
- 縦スクロール量
- C0010の長文表示
- 夜間モード
- 横スクロールの有無

### 内容

- Romanizationが発音確認に役立つか
- 解説が長すぎないか
- 解説が短すぎないか
- 専門用語が多すぎないか
- 「なぜこの訳になるか」が腹落ちするか
- 同じ文法の説明が冗長になっていないか
- 例文が作品世界と結び付いているか

### 音声

- 単語TTSの自然さ
- 例文TTSの自然さ
- 音量
- 速度
- 通勤環境で聞き取りやすいか

気づきは、後で次のようなファイルへ蓄積するとよい。

```text
language/docs/anki_learning_notes_ko.md
```

---

## 18. 韓国語Core 11から50への方針

Core 10の通勤学習で大きな問題がなければ、10語ずつ拡張する。

```text
Core 11-20
Core 21-30
Core 31-40
Core 41-50
```

各10語で行うこと：

1. Concept Markdownを作成
2. master CSVを更新
3. 差分Anki CSVを作成
4. 全件Anki CSVを更新
5. 全例文に`ExampleBreakdown`を付ける
6. 全例文に`ExampleExplanation`を付ける
7. Windows版Ankiへ差分インポート
8. 追加件数と重複なしを確認
9. Windows版で表示とTTSを確認
10. AnkiWebへ同期
11. AnkiDroidへ同期
12. 通勤中に実地検証
13. GitHubへコミット

### Core 11から20の候補

| ID | 한국어 | 日本語 |
|---|---|---|
| C0011 | 경로 | 経路 |
| C0012 | 복호화 | 復号 |
| C0013 | 열쇠 | 鍵 |
| C0014 | 참조 | 参照 |
| C0015 | 식별자 | 識別子 |
| C0016 | 설정 | 設定 |
| C0017 | 정지 | 停止 |
| C0018 | 재개 | 再開 |
| C0019 | 실행 | 実行 |
| C0020 | 영향 | 影響 |

この候補は第12節の読解に直結する語を優先している。作成時には第12節本文との一致、語の重要度、既存Conceptとの重複を再確認する。

---

## 19. Core 50でロシア語版Novelへ移る方針

韓国語Core 100まで一気に進まず、韓国語Core 50を第一観測点とする。

推奨順序：

```text
韓国語Core 10
  ↓
通勤学習による実地検証
  ↓
韓国語Core 20
  ↓
韓国語Core 30
  ↓
韓国語Core 40
  ↓
韓国語Core 50
  ↓
設計レビュー
  ↓
第12節ロシア語版Novel
  ↓
ロシア語Anki Core 5試作
  ↓
ロシア語Core 10で端末検証
  ↓
ロシア語Core 50
  ↓
言語間の設計レビュー
  ↓
韓国語Core 51以降へ戻る
```

### Core 50で切り替える理由

- 韓国語で教材制作の基本パイプラインが十分に成熟する
- Core 100まで韓国語固有の設計を固定しすぎずに済む
- ロシア語で必要な格、強勢、語形情報を早期に設計へ反映できる
- Concept IDが本当に多言語で機能するか確認できる
- 小説制作と教材制作が互いを止めず、交互に進む
- 翻訳による概念のずれをCore 51以降へ反映できる

### ロシア語版の作業順

1. 第12節ロシア語版Novelを作成する
2. 本文で採用した訳語と語形を抽出する
3. C0001からC0050へロシア語レイヤーを追加する
4. ロシア語用ノートタイプを設計する
5. Core 5で試作する
6. Windows版Ankiで表示とTTSを確認する
7. AnkiWebとAnkiDroidで同期する
8. Core 10で学習体験を確認する
9. 問題がなければCore 50まで拡張する

---

## 20. Core 1000までの全体ロードマップ

Core 1000を先に完成させてからNovelへ移る方式は採用しない。

Core 1000は、複数の節を五言語で通過した結果として形成する。

推奨される螺旋型の進行：

```text
第12節
  ↓
韓国語Core 50
  ↓
第12節ロシア語版
  ↓
ロシア語Core 50
  ↓
韓国語Core 51-100
  ↓
第12節臺灣繁體中文版
  ↓
臺灣華語Core 100
  ↓
第12節英語版
  ↓
英語Core 100
  ↓
第12節の五言語読解ユニット完成
  ↓
第13節
  ↓
C0101以降を追加
  ↓
Core 200付近へ
  ↓
次の節
```

語彙の追加数は、必ずしも各節100語に固定しない。

```text
第12節：C0001-C0100
第13節：C0101-C0165
第14節：C0166-C0240
```

のように、作品読解に必要な概念数に応じて増減してよい。

一方、Ankiの公開・配布単位は100語ごとにまとめることができる。

---

## 21. 次回の開始手順

次回はCore 11から20へ進む前に、通勤学習の初期所感を確認する。

### チェックリスト

- [ ] AnkiDroidでCore 10を一巡した
- [ ] 単語TTSが通勤環境で聞こえる
- [ ] 例文TTSが通勤環境で聞こえる
- [ ] 解説欄が最後まで読める
- [ ] C0010の長文でも横スクロールが出ない
- [ ] 解説量が負担になりすぎない
- [ ] `ExampleBreakdown`が理解に役立つ
- [ ] `ExampleExplanation`で日本語訳への道筋が分かる
- [ ] AnkiDroidで学習後に同期した
- [ ] Windows版Ankiで同期し、学習履歴が反映された
- [ ] 改善点をメモした

### 問題がなければ作成するもの

```text
C0011-C0020のConcept Markdown
ko_core20_master.csv
ko_core11-20_anki.csv
ko_core20_anki.csv
```

すべての新規カードに、最初から次を含める。

```text
ExampleBreakdown
ExampleExplanation
```

---

## 22. リポジトリへ今後追加したい文書

```text
language/docs/
├─ MEMORIOPOLIS_LANGUAGE_COURSE_HANDOFF_COMPLETE_2026-09-08.md
├─ anki_learning_notes_ko.md
├─ explanation_writing_guide.md
└─ multilingual_field_design.md
```

### `anki_learning_notes_ko.md`

通勤学習で得た実地の気づきを記録する。

### `explanation_writing_guide.md`

例文解説の品質基準、良い例、避けたい例、初出と再登場の扱いをまとめる。

### `multilingual_field_design.md`

韓国語、ロシア語、臺灣華語、英語のフィールド差を整理する。

---

## 23. 完了済みチェックリスト

- [x] `language/anki/`を作成
- [x] `language/audio/`を作成
- [x] `language/glossary/`を作成
- [x] `language/glossary/concept/`を作成
- [x] `language/lessons/`を作成
- [x] C0001からC0010のConcept Markdownを作成
- [x] 韓国語Core 10 master CSVを作成
- [x] 韓国語Core 10 Anki CSVを作成
- [x] Windows版Ankiを導入
- [x] `MEMORIOPOLIS::Korean`デッキを作成
- [x] 韓国語用ノートタイプを作成
- [x] AnkiテンプレートをGitHubへ保存
- [x] Windowsへ韓国語TTSを追加
- [x] 単語TTSを確認
- [x] 例文TTSを確認
- [x] `ExampleBreakdown`を追加
- [x] `ExampleExplanation`を追加
- [x] Core 10全件へ例文分解を追加
- [x] Core 10全件へ初学者向け解説を追加
- [x] 解説用CSSを追加
- [x] 夜間モード用CSSを追加
- [x] テンプレートREADMEへ執筆方針を追加
- [x] C0010の長文表示を確認
- [x] Ankiコレクションをバックアップ
- [x] GitHubの`main`へpush
- [x] AnkiWebアカウントを作成・認証
- [x] Windows版AnkiからAnkiWebへ同期
- [x] AnkiWeb上でカードと解説を確認
- [x] AnkiWebブラウザー版のTTS制約を確認
- [x] AnkiDroidをインストール
- [x] AnkiDroidとAnkiWebを同期
- [x] AnkiDroidで単語音声を確認
- [x] AnkiDroidで例文音声を確認

---

## 24. 現在地

現在、次の制作・学習系統が実働している。

```text
MEMORIOPOLIS GitHub正本
  ↓
言語非依存のConcept Dictionary
  ↓
韓国語Core Vocabulary
  ↓
単語・例文・Romanization・日本語訳
  ↓
文の組み立て
  ↓
なぜその意味になるのかという解説
  ↓
Windows版Anki
  ↓
AnkiWeb同期
  ↓
AnkiDroid
  ↓
通勤時間の音声付き反復学習
```

『記憶都市読解コース』は、単語を暗記する教材から、文が意味へ変わる過程を読者へ開く教材へ進んだ。

初級と中級の間にある説明されない空白を、時間のある人だけが自力で越えるのではなく、必要な橋を教材側が用意する。

その橋は、次の二つの問いによって支えられる。

```text
この文は、どのように組み立てられているか。

なぜ、この日本語訳になるのか。
```

この原則を、今後の韓国語Core 50、ロシア語版Novel、臺灣華語版、英語版、そして五言語共通のConcept Dictionaryへ継承する。

---

## 25. 次回への一文

次回は、通勤時間にCore 10を使った読者自身の感触から始める。

教材を先に増やすのではなく、実際に橋を渡ってみて、どこが歩きやすく、どこに手すりが足りないかを確認する。

その確認を経て、韓国語Core 11から20へ進む。
