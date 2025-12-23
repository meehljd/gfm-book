# Compliance Review: `p1-ch04-vep-classical` vs Project Instructions

Date: 2025-12-23

## Inputs
- Instructions: `claude-project-instructions.md`
- Chapter: `p1-ch04-vep-classical.qmd` (264 lines)

## Automated Rule Checks

| Check | Result | Evidence |
|---|---:|---|
| Em-dash character (U+2014 (em dash)) count | 1 | FAIL (line 26) |
| Bullet list lines (`-`, `*`, `+`, `•`) | 0 | PASS |
| Meta-commentary triggers ('This chapter…', 'in/throughout this chapter…') | 5 | FAIL (lines 5, 56, 162, 254, 256) |
| Figure blocks present | 5 | PASS (fig-variant-funnel, fig-conservation-scores, fig-cadd-training, fig-ensemble-performance, fig-circularity-problem) |
| In-text figure references (`@fig-*`) | 0 | WARN |
| Citation brackets (`[@...]`) | 10 | INFO |
| Bracket citations followed by comma (mid-sentence) | 0 | PASS |

## Issues

### ISSUE-001 (critical)
- Type: output_format
- Rule: All content must be delivered as markdown files (.md); never create .qmd files.
- Location: `/mnt/data/p1-ch04-vep-classical.qmd` lines 1-1
- Heading path: Classical Variant Prediction
- Evidence: File name is `p1-ch04-vep-classical.qmd` (Quarto .qmd).
- Recommendation: Convert/rename to `.md` for the deliverable. Keep Pandoc-compatible constructs (fenced divs for figures, cross-ref ids), but enforce the `.md` extension.

### ISSUE-002 (critical)
- Type: style_em_dash
- Rule: ZERO em-dashes (—). Use commas, parentheses, colons/semicolons, or split sentences instead.
- Location: `/mnt/data/p1-ch04-vep-classical.qmd` lines 26-26
- Heading path: Classical Variant Prediction > Conservation-Based Approaches
- Evidence: [High] Multi-panel figure. Panel A: Multiple sequence alignment at a highly conserved position (same nucleotide across 30+ species) vs a neutrally evolving position (variable nucleotides). Show phylogenetic tree alongsi…
- Recommendation: Rewrite the caption sentence to remove the em-dash (e.g., replace with a comma or period).

### ISSUE-003 (major)
- Type: style_meta_commentary
- Rule: Zero meta-commentary (avoid 'This chapter ...' framing and chapter-outline narration).
- Location: `/mnt/data/p1-ch04-vep-classical.qmd` lines 5-5
- Heading path: Classical Variant Prediction
- Evidence: This chapter examines the conceptual foundations and practical methods that dominated variant interpretation before the foundation model era. The trajectory traces from single-signal predictors through increasingly soph…
- Recommendation: Rewrite to state stakes directly without describing what the chapter will do. Remove 'This chapter examines…' and avoid enumerating the chapter trajectory as an outline.

### ISSUE-004 (minor)
- Type: style_meta_commentary
- Rule: Avoid chapter-structure narration (e.g., 'later in this chapter'); prefer direct statements or explicit cross-references.
- Location: `/mnt/data/p1-ch04-vep-classical.qmd` lines 56-56
- Heading path: Classical Variant Prediction > Conservation-Based Approaches > Clinical Application and Boundaries
- Evidence: These boundaries do not diminish the value of conservation; they define where that value applies. Conservation provides information largely orthogonal to population frequency (which reflects recent human history rather …
- Recommendation: Delete 'later in this chapter' or replace with a direct claim (or a specific cross-reference) without chapter-structure scaffolding.

### ISSUE-005 (minor)
- Type: style_meta_commentary
- Rule: Avoid unnecessary 'in this chapter' self-references; prefer content-scoped phrasing.
- Location: `/mnt/data/p1-ch04-vep-classical.qmd` lines 162-162
- Heading path: Classical Variant Prediction > The CADD Framework > What CADD Measures Versus What Clinicians Need
- Evidence: CADD also cannot account for genetic background, environmental interactions, or incomplete penetrance. A variant might be highly deleterious in one genetic context and tolerated in another, but CADD assigns a single sco…
- Recommendation: Replace 'in this chapter' with 'among classical predictors' / 'across these methods' / 'in feature-engineered approaches' (or similar).

### ISSUE-006 (major)
- Type: style_meta_commentary
- Rule: Zero meta-commentary (avoid 'Throughout this chapter, we have seen…' recap framing).
- Location: `/mnt/data/p1-ch04-vep-classical.qmd` lines 254-254
- Heading path: Classical Variant Prediction > Limitations of the Feature Engineering Paradigm > The Persistent Gap Between Measurement and Need
- Evidence: Throughout this chapter, we have seen how each classical method measures something related to but distinct from clinical pathogenicity. Conservation scores measure evolutionary constraint. Protein-level predictors measu…
- Recommendation: Rewrite as a direct synthesis without narrating the chapter (e.g., 'Classical predictors target evolutionary constraint, structural disruption, or evolutionary tolerance; none directly answers…').

### ISSUE-007 (minor)
- Type: style_meta_commentary
- Rule: Avoid 'methods in this chapter' phrasing; keep claims content-based.
- Location: `/mnt/data/p1-ch04-vep-classical.qmd` lines 256-256
- Heading path: Classical Variant Prediction > Limitations of the Feature Engineering Paradigm > The Persistent Gap Between Measurement and Need
- Evidence: This gap is not merely a limitation of specific methods but reflects something deeper about the variant interpretation problem. The clinically relevant question depends on context (which tissue, which genetic background…
- Recommendation: Replace 'The methods in this chapter' with 'Classical methods' / 'These approaches' / 'Feature-engineered predictors' (or similar).

### ISSUE-008 (minor)
- Type: style_meta_commentary
- Rule: Avoid generic 'chapters that follow' structural narration; use explicit forward references or direct topical framing.
- Location: `/mnt/data/p1-ch04-vep-classical.qmd` lines 264-264
- Heading path: Classical Variant Prediction > Limitations of the Feature Engineering Paradigm > From Features to Representations
- Evidence: Classical methods remain valuable: as baselines that establish the performance floor modern methods must exceed, as interpretable components when understanding matters as much as prediction, and as reminders of what the…
- Recommendation: Prefer an explicit cross-reference (e.g., '@sec-vep-fm') or reframe as a direct topical transition without mentioning chapter order.

### ISSUE-009 (moderate)
- Type: citations_numbers
- Rule: Specific statistics/percentages should be cited when used to support a technical argument.
- Location: `/mnt/data/p1-ch04-vep-classical.qmd` lines 50-50
- Heading path: Classical Variant Prediction > Conservation-Based Approaches > Clinical Application and Boundaries
- Evidence: The boundaries of conservation-based approaches are equally important to recognize, and these boundaries are not merely technical inconveniences but reflect fundamental gaps in what evolutionary signal can reveal. Conse…
- Recommendation: Add a citation supporting the '3% of the human genome' claim (or soften/rephrase if intended as a rough illustrative scale).

### ISSUE-010 (minor)
- Type: cross_references
- Rule: Use in-text figure references (@fig-*) where figures are discussed.
- Location: `/mnt/data/p1-ch04-vep-classical.qmd` lines 9-208
- Heading path: Classical Variant Prediction
- Evidence: Figure blocks present (fig-variant-funnel, fig-conservation-scores, fig-cadd-training, fig-ensemble-performance, fig-circularity-problem) but no '@fig-*' references appear in prose.
- Recommendation: Add in-text references near the relevant discussion (e.g., 'Figure @fig-variant-funnel summarizes…').

### ISSUE-011 (minor)
- Type: headings_style
- Rule: Avoid leading 'The' in headings (prefer concise noun phrases).
- Location: `/mnt/data/p1-ch04-vep-classical.qmd` lines 103-252
- Heading path: (headings)
- Evidence: line 103: 'The CADD Framework'; line 210: 'The Circularity Problem'; line 240: 'The Feature Ceiling'; line 252: 'The Persistent Gap Between Measurement and Need'
- Recommendation: Drop leading 'The' where feasible (e.g., 'CADD Framework', 'Circularity Problem', 'Feature Ceiling', 'Persistent Gap Between Measurement and Need').

### ISSUE-012 (minor)
- Type: headings_style
- Rule: Heading length guidelines: ## headings typically 3-5 words; ### headings typically 2-4 words.
- Location: `/mnt/data/p1-ch04-vep-classical.qmd` lines 1-258
- Heading path: (headings)
- Evidence: ## out of range: line 236 (6 words): Limitations of the Feature Engineering Paradigm ### out of range: line 40 (7 words): What Conservation Measures Versus What Clinicians Need; line 62 (6 words): SIFT: Sequence Homology as Functional Constraint; line 72 (5 words): PolyPhen-2: Integrating Structure and Sequence; line 82 (8 words): What Protein-Level Predictors Measure Versus What Clinicians Need; line 109 (6 words): Evolutionary Proxy Training and Label Sources; line 154 (7 words): What CADD Measures Versus What Clinicians Need; line 169 (1 words): REVEL; line 179 (1 words): M-CAP; line 252 (7 words): The Persistent Gap Between Measurement and Need
- Recommendation: If enforcing strict compactness, shorten the out-of-range headings while keeping noun-phrase style.

### ISSUE-013 (minor)
- Type: headings_style
- Rule: Prefer noun-phrase headings; avoid gerund (-ing) headings when possible.
- Location: `/mnt/data/p1-ch04-vep-classical.qmd` lines 30-30
- Heading path: (headings)
- Evidence: line 30: 'Measuring Evolutionary Constraint'
- Recommendation: Convert to noun phrases where feasible (e.g., 'Evolutionary Constraint Measurement', 'Structure and Sequence Integration').

### ISSUE-014 (minor)
- Type: typography
- Rule: Avoid excessive bolding in a single sentence; bold glossary terms on first mention only to reduce visual noise.
- Location: `/mnt/data/p1-ch04-vep-classical.qmd` lines 5-202
- Heading path: (multiple locations)
- Evidence: Lines with ≥2 bold spans: line 5; line 7; line 123; line 202
- Recommendation: If desired, keep bold for the single primary term per sentence and move other term explanations to adjacent sentences (or drop bold after first mention).

### ISSUE-015 (minor)
- Type: style_structure
- Rule: Avoid ordinal scaffolding ('one of two… the second…') when strict 'no numbered-lists-in-prose' enforcement is desired.
- Location: `/mnt/data/p1-ch04-vep-classical.qmd` lines 202-202
- Heading path: Classical Variant Prediction > Circularity and Ascertainment Bias
- Evidence: A diagnostic laboratory classifies a novel missense variant as pathogenic based partly on its high CADD score. That classification enters ClinVar. Two years later, a benchmarking study evaluates CADD performance on Clin…
- Recommendation: Rewrite as narrative without ordinal markers (e.g., name both problems in one sentence, then develop each in turn without 'second').
