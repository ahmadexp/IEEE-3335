# Publication Review, 17 September 2026

This review covers the active proposal, its conformance and evidence artifacts, and the PDF build. Changes are draft candidate text for working-group review. Completion of an editorial action does not constitute working-group ratification or IEEE approval.

## Corrections and improvements

| Area | Change and reason |
|------|-------------------|
| Normative reference [1] | Corrected an IPMI citation that named DMTF DSP0236, an MCTP document. Clause 8 now identifies the actual IPMI baseline. Source eligibility remains open under AI-030. |
| Scope and organization | Extended the optional timing-flow applicability reference through Clause 9 and added Annex E to the document map and front-matter description. |
| Terminology | Defined fault, stale, and unknown control states; corrected the gRPC expansion; replaced the unexplained WiWi example with wireless time transfer. |
| Base conformance | Included timestamp information consistently with the providing-interface definition. Expanded implementation, revision, control-mapping, and security declarations. |
| Draft status and deviations | Removed wording that could imply a conformance claim against an unapproved draft. Clarified that a test-method waiver cannot waive an applicable mandatory requirement. |
| Documentation | Aligned supplier terminology and distinguished mandatory conformance-statement availability from recommended availability of supporting integration documentation. |
| Timestamp performance | Linked event-capture performance declarations explicitly to the bounded timestamp-error requirements in 6.4.1. |
| Conditional objects | Expressed the existing conditional-object obligation using the requirement term in 4.1. All 16 objects in 8.10.3 now appear individually in the requirements index. |
| Test guidance | Added control-status, extension/version compatibility, event/telemetry, update, boot, protected-storage, transport/replay, and sanitization checks. Corrected the required-object test to reject both unsupported and unspecified object status. These are procedures, not hardware test results. |
| Conformance proforma | Added control and security declaration records, noise-transfer and noise-tolerance records, shared performance context, and clearer treatment of failed requirements. |
| PDF layout | Widened proforma label columns, balanced the cross-platform comparison, and reserved space to keep table headings and introductions with opening table rows. |
| Build reliability | The build runs checks first, propagates Pandoc failures, creates output in a temporary directory, and replaces the existing PDF only after success. |
| Regression protection | Added checks for unexpected active sources, document-map omissions, undefined status terms, reference identity/numbering, and nine regression tests covering editorial failures and conditional-object index coverage. |

## Verification

- `make requirements` generated 554 requirement statements from 353 source occurrences of the mandatory requirement term.
- `make check` passed for all 16 manuscript sources and 14 normative references, including nine regression tests and Python syntax checks.
- `make` completed successfully with Pandoc and XeLaTeX.
- A deliberately invalid PDF-engine configuration produced a failing build, preserved the previous PDF byte-for-byte, and left no temporary build directory.
- PDF pages were rendered for visual review. Dense control, security, conformance, and host-mapping tables received additional inspection.
- Automated PDF inspection checked page boundaries, the dated footer and page number on every page, and the absence of the prohibited em dash character.
- `git diff --check` passed.

## Source checks

The [DMTF DSP0236 catalog entry](https://www.dmtf.org/dsp/DSP0236) establishes that the identifier belongs to MCTP. [Intel's IPMI publication page](https://www.intel.com/content/www/us/en/products/docs/servers/ipmi/ipmi-home.html) supplies the actual IPMI source. The reference audit records the exact baseline and its embedded terms.

The [gRPC FAQ](https://grpc.io/docs/what-is-grpc/faq/) supports the corrected acronym entry. [IEEE SA Operations Manual Clause 6](https://standards.ieee.org/about/policies/opman/sect6/) supplies the draft-status, requirement-term, and normative-reference review basis.

## Remaining actions

The controlling register is `PUBLICATION_READINESS.md`. The highest-priority unresolved work remains the 1PPS profile, PCIe discovery encoding, control identifier/version governance, reference eligibility and editions, and official IEEE front matter. Independent metrology and security review and representative Windows, macOS, and Linux validation remain necessary.

AI-030 specifically requests IEEE SA disposition of the IPMI source's embedded NDA/adopter-agreement language. Correcting its identity does not close that eligibility review.

AI-031 records a typesetting limitation: current review line numbering covers paragraph lines from the Abstract onward, but table cells, displayed equations, and figure content do not have equivalent per-line coverage. The README now describes the actual behavior.
