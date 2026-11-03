# Kevin Godfrey feedback review and proposed resolutions

Review date: 3 November 2026.

Kevin's feedback identifies substantive interoperability, verification, documentation, and usability improvements. The recommended response is to accept the practical objectives while refining proposals that would remove useful metrics, weaken evidence, or exclude embedded implementations. The immediate priorities are the 1PPS profile, evidence and confidentiality rules, test access, delay compensation, and measurement terminology.

This review proposes dispositions; it does not record Working Group approval or implementation. The manuscript and proposal PDF have not been changed by this review.

Subsequent implementation on 3 November 2026 is recorded in [the implementation disposition](KEVIN_GODFREY_FEEDBACK_20261030_DISPOSITION.md). [Open WG decisions and reference dependencies](KEVIN_GODFREY_WG_DECISIONS_20261103.md) are maintained separately. The assessment below preserves the pre-edit findings.

## Review basis

- Source: Kevin Godfrey, *P3335 v7 Comments (Kevin Godfrey 30Oct2026).docx*, dated 30 October 2026, with input from colleagues at Calnex.
- Source SHA-256: `7482ad20e7a897ddb212ec98258867ab8c5a9343656a0101eaf4c9d26c79748a`.
- Comparison: the active repository manuscript at commit `634d6ec0a190d8c11be851934c7f7c294fb25d7d`, together with its figure sources and existing publication-readiness register. A separate copy of the circulated v7 proposal was not supplied; clause quotations were checked against this repository text.
- The supplied DOCX contains body-text feedback, with no embedded Word comment part or tracked insertions/deletions. All nine rendered pages and all substantive body text were reviewed.
- Page references below refer to the reviewed nine-page rendering of Kevin's document, not proposal PDF page numbers. IDs are assigned here for tracking; Kevin did not number his comments. Compound comments are split, and repeated comments are explicitly linked, yielding 51 review items.
- Source checks reflect availability on 3 November 2026. Restricted or unpublished standards text was not treated as reviewed.

## Principal findings

### Evidence and confidentiality need separate rules

Clause 4.8 currently permits documentation review as an alternative to testing and makes evidence fields conditional on test evidence being used. That leaves an avoidable ambiguity for functional and measured-performance claims. Require relevant functional and performance evidence, while retaining document inspection for documentary obligations. This need not require third-party certification or testing every manufactured unit.

Kevin's concern about public disclosure is also justified. Clauses 4.7, 5.1, 5.10, and 6.1 use different publication and availability language. However, B.6 already permits controlled access when data cannot be shared, and Annex B is informative. The solution is a consistent distinction between the public claim, integration information, and retained supporting evidence, not deletion of the evidence requirement.

### The 1PPS profile needs an explicit standards decision

The direct source check of G.703 Amendment 1 confirms that its 50 ohm measurement interface in 19.2 uses a leading-edge midpoint marker, rise time below 5 ns, pulse width from 100 ns to 500 ms, and a 3 m measurement cable assumption. The voltage table in 19.2.2 is explicitly provided for information. The separate distribution interface is addressed in 19.1. [S1]

Consequently, the proposed P3335 rise-time limit is looser; its 1 microsecond minimum width is a narrower subset, not by itself an incompatible transmitted pulse. Specify which interface is adopted, retain any intentionally binding P3335 voltage requirements, and avoid applying the measurement-cable restriction to every timing or antenna cable. The existing 100 ns inter-output alignment rule is a separate P3335 decision, not settled by adopting G.703.

### Keep measurement choices appropriate to the claim

Use time error and time variation for 1PPS declarations, with explicit sampling and bandwidth. In G.810, the 10 Hz jitter/wander boundary concerns the frequency of timing variations, not the pulse repetition frequency. A once-per-second edge-error record does not by itself characterize a high-frequency jitter spectrum. [S7]

Do not remove ADEV everywhere. It describes fractional-frequency stability; TDEV describes time stability and relates to modified Allan deviation, not directly to ordinary ADEV. Likewise, a time-domain result does not automatically prove a phase-noise mask. Accept alternative measurements only where the claimed quantity and applicable profile support them. [S5]

Traceability is a property of a measurement result, not a privilege limited to PRTC devices. Clarify that a direct UTC(k) feed or an NMI laboratory visit is not required. A GNSS receiver or simulator can support a suitable test, but its reference, calibration, and uncertainty still need to support the particular claim. [S6, S8]

### Preserve implementation neutrality while improving testability

The test-access objective is strong, but requiring every implementation to add physical 1PPS, 10 MHz, and ToD test points would change the current logical-only and embedded conformance model. Require an independently usable verification route at each claimed measurement point, with physical access or a documented equivalent appropriate to the implementation. A device's self-reported value alone is not independent verification.

Similarly, a mandatory physical serial label, power monitor, or battery-health sensor needs an applicability rule. Clause 8 already contains a required instance selector and one conditional device serial object; it does not define the multiple equipment serial numbers described in the feedback.

### Reference and UTC updates are timely but need precise handling

ITU lists G.8260 (08/2026) as approved and in force, but prepublished with TIES-restricted text. G.Sup92 (07/2026) is approved and in force but marked to be published; its 10/2025 edition is superseded. Update the reference plan now, but complete the text and availability review before changing the normative baseline. [S2, S3]

CGPM Resolution 5 (2026) sets continuous UTC to become effective on 20 May 2027 and increases the permitted UT1-UTC difference to 3600 seconds. It does not specify a scheduled one-hour insertion. Keep historical conversion, current-offset validity, protocol interoperability, and discontinuity handling, while removing any implication that recurring leap events are an immutable future assumption. [S4]

## Proposed comment dispositions

Disposition labels describe recommendations, not completed actions:

- **Accept:** prepare a targeted clarification or addition.
- **Refine:** accept the objective with the technical qualifications stated.
- **WG decision:** scope, mandatory capability, or conformance policy needs agreement before editing it into the proposal.
- **Verify source:** obtain and review the exact source before adopting it.

### General structure and documentation

| ID | Source location | Topic and affected clauses | Proposed disposition |
|----|-----------------|---------------------------|----------------------|
| KG-01 | p. 1, General | Split the reference model from implementation Types | **WG decision.** First add a requirement-applicability matrix and worked configurations within the existing document. PCIe/GNSS, standalone GNSS/PTP, and PTP/PTP are useful examples, but are not an exhaustive or mutually exclusive classification. A multi-document restructuring requires a separate scope and maintenance decision. |
| KG-02 | pp. 1-2, Documentation | Public datasheet versus detailed documentation; 4.7, 4.8, 5.10, 6.1, 6.4.1, 6.11, 7.2.1, B.1, B.6, Annex D | **Refine.** Establish public claim information, integration information available to evaluators, and retained evidence with controlled access. State how to request restricted information. B.6 already recognizes restricted data. Do not equate confidentiality with permission to make an unsupported or unevaluable claim. |

### Pulse interfaces and batteries

| ID | Source location | Topic and affected clauses | Proposed disposition |
|----|-----------------|---------------------------|----------------------|
| KG-03 | p. 2, 1PPS | Adopt G.703 instead of a divergent profile; 7.3.2 | **WG decision.** Recommend aligning the Physical Timing Output profile with the specific G.703 measurement-interface clause. Distinguish that adoption from other receive and distribution interfaces. Resolve the voltage-table status and P3335-specific alignment limit at the same time. See S1 and the principal finding above. |
| KG-04 | p. 2, 1PPS | Informative G.703 summary and precedence | **Refine.** Add a short original summary and official download link, with the dated normative reference controlling its adopted requirements. Avoid duplicating extensive tables or creating two independent normative definitions. An additional annex is optional, not necessary to resolve the comment. |
| KG-05 | p. 2, 1PPS | Pulse width and rise time; 7.3.2 | **Refine.** Use the limits verified above if KG-03 is adopted. Correct the real rise-time mismatch; describe the pulse-width difference accurately as a narrower allowed range. Add the precise on-time marker and corresponding receive-compatibility tests. |
| KG-06 | p. 2, 1PPS | Maximum cable length; 7.3.2, 7.5, B.2 | **Refine.** Apply the cited length assumption to the adopted measurement arrangement, not every 1PPS installation, differential distribution link, or GNSS RF path. Continue to declare and compensate material fixture delay. |
| KG-07 | p. 2, 1PPS | Writable receive-cable delay compensation; 7.2, 8.10.3 | **WG decision.** The common configurable object is missing. Define a per-interface correction with units, sign, bounds, readback, persistence, authorization, and application point. Resolve together with the broader GNSS/input proposal KG-42. |
| KG-08 | p. 2, Batteries | Are backup batteries permitted; 9.4.2, 9.6.2 | **Accept.** State explicitly that backup energy is optional. Existing clauses already cover claimed backup energy and list batteries as service-life items. Clarify whether backup preserves configuration, an RTC, the unified timescale, or actual providing-interface service. |
| KG-09 | p. 2, Batteries | Battery documentation and shipping | **Refine.** Add chemistry, rating, replaceability, service and disposal information, plus identification of applicable transport documentation. Do not assert one universal rule for every battery: chemistry, installation, transport mode, and jurisdiction matter. Regulatory compliance remains outside P3335 conformance. See S10. |
| KG-10 | p. 2, Batteries | Battery state and condition objects | **WG decision.** Define capability-scoped battery telemetry and fault semantics. Distinguish an absent battery from present but unmonitored energy storage. Do not imply that every backup cell can measure state of charge or health. Consolidate with KG-41. |

### Terminology and conformance

| ID | Source location | Topic and affected clauses | Proposed disposition |
|----|-----------------|---------------------------|----------------------|
| KG-11 | p. 3, References | G.8260 (08/2026); 1.5, 2.1, Clause 6, reference audit | **Verify source.** The revision exists and was approved on 29 August 2026. Obtain an authorized copy, compare definitions and metric provisions, and resolve availability before replacing the dated baseline. Do not only change the year. See S2. |
| KG-12 | p. 3, References | Add G.Sup92; 10.2.1, C.1 | **Verify source.** Recommend an informative reference. The current approved edition is 07/2026 and is awaiting publication, not the superseded 10/2025 edition. Record the exact edition actually reviewed and refresh at publication freeze. See S3. |
| KG-13 | p. 3, 3.1 | Define gateware | **Accept.** Define the configuration or logic description used to implement functions in programmable logic, such as an FPGA. Keep it distinct from processor-executed firmware; avoid relying only on the analogy to firmware. |
| KG-14 | p. 3, 3.2 | Remove unused abbreviations | **Accept.** CFM and LFM are indeed unused outside the list. The audit also identified DMTF, EMI, LOS, NMI, OCP, OCP TAP, TAP, TIE, TLS, microsecond-symbol, and WR entries for editorial review. Recheck after revisions, including figure text and newly added references. |
| KG-15 | p. 3, 3.2 | BeiDou and Galileo | **Refine.** Both names are already used in 8.10.7, so explain them consistently with the other constellations. They are names, not acronyms to be given invented expansions. A short constellation terminology table is suitable. |
| KG-16 | p. 3, first 4.3 comment | Mandatory timing test access | **WG decision.** Require a practical verification route for each claimed timing quantity. Do not require unimplemented signal types or physical pins on every logical-only implementation. Document any fixture and how it relates to the actual providing-interface measurement point. |
| KG-17 | p. 3, first 4.3 comment | Internal test-point alignment and accessibility | **Refine.** When physical test points are the verification route, identify them and document connection, loading, safety, delay, uncertainty, and alignment. Avoid destructive rework. Permit a supplied or specified fixture when ordinary probes are unsuitable; banning all custom probes could exclude legitimate high-speed interfaces. |
| KG-18 | p. 3, second 4.3 comment | Refer to a performance specification instead of repeating metric declarations | **Refine.** Allow incorporation by an exact document edition, class, clause, configuration, and measurement point. Preserve declarations for uncovered P3335 requirements and implementation-specific conditions. A bare standard number is insufficient. |
| KG-19 | p. 4, 4.4 | Embedded implementation test access | **WG decision.** Same policy as KG-16. The current equivalent-measurement-point requirement is a useful starting point but does not establish access or independent verifiability. Preserve the logical-interface route unless the WG deliberately changes scope. |
| KG-20 | p. 4, first 4.5 comment | Add UTC(k) to receive interfaces | **Refine.** Explain UTC(k) as a reference-timescale realization conveyed through a declared signal or protocol, for example 1PPS plus ToD. It is not itself an electrical or packet interface type. Align 4.5, 6.4.1, and Figure 3 accordingly. |
| KG-21 | p. 4, second 4.5 comment | Undefined environmental profiles | **Accept.** Remove or qualify the example bullet so it does not imply P3335 defines numeric data-centre, telecom, or industrial profiles. Clause 9 already mandates environmental declarations; no universal operating range is needed to retain that declaration model. Also review the optional-feature definition and 4.3. |
| KG-22 | p. 4, 4.6 | Recognize external performance standards | **Refine.** Explicitly permit supplier, application, and external-standard classes. Require identification and conditions for every claimed class, not only supplier-defined ones. Do not import an unfinished clock specification as an approved normative dependency. The precise G.FTS-Lite-clk source remains to be obtained; the related G.FTS-Lite profile work item is still under study. See S11. |
| KG-23 | p. 4, 4.8 | Require functional and performance testing | **Accept.** Require evidence appropriate to applicable functional and performance requirements, with documentary review for documentary requirements. Clarify that self-declaration is possible and that neither an accredited third-party lab nor production-unit testing is automatically required. Coordinate with Annex D evidence fields. |

### Architecture and performance

| ID | Source location | Topic and affected clauses | Proposed disposition |
|----|-----------------|---------------------------|----------------------|
| KG-24 | pp. 4-5, Leap Seconds | Future UTC behavior; 5.3.2, 10.3.4, E.4 | **Refine.** Update to the adopted continuous-UTC decision, not a speculative leap-hour mechanism. Preserve conversion of historical timestamps, validity of UTC/TAI relationships, legacy protocol flags, and declared behavior for unsupported adjustments. Check related 8.10.4 semantics too. See S4. |
| KG-25 | p. 5, Time Jitter | 1PPS time error versus jitter; 3.1, 5.7, 6.7, 7.3.2, A.1, A.6 | **Refine.** Use pulse time error and explicitly defined time-variation statistics as the general terms. Explain domain-specific jitter/wander terminology and sampling limits. Retain jitter where a defined interface/profile genuinely uses it; do not base the terminology solely on pulse repetition rate. See S7. |
| KG-26 | p. 5, first 5.7 comment | Referenced numeric requirements | **Accept.** Explain that numeric limits can be stated directly or incorporated by a specific normative reference. Distinguish incorporation from an informative citation or a supplier's separately claimed application profile. |
| KG-27 | p. 5, second 5.7 comment | Keep categories separate from metric lists | **Accept.** Remove parenthetical metric examples from the category list and point to Clause 6 and Annex A for selection. This is a readability change, not a decision to delete those metrics. |
| KG-28 | p. 5, 5.9 | Optional status LEDs | **Accept.** Permit local indicators on suitable physical products. Document their meaning and failure/invalid states when implemented; keep the control interface authoritative. Do not mandate a particular colour scheme or LEDs on embedded logic. |
| KG-29 | p. 5, 5.10 | Protect PLL and disciplining intellectual property | **Refine.** Require externally observable response, relevant bandwidth/masks, operating modes, and limitations rather than proprietary loop topology or algorithms. Bandwidth alone may not characterize adaptive or nonlinear loops. Preserve reproducibility of the noise-transfer/tolerance claims in 6.4.2 and 6.4.3. |
| KG-30 | p. 6, 6.3 | Permit GNSS and simulator reference arrangements | **Refine.** Clarify suitable calibrated laboratory, GNSS, and simulator arrangements without removing measurement traceability or uncertainty. The current text already permits another declared reference. Distinguish output error relative to the supplied reference from an absolute UTC claim, including common-reference error cancellation. See S6 and S8. |
| KG-31 | p. 6, Phase noise | Substitute time-domain verification; 6.6, A.5, B.4.4 and related mentions | **Refine.** Permit a profile-defined time-domain assessment where appropriate, but retain spectral characterization for a spectral claim. Retain the conversion-method and bandwidth safeguards; a single integrated result cannot establish compliance at every offset frequency. See S5. |
| KG-32 | p. 7, Allan Deviation | Remove ADEV; 6.6, A.2, B.4.2, D.7 | **Refine.** Do not delete ADEV globally. Make applicability explicit at declared TimeCard outputs and avoid demanding confidential internal-component characterization. Retain fractional-frequency offset, TDEV, and ADEV as distinct quantities. ADEV is not confined to short-term analysis of isolated oscillators; NIST also applies it to UTC(NIST). See S5 and S9. |
| KG-33 | p. 7, 6.8 | Replace holdover checklist with external standards | **Refine.** Permit precise incorporation of an applicable holdover class, but retain fallback reporting for devices without one and identify entry conditions and initial error. Also resolve the additional MTIE issue below before accepting any holdover wording. |
| KG-34 | p. 7, 6.9 | Replace dynamic-operation checklist with external standards | **Refine.** Permit references for covered transitions, while retaining P3335 coverage of host sleep, removal, driver restart, and correlation invalidation. A telecom clock profile may not cover those host behaviors. |
| KG-35 | p. 7, 6.11 | Include applicable standards in reporting | **Accept.** Add governing document, edition/amendment, clause, class/mask, and configuration to the declaration checklist and Annex D. Distinguish a governing requirement from background material. |
| KG-36 | p. 7, 7.2.4 | Reference G.703 for receive interfaces | **Refine.** Identify the supported G.703 interface where claimed, with matching acceptance and termination declarations. Do not require every proprietary or embedded pulse input to implement the same physical interface. Coordinate with KG-03 and KG-05. |
| KG-37 | p. 7, 7.3.1 | Behavior during software updates | **Accept.** Add firmware, gateware, and software update/restart explicitly to output validity and continuity declarations. Clause 6.9 already covers timing-degrading updates; this closes a cross-clause omission rather than introducing an unrelated requirement. |
| KG-38 | pp. 7-8, 7.3.2 | Add BNC | **Accept.** Name a mechanically retained 50 ohm BNC explicitly; retain TNC and the other supported examples. The existing generic connector allowance is broad, but an explicit example removes uncertainty. Avoid treating a 75 ohm BNC as the same profile. |

### Control model environment and test guidance

| ID | Source location | Topic and affected clauses | Proposed disposition |
|----|-----------------|---------------------------|----------------------|
| KG-39 | p. 8, Serial Number | Equipment identity and exterior label; 8.10.2, 8.10.3 | **WG decision.** Strengthen persistent product identity for physical units and its relationship to a visible label. Reuse `TC_SERIAL`; do not add a second competing serial object. Preserve `TC_INSTANCE_ID` for selecting instances and define identity for multiple logical instances within one product. |
| KG-40 | p. 8, Power Reporting | Power status and dip alarms | **WG decision.** Add a capability-scoped power-state model, measurable rail/alarm conditions, detection limits, and retention behavior. A fully unpowered device cannot necessarily report its loss through the failed interface. Specify backup/out-of-band reporting or post-restart event evidence where supported, not an impossible universal live alarm. |
| KG-41 | p. 8, Power Reporting | Conditional battery health/status objects | **WG decision.** Duplicate of KG-10; resolve in one battery model with shared capability, validity, alarm, and evidence rules. |
| KG-42 | p. 8, 8.10.3 | GNSS and other input cable compensation | **WG decision.** Extend KG-07 to per-source/per-interface delay handling. Distinguish physical path delay from an already-applied receiver correction, define sign and effective timing point, and prevent double correction. Specify readback and safe behavior for unsupported or invalid writes. |
| KG-43 | p. 8, Environmental units | Units in Clause 9 and Annex D | **Refine.** Specify SI units and permitted prefixes: degrees Celsius, percent relative humidity plus condensation condition, metres, pascals, kilograms, watts, and volts. Millimetres are practical for mechanical drawings. Use Pa or kPa for pressure; bar/mbar can be supplementary declared units, not labelled SI units. See S12. |
| KG-44 | pp. 8-9, 10.2 | Application-specific references | **Accept.** Link each application paragraph to relevant, edition-checked references. Start with data-centre guidance, telecom clock/PTP profiles, the existing power-system profile, and metrology sources. Select any financial or industrial regulatory examples for their actual jurisdiction and application rather than implying universal applicability. |
| KG-45 | p. 9, Annex A | Identify selected masks; A.3, A.4, A.7, A.9, Annex D | **Accept.** Add an exact mask/profile identifier, edition, parameter set, intervals, filtering, and acceptance rule to normative declarations in Clause 6 and the Annex D proforma. Annex A can explain these but cannot create the obligation by itself. |
| KG-46 | p. 9, Annex A | TDEV and MTIE units | **Accept.** State that both are expressed in seconds, with labelled submultiples permitted. Identify the units of time-error samples and averaging/observation intervals separately. |
| KG-47 | p. 9, A.6 | Clarify time jitter and overlap with phase noise | **Refine.** Consolidate with KG-25 and KG-31. Recast A.6 around pulse/event time error and timing variation, with domain-specific jitter clearly scoped. Do not treat all time-domain and spectral metrics as interchangeable. |
| KG-48 | p. 9, B.1 | Figure 3 optional interfaces | **Accept.** Make the fixture explicitly illustrative and label reference, input, output, and measurement paths by function. Show packet/host measurement alternatives where useful without implying every optional interface is required. Also address the missing independent measurement-reference connection noted below. |
| KG-49 | p. 9, B.1 | UTC(k) in Figure 3 but not 4.5 | **Refine.** Resolve with KG-20: separate reference origin/timescale from the interface conveying it. A lab reference label should not imply a mandatory DUT input type. |
| KG-50 | p. 9, B.1 | Remove ADEV from Figure 3 | **Refine.** Replace the fixed analyzer list with a generic applicable-metrics label, or mark the list as examples. This diagram simplification does not justify deleting ADEV from the standard. See KG-32. |
| KG-51 | p. 9, B.3.2 | Add PTP and other host-bus output tests | **Accept.** The PTM row is already conditional on a profile with PTM, so PTM is not currently mandatory there. Add conditional PTP, IRIG, and other declared host/logical-output examples to improve balance and coverage. Keep common format, validity, alignment, and continuity tests applicable across interfaces. |

## Additional issues exposed by the review

### MTIE cannot replace an absolute holdover error bound

Clause 6.8 currently requires MTIE when reporting bounded holdover time error. Annex A.4 defines MTIE as peak-to-peak variation, so it removes constant offset: a record with a constant 1 microsecond error has zero MTIE. An MTIE curve alone therefore cannot establish an absolute time-error bound or capture the initial offset at holdover entry.

Recommended correction: require the absolute or explicitly initial-offset-relative error envelope appropriate to the claim, together with initial-error treatment. Require MTIE in addition when the claimed profile or stability claim calls for it. Keep these quantities distinct in 6.5, 6.8, A.9, B.4.8, and D.7. This follows directly from the draft's own definitions, independently of Kevin's preference for external profiles.

### Figure 3 omits the measurement reference path

The current SVG connects the reference only to the DUT. The counter and analyzer receive DUT outputs but no reference/comparison connection. A standalone drawing of a time-error test should show the measurement reference, or explicitly show the analyzer's independent internal reference, and identify common-reference correlations. Correcting this matters more than merely adding optional interface names.

### Control additions require more than new table rows

Delay, battery, and power objects need capabilities, records, states, units, access rights, event behavior, persistence, tests, and version compatibility. Adding names alone would leave different implementations free to interpret the same object differently. Close these together with the existing information-model and identifier-governance actions.

## Candidate wording for discussion

These passages illustrate the recommended direction. They are not approved requirements and have not been inserted into the manuscript.

### Documentation availability

> The supplier shall identify the documentation and evidence supporting each conformance claim and shall state how evaluators can obtain them. A public claim summary shall identify the implementation, claimed profiles and interfaces, bounded performance claims and conditions, and environmental limits. Detailed interface documentation and supporting evidence may be supplied through controlled access arrangements that permit evaluation of the claim. Disclosure of proprietary internal designs, source code, or disciplining algorithms is not required by this standard. Confidentiality arrangements shall not substitute for evidence of an applicable requirement.

The WG should settle the access policy for commercial, custom, embedded, and non-commercial implementations before finalizing this wording. Safety, regulatory, or independently binding disclosure obligations are not relaxed by it. Reconcile 4.7, 5.1, 5.10, 6.1, B.6, and Annex D as one edit.

### Verification evidence

> A conformance claim shall be supported by functional test evidence for applicable functional requirements and performance test evidence for applicable measured-performance requirements. Documentation review shall verify applicable documentation and declaration requirements and may evaluate the supporting test records; it shall not substitute for evidence that the claimed functions and performance have been demonstrated. The evidence shall identify the tested implementation, configuration, measurement method, uncertainty where applicable, result, and applicable requirement.

Add a separate clarification that the supplier may perform the evaluation unless a claimed profile or external obligation requires otherwise. Describe how evidence for a tested configuration supports a product family without implying that every shipped unit receives the complete qualification suite.

### External performance profiles

> An implementation may claim a supplier-defined, application-defined, or externally standardized performance class. For each claimed class, the conformance statement shall identify the governing document and edition, applicable clauses and masks, implementation configuration, measurement points, operating conditions, and supporting evidence. Incorporation by reference does not waive an applicable P3335 requirement that the referenced specification does not cover.

Do not add an undated dependency on the latest revision or use a document under development as though it were an approved standard.

### Measurement references

> The reference arrangement shall be suitable for the measurand, declared limit, and uncertainty of the reported result. Suitable arrangements may include calibrated laboratory references, characterized GNSS references, or characterized GNSS simulators. The report shall identify the reference timescale or frequency, the calibration and reference relationships supporting the result, and the relevant uncertainty contributions. A comparison relative to an applied input reference shall be distinguished from an absolute time-accuracy claim relative to UTC or another external timescale.

Retain the definition of metrological traceability and clarify how it applies to the result. This addition is not a blanket exemption from calibration, nor an assertion that any simulator provides an absolute UTC reference.

### Verification access

> For each declared timing-performance measurement point, the supplier shall specify an independently usable verification method and the access needed to perform it. The method may use an implemented providing interface, an accessible test point, or a documented equivalent fixture or logical measurement method. The supplier shall characterize the relationship between any auxiliary test point and the claimed measurement point, including loading, delay, correction, and uncertainty.

Whether physical test points are mandatory for particular product profiles remains a WG decision. Do not add all three example signal types to base conformance implicitly.

## Recommended action sequence

Suggested owners below are roles for assignment, not commitments by named people. All implementation actions remain open.

| Order | Action package | Suggested owner | Completion criterion |
|-------|----------------|-----------------|----------------------|
| 1 | Agree documentation tiers and evidence policy, KG-02, KG-23, KG-29 | Editor with suppliers and test specialists | One consistent availability policy; no undocumented exemption from applicable testing; no requirement to reveal proprietary algorithms. Review 4.7, 4.8, 5.1, 5.10, 6.1, B.6, and Annex D together. |
| 2 | Resolve 1PPS and test access, KG-03 through KG-07, KG-16, KG-17, KG-19, KG-36, KG-38 | Interface and conformance reviewers | WG records the adopted interface, binding limits, marker, cable/test assumptions, connector examples, receive compatibility, alignment limit, and embedded verification route. Link to existing actions AI-003 and AI-004. |
| 3 | Resolve metric and reference semantics, KG-25, KG-30 through KG-34, KG-45 through KG-47 | Metrology reviewers | Distinct time-error, stability, spectral, and uncertainty claims; corrected holdover rule; validated reference examples; no inappropriate universal metric deletion. Link to AI-021 and AI-028. |
| 4 | Specify installation and power control objects, KG-07 through KG-10, KG-39 through KG-42 | Control-model reviewers | Complete records and capability rules, identity behavior, calibration sign examples, write rejection, persistence, and test cases. Link to AI-006 and AI-018. |
| 5 | Refresh external references and UTC discussion, KG-11, KG-12, KG-22, KG-24, KG-44 | Reference editor and liaison reviewers | Exact approved/available editions recorded; authorized G.8260 comparison complete; current UTC decision represented accurately; unfinished sources clearly separated. Link to AI-007 and AI-017. |
| 6 | Prepare low-risk editorial changes, KG-13 through KG-15, KG-21, KG-26 through KG-28, KG-35, KG-37, KG-43, KG-46 | Editor | Definitions, units, categories, indicator guidance, update behavior, and cross-references consistent. Abbreviation audit rerun after edits. |
| 7 | Update figures and verification examples, KG-48 through KG-51 | Test and figure editors | Figure 3 shows a valid measurement arrangement; conditional interface examples are balanced; Annex B remains informative. Extend tests for any newly adopted objects and profiles. |
| 8 | Decide document organization, KG-01, KG-18 | WG chair and editor | Publish an applicability matrix and examples first; record whether separate future profiles or documents are warranted. Avoid making a document split a prerequisite for unrelated corrections. |

After approved edits: regenerate `REQUIREMENTS_INDEX.md`, run `make check`, rebuild and visually inspect the proposal PDF, and check all altered conformance declarations against Annex D. Recheck references and publication metadata before any push. No push, commit, or claim of comment closure is part of this review.

## Source checks

The following sources support the technical qualifications and status checks above. Recommendations about how P3335 should change are editorial and technical judgments, not decisions attributed to these organizations.

- **S1:** ITU-T G.703 (04/2016), Amendment 1 (05/2021), particularly 19.1 and 19.2 and Tables 19-5 and 19-6. [Official catalog and download](https://www.itu.int/rec/T-REC-G.703-202105-I!Amd1/en). The official PDF was inspected directly.
- **S2:** [G.8260 (08/2026) official record](https://www.itu.int/rec/T-REC-G.8260-202608-P/en). Approval and restricted prepublication status verified; full revised text not reviewed.
- **S3:** [G.Sup92 (07/2026) official record](https://www.itu.int/rec/T-REC-G.Sup92-202607-I/en) and [edition history](https://www.itu.int/rec/T-REC-G.Sup92/en). Current approval and publication status verified; the 2026 text was not available for review through the catalog.
- **S4:** BIPM, [Resolution 5 of the 28th CGPM](https://www.bipm.org/en/cgpm-2026/resolution-5), 2026. Adopted continuous-UTC decision and effective date, not the earlier draft resolution.
- **S5:** NIST, [Handbook of Frequency Stability Analysis](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication1065.pdf), SP 1065, particularly 5.2.2, 5.2.6, 5.2.19, and Clause 7 on domain conversions.
- **S6:** JCGM, [International Vocabulary of Metrology](https://www.bipm.org/documents/20126/2071204/JCGM_200_2012.pdf), JCGM 200:2012, 2.41 on metrological traceability.
- **S7:** ITU-T, [G.810 (08/1996)](https://www.itu.int/rec/T-REC-G.810-199608-I/en), 4.1.12 and 4.1.15 on jitter and wander.
- **S8:** ITU-T, [G.8272 (07/2025)](https://www.itu.int/rec/T-REC-G.8272-202507-I/en), Appendix I, including I.3.3 on GNSS simulator comparison. This publicly available edition was inspected; the [catalog](https://www.itu.int/rec/T-REC-G.8272/en) also lists an 08/2026 amendment in prepublication, which still needs review before selecting an updated normative baseline.
- **S9:** NIST, [Performance of UTC(NIST) and UTC(NIST) Adjustments](https://www.nist.gov/pml/time-and-frequency-division/time-realization/utcnist-time-scale/performance-utcnist-and-utcnist). Figures 12 and 13 use TDEV and overlapping ADEV for timescale performance.
- **S10:** PHMSA, [Lithium Battery Test Summaries](https://www.phmsa.dot.gov/training/hazmat/new-un-requirement-test-summaries), revised guidance. The guidance distinguishes covered lithium cells/batteries and exceptions, illustrating why the draft should refer to applicable obligations rather than state an unqualified rule for every battery. This is not a shipment-specific compliance determination.
- **S11:** ITU-T, [G.FTS-Lite work item](https://www.itu.int/itu-t/workprog/wp_item.aspx?isn=23831), listed as under study. This is the related PTP profile work item, not verification of the separate G.FTS-Lite-clk document named by Kevin.
- **S12:** NIST, [Guide to the SI, Chapter 4](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes), for derived units and prefixes, including the pascal for pressure.
