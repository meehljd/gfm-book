# Fact-Check Report: Part 2 (Architectures)

**Date:** 2026-01-19
**Chapters Reviewed:**
- Chapter 5: Tokens and Embeddings (`/root/gfm-book/part_2/p2-ch05-representations.qmd`)
- Chapter 6: Convolutional Networks (`/root/gfm-book/part_2/p2-ch06-cnn.qmd`)
- Chapter 7: Transformers and Attention (`/root/gfm-book/part_2/p2-ch07-attention.qmd`)

---

## Executive Summary

| Check Type | Ch05 | Ch06 | Ch07 | Overall |
|------------|------|------|------|---------|
| **Citation Coverage** | WARN | PASS | PASS | WARN |
| **Quantitative Claims** | WARN | WARN | WARN | WARN |
| **Historical/Attribution Claims** | PASS | PASS | PASS | PASS |
| **Technical Accuracy** | PASS | PASS | PASS | PASS |
| **Speculation as Fact** | PASS | PASS | PASS | PASS |
| **Potential Hallucinations** | WARN | PASS | WARN | WARN |

**Legend:** PASS = No significant issues; WARN = Issues found requiring attention; FAIL = Critical issues

---

## Chapter 5: Tokens and Embeddings

### Properly Cited Claims (Verified in Bibliography)

| Claim | Citation | Status |
|-------|----------|--------|
| DNABERT pioneered k-mer approach for genomic transformers in 2021 | @ji_dnabert_2021 | VERIFIED |
| DNABERT-2 articulated overlapping k-mer problems in 2024 | @zhou_dnabert-2_2024 | VERIFIED |
| HyenaDNA introduced single-nucleotide tokens in 2023 | @nguyen_hyenadna_2023 | VERIFIED |
| GenSLMs pioneered codon-level tokenization in 2022 | @zvyagin_genslms_2022 | VERIFIED |
| Life-Code extended codon-aware tokenization in 2025 | @liu_life-code_2025 | VERIFIED |
| GROVER trained BPE on human genome | @sanabria_grover_2024 | VERIFIED |
| BioToken extends tokenization to include structural annotations | @medvedev_biotoken_2025 | VERIFIED |
| Caduceus bidirectional architecture | @schiff_caduceus_2024 | VERIFIED |
| Nucleotide Transformer strand handling | @dalla-torre_nucleotide_2023 | VERIFIED |

### Unsupported Claims Requiring Citations

#### CRITICAL (Quantitative/Technical Claims)

1. **Line 95** - BPE algorithm origin claim:
   > "The algorithm, originally developed for data compression..."

   **Issue:** No citation for the original BPE paper (Gage 1994 or Sennrich et al. 2016 for NLP adaptation).
   **Severity:** CRITICAL - Historical attribution without source
   **Recommendation:** Add citation: Gage, Philip. "A New Algorithm for Data Compression." C Users Journal 12, no. 2 (1994): 23-38. Or Sennrich et al. 2016 for NLP context.

2. **Line 132** - BPE compression ratio claim:
   > "A 10 kb sequence might compress to 2,000 or 3,000 tokens depending on its repetitive structure"

   **Issue:** Specific compression ratio presented without citation.
   **Severity:** IMPORTANT - Quantitative claim needs source
   **Recommendation:** Add citation or qualify as "approximately" with reference to DNABERT-2 or NT paper for empirical compression ratios.

3. **Line 134** - DNABERT-2 efficiency claims:
   > "21 times fewer parameters and requiring approximately 92 times less GPU time"

   **Issue:** These specific numbers (21x, 92x) need verification. The citation is present but the exact numbers should be verified.
   **Severity:** IMPORTANT - Verify against source paper
   **Status:** Citation present (@zhou_dnabert-2_2024), but numbers should be double-checked

4. **Line 152-153** - Tokens per kb for BPE:
   > "BPE: 200-500 tokens per kb"

   **Issue:** This range is presented as fact without citation.
   **Severity:** MINOR - Reasonable estimate but needs source

5. **Line 176** - State space model development claim:
   > "The development of sub-quadratic architectures including Hyena, Mamba, and state space models has fundamentally changed..."

   **Issue:** Already marked as "[Citations Needed]" in text. Need citations for Hyena and Mamba.
   **Severity:** CRITICAL - Already acknowledged gap
   **Recommendation:** Add @poli_hyena_2023 and @gu_mamba_2024 (both present in bibliography)

6. **Line 241** - Embedding dimension claim:
   > "DNABERT-2's BPE tokens use 768-dimensional embeddings"

   **Issue:** Specific technical detail without citation.
   **Severity:** MINOR - Technical detail, verify against paper

7. **Line 243** - Embedding space organization claims:
   > "GC content...emerges as a major axis of variation...Repetitive elements cluster together..."

   **Issue:** These claims about learned representation structure need citation.
   **Severity:** IMPORTANT - These are empirical findings requiring source
   **Recommendation:** Cite GROVER paper or other embedding analysis work

8. **Line 267** - Circular genome handling:
   > "Some models address this through circular position encodings..."

   **Issue:** Already marked as "[Citation Needed]"
   **Severity:** IMPORTANT - Vague claim about "some models" without examples

9. **Line 296** - Vocabulary size claim:
   > "BPE vocabularies...typically ranging from 4,096 to 32,000 tokens for genomic applications"

   **Issue:** Range presented without citation.
   **Severity:** MINOR - General knowledge but should be sourced

#### IMPORTANT (Technical/Methodological Claims)

10. **Line 166** - HyenaDNA benchmark claims:
    > "On the Nucleotide Transformer benchmarks, HyenaDNA reached state-of-the-art performance on 12 of 18 datasets"
    > "On GenomicBenchmarks, it surpassed prior state-of-the-art on 7 of 8 datasets by an average of 10 accuracy points"

    **Issue:** Citation present but specific numbers (12/18, 7/8, 10 points) should be verified.
    **Severity:** IMPORTANT - Verify against @nguyen_hyenadna_2023

11. **Line 166** - Context length comparison:
    > "500-fold increase in context length over dense attention models"

    **Issue:** This specific multiplier needs verification.
    **Severity:** IMPORTANT

### Opinions/Speculation Presented as Fact

1. **Line 20-21** - Opening anecdote:
   > "In 2018, a variant effect predictor showed near-perfect performance..."

   **Issue:** This appears to be a hypothetical/illustrative scenario, not a documented case. While pedagogically effective, it could be misread as a real incident.
   **Severity:** MINOR - Clearly serves pedagogical purpose
   **Recommendation:** Consider adding "Consider a scenario where..." or citing an actual case

2. **Line 126** - Alu element claim:
   > "Alu elements...appear over one million times"

   **Issue:** This is a well-known fact but should have citation.
   **Severity:** MINOR - Common knowledge in genomics but citation would strengthen

### Potential Hallucinations

1. **Line 166** - "500-fold increase" claim:
   **Concern:** The specific "500-fold" multiplier for HyenaDNA context improvement seems suspiciously round. Needs verification.

2. **Line 134** - "92 times less GPU time":
   **Concern:** Very specific number (92x) - verify this is exact from DNABERT-2 paper, not approximated.

---

## Chapter 6: Convolutional Networks

### Properly Cited Claims (Verified in Bibliography)

| Claim | Citation | Status |
|-------|----------|--------|
| DeepSEA 2015 original paper | @zhou_deepsea_2015 | VERIFIED |
| Basset 2016 DNase prediction | @kelley_basset_2016 | VERIFIED |
| DanQ hybrid CNN-RNN | @quang_danq_2016 | VERIFIED |
| ExPecto tissue expression | @zhou_expecto_2018 | VERIFIED |
| SpliceAI predicting splicing | @jaganathan_predicting_2019 | VERIFIED |
| LSTM introduction | @hochreiter_long_1997 | VERIFIED |
| GRU properties | @cho_properties_2014 | VERIFIED |
| Enformer hybrid model | @avsec_enformer_2021 | VERIFIED |
| MaxEntScan reference | @yeo_maximum_2004 | VERIFIED |
| ENCODE/Roadmap data | @kagda_data_2025; @kundaje_integrative_2015 | VERIFIED |

### Unsupported Claims Requiring Citations

#### CRITICAL

1. **Line 101-105** - Model receptive field table:
   > "| Model | Receptive Field | What It Can Capture |"
   > "| DeepSEA | ~1,000 bp |"
   > "| SpliceAI | ~10,000 bp |"
   > "| Enformer | ~200,000 bp |"

   **Issue:** These specific receptive field values need citations or derivation.
   **Severity:** IMPORTANT - Presented as factual reference data
   **Recommendation:** Either derive mathematically or cite original papers

#### IMPORTANT

2. **Line 168-169** - DeepSEA architecture specifics:
   > "three convolutional layers with 320, 480, and 960 filters respectively"
   > "fully connected layer with 925 units"
   > "final output layer with 919 sigmoid units"

   **Issue:** These specific architectural numbers should reference the original paper.
   **Severity:** MINOR - Citation is present; these are factual details from it

3. **Line 297-299** - ExPecto correlation claim:
   > "ExPecto achieved 0.819 median Spearman correlation between predicted and observed expression"

   **Issue:** Citation present (@zhou_expecto_2018), but verify this specific number.
   **Severity:** IMPORTANT - Quantitative claim to verify

4. **Line 366** - SpliceAI performance:
   > "95% top-k accuracy for splice site identification (compared to 57% for MaxEntScan)"
   > "0.98 precision-recall area under the curve (auPRC)"

   **Issue:** Citation present (@jaganathan_predicting_2019), but verify these specific numbers.
   **Severity:** IMPORTANT - Clinical-grade claims need verification

5. **Line 393-394** - SpliceAI validation rates:
   > "approximately 50% at delta >= 0.2, 75% at delta >= 0.5, and 85% at delta >= 0.8"

   **Issue:** These specific validation rates need verification against source.
   **Severity:** IMPORTANT

6. **Line 397** - Cryptic splice mutation statistics:
   > "1.51-fold enrichment (p = 4.2 x 10^-4)"
   > "Approximately 9% of pathogenic de novo mutations in intellectual disability act through cryptic splicing"

   **Issue:** These are very specific statistics requiring verification.
   **Severity:** IMPORTANT - Clinical statistics

7. **Line 421** - Context window claims:
   > "DeepSEA's three-layer architecture effectively considers roughly 1 kb"
   > "ExPecto's Beluga component operates on 2 kb windows"

   **Issue:** Should be derived or cited.
   **Severity:** MINOR

8. **Line 468** - RNN range estimates:
   > "Vanilla RNN: ~10-50 positions practical range"
   > "LSTM/GRU: ~100-1000 positions practical range"

   **Issue:** These estimates lack citations.
   **Severity:** MINOR - General ML knowledge but should be sourced

### Opinions/Speculation Presented as Fact

1. **Lines 303-306** - Clinical case opening:
   > "A child presents with developmental delay...Three years later, research RNA sequencing identifies aberrant splicing..."

   **Issue:** Appears to be illustrative/hypothetical scenario.
   **Severity:** MINOR - Pedagogically appropriate

2. **Line 502** - DanQ adoption claim:
   > "The model saw limited adoption compared to simpler convolutional alternatives."

   **Issue:** This is an assertion about community adoption without citation.
   **Severity:** MINOR - Likely accurate but unsubstantiated

### Potential Hallucinations

**None identified.** Chapter 6 appears well-grounded in cited sources.

---

## Chapter 7: Transformers and Attention

### Properly Cited Claims (Verified in Bibliography)

| Claim | Citation | Status |
|-------|----------|--------|
| Attention mechanism (Vaswani et al.) | @vaswani_attention_2023 | VERIFIED |
| DNABERT encoder-only | @ji_dnabert_2021 | VERIFIED |
| Nucleotide Transformer architecture | @dalla-torre_nucleotide_2023 | VERIFIED |
| HyenaDNA long-range modeling | @nguyen_hyenadna_2023 | VERIFIED |
| Caduceus bidirectional | @schiff_caduceus_2024 | VERIFIED |
| Enformer hybrid | @avsec_enformer_2021 | VERIFIED |
| Borzoi | @linder_borzoi_2025 | VERIFIED |
| DNABERT-2 | @zhou_dnabert-2_2024 | VERIFIED |
| Mamba SSM | @gu_mamba_2024 | VERIFIED |
| S4 model | @gu_efficiently_2022 | VERIFIED |
| Hyena hierarchy | @poli_hyena_2023 | VERIFIED |
| Evo model | @nguyen_sequence_2024 | VERIFIED |
| Evo 2 | @brixi_evo_2025 | VERIFIED |
| GenSLM | @zvyagin_genslms_2022 | VERIFIED |
| ESM-2 | @lin_esm-2_2022 | VERIFIED |
| T5 relative position | @raffel_exploring_2023 | VERIFIED |
| ALiBi | @press_train_2022 | VERIFIED |
| RoPE/RoFormer | @su_roformer_2024 | VERIFIED |
| Pre-norm vs post-norm | @xiong_layer_2020 | VERIFIED |
| AdamW | @loshchilov_decoupled_2019 | VERIFIED |
| Scaling laws | @kaplan_scaling_2020 | VERIFIED |
| Linformer | @wang_linformer_2020 | VERIFIED |
| Performer | @choromanski_rethinking_2022 | VERIFIED |
| FlashAttention | @dao_flashattention_2022 | VERIFIED |

### Unsupported Claims Requiring Citations

#### CRITICAL

1. **Line 356-358** - Computational cost example:
   > "For a 10-kilobase sequence tokenized at single-nucleotide resolution, this means 100 million attention computations per layer. A 200-kilobase sequence requires 40 billion computations per layer."

   **Issue:** These are mathematical derivations (10k^2 = 100M, 200k^2 = 40B), which are correct but should be stated as calculations, not empirical claims.
   **Severity:** MINOR - Mathematically correct, presentation issue

2. **Line 358** - HLA region statistics:
   > "HLA region...spans approximately 4 megabases"
   > "approximately 40,000 organ transplants performed annually in the United States"

   **Issue:** These statistics need citations.
   **Severity:** IMPORTANT - Medical statistics without source
   **Recommendation:** Add CDC/UNOS citation for transplant statistics, genomics reference for HLA size

3. **Line 421-422** - Memory calculation:
   > "A 100-kilobase sequence with 16 attention heads and 12 layers requires storing...approximately 2 terabytes at 32-bit precision"

   **Issue:** This specific memory calculation should be shown as derivation or cited.
   **Severity:** MINOR - Mathematical but should show work

4. **Line 494** - Learning rate claims:
   > "genomic transformers often use peak learning rates of 1e-4 to 5e-4"
   > "somewhat lower than the 1e-3 to 3e-3 common in language modeling"

   **Issue:** These specific ranges need citation.
   **Severity:** MINOR - Practitioner knowledge but should be sourced

5. **Line 514** - Batch size example:
   > "Nucleotide Transformer's 2.5B model accumulated gradients from physical batches of just 2 sequences to reach 1 million tokens per update"

   **Issue:** Very specific claim; citation present but verify exact numbers.
   **Severity:** IMPORTANT - Verify against @dalla-torre_nucleotide_2023

#### IMPORTANT

6. **Lines 370-381** - Model comparison table:
   > Full architectural specifications for multiple models

   **Issue:** Many specific numbers (widths, depths, parameters, contexts) need verification.
   **Severity:** IMPORTANT - Table should cite sources for each row
   **Recommendation:** Add footnotes or inline citations for each model's specifications

7. **Line 382** - DNABERT architecture claim:
   > "DNABERT using the same 12-layer, 768-dimension configuration as BERT-base"

   **Issue:** Should cite BERT paper for comparison.
   **Severity:** MINOR

8. **Line 388** - HyenaDNA parameter claim:
   > "HyenaDNA achieves state-of-the-art results on 12 of 18 benchmarks from the Nucleotide Transformer suite while using 1,500 times fewer parameters"

   **Issue:** "1,500 times fewer parameters" is very specific and needs verification.
   **Severity:** IMPORTANT - Verify against source

9. **Line 396-397** - Enformer downsampling:
   > "A 200-kilobase genomic region might be compressed to roughly 1,500 positions after CNN processing"

   **Issue:** Compression ratio claim needs citation or derivation.
   **Severity:** MINOR

10. **Line 500** - Dropout rates:
    > "Genomic transformers, like DNABERT, use standard dropout rates of 0.1 to 0.2"

    **Issue:** Needs citation.
    **Severity:** MINOR

### Opinions/Speculation Presented as Fact

1. **Line 364** - Entropy claim:
   > "The entropy of DNA sequence is higher than English text, meaning more parameters may be needed to model the same sequence length."

   **Issue:** This is a theoretical claim that needs citation. DNA entropy vs. text entropy is a researchable comparison.
   **Severity:** IMPORTANT - Claims about relative entropy need source

2. **Line 508** - Gradient imbalance claim:
   > "Common k-mers receive large gradients from frequent occurrence while rare but biologically important tokens...receive small gradients"

   **Issue:** This is a mechanistic claim about training dynamics without citation.
   **Severity:** MINOR - Reasonable inference but should be cited if empirically demonstrated

### Potential Hallucinations

1. **Line 388** - "1,500 times fewer parameters":
   **Concern:** This is an extremely specific multiplier. HyenaDNA papers report ~7M parameters vs NT 2.5B would be ~357x, not 1,500x. This may be comparing to a different model or be incorrect.
   **Severity:** HIGH - Likely error
   **Recommendation:** Verify calculation. 2.5B / 7M = ~357x, not 1,500x

2. **Line 145** - SCN5A prevalence:
   > "mutations in which cause Brugada syndrome and long QT syndrome, affecting approximately 1 in 2,000 individuals"

   **Concern:** This specific prevalence (1 in 2,000) needs citation and verification. Brugada syndrome prevalence varies significantly by population (higher in Southeast Asia).
   **Severity:** IMPORTANT - Medical statistic without source

---

## Summary of All Uncited Claims by Severity

### CRITICAL (Must Fix Before Publication)

| Location | Claim | Recommendation |
|----------|-------|----------------|
| Ch05:95 | BPE algorithm origin | Add Gage 1994 or Sennrich 2016 citation |
| Ch05:176 | Hyena, Mamba, SSM development | Add @poli_hyena_2023, @gu_mamba_2024 (already in bib) |
| Ch05:267 | Circular genome handling | Provide specific model examples or remove |

### IMPORTANT (Should Fix)

| Location | Claim | Recommendation |
|----------|-------|----------------|
| Ch05:132 | BPE compression ratios | Cite DNABERT-2 or qualify with "approximately" |
| Ch05:134 | 21x/92x efficiency claims | Verify exact numbers against paper |
| Ch05:166 | HyenaDNA benchmark numbers | Verify 12/18, 7/8, 10 points, 500-fold |
| Ch05:243 | Embedding space organization | Cite GROVER or embedding analysis paper |
| Ch06:297 | ExPecto 0.819 correlation | Verify against source |
| Ch06:366 | SpliceAI 95%/0.98 numbers | Verify against source |
| Ch06:393-397 | SpliceAI validation rates | Verify against source |
| Ch07:145 | SCN5A prevalence 1:2000 | Add medical citation |
| Ch07:358 | HLA 4Mb, transplant statistics | Add citations |
| Ch07:364 | DNA entropy vs. text | Add citation or remove |
| Ch07:370-381 | Model specification table | Add citations per row |
| Ch07:388 | 1,500x parameter claim | **LIKELY ERROR** - verify/correct |

### MINOR (Consider Fixing)

| Location | Claim | Recommendation |
|----------|-------|----------------|
| Ch05:126 | Alu element count | Add genomics textbook citation |
| Ch05:152-153 | BPE tokens per kb | Cite or qualify |
| Ch05:241 | DNABERT-2 768 dimensions | Verify technical detail |
| Ch05:296 | BPE vocabulary ranges | Cite examples |
| Ch06:101-105 | Receptive field table | Derive or cite |
| Ch06:468 | RNN range estimates | Cite ML textbook |
| Ch06:502 | DanQ adoption claim | Cite or soften language |
| Ch07:494 | Learning rate ranges | Cite or soften |
| Ch07:500 | Dropout rates | Cite |

---

## Recommendations

### Immediate Actions Required

1. **Fix the likely hallucination in Ch07:388** regarding "1,500 times fewer parameters" - this calculation appears incorrect.

2. **Add the already-identified missing citations in Ch05** marked with "[Citation Needed]" - the Hyena/Mamba/SSM citations exist in the bibliography but are not referenced.

3. **Verify all quantitative claims** against their cited sources, particularly:
   - DNABERT-2 efficiency numbers (21x, 92x)
   - HyenaDNA benchmark numbers (12/18, 7/8, 500-fold)
   - SpliceAI clinical statistics

### Before Publication

1. **Add medical/epidemiological citations** for disease prevalence statistics (SCN5A, transplants).

2. **Add original source citations** for BPE algorithm (Gage 1994 or Sennrich 2016).

3. **Verify model specification table** (Ch07:370-381) entries against original papers and add per-row citations.

4. **Review opening anecdotes** in each chapter to clarify whether they are real cases or illustrative scenarios.

### Quality Patterns Observed

**Strengths:**
- Most major model claims are properly cited
- Citations generally align with bibliography entries
- Technical explanations are accurate
- Good use of "approximately" and hedging language in many places

**Weaknesses:**
- Quantitative claims sometimes lack verification markers
- Model comparison tables need better citation support
- Some very specific numbers (92x, 1,500x, 500-fold) are suspiciously round
- Medical statistics occasionally appear without sources

---

## Verification Checklist

Before marking this report complete, the following items should be verified against source papers:

- [ ] DNABERT-2: 21x fewer parameters, 92x less GPU time
- [ ] HyenaDNA: 12/18 NT benchmarks, 7/8 GenomicBenchmarks, 10 accuracy points, 500-fold context increase
- [ ] ExPecto: 0.819 median Spearman correlation
- [ ] SpliceAI: 95% top-k accuracy, 57% MaxEntScan, 0.98 auPRC
- [ ] SpliceAI: 50%/75%/85% validation rates at 0.2/0.5/0.8 thresholds
- [ ] SpliceAI: 1.51-fold enrichment, p = 4.2e-4, 9% cryptic splice
- [ ] Model table: All parameters, layers, contexts for each model
- [ ] HyenaDNA vs NT parameter ratio (claimed 1,500x - likely incorrect)

---

*Report generated by fact-checker agent. Manual verification of flagged items recommended before publication.*
