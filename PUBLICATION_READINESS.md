# IEEE P3335 Publication Readiness

This file is the working-group action register for the Markdown draft. It is not part of the proposed standard. Status reflects the repository as of the latest editorial pass; `TBD` owners require working-group assignment.

## Editorial and process basis

- IEEE SA Standards Board Operations Manual, Clause 6: normative and informative material, draft-status notices, requirement words, document structure, and normative references. <https://standards.ieee.org/about/policies/opman/sect6/>
- IEEE SA Normative References FAQ: indispensability, citation, availability, commercial-terms, and open-source requirements. <https://standards.ieee.org/faqs/references/>
- Public P3335 project and PAR trace recorded in `references/P3335_PAR_SCOPE_PURPOSE.md`.

## Current readiness baseline

| Area | Current result |
|------|----------------|
| Draft status | Front matter identifies the document as unapproved, subject to change, and not for conformance or compliance use. Official IEEE copyright, patents, participant, and template material remains external. |
| Scope and purpose | Clause 1 is aligned to the public PAR and separates scope, purpose, need, and implementation freedom. |
| Conformance | Clause 4 defines base conformance, conditional profiles, supplier statements, evidence, and an informative Annex D proforma. |
| Architecture | Clause 5 specifies externally observable boundaries, one unified timescale, source selection, host transfer, stable instance selection, host lifecycle behavior, measurement points, and documentation. |
| Performance | Clause 6 uses bounded declarations, traceable methods, uncertainty, and explicit decision rules rather than unsupported universal product classes. |
| Timing interfaces | Clause 7 defines common receive/provide declarations, conditional protocol conformance, concrete 1PPS output limits, continuity, and timing-interface status. |
| Control interfaces | Clause 8 separates transport bindings from the baseline semantic model, defines atomic time reads, a portable PCIe discovery descriptor, binary ABI validation, stable identity, bounded host-time correlation, time-control ownership, lifecycle recovery, required and conditional objects, versioning, extension behavior, and security profiles. |
| Environment | Clause 9 uses implementation-neutral operating, full-performance, storage, survival, qualification, and lifecycle declarations. |
| Informative material | Clauses and annexes use neutral examples without arbitrary universal limits; Annexes A and B explain metrics and test evidence, Annex C contains a focused, source-checked bibliography, and Annex E maps the host requirements to Windows, macOS, and Linux. |
| Traceability tooling | `make check` validates the manuscript and verifies that `REQUIREMENTS_INDEX.md` matches the normative sources. |
| Build | `make` builds source-controlled figures, front matter, clauses, and annexes into the review PDF. |

## Remaining decision gaps

| Priority | Decision or external dependency | Why it remains |
|----------|---------------------------------|----------------|
| P0 | Ratify the Physical Timing Output profile and its 1PPS electrical and alignment limits. | The text is a complete draft candidate derived from contributions, but it changes product conformance scope. |
| P0 | Ratify the P3335 PCIe discovery-descriptor locator and serialized binary encoding. | Clause 8 now defines mandatory descriptor content and receiver behavior, but the fixed locator, field encoding, identifier allocations, and migration policy require working-group ownership. |
| P0 | Freeze the baseline control vocabulary and extension policy. | Object names and semantics are usable draft text; stable numeric encodings or a registry require WG ownership and compatibility policy. |
| P0 | Complete IEEE SA editorial/legal review of every Clause 2 reference. | The technical-use audit is complete, but availability and commercial-terms review cannot be closed solely in the repository. |
| P0 | Obtain official IEEE SA front matter and publication template. | The draft notice is present; copyright, patents, participants, trademarks, and final IEEE production formatting require IEEE SA input. |
| P1 | Ratify the reporting-only performance strategy. | The current model enables comparison but deliberately creates no universal numeric product class. |
| P1 | Ratify Annex B as informative or select a normative conformance-test approach. | The procedures are now reproducible examples, but their formal status is a WG policy decision. |
| P1 | Review security profiles for cryptographic interoperability. | Required outcomes are defined; algorithm suites, trust-anchor formats, protocol versions, and certification targets are not fixed. |
| P1 | Ratify the Clause 9 declaration model and any market-specific environmental profiles. | The current text avoids arbitrary universal limits; application profiles can still add numeric limits. |
| P1 | Obtain an independent metrology review of Clause 6 and Annexes A and B. | Formulae and procedures have been editorially corrected but should be reviewed by timing-metrology specialists before ballot. |
| P1 | Decide whether Annex D remains informative or becomes a formal conformance proforma after requirement freeze. | The current proforma is useful but does not yet enumerate every requirement as a ballot-stable checklist. |
| P2 | Decide whether generated editorial IDs are sufficient or stable requirement IDs are embedded in normative text. | Generated IDs intentionally change when requirements are reordered. |
| P2 | Complete provenance-preserving migration of `Unsorted/`. | Triage rules exist, but bulk moves should be reviewed separately from normative edits. |

## Action items

| ID | Priority | Status | Owner | Action | Deliverable and acceptance condition |
|----|----------|--------|-------|--------|--------------------------------------|
| AI-001 | P0 | Closed | TBD | Obtain and trace the approved PAR scope and purpose. | `references/P3335_PAR_SCOPE_PURPOSE.md` identifies public sources and approval trace. |
| AI-002 | P0 | Closed | TBD | Align Clause 1 with the PAR. | Scope and purpose are aligned; explanatory content is clearly separated. |
| AI-003 | P0 | Draft candidate; WG vote needed | TBD | Decide the base-conformance status of 1PPS. | WG accepts, rejects, or revises the Physical Timing Output profile in 4.4. |
| AI-004 | P0 | Draft candidate; WG vote needed | TBD | Ratify the 1PPS requirement package. | Connector, load, voltage, edge, width, rise time, measurement point, uncertainty, and alignment limit are approved in 7.3.2. |
| AI-005 | P0 | Draft candidate; encoding vote needed | TBD | Define the host interoperability boundary. | WG approves the P3335 discovery descriptor, baseline host mapping, ABI rules, and allocation ownership or records the remaining permitted binding choices. |
| AI-006 | P0 | Draft candidate; WG review needed | TBD | Freeze the baseline control information model. | Required and conditional objects, stable identity, host-time correlation, time-control status, state vocabulary, support/validity semantics, atomic timestamp behavior, and extension rules are approved. |
| AI-007 | P0 | Technical audit complete; legal/editorial review pending | TBD | Complete Clause 2 reference review. | Every reference passes edition, availability, commercial-terms, citation, and normative-use review; results update `references/NORMATIVE_REFERENCE_AUDIT.md`. |
| AI-008 | P1 | Draft candidate; WG vote needed | TBD | Decide the performance-class strategy. | WG approves reporting-only base conformance or supplies numeric classes with measurement conditions. |
| AI-009 | P1 | Closed | TBD | Define bounded performance reporting. | Clause 6 covers time, stability, frequency, phase noise, pulse timing, holdover, transitions, environment, uncertainty, and decision rules. |
| AI-010 | P1 | Draft candidate; WG vote needed | TBD | Decide the formal status of test procedures. | Annex B remains informative, becomes normative, or is replaced by an external conformance-test reference. |
| AI-011 | P1 | Closed for informative status | TBD | Make test procedures reproducible. | Tests identify applicability, conditions, method, evidence, declared limit, uncertainty, and decision rule. |
| AI-012 | P1 | Closed | TBD | Add source-controlled figures. | Architecture, unified-timescale, and representative fixture figures build from committed sources. |
| AI-013 | P1 | Closed as editorial tooling | TBD | Generate and verify a requirements index. | Block-aware index is regenerated or checked through `make check`; index states that IDs are non-normative and unstable. |
| AI-014 | P1 | Draft candidate; security review needed | TBD | Define security profiles. | Baseline, Managed, and Secure Infrastructure outcomes are specified; WG decides cryptographic suites and certification expectations. |
| AI-015 | P1 | Closed | TBD | Improve the review build and draft labeling. | Front matter, metadata, figures, deeper TOC, scratch cleanup, `make check`, and `make` operate successfully. |
| AI-016 | P2 | Partially resolved | TBD | Triage `Unsorted/` without losing provenance. | `Unsorted/README.md` defines classes and migration rules; reviewed file migration remains. |
| AI-017 | P0 | Open | TBD | Ratify current normative-reference editions. | WG confirms IEEE 802.1AS-2025, IEEE 1139-2022, IEEE 1193-2022, MIPI I3C Basic v1.2, and the retained dated baselines. |
| AI-018 | P0 | Open | TBD | Establish control identifier and host-binding governance. | Allocation authority, reserved ranges, version policy, and compatibility process are documented. |
| AI-019 | P0 | External dependency | TBD | Obtain official IEEE SA publication front matter. | IEEE-approved copyright, patents, participants, trademark, and draft boilerplate replace the repository placeholders. |
| AI-020 | P1 | Draft candidate; WG review needed | TBD | Ratify the environmental declaration model. | WG approves Clause 9 and identifies any numeric application profiles needed for target markets. |
| AI-021 | P1 | Open | TBD | Conduct independent metrology review. | Named reviewers confirm Clause 6 and Annexes A and B or record and resolve technical comments. |
| AI-022 | P1 | Draft candidate; requirement freeze needed | TBD | Finalize the conformance-statement proforma. | Annex D is checked against the frozen requirements and its normative or informative status is approved. |
| AI-023 | P1 | Closed | TBD | Audit the informative bibliography. | Misattributed or untraceable entries are removed; retained technical publications include sufficient bibliographic data and publisher or DOI links. |
| AI-024 | P0 | Draft candidate; WG vote needed | TBD | Ratify the portable PCIe discovery descriptor. | WG approves the locator, signature, header and entry encoding, resource types, capability allocation, consistency mechanism, and fail-closed compatibility behavior in 8.9.1. |
| AI-025 | P0 | Draft candidate; host-time review needed | TBD | Ratify host-time correlation and discipline eligibility. | WG approves the `HOST_TIME_CORRELATION` fields, clock and timescale semantics, discontinuity handling, freshness and window limits, and eligibility rules in 8.10.4. |
| AI-026 | P1 | Draft candidate; cross-platform validation needed | TBD | Validate host lifecycle, identity, ABI, and ownership requirements. | Annex B host tests are executed on representative Windows, macOS, and Linux implementations, with limitations and resulting normative comments recorded. |
| AI-027 | P1 | Draft candidate; reviewer confirmation needed | TBD | Ratify the timing-flow scope clarification and noise-response requirements. | Stefano confirms the comment dispositions; the WG approves the 1.1 deployment model and the noise-transfer, noise-tolerance, cTE, and dTE text in Clauses 3, 5, and 6. |

## Recommended sequence

1. Resolve AI-003, AI-004, AI-005, AI-006, AI-017, AI-018, AI-024, and AI-025 as the interoperability core.
2. Resolve AI-008, AI-010, AI-014, AI-020, AI-021, AI-022, AI-026, and AI-027 as the validation and profile layer.
3. Complete AI-007 and AI-019 with the IEEE SA program manager and project editor.
4. Regenerate the requirements index after every normative edit using `make requirements`.
5. Run `make check`, rebuild with `make`, and visually review the PDF before each ballot-facing circulation.
6. Complete AI-016 in a separate provenance-preserving change.

## Repeatable local checks

`make check` performs placeholder, requirement-word, informative-material, normative-reference-use, duplicate-object, requirements-index freshness, and Python syntax checks. The PDF build remains a separate `make` step so editorial checks can run quickly during drafting.
