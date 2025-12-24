# Instruction Compliance Report: Clinical Risk Prediction
## Source
- File: `p6-ch25-clinical-risk.qmd`
- Chapter title: Clinical Risk Prediction
- Total lines: 279

## Summary of Issues
- **CRITICAL**: 3
- **HIGH**: 22
- **MEDIUM**: 4
- **LOW**: 0

## Issues

### CRITICAL
#### CRITICAL-01: OUTPUT_FORMAT_QMD
- Location: Line 1 (Section: Clinical Risk Prediction)
- Evidence: Source file is `p6-ch25-clinical-risk.qmd` (Quarto .qmd), but project instructions require delivering chapter prose as `.md`.
- Recommendation: Convert final deliverable to `.md` (no YAML frontmatter) per project output requirements.

#### CRITICAL-02: META_COMMENTARY
- Location: Line 7 (Section: Clinical Risk Prediction)
- Evidence: …into tools that change practice remains the open question. This chapter examines that translation challenge: how foundation model f…
- Recommendation: Remove self-referential framing (e.g., “This chapter…”, “In this chapter…”). State the substantive claims directly.

#### CRITICAL-03: META_COMMENTARY
- Location: Line 257 (Section: Clinical Risk Prediction > Translation Checklist)
- Evidence: …rational requirements. The following considerations distill this chapter's themes into actionable guidance.
- Recommendation: Remove self-referential framing (e.g., “This chapter…”, “In this chapter…”). State the substantive claims directly.


### HIGH
#### HIGH-01: ORDINAL_SCAFFOLDING
- Location: Line 13 (Section: Clinical Risk Prediction > From Polygenic Scores to Foundation Model Features)
- Evidence: Three limitations constrain the clinical impact of this approach. First, the linear additive model cannot capture epistatic interactions where the effect of one variant depends on the presence of others, nor can it represent the complex nonlinear relationships between genetic variation and disease that emerge from regulatory networks and cellular pathways. Second, polygenic scores derived from European-ancestry genome-wide association studies substantially underperform in other populations, with effect sizes often attenuating by half or more in African or East Asian ancestries due to differences in linkage disequilibrium structure and allele frequencies (@sec-confounding). Third, a single scalar provides no mechanistic insight: a high polygenic score for diabetes does not indicate whether risk stems from impaired insulin secretion, insulin resistance, or altered satiety signaling, information that might guide intervention selection.
- Recommendation: Remove ordinal scaffolding (“First…, Second…”) and rewrite as prose without enumerative crutches (or use a table/callout if appropriate).

#### HIGH-02: MALFORMED_CITATION_SYNTAX
- Location: Line 15 (Section: Clinical Risk Prediction > From Polygenic Scores to Foundation Model Features)
- Evidence: Foundation models address these limitations through richer representations. Instead of treating variants as independent weighted features, models like Delphi and G2PT learn genome-wide embeddings that encode sequence context, regulatory annotations, and cross-variant interactions [@`georgantas_delphi_2024`; @`lee_g2pt_2025`]. These approaches can capture nonlinear structure in genetic risk, leverage functional priors that transfer across ancestries, and provide attention-based attributions that highlight which genomic regions contribute most to predictions. Fine-mapping models like MIFM estimate posterior probabilities for causal variants within association loci, allowing risk models to weight variants by evidence for causality rather than treating all correlated variants equally [@`rakowski_mifm_2025`].
- Recommendation: Fix citation syntax to standard Pandoc/Quarto form (e.g., `[@citekey]` or `Author et al. @citekey`) and remove backticks embedded in citekeys.

#### HIGH-03: MALFORMED_CITATION_SYNTAX
- Location: Line 35 (Section: Clinical Risk Prediction > Feature Integration Architectures)
- Evidence: DNA-level foundation models provide variant effect predictions without requiring trait-specific training. Systems like Nucleotide Transformer, HyenaDNA, and GPN compute sequence-based deleteriousness scores that reflect how mutations disrupt regulatory grammar, splice sites, or protein-coding sequences [@dalla-torre_nucleotide_2023; @`nguyen_hyenadna_2023`; @`benegas_gpn_2023`]. These zero-shot predictions transfer across traits and ancestries because they derive from sequence properties rather than population-specific association statistics. Fine-mapping models like MIFM integrate such functional priors with association evidence to estimate which variants within a locus are likely causal, providing principled weights for aggregation [@`rakowski_mifm_2025`].
- Recommendation: Fix citation syntax to standard Pandoc/Quarto form (e.g., `[@citekey]` or `Author et al. @citekey`) and remove backticks embedded in citekeys.

#### HIGH-04: MALFORMED_IMAGE_LINK
- Location: Line 38 (Section: Clinical Risk Prediction > Feature Integration Architectures)
- Evidence: ![**FIGURE PLACEHOLDER A**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER%20A``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-05: MALFORMED_IMAGE_LINK
- Location: Line 40 (Section: Clinical Risk Prediction > Feature Integration Architectures)
- Evidence: ![**FIGURE PLACEHOLDER B**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER%20B``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-06: MALFORMED_IMAGE_LINK
- Location: Line 42 (Section: Clinical Risk Prediction > Feature Integration Architectures)
- Evidence: ![**FIGURE PLACEHOLDER C**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER%20C``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-07: MALFORMED_CITATION_SYNTAX
- Location: Line 50 (Section: Clinical Risk Prediction > Feature Integration Architectures)
- Evidence: Multi-omics foundation models extend beyond germline sequence. Cell-type-resolved representations from GLUE, scGLUE, and CpGPT capture regulatory state across chromatin accessibility, methylation, and expression (@sec-single-cell) [@`cao_glue_2022`; @`camillo_cpgpt_2024`]. Rare variant burden scores from DeepRVAT aggregate predicted effects across genes into pathway-level impairment measures [@`clarke_deeprvat_2024`]. For oncology applications, tumor embedding models like SetQuence and graph neural network-based subtypers encode complex somatic mutation landscapes into patient-level representations [@`jurenaite_setquence_2024`; @`li_mogcn_2022`].
- Recommendation: Fix citation syntax to standard Pandoc/Quarto form (e.g., `[@citekey]` or `Author et al. @citekey`) and remove backticks embedded in citekeys.

#### HIGH-08: MALFORMED_IMAGE_LINK
- Location: Line 70 (Section: Clinical Risk Prediction > Temporal Modeling Architectures)
- Evidence: ![**FIGURE PLACEHOLDER A**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER%20A``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-09: MALFORMED_IMAGE_LINK
- Location: Line 72 (Section: Clinical Risk Prediction > Temporal Modeling Architectures)
- Evidence: ![**FIGURE PLACEHOLDER B**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER%20B``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-10: MALFORMED_IMAGE_LINK
- Location: Line 74 (Section: Clinical Risk Prediction > Temporal Modeling Architectures)
- Evidence: ![**FIGURE PLACEHOLDER C**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER%20C``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-11: MALFORMED_CITATION_SYNTAX
- Location: Line 79 (Section: Clinical Risk Prediction > Temporal Modeling Architectures)
- Evidence: Deep survival models extend this framework through neural network architectures that learn nonlinear feature interactions. DeepSurv replaces the linear Cox predictor with a multilayer network while preserving the partial likelihood objective [@`katzman_deepsurv_2018`]. Deep Survival Machines model the survival distribution as a mixture of parametric components, enabling richer distributional assumptions than the semiparametric Cox approach [@`nagpal_deep_2021`]. These architectures naturally accommodate the high-dimensional embeddings that foundation models produce, though the risk of overfitting increases and careful regularization becomes essential.
- Recommendation: Fix citation syntax to standard Pandoc/Quarto form (e.g., `[@citekey]` or `Author et al. @citekey`) and remove backticks embedded in citekeys.

#### HIGH-12: MALFORMED_CITATION_SYNTAX
- Location: Line 85 (Section: Clinical Risk Prediction > Temporal Modeling Architectures)
- Evidence: Transformer architectures designed for irregularly sampled time series offer a natural framework for clinical trajectories. Models like STraTS and similar clinical transformers handle the variable timing and missing measurements characteristic of real-world healthcare data [@`tipirneni_self_2022`]. Position encodings based on actual timestamps rather than sequence position accommodate irregular sampling. Attention mechanisms identify which historical measurements most inform current predictions. Foundation model embeddings at each timepoint provide richer input representations than raw laboratory values alone.
- Recommendation: Fix citation syntax to standard Pandoc/Quarto form (e.g., `[@citekey]` or `Author et al. @citekey`) and remove backticks embedded in citekeys.

#### HIGH-13: MALFORMED_IMAGE_LINK
- Location: Line 118 (Section: Clinical Risk Prediction > Evaluation for Clinical Deployment > The Validation Hierarchy)
- Evidence: ![**FIGURE PLACEHOLDER**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-14: MALFORMED_IMAGE_LINK
- Location: Line 134 (Section: Clinical Risk Prediction > Uncertainty Quantification)
- Evidence: ![**FIGURE PLACEHOLDER**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-15: MALFORMED_IMAGE_LINK
- Location: Line 152 (Section: Clinical Risk Prediction > Fairness and Health Equity)
- Evidence: ![**FIGURE PLACEHOLDER A**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER%20A``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-16: MALFORMED_IMAGE_LINK
- Location: Line 154 (Section: Clinical Risk Prediction > Fairness and Health Equity)
- Evidence: ![**FIGURE PLACEHOLDER B**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER%20B``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-17: MALFORMED_IMAGE_LINK
- Location: Line 156 (Section: Clinical Risk Prediction > Fairness and Health Equity)
- Evidence: ![**FIGURE PLACEHOLDER C**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER%20C``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-18: MALFORMED_IMAGE_LINK
- Location: Line 158 (Section: Clinical Risk Prediction > Fairness and Health Equity)
- Evidence: ![**FIGURE PLACEHOLDER D**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER%20D``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-19: MALFORMED_IMAGE_LINK
- Location: Line 176 (Section: Clinical Risk Prediction > Clinical Integration)
- Evidence: ![**FIGURE PLACEHOLDER**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-20: MALFORMED_CITATION_SYNTAX
- Location: Line 221 (Section: Clinical Risk Prediction > Case Studies > Cardiometabolic Risk Stratification)
- Evidence: A foundation model-augmented risk system could refine this assessment. Variant effect scores from DNA foundation models annotate variants in cardiometabolic risk loci with predicted regulatory and coding impacts. A polygenic embedding model like Delphi or G2PT produces a genome-wide representation capturing nonlinear risk structure beyond simple effect size sums [@`georgantas_delphi_2024`; @`lee_g2pt_2025`]. This genomic embedding combines with electronic health record features through an intermediate fusion architecture, producing an updated 10-year risk estimate of 11.4%, above the treatment threshold.
- Recommendation: Fix citation syntax to standard Pandoc/Quarto form (e.g., `[@citekey]` or `Author et al. @citekey`) and remove backticks embedded in citekeys.

#### HIGH-21: MALFORMED_IMAGE_LINK
- Location: Line 224 (Section: Clinical Risk Prediction > Case Studies > Cardiometabolic Risk Stratification)
- Evidence: ![**FIGURE PLACEHOLDER**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-22: MALFORMED_CITATION_SYNTAX
- Location: Line 237 (Section: Clinical Risk Prediction > Case Studies > Oncology Prognosis)
- Evidence: Foundation models can enrich prognostic assessment through multiple channels. Tumor mutation profiles encoded through models like SetQuence or SetOmic produce embeddings capturing the specific constellation of somatic alterations beyond simple mutation counts [@`jurenaite_setquence_2024`]. Transcriptomic profiling integrated through GLUE-style latent spaces adds expression context reflecting tumor microenvironment and pathway activity [@`cao_glue_2022`]. Graph neural network-based subtyping assigns the tumor to a molecular subtype with characteristic prognosis and treatment response patterns [@`li_mogcn_2022`].
- Recommendation: Fix citation syntax to standard Pandoc/Quarto form (e.g., `[@citekey]` or `Author et al. @citekey`) and remove backticks embedded in citekeys.


### MEDIUM
#### MEDIUM-01: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 97 (Section: Clinical Risk Prediction > Evaluation for Clinical Deployment > Discrimination)
- Evidence: Strong discrimination is necessary but not sufficient. A model that correctly ranks patients but systematically overestimates or underestimates absolute risk magnitudes will lead to inappropriate clinical decisions. If a model predicts 5% risk for patients who actually experience 15% event rates, physicians using those predictions will undertreat. Conversely, systematically inflated predictions lead to overtreatment with attendant harms and costs.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-02: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 101 (Section: Clinical Risk Prediction > Evaluation for Clinical Deployment > Calibration)
- Evidence: Calibration asks whether predicted probabilities match observed frequencies. If a model assigns 20% risk to a group of patients, approximately 20% should experience the outcome. Well-calibrated predictions can be interpreted at face value and used directly for clinical decision-making; miscalibrated predictions mislead regardless of discrimination quality.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-03: TRANSITION_STARTER
- Location: Line 167 (Section: Clinical Risk Prediction > Fairness and Health Equity)
- Evidence: …oups, and localized fine-tuning using deployment-site data. However, technical interventions alone cannot overcome structural i…
- Recommendation: Rephrase to avoid starting a sentence with this transition word, or reduce frequency.

#### MEDIUM-04: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 226 (Section: Clinical Risk Prediction > Case Studies > Cardiometabolic Risk Stratification)
- Evidence: [Enhancing] Patient journey diagram. Patient profile: 52yo man, LDL 145, BP 138/88, HbA1c 5.9%; family history (father MI at 58); traditional risk 8.2% (below statin threshold). FM integration: DNA FMs annotate variants; polygenic embedding (Delphi/G2PT) captures nonlinear risk; fusion with EHR; updated estimate 11.4% (above threshold). Clinical decision impact: Threshold crossed → statin indicated; pathway attribution → LDL metabolism (supports mechanism); attention attribution → regions for counseling. Validation requirements: External validation, equity analysis. Key insight: Value depends on whether refined estimate enables different action.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

## Quick Fix Checklist
- [ ] Eliminate list-style scaffolding (bullets, numbered lists, “First/Second/Third” ordinals) in flowing prose.
- [ ] Remove meta-commentary (“This chapter…”, “In this chapter…”, “In this section…”).
- [ ] Fix malformed citations (remove backticks in citekeys; use standard `[@citekey]` form).
- [ ] Audit numeric/statistical claims and add citations where needed.
- [ ] Fix malformed image placeholder Markdown so Quarto renders figures correctly.
- [ ] Convert final deliverable to `.md` per output requirements.
- [ ] Reduce sentence-start transitions (e.g., “However,”).

