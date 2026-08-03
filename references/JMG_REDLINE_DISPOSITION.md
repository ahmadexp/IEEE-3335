# JMG Redline Comment Disposition

Source reviewed: `IEEE3335 (20260730) JMG Redline.pdf`

## Action items

| Action item | Status | Resolution |
|-------------|--------|------------|
| A1. Apply IEEE requirement styling | Closed | Every `shall` in the manuscript is bold, and the draft check rejects an unbolded occurrence. |
| A2. Control normative references | Closed | All 14 references have numbered identifiers and fixed editions; later editions require a P3335 amendment or revision. |
| A3. Close terminology and acronym gaps | Closed | Added or clarified evidence, precision, granularity, resolution, receive interface, reference signal, unspecified, traceability, BAR, DCLS, TNC, and other used acronyms. |
| A4. Bound traceability claims | Closed | P3335 now describes TimeCard evidence supporting system-level traceability analysis and avoids asserting end-to-end traceability. |
| A5. Tighten conformance statements | Closed | Minimum claim content, publication and supply obligations, and Annex B precedence are explicit. |
| A6. Clarify performance transitions | Closed | Holdover conditions, reference restoration, phase derivatives, and environmental and host-system effects are explicit. |
| A7. Improve timing-interface requirements | Closed | Added threaded connector options, fixed-edition protocol citations, and observable extension behavior. |
| A8. Improve control-interface requirements | Closed | Clarified PCIe scope, IPMI namespaces, SNMP obligations, atomicity, extension compatibility, units, evidence objects, and security declarations. |
| A9. Complete environmental declarations | Closed | Added normal-operation entry, storage degradation, shock and vibration standards, and regulatory wording. |
| A10. Polish informative guidance | Closed | Expanded error budgets, thermal independence, cabling changes, correlated failures, monitoring, physical failures, and IEEE 1193 context. |
| A11. Repair table layout | Closed | Added stable wrapping column widths and row spacing across all manuscript tables. |
| A12. Repair figure layout | Closed | Enlarged type, increased contrast, simplified labels, and rebuilt all three diagrams with print-stable geometry. |

## Detailed disposition

| ID | PDF page | Comment topic | Disposition |
|----|----------|---------------|-------------|
| 1 | 1 | Bold all `shall` terms | Accepted. All manuscript occurrences are bold and automatically checked. |
| 2 | 7 | Tables unreadable; widen content and separate rows | Accepted. A table-layout filter assigns wrapping widths by column count, and table row spacing is increased. |
| 3 | 7 | Dated and undated reference boilerplate | Accepted. The clause now permits only the explicitly dated editions. |
| 4 | 7 | Prevent scope creep with issue dates | Accepted. Every normative entry identifies an issue date, edition, or dated amendment. |
| 5 | 7 | Number references and cite by identifier | Accepted. Clause 2 uses [1] through [14], and normative body citations use those identifiers. |
| 6 | 8 | Align or explain relationship with IEEE 1588 terms | Accepted. Clause 3 and A.7 define P3335 declaration semantics and state the IEEE 1588 protocol precedence. |
| 7 | 8 | Dictionary referral | Accepted with comment 8. The sentence was deleted. |
| 8 | 8 | Delete IEEE Standards Dictionary sentence | Accepted. The sentence was deleted so Clause 3 closes the terms used by P3335. |
| 9 | 8 | Define evidence | Accepted. Clause 3 defines records and material used to evaluate a conformance claim. |
| 10 | 8 | Clarify ensemble operation | Accepted. The definition now describes combined selected observations producing a synthesized reference. |
| 11 | 8 | Align granularity with A.7 | Accepted. Clause 3 and A.7 use the same representable-step meaning and distinguish other metrics. |
| 12 | 9 | Add precision | Accepted. Precision is defined in Clause 3 and retained in A.7. |
| 13 | 9 | Clarify receive interface and reference signal | Accepted. Both definitions now identify the inbound boundary, measurement point, marker, and use. |
| 14 | 9 | Align resolution with A.7 | Accepted. Clause 3 and A.7 use consistent indication-based wording. |
| 15 | 9 | Limit TimeCard traceability claim | Accepted. Clauses 1, 3, 5, and 8 now frame TimeCard declarations as support for system-level analysis. |
| 16 | 9 | Define unspecified | Accepted. Clause 3 distinguishes it from unknown, unavailable, and unsupported. |
| 17 | 9 | Define BAR | Accepted. BAR is added to 3.2. |
| 18 | 9 | Qualify DCLS as IRIG | Accepted. DCLS is identified as IRIG time-code modulation. |
| 19 | 11 | Add at least the following | Accepted in 4.2. |
| 20 | 11 | Timing output providing terminology | Accepted in the first base conformance requirement. |
| 21 | 11 | Timing output providing terminology | Accepted in the second base conformance requirement and logical-only profile text. |
| 22 | 13 | Conformance statement both published and supplied | Accepted in 4.7. |
| 23 | 13 | Annex B does not add, change, or replace | Accepted in 4.8. |
| 24 | 14 | Figure 1 illegible | Accepted. Figure 1 uses larger type, stronger contrast, shorter labels, and explicit connectors. |
| 25 | 16 | Figure 2 illegible | Accepted. Figure 2 uses larger type, stronger contrast, and a simplified holdover path. |
| 26 | 20 | Replace applicable references wording | Accepted. Holdover begins after loss of all external references being used. |
| 27 | 21 | Expand holdover conditions and restoration | Accepted. Sensor location, thermal profile, voltage, qualification, transients, continuity, and relock are stated. |
| 28 | 21 | Cover phase-derivative discontinuities | Accepted. Phase steps, frequency steps, slope changes, kinks, corners, and recovery transients are covered. |
| 29 | 21 | Explain system-integration effects | Accepted. The heading is now Environmental and host-system effects. |
| 30 | 22 | Later reference releases require P3335 update | Accepted in the Clause 2 applicability rule and the PCIe mapping text. |
| 31 | 23 | Support TNC and Type-N connectors | Accepted. The profile permits SMA, TNC, Type-N, or another retained 50 ohm coaxial connector with an SMA test adapter. |
| 32 | 25 | Extension requirement too vague | Accepted. It now specifies preserved syntax, semantics, states, errors, discovery, and namespace behavior. |
| 33 | 26 | PCIe requirement scope unclear | Accepted. Each implemented PCIe control mapping is covered. |
| 34 | 26 | Unique IPMI command identifiers | Accepted. Extension commands cannot redefine, alias, or overlap standard identifiers. |
| 35 | 26 | Cannot conform to an architecture | Accepted. The SNMP clause identifies applicable framework elements and required declaration fields. |
| 36 | 27 | Consumer unclear | Accepted. The text uses receiving implementation and states the compatibility behavior being solved. |
| 37 | 27 | Coherent should be atomic | Accepted. The heading and requirements consistently use atomic reads. |
| 38 | 28 | Add BAR and perform acronym sweep | Accepted. BAR and all substantive undefined acronyms found by the sweep were added or removed from figures. |
| 39 | 29 | TC_TIME should be atomic | Accepted. `TC_TIME` is an atomic unified-timescale value. |
| 40 | 30 | Ink markup on table collision | Accepted with comment 41. Column widths now reserve adequate identifier and semantics space. |
| 41 | 30 | Text collisions | Accepted. The rendered object tables wrap without overlapping adjacent columns. |
| 42 | 30 | Temperature in degrees Centigrade | Accepted using the SI term Celsius. Units are `mdeg C`, and the semantics state millidegrees Celsius. |
| 43 | 30 | Traceability state is invalid | Accepted. `TRACEABILITY_STATE` was replaced by `REFERENCE_EVIDENCE`, which reports evidence availability without asserting traceability. |
| 44 | 31 | Implementation with no security needs | Accepted. `none` is an explicit valid declaration, and mechanisms are required only by applicable claims or profiles. |
| 45 | 32 | Declare normal-operation start | Accepted in 9.2, distinct from first usable, locked, and full-performance milestones. |
| 46 | 32 | Storage damaged or degraded | Accepted in 9.1. |
| 47 | 33 | Shock and vibration governing standard | Accepted. The declaration includes the governing standard and edition, if any. |
| 48 | 35 | Add only to regulatory wording | Accepted in 9.8. |
| 49 | 35 | Informative clause does not add or alter requirements | Accepted in Clause 10 introduction. |
| 50 | 35 | Add error and uncertainty budget | Accepted in 10.1. |
| 51 | 36 | Thermal effects independent of ambient | Accepted in 10.3.1. |
| 52 | 36 | Add including to installation changes | Accepted with concrete examples in 10.3.2. |
| 53 | 36 | Use correlated failure | Accepted throughout the affected informative guidance. |
| 54 | 36 | Monitor at least listed items | Accepted in 10.4.2. |
| 55 | 37 | Add loose connectors and broken cables | Accepted in the common integration failures table. |
| 56 | 37 | Identify IEEE 1193 basis | Accepted in the Annex A introduction, with IEEE 1193 retained as the controlling source when normatively cited. |
| 57 | 39 | Make IEEE 1588 alignment explicit | Accepted in A.7 with separate protocol and P3335 declaration precedence. |
| 58 | 40 | Figure 3 illegible | Accepted. Figure 3 uses larger type, stronger contrast, and explicit signal paths. |
