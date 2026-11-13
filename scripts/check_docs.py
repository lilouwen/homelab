#!/usr/bin/env python3
"""Validate relative Markdown and HTML links without network access or dependencies."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

REPO = Path(__file__).resolve().parents[1]
FENCE = re.compile(r"(?ms)^([ \t]*)(?:\x60{3,}|~{3,})[^\n]*\n.*?^\1(?:\x60{3,}|~{3,})[ \t]*$")
INLINE = re.compile(r"\]\(([^)\n]+)\)")
REFERENCE = re.compile(r"(?m)^\s{0,3}\[[^\]]+\]:\s*(\S+)")
IGNORED_PREFIXES = ("http:", "https:", "mailto:", "tel:", "data:", "//")


class Links(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.targets: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag not in ("a", "img", "source"):
            return
        for key, value in attrs:
            if key in ("href", "src", "srcset") and value:
                # srcset values have optional density descriptors.
                values = [part.strip().split()[0] for part in value.split(",")] if key == "srcset" else [value]
                self.targets.extend(values)


def remove_fenced_code(text: str) -> str:
    return FENCE.sub("", text)


def is_local(target: str) -> bool:
    clean = target.strip().strip("<>")
    return bool(clean) and not clean.startswith(("#", *IGNORED_PREFIXES)) and not re.match(
        r"^[a-zA-Z][a-zA-Z0-9+.-]*:", clean
    )


def local_path(source: Path, target: str) -> Path | None:
    if not is_local(target):
        return None

    raw = target.strip().strip("<>")
    parsed = urlsplit(raw)
    if not parsed.path:
        return None

    name = unquote(parsed.path)
    candidate = (REPO / name.lstrip("/")) if name.startswith("/") else (source.parent / name)
    return candidate.resolve()


def validate() -> int:
    errors: list[str] = []
    markdown_files = sorted(path for path in REPO.rglob("*.md") if ".git" not in path.parts)
    checked = 0

    for file in markdown_files:
        body = remove_fenced_code(file.read_text(encoding="utf-8"))
        targets = INLINE.findall(body) + REFERENCE.findall(body)
        parser = Links()
        parser.feed(body)
        targets.extend(parser.targets)

        for target in targets:
            # Markdown links with an optional quoted title.
            if ' "' in target or " '" in target:
                target = re.split(r"\s+[\"']", target, maxsplit=1)[0]
            path = local_path(file, target)
            if path is None:
                continue
            checked += 1
            try:
                path.relative_to(REPO)
            except ValueError:
                errors.append(f"{file.relative_to(REPO)}: link escapes repository: {target}")
                continue
            if not path.exists():
                errors.append(f"{file.relative_to(REPO)}: missing local target: {target}")

    print(f"Checked {len(markdown_files)} Markdown files and {checked} local links.")
    for message in errors:
        print("ERROR:", message, file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(validate())
