# Compliance Review: `p2-ch07-attention` vs Project Instructions

Date: 2025-12-23

## Inputs
- Instructions: `claude-project-instructions.md`
- Chapter: `p2-ch07-attention.qmd` (301 lines)

## Automated Rule Checks

| Check | Result | Evidence |
|---|---:|---|
| Em-dash character (U+2014) count | 0 | PASS |
| Bullet/list lines (`-`, `*`, `+`, `•`, `1.`) | 0 | PASS |
| Meta-commentary triggers | 1 | FAIL (count=1) — See Issues for locations. |
| Figure blocks present | 6 | PASS (fig-self-attention, fig-multihead-attention, fig-attention-patterns, fig-transformer-block, fig-encoder-decoder…) |
| In-text figure references (`@fig-*`) | 0 | FAIL (No @fig-* references found.) |
| Bracket citations (`[@...]`) | 27 | INFO |
| Bracket citations followed by comma (`[@...],`) | 3 | FAIL (count=3) |
| Suspicious emphasis markers (`****`) | 4 | FAIL (count=4) |

## Issues

### ISSUE-001 (critical) output_format
Rule: All content must be delivered as markdown files (.md); never create .qmd files.
Location: /mnt/data/p2-ch07-attention.qmd lines 1-1
Heading path: Transformers and Attention
Evidence: File name is `p2-ch07-attention.qmd` (Quarto .qmd).
Recommendation: Convert/rename to `.md` for the deliverable. Keep Pandoc-compatible constructs (fenced divs for figures, cross-ref ids), but enforce the `.md` extension.

### ISSUE-002 (critical) style_meta_commentary
Rule: ZERO meta-commentary (avoid 'This chapter…', 'In this section…', 'in the following…' framing and chapter-outline narration).
Location: /mnt/data/p2-ch07-attention.qmd lines 7-7
Heading path: Transformers and Attention
Evidence: This chapter examines the attention mechanism and **transformer architecture** from the perspective of genom...isms still struggle establishes the foundation for the models examined throughout the remainder of this book.
Recommendation: Rewrite to state stakes and claims directly, without referencing the chapter/section structure. If needed, use an explicit cross-reference (e.g., '@sec-…') rather than 'in the following'.

### ISSUE-003 (minor) cross_references
Rule: Use in-text figure references (@fig-*) where figures are discussed.
Location: /mnt/data/p2-ch07-attention.qmd lines 1-301
Heading path: Transformers and Attention
Evidence: Figure blocks present (fig-self-attention, fig-multihead-attention, fig-attention-patterns, fig-transformer-block, fig-encoder-decoder, fig-quadratic-ceiling) but no '@fig-*' references appear in prose.
Recommendation: Add in-text references near the relevant discussion (e.g., 'Figure @fig-… summarizes…').

### ISSUE-004 (minor) figures_count
Rule: Chapters should suggest ~3-5 figures with specific purposes.
Location: /mnt/data/p2-ch07-attention.qmd lines 1-301
Heading path: Transformers and Attention
Evidence: Detected 6 figure blocks: fig-self-attention, fig-multihead-attention, fig-attention-patterns, fig-transformer-block, fig-encoder-decoder, fig-quadratic-ceiling
Recommendation: If strictly enforcing the 3-5 figure guideline, merge redundant figures or move extras to an appendix.

### ISSUE-005 (minor) citations_punctuation
Rule: Avoid mid-sentence bracket citations that break flow (especially patterns like '[@cite],'). Prefer end-of-sentence citations or integrate authors into prose.
Location: /mnt/data/p2-ch07-attention.qmd lines 5-281
Heading path: Transformers and Attention
Evidence: Lines with bracket citation immediately followed by comma: 5, 281
Recommendation: Move citations to sentence ends (e.g., '... mechanism. [@cite]') or rewrite as 'Author et al. @cite showed…'. Remove the comma after the citation bracket.

### ISSUE-006 (major) markdown_formatting
Rule: Avoid malformed or excessive emphasis markers (e.g., '****') that can render unpredictably.
Location: /mnt/data/p2-ch07-attention.qmd lines 7-199
Heading path: Transformers and Attention
Evidence: Lines containing '****': 7, 95, 133, 199
Recommendation: Replace quadruple-asterisk patterns with standard bold/italic markup (usually `**term**`). Verify rendered output for headings and emphasized terms.

### ISSUE-007 (minor) headings_style
Rule: Avoid leading 'The' in headings (prefer concise noun phrases).
Location: /mnt/data/p2-ch07-attention.qmd lines 10-271
Heading path: Transformers and Attention > The Self-Attention Mechanism
Evidence: line 10: 'The **Self-Attention** Mechanism'; line 116: 'The Transformer Block'; line 150: 'The Quadratic Barrier'; line 271: 'The Quadratic Ceiling'
Recommendation: Drop leading 'The' where feasible (e.g., 'CADD Framework' not 'The CADD Framework').

### ISSUE-008 (minor) headings_style
Rule: Heading length guideline: ## headings typically 3-5 words.
Location: /mnt/data/p2-ch07-attention.qmd lines 75-228
Heading path: Transformers and Attention > Positional Encoding
Evidence: line 75 (2 words): '**Positional Encoding**'; line 228 (2 words): 'Training Dynamics'
Recommendation: Shorten or expand out-of-range headings while keeping noun-phrase style, if enforcing strict compactness.

### ISSUE-009 (minor) headings_style
Rule: Heading length guideline: ### headings typically 2-4 words.
Location: /mnt/data/p2-ch07-attention.qmd lines 22-240
Heading path: Transformers and Attention > The Self-Attention Mechanism > Query, Key, and Value Vectors
Evidence: line 22 (5 words): 'Query, Key, and Value Vectors'; line 232 (1 words): 'Optimization'; line 240 (1 words): 'Regularization'
Recommendation: Shorten or expand out-of-range headings while keeping noun-phrase style, if enforcing strict compactness.

### ISSUE-010 (minor) headings_style
Rule: Prefer noun-phrase headings; avoid gerund (-ing) headings when possible.
Location: /mnt/data/p2-ch07-attention.qmd lines 146-283
Heading path: Transformers and Attention > Scaling to Genomic Sequences
Evidence: line 146: 'Scaling to Genomic Sequences'; line 228: 'Training Dynamics'; line 283: 'Choosing Architectures'
Recommendation: Rewrite gerund headings as noun phrases (e.g., 'Pretraining Objectives' instead of 'Pretraining').

### ISSUE-011 (minor) typography
Rule: Avoid excessive bolding (reduce visual noise; bold glossary terms on first mention only).
Location: /mnt/data/p2-ch07-attention.qmd lines 7-256
Heading path: Transformers and Attention
Evidence: Lines with ≥2 bold spans: 7, 24, 79, 95, 129, 133, 162, 178, 199, 205, 244, 250, … (+1 more)
Recommendation: Keep bold for the single primary term on first mention; remove additional bold spans or distribute emphasis across sentences.
