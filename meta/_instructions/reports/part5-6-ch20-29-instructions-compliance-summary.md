# Instruction Compliance Summary: Chapters 20–29

This summary consolidates issues found while checking Chapters 20–29 against the project writing guidelines.

## Per-Chapter Issue Counts

| Chapter | Title | Critical | High | Medium | Low | Total |
|---|---:|---:|---:|---:|---:|---:|
| ch20-benchmarks | Benchmarks | 2 | 0 | 4 | 0 | 6 |
| ch21-eval | Evaluation Principles | 2 | 1 | 16 | 5 | 24 |
| ch22-confounding | Confounders and Leakage | 5 | 1 | 3 | 3 | 12 |
| ch23-uncertainty | **Uncertainty Quantification** | 4 | 1 | 22 | 0 | 27 |
| ch24-interpretability | **Interpretability** | 2 | 1 | 2 | 0 | 5 |
| ch25-clinical-risk | Clinical Risk Prediction | 3 | 22 | 4 | 0 | 29 |
| ch26-rare-disease | Rare Disease Diagnosis | 2 | 10 | 5 | 1 | 18 |
| ch27-drug-discovery | Drug Discovery | 3 | 10 | 1 | 2 | 16 |
| ch28-design | Sequence Design | 3 | 12 | 2 | 3 | 20 |
| ch29-future | Ethical and Frontiers | 2 | 9 | 2 | 1 | 14 |

## Cross-Cutting Issues and Batch Fixes

### Output format is `.qmd` instead of required `.md`

- Affected chapters: ch20-benchmarks, ch21-eval, ch22-confounding, ch23-uncertainty, ch24-interpretability, ch25-clinical-risk, ch26-rare-disease, ch27-drug-discovery, ch28-design, ch29-future
- Fix: convert/emit final prose as `.md` files (no YAML frontmatter), per project output requirements.

### Meta-commentary present

- Affected chapters: ch20-benchmarks, ch21-eval, ch22-confounding, ch23-uncertainty, ch24-interpretability, ch25-clinical-risk, ch26-rare-disease, ch27-drug-discovery, ch28-design, ch29-future
- Common pattern: sentences like “This chapter …” or “In this chapter …”.
- Fix: delete the self-referential sentence(s) and merge any necessary content into direct statements.

### Em-dash (—) violations

- Affected chapters: ch22-confounding, ch28-design
- Fix: global search for `—` and replace with colon/semicolon/parentheses or split sentences.

### Numbered-list scaffolding in prose (“First…, Second…”) 

- Affected chapters: ch22-confounding, ch23-uncertainty, ch25-clinical-risk, ch27-drug-discovery
- Fix: rewrite into prose without ordinal enumeration. If sequential steps must be preserved, use a table or a boxed callout (if allowed) rather than ordinal scaffolding.

### Malformed image placeholder Markdown

- Affected chapters: ch25-clinical-risk, ch26-rare-disease, ch27-drug-discovery, ch28-design, ch29-future
- Symptom: image links like `![...](\`https:\`//placehold.co/...``)` include stray backticks and may not render.
- Fix: remove backticks and restore valid URLs, e.g., `![...](https://placehold.co/300x200?text=...)`.

### Malformed citation syntax

- Affected chapters: ch25-clinical-risk, ch27-drug-discovery, ch28-design
- Symptom: citekeys wrapped/split by backticks (e.g., `[@`rakowski_mifm_2025`]` or `@dalla-`torre_...`). This is likely to break Pandoc/Quarto citation parsing.
- Fix: remove backticks from citekeys and use standard citation forms (`[@rakowski_mifm_2025]`, `Dalla Torre et al. @dalla_torre_nucleotide_2023`, etc.).

### Chapters with no citations detected

- Affected chapters: ch21-eval, ch24-interpretability, ch26-rare-disease, ch29-future
- Risk: guidelines expect citations for technical claims, performance numbers, and historical facts.
- Fix: add citations throughout; prioritize all numbers/metrics and model/dataset claims.

### Sentence-start transitions (“However,”)

- Affected chapters: ch20-benchmarks, ch21-eval, ch25-clinical-risk, ch28-design
- Fix: rephrase to avoid relying on transition openers, or reduce frequency.

### Vague enthusiasm adjectives (“powerful”, “impressive”, “remarkable”)

- Affected chapters: ch21-eval, ch22-confounding, ch26-rare-disease, ch27-drug-discovery, ch28-design, ch29-future
- Fix: replace with neutral, precise descriptors (e.g., “high-capacity”, “high-performing”, “state-of-the-art in X benchmark”), unless quoting a cited source.

### Tutorial-style code blocks

- Affected chapters: ch21-eval
- Fix: confirm necessity; otherwise paraphrase conceptually or move to an appendix/boxed supplement.

### Potential missing citations for numeric/statistical claims

- Affected chapters: ch20-benchmarks, ch21-eval, ch22-confounding, ch23-uncertainty, ch24-interpretability, ch25-clinical-risk, ch26-rare-disease, ch27-drug-discovery, ch29-future
- Fix: audit each flagged number; if it is not purely illustrative, add a citation.

## Notes on Non-Negotiables

- Bullet lists in main prose: no Markdown list bullets were detected in these chapters (automated check).
- Em-dashes: detected only in ch22-confounding, ch28-design.

## Pointers

Each chapter has a dedicated report with exact line-level locations and suggested fixes.
