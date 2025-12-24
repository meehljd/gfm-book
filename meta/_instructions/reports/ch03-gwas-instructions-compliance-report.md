# Compliance Review: `p1-ch03-gwas` vs Project Instructions

Date: 2025-12-23

## Inputs
- Instructions: `claude-project-instructions.md`
- Chapter: `p1-ch03-gwas.qmd` (280 lines)

## Automated Rule Checks

| Check | Result | Evidence |
|---|---:|---|
| Em-dash character (U+2014 (em dash)) count | 2 | FAIL (lines 58, 116) |
| Bullet list lines (`-`, `*`, `+`, `•`) | 0 | PASS |
| Meta-commentary triggers ('This chapter…', 'In this chapter…', 'This section…') | 0 | PASS |
| Figure blocks present | 5 | PASS (fig-manhattan-anatomy, fig-heritability-decomposition, fig-ld-tag-causal, fig-pgs-construction, fig-pgs-portability) |
| In-text figure references (`@fig-*`) | 0 | WARN |
| Citation brackets (`[@...]`) | 18 | INFO |
| Bracket citations followed by comma (mid-sentence) | 0 | PASS |

## Issues

### ISSUE-001 (critical)
- Type: output_format
- Rule: All content must be delivered as markdown files (.md); never create .qmd files.
- Location: `/mnt/data/p1-ch03-gwas.qmd` lines 1-1
- Heading path: GWAS and Polygenic Scores
- Evidence: File name is `p1-ch03-gwas.qmd` (Quarto .qmd).
- Recommendation: Convert/rename to `.md`. Keep Pandoc-compatible constructs (fenced divs for figures, cross-ref ids), but enforce the `.md` extension as the deliverable.

### ISSUE-002 (critical)
- Type: style_em_dash
- Rule: ZERO em-dashes (—). Use commas, parentheses, colons/semicolons, or split sentences instead.
- Location: `/mnt/data/p1-ch03-gwas.qmd` lines 58-58
- Heading path: GWAS and Polygenic Scores > The GWAS Framework > Visualizing Genome-Wide Results
- Evidence: …ed along x-axis; (5) Inset zoom on one peak showing how multiple variants exceed threshold—illustrating that GWAS identifies loci, not causal variants. Include Q-Q plot inset showin…
- Recommendation: Rewrite the caption to remove the em-dash. Example: change 'exceed threshold—illustrating…' to 'exceed threshold, illustrating…' or split into two sentences.

### ISSUE-003 (critical)
- Type: style_em_dash
- Rule: ZERO em-dashes (—). Use commas, parentheses, colons/semicolons, or split sentences instead.
- Location: `/mnt/data/p1-ch03-gwas.qmd` lines 116-116
- Heading path: GWAS and Polygenic Scores > Linkage Disequilibrium and the Association-Causation Gap
- Evidence: …e of LD. Panel C: Same causal variant shown in two populations with different LD structure—in one population, tags are highly correlated with causal variant; in another, the correla…
- Recommendation: Rewrite the caption to remove the em-dash. Example: replace 'LD structure—in one population…' with 'LD structure. In one population…' or use parentheses.

### ISSUE-004 (minor)
- Type: cross_references
- Rule: Use in-text figure references (@fig-*) where figures are discussed.
- Location: `/mnt/data/p1-ch03-gwas.qmd` lines 55-252
- Heading path: GWAS and Polygenic Scores
- Evidence: Figure blocks present (fig-manhattan-anatomy, fig-heritability-decomposition, fig-ld-tag-causal, fig-pgs-construction, fig-pgs-portability) but no '@fig-*' references appear in prose.
- Recommendation: Add in-text references near the relevant discussion (e.g., 'Figure @fig-manhattan-anatomy illustrates…').

### ISSUE-005 (minor)
- Type: headings_style
- Rule: Avoid leading 'The' in headings (prefer concise noun phrases).
- Location: `/mnt/data/p1-ch03-gwas.qmd` lines 9-258
- Heading path: (headings)
- Evidence: line 9 'The GWAS Framework'; line 119 'The Structure of Linkage Disequilibrium'; line 139 'The Statistical Framework'; line 258 'The Portability Problem'
- Recommendation: Drop leading 'The' where feasible (e.g., 'GWAS Framework', 'Structure of Linkage Disequilibrium', 'Statistical Framework', 'Portability Problem').

### ISSUE-006 (minor)
- Type: headings_style
- Rule: Heading length guidelines: ## headings typically 3-5 words; ### headings 2-4 words.
- Location: `/mnt/data/p1-ch03-gwas.qmd` lines 19-135
- Heading path: (headings)
- Evidence: line 19 (5 words) 'Association Models for Quantitative Traits'; line 33 (5 words) 'Association Models for Disease Outcomes'; line 87 (6 words) 'SNP-Heritability and the Missing Heritability Problem'; line 95 (6 words) 'Implications for GWAS and Polygenic Scores'; line 103 (6 words) 'Linkage Disequilibrium and the Association-Causation Gap'; line 119 (5 words) 'The Structure of Linkage Disequilibrium'; line 127 (7 words) 'Causal Variants, Tag Variants, and GWAS Catalogs'; line 135 (6 words) 'Fine-Mapping: From Loci to Causal Variants'
- Recommendation: If enforcing strict compactness, shorten to 3-5 words for ## and 2-4 words for ### while keeping noun-phrase style (e.g., 'Quantitative Trait Models', 'Disease Association Models', 'Missing Heritability', 'GWAS Causation Gap').

### ISSUE-007 (minor)
- Type: headings_style
- Rule: Prefer noun-phrase headings; avoid gerund (-ing) headings when possible.
- Location: `/mnt/data/p1-ch03-gwas.qmd` lines 47-218
- Heading path: (headings)
- Evidence: line 47 'Visualizing Genome-Wide Results'; line 61 'Controlling for Population Structure'; line 149 'Leveraging Functional Annotations'; line 190 'Clumping and Thresholding'; line 218 'Interpreting Polygenic Scores'
- Recommendation: Convert to noun phrases (e.g., 'Genome-Wide Result Visualization', 'Population Structure Control', 'Functional Annotation Priors', 'C+T Method', 'Polygenic Score Interpretation').

### ISSUE-008 (moderate)
- Type: style_structure
- Rule: Avoid numbered lists disguised as prose (e.g., 'First… Second… Third…') in flowing narrative.
- Location: `/mnt/data/p1-ch03-gwas.qmd` lines 145-145
- Heading path: GWAS and Polygenic Scores > Fine-Mapping: From Loci to Causal Variants > The Statistical Framework
- Evidence: The procedure typically proceeds as follows. First, researchers define a region around an index SNP, often all variants within 1 megabase. Second, the…
- Recommendation: Rewrite as narrative (use a colon/semicolons without ordinal markers) or move stepwise material into a table/figure caption. Keep prose flowing without 'First/Second/Third' scaffolding.

### ISSUE-009 (moderate)
- Type: style_structure
- Rule: Avoid numbered lists disguised as prose (e.g., 'First… Second… Third…') in flowing narrative.
- Location: `/mnt/data/p1-ch03-gwas.qmd` lines 194-194
- Heading path: GWAS and Polygenic Scores > Polygenic Score Construction > Clumping and Thresholding
- Evidence: The procedure involves three steps. First, clumping: rank variants by p-value, then iteratively select the most significant variant and remov…
- Recommendation: Rewrite as narrative (use a colon/semicolons without ordinal markers) or present steps in a table (tables are an allowed exception to the no-bullets rule).

### ISSUE-010 (minor)
- Type: style_tone
- Rule: Avoid false enthusiasm adjectives (e.g., 'remarkable', 'impressive') unless used with technical precision.
- Location: `/mnt/data/p1-ch03-gwas.qmd` lines 5-5
- Heading path: GWAS and Polygenic Scores
- Evidence: …ght and blood pressure to schizophrenia and type 2 diabetes. These associations replicate across studies with remarkable consistency, confirming that the signals are real. Yet the path from associated region to biological mechanis…
- Recommendation: If tone enforcement is strict, replace 'remarkable consistency' with a more neutral phrasing (e.g., 'high consistency' or 'consistent replication across studies').

### ISSUE-011 (moderate)
- Type: citations_numbers
- Rule: Specific clinical performance comparisons should be cited near the claim.
- Location: `/mnt/data/p1-ch03-gwas.qmd` lines 7-7
- Heading path: GWAS and Polygenic Scores
- Evidence: …es achieve clinically meaningful discrimination: individuals in the top percentile of coronary artery disease risk have odds ratios comparable to monogenic familial hypercholesterolemia. Yet polygenic scores inherit all the limitations of the associat…
- Recommendation: Add a supporting citation near this statement (likely the same sources cited later: [@khera_genome-wide_2017] and related PGS clinical stratification work), or soften the comparison to avoid an unsupported performance claim in the introduction.