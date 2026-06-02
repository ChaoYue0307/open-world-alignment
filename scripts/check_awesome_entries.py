#!/usr/bin/env python3
"""Check curated resource entries for basic consistency."""

from __future__ import annotations

import re
import sys
from pathlib import Path


LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


def main() -> int:
    seen: dict[str, Path] = {}
    errors: list[str] = []

    for file_path in sorted(Path("awesome").glob("*.md")):
        for line_no, line in enumerate(file_path.read_text(encoding="utf-8").splitlines(), start=1):
            stripped = line.strip()
            if not stripped.startswith("- ["):
                continue
            match = LINK_RE.search(stripped)
            if not match:
                errors.append(f"{file_path}:{line_no}: resource entry must include a Markdown link")
                continue
            title, url = match.group(1), match.group(2)
            if ":" not in stripped.split(")", 1)[-1]:
                errors.append(f"{file_path}:{line_no}: resource entry must include a relevance note after the link")
            if url in seen:
                errors.append(f"{file_path}:{line_no}: duplicate resource URL also in {seen[url]}")
            seen[url] = file_path
            if not title.strip():
                errors.append(f"{file_path}:{line_no}: empty resource title")

    print(f"checked {len(seen)} awesome resources")
    for error in errors:
        print(error)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
