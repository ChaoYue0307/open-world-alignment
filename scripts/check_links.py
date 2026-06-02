#!/usr/bin/env python3
"""Check local Markdown links."""

from __future__ import annotations

import re
import sys
from pathlib import Path


LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def main() -> int:
    bad: list[str] = []
    checked = 0
    for file_path in Path(".").rglob("*.md"):
        if ".git" in file_path.parts:
            continue
        text = file_path.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = match.group(1).split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            checked += 1
            if not (file_path.parent / target).exists():
                bad.append(f"{file_path}: {match.group(1)}")

    print(f"checked {checked} local markdown links")
    for item in bad:
        print(f"broken {item}")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
