# Compliance Review: `p2-ch09-transfer` vs Project Instructions

Date: 2025-12-23

## Inputs
- Instructions: `claude-project-instructions.md`
- Chapter: `p2-ch09-transfer.qmd` (292 lines)

## Automated Rule Checks

| Check | Result | Evidence |
|---|---:|---|
| Em-dash character (U+2014) count | 0 | PASS |
| Bullet/list lines (`-`, `*`, `+`, `•`, `1.`) | 0 | PASS |
| Meta-commentary triggers | 2 | FAIL (count=2) — See Issues for locations. |
| Figure blocks present | 5 | PASS (fig-domain-alignment, fig-lora-architecture, fig-adaptation-decision-tree, fig-domain-shift-detection, fig-validation-pitfalls) |
| In-text figure references (`@fig-*`) | 0 | FAIL (No @fig-* references found.) |
| Bracket citations (`[@...]`) | 38 | INFO |
| Bracket citations followed by comma (`[@...],`) | 0 | PASS |
| Suspicious emphasis markers (`****`) | 1 | FAIL (count=1) |

## Issues

### ISSUE-001 (critical) output_format
Rule: All content must be delivered as markdown files (.md); never create .qmd files.
Location: /mnt/data/p2-ch09-transfer.qmd lines 1-1
Heading path: Transfer and Adaptation
Evidence: File name is `p2-ch09-transfer.qmd` (Quarto .qmd).
Recommendation: Convert/rename to `.md` for the deliverable. Keep Pandoc-compatible constructs (fenced divs for figures, cross-ref ids), but enforce the `.md` extension.

### ISSUE-002 (critical) style_meta_commentary
Rule: ZERO meta-commentary (avoid 'This chapter…', 'In this section…', 'in the following…' framing and chapter-outline narration).
Location: /mnt/data/p2-ch09-transfer.qmd lines 7-7
Heading path: Transfer and Adaptation
Evidence: The reality requires careful navigation. Every adaptation decision involves tradeoffs: preserving pretrained...hat separates practitioners who apply foundation models effectively from those who treat them as black boxes.
Recommendation: Rewrite to state stakes and claims directly, without referencing the chapter/section structure. If needed, use an explicit cross-reference (e.g., '@sec-…') rather than 'in the following'.

### ISSUE-003 (minor) style_meta_commentary
Rule: ZERO meta-commentary (avoid 'This chapter…', 'In this section…', 'in the following…' framing and chapter-outline narration).
Location: /mnt/data/p2-ch09-transfer.qmd lines 207-207
Heading path: Transfer and Adaptation > Case Studies in Transfer Learning
Evidence: The contrast between successful and failed transfer illuminates the principles developed throughout this chapter. Four cases span different outcomes and reveal the conditions that distinguish success from failure.
Recommendation: Rewrite to state stakes and claims directly, without referencing the chapter/section structure. If needed, use an explicit cross-reference (e.g., '@sec-…') rather than 'in the following'.

### ISSUE-004 (minor) cross_references
Rule: Use in-text figure references (@fig-*) where figures are discussed.
Location: /mnt/data/p2-ch09-transfer.qmd lines 1-292
Heading path: Transfer and Adaptation
Evidence: Figure blocks present (fig-domain-alignment, fig-lora-architecture, fig-adaptation-decision-tree, fig-domain-shift-detection, fig-validation-pitfalls) but no '@fig-*' references appear in prose.
Recommendation: Add in-text references near the relevant discussion (e.g., 'Figure @fig-… summarizes…').

### ISSUE-005 (major) markdown_formatting
Rule: Avoid malformed or excessive emphasis markers (e.g., '****') that can render unpredictably.
Location: /mnt/data/p2-ch09-transfer.qmd lines 42-42
Heading path: Transfer and Adaptation > Feature Extraction with Frozen Backbones > Linear Probing
Evidence: Lines containing '****': 42
Recommendation: Replace quadruple-asterisk patterns with standard bold/italic markup (usually `**term**`). Verify rendered output for headings and emphasized terms.

### ISSUE-006 (minor) headings_style
Rule: Avoid leading 'The' in headings (prefer concise noun phrases).
Location: /mnt/data/p2-ch09-transfer.qmd lines 19-90
Heading path: Transfer and Adaptation > Source and Target Domains > The Gap Between Pretraining and Deployment
Evidence: line 19: 'The Gap Between Pretraining and Deployment'; line 90: 'The Risks of Unconstrained Adaptation'
Recommendation: Drop leading 'The' where feasible (e.g., 'CADD Framework' not 'The CADD Framework').

### ISSUE-007 (minor) headings_style
Rule: Heading length guideline: ## headings typically 3-5 words.
Location: /mnt/data/p2-ch09-transfer.qmd lines 51-265
Heading path: Transfer and Adaptation > Parameter-Efficient Fine-Tuning
Evidence: line 51 (2 words): 'Parameter-Efficient Fine-Tuning'; line 78 (2 words): 'Full Fine-Tuning'; line 97 (2 words): 'Probing Representations'; line 265 (2 words): 'Emerging Directions'
Recommendation: Shorten or expand out-of-range headings while keeping noun-phrase style, if enforcing strict compactness.

### ISSUE-008 (minor) headings_style
Rule: Heading length guideline: ### headings typically 2-4 words.
Location: /mnt/data/p2-ch09-transfer.qmd lines 19-259
Heading path: Transfer and Adaptation > Source and Target Domains > The Gap Between Pretraining and Deployment
Evidence: line 19 (6 words): 'The Gap Between Pretraining and Deployment'; line 90 (5 words): 'The Risks of Unconstrai...Transfer Without Task-Specific Data'; line 259 (6 words): 'Evaluation Practices That Reveal True Performance'
Recommendation: Shorten or expand out-of-range headings while keeping noun-phrase style, if enforcing strict compactness.

### ISSUE-009 (minor) headings_style
Rule: Prefer noun-phrase headings; avoid gerund (-ing) headings when possible.
Location: /mnt/data/p2-ch09-transfer.qmd lines 27-265
Heading path: Transfer and Adaptation > Source and Target Domains > Recognizing Transfer Outcomes
Evidence: line 27: 'Recognizing Transfer Outcomes'; line 84: 'Making Full Fine-Tuning Work'; line 97: 'Probing Represe...: 'Detecting and Mitigating Shift'; line 194: 'Diagnosing Negative Transfer'; line 265: 'Emerging Directions'
Recommendation: Rewrite gerund headings as noun phrases (e.g., 'Pretraining Objectives' instead of 'Pretraining').

### ISSUE-010 (moderate) style_false_enthusiasm
Rule: Avoid 'false enthusiasm' adjectives ('remarkable', 'impressive', 'powerful', etc.) unless quoting/citing field consensus.
Location: /mnt/data/p2-ch09-transfer.qmd lines 292-292
Heading path: Transfer and Adaptation > Amplification and Its Risks
Evidence: line 292: contains 'impressive'
Recommendation: Replace with neutral academic descriptors ('substantial', 'notable', 'high', 'consistent') or justify with citation/attribution if keeping evaluative language.
