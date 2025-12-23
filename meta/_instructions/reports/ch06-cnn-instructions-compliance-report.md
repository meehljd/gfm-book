# Compliance Review: `p2-ch06-cnn` vs Project Instructions

Date: 2025-12-23

## Inputs
- Instructions: `claude-project-instructions.md`
- Chapter: `p2-ch06-cnn.qmd` (252 lines)

## Automated Rule Checks

| Check | Result | Evidence |
|---|---:|---|
| Em-dash character (U+2014) count | 0 | PASS |
| Bullet/list lines (`-`, `*`, `+`, `•`, `1.`) | 0 | PASS |
| Meta-commentary triggers | 2 | FAIL (count=2) — See Issues for locations. |
| Figure blocks present | 5 | PASS (fig-conv-pattern-detector, fig-deepsea-architecture, fig-expecto-pipeline, fig-spliceai-architecture, fig-receptive-field-ceiling) |
| In-text figure references (`@fig-*`) | 0 | FAIL (No @fig-* references found.) |
| Bracket citations (`[@...]`) | 11 | INFO |
| Bracket citations followed by comma (`[@...],`) | 0 | PASS |
| Suspicious emphasis markers (`****`) | 3 | FAIL (count=3) |

## Issues

### ISSUE-001 (critical) output_format
Rule: All content must be delivered as markdown files (.md); never create .qmd files.
Location: /mnt/data/p2-ch06-cnn.qmd lines 1-1
Heading path: Convolutional Networks
Evidence: File name is `p2-ch06-cnn.qmd` (Quarto .qmd).
Recommendation: Convert/rename to `.md` for the deliverable. Keep Pandoc-compatible constructs (fenced divs for figures, cross-ref ids), but enforce the `.md` extension.

### ISSUE-002 (critical) style_meta_commentary
Rule: ZERO meta-commentary (avoid 'This chapter…', 'In this section…', 'in the following…' framing and chapter-outline narration).
Location: /mnt/data/p2-ch06-cnn.qmd lines 5-5
Heading path: Convolutional Networks
Evidence: The models examined in this chapter established paradigms that persist in modern genomic AI. DeepSEA demonst...ional filters, and apply to variant interpretation. The success was remarkable; the paradigm seemed complete.
Recommendation: Rewrite to state stakes and claims directly, without referencing the chapter/section structure. If needed, use an explicit cross-reference (e.g., '@sec-…') rather than 'in the following'.

### ISSUE-003 (critical) style_meta_commentary
Rule: ZERO meta-commentary (avoid 'This chapter…', 'In this section…', 'in the following…' framing and chapter-outline narration).
Location: /mnt/data/p2-ch06-cnn.qmd lines 7-7
Heading path: Convolutional Networks
Evidence: Yet these models revealed a fundamental architectural limitation. Convolutional networks integrate informati...ctural ceiling establishes the foundation for the **attention mechanism**s examined in the following chapter.
Recommendation: Rewrite to state stakes and claims directly, without referencing the chapter/section structure. If needed, use an explicit cross-reference (e.g., '@sec-…') rather than 'in the following'.

### ISSUE-004 (minor) cross_references
Rule: Use in-text figure references (@fig-*) where figures are discussed.
Location: /mnt/data/p2-ch06-cnn.qmd lines 1-252
Heading path: Convolutional Networks
Evidence: Figure blocks present (fig-conv-pattern-detector, fig-deepsea-architecture, fig-expecto-pipeline, fig-spliceai-architecture, fig-receptive-field-ceiling) but no '@fig-*' references appear in prose.
Recommendation: Add in-text references near the relevant discussion (e.g., 'Figure @fig-… summarizes…').

### ISSUE-005 (major) markdown_formatting
Rule: Avoid malformed or excessive emphasis markers (e.g., '****') that can render unpredictably.
Location: /mnt/data/p2-ch06-cnn.qmd lines 31-226
Heading path: Convolutional Networks > Convolutions as Sequence Pattern Detectors
Evidence: Lines containing '****': 31, 118, 226
Recommendation: Replace quadruple-asterisk patterns with standard bold/italic markup (usually `**term**`). Verify rendered output for headings and emphasized terms.

### ISSUE-006 (minor) headings_style
Rule: Avoid leading 'The' in headings (prefer concise noun phrases).
Location: /mnt/data/p2-ch06-cnn.qmd lines 35-238
Heading path: Convolutional Networks > DeepSEA: Regulatory Prediction from Sequence > The Noncoding Variant Problem
Evidence: line 35: 'The Noncoding Variant Problem'; line 114: 'The Modular Architecture'; line 136: 'The Cryptic Splic...e Receptive Field Ceiling'; line 222: 'The Vanishing Gradient Problem'; line 238: 'The Sequential Bottleneck'
Recommendation: Drop leading 'The' where feasible (e.g., 'CADD Framework' not 'The CADD Framework').

### ISSUE-007 (minor) headings_style
Rule: Heading length guideline: ### headings typically 2-4 words.
Location: /mnt/data/p2-ch06-cnn.qmd lines 65-230
Heading path: Convolutional Networks > DeepSEA: Regulatory Prediction from Sequence > Learned Representations and Biological Validation
Evidence: line 65 (5 words): 'Learned Representations and Biological Validation'; line 125 (5 words): 'Expression Prediction and Variant Effects'; line 230 (5 words): 'DanQ: Combining Convolutions and Recurrence'
Recommendation: Shorten or expand out-of-range headings while keeping noun-phrase style, if enforcing strict compactness.

### ISSUE-008 (moderate) style_false_enthusiasm
Rule: Avoid 'false enthusiasm' adjectives ('remarkable', 'impressive', 'powerful', etc.) unless quoting/citing field consensus.
Location: /mnt/data/p2-ch06-cnn.qmd lines 5-208
Heading path: Convolutional Networks
Evidence: line 5: contains 'remarkable'; line 208: contains 'breakthrough'
Recommendation: Replace with neutral academic descriptors ('substantial', 'notable', 'high', 'consistent') or justify with citation/attribution if keeping evaluative language.
