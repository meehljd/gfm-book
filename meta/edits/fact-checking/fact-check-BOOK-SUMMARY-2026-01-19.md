# Fact-Check Summary Report: Genomic Foundation Models (Complete Book)

**Generated:** 2026-01-19
**Scope:** All 32 chapters + 6 appendices
**Purpose:** Ensure factual grounding, identify speculation presented as fact, detect potential hallucinations

---

## Executive Summary

| Part | Chapters | Overall Status | Critical Issues | Important Issues |
|------|----------|----------------|-----------------|------------------|
| Part 1 | Ch 1-4 (Data Foundations) | **PASS** | 1 | 6 |
| Part 2 | Ch 5-7 (Architectures) | **WARN** | 3 | 12 |
| Part 3 | Ch 8-13 (Learning & Evaluation) | **WARN** | 3 | 9 |
| Part 4 | Ch 14-18 (FM Families) | **WARN** | 15 | 28 |
| Part 5 | Ch 19-23 (Cellular Context) | **WARN** | 4 | 20+ |
| Part 6 | Ch 24-27 (Responsible Deployment) | **WARN** | 0 | 5 |
| Part 7 | Ch 28-32 (Applications) | **WARN** | 6 | 9 |
| Appendices | A-F | **WARN** | 3 | 20 |

**Book-Wide Assessment:** The book demonstrates generally strong citation practices with no evidence of systematic hallucination. However, there are approximately **35 critical issues** and **100+ important issues** that should be addressed before publication.

---

## Key Findings

### 1. Strengths

- **Excellent citation coverage** for foundational concepts, methods, and primary model papers
- **Appropriate epistemic hedging** - speculation is generally marked with "may," "might," "suggests"
- **No systematic hallucinations detected** - all specific claims appear grounded in literature
- **Self-identification of gaps** - many chapters contain explicit `[Citation Needed]` markers showing author awareness
- **Historical attributions are accurate** - first author, pioneering claims are correctly attributed

### 2. Critical Issues Requiring Immediate Attention

#### A. Potential Hallucinations (Verify or Remove)

| Location | Claim | Concern |
|----------|-------|---------|
| Part 2, Ch07 | "1,500 times fewer parameters" (HyenaDNA vs NT) | Calculation appears incorrect (should be ~357x) |
| Part 3, Ch11 | Long Range Benchmark (LRB), DNALongBench, GenBench | May not exist as named - verify or clarify |
| Part 4 | Evo 2 "9.3 trillion tokens", "7B/40B parameters" | Very specific - verify against paper |
| Part 7, Ch30 | Metformin "1.8 hops" network distance | Suspiciously specific without citation |
| Part 7, Ch32 | Geisinger "847 VUS reclassified" | Very specific - cite or mark illustrative |

#### B. Author-Identified [Citation Needed] Markers

The following count of explicit `[Citation Needed]` tags exist in the text:

| Part | Count | Status |
|------|-------|--------|
| Part 2 | 3 | Must resolve |
| Part 3 | 4 | Must resolve |
| Part 4 | 10+ | Must resolve |
| Part 5 | 30+ | Must resolve |
| Part 6 | 5 | Must resolve |
| Part 7 | 15 | Must resolve |

**Total: ~67 explicit [Citation Needed] markers to address**

#### C. Missing Canonical Citations

| Claim | Appears In | Recommended Citation |
|-------|------------|---------------------|
| BPE algorithm origin | Ch05 | Gage 1994 or Sennrich et al. 2016 |
| 2x genetic validation success | Ch30 | Nelson et al. 2015 Nature Genetics |
| Hi-C method | Ch21 | Lieberman-Aiden et al. 2009 |
| scRNA-seq introduction | Ch20 | Tang et al. 2009 |
| BRCA penetrance (45-85%) | Ch27 | Kuchenbaecker et al. 2017 JAMA |
| PRS portability (40-75% reduction) | Multiple | Martin et al. 2019 Nature Genetics |

### 3. Quantitative Claims Without Citations

The most common issue across the book is specific quantitative claims lacking citations:

- **Model specifications** (parameter counts, layer counts, context lengths)
- **Benchmark results** (auROC, accuracy, correlation values)
- **Database statistics** (sample sizes, variant counts)
- **Training data sizes** (tokens, sequences, samples)
- **Cost/compute estimates** (GPU hours, pricing)

### 4. Opinions/Speculation as Fact

**Assessment: Generally Well-Handled**

The book appropriately hedges speculative content. Only minor instances identified:
- Ch32 (Frontiers): Some predictions could use additional hedging
- Appendix A: Flat minima generalization claims are debated research findings

---

## Issues by Category

### Category 1: Missing Citations for Specific Numbers

| Type | Count | Examples |
|------|-------|----------|
| Model parameters | ~25 | ESM-2 15B, NT 2.5B, Evo 2 40B |
| Benchmark results | ~20 | auROC values, correlation coefficients |
| Database sizes | ~15 | gnomAD 730K, ClinVar 2M, UniRef sizes |
| Training data | ~10 | Token counts, sequence counts |
| Performance comparisons | ~15 | "X outperforms Y by Z%" |

### Category 2: Outdated Statistics

| Claim | Current Citation | Issue |
|-------|-----------------|-------|
| ClinVar VUS counts | Landrum 2018 | 6+ years old; numbers changed significantly |
| FDA AI devices (500+) | FDA 2025 | Rapidly changing; verify current |
| Database sizes | Various | Should include access date |

### Category 3: Preprint Citations Needing Verification

| Citation Key | Concern |
|--------------|---------|
| @brixi_evo_2025 | Verify published status |
| @linder_borzoi_2025 | Verify published status |
| @avsec_alphagenome_2025 | Verify published status |
| @hayes_esm-3_2025 | Verify published status |
| @liu_life-code_2025 | Verify published status |

---

## Recommendations

### Priority 1: Critical (Before Publication)

1. **Resolve the potential hallucination in Ch07** regarding HyenaDNA "1,500x fewer parameters"

2. **Verify benchmark names** in Ch11 (LRB, DNALongBench, GenBench) exist or clarify as proposed/emerging

3. **Add citations for all 67+ explicit [Citation Needed] markers**

4. **Verify all 2025 citations** are published (not abandoned preprints)

5. **Add the canonical "2x genetic validation" citation** (Nelson et al. 2015) - this underlies the drug discovery chapter

### Priority 2: Important (Should Address)

1. **Add database version stamps** and access dates to all statistics

2. **Verify model specification tables** against primary papers

3. **Add BRCA penetrance citation** (Kuchenbaecker et al. 2017)

4. **Add Hi-C and scRNA-seq founding citations**

5. **Update ClinVar statistics** to reflect 2024-2025 data

6. **Clarify case studies** as illustrative vs. real data (especially Ch32)

### Priority 3: Minor (Recommended)

1. Add hedging to flat minima/generalization claims in Appendix A/B

2. Add footnotes for theoretical vs. empirical speedup claims

3. Periodically verify URLs in Appendix E

4. Complete TODO items in Glossary (Appendix F)

---

## Chapter-by-Chapter Quick Reference

### Part 1: Data Foundations
- **Ch01 (NGS):** Add DeepVariant benchmark citation (line 510-511)
- **Ch02 (Data):** Update PDB structure count, verify timing claims
- **Ch03 (GWAS):** Minor SNP-heritability citation gap
- **Ch04 (VEP):** Minor variant count citation gap

### Part 2: Architectures
- **Ch05 (Representations):** Add BPE origin citation, fix SSM citations
- **Ch06 (CNN):** Verify SpliceAI performance numbers
- **Ch07 (Attention):** FIX "1,500x parameter" error, add HLA/SCN5A citations

### Part 3: Learning & Evaluation
- **Ch08 (Pretraining):** Resolve 7 explicit [Citation Needed] markers
- **Ch09 (Transfer):** PASS - well cited
- **Ch10 (Adaptation):** PASS - appropriate guidelines
- **Ch11 (Benchmarks):** CRITICAL - verify LRB/DNALongBench/GenBench exist
- **Ch12 (Evaluation):** Add KING/PLINK tool citations
- **Ch13 (Confounding):** Add 2025 Nature Comms citation

### Part 4: FM Families
- **Ch14 (Principles):** Add scaling law specifics citations
- **Ch15 (DNA-LM):** Verify Evo 2 training data numbers
- **Ch16 (Protein-LM):** Verify ESM-2 table, check Nobel Prize date
- **Ch17 (Regulatory):** Add ChromHMM citation, verify Borzoi/AlphaGenome
- **Ch18 (VEP-FM):** Resolve 9 explicit [Citation Needed] markers

### Part 5: Cellular Context
- **Ch19 (RNA):** Add PDB structure counts, complexity citations
- **Ch20 (Single-Cell):** Add 2009 scRNA-seq citation, dropout rates
- **Ch21 (3D Genome):** Add Hi-C, ICE, Micro-C method citations
- **Ch22 (Networks):** PASS - excellent citation coverage
- **Ch23 (Multi-Omics):** Add MOFA+, totalVI, CLIP citations

### Part 6: Responsible Deployment
- **Ch24 (Uncertainty):** Update ClinVar statistics, add temperature range citation
- **Ch25 (Interpretability):** Resolve 5 explicit [Citation Needed] markers
- **Ch26 (Causal):** PASS - comprehensive citations
- **Ch27 (Regulatory):** Add BRCA penetrance, PRS portability citations

### Part 7: Applications
- **Ch28 (Clinical Risk):** Resolve 4 [Citation Needed] markers
- **Ch29 (Rare Disease):** Minor ACMG guideline citation
- **Ch30 (Drug Discovery):** Add Nelson 2015, verify metformin network claim
- **Ch31 (Design):** Resolve 7 [Citation Needed] markers
- **Ch32 (Frontiers):** Clarify case studies as illustrative, verify Geisinger numbers

### Appendices
- **App A (DL Primer):** Fix Vaswani citation date (2017 not 2023)
- **App B (Compute):** Add hardware/pricing sources and dates
- **App C (Data Curation):** Add database versions and access dates
- **App D (Models):** Fix RoseTTAFold citation (not AlphaFold2)
- **App E (Resources):** Add access dates to URLs
- **App F (Glossary):** Complete TODO items

---

## Statistics

| Metric | Count |
|--------|-------|
| Chapters reviewed | 32 + 6 appendices |
| Critical issues | ~35 |
| Important issues | ~100 |
| Minor issues | ~50 |
| Explicit [Citation Needed] markers | ~67 |
| Potential hallucinations flagged | 5-8 |
| Opinions as fact | <10 (minor) |
| Parts passing with no changes | 0 |
| Parts passing with minor changes | Part 1 |

---

## Conclusion

The book demonstrates strong scholarly practice overall, with comprehensive citation coverage for foundational concepts and appropriate epistemic humility for uncertain claims. The primary issues are:

1. **Specific quantitative claims without citations** - particularly model specs and benchmark results
2. **Self-identified gaps** - 67+ [Citation Needed] markers need resolution
3. **A few potential calculation errors** - particularly the HyenaDNA parameter comparison
4. **Some unverified benchmark names** - need confirmation they exist as described

With attention to these issues, the book will maintain high factual integrity suitable for publication.

---

*Report compiled from 8 individual fact-check reports covering all book content.*
*Individual reports available in `/root/gfm-book/meta/reports/fact-check-part*-2026-01-19.md`*
