# Fact-Check Report: Part 5 (Cellular Context)

**Date:** 2026-01-19
**Chapters Reviewed:** Ch19 (RNA), Ch20 (Single-Cell), Ch21 (3D Genome), Ch22 (Networks), Ch23 (Multi-Omics)
**Reviewer:** Claude Code (Automated Fact-Check)

---

## Executive Summary

| Check Type | Ch19 | Ch20 | Ch21 | Ch22 | Ch23 |
|------------|------|------|------|------|------|
| Unsupported Quantitative Claims | WARN | WARN | WARN | PASS | WARN |
| Missing Citations for Key Claims | WARN | WARN | WARN | PASS | WARN |
| Opinions Presented as Facts | PASS | PASS | PASS | PASS | PASS |
| Potential Hallucinations | WARN | WARN | WARN | PASS | PASS |

**Overall Assessment:** Part 5 has moderate citation coverage but several chapters contain specific quantitative claims and attribution claims that require citations. The most concerning gaps are around specific statistics (PDB structure counts, dropout rates, dataset sizes) that need verification.

---

## Chapter 19: RNA Structure and Function

### Critical Issues (Require Immediate Attention)

1. **PDB Structure Counts** (Lines 116-117, 213, 460)
   - Claim: "The Protein Data Bank contains over 200,000 protein structures but fewer than 2,000 RNA structures"
   - Status: **[Citation Needed]** - This specific quantitative claim is repeated multiple times and requires a citation to PDB statistics or a review paper.
   - Severity: **Critical** - These numbers underpin a central argument of the chapter.

2. **Algorithmic Complexity Claims** (Line 102)
   - Claim: "Standard dynamic programming approaches for secondary structure prediction exclude pseudoknots because their inclusion increases computational complexity from O(n^3) to O(n^6) or worse"
   - Status: **[Citation Needed]** - This algorithmic claim should cite the original computational biology literature.
   - Severity: **Critical** - Foundational to understanding the challenge.

### Important Issues (Should Be Addressed)

3. **Mfold and ViennaRNA** (Line 127)
   - Claim: "*Mfold* and the *ViennaRNA* package represent the most widely used implementations"
   - Status: **[Citation Needed]** - Should cite Zuker (Mfold) and Lorenz et al. (ViennaRNA).
   - Severity: **Important**

4. **RNAErnie Claims** (Line 220)
   - Claim: "*RNAErnie* and related models experiment with multi-task objectives..."
   - Status: **[Citation Needed]** - Should cite the RNAErnie paper.
   - Severity: **Important**

5. **UTR Borrowing Practice** (Line 340)
   - Claim: "Current mRNA therapeutics typically use UTRs borrowed from highly expressed endogenous genes (human alpha-globin and beta-globin UTRs are common choices)"
   - Status: **[Citation Needed]** - Industry practice claim needs citation.
   - Severity: **Important**

6. **COVID-19 Vaccine Design** (Lines 372-373)
   - Claim about vaccine design elements (N1-methylpseudouridine, codon optimization, etc.)
   - Status: **[Citation Needed]** - Should cite Kariko et al. or vaccine development papers.
   - Severity: **Important**

7. **miRNA Target Validation Rates** (Line 431)
   - Claim: "Experimental validation rates for top predictions rarely exceed 50%"
   - Status: **[Citation Needed]** - Quantitative claim about validation rates.
   - Severity: **Important**

### Minor Issues

8. **Pangolin Model** (Line 447)
   - Claim about tissue-specific splicing model
   - Status: **[Citation Needed]** - Model attribution.
   - Severity: **Minor**

---

## Chapter 20: Single-Cell Models

### Critical Issues

1. **scRNA-seq Introduction Date** (Line 45)
   - Claim: "The technology has evolved rapidly since its introduction in 2009"
   - Status: **[Citation Needed]** - Should cite Tang et al. 2009 or the original method paper.
   - Severity: **Critical** - Historical attribution claim.

2. **Current Dataset Scales** (Line 45)
   - Claim: "current platforms routinely profile hundreds of thousands of cells, with some studies exceeding a million"
   - Status: **[Citation Needed]** - Should cite specific studies or cell atlas projects.
   - Severity: **Critical** - Quantitative claim about field state.

### Important Issues

3. **Dropout Rates** (Lines 81-82)
   - Claim: "A gene with true expression may appear as zero in 50% to 90% of cells where it is actually transcribed"
   - Status: **[Citation Needed]** - Specific quantitative range needs citation.
   - Severity: **Important**

4. **Environmental Exposure and Methylation** (Line 355)
   - Claim: "Environmental exposures including diet, smoking, and stress leave lasting methylation signatures that persist long after the exposure ends"
   - Status: **[Citation Needed]** - Should cite epigenetic epidemiology literature.
   - Severity: **Important**

---

## Chapter 21: 3D Genome Organization

### Critical Issues

1. **Hi-C Technical Details** (Line 135)
   - Claim: "Hi-C extends this principle genome-wide by incorporating biotinylated nucleotides at ligation junctions"
   - Status: **[Citation Needed]** - Should cite Lieberman-Aiden et al. 2009 or method paper.
   - Severity: **Critical**

2. **ICE Normalization** (Line 135)
   - Claim: "The ICE (iterative correction and eigenvector decomposition) method and related approaches remove these technical artifacts"
   - Status: **[Citation Needed]** - Should cite Imakaev et al. 2012.
   - Severity: **Critical**

### Important Issues

3. **Micro-C Method** (Line 157)
   - Claim: "Micro-C achieves nucleosome-level resolution by using micrococcal nuclease instead of restriction enzymes"
   - Status: **[Citation Needed]** - Should cite Hsieh et al. method paper.
   - Severity: **Important**

4. **Single-Cell Hi-C Contact Rates** (Line 157)
   - Claim: "any two loci contact each other in only 5 to 15 percent of cells"
   - Status: **[Citation Needed]** - Specific quantitative range.
   - Severity: **Important**

5. **LINE/Alu Compartment Association** (Line 236)
   - Claim: "LINE elements with B compartment; Alu elements with A compartment"
   - Status: **[Citation Needed]** - Should cite studies on repeat element distribution.
   - Severity: **Important**

6. **Cancer Structural Variants** (Line 269)
   - Claim: "Similar mechanisms operate in cancer, where structural variants create novel enhancer-oncogene contacts that drive tumor growth"
   - Status: **[Citation Needed]** - Should cite oncology literature.
   - Severity: **Important**

7. **Activity-by-Contact Framework** (Line 283)
   - Claim about expression proportional to enhancer activity weighted by contact frequency
   - Status: **[Citation Needed]** - Should cite Fulco et al. or ABC model paper.
   - Severity: **Important**

8. **TAD Disruption Minimal Effects** (Lines 287, 370)
   - Claims about cohesin degradation and TAD boundary deletion having limited expression effects
   - Status: **[Citation Needed]** - Should cite Rao et al. 2017 or perturbation studies.
   - Severity: **Important**

### Minor Issues

9. **Spatial Transcriptomics Technologies** (Lines 300, 316, 320-321)
   - Multiple claims about MERFISH, Stereo-seq, Nicheformer, SpaGCN, CellPLM, STACI, GraphST
   - Status: **[Citation Needed]** for each
   - Severity: **Minor** - Individual method citations

10. **Tumor Immunotherapy Response** (Line 336)
    - Claim: "tumors with immune cells infiltrating the tumor core respond better to immunotherapy than those with immune exclusion at the tumor periphery"
    - Status: **[Citation Needed]** - Clinical oncology claim.
    - Severity: **Minor**

---

## Chapter 22: Graph and Network Models

### Assessment: PASS

This chapter has excellent citation coverage. Key databases (STRING, BioGRID, IntAct, Hetionet, PrimeKG, DisGeNET) are properly cited. GNN architecture papers (GCN, GraphSAGE, GAT) are appropriately referenced. No critical unsupported claims identified.

### Minor Issues

1. **PPI Coverage Estimate** (Line 46)
   - Claim: "current estimates suggest only 20-30% of human PPIs are catalogued"
   - Status: Has citations [@szklarczyk_string_2023; @venkatesan_empirical_2008; @hart_how_2006]
   - Assessment: **PASS** - Properly cited

---

## Chapter 23: Multi-Omics Integration

### Important Issues

1. **GWAS Heritability Explained** (Line 43)
   - Claim: "Genome-wide association studies explain perhaps 10-20% of heritability for most common diseases through identified variants"
   - Status: **[Citation Needed]** - Should cite missing heritability literature.
   - Severity: **Important**

2. **MOFA+ Extensions** (Line 178)
   - Claim: "*MOFA+* extends this framework to handle multiple sample groups..."
   - Status: **[Citation Needed]** - Should cite Argelaguet et al. MOFA+ paper.
   - Severity: **Important**

3. **totalVI Method** (Line 187)
   - Claim: "*totalVI* integrates protein abundance from CITE-seq with gene expression..."
   - Status: **[Citation Needed]** - Should cite Gayoso et al.
   - Severity: **Important**

4. **MultiVI Method** (Line 191)
   - Claim: "*MultiVI* extends this framework to integrate gene expression with chromatin accessibility"
   - Status: **[Citation Needed]** - Should cite method paper.
   - Severity: **Important**

5. **CLIP Model Reference** (Line 218)
   - Claim: "The *CLIP* model for vision-language demonstrated that contrastive objectives can align embeddings"
   - Status: **[Citation Needed]** - Should cite Radford et al.
   - Severity: **Important**

6. **Radiogenomics Claims** (Lines 268-269)
   - Claims about glioblastoma imaging-methylation associations and lung cancer radiomic-mutational correlations
   - Status: **[Citation Needed]** - Should cite radiogenomics studies.
   - Severity: **Important**

7. **Medical Imaging Foundation Models** (Line 271)
   - Claim: "Foundation models for medical imaging, pretrained on millions of scans through self-supervised objectives"
   - Status: **[Citation Needed]** - Should cite specific models (e.g., SAM, MedSAM).
   - Severity: **Important**

---

## Opinions/Speculation Presented as Facts

### Assessment: Generally Well-Handled

The chapters appropriately hedge speculative content with phrases like:
- "may" / "might" / "could"
- "The emerging view is..."
- "remains an open question"
- "Whether [X] remains unclear"

**Examples of Good Practice:**
- Ch19 Line 476: "No comparable RNA breakthrough has occurred"
- Ch20 Line 325: "whether those patterns reflect causal regulatory relationships, or merely correlations useful for prediction, remains open"
- Ch21 Line 287: "the causality question complicates interpretation"
- Ch23 Line 57: "Naive concatenation of features often performs worse than single-modality models"

No significant instances of opinions stated as facts were identified.

---

## Potential Hallucinations Flagged

### High Concern

1. **RNA-FM Training Data** (Ch19, Line 196)
   - Claim: "RNA-FM trained on approximately 23 million noncoding RNA sequences from RNAcentral"
   - Concern: This specific number should be verified against the actual paper.
   - **Recommendation:** Verify against Chen et al. 2022 citation.

2. **TranscriptFormer Scale** (Ch20, Line 262)
   - Claim: "training on over 112 million cells spanning 1.5 billion years of evolution across 12 species"
   - Concern: Very specific numbers that should be verified.
   - **Recommendation:** Verify against Pearce et al. 2025 citation.

### Moderate Concern

3. **scGPT Training Scale** (Ch20, Line 238)
   - Claim: "trained on over 33 million cells"
   - Concern: Should verify against paper.
   - Has citation [@cui_scgpt_2024] - verify number matches.

4. **scFoundation Scale** (Ch20, Line 253)
   - Claim: "training on over 50 million cells"
   - Has citation [@hao_large-scale_2024] - verify number matches.

5. **CpGPT Training Data** (Ch20, Line 359)
   - Claim: "pretrained on over 1,500 DNA methylation datasets encompassing more than 100,000 samples"
   - Has citation [@camillo_cpgpt_2024] - verify numbers match.

6. **Hetionet Statistics** (Ch22, Line 54)
   - Claim: "47,031 nodes across 11 types... with 2.25 million edges spanning 24 relationship types"
   - Has citation [@himmelstein_systematic_2017] - verify numbers match.

### Low Concern (Likely Accurate but Verify)

7. **Akita Correlation** (Ch21, Line 182)
   - Claim: "achieves correlation coefficients of 0.6 to 0.8 between predicted and observed contact maps"
   - Should verify against Fudenberg et al. 2020.

---

## Summary of Citations Needed

### By Priority

**Critical (Must Add):**
1. PDB structure counts (200,000 protein vs 2,000 RNA)
2. Pseudoknot complexity O(n^3) to O(n^6)
3. scRNA-seq 2009 introduction
4. Hi-C method and ICE normalization

**Important (Should Add):**
1. Mfold/ViennaRNA citations
2. COVID-19 vaccine design elements
3. Dropout rates in scRNA-seq
4. Environmental epigenetic persistence
5. GWAS heritability percentages
6. totalVI, MultiVI, CLIP method papers
7. Radiogenomics studies
8. Various spatial transcriptomics methods

**Minor (Nice to Have):**
1. Pangolin model
2. Individual spatial FM methods
3. Tumor immunotherapy response patterns

---

## Recommendations

### Immediate Actions

1. **Add PDB citation**: Add citation for RNA/protein structure statistics, possibly Berman et al. or PDB statistics page.

2. **Add computational complexity citation**: Cite Rivas & Eddy 1999 or similar for pseudoknot complexity analysis.

3. **Add scRNA-seq history citation**: Cite Tang et al. 2009 for introduction of the technology.

4. **Add Hi-C method citations**: Cite Lieberman-Aiden et al. 2009 for Hi-C and Imakaev et al. 2012 for ICE.

### Medium-Term Actions

5. **Verify quantitative claims**: Cross-check all specific numbers (training set sizes, correlation coefficients, coverage percentages) against cited papers.

6. **Add method citations**: Several methods are mentioned without citations (RNAErnie, Pangolin, various spatial models). Add appropriate references.

7. **Add clinical practice citations**: Claims about mRNA therapeutic design practices and clinical outcomes need supporting references.

### Quality Assurance

8. **Run citation verification**: For all cited papers with specific statistics, verify the numbers in the text match what the papers report.

9. **Consider meta-review citation**: For broad claims like "heritability explained" or "dropout rates," consider citing review papers that survey multiple studies.

---

## Appendix: Complete List of [Citation Needed] Markers

| Chapter | Line | Claim Summary |
|---------|------|---------------|
| Ch19 | 102 | Pseudoknot complexity O(n^6) |
| Ch19 | 116-117 | PDB structure counts |
| Ch19 | 127 | Mfold/ViennaRNA implementations |
| Ch19 | 220 | RNAErnie multi-task objectives |
| Ch19 | 340 | UTR borrowing in therapeutics |
| Ch19 | 372-373 | COVID-19 vaccine design |
| Ch19 | 431 | miRNA validation rates |
| Ch19 | 447 | Pangolin tissue-specific splicing |
| Ch19 | 460 | PDB structure counts (repeat) |
| Ch20 | 45 | scRNA-seq 2009 introduction |
| Ch20 | 45 | Dataset scale claims |
| Ch20 | 81-82 | Dropout rate percentages |
| Ch20 | 355 | Environmental methylation effects |
| Ch21 | 135 | Hi-C biotinylation method |
| Ch21 | 135 | ICE normalization method |
| Ch21 | 157 | Micro-C method |
| Ch21 | 157 | Single-cell Hi-C contact rates |
| Ch21 | 236 | LINE/Alu compartment distribution |
| Ch21 | 269 | Cancer structural variants |
| Ch21 | 283 | Activity-by-contact framework |
| Ch21 | 287 | TAD disruption effects |
| Ch21 | 300 | MERFISH spatial method |
| Ch21 | 300 | Stereo-seq method |
| Ch21 | 316 | Gene detection rates <10% |
| Ch21 | 320 | Nicheformer model |
| Ch21 | 320 | SpaGCN model |
| Ch21 | 321 | CellPLM model |
| Ch21 | 321 | STACI model |
| Ch21 | 321 | GraphST model |
| Ch21 | 336 | Immunotherapy response patterns |
| Ch21 | 370 | TAD boundary deletion effects |
| Ch23 | 43 | GWAS heritability 10-20% |
| Ch23 | 178 | MOFA+ extensions |
| Ch23 | 187 | totalVI method |
| Ch23 | 191 | MultiVI method |
| Ch23 | 218 | CLIP vision-language model |
| Ch23 | 268 | Glioblastoma radiogenomics |
| Ch23 | 268 | Lung cancer radiomics |
| Ch23 | 271 | Medical imaging FMs |

---

*Report generated by automated fact-checking process. All flagged items should be reviewed by a human editor for final determination.*
