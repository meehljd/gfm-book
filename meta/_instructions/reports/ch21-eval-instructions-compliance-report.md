# Instruction Compliance Report: Evaluation Principles
## Source
- File: `p5-ch21-eval.qmd`
- Chapter title: Evaluation Principles
- Total lines: 361

## Summary of Issues
- **CRITICAL**: 2
- **HIGH**: 1
- **MEDIUM**: 16
- **LOW**: 5

## Issues

### CRITICAL
#### CRITICAL-01: OUTPUT_FORMAT_QMD
- Location: Line 1 (Section: Evaluation Principles)
- Evidence: Source file is `p5-ch21-eval.qmd` (Quarto .qmd), but project instructions require delivering chapter prose as `.md`.
- Recommendation: Convert final deliverable to `.md` (no YAML frontmatter) per project output requirements.

#### CRITICAL-02: META_COMMENTARY
- Location: Line 7 (Section: Evaluation Principles)
- Evidence: This chapter addresses how to use benchmarks appropriately to draw valid…
- Recommendation: Remove self-referential framing (e.g., “This chapter…”, “In this chapter…”). State the substantive claims directly.


### HIGH
#### HIGH-01: NO_CITATIONS_DETECTED
- Location: Line 1 (Section: Evaluation Principles)
- Evidence: No citation keys of the form [@citekey] or @citekey were detected in this chapter.
- Recommendation: Add citations for technical claims (performance numbers, dataset sizes, benchmark results, historical facts) using the project’s citation style.


### MEDIUM
#### MEDIUM-01: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 22 (Section: Evaluation Principles > Why Random Splits Fail)
- Evidence: [Essential] Three-panel comparison. Panel A (Image classification): Grid of images; random assignment works; independent. Panel B (Protein classification): Family tree; random split places related across train/test; 80% identity highlighted; "memorization pathway." Panel C (Variant prediction): Gene diagram with variants; same gene in train/test; family pedigree spanning splits; population structure. Annotations: sequence identity, relatedness, pseudo-replication.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-02: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 25 (Section: Evaluation Principles > Why Random Splits Fail)
- Evidence: The problem compounds when sequence identity is high. Two proteins sharing 80% sequence identity will typically have similar structures and functions. A model trained on one and tested on the other is not really being tested on a novel example; it is being asked to interpolate within a region of sequence space it has already explored. Even at 30% sequence identity, the so-called "twilight zone" of homology detection, proteins often share structural and functional similarities that can be exploited by sufficiently powerful models.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-03: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 29 (Section: Evaluation Principles > Why Random Splits Fail)
- Evidence: The consequence is that random splits systematically overestimate generalization. A model that achieves 0.90 area under the receiver operating characteristic curve (**AUROC**) with random splitting might achieve only 0.75 AUROC when evaluated on truly held-out examples, with the gap reflecting how much the model learned about biology versus how much it learned about the structure of the training data. Recognizing this problem is the first step toward solving it.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-04: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 43 (Section: Evaluation Principles > Homology-Aware Splitting > Clustering Tools and Workflows)
- Evidence: Two tools dominate homology-aware splitting in practice. **CD-HIT** clusters sequences by greedy incremental clustering, assigning each sequence to an existing cluster if it exceeds a similarity threshold to the cluster representative, or creating a new cluster otherwise. The algorithm is fast and scales to millions of sequences. For proteins, a typical workflow clusters at 40% sequence identity for stringent splitting or 70% for moderate splitting. For nucleotide sequences, thresholds are typically higher (80-95%) due to different evolutionary rates.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-05: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 62 (Section: Create database and cluster at 30% identity)
- Evidence: The choice of identity threshold involves trade-offs. Stricter thresholds (lower identity for proteins, higher for nucleotides) create harder generalization tests but may leave insufficient data for training if clusters are small. Permissive thresholds retain more training data but allow more leakage through homologous sequences. For protein function prediction, 30-40% identity thresholds are common; for **variant effect prediction** within genes, even stricter gene-family-level splits may be necessary.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-06: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 68 (Section: Create database and cluster at 30% identity > Practical Considerations)
- Evidence: **Transitive homology** creates hidden relationships that pairwise clustering can miss. Protein A may share 35% identity with protein B, and protein B may share 35% identity with protein C, yet A and C share only 20% identity. If A is in training and C is in testing, B serves as an indirect bridge. Connected component analysis or multi-step clustering can address these transitive relationships, though at increased computational cost.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-07: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 88 (Section: Create database and cluster at 30% identity > Splitting by Biological Axis > Splitting by Individual)
- Evidence: Family structure creates subtler leakage. First-degree relatives share approximately 50% of their genomes identical by descent. Even distant relatives share genomic segments that can be exploited by sufficiently powerful models. Best practice involves computing kinship coefficients across all individuals and either excluding one member of each related pair or assigning entire family clusters to the same split. The UK Biobank provides pre-computed relatedness estimates; other cohorts may require explicit calculation using tools like KING or `PLINK`.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-08: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 154 (Section: Create database and cluster at 30% identity > Leakage Taxonomy and Detection > Detection Strategies)
- Evidence: Several strategies help detect leakage. **Baseline analysis** asks whether simple models that could not plausibly have learned biology achieve suspiciously high performance. If a linear model using only allele frequency achieves 0.80 AUROC on a pathogenicity benchmark, and a sophisticated deep model achieves 0.82, the marginal improvement may not justify claims of biological insight.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-09: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 176 (Section: Create database and cluster at 30% identity > Metrics for Genomic Tasks > Discrimination Metrics)
- Evidence: The **area under the precision-recall curve (AUPRC)** better reflects performance when positives are rare. For variant pathogenicity prediction, where perhaps 1% of variants are truly pathogenic, a model achieving 0.95 AUROC might still have poor precision at useful recall levels. AUPRC directly captures the precision-recall trade-off that matters for applications requiring both high sensitivity and manageable false positive rates.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-10: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 178 (Section: Create database and cluster at 30% identity > Metrics for Genomic Tasks > Discrimination Metrics)
- Evidence: **Sensitivity**, **specificity**, **positive predictive value**, and **negative predictive value** require specifying a decision threshold. These metrics are more interpretable for specific use cases (e.g., "the model identifies 90% of pathogenic variants while flagging only 5% of benign variants as false positives") but require choosing thresholds that may not generalize across settings.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-11: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 206 (Section: Create database and cluster at 30% identity > Baseline Selection)
- Evidence: Baseline comparisons determine the meaning of reported performance. A model achieving 0.85 AUROC might represent a major advance if the best prior method achieved 0.70, or a trivial improvement if simple heuristics achieve 0.83. Choosing appropriate baselines is as important as choosing appropriate metrics.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-12: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 258 (Section: Create database and cluster at 30% identity > Statistical Rigor > Significance Testing)
- Evidence: For classification metrics, significance tests ask whether observed differences exceed what would be expected from sampling variation. **Bootstrap **confidence interval**s** resample the test set with replacement, recompute metrics on each resample, and report the distribution of metric values. Non-overlapping 95% confidence intervals suggest significant differences. **Permutation tests** shuffle predictions between models and measure how often shuffled differences exceed observed differences.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-13: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 260 (Section: Create database and cluster at 30% identity > Statistical Rigor > Significance Testing)
- Evidence: For comparing multiple models across multiple benchmarks, correction for multiple testing becomes important. Without correction, 20 pairwise comparisons will produce an expected one false positive at the 0.05 level even when all models perform equally. The **Bonferroni correction** divides the significance threshold by the number of tests; the **Benjamini-Hochberg procedure** controls false discovery rate with more power than Bonferroni.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-14: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 264 (Section: Create database and cluster at 30% identity > Statistical Rigor > Effect Sizes)
- Evidence: Statistical significance does not imply practical significance. A difference of 0.001 AUROC might be statistically significant with millions of test examples while being practically meaningless. **Effect sizes** quantify the magnitude of differences independent of sample size. Cohen's d for continuous outcomes and odds ratios for binary outcomes provide standardized measures of effect magnitude.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-15: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 270 (Section: Create database and cluster at 30% identity > Statistical Rigor > Confidence Intervals on Metrics)
- Evidence: Point estimates of AUROC or correlation should be accompanied by confidence intervals. **DeLong's method** provides analytical confidence intervals for AUROC; **bootstrap methods** provide distribution-free intervals for any metric. Reporting "AUROC = 0.85 (95% CI: 0.82-0.88)" is more informative than "AUROC = 0.85" alone.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-16: TRANSITION_STARTER
- Location: Line 322 (Section: Create database and cluster at 30% identity > Calibration Essentials > Assessing Calibration)
- Evidence: …lities across bins. Lower ECE indicates better calibration. However, ECE is sensitive to binning choices and should be reported…
- Recommendation: Rephrase to avoid starting a sentence with this transition word, or reduce frequency.


### LOW
#### LOW-01: FALSE_ENTHUSIASM_WORD
- Location: Line 25 (Section: Evaluation Principles > Why Random Splits Fail)
- Evidence: …nctional similarities that can be exploited by sufficiently powerful models.
- Recommendation: Replace with a more precise, neutral descriptor (e.g., “high-capacity”, “expressive”, “high-performing”) unless quoting a source.

#### LOW-02: CODE_BLOCK_PRESENT
- Location: Line 45 (Section: Evaluation Principles > Homology-Aware Splitting > Clustering Tools and Workflows)
- Evidence: Fenced code block from line 45 to 51 (```bash). Consider whether this belongs in flowing prose; guidelines suggest minimizing tutorial-style code blocks.
- Recommendation: Confirm the code block is strictly necessary for pedagogy; otherwise summarize conceptually or move to an appendix/box.

#### LOW-03: CODE_BLOCK_PRESENT
- Location: Line 55 (Section: Cluster nucleotides at 90% identity)
- Evidence: Fenced code block from line 55 to 60 (```bash). Consider whether this belongs in flowing prose; guidelines suggest minimizing tutorial-style code blocks.
- Recommendation: Confirm the code block is strictly necessary for pedagogy; otherwise summarize conceptually or move to an appendix/box.

#### LOW-04: FALSE_ENTHUSIASM_WORD
- Location: Line 88 (Section: Create database and cluster at 30% identity > Splitting by Biological Axis > Splitting by Individual)
- Evidence: …hare genomic segments that can be exploited by sufficiently powerful models. Best practice involves computing kinship coefficien…
- Recommendation: Replace with a more precise, neutral descriptor (e.g., “high-capacity”, “expressive”, “high-performing”) unless quoting a source.

#### LOW-05: FALSE_ENTHUSIASM_WORD
- Location: Line 210 (Section: Create database and cluster at 30% identity > Baseline Selection > Strong Baselines, Not Straw Men)
- Evidence: …naive prior or a deliberately crippled baseline will appear impressive regardless of whether it offers genuine value. Strong basel…
- Recommendation: Replace with a more precise, neutral descriptor (e.g., “high-capacity”, “expressive”, “high-performing”) unless quoting a source.

## Quick Fix Checklist
- [ ] Remove meta-commentary (“This chapter…”, “In this chapter…”, “In this section…”).
- [ ] Audit numeric/statistical claims and add citations where needed.
- [ ] Convert final deliverable to `.md` per output requirements.
- [ ] Confirm code blocks are necessary; otherwise move to appendix or paraphrase conceptually.
- [ ] Reduce sentence-start transitions (e.g., “However,”).
- [ ] Replace vague enthusiasm adjectives (“powerful”, “impressive”, “remarkable”) with precise neutral language.

