# IEEE P3335 Publication Readiness Notes

This file tracks editorial and technical gaps found during the repository-wide readiness pass. It is intended as a working-group punch list, not as part of the draft standard.

## Style and Process Anchors

The pass used the following IEEE SA guidance as the editorial baseline:

- IEEE SA Standards Board Operations Manual, Clause 6: normative material defines conformance, informative material is provided for information only, and normative references are indispensable and cited where they apply. <https://standards.ieee.org/about/policies/opman/sect6/>
- IEEE SA Normative References FAQ: Clause 2 should include only references that are indispensable for applying the standard, and each should be cited as a source of mandatory requirements. <https://standards.ieee.org/faqs/references/>

## Completed in This Pass

| Area | Status | Notes |
|------|--------|-------|
| Clause 4 conformance | Improved | Replaced internal methodology notes with standards-facing conformance requirements, optional feature claims, conformance statement content, and test-evidence expectations. |
| Clause 2 references | Improved | Removed the in-clause bibliography and limited Clause 2 to normative references; background material moved to Annex C. |
| Clause 5 architecture | Improved | Rewrote the architecture clause around externally observable functions, implementation boundaries, unified timescale behavior, optional features, and documentation. |
| Clause 6 performance | Improved | Recast performance as bounded reporting and characterization requirements instead of universal numeric limits. |
| Clause 7 timing interfaces | Improved | Replaced an unsupported universal 1 ns alignment requirement with declared measurement-point and alignment-bound requirements. |
| Clause 8 control interfaces | Improved | Added reserved-value handling and tightened extension interoperability language. |
| Clause 9 environment | Improved | Removed accidental nested "Annex A" and converted that material into an informative Clause 9 subclause. |
| Annex C bibliography | Improved | Removed duplicate normative references and a commercial-looking background item. |
| Repository README | Improved | Replaced stale page counts with active source-of-truth guidance. |

## Remaining High-Priority Gaps

| Priority | Gap | Why it matters | Recommended next action |
|----------|-----|----------------|-------------------------|
| P0 | PAR scope and purpose text is not formally integrated. | IEEE drafts need scope/purpose alignment with the approved PAR; mismatches can create ballot and publication delays. | Insert the approved PAR scope and purpose text into Clause 1 and verify that all clauses remain inside that scope. |
| P0 | Mandatory versus optional 1PPS output is unresolved. | Source material proposes mandatory 1PPS, while the active draft currently requires at least one providing interface. This affects base conformance. | Working group should decide whether 1PPS is a base requirement, a profile requirement, or an optional feature. |
| P0 | Host interface mapping is conceptual. | Interoperability depends on a concrete mapping: discovery, register/API model, timestamp formats, error codes, units, and driver-visible behavior. | Define at least one complete baseline host mapping, likely PCIe/PTM plus a register or information model. |
| P0 | Control information model is incomplete. | Clause 8 names common capabilities but does not yet provide a stable schema, object model, register map, or protocol mapping. | Promote the GNSS/top-level information-model work into Clause 8 or a normative annex once stable. |
| P0 | Normative references need final legal/editorial review. | IEEE rules require normative references to be indispensable, available, and free of commercial terms and conditions. Open-source normative references have additional hosting constraints. | Review each Clause 2 entry against every normative citation; demote any reference that is not indispensable. |
| P1 | Numeric performance profiles are not decided. | A reporting-only model improves comparability but does not create minimum product classes. Some markets may expect profiles or classes. | Decide whether P3335 defines no numeric minima, one minimum baseline, or optional named performance classes. |
| P1 | Test procedures remain informative. | Conformance claims are harder to verify if pass/fail procedures are not normative or externally referenced. | Decide whether Annex B stays informative, becomes normative, or references external conformance test specifications. |
| P1 | Figures are missing. | IEEE drafts normally benefit from architecture, timing-flow, and test-fixture figures; the original context diagram placeholder has been removed from normative text. | Add generated or source-controlled figures for architecture context, unified timescale flow, and representative test setup. |
| P1 | Requirement IDs/traceability are absent. | Ballot resolution and conformance review become harder as requirements grow. | Add stable requirement identifiers or a generated requirements index once clauses stabilize. |
| P1 | Security profile is conditional but not classified. | Secure deployment requirements currently apply when claimed or marketed; product classes would make this clearer. | Define security profiles such as baseline, managed, and secure infrastructure. |
| P2 | Build output is Pandoc-generic, not IEEE-publication formatted. | The PDF is useful for review but is not a true IEEE SA publication package. | Add metadata/front matter placeholders and consider a template path compatible with IEEE SA editorial processing. |
| P2 | `Unsorted/` remains large and mixed. | Useful source material is hard to separate from obsolete or duplicated notes. | Triage `Unsorted/` into `contributions/`, `archive/`, and `source-extractions/`, preserving provenance. |

## Gap Closure Action Items

The following action items convert the remaining gaps into assignable work. Owners are intentionally listed as `TBD` until the working group assigns names. The status column records the draft resolution attempted in this pass.

| ID | Priority | Status | Owner | Action item | Deliverable | Acceptance criteria | Dependencies |
|----|----------|--------|-------|-------------|-------------|---------------------|--------------|
| AI-001 | P0 | Closed | TBD | Obtain the approved PAR scope and purpose text. | `references/P3335_PAR_SCOPE_PURPOSE.md`. | Source, approval date, and exact text are traceable. | None |
| AI-002 | P0 | Closed | TBD | Align Clause 1 with the approved PAR. | Patch to `01 - Overview/README.md`. | Scope and purpose are aligned to public PAR text; broader explanatory text is informative. | AI-001 |
| AI-003 | P0 | Draft-resolved; WG ratification needed | TBD | Decide the base conformance status of 1PPS. | Clause 4 conformance profiles. | 1PPS is required for Physical Timing Output profile; logical-only Base TimeCard conformance remains possible without physical 1PPS. | None |
| AI-004 | P0 | Draft-resolved; WG ratification needed | TBD | Draft the 1PPS requirement package after the decision. | Patch to Clause 7. | Requirement includes connector, edge definition, load, pulse width, rise time, measurement point, alignment reporting, and test reference. | AI-003 |
| AI-005 | P0 | Draft-resolved | TBD | Define the baseline host interface mapping. | Clause 8.9. | Includes discovery, enumeration, register/API model, timestamp format, units, endianness, error handling, interrupt/polling behavior, and correction terms. | AI-003 if 1PPS alignment is used as a cross-check |
| AI-006 | P0 | Draft-resolved | TBD | Promote the control information model from source material. | Clause 8.10. | Defines object/register naming, data types, access mode, reserved values, units, versioning, and source, state, offset, alarm, firmware, GNSS, and traceability objects. | AI-005 for host-mapping alignment |
| AI-007 | P0 | Initial audit complete; legal/editorial review pending | TBD | Audit every Clause 2 normative reference. | `references/NORMATIVE_REFERENCE_AUDIT.md`. | Each Clause 2 entry is cited by normative text and has a clear role; final commercial-terms review remains. | AI-004, AI-005, AI-006 may add citations |
| AI-008 | P1 | Draft-resolved; WG ratification needed | TBD | Decide performance class strategy. | Clause 4.6 and Clause 6.2. | Base conformance is reporting-only; named numeric performance classes may be externally or vendor-defined but are not universal minima in this draft. | None |
| AI-009 | P1 | Closed | TBD | Draft performance profiles or reporting-only confirmation. | Patch to Clause 6. | Time accuracy, stability, frequency, phase noise, pulse timing, holdover, and environment have clear reporting requirements. | AI-008 |
| AI-010 | P1 | Draft-resolved; WG ratification needed | TBD | Decide status of Annex B test procedures. | Clause 4.8 and Annex B title/status. | Annex B remains informative and is not a normative conformance-test suite in this draft. | AI-008, AI-009 |
| AI-011 | P1 | Draft-resolved | TBD | Convert test coverage into pass/fail procedures where required. | Patch to Annex B. | Functional/control tests now include applicability, method, and pass/fail basis; performance tests retain metric-based evaluation. | AI-010 |
| AI-012 | P1 | Closed | TBD | Create source-controlled figures. | `figures/*.svg`, `figures/rendered/*.pdf`, Clause 5 and Annex B references. | Includes architecture context, unified timescale/time-flow, and representative test fixture; all figures have captions and are referenced in text. | AI-005 and AI-011 for accurate diagrams |
| AI-013 | P1 | Closed | TBD | Add requirement IDs or a generated requirements index. | `scripts/requirements_index.py` and `REQUIREMENTS_INDEX.md`. | Every current `shall` in normative clauses is indexed with a generated identifier, source, line, and text. | Major normative text should be stable first |
| AI-014 | P1 | Draft-resolved | TBD | Define security profiles. | Clause 4.4 and Clause 8.11. | Profiles distinguish baseline, managed, and secure infrastructure behavior; optional security claims have clear mandatory requirements. | AI-006 |
| AI-015 | P2 | Closed | TBD | Improve the publication build package. | `metadata.yaml` and Makefile updates. | `make` uses metadata, builds a deeper TOC, and removes LaTeX scratch files from the root. | None |
| AI-016 | P2 | Partially resolved | TBD | Triage `Unsorted/` without losing provenance. | `Unsorted/README.md`. | Triage classes and migration rules are documented; bulk file moves deferred to a separate provenance-preserving patch. | None |

## Recommended Sequencing

1. Ratify or amend draft-resolved decisions: AI-003, AI-004, AI-008, and AI-010.
2. Review the new interoperability core: AI-005, AI-006, and AI-014.
3. Complete final editorial/legal reference review for AI-007.
4. Regenerate `REQUIREMENTS_INDEX.md` after each normative edit using `python3 scripts/requirements_index.py`.
5. Rebuild `IEEE3335.pdf`, run the editorial checks below, and review the generated PDF before ballot-facing circulation.
6. Perform the `Unsorted/` migration in a separate provenance-preserving patch after approving the triage plan.

## Editorial Checks to Repeat Before Ballot

- Scan active draft files for `TODO`, `TBD`, editor notes, `<<...>>`, and accidental local bibliographies.
- Verify every Clause 2 reference is cited by normative text.
- Verify every informative annex avoids mandatory requirements unless intentionally changed to normative.
- Verify every optional feature has a clear "if implemented, then..." requirement path.
- Verify every performance requirement has a metric, measurement point, operating condition, and pass/fail basis.
- Build the PDF from a clean checkout and compare the generated table of contents against the intended clause order.
