# Fact-Check Report: Part 6 (Responsible Deployment)

**Date:** 2026-01-19
**Reviewer:** Automated Fact-Check Agent
**Chapters Reviewed:**
- Chapter 24: Uncertainty Quantification (`p6-ch24-uncertainty.qmd`)
- Chapter 25: Interpretability (`p6-ch25-interpretability.qmd`)
- Chapter 26: Causal Inference (`p6-ch26-causal.qmd`)
- Chapter 27: Regulatory and Governance (`p6-ch27-regulatory.qmd`)

---

## Executive Summary

| Check Type | Ch24 | Ch25 | Ch26 | Ch27 | Overall |
|------------|------|------|------|------|---------|
| Quantitative claims without citations | WARN | WARN | PASS | WARN | **WARN** |
| Regulatory/legal claims | N/A | PASS | PASS | WARN | **WARN** |
| Historical/attribution claims | PASS | WARN | PASS | PASS | **WARN** |
| Opinions stated as facts | PASS | PASS | PASS | PASS | **PASS** |
| Potential hallucinations | WARN | WARN | PASS | WARN | **WARN** |

**Legend:** PASS = No significant issues; WARN = Issues requiring attention; FAIL = Critical issues

---

## Chapter 24: Uncertainty Quantification

### Properly Cited Claims
The chapter has good citation coverage for foundational concepts:
- Deep neural network miscalibration [@guo_calibration_2017]
- DeepLIFT method [@shrikumar_learning_2017]
- Integrated gradients [@sundararajan_axiomatic_2017]
- MC Dropout as Bayesian approximation [@gal_dropout_2016]
- Deep mutational scanning noise levels [@fowler_deep_2014; @rubin_statistical_2017]
- ClinVar VUS statistics [@landrum_clinvar_2018]

### Unsupported Claims Requiring Citations

#### Critical (Could mislead readers or affect clinical decisions)
1. **Line ~62**: "ClinVar contains approximately two million VUS compared to roughly 250,000 variants classified as pathogenic"
   - **Status:** Cites @landrum_clinvar_2018 but this is outdated (2018). Numbers have changed significantly.
   - **Recommendation:** Update citation to current ClinVar statistics or note the approximate/dated nature of these figures.

#### Important (Factual claims that should be verified)
1. **Line ~102**: "deep mutational scanning experiments typically exhibit 10 to 20 percent technical variation between replicates"
   - **Status:** Cited [@fowler_deep_2014; @rubin_statistical_2017] - VERIFIED

2. **Line ~287**: "optimal temperature is learned by minimizing negative log-likelihood on a held-out calibration set, typically yielding T between 1.5 and 3 for overconfident deep networks"
   - **Status:** [Citation Needed] - This specific range (1.5-3) needs a citation or should be qualified as approximate/typical.

3. **Line ~539**: "language models assign high likelihood to repetitive sequences, sequences with unusual but consistent patterns"
   - **Status:** Marked [Citation Needed] in the text itself - needs citation added.

#### Minor (General claims that are widely accepted)
- None identified.

### Opinions/Speculation Stated as Facts
- None identified. The chapter appropriately uses hedging language ("may," "can," "often") for uncertain claims.

### Potential Hallucinations
1. **Temperature range 1.5-3**: The specific range of "typically yielding T between 1.5 and 3" is plausible but overly specific without citation.

---

## Chapter 25: Interpretability

### Properly Cited Claims
- DeepLIFT methodology [@shrikumar_learning_2017]
- Integrated gradients [@sundararajan_axiomatic_2017]
- TF-MoDISco method [@shrikumar_technical_2018]
- BERTology overview [@rogers_primer_2021]
- ACMG-AMP guidelines [@richards_standards_2015]
- SpliceAI [@jaganathan_predicting_2019]
- Attention as explanation critique [@jain_attention_2019]

### Unsupported Claims Requiring Citations

#### Critical
1. **Line ~52-53**: "ISM predictions correlate with experimental deep mutational scanning (r approximately 0.6-0.8)"
   - **Status:** [Citation Needed] - This specific correlation range needs citation. The claim appears in a figure caption.
   - **Recommendation:** Add citation to deep mutational scanning validation studies.

2. **Line ~128**: "DeepSEA filters include recognizable matches to CTCF, AP-1, and cell-type-specific factors"
   - **Status:** Explicitly marked as "[Citation Needed: Zhou & Troyanskaya, DeepSEA paper]" in text
   - **Recommendation:** Add proper citation to DeepSEA paper (Zhou & Troyanskaya, Nature Methods, 2015)

3. **Line ~174**: "Applications to models like BPNet trained on ChIP-seq data have recovered known transcription factor motifs, discovered novel sequence variants, and revealed spacing constraints validated through synthetic reporter assays"
   - **Status:** Explicitly marked "[Citation Needed: BPNet paper]"
   - **Recommendation:** Add citation to Avsec et al., Nature Genetics, 2021

#### Important
1. **Line ~365**: "Attention head analysis in DNA language models has identified heads specialized for different genomic functions: some attend within genes, others across regulatory regions, still others implement positional computations"
   - **Status:** Explicitly marked "[Citation Needed]"
   - **Recommendation:** Add citation to relevant mechanistic interpretability work on DNA language models.

2. **Line ~417**: "Critics have noted that evidential deep learning can produce unreliable uncertainty estimates when the distributional assumptions are violated or when training data is limited"
   - **Status:** Explicitly marked "[Citation Needed]"
   - **Recommendation:** Add citation to critiques of evidential deep learning (e.g., Bengs et al., ICLR 2022)

#### Minor
- None identified.

### Opinions/Speculation Stated as Facts
- None identified. The chapter appropriately distinguishes between established methods and emerging research.

### Potential Hallucinations
1. **ISM correlation range (0.6-0.8)**: This is plausible but needs verification with specific studies.

---

## Chapter 26: Causal Inference

### Properly Cited Claims
Excellent citation coverage:
- Pearl's ladder of causation [@pearl_book_2018]
- Mendelian randomization foundations [@davey_smith_mendelian_2003; @lawlor_mendelian_2008]
- MR-Egger and robust methods [@bowden_mendelian_2015; @hartwig_robust_2017]
- pQTL-based drug target validation [@schmidt_genetic_2020]
- Model-X knockoffs [@candes_panning_2018]
- Bayesian fine-mapping [@maller_bayesian_2012; @benner_finemap_2016]
- Colocalization methods [@giambartolomei_bayesian_2014]
- CRISPR screen methodology [@shalem_genome-scale_2014; @adamson_multiplexed_2016]
- Geneformer [@theodoris_geneformer_2023]
- Drug-biological embeddings [@zitnik_modeling_2018]
- GENIE3 network inference [@huynh-thu_inferring_2010]
- Attention interpretation critique [@jain_attention_2019]
- Granger causality [@granger_investigating_1969]
- RNA velocity [@la_manno_rna_2018]
- Causal reasoning in LLMs [@kiciman_causal_2024]

### Unsupported Claims Requiring Citations
- **None identified.** This chapter has comprehensive citation coverage.

### Opinions/Speculation Stated as Facts
- None identified. The chapter appropriately uses conditional language for uncertain claims.

### Potential Hallucinations
- None identified.

---

## Chapter 27: Regulatory and Governance

### Properly Cited Claims
Strong citation coverage for regulatory frameworks:
- IMDRF SaMD guidance [@international_medical_device_regulators_forum_software_2014; @international_medical_device_regulators_forum_software_2017]
- FDA AI device statistics [@food_and_drug_administration_artificial_2025]
- First autonomous AI FDA clearance [@abramoff_pivotal_2018]
- FDA AI/ML SaMD action plan [@us_food_and_drug_administration_artificial_2021]
- FDA guidance updates [@food_and_drug_administration_using_2023]
- EU MDR [@european_parliament_regulation_2017]
- EU AI Act [@european_parliament_regulation_2024]
- GDPR [@european_parliament_regulation_2016]
- Common Rule [@health_and_human_services_federal_2018]
- GINA [@us_congress_genetic_2008]
- CDC ACCE framework [@center_for_disease_control_acce_2022]
- LDT guidance [@food_and_drug_administration_laboratory_2024]
- Dynamic consent [@kaye_dynamic_2014]
- UK Biobank [@sudlow_uk_2015; @bycroft_uk_2018]
- Federated learning [@rieke_future_2020]
- Gradient reconstruction attacks [@zhu_deep_2019]
- Re-identification risks [@gymrek_identifying_2013; @homer_resolving_2008; @erlich_routes_2014]
- Model cards [@mitchell_model_2019]
- Datasheets [@gebru_datasheets_2021]
- PRS ancestry disparities [@martin_clinical_2019]
- Myriad decision [@supreme_court_of_the_united_states_assoc_2013]
- AI inventorship [@arnold_thaler_2021]
- Automation bias [@parasuraman_complacency_2010]
- Biosecurity evaluation [@soice_can_2023; @shevlane_structured_2022]

### Unsupported Claims Requiring Citations

#### Critical
1. **Line ~26**: "As of 2024, more than 500 AI-enabled medical devices have received FDA authorization, but fewer than a dozen involve genomic interpretation, and none yet deploys a foundation model at scale"
   - **Status:** Cites [@food_and_drug_administration_artificial_2025] for the 500+ figure. The "<12 genomic" and "none FM" claims need verification.
   - **Recommendation:** Verify the specific counts or add qualifying language ("approximately," "to our knowledge").

2. **Lines ~45-46**: "Hereditary breast and ovarian cancer syndrome (BRCA1/2) is a serious condition: pathogenic variants confer 45-85% lifetime breast cancer risk and 10-45% ovarian cancer risk"
   - **Status:** [Citation Needed] - These specific penetrance ranges are widely cited but should have a primary citation.
   - **Recommendation:** Add citation (e.g., Kuchenbaecker et al., JAMA, 2017)

3. **Line ~381-382**: "Polygenic scores derived from European-ancestry GWAS show 40 to 75 percent reductions in prediction accuracy for African-ancestry individuals"
   - **Status:** References @sec-ch03-portability but the specific percentages (40-75%) need citation here.
   - **Recommendation:** Add inline citation (e.g., Martin et al., Nature Genetics, 2019)

#### Important
1. **Line ~108**: Table states typical regulatory timelines (e.g., "FDA: 6-18 months", "EU MDR: 12-24 months")
   - **Status:** [Citation Needed] - These timelines are reasonable estimates but should be cited or qualified.
   - **Recommendation:** Add source or note these are approximate industry estimates.

#### Minor
- None identified.

### Opinions/Speculation Stated as Facts
- None identified. The chapter appropriately uses hedging language for uncertain regulatory developments.

### Potential Hallucinations
1. **BRCA1/2 penetrance figures**: The 45-85% breast cancer and 10-45% ovarian cancer ranges are consistent with literature but should be cited.
2. **Regulatory timeline estimates**: Plausible but should be verified or qualified.

---

## Summary of All Issues

### Claims Explicitly Marked [Citation Needed] in Text
The authors have self-identified several gaps that should be addressed:

| Chapter | Location | Claim | Recommended Citation |
|---------|----------|-------|---------------------|
| 25 | Line ~128 | DeepSEA filter motif matches | Zhou & Troyanskaya, Nature Methods, 2015 |
| 25 | Line ~174 | BPNet motif discovery | Avsec et al., Nature Genetics, 2021 |
| 25 | Line ~365 | DNA LM attention head specialization | [Research citation needed] |
| 25 | Line ~417 | Evidential deep learning critiques | Bengs et al., ICLR 2022 |
| 24 | Line ~539 | LM high likelihood for repetitive sequences | [Research citation needed] |

### Additional Citations Recommended

| Chapter | Claim | Recommendation |
|---------|-------|----------------|
| 24 | Temperature scaling range 1.5-3 | Cite Guo et al. 2017 or qualify as approximate |
| 25 | ISM-DMS correlation 0.6-0.8 | Add experimental validation citation |
| 27 | BRCA penetrance figures | Kuchenbaecker et al., JAMA, 2017 |
| 27 | PRS accuracy reduction 40-75% | Martin et al., Nature Genetics, 2019 |
| 27 | <12 genomic AI devices | Verify or qualify with "approximately" |

### Claims at Risk of Being Outdated

| Chapter | Claim | Issue |
|---------|-------|-------|
| 24 | ClinVar VUS/pathogenic counts | 2018 citation; numbers have changed significantly |
| 27 | 500+ FDA-cleared AI devices | Rapidly changing; ensure citation is current |

---

## Recommendations

### Immediate Actions
1. **Address explicit [Citation Needed] markers** - Five claims are self-identified as needing citations
2. **Add BRCA penetrance citation** - Critical clinical figure needs primary source
3. **Verify ClinVar statistics** - Update to current numbers or note approximation

### Before Publication
1. **Update regulatory statistics** - FDA device counts and timeline estimates should be verified
2. **Add ISM-DMS validation citation** - Important for interpretability chapter credibility
3. **Review temperature scaling range** - Either cite source or soften language to "typically between approximately 1.5 and 3"

### Style Consistency
- The chapters appropriately use cross-references to other book chapters for detailed treatments
- Citation density is appropriate for a textbook format
- Hedging language is used appropriately for uncertain claims

---

## Quality Assessment

**Overall Assessment:** The Part 6 chapters demonstrate good scholarly practice with comprehensive citation coverage for foundational concepts and methods. The most significant issues are:

1. **Self-identified gaps**: Five [Citation Needed] markers should be resolved
2. **Specific quantitative claims**: A few precise numerical claims (penetrance figures, correlation ranges, device counts) need primary citations
3. **Dated statistics**: Some ClinVar and FDA statistics may be outdated

The chapters avoid speculation-as-fact and potential hallucinations are limited to a few specific numerical claims that are plausible but unverified. The regulatory chapter in particular shows excellent citation coverage for a rapidly evolving field.

**Recommendation:** Address the explicit [Citation Needed] markers and the high-priority citations identified above before final publication. The chapters are otherwise well-grounded in the literature.
