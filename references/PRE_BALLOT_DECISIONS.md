# P3335 pre-ballot decision agenda

This is the agenda after the full pass on the unofficial draft incorporating the v8 review. It is not ballot text, a vote record, or an assertion of reviewer acceptance. IDs refer to the [publication action register](../PUBLICATION_READINESS.md), [Kevin's decisions and reference dependencies](KEVIN_GODFREY_WG_DECISIONS_20261103.md), and [Rodney's dispositions](RODNEY_CUMMINGS_V8_DISPOSITION_20261110.md). Related requests are grouped so the WG need not decide the same question twice.

## Decisions for the working group

| Topic | Decision requested | Tracking |
|-------|--------------------|----------|
| Document and application scope | Retain one core document with conditional profiles or split by implementation type? Confirm the directly attached application, optional packet roles, and the associated error and noise terminology. | WG-K01; AI-027 |
| Physical timing output | Decide which implementations require 1PPS. Ratify the connector, load, voltage, edge, width, alignment limit and measurement point. Decide whether G.703 19.2 or its Annex B option replaces the current profile, and separately whether to specify a companion serial ToD profile. | AI-003, AI-004; WG-K02; R4 |
| NTP providing interface | The PAR mentions NTP distribution. Section 7.2.2 specifies NTP receive behavior; 7.3.3 has no corresponding NTP providing-profile rule. Decide whether the common output declaration is sufficient or whether a direct NTP server claim needs a dated protocol requirement and tests. A downstream host running its own NTP service is a different implementation boundary. | AI-034 |
| Control model and registry | Keep normative object semantics, move them to an informative annex, or specify a common binding? Approve versioning, identifiers and extension governance. Decide which interfaces require delay compensation, its sign, units, range, readback, and how double correction is prevented. | AI-006, AI-018; WG-K03; R1 |
| PCIe and host integration | Ratify a discoverable PCIe locator, serialized encoding, allocation authority and compatibility rules. Approve correlation fields, sample eligibility, identity, lifecycle and ownership rules after independent host implementations are exercised. Decide separately whether every physical unit needs a persistent serial and exterior label. | AI-005, AI-024 to AI-026; WG-K05 |
| Performance and metrics | Retain bounded supplier declarations, reduce the base metric set, or rely on external profiles? Confirm noise transfer and tolerance, constant and dynamic time error, and whether ADEV remains conditional, moves to informative guidance, or is removed. | AI-008, AI-021, AI-027; R3, R5 |
| Public claims and evidence | Agree on the minimum public statement and published performance data versus records available under controlled access. Decide whether Annex B stays informative, whether Annex D becomes mandatory, and whether independent verification access requires physical test points or permits logical or fixture-based evidence. | AI-010, AI-022; WG-K04, WG-K08; R2 |
| Security profiles | Ratify profile applicability, required outcomes, and whether specific protocol versions, cryptographic suites, trust anchors or certification targets are necessary for interoperability. | AI-014 |
| Environment and telemetry | Retain declarations only or introduce market-specific numeric environmental classes? Decide which power-dip, alarm and backup-energy telemetry capabilities are mandatory, including behavior when the monitoring power domain is lost. | AI-020; WG-K06, WG-K07 |
| References, terms and identifiers | Ratify dated normative references after eligibility review. Reconcile overlapping P1952 terminology through authorized liaison and decide whether requirement identifiers need ballot-stable assignments or can remain editorial. | AI-007, AI-017, AI-028, AI-030; requirement-ID decision in the register |

## Evidence and external dependencies

- **IEEE SA and project editor:** resolve the IPMI source terms, confirm normative-reference availability and obtain official legal/front matter. Retain the approved PAR text; refer its RFC parenthesis and PHC expansion to the project editor. These are not resolved by an editorial vote. See AI-007, AI-019 and AI-030.
- **Technical sources:** [G.8260](https://www.itu.int/rec/T-REC-G.8260/en) still lists the August 2026 edition as prepublished. [G.Sup92](https://www.itu.int/rec/T-REC-G.Sup92/en) lists July 2026 as to be published. Obtain and evaluate the relevant editions and the exact G.FTS-Lite-clk source before changing citations (REF-K01 to REF-K03). No normative edition was updated in this pass.
- **Review and implementation evidence:** obtain the independent metrology review, exercise representative Windows, macOS and Linux implementations, obtain the authorized P1952 comparison, and return dispositions to the reviewers. In particular, ask Rodney to confirm RC-04, RC-05, RC-06, RC-10 and RC-15. Editorial tests do not establish hardware behavior or reviewer agreement.
- **Editorial work, not a policy vote:** complete the per-requirement testability review (RC-01), finish review line numbering for non-paragraph material (AI-031), and triage archival contributions separately (AI-016).

## Corrections in this pass

Clause 6 and Annexes A, B and D now distinguish declaring a bound from demonstrating it, an absolute holdover offset from an observed change, and a measured value from its decision-rule outcome. Clauses 7 and 8 and Annexes B, D and E distinguish a phase or frequency reference from a time label, fixed GNSS capabilities from writable controls, sample validity from eligibility for host discipline, and PCIe-only fields from generic host fields. Clause 8.4 no longer grants a trailing-field exception to a truncated message or unsupported version.

The requirements index now retains profile inheritance, indexes standalone obligations before a list once, and does not turn the explanatory 4.3 roadmap into requirements. No numeric performance limit, protocol edition, common wire encoding, reviewer disposition, or WG vote was changed.
