# Section 11 Shorts Storyboard Builder

## 配置

リポジトリのルートを基準に，次へ配置します．

```text
scripts/build_section11_shorts_storyboard.py
experience/chapter04/section11/trailer/section11_shorts_timeline.vtt
experience/chapter04/section11/trailer/README.md
```

元画像は，既存の次の場所を参照します．

```text
experience/chapter04/section11/assets/images/
```

画像原本の複製や上書きは行いません．

## 必要なもの

- Python 3.10以降
- Pillow
- ffmpeg

Pillowの確認：

```powershell
python -c "import PIL; print(PIL.__version__)"
```

ffmpegの確認：

```powershell
ffmpeg -version
```

## 実行

リポジトリのルートで実行します．

```powershell
python scripts/build_section11_shorts_storyboard.py
```

## 出力

```text
experience/chapter04/section11/trailer/previews/
├─ shot_01_01.8s.png
├─ shot_02_05.5s.png
├─ shot_03_08.8s.png
├─ shot_04_11.8s.png
├─ shot_05_15.2s.png
├─ shot_06_17.4s.png
└─ shot_07_19.5s.png

experience/chapter04/section11/trailer/output/
└─ section11_trailer_ja_storyboard.mp4
```

## 最初の確認

まず7枚の縦型プレビューを確認します．

1. 第一景で同形の通知が見えるか．
2. 第二景で多関節の指と袖口が切れていないか．
3. 古地層が縦方向の時間として見えるか．
4. `A. K. I.` が大きすぎないか．
5. 第六景で二つの通知と指が同時に残るか．
6. テキストが右側のShorts操作UI領域へ入りすぎていないか．
7. 最終CTAが下端へ寄りすぎていないか．

## クロップ調整

スクリプト内の `SHOTS` にある `focus_x` と `focus_y` を0.0から1.0で調整します．

```python
Shot(7.0, 10.4, "scene02_old_application_1.png", 0.44, 0.62, ...)
```

- `focus_x` を小さくすると左側へ移動します．
- `focus_x` を大きくすると右側へ移動します．
- `focus_y` を小さくすると上側へ移動します．
- `focus_y` を大きくすると下側へ移動します．

## 注意

- 本ファイルは無音絵コンテです．
- 人物の顔や指をAI補間で動かしません．
- `I = 「私」` の示唆は追加しません．
- 元画像に含まれる疑似文字は背景情報として扱います．
- 最終版の作成前に，プレビュー，無音MP4，スマートフォン実機の順で確認します．
