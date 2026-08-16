from pathlib import Path
import re
import sys


TARGETS = [
    Path("novel"),
]

errors = []


def report(path: Path, line_no: int, message: str, line: str) -> None:
    errors.append(
        f"{path}:{line_no}: {message}\n"
        f"    {line.rstrip()}"
    )


def check_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    in_code_block = False

    for line_no, line in enumerate(lines, start=1):
        stripped = line.strip()

        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue

        if in_code_block:
            continue

        # note専用のインライン数式を禁止
        if re.search(r"\$\$\{.+?\}\$\$", line):
            report(
                path,
                line_no,
                "note専用の $${...}$$ が含まれています",
                line,
            )

        # LaTeXコマンドの二重バックスラッシュを検出
        if re.search(
            r"\\\\(?:delta|mathrm|tau|rho|sigma|alpha|beta|gamma)",
            line,
        ):
            report(
                path,
                line_no,
                "LaTeXコマンドのバックスラッシュが二重です",
                line,
            )

        # ブロック数式
        if "$$" in line:
            if not re.fullmatch(r"\s*\$\$.+\$\$\s*", line):
                report(
                    path,
                    line_no,
                    "ブロック数式は $$...$$ の一行形式にしてください",
                    line,
                )
            continue

        # インライン数式を抽出
        for match in re.finditer(r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)", line):
            start, end = match.span()

            before[(path: Path, line_no: int, message: str, line: str) -> None:
.append(
"{path}:{line_no}: {message}\n"
"    {line.rstrip()後に半角スペースを要求
            if start > 0 and before != " ":
                report(
                    path,
                    line_no,
                    "インライン数式の直前に半角スペースがありません",
                    line,
                )

            if end < len(line) and after != " ":
                report(
                    path,
                    line_no,
                    "インライン数式の直後に半角スペースがありません",
                    line,
                )

            expression = match.group(1)

            if expression.startswith(" ") or expression.endswith(" "):
                report(
                    path,
                    line_no,
                    "数式の $ の内側には空白を入れないでください",
                    line,
                )

            if "\\\\" in expression:
                report(
                    path,
                    line_no,
                    "数式内に二重バックスラッシュがあります",
                    line,
                )


def main() -> int:
    markdown_files = []

    for target in TARGETS:
        if target.exists():
            markdown_files.extend(target.rglob("*.md"))

    if not markdow*_files:
        print("No Markdown*files found.")
        return 0

 *  for path in sorted(markdown_file*):
        check_file(path)

    i* errors:
        print("Markdown m*th style check failed.\n")
       *print("\n\n".join(errors))
       *print(f"\nTotal errors: {len(error*)}")
        return 1

    print(
*       f"Markdown math style check*passed: "
        f"{len(markdown_*iles)} files checked."
    )
    r*turn 0


if __name__ == "__main__"*
    sys.exit(main())