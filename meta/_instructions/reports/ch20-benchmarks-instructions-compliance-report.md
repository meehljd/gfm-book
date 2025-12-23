# Instruction Compliance Report: Benchmarks
## Source
- File: `p5-ch20-benchmarks.qmd`
- Chapter title: Benchmarks
- Total lines: 330

## Summary of Issues
- **CRITICAL**: 2
- **HIGH**: 0
- **MEDIUM**: 4
- **LOW**: 0

## Issues

### CRITICAL
#### CRITICAL-01: OUTPUT_FORMAT_QMD
- Location: Line 1 (Section: Benchmarks)
- Evidence: Source file is `p5-ch20-benchmarks.qmd` (Quarto .qmd), but project instructions require delivering chapter prose as `.md`.
- Recommendation: Convert final deliverable to `.md` (no YAML frontmatter) per project output requirements.

#### CRITICAL-02: META_COMMENTARY
- Location: Line 8 (Section: Benchmarks)
- Evidence: This chapter surveys the benchmark landscape for genomic foundation mode…
- Recommendation: Remove self-referential framing (e.g., “This chapter…”, “In this chapter…”). State the substantive claims directly.


### MEDIUM
#### MEDIUM-01: TRANSITION_STARTER
- Location: Line 146 (Section: Benchmarks > Variant Effect Prediction Benchmarks > Deep Mutational Scanning Benchmarks)
- Evidence: …n clinical inference that may involve multiple assumptions. However, the relationship between DMS fitness and clinical pathogen…
- Recommendation: Rephrase to avoid starting a sentence with this transition word, or reduce frequency.

#### MEDIUM-02: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 238 (Section: Benchmarks > Benchmark Saturation and Staleness > Saturation: When Benchmarks Stop Discriminating)
- Evidence: Saturation is problematic because it removes the benchmark's value for model selection. When all reasonable models achieve 0.97 AUROC, differences between 0.970 and 0.975 are unlikely to reflect meaningful capability differences. Yet benchmark reporting conventions often emphasize such decimal places, creating an illusion of progress.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-03: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 286 (Section: Benchmarks > The Benchmark-Deployment Gap > Calibration Requirements)
- Evidence: Clinical deployment requires not just accurate rankings but accurate probability estimates. A variant classifier that achieves 0.95 AUROC by assigning probability 0.9 to all pathogenic variants and 0.3 to all benign variants discriminates well but provides miscalibrated uncertainty. Clinical decisions that depend on thresholded predictions (reporting variants above a certain probability) will perform poorly if those probabilities don't reflect actual pathogenicity rates.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-04: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 313 (Section: Benchmarks > Systematic Gaps in Current Benchmarks)
- Evidence: [High] Grouped bar chart or heatmap. Rows: Different tasks/models. Columns: Ancestry groups (European, African, East Asian, South Asian, Admixed). Values: Performance metrics. Specific comparisons: PGS 40-75% reduction non-European; ClinVar-trained models across ancestries. Annotations: sample sizes, significance, training data representation. Key insight: aggregate conceals systematic failures.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

## Quick Fix Checklist
- [ ] Remove meta-commentary (“This chapter…”, “In this chapter…”, “In this section…”).
- [ ] Audit numeric/statistical claims and add citations where needed.
- [ ] Convert final deliverable to `.md` per output requirements.
- [ ] Reduce sentence-start transitions (e.g., “However,”).

