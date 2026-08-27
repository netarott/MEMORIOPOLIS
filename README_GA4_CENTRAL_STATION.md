# Google Analytics 4 中央駅導入パッケージ（非モーダル版）

## 測定ID

`G-L51VXQ23B6`

## 配置

ZIPをリポジトリルートへ展開し、次のファイルを配置・差し替えします。

```text
experience/index.html                              差し替え
experience/privacy.html                            新規
experience/assets/js/analytics-consent.js          新規
experience/assets/css/analytics-consent.css        新規
```

現在の `deploy-pages.yml` は `experience/assets/` を公開成果物へコピーするため、assets用の追加変更は不要です。`experience/privacy.html` は中央駅の `experience/index.html` と同じ公開ルートからコピーされる現行構成では、ワークフローの `cp experience/index.html _site/index.html` だけでは公開されません。次の行を `Assemble Pages artifact` に追加してください。

```bash
cp experience/privacy.html _site/privacy.html
```

確認用の行も追加します。

```bash
test -f _site/privacy.html
```

## 動作

- 初回訪問では画面右下に非モーダルの選択パネルを表示します。
- 選択前も中央駅と作品を通常どおり閲覧できます。Googleの解析タグは読み込みません。
- 「観測を許可する」を選ぶとGA4を読み込み、ページビューを送信します。
- 「許可しない」を選ぶとGA4を読み込みません。
- 選択はローカルストレージへ保存します。
- 中央駅下部とプライバシーページから選び直せます。
- Google Signalsと広告パーソナライズ信号は明示的に無効化しています。

## ローカル確認

```powershell
python -m http.server 8000
```

```text
http://localhost:8000/experience/
```

初回確認後、設定を消して再試験するには、開発者ツールのConsoleで次を実行して再読み込みします。

```javascript
localStorage.removeItem('memoriopolis_analytics_consent');
location.reload();
```

## 公開確認

1. Commit & Push
2. GitHub Actionsのbuild / deploy成功を確認
3. 中央駅を開いて「観測を許可する」を選択
4. GA4のリアルタイムレポートを確認
5. 中央駅下部の「解析設定を変更」で拒否へ変更できることを確認

## 注意

このパッケージは中央駅だけの非モーダル最小導入です。第九節、制作ノート、Python観測窓にはまだ解析タグを追加しません。
