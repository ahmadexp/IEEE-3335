# Working Group decisions from Kevin Godfrey feedback

Status as of 3 November 2026. These items remain open and are not adopted by the accompanying manuscript edits. The proposal remains an unofficial, unapproved draft. Editorial implementation does not constitute WG ratification.

The [implementation disposition](KEVIN_GODFREY_FEEDBACK_20261030_DISPOSITION.md) accounts for all 51 review items. The [original assessment](KEVIN_GODFREY_FEEDBACK_20261030_REVIEW.md) preserves the rationale and source checks.

## Decisions requiring agreement

| ID | Related comments | Decision needed | Current treatment and closure criterion |
|----|------------------|-----------------|-----------------------------------------|
| WG-K01 | KG-01 | Keep one core standard with profiles, or split it into implementation-Type documents? | Added informative configuration examples in 4.10, without new Types. Record the document and maintenance structure before creating separate normative profiles. |
| WG-K02 | KG-03, KG-05, KG-06 | Adopt G.703 19.2 as the Physical Timing Output baseline, and which additional P3335 requirements remain binding? | Existing 7.3.2 voltage, pulse-width, rise-time, and alignment limits are unchanged. B.2.1 explains the distinction. Decide the signal marker, binding voltage status, width/rise limits, measurement-cable assumption, compatibility tests, and separate 100 ns alignment rule together. Linked to AI-003 and AI-004. |
| WG-K03 | KG-07, KG-42 | Which interfaces require configurable delay compensation, and what is the common object contract? | No new objects added. Approve per-interface identity, units, sign, range, resolution, applied/readback semantics, persistence, authorization, update behavior, uncertainty, and prevention of duplicate receiver/host corrections. Linked to AI-006 and AI-018. |
| WG-K04 | KG-16, KG-17, KG-19 | Is independent verification access a new base requirement, and when are physical test points mandatory? | Existing embedded/logical conformance remains. Added informative fixture/access guidance in B.2 only. Decide acceptable physical, logical, and fixture routes, accessibility/safety requirements, and calibration to the actual claimed measurement point. Do not implicitly require unimplemented 1PPS, 10 MHz, or ToD outputs. |
| WG-K05 | KG-39 | Must every physical product have a persistent equipment serial and exterior label? | Existing required `TC_INSTANCE_ID` and conditional `TC_SERIAL` remain unchanged. Decide applicability to cards, modules, embedded functions, and multiple logical instances, with namespace and lifecycle rules. Linked to AI-006 and AI-026. |
| WG-K06 | KG-40 | Which power monitoring, power-dip detection, and alarm capabilities are mandatory? | No sensor or power object added. Specify detectable conditions, bandwidth/thresholds, live versus retained reporting, loss of the reporting power domain, and out-of-band or post-restart behavior. |
| WG-K07 | KG-10, KG-41 | What battery telemetry is required when backup energy is present? | Backup-function and battery-documentation clarifications are applied, but new telemetry is deferred. Distinguish absent, present-unmonitored, unavailable, and fault states; define which health/charge estimates are meaningful and whether instrumentation is mandatory. |
| WG-K08 | KG-02 | May a minimal public claim summary replace the existing public conformance statement or published performance declarations? | No reduction applied. Clause 4.7 still requires the public statement and 6.1 still requires published declarations. Supporting records may use controlled access. Decide any alternative public minimum and access policy for commercial, custom, embedded, and non-commercial implementations explicitly. |

## Reference dependencies

These are source-review dependencies, not completed technical decisions.

| ID | Related comments | Dependency | Required next action |
|----|------------------|------------|----------------------|
| REF-K01 | KG-11 | G.8260 (08/2026) is approved but prepublished and restricted in the official catalog. | Obtain an authorized copy, compare definitions and methods against the retained 11/2022 plus 01/2024 baseline, resolve reference eligibility/availability, and obtain agreement before updating Clause 2 and all citations. Linked to AI-007 and AI-017. |
| REF-K02 | KG-12 | G.Sup92 (07/2026) is approved but awaiting publication. | The bibliography links only the public catalog. Obtain and review the published text before substituting a technical citation or asserting its contents. The superseded 10/2025 text was not silently used as the new edition. |
| REF-K03 | KG-22 | The exact G.FTS-Lite-clk source named in the feedback has not been reviewed. | Obtain the precise work-item identifier, text, and status. The related G.FTS-Lite PTP profile is under study and is not evidence that the separate clock specification is approved. No new normative dependency is introduced. |

The dated G.8272 (07/2025) Appendix I is used only as an informative test example. Its 08/2026 amendment also needs review before any proposal to adopt an updated baseline.

## Evidence needed for closure

For each decision, record the agreed wording, applicable implementation classes, meeting or ballot decision reference, responsible editor, and affected tests. Update the requirements index and Annex D with the approved technical changes. A recommended disposition or a successful PDF build does not close a WG decision.

The applied evidence, metrology, documentation, and terminology changes remain draft candidate text for normal WG review. Existing publication-readiness actions, including independent metrology review and official front matter, are not closed by this revision.

## Verified source records

- [G.703 Amendment 1 official record](https://www.itu.int/rec/T-REC-G.703-202105-I!Amd1/en).
- [G.8260 (08/2026) official record](https://www.itu.int/rec/T-REC-G.8260-202608-P/en).
- [G.Sup92 (07/2026) official record](https://www.itu.int/rec/T-REC-G.Sup92-202607-I/en).
- [Related G.FTS-Lite PTP profile work item](https://www.itu.int/itu-t/workprog/wp_item.aspx?isn=23831).
- [G.8272 edition and amendment history](https://www.itu.int/rec/T-REC-G.8272/en).
