#!/usr/bin/env python3
"""Build the Chapter 04 Section 09 Pages data from five canonical Markdown files.

The Markdown files under novel/chapter04/section09 are the single source of
truth. This script extracts the first level-1 heading as each language title,
preserves the remaining Markdown body, reads LOCALIZATION_READY as a status
marker, and writes experience/chapter04/section09/data/section09.json.

The generated JSON is a build artifact. Do not edit it by hand.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Final

LANGUAGE_FILES: Final[dict[str, str]] = {
    "ja": "section09_ja.md",
    "en": "section09_en.md",
    "zh-TW": "section09_zh-TW.md",
    "ko": "section09_ko.md",
    "ru": "section09_ru.md",
}

REQUIRED_TOP_LEVEL_KEYS: Final[tuple[str, ...]] = (
    "metadata",
    "titles",
    "content",
    "links",
)

HEADING_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$"
)
FENCE_PATTERN: Final[re.Pattern[str]] = re.compile(r"^\s*(`{3,}|~{3,})")


class BuildError(RuntimeError):
    """Raised when canonical input cannot safely produce a complete build."""


def find_repo_root(start: Path) -> Path:
    """Find a repository root containing both novel/ and experience/."""
    current = start.resolve()
    if current.is_file():
        current = current.parent

    for candidate in (current, *current.parents):
        if (candidate / "novel").is_dir() and (candidate / "experience").is_dir():
            return candidate

    raise BuildError(
        "repository root not found; run the script inside the MEMORIOPOLIS "
        "repository or pass --repo-root"
    )


def extract_title_and_body(path: Path) -> tuple[str, str]:
    """Extract the last heading in the opening heading block and its body.

    Canonical Section 09 files begin with a hierarchy such as work title,
    chapter title, and section title. Blank lines may occur between those
    headings. The final heading before the first prose or other body element is
    therefore used as the section title. The heading level itself is not
    interpreted, and fenced code content is never treated as a heading.
    """
    try:
        text = path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError as exc:
        raise BuildError(f"UTF-8 decode failed: {path}") from exc
    except OSError as exc:
        raise BuildError(f"cannot read file: {path}") from exc

    lines = text.splitlines(keepends=True)
    last_heading_index: int | None = None
    last_heading_text: str | None = None
    opening_block_started = False

    for index, line in enumerate(lines):
        line_without_eol = line.rstrip("\r\n")

        if not line_without_eol.strip():
            continue

        heading_match = HEADING_PATTERN.match(line_without_eol)
        if heading_match:
            opening_block_started = True
            last_heading_index = index
            last_heading_text = heading_match.group(2).strip()
            continue

        # The first nonblank, non-heading line starts the body. Anything after
        # this point belongs to the body and must not affect title extraction.
        if opening_block_started:
            break

        # A canonical file must begin, apart from blank lines, with its heading
        # hierarchy. Front matter or prose before the first heading is rejected
        # rather than silently interpreted.
        raise BuildError(
            f"opening heading block not found before body content: {path} "
            f"(line {index + 1})"
        )

    if last_heading_index is None or last_heading_text is None:
        raise BuildError(f"title not found: {path}")
    if not last_heading_text:
        raise BuildError(f"title is empty: {path}")

    body_lines = lines[last_heading_index + 1 :]
    if body_lines and body_lines[0].strip() == "":
        body_lines = body_lines[1:]
    body = "".join(body_lines)
    return last_heading_text, body


def build_document(source_dir: Path) -> dict[str, object]:
    """Read all canonical inputs and construct the Section 09 JSON document."""
    missing = [
        source_dir / filename
        for filename in LANGUAGE_FILES.values()
        if not (source_dir / filename).is_file()
    ]
    if missing:
        formatted = "\n".join(f"  - {path}" for path in missing)
        raise BuildError(f"required language file(s) missing:\n{formatted}")

    titles: dict[str, str] = {}
    content: dict[str, str] = {}

    for language, filename in LANGUAGE_FILES.items():
        title, body = extract_title_and_body(source_dir / filename)
        titles[language] = title
        content[language] = body

    document: dict[str, object] = {
        "metadata": {
            "chapter": 4,
            "section": 9,
            "slug": "section09",
            "localization_ready": (source_dir / "LOCALIZATION_READY").is_file(),
        },
        "titles": titles,
        "content": content,
        "links": {
            "production_notes": "section09-production-notes.md",
            "localization_review": "localization-review.md",
            "python_model": "python/section09_time_model.py",
        },
    }

    validate_document(document)
    return document


def validate_document(document: dict[str, object]) -> None:
    """Validate the required structure before writing any output."""
    missing_keys = [key for key in REQUIRED_TOP_LEVEL_KEYS if key not in document]
    if missing_keys:
        raise BuildError(
            "generated JSON is missing top-level key(s): " + ", ".join(missing_keys)
        )

    titles = document.get("titles")
    content = document.get("content")
    if not isinstance(titles, dict) or not isinstance(content, dict):
        raise BuildError("titles and content must be JSON objects")

    expected_languages = set(LANGUAGE_FILES)
    if set(titles) != expected_languages:
        raise BuildError("titles do not contain exactly the five required languages")
    if set(content) != expected_languages:
        raise BuildError("content does not contain exactly the five required languages")

    for language in LANGUAGE_FILES:
        if not isinstance(titles[language], str) or not titles[language].strip():
            raise BuildError(f"title is missing or empty for language: {language}")
        if not isinstance(content[language], str):
            raise BuildError(f"content is not text for language: {language}")


def write_json_atomic(document: dict[str, object], output_path: Path) -> None:
    """Write UTF-8 JSON atomically so a failed build cannot corrupt prior output."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = output_path.with_suffix(output_path.suffix + ".tmp")

    try:
        with temporary_path.open("w", encoding="utf-8", newline="\n") as handle:
            json.dump(document, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.replace(temporary_path, output_path)
    except OSError as exc:
        try:
            temporary_path.unlink(missing_ok=True)
        except OSError:
            pass
        raise BuildError(f"cannot write output: {output_path}") from exc


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build Chapter 04 Section 09 JSON from the five canonical Markdown files."
        )
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        help="MEMORIOPOLIS repository root; auto-detected when omitted",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help=(
            "optional output path; defaults to "
            "experience/chapter04/section09/data/section09.json"
        ),
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="validate and print a summary without writing section09.json",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_arguments()

    try:
        repo_root = (
            args.repo_root.expanduser().resolve()
            if args.repo_root
            else find_repo_root(Path(__file__))
        )
        source_dir = repo_root / "novel" / "chapter04" / "section09"
        output_path = (
            args.output.expanduser().resolve()
            if args.output
            else repo_root
            / "experience"
            / "chapter04"
            / "section09"
            / "data"
            / "section09.json"
        )

        if not source_dir.is_dir():
            raise BuildError(f"source directory not found: {source_dir}")

        document = build_document(source_dir)

        if args.check:
            print("Section 09 build check succeeded.")
            print(f"Source: {source_dir}")
            for language in LANGUAGE_FILES:
                title = document["titles"][language]  # type: ignore[index]
                body = document["content"][language]  # type: ignore[index]
                print(f"  {language}: title={title!r}, body_chars={len(body)}")
            return 0

        write_json_atomic(document, output_path)
        print("Section 09 build succeeded.")
        print(f"Source: {source_dir}")
        print(f"Output: {output_path}")
        return 0

    except BuildError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
