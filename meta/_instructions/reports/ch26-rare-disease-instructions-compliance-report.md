# Instruction Compliance Report: Rare Disease Diagnosis
## Source
- File: `p6-ch26-rare-disease.qmd`
- Chapter title: Rare Disease Diagnosis
- Total lines: 222

## Summary of Issues
- **CRITICAL**: 2
- **HIGH**: 10
- **MEDIUM**: 5
- **LOW**: 1

## Issues

### CRITICAL
#### CRITICAL-01: OUTPUT_FORMAT_QMD
- Location: Line 1 (Section: Rare Disease Diagnosis)
- Evidence: Source file is `p6-ch26-rare-disease.qmd` (Quarto .qmd), but project instructions require delivering chapter prose as `.md`.
- Recommendation: Convert final deliverable to `.md` (no YAML frontmatter) per project output requirements.

#### CRITICAL-02: META_COMMENTARY
- Location: Line 7 (Section: Rare Disease Diagnosis)
- Evidence: …ne of evidence within structured interpretation frameworks. This chapter examines how foundation model outputs integrate into clinic…
- Recommendation: Remove self-referential framing (e.g., “This chapter…”, “In this chapter…”). State the substantive claims directly.


### HIGH
#### HIGH-01: NO_CITATIONS_DETECTED
- Location: Line 1 (Section: Rare Disease Diagnosis)
- Evidence: No citation keys of the form [@citekey] or @citekey were detected in this chapter.
- Recommendation: Add citations for technical claims (performance numbers, dataset sizes, benchmark results, historical facts) using the project’s citation style.

#### HIGH-02: MALFORMED_IMAGE_LINK
- Location: Line 14 (Section: Rare Disease Diagnosis > The Variant Prioritization Funnel)
- Evidence: ![**FIGURE PLACEHOLDER**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-03: MALFORMED_IMAGE_LINK
- Location: Line 48 (Section: Rare Disease Diagnosis > ACMG-AMP Criteria and Computational Evidence)
- Evidence: ![**FIGURE PLACEHOLDER**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-04: MALFORMED_IMAGE_LINK
- Location: Line 82 (Section: Rare Disease Diagnosis > Family-Based Analysis)
- Evidence: ![**FIGURE PLACEHOLDER A**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER%20A``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-05: MALFORMED_IMAGE_LINK
- Location: Line 84 (Section: Rare Disease Diagnosis > Family-Based Analysis)
- Evidence: ![**FIGURE PLACEHOLDER B**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER%20B``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-06: MALFORMED_IMAGE_LINK
- Location: Line 86 (Section: Rare Disease Diagnosis > Family-Based Analysis)
- Evidence: ![**FIGURE PLACEHOLDER C**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER%20C``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-07: MALFORMED_IMAGE_LINK
- Location: Line 126 (Section: Rare Disease Diagnosis > Somatic Variant Interpretation in Cancer > Germline versus Somatic Distinction)
- Evidence: ![**FIGURE PLACEHOLDER A**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER%20A``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-08: MALFORMED_IMAGE_LINK
- Location: Line 128 (Section: Rare Disease Diagnosis > Somatic Variant Interpretation in Cancer > Germline versus Somatic Distinction)
- Evidence: ![**FIGURE PLACEHOLDER B**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER%20B``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-09: MALFORMED_IMAGE_LINK
- Location: Line 154 (Section: Rare Disease Diagnosis > Laboratory Validation)
- Evidence: ![**FIGURE PLACEHOLDER**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-10: MALFORMED_IMAGE_LINK
- Location: Line 217 (Section: Rare Disease Diagnosis > The Interpretive Partnership)
- Evidence: ![**FIGURE PLACEHOLDER**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.


### MEDIUM
#### MEDIUM-01: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 27 (Section: Rare Disease Diagnosis > The Variant Prioritization Funnel > Population Frequency Filters)
- Evidence: Variants common in the general population are unlikely to cause rare, severe disease. If a variant appears in 1% of gnomAD individuals, it cannot plausibly explain a condition affecting one in 100,000 people under a dominant model. Frequency thresholds depend on inheritance mode and disease prevalence: dominant conditions with complete penetrance require extremely rare variants (often absent from population databases), while recessive conditions can tolerate higher carrier frequencies.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-02: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 29 (Section: Rare Disease Diagnosis > The Variant Prioritization Funnel > Population Frequency Filters)
- Evidence: The gnomAD database provides allele frequencies across over 800,000 individuals from diverse ancestries. Applying a frequency threshold of 0.01% for dominant conditions and 1% for recessive carriers typically removes 95% or more of variants from consideration. Ancestry-matched frequencies matter: a variant rare in European populations may be common in African or East Asian populations, and global frequency alone can be misleading.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-03: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 75 (Section: Rare Disease Diagnosis > ACMG-AMP Criteria and Computational Evidence > Calibrating Predictions to Evidence Strength)
- Evidence: For *AlphaMissense* and similar foundation models, published validation shows that the highest-scoring variants (above 0.9) achieve odds ratios exceeding the strong evidence threshold in some gene contexts. ClinGen expert panels have begun incorporating these calibrations for specific genes, allowing upgraded evidence strength when predictions meet defined criteria. Clinicians should follow gene-specific expert panel recommendations when available rather than applying uniform thresholds across all genes.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-04: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 95 (Section: Rare Disease Diagnosis > Family-Based Analysis > *de novo* Variants)
- Evidence: The informativeness of *de novo* status depends on the mutation rate at that site and the expected *de novo* rate for the variant class. The human germline mutation rate is approximately 1 to 1.5 new mutations per 100 million base pairs per generation. For protein-coding exons (approximately 30 million base pairs), each individual carries roughly one new coding variant on average. Finding a damaging *de novo* variant in a candidate gene is therefore much more suspicious than finding an inherited variant of similar predicted effect.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-05: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 137 (Section: Rare Disease Diagnosis > Somatic Variant Interpretation in Cancer > Driver Classification)
- Evidence: Among somatic mutations, identifying drivers requires different evidence than germline pathogenicity assessment. Recurrence across independent tumors suggests selective advantage: if *BRAF* V600E appears in 50% of melanomas, this frequency far exceeds what chance would predict, implying functional importance. Databases like COSMIC catalog somatic mutation frequencies across cancer types, enabling recurrence-based prioritization.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.


### LOW
#### LOW-01: FALSE_ENTHUSIASM_WORD
- Location: Line 79 (Section: Rare Disease Diagnosis > Family-Based Analysis)
- Evidence: …relies on proband sequence alone. Family structure provides powerful additional information through inheritance pattern constrai…
- Recommendation: Replace with a more precise, neutral descriptor (e.g., “high-capacity”, “expressive”, “high-performing”) unless quoting a source.

## Quick Fix Checklist
- [ ] Remove meta-commentary (“This chapter…”, “In this chapter…”, “In this section…”).
- [ ] Audit numeric/statistical claims and add citations where needed.
- [ ] Fix malformed image placeholder Markdown so Quarto renders figures correctly.
- [ ] Convert final deliverable to `.md` per output requirements.
- [ ] Replace vague enthusiasm adjectives (“powerful”, “impressive”, “remarkable”) with precise neutral language.

