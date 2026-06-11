# IEEE P3335 TimeCard Specification

<img width="877" height="458" alt="logo_blue" src="https://github.com/user-attachments/assets/d7a902ab-45db-423e-98c3-9673068b70e5" />

This repository contains the working draft source for the **IEEE P3335 TimeCard Specification**. It defines the architectural framework, performance expectations, and interoperability objectives for TimeCard devices--modular timing subsystems that provide standardized, high-precision time, phase, and frequency services to host systems.

## Project Structure

The text is organized by clause, with each clause having its own dedicated folder. Inside each folder, a `README.md` file serves as the current draft source for that clause.

Other files (such as references, diagrams, or unstructured notes) may exist in these folders, but they are not considered part of the normative or informative text unless explicitly included or referenced within the chapter's respective `README.md` file.

### Active Draft Sources

| Clause / Annex | Source |
| :--- | :--- |
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

The `Unsorted/` directory is an archival working area for source contributions, extracted presentations, older material, and background notes. It is useful for editorial research but is not automatically included in the compiled draft.

## Building the Standard

The complete specification can be compiled from all of the individual clause `README.md` files into a single, unified PDF document.

### Requirements
You will need to have [Pandoc](https://pandoc.org/) and a LaTeX distribution (such as MacTeX or TeX Live) installed to perform the build. Specifically, the build utilizes the `xelatex` PDF engine to handle Unicode symbols seamlessly.

### Build Instructions
A `Makefile` is provided at the root of the repository to automate compiling the document.

To generate the concatenated standard book, simply run:
```bash
make
```

This command will:
1. Dynamically find all `01` through `10` and `Annex` chapter `README.md` files.
2. Sort them numerically and alphabetically.
3. Pass them logically to `pandoc`.
4. Output a single table-of-contents included document called `IEEE3335.pdf` at the root directory.

To remove the generated PDF and clean up the build output:
```bash
make clean
```

## Publication Readiness

See `PUBLICATION_READINESS.md` for the current editorial gap matrix, remaining working-group decisions, and recommended next actions before IEEE SA publication processing.
