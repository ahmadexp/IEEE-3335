#!/usr/bin/env python3
"""Run lightweight editorial and consistency checks on the active P3335 draft."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT_FILES = [
    ROOT / "00 - Front Matter/README.md",
    *[ROOT / f"{number:02d} - {name}/README.md" for number, name in [
        (1, "Overview"),
        (2, "Normative References"),
        (3, "Definitions, Acronyms and Abbreviations"),
        (4, "Conformance"),
        (5, "Architecture"),
        (6, "Performance Specifications"),
        (7, "Timing Interfaces"),
        (8, "Control Interfaces"),
        (9, "Environment"),
        (10, "Applications and Best Practices"),
    ]],
    ROOT / "Annex A - Metrics/README.md",
    ROOT / "Annex B - Test Procedures/README.md",
    ROOT / "Annex C - Bibliography/README.md",
    ROOT / "Annex D - Conformance Statement Proforma/README.md",
    ROOT / "Annex E - Host Operating-System Integration/README.md",
]
NORMATIVE_FILES = MANUSCRIPT_FILES[4:10]
INFORMATIVE_TECHNICAL_FILES = [MANUSCRIPT_FILES[10], *MANUSCRIPT_FILES[11:]]
DOCUMENT_STRUCTURE_LABELS = [
    *[f"Clause {number}" for number in range(1, 11)],
    *[f"Annex {letter}" for letter in "ABCDE"],
]
CONTROL_STATUS_TERMS = (
    "fault",
    "stale",
    "unavailable",
    "unknown",
    "unspecified",
    "unsupported",
    "valid",
)
PLACEHOLDER_RE = re.compile(
    r"\b(?:TODO|TBD|FIXME)\b|editor(?:'s)? note|<<|>>", re.IGNORECASE
)
SHALL_RE = re.compile(r"\bshall\b", re.IGNORECASE)
UNBOLDED_SHALL_RE = re.compile(r"(?<!\*\*)\bshall\b(?!\*\*)", re.IGNORECASE)
MUST_RE = re.compile(r"\bmust\b", re.IGNORECASE)
ACCURACY_RE = re.compile(r"\baccuracy\b", re.IGNORECASE)
QUALIFIED_ACCURACY_RE = re.compile(
    r"\b(?:TimeCard timestamp|timestamp|time|frequency|qualified|unqualified)[ -]\*{0,2}accuracy\b",
    re.IGNORECASE,
)
CONTROL_OBJECT_RE = re.compile(r"^\|\s*`([A-Z][A-Z0-9_]+)`\s*\|")
NORMATIVE_REFERENCE_MARKERS = [
    "IPMI Specification, Version 2.0, Revision 1.1",
    "IEEE Std 1139-2022",
    "IEEE Std 1193-2022",
    "IEEE Std 1588-2019",
    "IEEE Std 802.1AS-2025",
    "IETF RFC 3411",
    "IETF RFC 5905",
    "IRIG Standard 200-16",
    "ITU-T Recommendation G.703 (04/2016)",
    "ITU-T Recommendation G.810 (08/1996)",
    "ITU-T Recommendation G.8260 (11/2022)",
    "I3C Basic",
    "PCI Express Base Specification, Revision 5.0, Version 1.0",
    "SMBus",
]


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def main() -> int:
    errors: list[str] = []

    for path in MANUSCRIPT_FILES:
        if not path.exists():
            errors.append(f"missing manuscript source: {relative(path)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    texts = {path: path.read_text(encoding="utf-8") for path in MANUSCRIPT_FILES}

    discovered_files = sorted(
        path
        for path in ROOT.glob("*/README.md")
        if re.match(r"(?:\d{2}|Annex)", path.parent.name)
    )
    expected_files = set(MANUSCRIPT_FILES)
    for path in sorted(set(discovered_files) - expected_files):
        errors.append(f"unexpected active manuscript source: {relative(path)}")

    overview_text = texts[MANUSCRIPT_FILES[1]]
    for label in DOCUMENT_STRUCTURE_LABELS:
        if not re.search(rf"^\|\s*{re.escape(label)}\s*\|", overview_text, re.MULTILINE):
            errors.append(f"Clause 1 document structure is missing {label}")

    definitions_text = texts[MANUSCRIPT_FILES[3]]
    for term in CONTROL_STATUS_TERMS:
        if f"- **{term}:**" not in definitions_text:
            errors.append(f"Clause 3 is missing control-status definition: {term}")

    for path, text in texts.items():
        for line_number, line in enumerate(text.splitlines(), 1):
            if PLACEHOLDER_RE.search(line):
                errors.append(f"{relative(path)}:{line_number}: unresolved placeholder")
            if MUST_RE.search(line) and "The term **must**" not in line:
                errors.append(f"{relative(path)}:{line_number}: use shall/should/may/can instead of must")
            accuracy_text = QUALIFIED_ACCURACY_RE.sub("", line)
            if ACCURACY_RE.search(accuracy_text):
                errors.append(
                    f"{relative(path)}:{line_number}: qualify accuracy by measurement context"
                )
            if UNBOLDED_SHALL_RE.search(line):
                errors.append(f"{relative(path)}:{line_number}: shall is not bold")

    for path in INFORMATIVE_TECHNICAL_FILES:
        for line_number, line in enumerate(texts[path].splitlines(), 1):
            if SHALL_RE.search(line):
                errors.append(
                    f"{relative(path)}:{line_number}: shall appears in informative technical material"
                )

    reference_entries = re.findall(
        r"^- \[(\d+)\] (.+)$", texts[MANUSCRIPT_FILES[2]], re.MULTILINE
    )
    reference_ids = [int(number) for number, _ in reference_entries]
    if reference_ids != list(range(1, len(NORMATIVE_REFERENCE_MARKERS) + 1)):
        errors.append("Clause 2 reference identifiers are missing, duplicated, or out of order")
    entries_by_id = {int(number): entry.replace("**", "") for number, entry in reference_entries}
    for number, marker in enumerate(NORMATIVE_REFERENCE_MARKERS, 1):
        if marker not in entries_by_id.get(number, ""):
            errors.append(f"Clause 2 reference [{number}] does not match cited source: {marker}")

    normative_text = "\n".join(texts[path] for path in NORMATIVE_FILES)
    for marker in NORMATIVE_REFERENCE_MARKERS:
        if marker not in normative_text:
            errors.append(f"Clause 2 reference is not normatively cited: {marker}")

    for reference_number in range(1, len(NORMATIVE_REFERENCE_MARKERS) + 1):
        identifier = f"[{reference_number}]"
        if identifier not in normative_text:
            errors.append(f"Clause 2 reference is not cited by identifier: {identifier}")

    front_matter = texts[MANUSCRIPT_FILES[0]].lower()
    for phrase in ("unapproved draft", "subject to change", "conformance or compliance"):
        if phrase not in front_matter:
            errors.append(f"front matter is missing draft-status phrase: {phrase}")

    control_objects: dict[str, int] = {}
    control_path = ROOT / "08 - Control Interfaces/README.md"
    for line_number, line in enumerate(texts[control_path].splitlines(), 1):
        match = CONTROL_OBJECT_RE.match(line)
        if not match:
            continue
        name = match.group(1)
        if name in control_objects:
            errors.append(
                f"{relative(control_path)}:{line_number}: duplicate control object {name} "
                f"(first defined at line {control_objects[name]})"
            )
        control_objects[name] = line_number

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    shall_count = sum(
        len(SHALL_RE.findall(line))
        for path in NORMATIVE_FILES
        for line in texts[path].splitlines()
        if "**shall** indicates" not in line
    )
    print(
        f"Draft checks passed: {len(MANUSCRIPT_FILES)} sources, "
        f"{shall_count} normative shall occurrences, "
        f"{len(NORMATIVE_REFERENCE_MARKERS)} normative references cited, "
        f"{len(CONTROL_STATUS_TERMS)} control-status terms defined."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
