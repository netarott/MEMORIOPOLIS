#!/usr/bin/env python3
"""Build Chapter 04 Section 09 Pages data from canonical source files.

Required canonical sources:
- five localized section09_*.md files
- section09-production-notes.md
- python/section09_time_model.py

Output:
- experience/chapter04/section09/data/section09.json

The output JSON is generated data. Do not edit it by hand.
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
PRODUCTION_NOTES_FILE: Final[str] = "section09-production-notes.md"
PYTHON_MODEL_FILE: Final[str] = "python/section09_time_model.py"
PYTHON_MODEL_TITLE: Final[str] = "Section 09 Time Model"
REQUIRED_TOP_LEVEL_KEYS: Final[tuple[str, ...]] = (
    "metadata", "titles", "content", "documents", "links"
)
HEADING_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$"
)


class BuildError(RuntimeError):
    """Raised when canonical input cannot safely produce a complete build."""


def find_repo_root(start: Path) -> Path:
    current = start.resolve()
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / "novel").is_dir() and (candidate / "experience").is_dir():
            return candidate
    raise BuildError(
        "repository root not found; run inside the MEMORIOPOLIS repository "
        "or pass --repo-root"
    )


def read_utf8(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError as exc:
        raise BuildError(f"UTF-8 decode failed: {path}") from exc
    except OSError as exc:
        raise BuildError(f"cannot read file: {path}") from exc


def extract_title_and_body(path: Path) -> tuple[str, str]:
    """Use the final heading in the opening heading block as the document title."""
    text = read_utf8(path)
    lines = text.splitlines(keepends=True)
    last_heading_index: int | None = None
    last_heading_text: str | None = None
    opening_block_started = False

    for index, line in enumerate(lines):
        value = line.rstrip("\r\n")
        if not value.strip():
            continue
        match = HEADING_PATTERN.match(value)
        if match:
            opening_block_started = True
            last_heading_index = index
            last_heading_text = match.group(2).strip()
            continue
        if opening_block_started:
            break
        raise BuildError(
            f"opening heading block not found before body content: {path} "
            f"(line {index + 1})"
        )

    if last_heading_index is None or not last_heading_text:
        raise BuildError(f"title not found: {path}")

    body_lines = lines[last_heading_index + 1 :]
    if body_lines and body_lines[0].strip() == "":
        body_lines = body_lines[1:]
    return last_heading_text, "".join(body_lines)


def require_files(source_dir: Path) -> None:
    required_names = [
        *LANGUAGE_FILES.values(),
        PRODUCTION_NOTES_FILE,
        PYTHON_MODEL_FILE,
    ]
    missing = [source_dir / name for name in required_names if not (source_dir / name).is_file()]
    if missing:
        formatted = "\n".join(f"  - {path}" for path in missing)
        raise BuildError(f"required canonical file(s) missing:\n{formatted}")


def build_document(source_dir: Path) -> dict[str, object]:
    require_files(source_dir)

    titles: dict[str, str] = {}
    content: dict[str, str] = {}
    for language, filename in LANGUAGE_FILES.items():
        title, body = extract_title_and_body(source_dir / filename)
        titles[language] = title
        content[language] = body

    notes_title, notes_body = extract_title_and_body(source_dir / PRODUCTION_NOTES_FILE)
    python_content = read_utf8(source_dir / PYTHON_MODEL_FILE)
    if not python_content.strip():
        raise BuildError(f"Python model is empty: {source_dir / PYTHON_MODEL_FILE}")

    document: dict[str, object] = {
        "metadata": {
            "chapter": 4,
            "section": 9,
            "slug": "section09",
            "localization_ready": (source_dir / "LOCALIZATION_READY").is_file(),
        },
        "titles": titles,
        "content": content,
        "documents": {
            "production_notes": {
                "source": PRODUCTION_NOTES_FILE,
                "title": notes_title,
                "content": notes_body,
            },
            "python_model": {
                "source": PYTHON_MODEL_FILE,
                "language": "python",
                "title": PYTHON_MODEL_TITLE,
                "content": python_content,
            },
        },
        "links": {
            "production_notes": "notes.html",
            "localization_review": "localization-review.md",
            "python_model": "observation.html",
        },
    }
    validate_document(document)
    return document


def validate_document(document: dict[str, object]) -> None:
    missing = [key for key in REQUIRED_TOP_LEVEL_KEYS if key not in document]
    if missing:
        raise BuildError("generated JSON is missing: " + ", ".join(missing))

    titles = document.get("titles")
    content = document.get("content")
    documents = document.get("documents")
    if not isinstance(titles, dict) or not isinstance(content, dict):
        raise BuildError("titles and content must be JSON objects")
    if set(titles) != set(LANGUAGE_FILES) or set(content) != set(LANGUAGE_FILES):
        raise BuildError("titles and content must contain exactly five languages")
    for language in LANGUAGE_FILES:
        if not isinstance(titles[language], str) or not titles[language].strip():
            raise BuildError(f"title is missing or empty: {language}")
        if not isinstance(content[language], str):
            raise BuildError(f"content is not text: {language}")

    if not isinstance(documents, dict):
        raise BuildError("documents must be a JSON object")

    notes = documents.get("production_notes")
    if not isinstance(notes, dict):
        raise BuildError("documents.production_notes is missing")
    for key in ("source", "title", "content"):
        if not isinstance(notes.get(key), str):
            raise BuildError(f"documents.production_notes.{key} must be text")
    if not notes["title"].strip():
        raise BuildError("documents.production_notes.title is empty")

    python_model = documents.get("python_model")
    if not isinstance(python_model, dict):
        raise BuildError("documents.python_model is missing")
    for key in ("source", "language", "title", "content"):
        if not isinstance(python_model.get(key), str):
            raise BuildError(f"documents.python_model.{key} must be text")
    if python_model["language"] != "python":
        raise BuildError("documents.python_model.language must be python")
    if not python_model["title"].strip() or not python_model["content"].strip():
        raise BuildError("Python model title and content must not be empty")


def write_json_atomic(document: dict[str, object], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = output_path.with_suffix(output_path.suffix + ".tmp")
    try:
        with temporary_path.open("w", encoding="utf-8", newline="\n") as handle:
            json.dump(document, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.replace(temporary_path, output_path)
    except OSError as exc:
        temporary_path.unlink(missing_ok=True)
        raise BuildError(f"cannot write output: {output_path}") from exc


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build Section 09 Pages JSON.")
    parser.add_argument("--repo-root", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_arguments()
    try:
        repo_root = args.repo_root.expanduser().resolve() if args.repo_root else find_repo_root(Path(__file__))
        source_dir = repo_root / "novel" / "chapter04" / "section09"
        output_path = (
            args.output.expanduser().resolve()
            if args.output
            else repo_root / "experience" / "chapter04" / "section09" / "data" / "section09.json"
        )
        if not source_dir.is_dir():
            raise BuildError(f"source directory not found: {source_dir}")

        document = build_document(source_dir)
        if args.check:
            print("Section 09 build check succeeded.")
            print(f"Source: {source_dir}")
            for language in LANGUAGE_FILES:
                print(
                    f"  {language}: title={document['titles'][language]!r}, "
                    f"body_chars={len(document['content'][language])}"
                )
            notes = document["documents"]["production_notes"]
            model = document["documents"]["python_model"]
            print(f"  production_notes: title={notes['title']!r}, body_chars={len(notes['content'])}")
            print(f"  python_model: source={model['source']!r}, code_chars={len(model['content'])}")
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
