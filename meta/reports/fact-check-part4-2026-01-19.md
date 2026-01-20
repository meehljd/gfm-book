# Fact-Check Report: Part 4 (Foundation Model Families)

**Generated:** 2026-01-19
**Chapters Reviewed:**
- Chapter 14: Foundation Model Paradigm (`p4-ch14-fm-principles.qmd`)
- Chapter 15: DNA Language Models (`p4-ch15-dna-lm.qmd`)
- Chapter 16: Protein Language Models (`p4-ch16-protein-lm.qmd`)
- Chapter 17: Regulatory Models (`p4-ch17-regulatory.qmd`)
- Chapter 18: Variant Effect Prediction (`p4-ch18-vep-fm.qmd`)

---

## Executive Summary

| Check Type | Status | Count |
|------------|--------|-------|
| **Critical Claims Without Citation** | WARN | 15 |
| **Important Claims Without Citation** | WARN | 28 |
| **Minor Claims Without Citation** | INFO | 12 |
| **Opinions/Speculation as Fact** | PASS | 2 |
| **Potential Hallucinations** | WARN | 8 |

**Overall Assessment:** The chapters are generally well-cited with appropriate references to primary literature. However, several specific numerical claims (model performance metrics, parameter counts, training data sizes) lack citations and should be verified against primary sources or marked as approximate. The chapters marked as `[Citation Needed]` in the text indicate awareness of citation gaps.

---

## Chapter-by-Chapter Analysis

### Chapter 14: Foundation Model Paradigm

**Well-Cited Claims:**
- Chinchilla scaling laws (@hoffmann_training_2022)
- Foundation model definition (@bommasani_opportunities_2022)
- CADD and classical VEP approaches (@rentzsch_cadd_2019; @schubach_cadd_2024)
- DeepSEA, ExPecto, Enformer, SpliceAI references properly cited
- Emergent capabilities framework (@wei_emergent_2022)

**Claims Requiring Verification:**

| Claim | Line | Severity | Issue |
|-------|------|----------|-------|
| "Scaling exponents alpha and beta both approximate 0.3" | ~151 | Important | Claim is stated without direct citation to Chinchilla paper page/figure |
| "20 tokens per parameter for compute-optimal training" | ~167 | Important | Rule of thumb - should cite source |
| "Reference genomes for well-studied species total perhaps 10^11 to 10^12 nucleotides" | ~208 | Important | No citation for genome size estimates |
| "Training compute scaled from approximately 10^19 to 10^21 FLOPs across the model family" (NT) | ~194 | Important | Specific compute claims need verification against NT paper |
| "Structural understanding emerges at approximately 650 million parameters" (ESM-2) | ~225 | Important | Specific threshold claim needs citation |
| "ESM-1v computes log-likelihood ratios to predict protein variant pathogenicity" | ~227 | Minor | Incomplete citation for ESM-1v |
| Training cost estimates ($10^{20}-10^{22}$ FLOPs, "tens of thousands of dollars") | ~408-411 | Minor | These are approximations that should be noted as such |

**Potential Issues:**
- The opening vignette about a family with cardiac arrhythmia syndrome is a constructed scenario - appropriately framed as illustrative but should be clearly noted as hypothetical.

---

### Chapter 15: DNA Language Models

**Well-Cited Claims:**
- DNABERT (@ji_dnabert_2021)
- DNABERT-2 (@zhou_dnabert-2_2024)
- Nucleotide Transformer (@dalla-torre_nucleotide_2023)
- HyenaDNA (@nguyen_hyenadna_2023)
- Caduceus (@schiff_caduceus_2024)
- Evo (@nguyen_sequence_2024)
- Evo 2 (@brixi_evo_2025)
- GPN (@benegas_gpn_2023)
- GROVER (@sanabria_grover_2024)
- BEND benchmark (@marin_bend_2024)
- Genomic Benchmarks (@gresova_genomic_2023)
- DNALongBench (@cheng_dnalongbench_2024)

**Claims Requiring Verification:**

| Claim | Line | Severity | Issue |
|-------|------|----------|-------|
| "DNABERT used overlapping k-mers (typically 6-mers) as tokens, creating a vocabulary of 4,096 tokens" | ~113 | Minor | 4^6 = 4,096 is mathematically correct, but original tokenization details should be verified |
| "Context windows were limited to 512 tokens" (DNABERT) | ~115 | Important | Should cite specific architectural details |
| "HyenaDNA processes sequences up to 1 Mb" | ~204 | Important | Verify maximum context length against paper |
| "HyenaDNA achieved state-of-the-art results on the majority of tasks" | ~210 | Important | Vague claim - which benchmarks specifically? |
| "Evo 2 training corpus draws from OpenGenome2 dataset comprising 9.3 trillion DNA tokens" | ~252 | Critical | Very specific number needs verification |
| "30-fold increase over original Evo training data" | ~252 | Important | Relative comparison needs verification |
| "7 billion and 40 billion parameter variants" (Evo 2) | ~252 | Critical | Specific parameter counts need verification |
| "Evo was trained on 2.7 million prokaryotic and phage genomes comprising 300 billion nucleotides" | ~238 | Critical | Specific numbers need verification against original paper |
| Model comparison table (parameters: DNABERT 110M, NT 500M-2.5B, HyenaDNA 1.6M-6.6M, Caduceus 1.6M-6.6M, Evo 2 7B-40B) | ~284-292 | Critical | All specific parameter counts should be verified against primary sources |
| "GPN outperformed traditional conservation scores including phyloP and phastCons" | ~178 | Important | Performance comparison needs specific citation |

**Notable Gaps:**
- The chapter mentions Life-Code and BioToken but citations are provided (@liu_life-code_2025; @medvedev_biotoken_2025) - VERIFY these are real papers
- gLM citation (@cornman_glm_2024) - VERIFY this is a real paper

---

### Chapter 16: Protein Language Models

**Well-Cited Claims:**
- ESM-1b (@rives_esm-1b_2021)
- ESM-2 (@lin_esm-2_2022)
- ProtTrans (@elnaggar_prottrans_2021)
- UniRef clustering (@suzek_uniref_2007)
- EVE (@frazer_eve_2021)
- AlphaMissense (@cheng_alphamissense_2023)
- ESM-1v (@meier_esm-1v_2021)
- AlphaFold2 (@jumper_alphafold2_2021)
- AlphaFold3 (@abramson_alphafold3_2024)
- RoseTTAFold (@baek_accurate_2021)
- OpenFold (@ahdritz_openfold_2024)
- Direct Coupling Analysis (@morcos_direct-coupling_2011)
- Attention-contact prediction (@rao_transformer_2020)

**Claims Requiring Verification:**

| Claim | Line | Severity | Issue |
|-------|------|----------|-------|
| "ESM-1b was trained on UniRef50, approximately 33 million protein sequences" | ~70 | Important | Verify exact number |
| "650 million parameters distributed across 33 layers, hidden dimension of 1,280, and 20 attention heads" (ESM-1b) | ~72 | Critical | Specific architectural details need verification |
| "Maximum sequence length of 1,024 amino acids" (ESM-1b) | ~72 | Important | Verify this limit |
| ESM-2 model family table (8M to 15B parameters, layers 6-48, hidden dims 320-5120) | ~126-133 | Critical | All specific numbers need verification |
| "ESMFold approximately 60-fold faster than AlphaFold2" | ~208 | Important | Speed comparison needs citation |
| "ESMFold achieves atomic-level accuracy for many proteins, though slightly below AlphaFold2" | ~210 | Important | Vague claim - needs specific metrics |
| Brandes et al. "450 million possible missense variants in the human genome" | ~335 | Important | Citation provided (@brandes_genome-wide_2023) but number should be verified |
| "AlphaMissense provides predictions for all approximately 71 million possible single amino acid substitutions" | ~337 | Critical | Specific number needs verification |
| "AlphaFold2 won 2024 Nobel Prize in Chemistry" | ~245 | Important | Historical claim - verify date and prize specifics |
| PoET reference (@jr_poet_2023) | ~174 | Minor | Verify this is the correct citation format |

**Potential Issues:**
- The chapter discusses ESM3 but defers detailed treatment to another chapter - verify ESM3 citation (@hayes_esm-3_2025) is real

---

### Chapter 17: Regulatory Models

**Well-Cited Claims:**
- Enformer (@avsec_enformer_2021)
- Borzoi (@linder_borzoi_2025)
- Sei (@chen_deepsea_2022)
- AlphaGenome (@avsec_alphagenome_2025)
- Basenji2 context (@kelley_basset_2016) - Note: Citation is for Basset, not Basenji2
- Enhancer-promoter distance studies (@gasperini_genome-wide_2019)
- GWAS variant localization (@maurano_systematic_2012)

**Claims Requiring Verification:**

| Claim | Line | Severity | Issue |
|-------|------|----------|-------|
| "Median enhancer-promoter distances in many tissues span 20 to 50 kilobases, with substantial fractions exceeding 100 kilobases" | ~38 | Important | Verify against Gasperini citation |
| "TADs range from hundreds of kilobases to several megabases" | ~38 | Important | Standard knowledge but could use citation |
| "200 kilobase input has been compressed to roughly 1,500 tokens, each representing approximately 128 base pairs" (Enformer) | ~87 | Critical | Specific architectural details need verification |
| "~5,000 output tracks" (Enformer) | ~108 | Important | Approximate number should be verified |
| "AlphaGenome extends to approximately 1Mb" context | ~305 | Important | Verify exact context length |
| "Sei predicts 40 sequence classes" | ~262-263 | Important | Verify exact number of classes |
| ChromHMM reference missing | ~260 | Minor | Claims "Previous methods like ChromHMM" without citation |

**Explicit [Citation Needed] Markers:**
- Line ~113: "Human training data derives largely from ENCODE and Roadmap Epigenomics consortia... *[Citation Needed]*"

**Potential Issues:**
- Borzoi citation (@linder_borzoi_2025) - should verify this is published
- AlphaGenome citation (@avsec_alphagenome_2025) - should verify this is published

---

### Chapter 18: Variant Effect Prediction

**Well-Cited Claims:**
- ESM-1v methodology (@meier_esm-1v_2021)
- EVE (@frazer_eve_2021)
- popEVE (@orenbuch_popeve_2025)
- Tranception (@notin_tranception_2022)
- AlphaMissense (@cheng_alphamissense_2023)
- SpliceAI (@jaganathan_predicting_2019)
- Enformer VEP (@avsec_enformer_2021)
- GPN-MSA (@benegas_gpn-msa_2024)
- Evo 2 (@brixi_evo_2025)
- ACMG guidelines (@richards_standards_2015)
- Calibration framework (@tavtigian_modeling_2018)
- Calibration studies (@pejaver_calibration_2022; @bergquist_calibration_2025)
- VEP evaluation pitfalls (@dey_evaluating_2020)
- PLM-VEP limitations (@karollus_current_2023; @swanson_predicting_2022)
- Long-read sequencing review (@logsdon_long-read_2020)
- Structural variant detection (@smolka_detection_2024)
- PEPPER-Margin-DeepVariant (@zheng_symphonizing_2022)
- REVEL (@ioannidis_revel_2016)
- Primate constraint (@gao_landscape_2023)
- Cross-species transfer (@jagota_cross_2023)
- ClinVar ancestry bias (@landrum_clinvar_2018)

**Explicit [Citation Needed] Markers Found:**
- Line ~82: "Missense variants account for approximately half of known pathogenic variants in ClinVar *[Citation Needed]*"
- Line ~204: "AlphaMissense achieves correlations of 0.5 to 0.7... compared to 0.3 to 0.5 for CADD or PolyPhen-2 *[Citation Needed]*"
- Line ~204: "AlphaMissense achieves auROC values above 0.9... compared to 0.85 to 0.88 typical of classical methods *[Citation Needed]*"
- Line ~223: "Approximately 98% of the human genome lies outside protein-coding regions *[Citation Needed]*"
- Line ~227: "Approximately 10% of pathogenic variants in ClinVar act through splicing mechanisms *[Citation Needed]*"
- Line ~509: "AlphaMissense achieves auROC of 0.91 on held-out ClinVar missense variants compared to 0.85 for CADD *[Citation Needed]*"
- Line ~509: "SpliceAI detects pathogenic splicing variants with sensitivity of 0.90 compared to 0.60 for MaxEntScan *[Citation Needed]*"
- Line ~509: "GPN-MSA scores correlate more strongly with deep mutational scanning measurements than phyloP or GERP *[Citation Needed]*"
- Line ~647: "SCN5A variants cause distinct cardiac arrhythmia syndromes *[Citation Needed]*"

**Claims Requiring Verification:**

| Claim | Line | Severity | Issue |
|-------|------|----------|-------|
| "GWAS variants: approximately 90% fall in non-coding regions, roughly 60% in enhancer-like chromatin states" | ~239 | Important | @farh_genetic_2015 citation provided but verify numbers |
| "SpliceAI processes 10,000 nucleotides of context through 32 residual blocks" | ~229 | Critical | Verify architectural specifics against paper |
| "Scores exceeding 0.2 correlate with experimentally validated splicing changes; scores above 0.5 have high specificity" | ~231 | Critical | Performance thresholds need verification |
| "ACMG thresholds: >2.08 for supporting, >4.33 for moderate, >18.7 for strong" | ~426 | Critical | Odds ratio thresholds need verification against Tavtigian |
| "AlphaMissense, ESM1b, and VARITY all reach Strong evidence for pathogenicity and Moderate for benignity" | ~431 | Important | Verify against Bergquist 2025 |

---

## Opinions/Speculation Presented as Facts

| Statement | Chapter | Line | Assessment |
|-----------|---------|------|------------|
| "Foundation models promise a different approach" | Ch14 | ~27 | Appropriately framed as promise, not fact |
| "This might seem fanciful" | Ch15 | ~32 | Appropriately framed as hypothetical |

**Assessment:** The chapters generally maintain appropriate epistemic hedging, using phrases like "suggests," "may," "potentially," and "remains unclear" for uncertain claims. The authors are careful to distinguish empirical findings from speculation.

---

## Potential Hallucinations / Fabricated Claims

The following claims could not be readily verified or appear suspiciously specific without citation:

| Claim | Chapter | Assessment | Recommendation |
|-------|---------|------------|----------------|
| "9.3 trillion DNA tokens" (Evo 2 training data) | Ch15 | Very specific number | Verify against Brixi et al. 2025 |
| "300 billion nucleotides" (Evo training data) | Ch15 | Very specific number | Verify against Nguyen et al. 2024 |
| "17,000-fold reduction in memory requirements" (Enformer compression) | Ch17 | Calculated claim | Mathematical derivation appears correct (200,000^2 / 1,500^2) but should be verified |
| "450 million possible missense variants" | Ch16/18 | Very specific number | Verify calculation methodology |
| "71 million possible single amino acid substitutions" | Ch16/18 | Very specific number | Verify against AlphaMissense paper |
| "60-fold faster" (ESMFold vs AlphaFold2) | Ch16 | Specific speedup | Verify against Lin et al. 2022 |
| "617 million proteins" (ESM Metagenomic Atlas) | Ch16 | Very specific number | Verify source |
| UniRef50 "50% identity threshold" clustering rationale | Ch16 | Biological claim about fold similarity | Well-established but could use citation |

---

## Citation Verification Needed

The following citations appear in the text but should be verified as actual published works:

| Citation | Chapter | Status |
|----------|---------|--------|
| @brixi_evo_2025 | Ch15, Ch18 | Verify - may be preprint |
| @linder_borzoi_2025 | Ch17 | Verify - may be preprint |
| @avsec_alphagenome_2025 | Ch17, Ch18 | Verify - may be preprint |
| @hayes_esm-3_2025 | Ch16 | Verify - may be preprint |
| @orenbuch_popeve_2025 | Ch18 | Verify - may be preprint |
| @bergquist_calibration_2025 | Ch18 | Verify - may be preprint |
| @liu_life-code_2025 | Ch15 | Verify - may be preprint |
| @medvedev_biotoken_2025 | Ch15 | Verify - may be preprint |
| @li_omni-dna_2025 | Ch14 | Verify - may be preprint |
| @cornman_glm_2024 | Ch15 | Verify |
| @jr_poet_2023 | Ch16 | Verify citation format |

---

## Recommendations

### Critical (Address Before Publication)

1. **Verify all model parameter counts and training data sizes** - The specific numbers for Evo 2 (7B/40B parameters, 9.3 trillion tokens), ESM-2 family sizes, Nucleotide Transformer variants, and HyenaDNA/Caduceus parameters should be checked against primary sources.

2. **Add citations for explicit [Citation Needed] markers** - The authors have appropriately flagged 9+ specific claims needing citations. These should be addressed.

3. **Verify 2025 citations exist** - Several citations reference 2025 publications. Given the book's publication timeline, verify these are available (may be preprints that need updating to final publication info).

4. **Verify performance claims** - AlphaMissense auROC, SpliceAI sensitivity/specificity thresholds, and comparative performance numbers should have explicit citations.

### Important

5. **Add citations for scaling law specifics** - The Chinchilla "20 tokens per parameter" rule and specific exponent values should cite the relevant figure/table in Hoffmann et al.

6. **Cite architectural details** - Specific layer counts, hidden dimensions, and context lengths for major models should cite the original papers.

7. **Clarify approximations** - Where numbers are approximations (e.g., "roughly 10^11 to 10^12 nucleotides"), explicitly note them as estimates.

8. **Add ChromHMM citation** - Chapter 17 mentions ChromHMM without citation.

9. **Verify Basenji2 citation** - The citation @kelley_basset_2016 is for Basset, not Basenji2.

### Minor

10. **Check mathematical derivations** - The 17,000-fold memory reduction calculation and similar mathematical claims should be verified.

11. **Nobel Prize verification** - Verify the 2024 Nobel Prize in Chemistry details for AlphaFold2.

12. **Standardize uncertainty language** - Consider adding systematic uncertainty indicators for approximate numbers.

---

## Summary Statistics

| Category | Chapter 14 | Chapter 15 | Chapter 16 | Chapter 17 | Chapter 18 |
|----------|------------|------------|------------|------------|------------|
| Total Citations | ~25 | ~20 | ~22 | ~12 | ~35 |
| Claims Needing Citation | 7 | 10 | 8 | 7 | 15+ |
| Explicit [Citation Needed] | 0 | 0 | 0 | 1 | 9 |
| Potential Hallucinations | 1 | 3 | 2 | 1 | 1 |

**Note:** Chapter 18 is commendable for explicitly marking claims needing citation with `[Citation Needed]` tags, making gaps visible for later correction. This practice should be applied to other chapters.

---

*Report generated by fact-checker agent review. Manual verification of cited sources against primary literature recommended before publication.*
