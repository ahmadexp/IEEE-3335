#!/usr/bin/env python3
"""Generate a simple requirements index from active IEEE P3335 draft clauses."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ACTIVE_FILES = [
    "04 - Conformance/README.md",
    "05 - Architecture/README.md",
    "06 - Performance Specifications/README.md",
    "07 - Timing Interfaces/README.md",
    "08 - Control Interfaces/README.md",
    "09 - Environment/README.md",
]


def clause_id(path: Path) -> str:
    match = re.match(r"(\d{2})", path.name)
    if match:
        return match.group(1)
    return "XX"


def normalize(text: str) -> str:
    text = re.sub(r"\s+", " ", text.strip())
    return text.replace("|", "\\|")


def main() -> None:
    rows: list[tuple[str, str, int, str]] = []

    for rel in ACTIVE_FILES:
        path = ROOT / rel
        clause = clause_id(path.parent)
        counter = 1
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if "**shall** indicates" in line:
                continue
            if re.search(r"\bshall\b", line, re.IGNORECASE):
                req_id = f"P3335-{clause}-{counter:03d}"
                rows.append((req_id, rel, lineno, normalize(line)))
                counter += 1

    out = [
        "# IEEE P3335 Requirements Index",
        "",
        "This file is generated from active normative Markdown clauses by `scripts/requirements_index.py`.",
        "Regenerate it after normative edits.",
        "",
        "| ID | Source | Line | Requirement text |",
        "|----|--------|------|------------------|",
    ]

    for req_id, rel, lineno, text in rows:
        out.append(f"| {req_id} | `{rel}` | {lineno} | {text} |")

    (ROOT / "REQUIREMENTS_INDEX.md").write_text("\n".join(out) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
