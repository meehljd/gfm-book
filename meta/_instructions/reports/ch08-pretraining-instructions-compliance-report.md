# Compliance Review: `p2-ch08-pretraining` vs Project Instructions

Date: 2025-12-23

## Inputs
- Instructions: `claude-project-instructions.md`
- Chapter: `p2-ch08-pretraining.qmd` (292 lines)

## Automated Rule Checks

| Check | Result | Evidence |
|---|---:|---|
| Em-dash character (U+2014) count | 0 | PASS |
| Bullet/list lines (`-`, `*`, `+`, `•`, `1.`) | 0 | PASS |
| Meta-commentary triggers | 1 | FAIL (count=1) — See Issues for locations. |
| Figure blocks present | 5 | PASS (fig-pretraining-objectives, fig-masking-strategies, fig-bidirectional-vs-autoregressive, fig-cross-species-contrastive, fig-multitask-pretraining) |
| In-text figure references (`@fig-*`) | 0 | FAIL (No @fig-* references found.) |
| Bracket citations (`[@...]`) | 22 | INFO |
| Bracket citations followed by comma (`[@...],`) | 5 | FAIL (count=5) |
| Suspicious emphasis markers (`****`) | 2 | FAIL (count=2) |

## Issues

### ISSUE-001 (critical) output_format
Rule: All content must be delivered as markdown files (.md); never create .qmd files.
Location: /mnt/data/p2-ch08-pretraining.qmd lines 1-1
Heading path: Pretraining Strategies
Evidence: File name is `p2-ch08-pretraining.qmd` (Quarto .qmd).
Recommendation: Convert/rename to `.md` for the deliverable. Keep Pandoc-compatible constructs (fenced divs for figures, cross-ref ids), but enforce the `.md` extension.

### ISSUE-002 (critical) style_meta_commentary
Rule: ZERO meta-commentary (avoid 'This chapter…', 'In this section…', 'in the following…' framing and chapter-outline narration).
Location: /mnt/data/p2-ch08-pretraining.qmd lines 7-7
Heading path: Pretraining Strategies
Evidence: This chapter examines the major pretraining strategies employed by genomic foundation models, from masked la...ns, what tradeoffs each involves, and how to reason about novel objectives as the field continues to develop.
Recommendation: Rewrite to state stakes and claims directly, without referencing the chapter/section structure. If needed, use an explicit cross-reference (e.g., '@sec-…') rather than 'in the following'.

### ISSUE-003 (minor) cross_references
Rule: Use in-text figure references (@fig-*) where figures are discussed.
Location: /mnt/data/p2-ch08-pretraining.qmd lines 1-292
Heading path: Pretraining Strategies
Evidence: Figure blocks present (fig-pretraining-objectives, fig-masking-strategies, fig-bidirectional-vs-autoregressive, fig-cross-species-contrastive, fig-multitask-pretraining) but no '@fig-*' references appear in prose.
Recommendation: Add in-text references near the relevant discussion (e.g., 'Figure @fig-… summarizes…').

### ISSUE-004 (minor) citations_punctuation
Rule: Avoid mid-sentence bracket citations that break flow (especially patterns like '[@cite],'). Prefer end-of-sentence citations or integrate authors into prose.
Location: /mnt/data/p2-ch08-pretraining.qmd lines 45-231
Heading path: Pretraining Strategies > Masked Language Modeling > Masking Strategies and Their Implications
Evidence: Lines with bracket citation immediately followed by comma: 45, 105, 208, 229, 231
Recommendation: Move citations to sentence ends (e.g., '... mechanism. [@cite]') or rewrite as 'Author et al. @cite showed…'. Remove the comma after the citation bracket.

### ISSUE-005 (major) markdown_formatting
Rule: Avoid malformed or excessive emphasis markers (e.g., '****') that can render unpredictably.
Location: /mnt/data/p2-ch08-pretraining.qmd lines 128-257
Heading path: Pretraining Strategies > Contrastive Learning
Evidence: Lines containing '****': 128, 257
Recommendation: Replace quadruple-asterisk patterns with standard bold/italic markup (usually `**term**`). Verify rendered output for headings and emphasized terms.

### ISSUE-006 (minor) headings_style
Rule: Heading length guideline: ## headings typically 3-5 words.
Location: /mnt/data/p2-ch08-pretraining.qmd lines 60-286
Heading path: Pretraining Strategies > Next-Token Prediction
Evidence: line 60 (2 words): 'Next-Token Prediction'; line 122 (2 words): 'Contrastive Learning'; line 163 (2 words):...line 273 (2 words): 'Open Questions'; line 286 (6 words): 'From Sequence Statistics to Biological Knowledge'
Recommendation: Shorten or expand out-of-range headings while keeping noun-phrase style, if enforcing strict compactness.

### ISSUE-007 (minor) headings_style
Rule: Heading length guideline: ### headings typically 2-4 words.
Location: /mnt/data/p2-ch08-pretraining.qmd lines 30-193
Heading path: Pretraining Strategies > Masked Language Modeling > Masking Strategies and Their Implications
Evidence: line 30 (5 words): 'Masking Strategies and Their Implications'; line 51 (5 words): 'What Masked Language Mod...): 'Augmentation Design for Genomic Sequences'; line 193 (7 words): 'When Multi-Task Helps and When It Hurts'
Recommendation: Shorten or expand out-of-range headings while keeping noun-phrase style, if enforcing strict compactness.

### ISSUE-008 (minor) headings_style
Rule: Prefer noun-phrase headings; avoid gerund (-ing) headings when possible.
Location: /mnt/data/p2-ch08-pretraining.qmd lines 30-260
Heading path: Pretraining Strategies > Masked Language Modeling > Masking Strategies and Their Implications
Evidence: line 30: 'Masking Strategies and Their Implications'; line 80: 'Comparing MLM and Autoregressive Objectives'...ng and Debugging'; line 245: 'Choosing the Right Strategy'; line 260: 'Pretraining in Practice: Case Studies'
Recommendation: Rewrite gerund headings as noun phrases (e.g., 'Pretraining Objectives' instead of 'Pretraining').

### ISSUE-009 (moderate) style_false_enthusiasm
Rule: Avoid 'false enthusiasm' adjectives ('remarkable', 'impressive', 'powerful', etc.) unless quoting/citing field consensus.
Location: /mnt/data/p2-ch08-pretraining.qmd lines 156-156
Heading path: Pretraining Strategies > Contrastive Learning > Cross-Species Contrastive Learning
Evidence: line 156: contains 'powerful'
Recommendation: Replace with neutral academic descriptors ('substantial', 'notable', 'high', 'consistent') or justify with citation/attribution if keeping evaluative language.

### ISSUE-010 (moderate) style_anthropomorphization
Rule: Avoid anthropomorphization (e.g., models 'understand', 'think', 'want'). Prefer operational verbs like 'predict', 'represent', 'encode', 'assign probability'.
Location: /mnt/data/p2-ch08-pretraining.qmd lines 22-22
Heading path: Pretraining Strategies > Masked Language Modeling
Evidence: line 22: 'Consider predicting whether a splice site variant in *DMD*...ream-downstream integration that splice prediction demands.'
Recommendation: Replace 'understand' with 'integrate', 'condition on', 'represent', or 'predict', depending on meaning.

### ISSUE-011 (minor) typography
Rule: Avoid excessive bolding (reduce visual noise; bold glossary terms on first mention only).
Location: /mnt/data/p2-ch08-pretraining.qmd lines 3-266
Heading path: Pretraining Strategies
Evidence: Lines with ≥2 bold spans: 3, 16, 64, 68, 109, 128, 210, 221, 238, 240, 266
Recommendation: Keep bold for the single primary term on first mention; remove additional bold spans or distribute emphasis across sentences.
