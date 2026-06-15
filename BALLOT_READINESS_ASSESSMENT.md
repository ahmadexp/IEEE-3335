# IEEE P3335 Ballot-Readiness Assessment

_Assessment date: 2026-06-15. Scope: what remains before this draft can enter IEEE SA ballot and proceed to a published standard. This complements `PUBLICATION_READINESS.md` (the editorial punch list) by focusing on the IEEE SA process gates and the work that gates them._

## Bottom line

The **technical draft is in good shape**. All thirteen clauses and annexes are written, internally consistent, use proper `shall`/`should`/`may`/`can` requirement language, carry no leftover `TODO`/`TBD`/placeholder markers, and are backed by a generated requirements index (~162 indexed normative statements across Clauses 4–9), an architecture/conformance model with profiles, a normative-reference audit, and source-controlled figures. Content is not the blocker.

The blockers to balloting are **procedural and format-related**, and they sit against a **hard schedule constraint**. Roughly in priority order: (1) the PAR timeline, (2) ratifying the open working-group decisions, (3) converting the draft from Markdown into the IEEE SA MS Word template and passing Mandatory Editorial Coordination (MEC), (4) closing the normative-reference legal/editorial review, then (5) running the myProject ballot machinery through RevCom and publication.

---

## 1. Critical path / schedule (do this first)

**The PAR expires at the end of 2026.** P3335 ("Standard for Architecture and Interfaces for Time Card") was approved by NesCom on 2022-12-02; IEEE PARs are valid for four years, which places expiration at **31 December 2026 — about six months out.**

What this means practically:

- To finish under the current PAR you would need to pass MEC, open and close ballot (75% return, 75% approval), resolve comments and recirculate, and reach RevCom — all before year end. That is aggressive but not impossible if the draft is already mature.
- More realistically, **file a PAR extension request with NesCom before the PAR lapses.** A draft has been generated and you can demonstrate progress, so an extension (1–4 years, typically ≤2) is well within the rules. Extensions are blocked only if no draft exists after 4 years, or once a project hits 8 years from original approval without having initiated ballot — neither applies here.
- **Recommended action this quarter:** decide between "ballot under current PAR" vs. "file extension," and if extending, submit the request through myProject now rather than near the deadline.

Governance note: the WG page lists **Vice Chair and Secretary as TBD.** IEEE expects these officer roles filled; resolve before ballot formation.

---

## 2. Working-group decisions that must be ratified

`PUBLICATION_READINESS.md` records several items as "draft-resolved; WG ratification needed." These are editorial proposals that have **not yet been adopted by a working-group vote**, and ballot comments will reopen any that aren't formally closed:

- **AI-003 / AI-004 — 1PPS status.** Drafted as a *Physical Timing Output* profile requirement (not base conformance). WG must ratify.
- **AI-008 — Performance-class strategy.** Drafted as reporting-only with no universal numeric minima. WG must ratify (some telecom/finance balloters may push for named classes).
- **AI-010 — Annex B status.** Drafted as informative test procedures, not a normative conformance-test suite. WG must ratify.
- **PICS deferral (Clause 4.9).** No Protocol Implementation Conformance Statement in this draft. Acceptable, but confirm the WG accepts shipping without one, or schedule it.

Capture each of these as a recorded WG motion/vote so the resolution is defensible during ballot.

---

## 3. Format and editorial conformance (gates MEC)

This is the largest concrete work item. The draft today is **Markdown compiled to a generic Pandoc/LaTeX PDF**. IEEE SA ballot drafts must be submitted through myProject in the **IEEE SA MS Word template** and must pass **Mandatory Editorial Coordination (MEC)** before ballot opens. MEC checks draft labeling, copyright statements, title/front matter, and IEEE SA Style Manual conformance.

Required before/for MEC:

- **Port the content into the IEEE SA Word template**, including title page, copyright/permissions statement, abstract and keywords, participants/acknowledgements list, and an Introduction. The metadata file (`metadata.yaml`) currently carries only title/author placeholders.
- **Front-matter and labeling:** "Draft" labeling, draft number/date in headers, line numbering for ballot comments.
- **Trademark attribution:** first use of IEEE Std 1588™, 802.1AS™, etc. needs the trademark/citation treatment the Style Manual requires.
- **Terminology consistency:** the draft mixes "compliant/compliance" (Clauses 7–9) with "conforming/conformance" (Clauses 4–5). IEEE SA style prefers "conformance." Also normalize "this standard" vs. "this document"/"this specification."
- **Figures:** the three SVG/PDF figures are functional placeholders. MEC/RevCom expect professional, editable, properly captioned and in-text-referenced figures; confirm they meet the template's figure standards and that source files are retained.
- **Equations and units:** Annex A equations and SI units should be checked against Style Manual formatting.
- **Undefined acronyms used in text:** e.g., BeiDou, DCF77, MSF, O-RAN, PMU, SCADA, PDV, SSB, TDC, LFM, CFM, BTU, MiFID, LOA. Either add to Clause 3 or expand on first use.

---

## 4. Normative references — finish the legal/editorial review

`references/NORMATIVE_REFERENCE_AUDIT.md` confirms every Clause 2 entry is cited by normative text (good), but every entry is still marked "confirm edition/availability." Before ballot:

- Verify each reference is **indispensable** (a true normative dependency), publicly available, and free of impermissible commercial terms. Open/industry specs (SMBus, MIPI I3C, PCIe, DMTF, IRIG) need availability and citation-format confirmation.
- Resolve **edition questions**: dated vs. undated citations; whether IEEE 802.1AS-2020 vs. 802.1AS-2025 applies; whether NTS or later NTP RFCs should be normative or informative; PCIe revision handling.
- Confirm any reused OCP TAP material has **copyright permission / IEEE letter of permission** as needed.

---

## 5. Technical-completeness items to confirm stable

These are written but worth a deliberate WG stability check before locking for ballot, since they are the interoperability core:

- **Baseline PCIe host mapping (8.9)** and **baseline control information model (8.10)** — now concrete; confirm the object/register semantics are stable enough that the WG won't churn them during ballot.
- **Security profiles (8.11)** — baseline/managed/secure-infrastructure tiers are defined; confirm they map cleanly to the conformance profiles in 4.4.
- **Unified-timescale and alignment requirements (5.4, 7.3.2/7.3.4)** — the 100 ns default alignment bound is a real numeric requirement; confirm the WG stands behind it.

---

## 6. IEEE SA ballot machinery (the path to "full standard")

Once the draft passes MEC, the remaining process gates are procedural:

1. **Mandatory coordinations / sponsor approval** — any required inter-committee coordination (e.g., with the IEEE 1588 / 802.1 / 1139 communities) and Standards Committee sign-off to go to ballot.
2. **Call for patents / LOAs** maintained through the WG (ongoing IEEE requirement).
3. **Form the ballot group in myProject** — issue the invitation, recruit a balanced, sufficiently large balloting pool.
4. **SA ballot** — needs ≥75% return and ≥75% approval.
5. **Comment resolution and recirculation** — resolve all disapprove comments; recirculate changes until stable.
6. **RevCom submission** — Standards Review Committee verifies process was followed and recommends to the Standards Board.
7. **SASB approval, then editorial publication prep** — final IEEE editorial production into the published standard.

Budget several months minimum for ballot + recirculation + RevCom even with a clean draft — which reinforces the §1 recommendation to secure a PAR extension.

---

## Suggested next actions (sequenced)

1. **Decide PAR strategy and, if extending, file the NesCom extension now** (§1).
2. **Fill Vice Chair / Secretary roles** (§1).
3. **Hold a WG session to ratify AI-003, AI-004, AI-008, AI-010 and the PICS deferral** by recorded motion (§2).
4. **Begin the Word-template port** in parallel and assign an editor to drive MEC readiness (§3).
5. **Close the normative-reference legal/editorial review** (§4).
6. **Freeze the interoperability core (8.9/8.10/8.11) and regenerate `REQUIREMENTS_INDEX.md`** after the last normative edits (§5).
7. **Form the ballot group in myProject** once MEC is cleared (§6).

---

### Sources

- [P3335 Time Card Working Group — Home](https://sagroups.ieee.org/3335/)
- [IEEE SA NesCom 2022-12-02 recommendations (PAR approval)](https://standards.ieee.org/wp-content/uploads/2022/12/nescom-12022022rec.pdf)
- [IEEE SA Balloting Process FAQs](https://standards.ieee.org/faqs/balloting-process/)
- [IEEE — Submit a Draft for MEC](https://standards-support.ieee.org/hc/en-us/articles/4413200308628-Submit-a-Draft-for-MEC)
- [IEEE — Request an Extension for an Existing PAR](https://standards-support.ieee.org/hc/en-us/articles/4413124818068-Request-an-Extension-for-an-Existing-PAR)
- [IEEE SA Balloting and Comment Resolution Process Guidelines (RevCom)](https://standards.ieee.org/wp-content/uploads/import/governance/revcom/guidelines.pdf)
- [IEEE SA Normative References FAQ](https://standards.ieee.org/faqs/references/)
