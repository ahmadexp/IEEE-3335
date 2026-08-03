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
]
NORMATIVE_FILES = MANUSCRIPT_FILES[4:10]
INFORMATIVE_TECHNICAL_FILES = [MANUSCRIPT_FILES[10], *MANUSCRIPT_FILES[11:]]
PLACEHOLDER_RE = re.compile(
    r"\b(?:TODO|TBD|FIXME)\b|editor(?:'s)? note|<<|>>", re.IGNORECASE
)
SHALL_RE = re.compile(r"\bshall\b", re.IGNORECASE)
UNBOLDED_SHALL_RE = re.compile(r"(?<!\*\*)\bshall\b(?!\*\*)", re.IGNORECASE)
MUST_RE = re.compile(r"\bmust\b", re.IGNORECASE)
CONTROL_OBJECT_RE = re.compile(r"^\|\s*`([A-Z][A-Z0-9_]+)`\s*\|")
NORMATIVE_REFERENCE_MARKERS = [
    "DMTF DSP0236",
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
    "MIPI I3C",
    "PCI Express Base Specification, Revision 5.0, Version 1.0 [13]",
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

    for path, text in texts.items():
        for line_number, line in enumerate(text.splitlines(), 1):
            if PLACEHOLDER_RE.search(line):
                errors.append(f"{relative(path)}:{line_number}: unresolved placeholder")
            if MUST_RE.search(line) and "The term **must**" not in line:
                errors.append(f"{relative(path)}:{line_number}: use shall/should/may/can instead of must")
            if UNBOLDED_SHALL_RE.search(line):
                errors.append(f"{relative(path)}:{line_number}: shall is not bold")

    for path in INFORMATIVE_TECHNICAL_FILES:
        for line_number, line in enumerate(texts[path].splitlines(), 1):
            if SHALL_RE.search(line):
                errors.append(
                    f"{relative(path)}:{line_number}: shall appears in informative technical material"
                )

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
        f"{len(NORMATIVE_REFERENCE_MARKERS)} normative references cited."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
