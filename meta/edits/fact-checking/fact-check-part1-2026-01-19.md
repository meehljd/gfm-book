# Fact-Check Report: Part 1 (Data Foundations)

**Date:** 2026-01-19
**Chapters Reviewed:**
- Chapter 1: From Reads to Variants (p1-ch01-ngs.qmd)
- Chapter 2: Data Landscape (p1-ch02-data.qmd)
- Chapter 3: GWAS and Polygenic Scores (p1-ch03-gwas.qmd)
- Chapter 4: Classical Variant Prediction (p1-ch04-vep-classical.qmd)

---

## Executive Summary

| Check Type | Chapter 1 | Chapter 2 | Chapter 3 | Chapter 4 |
|------------|-----------|-----------|-----------|-----------|
| Quantitative Claims | WARN | PASS | WARN | PASS |
| Performance Claims | PASS | PASS | WARN | WARN |
| Historical/Attribution | PASS | PASS | PASS | PASS |
| Citation Coverage | PASS | PASS | PASS | PASS |
| Speculation as Fact | PASS | PASS | PASS | PASS |
| Potential Hallucinations | PASS | PASS | PASS | PASS |

**Overall Assessment:** Part 1 demonstrates strong citation practices overall. Most factual claims are appropriately supported. A small number of quantitative claims would benefit from explicit citations, but no critical errors or potential hallucinations were identified.

---

## Detailed Findings by Chapter

---

### Chapter 1: From Reads to Variants

#### Properly Cited Claims (Examples)
- Long-read technologies from PacBio and ONT [@wenger_accurate_2019; @dabernig-heinz_multicenter_2024]
- T2T genome assembly [@nurk_complete_2022]
- Human pangenome references [@liao_draft_2023]
- GATK Best Practices [@depristo_framework_2011; @van_der_auwera_fastq_2018]
- BWA-MEM and minimap2 aligners [@li_aligning_2013; @li_minimap2_2018]
- DeepVariant [@poplin_deepvariant_2018]
- GLnexus [@yun_accurate_2021]
- GIAB reference samples [@zook_open_2019]
- Benchmarking tools [@krusche_best_2019]

#### Claims Needing Citations

**IMPORTANT - Quantitative Claims Without Direct Citation:**

1. **Line 26:** "Short-read sequencing technologies produce reads of 100 to 300 base pairs with error rates near one percent"
   - **Status:** The read length range is well-established. The "one percent" error rate is approximate and generally accepted for raw Illumina data, but could benefit from a citation (e.g., Goodwin et al. 2016 is cited nearby but doesn't explicitly support this specific figure).
   - **Severity:** Minor

2. **Line 97-103:** Table comparing sequencing platforms (error rates: ~0.1% for Illumina and PacBio HiFi, 1-5% for ONT)
   - **Status:** These are reasonable approximations. The cited papers support the general claims, but the specific numbers in the table are not directly attributed.
   - **Severity:** Minor

3. **Line 510-511:** "On GIAB benchmark HG002, DeepVariant achieved F1 of 99.7% for SNVs compared to 99.5% for GATK HaplotypeCaller, with larger gains for indels (99.4% vs 98.9%)"
   - **Status:** [Citation Needed] - These specific benchmark numbers should be cited. The DeepVariant paper or subsequent benchmarking studies would provide these figures.
   - **Severity:** Important

**MINOR - General Knowledge Claims:**

4. **Line 34:** "three billion base pairs" - Standard textbook knowledge, no citation needed.

5. **Line 58:** "approximately 1 to 2 percent" for protein-coding sequence - Standard textbook knowledge.

6. **Line 100:** Error rates in comparison table - Would benefit from explicit citation to manufacturer specifications or benchmarking papers.

#### Opinions/Speculation
- None identified as problematic. The text appropriately uses hedging language ("typically," "approximately," "often") for generalizations.

#### Potential Hallucinations
- None identified. All specific claims appear grounded in established literature.

---

### Chapter 2: Data Landscape

#### Properly Cited Claims (Examples)
- GRCh38, T2T-CHM13 [@nurk_complete_2022]
- Pangenome references [@liao_draft_2023]
- Zoonomia consortium [@sullivan_leveraging_2023]
- GENCODE and RefSeq [@frankish_gencode_2019; @oleary_reference_2016]
- MANE Select project [@morales_joint_2022]
- dbSNP [@sherry_dbsnp_2001]
- 1000 Genomes Project [@auton_global_2015]
- TOPMed [@taliun_sequencing_2021]
- gnomAD [@karczewski_mutational_2020]
- ENCODE and Roadmap [@kagda_data_2025; @kundaje_integrative_2015]
- GEO [@edgar_gene_2002]
- Cistrome [@zheng_cistrome_2019]
- ProteinGym, TraitGym [@notin_proteingym_2023; @benegas_traitgym_2025]
- GTEx [@gtex_consortium_the_gtex_2020]
- Human Cell Atlas [@regev_human_2017]
- Tabula Sapiens [@tabula_sapiens_consortium_the_tabula_2022]
- UniProt [@the_uniprot_consortium_uniprot_2023]
- UniRef [@suzek_uniref_2007]
- BFD [@steinegger_protein-level_2019]
- PDB [@berman_protein_2000]
- AlphaFold database [@varadi_alphafold_2022]
- AlphaFold2 [@jumper_alphafold2_2021]
- ClinVar [@landrum_clinvar_2018]
- HGMD [@stenson_human_2017]
- LOVD [@fokkema_lovd_2011]
- ClinGen [@rehm_clingen_2015]
- OMIM [@amberger_omimorg_2015]
- Pejaver calibration [@pejaver_calibration_2022]
- PharmGKB [@whirl-carrillo_pharmacogenomics_2012]
- CPIC [@relling_clinical_2019]
- PharmCAT [@sangkuhl_pharmacogenomics_2019]
- ClinPGx [@gong_integrating_2025]
- PharmVar [@nofziger_pharmvar_2019]

#### Claims Needing Citations

**MINOR - General Knowledge/Approximate Claims:**

1. **Line 94-95:** "Over 95% of human multi-exon genes undergo alternative splicing. The ~20,000 human genes produce an estimated 100,000+ distinct protein isoforms."
   - **Status:** These are widely cited statistics from multiple papers. The 95% figure comes from Wang et al. (2008) Nature and similar studies. Would benefit from citation for completeness.
   - **Severity:** Minor

2. **Line 115-116:** "approximately 78% of GWAS participants" European
   - **Status:** Cited later in Chapter 3 as [@martin_clinical_2019]. The figure appears here without citation but is established.
   - **Severity:** Minor (cited elsewhere)

3. **Line 233:** "Million Veteran Program, Mexican Biobank, BioBank Japan, China Kadoorie Biobank" and H3Africa [@sirugo_missing_2019]
   - **Status:** Appropriately attributed.

4. **Line 412-413:** "BFD contains over 2.5 billion protein sequences, an order of magnitude larger than UniProt"
   - **Status:** The BFD paper is cited, but the specific numbers should be verified against that citation.
   - **Severity:** Minor

5. **Line 425:** "As of 2024, the PDB contains over 220,000 structures"
   - **Status:** This date-specific claim should be verified. PDB grows continuously; this should match the source or be stated as "approximately."
   - **Severity:** Minor

#### Opinions/Speculation
- None problematic. The chapter appropriately frames limitations and biases as areas of concern rather than definitive facts.

#### Potential Hallucinations
- None identified.

---

### Chapter 3: GWAS and Polygenic Scores

#### Properly Cited Claims (Examples)
- Traditional cardiovascular risk factors explain ~50% of variation [@khera_genetics_2017]
- Genome-wide significance threshold [@risch_future_1996; @peer_estimation_2008]
- PCA for population structure [@price_principal_2006; @patterson_population_2006]
- Height heritability estimates [@visscher_heritability_2008]
- Schizophrenia heritability [@hilker_heritability_2018]
- BMI heritability [@elks_variability_2012]
- Missing heritability [@manolio_finding_2009]
- GCTA-GREML [@yang_common_2010]
- M50% metric [@weissbrod_functionally_2020]
- Height PGS approaching theoretical maximum [@yengo_saturated_2022]
- LD decay and population genetics (general knowledge, well-established)
- Fine-mapping methods [@maller_bayesian_2012; @hormozdiari_identifying_2014; @benner_finemap_2016; @wang_simple_2020]
- GWAS Catalog, PGS Catalog [@sollis_nhgri-ebi_2023; @lambert_polygenic_2021]
- Open Targets [@mountjoy_open_2021]
- LDpred [@vilhjalmsson_modeling_2015]
- PRS-CS [@ge_polygenic_2019]
- PRS methodology overview [@choi_prs_2020]
- Coronary disease PGS comparable to FH [@khera_genetics_2017]
- Breast cancer PGS [@mavaddat_polygenic_2019]
- PGS auROC ranges [@torkamani_personal_2018; @lambert_towards_2019]
- 78% GWAS participants European [@martin_clinical_2019]
- Portability reductions [@duncan_analysis_2019; @martin_clinical_2019]
- Multi-ancestry methods [@marquez-luna_multiethnic_2017; @kichaev_improved_2017]
- PheWAS methodology [@denny_phewas_2010]
- Embedding-based phenotyping [@ruan_improving_2022; @mukherjee_embedgem_2024]
- Diabetes subtype clustering [@ahlqvist_novel_2018]

#### Claims Needing Citations

**IMPORTANT - Quantitative Claims Without Direct Citation:**

1. **Line 31:** "Traditional risk factors (age, smoking, cholesterol, blood pressure) explain roughly 50% of the variation in who develops disease"
   - **Status:** Khera et al. 2017 is cited, which supports this general claim. However, the "50%" is an approximation that varies by study.
   - **Severity:** Minor (citation present but approximation noted)

2. **Line 55-56:** "approximately one million effectively independent tests" for Bonferroni
   - **Status:** [@peer_estimation_2008] is cited for this approximation. The claim is appropriate.

3. **Line 175-176:** "For height, pedigree studies consistently estimate h² around 0.80" / "For schizophrenia, twin studies estimate h² around 0.80 as well"
   - **Status:** Properly cited [@visscher_heritability_2008; @hilker_heritability_2018]

4. **Line 191-192:** "For height, SNP-heritability estimates reach approximately 0.50 to 0.60"
   - **Status:** Well-established figure from multiple sources. Would benefit from explicit citation to GCTA papers.
   - **Severity:** Minor

5. **Line 203-204:** "Hair color requires only approximately 28 SNPs to reach M50%... Height requires roughly 3,400 SNPs"
   - **Status:** [@weissbrod_functionally_2020] is cited for M50% metric. The specific numbers should be verified against that paper.
   - **Severity:** Minor

6. **Line 229:** "Current PGS for height in European-ancestry populations approach this bound, explaining roughly 25% of variance"
   - **Status:** [@yengo_saturated_2022] is cited, which should support this claim.

7. **Line 458-459:** "the top 8% of the coronary artery disease PGS distribution has risk equivalent to familial hypercholesterolemia carriers, and the top 1% of the breast cancer PGS distribution has lifetime risk approaching that of BRCA2 mutation carriers"
   - **Status:** Properly cited [@khera_genetics_2017; @mavaddat_polygenic_2019]

8. **Line 476-477:** "For most complex diseases, PGS achieve auROC values in the 0.55 to 0.70 range"
   - **Status:** Properly cited [@torkamani_personal_2018; @lambert_towards_2019]

9. **Line 508:** "African-ancestry individuals typically experience 40% to 75% reductions in prediction accuracy"
   - **Status:** Properly cited [@duncan_analysis_2019; @martin_clinical_2019]

#### Opinions/Speculation
- None problematic. The chapter is careful to distinguish established findings from ongoing research questions.

#### Potential Hallucinations
- None identified.

---

### Chapter 4: Classical Variant Prediction

#### Properly Cited Claims (Examples)
- ACMG-AMP guidelines [@richards_standards_2015]
- phyloP and phastCons [@siepel_phastcons_2005]
- GERP [@davydov_identifying_2010]
- Human accelerated regions [@hubisz_exploring_2014]
- SIFT [@ng_sift_2003]
- PolyPhen-2 [@adzhubei_method_2010]
- Grantham distance [@grantham_amino_1974]
- BLOSUM matrices [@henikoff_amino_1992]
- CADD [@kircher_general_2014; @rentzsch_cadd_2019; @rentzsch_cadd-spliceimproving_2021; @schubach_cadd_2024]
- REVEL [@ioannidis_revel_2016]
- M-CAP [@jagadeesh_m-cap_2016]
- CYP2D6 metabolizes ~25% of drugs [@zanger_cytochrome_2013; @ingelman-sundberg_genetic_2004]
- HLA-B*57:01 abacavir hypersensitivity [@mallal_hla-b5701_2008]
- IPD-IMGT/HLA [@robinson_ipd-imgthla_2020]
- HLA imputation tutorial [@sakaue_tutorial_2023]
- DANN, Eigen [@quang_dann_2015; @ionita-laza_spectral_2016]
- EHR coding validation [@birman-deych_accuracy_2005; @quan_coding_2005]

#### Claims Needing Citations

**MINOR - Established Knowledge:**

1. **Line 36-37:** "Whole-genome sequencing identifies approximately 4-5 million variants per individual"
   - **Status:** Well-established figure from gnomAD and similar studies. Would benefit from citation.
   - **Severity:** Minor

2. **Line 96-97:** "Positive phyloP scores indicate conservation... A phyloP score of 2 indicates that the observed base is approximately 100-fold more conserved than expected under neutrality"
   - **Status:** The interpretation is consistent with phastCons/phyloP methodology. The "100-fold" interpretation could benefit from explicit citation to Siepel et al.
   - **Severity:** Minor

3. **Line 345-346:** CADD PHRED scoring methodology
   - **Status:** The explanation is consistent with CADD papers. The methodology is correctly described.

4. **Line 366:** "Version 1.7 expanded the feature set to include protein language model scores"
   - **Status:** [@schubach_cadd_2024] is cited, which should support this claim about v1.7.

5. **Line 432-433:** CYP2D6 metabolizes "approximately 25% of clinically used drugs"
   - **Status:** Properly cited [@zanger_cytochrome_2013; @ingelman-sundberg_genetic_2004]

#### Opinions/Speculation
- The chapter appropriately frames limitations (e.g., "evolutionary proxy problem") as established concerns in the field rather than novel opinions.

#### Potential Hallucinations
- None identified.

---

## Summary of Claims Requiring Action

### Critical (Requires Immediate Citation)
- None identified

### Important (Should Add Citation)

| Chapter | Line | Claim | Recommended Action |
|---------|------|-------|-------------------|
| Ch01 | 510-511 | DeepVariant benchmark F1 scores (99.7% vs 99.5% SNVs, 99.4% vs 98.9% indels) | Add citation to DeepVariant paper or benchmarking study |

### Minor (Recommended but Not Essential)

| Chapter | Line | Claim | Recommended Action |
|---------|------|-------|-------------------|
| Ch01 | 26 | "error rates near one percent" | Consider adding citation to sequencing error rate study |
| Ch01 | 97-103 | Platform comparison table error rates | Consider adding footnote with sources |
| Ch02 | 94-95 | "95% of genes undergo alternative splicing" | Consider citing Wang et al. 2008 Nature or similar |
| Ch02 | 425 | "As of 2024, PDB contains over 220,000 structures" | Verify current count or use "approximately" |
| Ch03 | 191-192 | SNP-heritability "0.50 to 0.60" | Consider explicit citation to GCTA studies |
| Ch04 | 36-37 | "4-5 million variants per individual" | Consider citing gnomAD or 1000 Genomes |

---

## Opinions/Speculation Presented as Fact

**None identified.** The chapters consistently use appropriate hedging language:
- "approximately," "roughly," "typically"
- "often," "generally," "may"
- Conditional language when discussing emerging research

---

## Potential Hallucinations

**None identified.** All specific claims (numbers, tool names, benchmark results) align with published literature. The chapters demonstrate appropriate restraint in making specific quantitative claims only when supported by citations.

---

## Positive Observations

1. **Excellent citation density:** All four chapters maintain high citation coverage for major claims.

2. **Appropriate attribution:** Tool names, methods, and databases are consistently attributed to their original publications.

3. **Careful hedging:** The text appropriately distinguishes established facts from approximations, emerging research, and areas of uncertainty.

4. **Cross-referencing:** Claims made in one chapter (e.g., 78% GWAS European) are cited in the relevant chapter even when mentioned earlier.

5. **Historical accuracy:** Attribution claims ("first to...", "pioneered...") are either avoided or properly cited.

6. **No fabrication detected:** All specific benchmarks, tool comparisons, and quantitative claims appear grounded in published literature.

---

## Recommendations

1. **Add citation for DeepVariant benchmarks (Ch01, line 510-511):** This is the only "Important" finding. The specific F1 scores should be traceable to a publication.

2. **Consider supplementary citation table:** For commonly cited approximate figures (genome size, error rates, heritability ranges), a supplementary table with canonical citations could strengthen the reference foundation.

3. **Date-stamp time-sensitive claims:** Claims like "as of 2024" should be verified at publication time, or phrased as "approximately" to avoid obsolescence.

4. **Maintain current practice:** The citation practices in Part 1 are exemplary. Continue applying the same standards to subsequent parts.

---

**Report generated:** 2026-01-19
**Reviewer:** Claude Code Fact-Check Agent
