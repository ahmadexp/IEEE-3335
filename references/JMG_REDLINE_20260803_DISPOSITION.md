# JMG Redline Comment Disposition, August 3, 2026 Draft

Source reviewed: `IEEE3335 (20260803) JMG Redline.pdf`

The redline contains 45 substantive comments and one companion stamp. All substantive comments are resolved in the active manuscript sources. The stamp circles the line number addressed by comment 1 and requires no separate text change.

## Action summary

| Area | Resolution |
|------|------------|
| Review usability | Pagewise line numbers are zero-padded for reliable page-line sorting. |
| Terminology | Added or clarified control plane, command queue, serial interface, `unspecified`, connector names, and units. |
| Normative language | Audited `can` and changed permission statements to `may`; retained `can` only for capability, possibility, or fact. |
| Control model | Clarified extension parsing, atomic observations, failure state, numeric overflow, state names, and non-GNSS satellite sources. |
| Environment | Added coolant cleanliness and maintenance, connector mating-cycle wording, and a dynamic out-of-performance indication. |
| Guidance and tests | Recast failure guidance, metric documentation, error correlation, and finite reference-qualification testing. |
| Publication | Converted all figures to black-and-white line art and added distributed-systems references with URLs. |

## Detailed disposition

| ID | PDF page | Comment topic | Disposition |
|----|----------|---------------|-------------|
| 1 | 5 | Zero-pad pagewise line numbers | Accepted. Line numbers 1 through 9 now render as 01 through 09. |
| 2 | 5 | Stamp around the first line number | Closed with comment 1. The stamp is a visual pointer, not an independent comment. |
| 3 | 8 | Define control plane | Accepted. Added a Clause 3 definition. |
| 4 | 8 | Data plane may contain multiple paths | Accepted. The definition now says path or set of paths. |
| 5 | 9 | Standards meaning and ordering of `unspecified` | Accepted. The definition records an intentional decision not to constrain a value or behavior, preserves the permitted object-field meaning, and follows `unified timescale`. |
| 6 | 10 | Define `mdeg C` | Accepted. Added millidegrees Celsius to 3.2. |
| 7 | 10 | Spell out MIPI | Accepted with current brand usage. The entry gives the original Mobile Industry Processor Interface expansion and notes that MIPI Alliance no longer expands MIPI as an acronym. |
| 8 | 10 | Define `ns` | Accepted. Added nanosecond to 3.2. |
| 9 | 10 | Define `ps` | Accepted. Added picosecond to 3.2. |
| 10 | 10 | Define serial | Accepted. Added a serial-interface definition to 3.1. |
| 11 | 10 | Identify SMA as coaxial | Accepted. |
| 12 | 11 | Identify TNC as coaxial | Accepted. |
| 13 | 11 | Add Type-N coaxial connector | Accepted. Added to 3.2; the physical timing profile already permits Type-N. |
| 14 | 11 | Add microsecond symbol | Accepted. Added `µs` to 3.2. |
| 15 | 11 | Discuss `unspecified` in requirement terms | Accepted. Clause 4.1 explains that it is not a requirement term and identifies an intentionally unconstrained choice. |
| 16 | 11 | Replace ambiguous `This` | Accepted. The sentence now identifies Clause 4. |
| 17 | 12 | Replace ambiguous `one` | Accepted. The requirement now refers to the single unified timescale. |
| 18 | 14 | Use monochrome line art for every figure | Accepted. All three SVG sources use white fills, black outlines, and black text and connectors. |
| 19 | 21 | Correct the `times-tamp` line break | Accepted while retaining IEEE's one-word `timestamp` terminology. A LaTeX hyphenation rule permits only the meaningful `time-stamp` break. |
| 20 | 23 | Require the specific protocol edition | Accepted. The declaration now calls for the specific edition or revision. |
| 21 | 26 | Define command queues and serial | Accepted. Both terms are defined in Clause 3. |
| 22 | 27 | Audit `can` versus permissive `may` | Accepted. Permission statements were changed to `may`; capability, possibility, and factual uses of `can` were retained. |
| 23 | 28 | Recast unknown-extension behavior | Accepted. The requirement is split into short statements covering recognized fields, uninterpreted optional fields, forwarding, and incompatibility reporting. |
| 24 | 28 | Replace `one logical observation` | Accepted. The requirement now says a single logical observation. |
| 25 | 28 | Add indeterminate state | Accepted. A failed write may not silently leave an indeterminate state or configuration. |
| 26 | 31 | Explain `mdeg C` | Closed with comment 6; the table also spells out millidegrees Celsius. |
| 27 | 31 | Define counter overflow behavior | Accepted. Mappings must define out-of-range and counter rollover or saturation behavior, reset conditions, and observable wrap or loss indication. `EVENT_COUNT` follows the mapping-declared policy and reports loss or overwrite. |
| 28 | 31 | Change probing permission to `may` | Accepted. |
| 29 | 31 | Identify `TC_STATE` values as states | Accepted. The list is introduced as the following states. |
| 30 | 32 | Address Starlink and similar constellations | Accepted. Clause 8 distinguishes non-GNSS satellite services from GNSS and requires service identity, vehicle selection, handover behavior, source identity, and health reporting when used for timing. |
| 31 | 34 | State coolant cleanliness assumptions | Accepted. Clause 9 now covers coolant type, contamination limits, filtration, maintenance, fouling, and derating or protection. |
| 32 | 34 | State number of mating cycles | Accepted. The requirement now uses the expected number of mating cycles. |
| 33 | 35 | Specify how degraded performance is indicated | Accepted. A control object or alarm provides a dynamic indication when the condition is detectable; otherwise the documentation identifies the required external monitoring. |
| 34 | 35 | Replace `valid` with applicable wording | Accepted. The sentence refers to applicable bounds that are not assured. |
| 35 | 36 | Regulatory approval cannot be granted | Accepted. The note says P3335 does not and cannot grant regulatory approval. |
| 36 | 38 | Replace `can` with `might be exceeded` | Accepted. |
| 37 | 38 | Rename common integration failures | Accepted. The heading is Common failure syndromes. |
| 38 | 38 | Trace correction sign and value | Accepted. |
| 39 | 38 | Replace shared infrastructure | Accepted. The cause is now lack of needed redundancy. |
| 40 | 38 | Remove software-only qualifier | Accepted. The cause is now conversion error, covering firmware, software, and other implementations. |
| 41 | 39 | Document metric conditions | Accepted. The annex says the listed conditions should accompany the result. |
| 42 | 40 | Replace ambiguous table header | Accepted. The header is Use in IEEE P3335. |
| 43 | 40 | Clarify nonconformance representation | Accepted. The departure is not to be represented or interpreted as IEEE 1588 conformance. |
| 44 | 41 | Specify error correlation | Accepted. Both the discussion and reporting guidance now say error correlation. |
| 45 | 42 | Avoid claiming universal valid-signal proof | Accepted. The test is now reference qualification and status using a finite declared set of acceptable conditions and counterexamples; the annex states that P3335 does not prescribe a universal validity proof. |
| 46 | 46 | Add Lamport and related references with URLs | Accepted. Added Lamport's event-ordering paper, the Byzantine Generals paper, Gray and Reuter, and van Steen and Tanenbaum with author, publisher, or book URLs. |
