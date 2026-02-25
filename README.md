# IEEE P3335 TimeCard Specification

<img width="877" height="458" alt="logo_blue" src="https://github.com/user-attachments/assets/d7a902ab-45db-423e-98c3-9673068b70e5" />

This repository serves as the working document scratchpad for the **IEEE P3335 TimeCard Specification**. It defines the architectural framework, performance expectations, and interoperability objectives for TimeCard devices—modular timing subsystems that provide standardized, high-precision time, phase, and frequency services to host systems.

## Project Structure

The text is organized by chapter, with each section having its own dedicated folder. Inside each folder, a `README.md` file serves as the definitive current state of the text for that clause. 

Other files (such as references, diagrams, or unstructured notes) may exist in these folders, but they are not considered part of the normative or informative text unless explicitly included or referenced within the chapter's respective `README.md` file.

### Chapter Statistics

Based on the standalone PDF compilations of the individual Markdown files, the current page counts for each chapter are as follows (assuming a standard 1-inch uniform margin layout):

| Chapter / Clause | LaTeX Compiled Pages |
| :--- | :--- |
| **01 - Overview** | 4 pages |
| **02 - Normative References** | 2 pages |
| **03 - Definitions, Acronyms and Abbreviations** | 3 pages |
| **04 - Conformance** | 2 pages |
| **05 - Architecture** | 9 pages |
| **06 - Performance Specifications** | 2 pages |
| **07 - Timing Interfaces** | 4 pages |
| **08 - Control Interfaces** | 5 pages |
| **09 - Environment** | 5 pages |
| **10 - Applications and Best Practices** | 4 pages |
| **Annex A - Metrics** | 5 pages |
| **Annex B - Test Procedures** | 3 pages |
| **Annex C - Bibliography** | 2 pages |

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

---

## Editor To-Do List
- Incorporate material from PAR into existing structure
- Iterate to create coherence across overlapping clauses

*(New to Markdown? Check out the [basic syntax guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).)*
