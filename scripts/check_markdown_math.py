from pathlib import Path
import re
import sys

TARGETS = [Path("novel")]
errors: list[str] = []


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

        # Reject note-specific inline math such as $${\delta}$$.
        if re.search(r"\$\$\{.+?\}\$\$", line):
            report(
                path,
                line_no,
                "note-specific inline math $${...}$$ is not allowed",
                line,
            )

        # Block math must be written on one line as $$...$$.
        if "$$" in line:
            if not re.fullmatch(r"\s*\$\$.+\$\$\s*", line):
                report(
                    path,
                    line_no,
                    "block math must use the one-line form $$...$$",
                    line,
                )
            continue

        # Inspect inline math delimited by single dollar signs.
        for match in re.finditer(
            r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)", line
        ):
            start, end = match.span()
            before = line[start - 1] if start > 0 else ""
            after = line[end] if end < len(line) else ""
            expression = match.group(1)

            if start > 0 and before != " ":
                report(
                    path,
                    line_no,
                    "add an ASCII space before inline math",
                    line,
                )

            if end < len(line) and after != " ":
                report(
                    path,
                    line_no,
                    "add an ASCII space after inline math",
                    line,
                )

            if expression.startswith(" ") or expression.endswith(" "):
                report(
                    path,
                    line_no,
                    "do not add spaces inside math delimiters",
                    line,
                )

            if "\\\\" in expression:
                report(
                    path,
                    line_no,
                    "a LaTeX command contains a doubled backslash",
                    line,
                )

    if in_code_block:
        report(
            path,
            len(lines),
            "an opening fenced code block is not closed",
            lines[-1] if lines else "",
        )


def main() -> int:
    markdown_files: list[Path] = []

    for target in TARGETS:
        if target.exists():
            markdown_files.extend(target.rglob("*.md"))

    if not markdown_files:
        print("No Markdown files found.")
        return 0

    for path in sorted(markdown_files):
        check_file(path)

    if errors:
        print("Markdown math style check failed.\n")
        print("\n\n".join(errors))
        print(f"\nTotal errors: {len(errors)}")
        return 1

    print(
        "Markdown math style check passed: "
        f"{len(markdown_files)} files checked."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
