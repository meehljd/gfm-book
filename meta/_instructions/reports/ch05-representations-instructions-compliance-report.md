# Compliance Review: `p2-ch05-representations` vs Project Instructions

Date: 2025-12-23

## Inputs
- Instructions: `claude-project-instructions.md`
- Chapter: `p2-ch05-representations.qmd` (221 lines)

## Automated Rule Checks

| Check | Result | Evidence |
|---|---:|---|
| Em-dash character (U+2014) count | 0 | PASS |
| Bullet/list lines (`-`, `*`, `+`, `•`, `1.`) | 0 | PASS |
| Meta-commentary triggers | 1 | FAIL (count=1) — See Issues for locations. |
| Figure blocks present | 5 | PASS (fig-tokenization-comparison, fig-biological-tokenization, fig-embedding-space, fig-position-encodings, fig-compression-resolution) |
| In-text figure references (`@fig-*`) | 0 | FAIL (No @fig-* references found.) |
| Bracket citations (`[@...]`) | 9 | INFO |
| Bracket citations followed by comma (`[@...],`) | 0 | PASS |
| Suspicious emphasis markers (`****`) | 1 | FAIL (count=1) |

## Issues

### ISSUE-001 (critical) output_format
Rule: All content must be delivered as markdown files (.md); never create .qmd files.
Location: /mnt/data/p2-ch05-representations.qmd lines 1-1
Heading path: Tokens and Embeddings
Evidence: File name is `p2-ch05-representations.qmd` (Quarto .qmd).
Recommendation: Convert/rename to `.md` for the deliverable. Keep Pandoc-compatible constructs (fenced divs for figures, cross-ref ids), but enforce the `.md` extension.

### ISSUE-002 (critical) style_meta_commentary
Rule: ZERO meta-commentary (avoid 'This chapter…', 'In this section…', 'in the following…' framing and chapter-outline narration).
Location: /mnt/data/p2-ch05-representations.qmd lines 7-7
Heading path: Tokens and Embeddings
Evidence: An analogy to natural language processing illuminates the fundamental tradeoffs. Training a language model o...ies through learned tokenization schemes, and traces how each choice shapes what downstream models can learn.
Recommendation: Rewrite to state stakes and claims directly, without referencing the chapter/section structure. If needed, use an explicit cross-reference (e.g., '@sec-…') rather than 'in the following'.

### ISSUE-003 (minor) cross_references
Rule: Use in-text figure references (@fig-*) where figures are discussed.
Location: /mnt/data/p2-ch05-representations.qmd lines 1-221
Heading path: Tokens and Embeddings
Evidence: Figure blocks present (fig-tokenization-comparison, fig-biological-tokenization, fig-embedding-space, fig-position-encodings, fig-compression-resolution) but no '@fig-*' references appear in prose.
Recommendation: Add in-text references near the relevant discussion (e.g., 'Figure @fig-… summarizes…').

### ISSUE-004 (major) markdown_formatting
Rule: Avoid malformed or excessive emphasis markers (e.g., '****') that can render unpredictably.
Location: /mnt/data/p2-ch05-representations.qmd lines 22-22
Heading path: Tokens and Embeddings > One-Hot Encoding: The convolutional neural network (CNN) Foundation
Evidence: Lines containing '****': 22
Recommendation: Replace quadruple-asterisk patterns with standard bold/italic markup (usually `**term**`). Verify rendered output for headings and emphasized terms.

### ISSUE-005 (minor) headings_style
Rule: Avoid leading 'The' in headings (prefer concise noun phrases).
Location: /mnt/data/p2-ch05-representations.qmd lines 209-209
Heading path: Tokens and Embeddings > The Compression-Resolution Trade-off
Evidence: line 209: 'The Compression-Resolution Trade-off'
Recommendation: Drop leading 'The' where feasible (e.g., 'CADD Framework' not 'The CADD Framework').

### ISSUE-006 (minor) headings_style
Rule: Heading length guideline: ## headings typically 3-5 words.
Location: /mnt/data/p2-ch05-representations.qmd lines 22-108
Heading path: Tokens and Embeddings > One-Hot Encoding: The convolutional neural network (CNN) Foundation
Evidence: line 22 (8 words): '**One-Hot Encoding**: The ****convolutional neural network** (CNN)** Foundation'; line 4...iologically-Informed Tokenization'; line 108 (6 words): 'From Tokens to Embeddings: Learning Representations'
Recommendation: Shorten or expand out-of-range headings while keeping noun-phrase style, if enforcing strict compactness.

### ISSUE-007 (minor) headings_style
Rule: Heading length guideline: ### headings typically 2-4 words.
Location: /mnt/data/p2-ch05-representations.qmd lines 193-193
Heading path: Tokens and Embeddings > Trade-offs and Practical Guidance > Vocabulary Size and Model Capacity
Evidence: line 193 (5 words): 'Vocabulary Size and Model Capacity'
Recommendation: Shorten or expand out-of-range headings while keeping noun-phrase style, if enforcing strict compactness.

### ISSUE-008 (minor) style_transition_cliche
Rule: Avoid 'However/Moreover/Importantly/…' as sentence starters (use sparingly).
Location: /mnt/data/p2-ch05-representations.qmd lines 128-128
Heading path: Tokens and Embeddings > Position Encodings: Where Tokens Live
Evidence: line 128: 'Moreover, …'
Recommendation: Rewrite to remove the sentence-starter adverb, or integrate contrast via sentence structure (e.g., 'Yet …', 'Despite …').
