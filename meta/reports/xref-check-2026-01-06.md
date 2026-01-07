# Cross-Reference Report

Generated: 2026-01-06
Scope: Entire book

## Summary

| Metric | Count |
|--------|------:|
| Total section definitions | 938 |
| Unique cross-references used | 226 |
| Total cross-reference instances | ~850 |
| **Broken references** | **0** |
| Orphaned sections (never referenced) | 713 |

**Status**: All cross-references resolve correctly. No broken links.

## Cross-Reference Statistics by Chapter

### Most Cross-Referenced Chapters (incoming)

| Chapter | Incoming Refs | Key Topic |
|---------|--------------|-----------|
| @sec-ch22-confounding | 45 | Confounders and Leakage |
| @sec-ch14-vep-fm | 36 | Variant Effect Prediction |
| @sec-ch13-regulatory | 36 | Regulatory Models |
| @sec-ch12-protein-lm | 35 | Protein Language Models |
| @sec-ch11-dna-lm | 30 | DNA Language Models |
| @sec-ch24-interpretability | 27 | Interpretability |
| @sec-ch21-eval | 27 | Evaluation Principles |
| @sec-ch26-rare-disease | 26 | Rare Disease Diagnosis |
| @sec-ch09-transfer | 25 | Transfer and Adaptation |

### Chapters with Most Outgoing References

| File | Outgoing Refs |
|------|--------------|
| p6-ch27-drug-discovery.qmd | 32 |
| p5-ch20-benchmarks.qmd | 32 |
| p3-ch11-dna-lm.qmd | 28 |
| p6-ch25-clinical-risk.qmd | 26 |
| p4-ch19-multi-omics.qmd | 25 |
| p4-ch18-networks.qmd | 25 |
| p3-ch10-fm-principles.qmd | 25 |
| p2-ch08-pretraining.qmd | 25 |
| p3-ch14-vep-fm.qmd | 24 |
| p2-ch09-transfer.qmd | 24 |

### Least Cross-Referenced Main Chapters

| Chapter | Incoming Refs | Notes |
|---------|--------------|-------|
| @sec-ch01-ngs | 4 | Foundational, less referenced |
| @sec-ch15-rna | 5 | RNA chapter, somewhat standalone |
| @sec-ch27-drug-discovery | 7 | Late chapter |
| @sec-ch18-networks | 8 | Networks chapter |

## Orphaned Sections Analysis

**713 sections** are defined but never cross-referenced. This is expected for:
- Subsections (### level) that don't need direct references
- Self-contained sections within their chapter

### Sample Orphaned Sections by Chapter

#### Chapter 1 (32 orphaned of ~40 total)
Most subsections are internal to the chapter:
- `sec-ch01-alignment`, `sec-ch01-artifacts`, `sec-ch01-benchmarks`
- `sec-ch01-giab`, `sec-ch01-glnexus`, `sec-ch01-hla`

#### Chapter 2 (18 orphaned)
- `sec-ch02-assays-labels`, `sec-ch02-binary-phenotypes`
- `sec-ch02-cistrome`, `sec-ch02-clingen`

#### Chapter 3 (20 orphaned)
- `sec-ch03-absolute-risk`, `sec-ch03-bayesian-pgs`
- `sec-ch03-fine-mapping-stats`, `sec-ch03-functional-priors`

**Note**: Most orphaned sections are fine - they're subsections that provide detail within their chapter. The chapter-level sections are well cross-referenced.

## Most Heavily Cross-Referenced Sections

These sections are referenced from multiple chapters:

| Section | References | Topic |
|---------|-----------|-------|
| @sec-ch22-ancestry-confounding | 13 | Population structure as confounder |
| @sec-ch13-enformer | 12 | Enformer architecture |
| @sec-ch23-calibration | 12 | Model calibration |
| @sec-ch03-portability | 12 | PGS portability problem |
| @sec-ch06-spliceai | 7 | SpliceAI model |
| @sec-ch02-dms | 7 | Deep mutational scanning |
| @sec-ch02-gnomad | 6 | gnomAD database |
| @sec-ch02-clinvar | 6 | ClinVar database |
| @sec-ch14-acmg-mapping | 6 | ACMG classification mapping |

## Cross-Reference Opportunities

Based on TODO notes and content analysis, these cross-references should be added:

### From TODO/notes.md Analysis

| Source | Target | Reason |
|--------|--------|--------|
| Ch11 (benchmarks section) | Ch20 | Benchmark details should be in Ch20 |
| Ch11 (practical use) | Ch5-9 | Transfer/adaptation covered there |
| Ch14 (uncertainty) | Ch23 | Avoid repeating Ch23 content |
| Ch14 (SpliceAI clinical) | Ch14 §14.5.3 | Internal ACMG mapping reference |

### Potential New Cross-References

Based on content overlap, consider adding:

| From Section | To Section | Topic Connection |
|--------------|------------|------------------|
| @sec-ch11-probing | @sec-ch12-emergent-knowledge | What models learn |
| @sec-ch11-benchmark-limitations | @sec-ch20-systematic-gaps | Benchmark problems |
| @sec-ch16-batch-effects | @sec-ch22-batch-effects | Batch effect handling |
| @sec-ch19-batch-effects | @sec-ch22-batch-effects | Batch effect handling |
| @sec-ch25-calibration | @sec-ch23-calibration | Calibration methods |
| @sec-ch14-calibration | @sec-ch23-calibration | Calibration methods |

## Appendix Reference Status

All appendix references are valid and used appropriately:

| Appendix | ID | References |
|----------|-----|-----------|
| Deep Learning Primer | @sec-apx-a-dl | Used in index |
| Compute | @sec-apx-b-compute | Used in Ch25, Ch27, Ch29 |
| Data Curation | @sec-apx-c-data-curation | Used in index |
| Model Reference | @sec-apx-d-models | Used in Ch27 |
| Resources | @sec-apx-e-resources | Used in index |
| Glossary | @sec-apx-f-glossary | Used in index |

## Recommendations

### Immediate Actions

1. **No broken references to fix** - All cross-references are valid

2. **Add cross-references per TODO notes**:
   - Ch11 → Ch20 (benchmarks)
   - Ch11 → Ch5-9 (practical usage)
   - Ch14 → Ch23 (uncertainty quantification)

### Low Priority

3. **Consider cross-referencing batch effects** - Three chapters discuss this topic:
   - Ch16 (single-cell batch effects)
   - Ch19 (multi-omics batch effects)
   - Ch22 (batch effects as confounding)

   Ch22 should be the primary reference; Ch16 and Ch19 should link to it.

4. **Consider cross-referencing calibration** - Three chapters discuss calibration:
   - Ch14 (VEP calibration)
   - Ch23 (uncertainty calibration)
   - Ch25 (clinical calibration)

   Ch23 should be primary; Ch14 and Ch25 should reference it.

## Reference Network Health

| Metric | Status |
|--------|--------|
| Broken references | None |
| Hub chapters (>25 incoming) | Ch22, Ch14, Ch13, Ch12, Ch11 |
| Isolated chapters (<5 incoming) | Ch1, Ch15 (expected) |
| Cross-part references | Strong (Parts reference each other) |
| Appendix integration | Good (all appendices referenced) |

**Overall Assessment**: Cross-reference network is healthy. No broken links. Some opportunities for additional cross-references to reduce content duplication.
