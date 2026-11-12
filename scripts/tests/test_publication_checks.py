"""Regression checks for omissions that can escape a successful PDF build."""

import contextlib
import io
import re
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import check_draft
import requirements_index


class PublicationChecks(unittest.TestCase):
    def setUp(self):
        self.texts = {
            path: path.read_text(encoding="utf-8")
            for path in check_draft.MANUSCRIPT_FILES
        }

    def assert_rejected(self, expected_error):
        errors = io.StringIO()
        with (
            patch.object(Path, "read_text", lambda path, **kwargs: self.texts[path]),
            contextlib.redirect_stdout(io.StringIO()),
            contextlib.redirect_stderr(errors),
        ):
            self.assertEqual(check_draft.main(), 1)
        self.assertIn(expected_error, errors.getvalue())

    def test_missing_annex_in_document_map(self):
        path = check_draft.ROOT / "01 - Overview/README.md"
        self.texts[path] = re.sub(r"^\| Annex E \|.*\n", "", self.texts[path], flags=re.M)
        self.assert_rejected("document structure is missing Annex E")

    def test_missing_control_status_definition(self):
        path = check_draft.ROOT / "03 - Definitions, Acronyms and Abbreviations/README.md"
        self.texts[path] = re.sub(r"^- \*\*stale:\*\*.*\n", "", self.texts[path], flags=re.M)
        self.assert_rejected("control-status definition: stale")

    def test_obligation_in_informative_material(self):
        path = check_draft.ROOT / "Annex B - Test Procedures/README.md"
        self.texts[path] += "\nA test **shall** use this example.\n"
        self.assert_rejected("shall appears in informative technical material")

    def test_informative_subclause_inside_normative_file(self):
        path = check_draft.MANUSCRIPT_FILES[4]
        self.texts[path] += "\n### 4.10.1 Additional example\n\nAn example **shall** be tested.\n"
        self.assert_rejected("shall appears in informative technical material")

    def test_undefined_reference_in_an_annex(self):
        self.texts[check_draft.MANUSCRIPT_FILES[-1]] += "\nSee [99].\n"
        self.assert_rejected("undefined normative reference [99]")

    def test_duplicate_control_object(self):
        path = check_draft.ROOT / "08 - Control Interfaces/README.md"
        self.texts[path] += "\n| `TC_TIME` | R | timestamp | s | Duplicate. |\n"
        self.assert_rejected("duplicate control object TC_TIME")

    def test_unqualified_accuracy(self):
        path = check_draft.ROOT / "06 - Performance Specifications/README.md"
        self.texts[path] += "\nAccuracy is a numeric output.\n"
        self.assert_rejected("qualify accuracy by measurement context")

    def test_unchecked_source_would_be_included_by_build(self):
        extra = check_draft.ROOT / "99 - Unreviewed/README.md"
        with patch.object(Path, "glob", return_value=[*self.texts, extra]):
            self.assert_rejected("unexpected active manuscript source: 99 - Unreviewed/README.md")

    def test_reference_identity_mismatch(self):
        path = check_draft.ROOT / "02 - Normative References/README.md"
        self.texts[path] = self.texts[path].replace(
            "IPMI Specification, Version 2.0, Revision 1.1", "DMTF DSP0236"
        )
        self.assert_rejected("reference [1] does not match cited source")

    def test_duplicate_reference_identifier(self):
        path = check_draft.ROOT / "02 - Normative References/README.md"
        self.texts[path] = self.texts[path].replace("- [2] ", "- [1] ", 1)
        self.assert_rejected("reference identifiers are missing, duplicated, or out of order")

    def test_conditional_objects_are_all_indexed(self):
        source = "08 - Control Interfaces/README.md"
        text = self.texts[check_draft.ROOT / source]
        section = text.split("### 8.10.3 ", 1)[1].split("### 8.10.4 ", 1)[0]
        objects = re.findall(r"^\|\s*`([A-Z][A-Z0-9_]+)`\s*\|", section, re.M)
        self.assertTrue(objects)
        requirements, _ = requirements_index.extract_requirements(source)
        indexed = [r.text for r in requirements if r.section.startswith("8.10.3 ")]
        for name in objects:
            with self.subTest(object=name):
                self.assertTrue(
                    any(f"`{name}`;" in statement for statement in indexed),
                    f"conditional object {name} is missing from the requirements index",
                )


class RequirementsIndexChecks(unittest.TestCase):
    def test_roadmap_is_not_a_list_of_obligations(self):
        rows, _ = requirements_index.extract_requirements("04 - Conformance/README.md")
        base = [row for row in rows if row.section.startswith("4.3 ")]
        self.assertEqual(len(base), 1)
        self.assertNotIn("controlling provisions", base[0].text)
        profile = next(row for row in rows if "every other physical timing output" in row.text)
        self.assertIn("Physical Timing Output", profile.text)
        self.assertNotIn("|", profile.text)

    def test_independent_obligation_before_list_is_indexed_once(self):
        rows, _ = requirements_index.extract_requirements("06 - Performance Specifications/README.md")
        publish = [row for row in rows if "shall publish performance declarations" in row.text]
        self.assertEqual(len(publish), 1)
        self.assertNotIn("Each declared value", publish[0].text)
        self.assertTrue(any("Each declared value shall identify: The measurement point." in row.text
                            for row in rows))

    def test_profile_inheritance_and_gnss_applicability_remain_visible(self):
        rows, _ = requirements_index.extract_requirements("08 - Control Interfaces/README.md")
        self.assertTrue(any("shall meet the Managed TimeCard profile" in row.text for row in rows))
        gnss = [row.text for row in rows if "each applicable object" in row.text
                and row.section.startswith("8.10.7 ")]
        self.assertEqual(len(gnss), 6)
        self.assertTrue(any("`GNSS_CONST_ENABLE`" in row and "when configuration is supported" in row
                            for row in gnss))


class KevinRevisionChecks(unittest.TestCase):
    def read_source(self, name):
        return (check_draft.ROOT / name).read_text(encoding="utf-8")

    def test_holdover_separates_absolute_error_from_variation(self):
        text = self.read_source("06 - Performance Specifications/README.md")
        holdover = text.split("## 6.8 ", 1)[1].split("## 6.9 ", 1)[0]
        self.assertIn("initial error is unknown", holdover)
        self.assertIn("not replace the holdover time-error envelope", holdover)
        self.assertIn("not be described as an absolute time-error bound", holdover)
        self.assertNotIn("shall** be used when reporting bounded holdover time error", holdover)

    def test_public_claims_and_test_evidence_are_preserved(self):
        text = self.read_source("04 - Conformance/README.md")
        self.assertIn("both publicly available and supplied with the product documentation", text)
        self.assertIn("Controlled access **shall** not replace the public information", text)
        self.assertIn("functional test evidence for applicable functional requirements", text)
        self.assertIn("performance test evidence for applicable measured-performance requirements", text)

    def test_1pps_limits_remain_pending_wg_decision(self):
        text = self.read_source("07 - Timing Interfaces/README.md")
        profile = text.split("### 7.3.2 ", 1)[1].split("### 7.3.3 ", 1)[0]
        for limit in (
            "between -0.3 V and 0.3 V",
            "between 1.2 V and 5.5 V",
            "at least 1 microsecond and not greater than 500 milliseconds",
            "less than 10 nanoseconds",
            "less than 100 nanoseconds",
        ):
            with self.subTest(limit=limit):
                self.assertIn(limit, profile)

    def test_serial_object_remains_conditional(self):
        text = self.read_source("08 - Control Interfaces/README.md")
        required = text.split("### 8.10.2 ", 1)[1].split("### 8.10.3 ", 1)[0]
        conditional = text.split("### 8.10.3 ", 1)[1].split("### 8.10.4 ", 1)[0]
        self.assertNotIn("`TC_SERIAL`", required)
        self.assertIn("`TC_SERIAL`", conditional)

    def test_figure_has_instrument_reference_path(self):
        tree = ET.parse(check_draft.ROOT / "figures/test-fixture.svg")
        path = tree.find(".//*[@id='measurement-reference-path']")
        self.assertIsNotNone(path)
        self.assertTrue(path.get("d"))

    def test_bibliography_identifiers_resolve(self):
        bibliography = self.read_source("Annex C - Bibliography/README.md")
        entries = re.findall(r"^- \*\*\[B(\d+)\]\*\*", bibliography, re.M)
        self.assertEqual(len(entries), len(set(entries)))
        cited = set()
        for path in check_draft.MANUSCRIPT_FILES:
            for group in re.findall(r"\[(B\d+(?:, B\d+)*)\]", path.read_text(encoding="utf-8")):
                cited.update(re.findall(r"B(\d+)", group))
        self.assertFalse(cited - set(entries), f"Missing bibliography entries: {cited - set(entries)}")

    def test_all_review_items_have_one_implementation_status(self):
        disposition = self.read_source("references/KEVIN_GODFREY_FEEDBACK_20261030_DISPOSITION.md")
        rows = re.findall(r"^\| (KG-\d{2}) \| (Applied|Partial|Deferred) \|", disposition, re.M)
        self.assertEqual([item for item, _ in rows], [f"KG-{i:02d}" for i in range(1, 52)])
        decisions = self.read_source("references/KEVIN_GODFREY_WG_DECISIONS_20261103.md")
        self.assertEqual(re.findall(r"^\| (WG-K\d{2}) \|", decisions, re.M),
                         [f"WG-K{i:02d}" for i in range(1, 9)])
        self.assertEqual(re.findall(r"^\| (REF-K\d{2}) \|", decisions, re.M),
                         [f"REF-K{i:02d}" for i in range(1, 4)])


class RodneyRevisionChecks(unittest.TestCase):
    def test_overview_preserves_approved_par_fields(self):
        overview = check_draft.MANUSCRIPT_FILES[1].read_text()
        trace = (check_draft.ROOT / "references/P3335_PAR_SCOPE_PURPOSE.md").read_text()
        for index, title in enumerate(("Scope", "Purpose", "Need"), 1):
            with self.subTest(field=title):
                actual = overview.split(f"## 1.{index} {title}\n", 1)[1].split("\n## ", 1)[0]
                expected = trace.split(f"## {title}\n", 1)[1].split("\n## ", 1)[0]
                self.assertEqual(actual.split(), expected.split())

    def test_required_objects_still_indexed_after_consolidation(self):
        control = "08 - Control Interfaces/README.md"
        source = (check_draft.ROOT / control).read_text()
        table = source.split("### 8.10.2 ", 1)[1].split("### 8.10.3 ", 1)[0]
        objects = re.findall(r"^\| `([A-Z0-9_]+)` \|", table, re.M)
        indexed, _ = requirements_index.extract_requirements(control)
        self.assertGreater(len(objects), 0)
        for name in objects:
            with self.subTest(object=name):
                self.assertTrue(any(f"`{name}`;" in row.text for row in indexed))

    def test_rodney_dispositions_cover_original_rows_and_flags(self):
        path = check_draft.ROOT / "references/RODNEY_CUMMINGS_V8_DISPOSITION_20261110.md"
        rows = re.findall(r"^\| RC-(\d{2}) \| (\d+) \| [^|]+ \| (Yes|No) \| (Applied|Partial) \|",
                          path.read_text(), re.M)
        self.assertEqual([(int(i), int(row)) for i, row, _, _ in rows],
                         [(i, i + 5) for i in range(1, 20)])
        self.assertEqual([int(i) for i, _, flag, _ in rows if flag == "Yes"], [4, 5, 6, 10, 15])


if __name__ == "__main__":
    unittest.main()
