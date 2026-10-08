# MEMORIOPOLIS Spanish Core20

## 基本仕様

- 言語基準: スペイン本国スペイン語（es-ES）
- Essay正本: `E0001_es.md`
- 対象Concept: C0011-C0020
- ノートタイプ: `MEMORIOPOLIS Spanish Vocabulary`
- フィールド数: 19
- CourseTags: `memoriopolis::es::core20`
- TTS: `es_ES`

## ファイル

- `es_core20_master_19fields.csv`: ヘッダー付き正本
- `es_core20_anki_19fields.csv`: ヘッダーなしAnkiインポート用

## Ankiインポート

1. ノートタイプを `MEMORIOPOLIS Spanish Vocabulary` にする。
2. 文字コードは UTF-8。
3. 区切り文字はカンマ。
4. フィールド順を19フィールドへ一致させる。
5. HTMLを許可する。
6. `ConceptScene`は19番目。
7. Core20共通画像10枚がAnkiメディアに存在することを確認する。

## ConceptScene

```text
C0011 memoriopolis_c0011_exist.webp
C0012 memoriopolis_c0012_do.webp
C0013 memoriopolis_c0013_have.webp
C0014 memoriopolis_c0014_send.webp
C0015 memoriopolis_c0015_receive.webp
C0016 memoriopolis_c0016_hear.webp
C0017 memoriopolis_c0017_search.webp
C0018 memoriopolis_c0018_move.webp
C0019 memoriopolis_c0019_connect.webp
C0020 memoriopolis_c0020_bound.webp
```

CSVのConceptScene列にはAnki用の`<img src="...">`を格納している。画像がメディア領域に存在すれば、インポート後に自動表示される。

## Concept境界

- `existir` / `hay` / `estar`
- `hacer` / `crear` / `realizar`
- `tener` / `poseer` / `mantener`
- `enviar` / `mandar`
- `recibir` / `aceptar` / `recoger`
- `oír` / `escuchar`
- `buscar` / `encontrar` / `investigar`
- `cambiar` / `mudarse` / `desplazarse`
- `conectarse` / `estar conectado` / `vincularse`
- `estar atado` / `estar vinculado` / `depender de`
