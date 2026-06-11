# Unsorted Source Material

This directory contains historical source contributions, extracted slides/documents, older draft material, and generated media used during development of IEEE P3335. The contents are not part of the active draft unless a clause explicitly references them.

## Proposed Triage Classes

| Class | Intended contents | Proposed destination |
|-------|-------------------|----------------------|
| Contributions | Original working-group proposals, source documents, and dated technical contributions. | `contributions/` |
| Source extractions | Markdown and extracted media generated from PDF, DOCX, and PPTX sources. | `source-extractions/` |
| Older clause material | Superseded clause drafts retained for provenance. | `archive/older-clauses/` |
| Generated media | Images extracted from slides and documents. | Stored next to the source extraction that generated them. |

## Migration Rules

- Preserve original filenames unless a file move would create an ambiguous duplicate.
- Keep generated images adjacent to the Markdown extraction that references them.
- Do not delete source PDFs, DOCX, or PPTX files unless the working group confirms they are redundant and recoverable elsewhere.
- Record moves in a manifest before performing large-scale reorganization.
- Do not include `Unsorted/` files in the compiled standard unless they are intentionally promoted into an active clause or annex.

## Next Migration Step

Create a move manifest that maps each file in this directory to one of the proposed destinations. Apply the move in a separate cleanup patch after the working group confirms the classification.
