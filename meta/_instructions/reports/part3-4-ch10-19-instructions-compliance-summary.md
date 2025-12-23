# Instructions Compliance Summary: Chapters 10-19

**Reviewed against:** `claude-project-instructions.md`

**Totals across chapters:** 24 blockers, 61 major issues, 20 minor issues.

## Cross-Cutting Findings

- All 10 chapters are currently stored as `.qmd` files, but the instructions require deliverables as `.md`.
- 9 of 10 chapters contain at least one explicit meta-telegraphing sentence (for example, "This chapter ...").
- Chapters 10-14 repeatedly use backticks inside citation keys (for example `[@`key`]`), which is nonstandard Pandoc/Quarto citation syntax.
- Em-dashes (—) appear in Chapters 13, 15, and 19 and must be removed entirely.

## Chapter-Level Status

| Chapter                     | Source                    |   Blockers |   Majors |   Minors | Key blockers                                     |
|:----------------------------|:--------------------------|-----------:|---------:|---------:|:-------------------------------------------------|
| Foundation Model Paradigm   | p3-ch10-fm-principles.qmd |          2 |       14 |        0 | Not .md output; Meta-commentary                  |
| DNA Language Models         | p3-ch11-dna-lm.qmd        |          2 |       12 |        3 | Not .md output; Meta-commentary                  |
| Protein *Language* Models   | p3-ch12-protein-lm.qmd    |          2 |       15 |        3 | Not .md output; Meta-commentary                  |
| Regulatory Models           | p3-ch13-regulatory.qmd    |          4 |        7 |        1 | Not .md output; Em-dash present; Meta-commentary |
| Variant Effect Prediction   | p3-ch14-vep-fm.qmd        |          2 |       13 |        3 | Not .md output; Meta-commentary                  |
| RNA Structure and Function  | p4-ch15-rna.qmd           |          4 |        0 |        2 | Not .md output; Em-dash present; Meta-commentary |
| Single-Cell Models          | p4-ch16-single-cell.qmd   |          2 |        0 |        4 | Not .md output; Meta-commentary                  |
| 3D Genome Organization      | p4-ch17-3d-genome.qmd     |          2 |        0 |        1 | Not .md output; Meta-commentary                  |
| Graph and Network Models    | p4-ch18-networks.qmd      |          2 |        0 |        3 | Not .md output; Meta-commentary                  |
| **Multi-Omics** Integration | p4-ch19-multi-omics.qmd   |          2 |        0 |        0 | Not .md output; Em-dash present                  |

## Recommended Global Fix Order

1. Convert each chapter deliverable to `.md` (retain Quarto-compatible markdown only if desired, but the file extension must be `.md`).
2. Remove meta-commentary sentences ("This chapter...", "In this section...", "we will...") and rewrite as direct content.
3. In Chapters 10-14, fix citation syntax by removing backticks from citation keys.
4. Remove all em-dashes (—) and replace with commas, parentheses, colons/semicolons, or sentence splits.
5. Address minor tone issues (false enthusiasm) and any anthropomorphic phrasing.
