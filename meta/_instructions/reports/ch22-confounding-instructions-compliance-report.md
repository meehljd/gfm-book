# Instruction Compliance Report: Confounders and Leakage
## Source
- File: `p5-ch22-confounding.qmd`
- Chapter title: Confounders and Leakage
- Total lines: 235

## Summary of Issues
- **CRITICAL**: 5
- **HIGH**: 1
- **MEDIUM**: 3
- **LOW**: 3

## Issues

### CRITICAL
#### CRITICAL-01: OUTPUT_FORMAT_QMD
- Location: Line 1 (Section: Confounders and Leakage)
- Evidence: Source file is `p5-ch22-confounding.qmd` (Quarto .qmd), but project instructions require delivering chapter prose as `.md`.
- Recommendation: Convert final deliverable to `.md` (no YAML frontmatter) per project output requirements.

#### CRITICAL-02: META_COMMENTARY
- Location: Line 7 (Section: Confounders and Leakage)
- Evidence: …if that correlation helps optimize the training objective. This chapter examines the major sources of confounding in genomic datase…
- Recommendation: Remove self-referential framing (e.g., “This chapter…”, “In this chapter…”). State the substantive claims directly.

#### CRITICAL-03: EM_DASH
- Location: Line 170 (Section: Confounders and Leakage > Mitigation Strategies)
- Evidence: …der scores by design). Annotation: "Approaches complementary—use multiple."
- Recommendation: Replace the em-dash (—) with a colon, semicolon, parentheses, or split into separate sentences.

#### CRITICAL-04: META_COMMENTARY
- Location: Line 231 (Section: Confounders and Leakage > Rigor as Response)
- Evidence: The confounding and bias problems examined in this chapter are not reasons for despair. They are reasons for rigor. Th…
- Recommendation: Remove self-referential framing (e.g., “This chapter…”, “In this chapter…”). State the substantive claims directly.

#### CRITICAL-05: META_COMMENTARY
- Location: Line 231 (Section: Confounders and Leakage > Rigor as Response)
- Evidence: The confounding and bias problems examined in this chapter are not reasons for despair. They are reasons for rigor. Th…
- Recommendation: Remove self-referential framing (e.g., “This chapter…”, “In this chapter…”). State the substantive claims directly.


### HIGH
#### HIGH-01: ORDINAL_SCAFFOLDING
- Location: Line 27 (Section: Confounders and Leakage > Confounding, Bias, and Leakage)
- Evidence: These phenomena interact. Confounders create biases in estimated effects. Leakage hides those biases by making held-out performance appear better than warranted. Distribution shift then reveals the problem when deployment performance collapses. For foundation models, three features magnify these risks. First, genomes encode ancestry, relatedness, and assay conditions in thousands of subtle features, even when those labels are never explicitly provided. Second, large transformers find shortcuts that smaller models would miss if those shortcuts improve the training objective. Third, complex training regimes involving pretraining on biobank-scale data, fine-tuning on curated labels, and evaluation on community benchmarks create many opportunities for direct and indirect leakage.
- Recommendation: Remove ordinal scaffolding (“First…, Second…”) and rewrite as prose without enumerative crutches (or use a table/callout if appropriate).


### MEDIUM
#### MEDIUM-01: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 3 (Section: Confounders and Leakage)
- Evidence: A variant effect predictor trained on **ClinVar** achieves 0.92 AUC on held-out variants from the same database, yet performance drops to 0.71 when evaluated on a prospectively collected clinical cohort. A **polygenic risk score** for coronary artery disease stratifies European-ancestry individuals with impressive discrimination, then fails almost completely when applied to individuals of African ancestry. A gene expression model trained on GTEx data predicts tissue-specific patterns with apparent **precision**, until deployment reveals it learned to distinguish sequencing centers rather than biological states. Each model worked brilliantly in evaluation and failed quietly in practice.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-02: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 64 (Section: Confounders and Leakage > Population Structure as a Shortcut)
- Evidence: [Essential] Multi-panel figure. Panel A (PCA of genomic data): *PC1* vs *PC2*; colored by ancestry; clear clustering. Panel B (Ancestry in k-mer frequencies): Heatmap across populations; even local composition differs. Panel C (The shortcut pathway): Flow diagram (Ancestry → Sequencing → Labels; Ancestry → Allele frequencies → Features; model learns via ancestry). Panel D (Cross-population performance): Bar chart showing 40-75% PGS reduction; "Shortcuts fail when relationship changes."
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-03: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 158 (Section: Confounders and Leakage > Detecting Confounding)
- Evidence: **Split sensitivity analysis** varies the splitting strategy to probe for leakage. Re-evaluate performance under locus-level splits, cohort holdouts, or temporal splits. Large drops in performance under stricter splitting indicate that initial results were inflated. A model that achieves 0.90 AUC with random splits but only 0.75 AUC with locus-level splits has likely memorized site-specific patterns.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.


### LOW
#### LOW-01: FALSE_ENTHUSIASM_WORD
- Location: Line 3 (Section: Confounders and Leakage)
- Evidence: …rtery disease stratifies European-ancestry individuals with impressive discrimination, then fails almost completely when applied t…
- Recommendation: Replace with a more precise, neutral descriptor (e.g., “high-capacity”, “expressive”, “high-performing”) unless quoting a source.

#### LOW-02: FALSE_ENTHUSIASM_WORD
- Location: Line 110 (Section: Confounders and Leakage > Label Bias and Circularity)
- Evidence: …nst benchmarks derived from the same resources, may achieve impressive scores while learning to reproduce the assumptions and bias…
- Recommendation: Replace with a more precise, neutral descriptor (e.g., “high-capacity”, “expressive”, “high-performing”) unless quoting a source.

#### LOW-03: FALSE_ENTHUSIASM_WORD
- Location: Line 231 (Section: Confounders and Leakage > Rigor as Response)
- Evidence: …cols are designed appropriately. The goal is not to abandon powerful models but to create conditions under which their power ser…
- Recommendation: Replace with a more precise, neutral descriptor (e.g., “high-capacity”, “expressive”, “high-performing”) unless quoting a source.

## Quick Fix Checklist
- [ ] Search for and remove all em-dashes (—).
- [ ] Eliminate list-style scaffolding (bullets, numbered lists, “First/Second/Third” ordinals) in flowing prose.
- [ ] Remove meta-commentary (“This chapter…”, “In this chapter…”, “In this section…”).
- [ ] Audit numeric/statistical claims and add citations where needed.
- [ ] Convert final deliverable to `.md` per output requirements.
- [ ] Replace vague enthusiasm adjectives (“powerful”, “impressive”, “remarkable”) with precise neutral language.

