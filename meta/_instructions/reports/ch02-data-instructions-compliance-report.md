# Compliance Review: `p1-ch02-data` vs Project Instructions

Date: 2025-12-23

## Inputs
- Instructions: `claude-project-instructions.md`
- Chapter: `p1-ch02-data.qmd` (232 lines)

## Automated Rule Checks

| Check | Result | Evidence |
|---|---:|---|
| Em-dash character (U+2014 (em dash)) count | 0 | PASS |
| Bullet list lines (`-`, `*`, `+`, `•`) | 0 | PASS |
| Meta-commentary triggers ('This chapter…', 'throughout this chapter…') | 3 | FAIL (lines 13, 58, 81) |
| Figure blocks present | 4 | PASS (fig-data-ecosystem, fig-ancestry-representation, fig-functional-genomics-matrix, fig-clinvar-landscape) |
| In-text figure references (`@fig-*`) | 0 | WARN |
| Citation brackets (`[@...]`) | 42 | INFO |
| Bracket citations followed by comma (mid-sentence) | 3 | WARN (lines 25, 95, 139) |

## Issues

### ISSUE-001 (critical)
- Type: output_format
- Rule: All content must be delivered as markdown files (.md); never create .qmd files.
- Location: `/mnt/data/p1-ch02-data.qmd` lines 1-1
- Heading path: The Data Landscape
- Evidence: File name is p1-ch02-data.qmd (Quarto .qmd).
- Recommendation: Convert/rename to .md. Ensure Quarto constructs remain Pandoc-compatible (fenced divs, cross-ref ids) or adjust accordingly.

### ISSUE-002 (major)
- Type: style_meta_commentary
- Rule: Zero meta-commentary (avoid 'This chapter ...' framing).
- Location: `/mnt/data/p1-ch02-data.qmd` lines 13-13
- Heading path: The Data Landscape
- Evidence: This chapter surveys the major data resources that underpin genomic machine learning, emphasizing what each resource measu…
- Recommendation: Rewrite to remove self-referential framing. State the stakes directly (e.g., 'Critical literacy about data provenance is prerequisite...') without describing what the chapter will do.

### ISSUE-003 (minor)
- Type: style_meta_commentary
- Rule: Avoid chapter-structure narration (e.g., 'throughout this chapter').
- Location: `/mnt/data/p1-ch02-data.qmd` lines 58-58
- Heading path: The Data Landscape > Population Variant Catalogs and Allele Frequencies > dbSNP and Variant Identifiers
- Evidence: …ces back to dbSNP and enables integration with functional annotations, clinical databases, and other catalogs throughout this chapter.
- Recommendation: Delete 'throughout this chapter' or replace with a direct statement about integration across resources.

### ISSUE-004 (minor)
- Type: style_meta_commentary
- Rule: Avoid unnecessary self-referential chapter mentions; prefer direct cross-references.
- Location: `/mnt/data/p1-ch02-data.qmd` lines 81-81
- Heading path: The Data Landscape > Cohorts, Biobanks, and GWAS Summary Data
- Evidence: …This tension between scientific utility and representational equity shapes every biobank-derived resource in this chapter and is discussed in detail in @sec-confounding.
- Recommendation: If strict 'no meta-commentary' enforcement is desired, drop 'this chapter' (e.g., 'This tension... is discussed in @sec-confounding.').

### ISSUE-005 (moderate)
- Type: citations_numbers
- Rule: Specific percentages/statistics should be cited (including in figure captions/recommendations).
- Location: `/mnt/data/p1-ch02-data.qmd` lines 47-47
- Heading path: The Data Landscape > Population Variant Catalogs and Allele Frequencies
- Evidence: …, GTEx donors, GWAS Catalog participants. Highlight the persistent European overrepresentation (approximately 78% of GWAS participants as of 2019) against global population proportions. Include a small world map inset show…
- Recommendation: Add a citation supporting the 'approximately 78% of GWAS participants as of 2019' statistic (likely @sirugo_diversity_2019 or another primary source).

### ISSUE-006 (minor)
- Type: cross_references
- Rule: Use in-text figure references (@fig-*) where figures are discussed.
- Location: `/mnt/data/p1-ch02-data.qmd` lines 7-201
- Heading path: The Data Landscape
- Evidence: Figure blocks present (fig-data-ecosystem, fig-ancestry-representation, fig-functional-genomics-matrix, fig-clinvar-landscape) but no '@fig-*' references appear in prose.
- Recommendation: Add in-text references (e.g., 'Figure @fig-data-ecosystem summarizes...') near the relevant discussion.

### ISSUE-007 (minor)
- Type: headings_style
- Rule: Avoid leading articles in headings; prefer concise noun phrases.
- Location: `/mnt/data/p1-ch02-data.qmd` lines 1-1
- Heading path: The Data Landscape
- Evidence: The Data Landscape
- Recommendation: Rename '# The Data Landscape' to '# Data Landscape' (or similar) if enforcing strict heading conventions.

### ISSUE-008 (minor)
- Type: headings_style
- Rule: Heading length guidelines: ## headings typically 3-5 words; ### headings typically 2-4 words.
- Location: `/mnt/data/p1-ch02-data.qmd` lines 40-135
- Heading path: The Data Landscape > Population Variant Catalogs and Allele Frequencies
- Evidence: ## out of range: line 40 (6 words): Population Variant Catalogs and Allele Frequencies; line 77 (6 words): Cohorts, Biobanks, and GWAS Summary Data; line 169 (6 words): Variant Interpretation Databases and Clinical Labels; line 226 (2 words): Inherited Constraints. ### out of range: line 60 (6 words): 1000 Genomes and Early Reference Panels; line 106 (5 words): ENCODE, Roadmap, and Related Consortia; line 129 (5 words): From Assays to Training Labels; line 135 (7 words): Deep Mutational Scanning and Multiplexed Variant Assays.
- Recommendation: If enforcing strict compactness, shorten these headings to 3-5 (##) / 2-4 (###) words while preserving meaning.

### ISSUE-009 (minor)
- Type: typography
- Rule: Avoid multiple bold terms in the same sentence when it adds visual noise; bold glossary terms on first mention.
- Location: `/mnt/data/p1-ch02-data.qmd` lines 50-213
- Heading path: The Data Landscape > Population Variant Catalogs and Allele Frequencies
- Evidence: Multiple bold terms appear in single sentences at lines 50, 102, and 213.
- Recommendation: If desired, keep bold for only the single primary glossary term per sentence and move other term explanations to adjacent sentences.

### ISSUE-010 (minor)
- Type: citations_style
- Rule: Avoid mid-sentence bracket citations that break flow; prefer end-of-sentence brackets or in-prose attribution.
- Location: `/mnt/data/p1-ch02-data.qmd` lines 25-139
- Heading path: The Data Landscape > Reference Genomes and Gene Annotations > Reference Assemblies
- Evidence: Bracket citations followed by commas (mid-sentence) at lines 25, 95, and 139.
- Recommendation: Rewrite as in-prose citations (e.g., 'Sullivan et al. ...') or move citations to sentence ends.

### ISSUE-011 (minor)
- Type: style_tone
- Rule: Avoid false enthusiasm adjectives (e.g., 'powerful') unless used with technical precision.
- Location: `/mnt/data/p1-ch02-data.qmd` lines 50-50
- Heading path: The Data Landscape > Population Variant Catalogs and Allele Frequencies
- Evidence: …, the proportion of chromosomes in a reference population carrying a given variant, serves as one of the most powerful priors in variant interpretation. Beyond simple filtering, allele frequencies inform statistical frameworks f…
- Recommendation: Consider replacing 'most powerful priors' with a more specific claim (e.g., 'one of the most informative priors') if tone enforcement is strict.