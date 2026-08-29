# 『記憶都市（メモリオポリス）』第四章 第十節 GitHub Pages Build設計書

## 第十節「二つの信頼」公開設計

**状態：実装前設計FIX候補**  
**更新日：2026年8月29日**  
**対象：五言語本文、第五幕・制作ノート、予告編、GA4観測、中央駅接続**

---

## 0．設計の目的

第十節「二つの信頼」を、GitHub上のMarkdown正本からGitHub Pages用の公開成果物へ変換する。

第九節の最小PoCで得た仕組みをそのまま複製せず、第十節の内容に合わせて整理する。

```text
第九節
= 五言語本文
+ 数式
+ BGM
+ 制作ノート
+ Python観測窓

第十節
= 五言語本文
+ 第五幕・制作ノート
+ 21秒の縦型予告編
+ 同意連動GA4
```

第十節では、作品閲覧をGA4への同意条件にしない。

中央駅で保存された解析設定を引き継ぎ、許可した読者に限って最小限のイベントを送信する。

---

## 1．設計原則

### 1.1 正本と公開成果物を分離する

```text
novel/
= 正本、制作制度、再生成可能な素材

experience/
= GitHub Pagesで公開する成果物
```

公開HTMLを手作業で正本化しない。

本文と制作ノートは、`novel/chapter04/section10/` のMarkdownを正本とする。

### 1.2 五言語を対等に扱う

対象言語：

```text
ja     日本語
 en    English
zh-TW  臺灣繁體中文
ko     한국어
ru     Русский
```

初期表示は日本語とする。

切り替え順は、この制作工程の順序に合わせる。

```text
日本語 → English → 臺灣繁體中文 → 한국어 → Русский
```

### 1.3 第五幕は付録にしない

`section10_production_notes.md` は、単なる翻訳レビューではない。

本文の後に続く「第五幕」として、独立ページで公開する。

本文ページからは、次の言葉で導く。

```text
第五幕「私たち」と書かなかった場所へ
```

### 1.4 予告編は読者が再生する

予告編は自動再生しない。

- 再生操作は読者に委ねる。
- 初期状態は停止とする。
- 音声付きMP4を使用する。
- ブラウザ標準の再生、停止、音量、全画面操作を利用できるようにする。
- インライン再生を許可する。

### 1.5 観測は任意参加とする

中央駅と同じローカルストレージキーを使用する。

```text
memoriopolis_analytics_consent
```

状態：

```text
granted
= GA4タグを読み込む

denied
= GA4タグを読み込まない

未設定
= GA4タグを読み込まない
= 作品は通常どおり閲覧可能
```

---

## 2．入力となる正本

配置：

```text
novel/chapter04/section10/
├── LOCALIZATION_READY
├── section10_ja.md
├── section10_en.md
├── section10_zh-TW.md
├── section10_ko.md
├── section10_ru.md
├── section10_production_notes.md
└── trailer/
    ├── storyboard.md
    ├── build_trailer.py
    ├── build_soundtrack.py
    ├── mux_trailer_audio.py
    ├── assets/
    │   ├── 01_operations_bureau.png
    │   ├── 02_artificial_hand.png
    │   ├── 03_boundary_line.png
    │   ├── 04_unnamed_space.png
    │   ├── 05_four_reflections.png
    │   └── 06_title_background.png
    └── output/
        └── section10_trailer_final.mp4
```

### 2.1 公開に必須の入力

```text
LOCALIZATION_READY
section10_ja.md
section10_en.md
section10_zh-TW.md
section10_ko.md
section10_ru.md
section10_production_notes.md
trailer/output/section10_trailer_final.mp4
```

### 2.2 Build前に検査すること

- `LOCALIZATION_READY` が存在する。
- 五言語Markdownがすべて存在する。
- 五言語の見出し階層が期待どおりである。
- 五言語の本文が空ではない。
- 制作ノートが存在する。
- 制作ノートに第五幕の見出しがある。
- 完成予告編が存在する。
- 予告編のファイルサイズが0ではない。
- 予告編がMP4である。

---

## 3．公開成果物

Build後のローカル公開成果物：

```text
experience/chapter04/section10/
├── index.html
├── notes.html
├── trailer.html
├── script.js
├── styles.css
└── media/
    └── section10_trailer_final.mp4
```

GitHub Actionsが組み立てるPages artifact：

```text
_site/chapter04/section10/
├── index.html
├── notes.html
├── trailer.html
├── script.js
├── styles.css
└── media/
    └── section10_trailer_final.mp4
```

公開URL：

```text
本文
https://netarott.github.io/MEMORIOPOLIS/chapter04/section10/

第五幕
https://netarott.github.io/MEMORIOPOLIS/chapter04/section10/notes.html

予告編
https://netarott.github.io/MEMORIOPOLIS/chapter04/section10/trailer.html
```

---

## 4．本文ページ `index.html`

### 4.1 役割

- 第十節本文を表示する。
- 五言語を切り替える。
- 第五幕へ導く。
- 予告編へ導く。
- 中央駅へ戻る。
- 許可された場合だけGA4で閲覧と操作を観測する。

### 4.2 ページ構成

```text
ヘッダー
├── 記憶都市
├── 第四章「翻訳者」
├── 第十節「二つの信頼」
└── 中央駅へ戻る

言語切り替え
├── 日本語
├── English
├── 臺灣繁體中文
├── 한국어
└── Русский

物語本文
└── 選択中の言語だけ表示

節末ナビゲーション
├── 第五幕へ
├── 予告編へ
└── 中央駅へ

フッター
├── GitHub正本への説明
├── アクセス解析について
└── 解析設定を変更
```

### 4.3 五言語本文の埋め込み方式

Build時に五言語MarkdownをHTMLへ変換し、一つの`index.html`へ埋め込む。

```html
<article data-language="ja">...</article>
<article data-language="en" hidden>...</article>
<article data-language="zh-TW" hidden>...</article>
<article data-language="ko" hidden>...</article>
<article data-language="ru" hidden>...</article>
```

利点：

- 言語切り替え時に追加通信が不要。
- 静的GitHub Pagesだけで動作する。
- 五言語の公開漏れをBuild時に検査できる。
- JavaScriptが無効でも日本語本文を表示できる。

### 4.4 言語切り替えUI

ボタン型の切り替えとする。

```html
<button type="button" data-language-button="ja">日本語</button>
```

状態表現：

- 選択中のボタンへ`aria-pressed="true"`を付与する。
- 非選択ボタンへ`aria-pressed="false"`を付与する。
- 選択中本文以外は`hidden`にする。
- `document.documentElement.lang`を選択言語に更新する。
- 選択言語をURLハッシュへ反映する。

例：

```text
#ja
#en
#zh-TW
#ko
#ru
```

初期選択：

```text
有効なURLハッシュがある
→ その言語

有効なURLハッシュがない
→ 日本語
```

### 4.5 読書位置

初版では、言語切り替え時に段落位置の同期を行わない。

理由：

- 言語によって段落長が異なる。
- 自動同期は誤った対応関係を作る可能性がある。
- 第九節と同様、全文を一つの作品として切り替える方が安定する。

言語切り替え後は、本文先頭付近へ穏やかに移動する。

ただし、読者が意図しない移動を避けるため、初版ではスクロール位置維持も比較対象とし、ローカル確認で決める。

---

## 5．第五幕ページ `notes.html`

### 5.1 正本

```text
novel/chapter04/section10/section10_production_notes.md
```

### 5.2 役割

- 第五幕「私たち」と書かなかった場所を表示する。
- 四つの言語からの反射を保存する。
- 第四回Returnで日本語正本を変更しなかった理由を示す。
- 第四人称／ポセイドンを記録する。
- 第十一節へ渡す問いを示す。

### 5.3 ページ構成

```text
ヘッダー
├── 第五幕
├── 「私たち」と書かなかった場所
└── 第十節本文へ戻る

制作ノート本文

節末ナビゲーション
├── 第十節本文へ戻る
├── 予告編を見る
└── 中央駅へ戻る
```

### 5.4 多言語断片

制作ノート中の英語、臺灣繁體中文、韓国語、ロシア語は、原文表記を保持する。

ページ全体は日本語だが、外国語引用部分へ適切な`lang`属性を付ける。

```html
<blockquote lang="en">...</blockquote>
<blockquote lang="zh-TW">...</blockquote>
<blockquote lang="ko">...</blockquote>
<blockquote lang="ru">...</blockquote>
```

自動付与が難しい場合、Buildスクリプト側で既知のアンカー部分へ付与する。

---

## 6．予告編ページ `trailer.html`

### 6.1 使用動画

正本：

```text
novel/chapter04/section10/trailer/output/section10_trailer_final.mp4
```

公開先：

```text
experience/chapter04/section10/media/section10_trailer_final.mp4
```

### 6.2 video要素

```html
<video
  controls
  playsinline
  preload="metadata"
  poster="../../assets/images/section10-trailer-poster.png">
  <source src="media/section10_trailer_final.mp4" type="video/mp4">
</video>
```

初版でポスター画像を別途用意しない場合、`poster`属性は省略する。

完成動画の素材6からポスターを作成する案は、公開確認後の追加改善とする。

### 6.3 再生方針

```text
autoplay  使用しない
muted     強制しない
loop      使用しない
controls  使用する
playsinline 使用する
preload   metadata
```

### 6.4 ページ構成

```text
ヘッダー
├── 第十節予告編
└── 第十節本文へ戻る

縦型動画

説明
├── 21秒
├── 五言語の反射
└── Pythonで再生成可能

ナビゲーション
├── 第十節本文へ
├── 第五幕へ
└── 中央駅へ
```

### 6.5 アクセシビリティ

初版では字幕が映像へ焼き込まれている。

追加で、動画直下にテキスト版の字幕を折りたたみ表示できるようにする。

```html
<details>
  <summary>予告編の字幕を読む</summary>
  ...
</details>
```

収録する字幕：

```text
いつもの名前。
いつもの言葉。
いつもの朝。

これが本人のメッセージだという根拠は？

疑うこと。
確かめること。

二つの答えのあいだに、
まだ名前のない空間ができた。

To verify.
不急著決定。
확인할 수 있는지
как мы доверяем

記憶都市（メモリオポリス）
第四章 第十節
「二つの信頼」
```

---

## 7．共有スタイル `styles.css`

### 7.1 方向性

第九節と同じ世界に見えるが、第十節固有の視覚言語を持たせる。

```text
背景       黒、濃紺
本文       白に近い灰色
補助文字   青みのある灰色
強調       淡いシアン
境界       細い光の線
余白       広め
```

### 7.2 主要要素

- 中央配置の読み物領域。
- 本文幅は日本語で読みやすい範囲に制限する。
- 長い英語・ロシア語でも窮屈にならない最大幅を持たせる。
- 言語切り替えは折り返し可能にする。
- スマートフォンではボタンを複数行にする。
- 縦型動画は画面高さを超えない。

動画の表示例：

```css
.trailer-video {
  width: min(100%, 27rem);
  max-height: 78vh;
  aspect-ratio: 9 / 16;
  background: #000;
}
```

### 7.3 第五幕の引用

四言語引用を同じ視覚的重みで扱う。

国旗、色分け、国別アイコンは使わない。

言語名は必要な場所に限って文字で表示する。

---

## 8．共有動作 `script.js`

### 8.1 担当機能

```text
言語切り替え
URLハッシュ更新
lang属性更新
GA4の許可状態継承
カスタムイベント送信
解析設定パネルの再表示
予告編再生イベント
```

### 8.2 GA4共通部品

中央駅の既存部品を利用する。

```text
experience/assets/js/analytics-consent.js
experience/assets/css/analytics-consent.css
```

第十節の3ページから、階層に合った相対パスで読み込む。

```html
<link rel="stylesheet" href="../../../assets/css/analytics-consent.css">
<script defer src="../../../assets/js/analytics-consent.js"></script>
```

第十節固有の`script.js`は、GA4が未許可または未読込の場合でもエラーにならないようにする。

イベント送信前に、次を確認する。

```javascript
localStorage.getItem('memoriopolis_analytics_consent') === 'granted'
typeof window.gtag === 'function'
```

### 8.3 カスタムイベント

#### `language_switch`

言語ボタンを使って表示言語を変更したとき、一回送信する。

パラメーター：

```text
section_id     section10
from_language  ja / en / zh-TW / ko / ru
to_language    ja / en / zh-TW / ko / ru
```

送らないもの：

- 読者名
- メールアドレス
- 個別の自由入力
- 独自のユーザー識別子

#### `open_production_notes`

本文または予告編ページから、第五幕へのリンクを読者が選択したときに送信する。

パラメーター：

```text
section_id  section10
source      story / trailer
```

#### `trailer_play`

予告編ページのvideo要素で、最初の`play`が発生したときに一回だけ送信する。

パラメーター：

```text
section_id  section10
trailer_id  section10_trailer_final
```

初版では、次を送らない。

```text
pause回数
再生位置
視聴完了率
音量変更
全画面操作
```

### 8.4 `page_view`

Googleタグの標準ページビューを利用する。

独自の`page_view`を重複送信しない。

---

## 9．Buildスクリプト

### 9.1 ファイル名

```text
scripts/build_section10.py
```

### 9.2 責務

```text
入力検査
五言語Markdown読み込み
制作ノート読み込み
MarkdownからHTMLへの変換
index.html生成
notes.html生成
trailer.html生成
script.js生成またはテンプレート配置
styles.css生成またはテンプレート配置
完成MP4のコピー
出力検査
```

### 9.3 実行方法

```powershell
py scripts/build_section10.py
```

検査のみ：

```powershell
py scripts/build_section10.py --check
```

### 9.4 出力先

```text
experience/chapter04/section10/
```

### 9.5 Markdown変換

候補：

- Python Markdownライブラリを使用する。
- 第九節Builderと同じ変換方針を再利用する。
- 不要な依存を増やさず、GitHub Actionsで再現できる方法を優先する。

第九節Builderに共通化可能な処理がある場合でも、最初から大規模なリファクタリングはしない。

第十節を一度正しくBuildした後に、共通化を検討する。

### 9.6 Buildの再現性

同じ入力から同じ公開成果物を生成する。

Build時刻、ローカル絶対パス、ユーザー名などをHTMLへ埋め込まない。

---

## 10．中央駅の更新

現在の中央駅には第九節への入口がある。

第十節公開時に、中央駅へ第十節の入口を追加する。

```text
第四章 第九節
「まだ送られていない矢印」

第四章 第十節
「二つの信頼」
```

### 10.1 表示順

新しい節を上へ置くことを候補とする。

```text
第十節
第九節
```

ただし、物語順を重視する場合は第九節、第十節の順とする。

初版では物語順を優先し、次を採用する。

```text
第九節
↓
第十節
```

### 10.2 第十節カード

```text
OPEN PLATFORM
第四章 第十節
「二つの信頼」
［第十節をひらく］
```

予告編は中央駅から直接開かず、第十節ページを経由する。

理由：

- 予告編だけを作品本体から切り離さない。
- 本文、第五幕、予告編を一つの節として経験してもらう。

---

## 11．GitHub Actionsの変更

対象：

```text
.github/workflows/deploy-pages.yml
```

### 11.1 pathsへ追加

```yaml
- "novel/chapter04/section10/**"
- "scripts/build_section10.py"
```

`experience/**`は既存対象として維持する。

### 11.2 Buildステップ

第九節と同様に、検査後にBuildする。

```bash
python scripts/build_section10.py --check
python scripts/build_section10.py
```

### 11.3 artifact組み立て

ディレクトリ作成：

```bash
mkdir -p _site/chapter04/section10
```

コピー：

```bash
cp -R experience/chapter04/section10/. _site/chapter04/section10/
```

### 11.4 存在検査

```bash
test -f _site/chapter04/section10/index.html
test -f _site/chapter04/section10/notes.html
test -f _site/chapter04/section10/trailer.html
test -f _site/chapter04/section10/script.js
test -f _site/chapter04/section10/styles.css
test -f _site/chapter04/section10/media/section10_trailer_final.mp4
```

MP4が空でないことも検査する。

```bash
test -s _site/chapter04/section10/media/section10_trailer_final.mp4
```

---

## 12．ローカルテスト

### 12.1 Build

```powershell
py scripts/build_section10.py --check
py scripts/build_section10.py
```

### 12.2 HTTPサーバー

リポジトリルートで実行する。

```powershell
py -m http.server 8000
```

確認URL：

```text
http://localhost:8000/experience/chapter04/section10/
http://localhost:8000/experience/chapter04/section10/notes.html
http://localhost:8000/experience/chapter04/section10/trailer.html
```

### 12.3 本文ページ確認

```text
[ ] 日本語が初期表示される
[ ] 五言語ボタンが表示される
[ ] 五言語すべてへ切り替えられる
[ ] URLハッシュが更新される
[ ] 再読み込み後もハッシュの言語が表示される
[ ] 見出しと本文が欠落していない
[ ] 第五幕へのリンクが動く
[ ] 予告編へのリンクが動く
[ ] 中央駅へのリンクが動く
[ ] JavaScript無効時に日本語本文が読める
```

### 12.4 第五幕確認

```text
[ ] 全文が表示される
[ ] 四言語引用が文字化けしない
[ ] ロシア語のёが保持される
[ ] 韓国語の分かち書きが保持される
[ ] 臺灣繁體中文が簡体字化されていない
[ ] 本文へ戻れる
[ ] 予告編へ移動できる
[ ] 中央駅へ戻れる
```

### 12.5 予告編確認

```text
[ ] 自動再生されない
[ ] 再生ボタンで開始する
[ ] 音声が再生される
[ ] 21秒で自然に終了する
[ ] 縦型比率が崩れない
[ ] スマートフォン幅に収まる
[ ] 全画面表示できる
[ ] 字幕テキスト版を開ける
[ ] 本文へ戻れる
[ ] 第五幕へ移動できる
```

### 12.6 GA4確認

まず、ローカルストレージを未設定にする。

```javascript
localStorage.removeItem('memoriopolis_analytics_consent');
location.reload();
```

確認：

```text
[ ] 未設定ではGA4タグを読み込まない
[ ] 未設定でもすべて閲覧できる
[ ] deniedではGA4タグを読み込まない
[ ] grantedではGA4タグを読み込む
[ ] language_switchは許可時だけ送信する
[ ] open_production_notesは許可時だけ送信する
[ ] trailer_playは許可時だけ一度送信する
[ ] page_viewを二重送信しない
```

---

## 13．公開後の確認

GitHub Actions：

```text
[ ] build成功
[ ] deploy成功
```

公開URL：

```text
[ ] 第十節本文が開く
[ ] 第五幕が開く
[ ] 予告編が再生できる
[ ] 中央駅から第十節へ移動できる
[ ] 第十節から中央駅へ戻れる
```

GA4リアルタイム：

```text
[ ] 第十節本文のpage_view
[ ] notes.htmlのpage_view
[ ] trailer.htmlのpage_view
[ ] language_switch
[ ] open_production_notes
[ ] trailer_play
```

イベント確認は篠原さん自身の許可済みブラウザで行う。

公開直後にイベント数が0でも、反映まで短い遅延がある可能性を考慮する。

---

## 14．Git管理方針

### 14.1 コミットするもの

```text
五言語Markdown
LOCALIZATION_READY
section10_production_notes.md
trailer/storyboard.md
trailer/build_trailer.py
trailer/build_soundtrack.py
trailer/mux_trailer_audio.py
trailer/assets/*.png
trailer/output/section10_trailer_final.mp4
build-section10-design.md
scripts/build_section10.py
experience/chapter04/section10/**
中央駅の更新
GitHub Actionsの更新
```

### 14.2 コミットしない中間成果物

```text
trailer/output/preview_frames/
trailer/output/section10_trailer_silent_prototype01.mp4
trailer/output/section10_trailer_soundtrack_prototype01.wav
trailer/output/section10_trailer_prototype01.mp4
```

これらは制作スクリプトから再生成できる。

### 14.3 `.gitignore`候補

```gitignore
# Section 10 trailer intermediate outputs
novel/chapter04/section10/trailer/output/preview_frames/
novel/chapter04/section10/trailer/output/*_prototype*.mp4
novel/chapter04/section10/trailer/output/*_prototype*.wav
```

完成版`section10_trailer_final.mp4`は追跡対象にする。

---

## 15．実装順序

```text
1. build-section10-design.mdをFIX
2. scripts/build_section10.pyを作成
3. --checkを実行
4. 第十節公開成果物を生成
5. ローカルHTTPサーバーで本文を確認
6. 五言語切り替えを確認
7. 第五幕ページを確認
8. 予告編ページを確認
9. GA4未許可時の動作を確認
10. GA4許可時のイベントを確認
11. 中央駅へ第十節入口を追加
12. deploy-pages.ymlを更新
13. git diffとgit diff --checkを確認
14. Commit & Push
15. GitHub Actions成功を確認
16. 公開URLを確認
17. GA4リアルタイムを確認
```

---

## 16．初版で行わないこと

- 第九節へのGA4後付け。
- 第十節へのPython観測窓追加。
- 予告編の自動再生。
- 予告編のループ再生。
- 再生位置や視聴完了率の細かな追跡。
- 言語切り替え時の段落単位同期。
- 五言語ごとの別URL作成。
- 国旗による言語選択。
- 第十一節へのリンク追加。
- 大規模な第九節Builderとの共通化。
- 外部動画配信サービスへの依存。

第十一節が未公開の間は、次節リンクを表示しない。

---

## 17．完了条件

第十節の公開実装は、次のすべてを満たした時点で完了とする。

```text
五言語本文が一つのページで切り替えられる
第五幕が独立ページとして読める
完成予告編が読者操作で再生できる
中央駅から第十節へ入れる
第十節から中央駅へ戻れる
未同意でも全機能を利用できる
許可時だけGA4が動く
最小イベントが重複なく送信される
GitHub Actionsで再現可能にBuildできる
公開URLでPCとスマートフォンの両方を確認できる
```

---

## 18．次に作成するもの

```text
scripts/build_section10.py
```

最初の実装目標：

```text
五言語Markdown
+ 第五幕Markdown
+ 完成予告編
↓
experience/chapter04/section10/
```

へ、再現可能な静的公開成果物を生成する。
