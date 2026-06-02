#!/usr/bin/env python3
"""Check curated resource entries for basic consistency."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import parse_qsl, urlparse, urlunparse


LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
TRACKING_KEYS = {"fbclid", "gclid", "mc_cid", "mc_eid"}
MANUSCRIPT_HOST = "pre" + "prints.org"
FORBIDDEN_DOMAINS = {"www." + MANUSCRIPT_HOST, MANUSCRIPT_HOST}


def is_external_url(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def normalized_external_url(url: str) -> str:
    parsed = urlparse(url)
    return urlunparse(parsed._replace(fragment=""))


def tracking_query_keys(url: str) -> list[str]:
    parsed = urlparse(url)
    keys = []
    for key, _value in parse_qsl(parsed.query, keep_blank_values=True):
        if key.lower().startswith("utm_") or key.lower() in TRACKING_KEYS:
            keys.append(key)
    return keys


def check_awesome(root: Path = Path("awesome")) -> tuple[int, list[str]]:
    seen: dict[str, Path] = {}
    errors: list[str] = []
    checked = 0

    for file_path in sorted(root.rglob("*.md")):
        for line_no, line in enumerate(file_path.read_text(encoding="utf-8").splitlines(), start=1):
            stripped = line.strip()
            if not stripped.startswith("- ["):
                continue
            match = LINK_RE.search(stripped)
            if not match:
                errors.append(f"{file_path}:{line_no}: resource entry must include a Markdown link")
                continue
            title, url = match.group(1), match.group(2)

            if not is_external_url(url):
                continue

            checked += 1
            if ":" not in stripped.split(")", 1)[-1]:
                errors.append(f"{file_path}:{line_no}: resource entry must include a relevance note after the link")
            query_keys = tracking_query_keys(url)
            if query_keys:
                errors.append(f"{file_path}:{line_no}: tracking query parameters are not allowed: {', '.join(query_keys)}")
            parsed = urlparse(url)
            if parsed.netloc.lower() in FORBIDDEN_DOMAINS:
                errors.append(f"{file_path}:{line_no}: forbidden source domain: {parsed.netloc}")
            normalized_url = normalized_external_url(url)
            if normalized_url in seen:
                errors.append(f"{file_path}:{line_no}: duplicate resource URL also in {seen[normalized_url]}")
            seen[normalized_url] = file_path
            if not title.strip():
                errors.append(f"{file_path}:{line_no}: empty resource title")

    return checked, errors


def main(argv: list[str]) -> int:
    root = Path(argv[1]) if len(argv) > 1 else Path("awesome")
    checked, errors = check_awesome(root)
    print(f"checked {checked} awesome resources")
    for error in errors:
        print(error)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
