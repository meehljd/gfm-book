# Part II Compliance Summary: Chapters 5–9 vs Project Instructions

Date: 2025-12-23

This summary aggregates the per-chapter compliance reports for Part II (Ch. 5–9). It is intended as a quick cross-chapter view of recurring problems and where to focus revision effort.

## Per-chapter issue counts

| Chapter | Lines | Critical | Major | Moderate | Minor | Primary issue themes |
|---|---:|---:|---:|---:|---:|---|
| `p2-ch05-representations` | 221 | 2 | 1 | 0 | 5 | headings_style, output_format, style_meta_commentary, cross_references, markdown_formatting |
| `p2-ch06-cnn` | 252 | 3 | 1 | 1 | 3 | style_meta_commentary, headings_style, output_format, cross_references, markdown_formatting |
| `p2-ch07-attention` | 301 | 2 | 1 | 0 | 8 | headings_style, output_format, style_meta_commentary, cross_references, figures_count |
| `p2-ch08-pretraining` | 292 | 2 | 1 | 2 | 6 | headings_style, output_format, style_meta_commentary, cross_references, citations_punctuation |
| `p2-ch09-transfer` | 292 | 2 | 1 | 1 | 6 | headings_style, style_meta_commentary, output_format, cross_references, markdown_formatting |

## Cross-chapter patterns to address first

1. **Output format mismatch (.qmd vs .md)** appears in every chapter (critical). Convert the deliverables to `.md` per the project rules.
2. **Meta-commentary in chapter openings** appears in every chapter (critical). Replace “This chapter…” / “In the following…” framing with stakes-first openings.
3. **Figure blocks exist but are not referenced in prose** across all chapters (minor). Add `@fig-*` references where figures are discussed.
4. **Suspicious emphasis markup (`****`)** occurs in every chapter (major). Fix the markdown so emphasis renders predictably (usually `**term**`).
5. **Heading-style drift** (leading “The”, gerund headings, word-count outliers) is common (minor). Standardize headings to concise noun phrases.

## Files

- `ch05-representations-instructions-compliance-report.md`
- `ch06-cnn-instructions-compliance-report.md`
- `ch07-attention-instructions-compliance-report.md`
- `ch08-pretraining-instructions-compliance-report.md`
- `ch09-transfer-instructions-compliance-report.md`