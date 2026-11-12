#!/usr/bin/env python3
"""Generate or verify the editorial requirements index for IEEE P3335."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "REQUIREMENTS_INDEX.md"
ACTIVE_FILES = [
    "04 - Conformance/README.md",
    "05 - Architecture/README.md",
    "06 - Performance Specifications/README.md",
    "07 - Timing Interfaces/README.md",
    "08 - Control Interfaces/README.md",
    "09 - Environment/README.md",
]
SHALL_RE = re.compile(r"\bshall\b", re.IGNORECASE)
LIST_RE = re.compile(r"^\s*(?:[-*]|\d+\.)\s+(.*)$")
TABLE_SEPARATOR_RE = re.compile(r"^\s*\|?(?:\s*:?-+:?\s*\|)+\s*$")


@dataclass(frozen=True)
class Requirement:
    source: str
    line: int
    section: str
    text: str
    shall_occurrences: int


def clause_id(relative_path: str) -> str:
    match = re.match(r"(\d{2})", relative_path)
    return match.group(1) if match else "XX"


def normalize(text: str) -> str:
    text = re.sub(r"\s+", " ", text.strip())
    return re.sub(r"\*\*(shall)\*\*", r"\1", text, flags=re.IGNORECASE)


def table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def following_items(lines: list[str], start: int) -> list[tuple[int, str]]:
    index = start + 1
    while index < len(lines) and not lines[index].strip():
        index += 1

    if index >= len(lines):
        return []

    first_list = LIST_RE.match(lines[index])
    if first_list:
        items: list[tuple[int, str]] = []
        while index < len(lines):
            match = LIST_RE.match(lines[index])
            if not match:
                break
            items.append((index + 1, match.group(1).strip()))
            index += 1
        return items

    if lines[index].lstrip().startswith("|"):
        table_lines: list[tuple[int, str]] = []
        while index < len(lines) and lines[index].lstrip().startswith("|"):
            table_lines.append((index + 1, lines[index]))
            index += 1
        if len(table_lines) < 3 or not TABLE_SEPARATOR_RE.match(table_lines[1][1]):
            return []
        return [
            (line_number, "; ".join(table_cells(line)))
            for line_number, line in table_lines[2:]
            if not TABLE_SEPARATOR_RE.match(line)
        ]

    return []


def extract_requirements(relative_path: str) -> tuple[list[Requirement], int]:
    path = ROOT / relative_path
    lines = path.read_text(encoding="utf-8").splitlines()
    requirements: list[Requirement] = []
    source_shall_count = 0
    section = ""

    def record(number: int, statement: str) -> None:
        requirements.append(Requirement(relative_path, number, section, normalize(statement),
                                        len(SHALL_RE.findall(statement))))

    for index, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("#"):
            section = stripped.lstrip("#").strip()

        occurrences = len(SHALL_RE.findall(line))
        if not occurrences:
            continue

        source_shall_count += occurrences
        if stripped.startswith("|"):
            cells = table_cells(stripped)
            for cell in cells:
                if SHALL_RE.search(cell):
                    record(index + 1, f"{cells[0]}: {cell}" if cell != cells[0] else cell)
            continue

        clean_line = normalize(LIST_RE.sub(r"\1", stripped))
        sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z`*])", clean_line)
        for statement in sentences:
            if not SHALL_RE.search(statement):
                continue
            # Only the lead-in governs implied items. Explicit child obligations
            # are indexed on their own lines; a parent may also require inheritance.
            if statement.endswith(":"):
                items = following_items(lines, index)
                implied = [(n, item) for n, item in items if not SHALL_RE.search(item)]
                if implied:
                    for number, item in implied:
                        record(number, f"{statement} {item}")
                if items and len(implied) == len(items):
                    continue
            record(index + 1, statement)

    return requirements, source_shall_count


def render() -> tuple[str, int, int]:
    all_requirements: list[tuple[str, Requirement]] = []
    source_shall_count = 0

    for relative_path in ACTIVE_FILES:
        requirements, file_shall_count = extract_requirements(relative_path)
        source_shall_count += file_shall_count
        clause = clause_id(relative_path)
        for counter, requirement in enumerate(requirements, 1):
            all_requirements.append((f"P3335-{clause}-{counter:03d}", requirement))

    output = [
        "# IEEE P3335 Requirements Index",
        "",
        "This editorial index is generated from the active normative Markdown clauses by `scripts/requirements_index.py`. It is not part of the standard and does not replace the controlling clause text. Generated identifiers can change when requirements are added, removed, or reordered.",
        "",
        f"Source `shall` occurrences: **{source_shall_count}**. Indexed requirement statements: **{len(all_requirements)}**. A framing requirement followed by a list or table is expanded into one row per item.",
        "",
        "| ID | Section | Source | Line | Requirement text |",
        "|----|---------|--------|------|------------------|",
    ]

    for requirement_id, requirement in all_requirements:
        cell_text = requirement.text.replace("|", "\\|")
        output.append(
            f"| {requirement_id} | {normalize(requirement.section)} | "
            f"`{requirement.source}` | {requirement.line} | {cell_text} |"
        )

    return "\n".join(output) + "\n", source_shall_count, len(all_requirements)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if REQUIREMENTS_INDEX.md is not current",
    )
    args = parser.parse_args()

    content, shall_count, requirement_count = render()
    if args.check:
        current = OUTPUT.read_text(encoding="utf-8") if OUTPUT.exists() else ""
        if current != content:
            print(
                "REQUIREMENTS_INDEX.md is out of date; run "
                "`python3 scripts/requirements_index.py`.",
                file=sys.stderr,
            )
            return 1
        print(
            f"Requirements index is current: {requirement_count} statements "
            f"from {shall_count} source shall occurrences."
        )
        return 0

    OUTPUT.write_text(content, encoding="utf-8")
    print(
        f"Wrote {OUTPUT.relative_to(ROOT)} with {requirement_count} statements "
        f"from {shall_count} source shall occurrences."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
