# Kevin Godfrey feedback implementation disposition

Revision date: 3 November 2026. Source and baseline are recorded in the [original review](KEVIN_GODFREY_FEEDBACK_20261030_REVIEW.md).

This record distinguishes changes made to the unofficial proposal from [open WG decisions and reference dependencies](KEVIN_GODFREY_WG_DECISIONS_20261103.md). Applied means implemented as draft candidate text, not approved by the WG or accepted by the reviewer. No conformance claim against the draft is implied.

## Comment accounting

The 51 review items comprise 34 applied, 6 partially addressed, and 11 deferred items. Partial and deferred items link to eight open WG decisions and three reference dependencies in the separate register.

| ID | Status | Implementation or remaining dependency |
|----|--------|----------------------------------------|
| KG-01 | Partial | Informative configuration/applicability matrix added in 4.10. A multi-document split or new implementation Types remain WG-K01. |
| KG-02 | Partial | 4.7, 5.1, 5.10, 6.1, B.6, and D.2 distinguish public claims from controlled-access supporting evidence. The existing public statement and performance declarations remain required; any reduction is WG-K08. |
| KG-03 | Deferred | Normative adoption of a different 1PPS baseline remains WG-K02. Existing numeric limits retained. |
| KG-04 | Applied | B.2.1 summarizes the specific G.703 measurement interface, links the freely available source, and identifies the controlling requirement for each claim. No new annex or conflicting normative copy added. |
| KG-05 | Deferred | Pulse-width/rise-time changes and adopted marker are contingent on WG-K02. Differences explained in B.2.1 without changing 7.3.2 limits. |
| KG-06 | Partial | B.2.1 scopes the cited cable assumption to the G.703 measurement interface. Adoption as a P3335 profile limit remains WG-K02. |
| KG-07 | Deferred | New delay-compensation control contract remains WG-K03. |
| KG-08 | Applied | 9.4.2 explicitly permits optional backup energy and distinguishes retained data, real-time clock, unified timescale, and actual output service. |
| KG-09 | Applied | 9.6.2 and D.8 add battery chemistry/rating, service/disposal, and applicable transport-documentation references without asserting universal shipping rules. |
| KG-10 | Deferred | New battery telemetry and sensing obligations remain WG-K07. |
| KG-11 | Deferred | REF-K01 records the approved but restricted/prepublished G.8260 revision. Clause 2 remains on the reviewed dated baseline. |
| KG-12 | Partial | C.6 and 10.2.1 identify the public G.Sup92 catalog. Technical adoption of unavailable 07/2026 content remains REF-K02. |
| KG-13 | Applied | Gateware defined in 3.1 and distinguished from processor instructions. |
| KG-14 | Applied | Removed unused acronym/unit entries identified by the review; added BNC for its new explicit use. |
| KG-15 | Applied | 3.2.1 explains BeiDou and Galileo as constellation names without invented acronym expansions. |
| KG-16 | Deferred | Mandatory verification access remains WG-K04; no new base signal or connector requirement added. |
| KG-17 | Partial | B.2 adds non-destructive fixture/test-point guidance, loading, safety, and calibration to the claimed measurement point. Mandatory physical-access rules remain WG-K04. |
| KG-18 | Applied | 4.6 permits precise incorporation of performance specifications while retaining uncovered P3335 declarations. |
| KG-19 | Deferred | Mandatory embedded test points remain WG-K04; equivalent logical measurement points remain permitted under 4.4. |
| KG-20 | Applied | 3.1 and 4.5 distinguish UTC(k) reference origin/timescale from transport interface; Figure 3 uses generic reference labels. |
| KG-21 | Applied | Removed undefined environmental-profile examples from optional-feature claims and definition. Clause 9 declarations remain mandatory. |
| KG-22 | Partial | 4.6 and 6.2 explicitly accommodate external-standard classes and exact identifiers for every class. The unfinished clock-document dependency remains REF-K03. |
| KG-23 | Applied | 4.8 requires applicable functional and performance test evidence. It distinguishes documentation checks, supplier evaluation, representative configurations, and per-unit testing; D.9 follows the same rules. |
| KG-24 | Applied | 5.3.2, 10.3.4, E.4, and B32 distinguish historical conversions and valid offsets from future UTC adjustment policy. Existing 8.10.4 validity/eligibility safeguards remain unchanged. |
| KG-25 | Applied | 3.1, 5.7, 6.7, 7.3.2, A.1, and A.6 use scoped pulse time error/variation and explain jitter bandwidth and sampling limitations. |
| KG-26 | Applied | 5.7 distinguishes explicitly incorporated normative numeric limits from informative references and separately claimed classes. |
| KG-27 | Applied | 5.7 lists performance categories without parenthetical metric lists. Detailed metrics remain in Clause 6 and Annex A. |
| KG-28 | Applied | 5.9 permits documented local indicators without replacing control status or mandating LEDs. |
| KG-29 | Applied | 5.10 requires observable disciplining response, modes, bandwidth/masks, and limitations rather than proprietary algorithms or loop topology. |
| KG-30 | Applied | 6.3 and B.4.1 clarify suitable laboratory/GNSS/simulator references, retained traceability, absolute versus relative claims, and shared-reference errors. |
| KG-31 | Applied | 6.6, A.5, and B.4.4 permit appropriate time-domain assessments while retaining spectral-mask and conversion safeguards. |
| KG-32 | Applied | 6.6 scopes ADEV to claimed output/measurement-point behavior and distinguishes it from TDEV and frequency offset. ADEV is retained with its informative definition and tests. |
| KG-33 | Applied | 6.8 permits exact holdover-profile references with fallback declarations. It also corrects the independent absolute-error/MTIE issue; A.9, B.4.8, and D.7 agree. |
| KG-34 | Applied | 6.9 permits referenced transition requirements but retains uncovered host and driver lifecycle cases. |
| KG-35 | Applied | 6.1, 6.11, and D.7 identify governing editions, clauses, classes/masks, conditions, and acceptance rules. |
| KG-36 | Applied | 7.2.4 requires identification of the specific interface and applicable provisions when G.703 compatibility is claimed. It does not make that interface universal. |
| KG-37 | Applied | 7.3.1 explicitly covers firmware, gateware, software updates, and restart. |
| KG-38 | Applied | 7.3.2 explicitly names BNC under the retained 50 ohm connector requirement; TNC is retained. |
| KG-39 | Deferred | Equipment serial/label mandate remains WG-K05. Existing control objects and identity semantics unchanged. |
| KG-40 | Deferred | New power monitoring/alarms remain WG-K06. |
| KG-41 | Deferred | Battery monitoring duplicate consolidated under WG-K07. |
| KG-42 | Deferred | GNSS and other input correction objects consolidated under WG-K03. |
| KG-43 | Applied | 9.1 specifies units and permitted prefixes, pressure reference, and supplementary unit conversions; D.8 follows it. |
| KG-44 | Applied | Each 10.2 application subsection now points to relevant technical, profile, or measurement references without inventing universal regulatory applicability. |
| KG-45 | Applied | 6.1, A.7, and D.7 identify masks, editions, parameters, intervals, filtering, and acceptance rules. |
| KG-46 | Applied | A.3, A.4, and D.7 state seconds or labelled submultiples for TDEV and MTIE. |
| KG-47 | Applied | A.6 recast as pulse/event timing variation and aligned with the scoped jitter and phase-noise treatment. |
| KG-48 | Applied | Figure 3 and B.1 are interface-neutral and illustrative; the measurement reference now connects explicitly to the instrument. |
| KG-49 | Applied | Figure 3 separates applied and measurement references from interface choices; 3.1 and 4.5 explain UTC(k). |
| KG-50 | Applied | Figure 3 uses an applicable-metrics label instead of a fixed analyzer metric list; ADEV remains available elsewhere. |
| KG-51 | Applied | B.3.2 adds conditional PTP, IRIG, and other host/logical output examples alongside conditional PTM. |

## Additional corrections

- The holdover error envelope is separate from MTIE, which does not include constant initial offset. Absolute versus initial-offset-relative results and initial uncertainty are explicit across normative text and annexes.
- The representative measurement fixture now includes the instrument's comparison-reference connection and calls out shared-reference correlations.
- The public-documentation minimum, existing 1PPS numeric limits, baseline control objects, and dated normative-reference list were preserved while approval-dependent changes were recorded separately.

## Validation

- Editorial checks passed across all 16 manuscript sources, including citation of all 14 normative references and definitions for all 7 control-status terms.
- The requirements index was regenerated and checked: 587 statements derived from 384 normative `shall` occurrences.
- All 16 regression tests passed, including comment accounting, reference resolution, holdover semantics, evidence access, the retained 1PPS limits, conditional serial identification, and the fixture's measurement-reference path.
- The [proposal PDF](../IEEE3335.pdf) was rebuilt with native Pandoc 3.13 and XeLaTeX. All 72 pages were rendered for visual review, with detailed inspection of the revised tables, bibliography, and fixture diagram. Text-boundary checks found no content outside the page or right text margin. Every page has the 3 November 2026 footer and its page number.
- Existing pagewise paragraph line numbering is preserved from the Abstract onward. Full table and equation line-number coverage remains the separate publication-readiness action AI-031.
- Source whitespace, punctuation, manuscript text, and PDF metadata were checked before delivery. `git diff --check` passed.

The default Pandoc and ImageMagick executables on the build host were incompatible with its architecture. The successful build used the `PANDOC` override and a native SVG renderer to regenerate the committed-format fixture PDF. System installations were not changed.

These checks establish document consistency and build integrity, not hardware qualification, independent metrology sign-off, WG approval, or access to restricted or unpublished standards text. The applied wording remains candidate text for WG review.
