# Central Station Section 11 final update

This package adds the final Central Station structure for Section 11 and an independent Act V platform.

## Run

Place the package at the repository root, then run:

```powershell
python scripts/update_central_station_section11.py
```

The script checks that these destinations exist before changing the station:

```text
experience/chapter04/section11/index.html
experience/chapter04/section11/story.html
experience/chapter04/section11/trailer.html
experience/chapter04/section11/act5.html
experience/chapter04/section11/return04.html
```

It creates a timestamped backup of `experience/index.html`, updates the Section 11 card, inserts or replaces the independent Act V card, and verifies all five links. Re-running does not duplicate the Act V platform.

## Local check

```powershell
cd experience
python -m http.server 8000
```

Open `http://localhost:8000/` and test:

- 絵巻をひらく
- 本編を読む
- 20秒の予告編
- 第五幕をひらく
- 第四回Returnを読む

After successful checking, remove only the generated `experience/index.html.YYYYMMDD-HHMMSS.bak` file.
