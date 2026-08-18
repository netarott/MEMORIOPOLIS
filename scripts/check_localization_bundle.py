from __future__ import annotations

from pathlib import Path
import re
import sys

LANGUAGES = ("ja", "en", "zh-TW", "ko", "ru")
SECTION_PATTERN = re.compile(r"^section(?P<number>\d{2})_ja\.md$")
INLINE_MATH = re.compile(r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)")
BLOCK_MATH = re.compile(r"\$\$(.+?)\$\$")
FENCED_PYTHON = re.compile(r"```python\s*\n(.*?)\n```", re.DOTALL)


def normalize_math(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip())


def extract_math(text: str) -> list[str]:
    values = [normalize_math(v) for v in BLOCK_MATH.findall(text)]
    text_without_blocks = BLOCK_MATH.sub("", text)
    values.extend(normalize_math(v) for v in INLINE_MATH.findall(text_without_blocks))
    return values


def extract_python(text: str) -> list[str]:
    return [block.strip() for block in FENCED_PYTHON.findall(text)]


def check_section(ja_file: Path) -> list[str]:
    section_dir = ja_file.parent
    section_number = SECTION_PATTERN.fullmatch(ja_file.name).group("number")
    marker = section_dir / "LOCALIZATION_READY"
    messages: list[str] = []

    existing = {
        language: section_dir / f"section{section_number}_{language}.md"
        for language in LANGUAGES
    }

    missing = [language for language, path in existing.items() if not path.exists()]

    if missing and marker.exists():
        messages.append(
            f"ERROR {section_dir}: missing localized editions: {', '.join(missing)}"
        )
        return messages

    if missing:
        messages.append(
            f"INFO  {section_dir}: localization is incomplete; missing: {', '.join(missing)}"
        )
        return messages

    texts: dict[str, str] = {}
    for language, path in existing.items():
        try:
            texts[language] = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            messages.append(f"ERROR {path}: file is not valid UTF-8")
            return messages

    ja_math = extract_math(texts["ja"])
    ja_python = extract_python(texts["ja"])

    for language in LANGUAGES[1:]:
        math_values = extract_math(texts[language])
        python_values = extract_python(texts[language])

        if math_values != ja_math:
            messages.append(
                f"ERROR {existing[language]}: mathematical expressions differ from Japanese canon"
            )

        if python_values != ja_python:
            messages.append(
                f"ERROR {existing[language]}: Python code blocks differ from Japanese canon"
            )

    if not any(message.startswith("ERROR") for message in messages):
        messages.append(
            f"PASS  {section_dir}: five editions present; math and Python blocks aligned"
        )

    return messages


def main() -> int:
    novel_root = Path("novel")
    if not novel_root.exists():
        print("ERROR novel directory was not found")
        return 1

    ja_files = sorted(
        path for path in novel_root.rglob("section??_ja.md")
        if SECTION_PATTERN.fullmatch(path.name)
    )

    if not ja_files:
        print("INFO no canonical Japanese section files found")
        return 0

    messages: list[str] = []
    for ja_file in ja_files:
        messages.extend(check_section(ja_file))

    print("\n".join(messages))
    errors = [message for message in messages if message.startswith("ERROR")]
    print(f"\nChecked sections: {len(ja_files)}; errors: {len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
