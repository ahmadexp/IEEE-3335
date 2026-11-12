# IEEE P3335 TimeCard Proposal

<img width="877" height="458" alt="logo_blue" src="https://github.com/user-attachments/assets/3409c764-63f7-4b3d-ae48-f75e585ee1dd" />

This repository contains the proposal source for **IEEE P3335, Architecture and Interfaces for Time Card**. It defines the architectural framework, performance declarations, and interoperability requirements for TimeCard devices, which are modular timing subsystems that provide standardized time, phase, frequency, and timestamp services to host and downstream systems.

## Project Structure

The text is organized by clause, with each clause having its own dedicated folder. Inside each folder, a `README.md` file serves as the current draft source for that clause.

Other files (such as references, diagrams, or unstructured notes) may exist in these folders, but they are not considered part of the normative or informative text unless explicitly included or referenced within the chapter's respective `README.md` file.

### Active Draft Sources

| Clause / Annex | Source |
| :--- | :--- |
| **Front matter** | `00 - Front Matter/README.md` |
| **1. Overview** | `01 - Overview/README.md` |
| **2. Normative References** | `02 - Normative References/README.md` |
| **3. Definitions, Acronyms, and Abbreviations** | `03 - Definitions, Acronyms and Abbreviations/README.md` |
| **4. Conformance** | `04 - Conformance/README.md` |
| **5. Architecture** | `05 - Architecture/README.md` |
| **6. Performance Specifications** | `06 - Performance Specifications/README.md` |
| **7. Timing Interfaces** | `07 - Timing Interfaces/README.md` |
| **8. Control Interfaces** | `08 - Control Interfaces/README.md` |
| **9. Environment** | `09 - Environment/README.md` |
| **10. Applications and Best Practices** | `10 - Applications and Best Practices/README.md` |
| **Annex A. Metrics** | `Annex A - Metrics/README.md` |
| **Annex B. Test Procedures** | `Annex B - Test Procedures/README.md` |
| **Annex C. Bibliography** | `Annex C - Bibliography/README.md` |
| **Annex D. Conformance Statement Proforma** | `Annex D - Conformance Statement Proforma/README.md` |
| **Annex E. Host Operating-System Integration** | `Annex E - Host Operating-System Integration/README.md` |

The `Unsorted/` directory is an archival working area for source contributions, extracted presentations, older material, and background notes. It is useful for editorial research but is not automatically included in the compiled draft.

## Building the Standard

The complete specification can be compiled from all of the individual clause `README.md` files into a single, unified PDF document.

### Requirements
You will need to have [Pandoc](https://pandoc.org/) and a LaTeX distribution (such as MacTeX or TeX Live) installed to perform the build. Specifically, the build utilizes the `xelatex` PDF engine to handle Unicode symbols seamlessly.

### Build Instructions
A `Makefile` is provided at the root of the repository to automate compiling the document.

The PDF build runs the editorial checks and regression tests first. After normative edits, run `make requirements` to refresh the generated index. A failed build returns an error and preserves the existing PDF; the output is replaced only after successful compilation.

To run editorial and traceability checks:
```bash
make check
```

To generate the complete proposal:
```bash
make
```

To select a particular Pandoc executable, use `make PANDOC=/path/to/pandoc`. The executable and LaTeX distribution must support the host architecture. Regenerating changed SVG figures also requires ImageMagick; `FIGURE_CONVERTER` can select its executable. Up-to-date rendered figure PDFs are kept in `figures/rendered/`.

This command will:
1. Dynamically find the front matter, all `01` through `10` clauses, and all annex `README.md` files.
2. Sort them numerically and alphabetically.
3. Pass them logically to `pandoc`.
4. Add pagewise review line numbers to paragraph lines from the Abstract onward. Full table and equation coverage is tracked in action AI-031.
5. Add the current build date to the footer of every page.
6. Output a single document with a table of contents called `IEEE3335.pdf` at the root directory.

To remove the generated PDF and clean up the build output:
```bash
make clean
```

## Publication Readiness

Read the [unofficial review PDF](IEEE3335.pdf), the [pre-ballot decision agenda](references/PRE_BALLOT_DECISIONS.md), and the [publication action register](PUBLICATION_READINESS.md). The agenda separates choices for the working group from evidence and external approvals still needed.

Supporting readiness artifacts:

- `references/P3335_PAR_SCOPE_PURPOSE.md` records the public PAR scope and purpose trace used for Clause 1.
- `references/NORMATIVE_REFERENCE_AUDIT.md` records the current Clause 2 reference audit.
- `references/PUBLICATION_REVIEW_20260917.md` records the September 17 review, corrections, validation, and remaining decisions.
- `references/KEVIN_GODFREY_FEEDBACK_20261030_DISPOSITION.md` records the changes following Kevin Godfrey's review and accounts for each comment.
- `references/KEVIN_GODFREY_WG_DECISIONS_20261103.md` separates the remaining WG decisions and reference dependencies from the applied draft changes.
- [Rodney Cummings's v8 dispositions](references/RODNEY_CUMMINGS_V8_DISPOSITION_20261110.md) account for all 19 comments and link to the response workbook.
- `figures/` contains source-controlled figure sources and rendered assets used by the draft.
- `REQUIREMENTS_INDEX.md` is generated from normative clauses with `python3 scripts/requirements_index.py`.
