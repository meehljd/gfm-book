# Implementation Log: 2025 Papers Additions

**Date:** 2026-01-20
**Source:** `/root/gfm-book/meta/proposed-additions-2025-papers.md`
**Implemented by:** Claude Code

---

## Summary

All 7 proposed additions from the 2025 papers review have been implemented into their target chapters. Content was inserted exactly as specified in the proposed-additions document, which had been editorially approved and revised for style compliance.

---

## Changes by Chapter

### 1. p3-ch11-benchmarks.qmd

**File:** `/root/gfm-book/part_3/p3-ch11-benchmarks.qmd`

| Addition | Section Title | Section ID | Insertion Point | Lines Added |
|----------|---------------|------------|-----------------|-------------|
| Geneformer Benchmark Study | When Foundation Models Fail: The Single-Cell Reality Check | `#sec-ch11-scfm-baselines` | After @sec-ch11-cross-species (line 178), before @sec-ch11-vep-benchmarks | ~16 |
| Data Leakage Methodology | The Leakage Tax: Genomic Heterogeneity Inflates Performance | `#sec-ch11-leakage-genomic` | After @sec-ch11-splitting (line 342), before @sec-ch11-metrics | ~14 |

**Content summary:**
- Addition 1: Cautionary finding from Nature Methods 2025 study showing *Geneformer* and *scGPT* underperform linear regression on perturbation prediction tasks
- Addition 2: Methodological guidance on homology-aware splitting to prevent data leakage in genomic benchmarks

**Citations added:**
- `@rood_geneformer_benchmark_2025`
- `@data_leakage_guidelines_2025`
- `@hashfrag_2025`

---

### 2. p3-ch13-confounding.qmd

**File:** `/root/gfm-book/part_3/p3-ch13-confounding.qmd`

| Addition | Section Title | Section ID | Insertion Point | Lines Added |
|----------|---------------|------------|-----------------|-------------|
| Ancestry Bias in VEPs | (Expanded existing section) | Within @sec-ch13-addressing-ancestry-bias | After existing content on PRS portability (line 213), before Knowledge Check | ~8 |

**Content summary:**
- Documents 2025 study showing systematic ancestry-stratified performance disparities in *CADD*, *REVEL*, and *AlphaMissense*
- auROC gaps of 0.05-0.12 between European and African ancestry groups
- Establishes ancestry-stratified evaluation as methodological requirement

**Citations added:**
- `@martin_pervasive_2025`

---

### 3. p4-ch14-fm-principles.qmd

**File:** `/root/gfm-book/part_4/p4-ch14-fm-principles.qmd`

| Addition | Section Title | Section ID | Insertion Point | Lines Added |
|----------|---------------|------------|-----------------|-------------|
| Downstream Scaling Laws | Downstream Scaling: A Modified Framework | `#sec-ch14-downstream-scaling` | After @sec-ch14-empirical-scaling (line 217), before @sec-ch14-emergence | ~50 |

**Content summary:**
- Modified scaling law framework for downstream tasks vs. pretraining
- Mathematical formulation: $L_{downstream}(D_{ft}, E) = L_{irreducible} + \frac{A'}{E^{\alpha'}} + \frac{B'}{D_{ft}^{\beta'}}$
- Sample efficiency evidence: 10-100x reduction in labeled data requirements
- Zero-shot approach using likelihood ratios

**Citations added:**
- `@hernandez_transfer_2021`
- `@iclr_downstream_2025`
- `@howard_universal_2018`
- `@meier_esm-1v_2021`

---

### 4. p4-ch15-dna-lm.qmd

**File:** `/root/gfm-book/part_4/p4-ch15-dna-lm.qmd`

| Addition | Section Title | Section ID | Insertion Point | Lines Added |
|----------|---------------|------------|-----------------|-------------|
| NTv3 Architecture | Architectural Convergence: NTv3 and U-Net Hybrids | `#sec-ch15-ntv3` | After @sec-ch15-evo2 / table (line 294), before @sec-ch15-training-data | ~20 |

**Content summary:**
- U-Net + Transformer hybrid architecture enabling single-nucleotide resolution in megabase contexts
- Encoder-bottleneck-decoder design with skip connections
- Convergent evolution with *AlphaGenome*
- Positions NTv3 as successor to NT 2.5B for 2025-2027 deployment

**Citations added:**
- `@dalla-torre_nucleotide_v3_2025`

**Figures referenced:**
- `@fig-ntv3-architecture` (placeholder: `../figs/part_4/ch15/XX-fig-ntv3-architecture.svg`)

---

### 5. p5-ch20-single-cell.qmd

**File:** `/root/gfm-book/part_5/p5-ch20-single-cell.qmd`

| Addition | Section Title | Section ID | Insertion Point | Lines Added |
|----------|---------------|------------|-----------------|-------------|
| Zero-Shot Limitations | The Zero-Shot Illusion | `#sec-ch20-zero-shot-limits` | After @sec-ch20-batch-effects (line 472), before @sec-ch20-imbalance | ~10 |

**Content summary:**
- Genome Biology 2025 study showing *scGPT* and *Geneformer* underperform classical methods on zero-shot tasks
- Highly variable genes + Harmony/scVI outperforms foundation models
- Core issue: pretraining objectives do not transfer to discriminative tasks
- Links to related finding in @sec-ch11-scfm-baselines

**Citations added:**
- `@scfm_zero_shot_limitations_2025`

---

### 6. p6-ch25-interpretability.qmd

**File:** `/root/gfm-book/part_6/p6-ch25-interpretability.qmd`

| Addition | Section Title | Section ID | Insertion Point | Lines Added |
|----------|---------------|------------|-----------------|-------------|
| Attention Interpretability Framework | Systematic Attention Analysis for Genomic Transformers | `#sec-ch25-attention-genomics` | After @sec-ch25-attention-caution (line 336), before @sec-ch25-global | ~25 |

**Content summary:**
- Framework distinguishing positional, compositional, and functional attention heads
- GPT-4-assisted workflow for automated head annotation
- Validation via ISM concordance (functional heads: r > 0.7; positional/compositional: r < 0.3)
- Practical interpretability recipe

**Citations added:**
- `@attention_interpretability_2025`

---

## Totals

| Metric | Value |
|--------|-------|
| Chapters modified | 6 |
| New sections added | 7 |
| Estimated lines added | ~143 |
| Estimated words added | ~2,750 |
| New citations | 9 |
| New figures referenced | 1 (placeholder) |

---

## Issues Encountered

**None.** All insertions completed successfully. The proposed content had been pre-edited to conform to the book's style guide, so no additional formatting changes were required.

---

## Follow-up Actions Required

1. **Add citations to bibliography:** The following citation keys need to be added to `bib/references.bib`:
   - `@rood_geneformer_benchmark_2025`
   - `@data_leakage_guidelines_2025`
   - `@hashfrag_2025`
   - `@martin_pervasive_2025`
   - `@hernandez_transfer_2021`
   - `@iclr_downstream_2025`
   - `@howard_universal_2018`
   - `@meier_esm-1v_2021`
   - `@dalla-torre_nucleotide_v3_2025`
   - `@scfm_zero_shot_limitations_2025`
   - `@attention_interpretability_2025`

2. **Create placeholder figure:** `figs/part_4/ch15/XX-fig-ntv3-architecture.svg` needs to be created or renamed with proper numbering.

3. **Verify cross-references:** Run `quarto render` to verify all new cross-references resolve correctly:
   - `@sec-ch11-scfm-baselines` (new)
   - `@sec-ch11-leakage-genomic` (new)
   - `@sec-ch14-downstream-scaling` (new)
   - `@sec-ch15-ntv3` (new)
   - `@sec-ch20-zero-shot-limits` (new)
   - `@sec-ch25-attention-genomics` (new)

4. **Update chapter word counts:** Regenerate `meta/qmd_headings.md` if needed.

---

## Verification Checklist

- [x] All 7 additions implemented at specified locations
- [x] Section IDs follow `@sec-chXX-topic` format
- [x] Callouts use correct Quarto syntax (`::: {.callout-note/tip/warning}`)
- [x] Citations use `@citation_key` format
- [x] Cross-references use `@sec-chXX-topic` format
- [x] Glossary terms bolded on first use where appropriate
- [x] No AI-isms (em-dashes, "importantly", "notably") in content
- [x] Mathematical content in proper LaTeX within `$$...$$` blocks
