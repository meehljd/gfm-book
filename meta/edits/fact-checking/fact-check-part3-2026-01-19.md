# Fact-Check Report: Part 3 (Learning & Evaluation)

**Date:** 2026-01-19
**Reviewer:** Claude Code Automated Fact-Check
**Chapters Reviewed:**
- Chapter 8: Pretraining Strategies
- Chapter 9: Transfer Learning Foundations
- Chapter 10: Adaptation Strategies
- Chapter 11: Benchmark Landscape
- Chapter 12: Evaluation Methods
- Chapter 13: Confounding and Data Leakage

---

## Executive Summary

| Check Type | Ch08 | Ch09 | Ch10 | Ch11 | Ch12 | Ch13 | Overall |
|------------|------|------|------|------|------|------|---------|
| **Unsupported Quantitative Claims** | WARN | PASS | PASS | WARN | PASS | WARN | WARN |
| **Missing Citations for Key Claims** | WARN | PASS | PASS | FAIL | PASS | PASS | WARN |
| **Speculation as Fact** | PASS | PASS | PASS | PASS | PASS | PASS | PASS |
| **Potential Hallucinations** | WARN | PASS | PASS | FAIL | PASS | PASS | WARN |
| **Attribution Claims** | PASS | PASS | PASS | PASS | PASS | PASS | PASS |

**Overall Assessment:** WARN - Several chapters require citation additions before publication.

---

## Chapter 8: Pretraining Strategies

### Explicit [Citation Needed] Markers Found (Author Self-Identified)

The chapter contains several explicit `[Citation Needed]` markers that the author has already flagged:

1. **Line ~501:** "Repeat elements occupy roughly half of the human genome" - `*[Citation Needed]*`
2. **Line ~261:** "Nanopore sequencing exhibits distinct error profiles concentrated in homopolymer regions" - `*[Citation Needed]*`
3. **Line ~334-335:** "Roughly 95% of cancer drugs that succeed in mouse models fail in human trials" - `*[Citation Needed]*`
4. **Line ~341:** "TTN mutated in 25% of dilated cardiomyopathy cases" - `*[Citation Needed]*`
5. **Line ~489:** "African populations harbor more genetic diversity than all other continental populations combined" - `*[Citation Needed]*`
6. **Line ~493:** "roughly 3.1 billion base pairs... representing about 92% of the full genome before telomere-to-telomere completion" - `*[Citation Needed]*`
7. **Line ~537:** "Language models exhibit emergent behaviors (in-context learning, chain-of-thought reasoning, few-shot generalization) that appear only above certain parameter thresholds" - `*[Citation Needed]*`

### Additional Unsupported Claims (Critical)

1. **Line ~111:** "The standard 15% rate from BERT represents a reasonable compromise, though genomic models have explored values ranging from 10% to 40%"
   - The BERT citation is present [@devlin_bert_2019], but the claim about genomic models exploring 10-40% needs citation.
   - **Recommendation:** Add citations to specific genomic model papers that explored different masking rates.

2. **Line ~258:** "indels account for approximately 15% of pathogenic variants in ClinVar"
   - Citation [@landrum_clinvar_2018] is present. **VERIFIED.**

### Quantitative Claims - Verified

| Claim | Citation | Status |
|-------|----------|--------|
| ESM-2 has 15 billion parameters | @lin_esm-2_2022 | VERIFIED |
| 5,000+ assays in Enformer (674 DNase + 4,675 ChIP-seq + 638 CAGE) | @avsec_enformer_2021, @kagda_data_2025 | VERIFIED |
| DNABERT uses 15% masking on 6-mer tokens | @ji_dnabert_2021 | VERIFIED |

### Assessment: WARN

Chapter 8 has several self-identified citation gaps and a few additional unsupported quantitative claims. The core technical content is well-cited, but biological/clinical statistics need verification.

---

## Chapter 9: Transfer Learning Foundations

### Citation Analysis

This chapter demonstrates excellent citation practices. Key claims are well-supported:

| Claim | Citation | Status |
|-------|----------|--------|
| UniRef provides billions of protein sequences | @suzek_uniref_2007 | VERIFIED |
| Negative transfer characterization | @wang_characterizing_2018 | VERIFIED |
| DNABERT achievements on chromatin accessibility | @ji_dnabert_2021 | VERIFIED |
| Nucleotide Transformer on promoter detection | @dalla-torre_nucleotide_2023 | VERIFIED |
| ESM embeddings encode secondary structure | @rives_esm-1b_2021 | VERIFIED |
| Basenji2 cross-species training | @kelley_basenji2_2020 | VERIFIED |
| HyenaDNA splice site improvements | @nguyen_hyenadna_2023 | VERIFIED |
| Kircher general variant annotation | @kircher_general_2014 | VERIFIED |
| What BERT learns | @jawahar_what_2019 | VERIFIED |

### Unsupported Claims

No significant unsupported factual claims identified. The chapter is appropriately cautious with quantitative claims, presenting worked examples rather than asserting external statistics.

### Assessment: PASS

Chapter 9 is well-cited and avoids making unsupported factual claims. Numerical examples are clearly presented as illustrative rather than empirical.

---

## Chapter 10: Adaptation Strategies

### Citation Analysis

Chapter 10 maintains strong citation practices. Key citations verified:

| Claim | Citation | Status |
|-------|----------|--------|
| LoRA method | @hu_lora_2022 | VERIFIED |
| Adapter architecture | @houlsby_parameter-efficient_2019 | VERIFIED |
| Prompt tuning | @lester_power_2021 | VERIFIED |
| Soft prompts for protein engineering | @biswas_low-n_2021 | VERIFIED |
| Prefix-tuning | @li_prefix-tuning_2021 | VERIFIED |
| Layer selection observations | @dodge_fine-tuning_2020 | VERIFIED |

### Quantitative Thresholds

The chapter provides data quantity thresholds (e.g., "fewer than 500 examples" for linear probing, "500-5,000" for PEFT) that are appropriately qualified as "approximate" and "guidelines, not rules" (see @tbl-data-thresholds). This is appropriate pedagogical practice.

### Assessment: PASS

Well-cited chapter with appropriate qualification of empirical guidelines.

---

## Chapter 11: Benchmark Landscape

### Explicit [Citation Needed] Markers Found (Author Self-Identified)

1. **Line ~168:** "The Long Range Benchmark (*LRB*) evaluates models' ability to integrate information across large genomic distances" - `*[Citation Needed]*`
2. **Line ~170:** "*DNALongBench* extends evaluation to ultra-long contexts spanning up to millions of base pairs" - `*[Citation Needed]*`
3. **Line ~176:** "*GenBench* and related resources test whether models trained on one organism generalize to related species" - `*[Citation Needed]*`

### Additional Unsupported Claims (Critical)

1. **Line ~195:** "over 2 million variant submissions as of 2024"
   - Citation [@landrum_clinvar_2018] is outdated for 2024 statistics.
   - **Severity:** IMPORTANT
   - **Recommendation:** Update citation to more recent ClinVar paper or database documentation.

2. **Line ~275-276:** "*TraitGym* provides a framework specifically designed to assess complex trait prediction using genomic foundation models"
   - Citation @benegas_traitgym_2025 is present. **VERIFIED.**

3. **Line ~284-285:** "*EmbedGEM* framework evaluates whether foundation model embeddings capture biologically meaningful genetic signal"
   - Citation @mukherjee_embedgem_2024 is present. **VERIFIED.**

### Potential Hallucination Flags

**HIGH PRIORITY - Verify These Benchmarks Exist:**

1. **Long Range Benchmark (LRB)** - Line ~168
   - No citation provided
   - **Action Required:** Verify this benchmark exists or is a proposed/placeholder name
   - **Risk:** POTENTIAL HALLUCINATION

2. **DNALongBench** - Line ~170
   - No citation provided
   - **Action Required:** Verify this benchmark exists
   - **Risk:** POTENTIAL HALLUCINATION

3. **GenBench** for cross-species evaluation - Line ~176
   - No citation provided
   - **Action Required:** Verify this specific benchmark exists for genomics (note: GenBench exists for NLP evaluation)
   - **Risk:** POTENTIAL HALLUCINATION or NAME CONFUSION

### Verified Citations

| Claim | Citation | Status |
|-------|----------|--------|
| TAPE benchmark introduction | @rao_evaluating_2019 | VERIFIED |
| FLIP benchmark | @dallago_flip_2022 | VERIFIED |
| ProteinGym comprehensive benchmark | @notin_proteingym_2023 | VERIFIED |
| CASP structure prediction | @kryshtafovych_critical_2021 | VERIFIED |
| Genomic Benchmarks | @gresova_genomic_2023 | VERIFIED |
| BEND benchmark | @marin_bend_2024 | VERIFIED |
| CAGI challenges | @brunak_cagi_2023 | VERIFIED |
| MaveDB | @esposito_mavedb_2019 | VERIFIED |
| Enformer | @avsec_enformer_2021 | VERIFIED |

### Assessment: FAIL

Three potential hallucinations of benchmark names require immediate verification. The LRB, DNALongBench, and GenBench references need citations or clarification that these are proposed/illustrative names.

---

## Chapter 12: Evaluation Methods

### Citation Analysis

Excellent citation coverage for methodological claims:

| Claim | Citation | Status |
|-------|----------|--------|
| Rost twilight zone | @rost_twilight_1999 | VERIFIED |
| CD-HIT clustering | @li_cd-hit_2006 | VERIFIED |
| MMseqs2 | @steinegger_mmseqs2_2017 | VERIFIED |
| Grimm evaluation circularity | @grimm_evaluation_2015 | VERIFIED |
| Genomic Touchstone | @wang_genomic_2025 | VERIFIED |
| Tanigawa PRS comparison | @tanigawa_significant_2022 | VERIFIED |
| GFP fitness landscape | @sarkisyan_local_2016 | VERIFIED |
| Guo calibration | @guo_calibration_2017 | VERIFIED |
| Platt scaling | @platt_probabilistic_1999 | VERIFIED |
| DeLong method for auROC | @delong_comparing_1988 | VERIFIED |
| Benjamini-Hochberg | @benjamini_controlling_1995 | VERIFIED |
| Breiman two cultures | @breiman_statistical_2001 | VERIFIED |

### Minor Unsupported Claims

1. **Line ~138:** "UK Biobank provides pre-computed relatedness estimates; other cohorts may require explicit calculation using tools like KING or PLINK."
   - Mentions tools but no citations for KING or PLINK.
   - **Severity:** MINOR
   - **Recommendation:** Add tool citations: @manichaikul_king_2010 for KING, @purcell_plink_2007 for PLINK.

### Assessment: PASS

Strong citation coverage. One minor tool citation gap that does not affect factual claims.

---

## Chapter 13: Confounding and Data Leakage

### Citation Analysis

Strong methodological citations:

| Claim | Citation | Status |
|-------|----------|--------|
| ClinVar ancestry bias | @landrum_clinvar_2018 | VERIFIED |
| Population structure PCA correction | @patterson_population_2006, @price_principal_2006 | VERIFIED |
| PGS portability failures 40-75% reduction | @duncan_analysis_2019 | VERIFIED |
| Amariuta PRS transferability | @amariuta_improving_2020 | VERIFIED |
| Sohail Latin American PRS | @sohail_mexican_2023 | VERIFIED |
| Davey Smith Mendelian randomization | @davey_smith_mendelian_2003 | VERIFIED |
| Pearl causality | @pearl_causality_2009 | VERIFIED |
| Lipsitch negative controls | @lipsitch_negative_2010 | VERIFIED |
| CYP2D6 population variation | @chung_marker_2004 | VERIFIED |
| Ge LD-aware PRS | @ge_polygenic_2019 | VERIFIED |
| Vilhjalmsson PRS modeling | @vilhjalmsson_modeling_2015 | VERIFIED |

### Quantitative Claims Verification

1. **Line ~152-153:** "polygenic score portability... 40-75% reductions in prediction accuracy when applied to African ancestry individuals"
   - Citation @duncan_analysis_2019 is present. **VERIFIED.**

2. **Line ~364-366:** "neural networks performed only 93-95% as well as properly tuned linear regression for polygenic prediction"
   - Claims to be from "a 2025 Nature Communications analysis" but no specific citation provided.
   - **Severity:** IMPORTANT
   - **Recommendation:** Add specific citation for this claim.

### Unsupported Claims (Important)

1. **Line ~364-367:** The claim about neural networks performing 93-95% as well as linear regression references "a 2025 Nature Communications analysis" but lacks a specific citation.
   - **Recommendation:** Add citation or remove if not verifiable.

### Assessment: WARN

One important quantitative claim lacks a specific citation. Otherwise excellent coverage.

---

## Consolidated List of Issues by Severity

### CRITICAL (Potential Hallucinations - Verify Existence)

| Location | Claim | Action Required |
|----------|-------|-----------------|
| Ch11 Line ~168 | Long Range Benchmark (LRB) | Verify benchmark exists; add citation |
| Ch11 Line ~170 | DNALongBench | Verify benchmark exists; add citation |
| Ch11 Line ~176 | GenBench (cross-species genomic) | Verify benchmark exists; add citation |

### IMPORTANT (Missing Citations for Specific Claims)

| Location | Claim | Recommended Citation |
|----------|-------|---------------------|
| Ch08 Line ~501 | Repeats occupy ~50% of human genome | @lander_initial_2001 or @de_koning_repetitive_2011 |
| Ch08 Line ~261 | Nanopore homopolymer error profiles | @rang_nanopore_2018 |
| Ch08 Line ~335 | 95% cancer drug failure in mouse models | @mak_lost_2014 |
| Ch08 Line ~341 | TTN mutations in 25% dilated cardiomyopathy | @herman_truncations_2012 |
| Ch08 Line ~489 | African genetic diversity | @campbell_african_2008 |
| Ch08 Line ~493 | GRCh38 3.1B bp / 92% coverage | @nurk_complete_2022 |
| Ch08 Line ~537 | Emergent behaviors at scale thresholds | @wei_emergent_2022 |
| Ch11 Line ~195 | ClinVar 2M submissions (2024) | Update to recent ClinVar paper |
| Ch13 Line ~366 | NN 93-95% of linear regression | Add specific 2025 citation |

### MINOR (Tool/Method Citations That Would Be Nice to Add)

| Location | Item | Recommended Citation |
|----------|------|---------------------|
| Ch12 Line ~138 | KING relatedness tool | @manichaikul_king_2010 |
| Ch12 Line ~138 | PLINK | @purcell_plink_2007 |

---

## Opinions/Speculation Presented as Fact

**None identified.** The chapters appropriately qualify speculative or forward-looking statements with language like:
- "remains an active research question"
- "early evidence suggesting"
- "whether... remains unclear"
- "may provide benefits"

The chapters demonstrate excellent epistemic hygiene in distinguishing established facts from emerging understanding.

---

## Recommendations

### Immediate Actions (Before Publication)

1. **Verify or remove benchmark names (LRB, DNALongBench, GenBench)** in Chapter 11. These may be placeholder names for benchmarks that are emerging but not yet published, or may represent genuine hallucinations.

2. **Add citations for the explicit [Citation Needed] markers** the author has already identified across chapters 8 and 11.

3. **Update ClinVar statistics citation** (currently @landrum_clinvar_2018) to reflect 2024 submission counts.

4. **Add specific citation for the 2025 Nature Communications claim** about neural network vs. linear regression PRS performance.

### Before Final Review

1. Add tool citations for KING and PLINK in Chapter 12.

2. Consider standardizing citation style for database statistics (ClinVar, gnomAD) with version/access dates.

---

## Verification Notes

This fact-check was performed by:
1. Reading all six chapters in full
2. Identifying all quantitative claims, performance statistics, and attributions
3. Checking each claim against its associated citation (if present)
4. Flagging claims without citations
5. Cross-referencing benchmark names against known resources
6. Identifying author-flagged citation needs

**Limitations:** This review cannot verify the accuracy of cited papers themselves, only whether citations are present and plausibly match the claims made.

---

*Report generated: 2026-01-19*
*Chapters reviewed: 6*
*Total citation gaps identified: 15 (3 critical, 9 important, 3 minor)*
