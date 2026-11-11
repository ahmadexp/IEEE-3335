# Opher Terminology Feedback Disposition, September 3, 2026

Source reviewed: Written feedback from Opher following the P3335 terminology discussion, transcribed by the Chair.

The terminology comments are addressed in the active manuscript sources. The P1952 comparison remains an explicit pre-ballot coordination action because the current P1952 working draft is not a public normative source.

## Action summary

| Area | Resolution |
|------|------------|
| Unqualified accuracy | Removed the generic Clause 3 definition and narrowed manuscript usage to qualified terms. |
| Qualified accuracy terms | Defined time accuracy, frequency accuracy, and TimeCard timestamp accuracy in their specific measurement contexts. |
| Accuracy versus resolution | Kept resolution and granularity distinct from TimeCard timestamp accuracy; the latter requires bounded error to a declared reference at the event instant. |
| TimeCard source | Defined TimeCard synchronization source and replaced ambiguous bare `source` uses where the synchronization concept was intended. |
| P1952 coordination | Added AI-028 for an authorized terminology comparison and Working Group disposition before ballot. |

## Detailed disposition

| ID | Comment topic | Disposition |
|----|---------------|-------------|
| OT-01 | Avoid defining generic accuracy and qualify the term where useful. | Accepted. Clause 3 no longer defines unqualified accuracy. It defines time accuracy, frequency accuracy, and TimeCard timestamp accuracy. Informative uses were qualified where they refer to one of those concepts. |
| OT-02 | Consider a qualified TimeCard timestamp-accuracy term. | Accepted with technical refinement. The definition and requirements use bounded timestamp error and uncertainty at a declared event measurement point. The illustrative wording equating accuracy with resolution was not adopted because resolution and accuracy characterize different properties. Clauses 6.4.1, 6.7, and 7.3.5 now state the declaration requirements, and Annexes A, B, and D carry them into guidance, testing, and the conformance proforma. |
| OT-03 | Define the extensively used TimeCard source concept. | Accepted as `TimeCard synchronization source`. The term covers an external reference signal, an internal primary reference, or a selected or synthesized ensemble used to initialize, discipline, or validate the unified timescale. Bare `source` uses in this sense were qualified, while unrelated established terms such as source impedance and power source were retained. |
| OT-04 | Consider P1952 terminology and encourage cross-group participation. | Accepted as a coordination action. AI-028 requires review against an authorized current P1952 glossary or draft and records intentional common terms and differences before ballot. No unpublished P1952 text is imported or made a normative dependency by this editorial pass. |

## Remaining action

AI-028 in `PUBLICATION_READINESS.md` tracks Opher's confirmation, the P1952 terminology comparison, and Working Group ratification.

Public project context: IEEE P1952, *Standard for Resilient Positioning, Navigation and Timing (PNT) User Equipment*, <https://standards.ieee.org/ieee/1952/10606/>.
