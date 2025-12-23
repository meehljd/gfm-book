# Instruction Compliance Report: **Uncertainty Quantification**
## Source
- File: `p5-ch23-uncertainty.qmd`
- Chapter title: **Uncertainty Quantification**
- Total lines: 405

## Summary of Issues
- **CRITICAL**: 4
- **HIGH**: 1
- **MEDIUM**: 22
- **LOW**: 0

## Issues

### CRITICAL
#### CRITICAL-01: OUTPUT_FORMAT_QMD
- Location: Line 1 (Section: **Uncertainty Quantification**)
- Evidence: Source file is `p5-ch23-uncertainty.qmd` (Quarto .qmd), but project instructions require delivering chapter prose as `.md`.
- Recommendation: Convert final deliverable to `.md` (no YAML frontmatter) per project output requirements.

#### CRITICAL-02: META_COMMENTARY
- Location: Line 7 (Section: **Uncertainty Quantification**)
- Evidence: This chapter develops the concepts and methods for quantifying, calibrat…
- Recommendation: Remove self-referential framing (e.g., “This chapter…”, “In this chapter…”). State the substantive claims directly.

#### CRITICAL-03: META_COMMENTARY
- Location: Line 401 (Section: **Uncertainty Quantification** > Necessary but Insufficient)
- Evidence: …alse negatives (missed diagnoses). The methods developed in this chapter, from temperature scaling through conformal prediction to o…
- Recommendation: Remove self-referential framing (e.g., “This chapter…”, “In this chapter…”). State the substantive claims directly.

#### CRITICAL-04: META_COMMENTARY
- Location: Line 401 (Section: **Uncertainty Quantification** > Necessary but Insufficient)
- Evidence: …d false negatives (missed diagnoses). The methods developed in this chapter, from temperature scaling through conformal prediction to o…
- Recommendation: Remove self-referential framing (e.g., “This chapter…”, “In this chapter…”). State the substantive claims directly.


### HIGH
#### HIGH-01: ORDINAL_SCAFFOLDING
- Location: Line 230 (Section: **Uncertainty Quantification** > **Conformal Prediction**: Distribution-Free Guarantees > Split Conformal Prediction)
- Evidence: The most practical conformal method, split conformal prediction, proceeds in five steps. First, split available labeled data into a proper training set and a calibration set. Second, train the model on the training set only. Third, compute non-conformity scores on the calibration set, where higher scores indicate poorer fit between the model's prediction and the true label. Fourth, find the threshold $q$ at the $(1-\alpha)(1+1/n)$ quantile of calibration scores, where $n$ is the calibration set size. Fifth, at test time, include in the prediction set all labels whose non-conformity score falls below $q$.
- Recommendation: Remove ordinal scaffolding (“First…, Second…”) and rewrite as prose without enumerative crutches (or use a table/callout if appropriate).


### MEDIUM
#### MEDIUM-01: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 3 (Section: **Uncertainty Quantification**)
- Evidence: A pathogenicity score of 0.73 means nothing unless we know what 0.73 means. If the model is well-calibrated, approximately 73% of variants receiving this score are truly pathogenic, and a clinician can weigh this probability against the costs of further testing. If the model is miscalibrated, the true pathogenicity rate among variants scored at 0.73 could be 40% or 95%, and the nominal probability provides no reliable basis for decision-making. The distinction is not between accurate and inaccurate models but between models that know what they know and models that do not. A miscalibrated model with high average accuracy can be more dangerous than a calibrated model with lower accuracy, because the miscalibrated model provides false confidence that leads to systematically wrong decisions.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-02: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 18 (Section: **Uncertainty Quantification** > Types of Uncertainty in Genomic Prediction > Why Uncertainty Matters)
- Evidence: Decision theory formalizes this intuition. The expected value of a clinical action depends on the probability of each outcome weighted by its utility. When a model reports 0.73 probability of pathogenicity, downstream decision-making implicitly assumes this probability is accurate. If the true probability is 0.50, actions optimized for 0.73 will systematically err. Uncertainty quantification ensures that the probabilities entering clinical decisions reflect genuine knowledge rather than artifacts of model architecture or training procedure.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-03: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 50 (Section: **Uncertainty Quantification** > Types of Uncertainty in Genomic Prediction > Decomposing Total Uncertainty)
- Evidence: The law of total variance provides a mathematical framework for decomposition. Total variance in predictions equals the sum of variance due to model uncertainty (epistemic) and variance inherent in the data-generating process (aleatoric). In practice, ensemble methods approximate epistemic uncertainty through disagreement between members: if five independently trained models produce predictions of 0.65, 0.68, 0.70, 0.72, and 0.75, the spread reflects epistemic uncertainty, while the residual variance within each model's predictions reflects aleatoric uncertainty. Heteroscedastic neural networks, which output both a predicted mean and a predicted variance, can estimate aleatoric uncertainty by learning input-dependent noise levels.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-04: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 66 (Section: **Uncertainty Quantification** > Calibration: Do Confidence Scores Mean What They Say?)
- Evidence: [Essential] Four-panel figure. Panel A (Perfect calibration): Reliability diagram on diagonal; "Predictions match reality." Panel B (Overconfident): Points below diagonal; model predicts 0.9, true frequency 0.6; common for DNNs; "Dangerous for clinical use." Panel C (Underconfident): Points above diagonal; "May miss actionable variants." Panel D (Miscalibration by subgroup): Two curves (European, African); one calibrated, one poor; "Aggregate can mask disparities." Annotations: expected calibration error (ECE), prediction histograms, "Calibration ≠ discrimination."
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-05: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 71 (Section: **Uncertainty Quantification** > Calibration: Do Confidence Scores Mean What They Say? > The Calibration Problem)
- Evidence: AlphaMissense outputs a continuous score between 0 and 1 for each possible missense variant in the human proteome. When it reports 0.85 for a particular variant, what does this number mean? If the model is calibrated, collecting all variants scored near 0.85 and checking their true clinical status should reveal that approximately 85% are pathogenic. Perfect calibration means that predicted probabilities match observed frequencies across the entire range of model outputs: among variants scored at 0.30, roughly 30% should be pathogenic; among variants scored at 0.95, roughly 95% should be pathogenic. This alignment between stated confidence and empirical accuracy is calibration, and most foundation models fail to achieve it.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-06: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 77 (Section: **Uncertainty Quantification** > Calibration: Do Confidence Scores Mean What They Say? > The Calibration Problem)
- Evidence: Calibration and discrimination are distinct properties. A model can achieve perfect area under the receiver operating characteristic curve (**AUROC**), correctly ranking all positive examples above all negative examples, while being arbitrarily miscalibrated. If a classifier assigns probability 0.99 to all positive examples and 0.98 to all negative examples, it ranks perfectly but provides useless probability estimates. Conversely, a calibrated model that assigns 0.51 to positives and 0.49 to negatives would be calibrated but nearly useless for discrimination. Clinical applications typically require both: accurate ranking to identify high-risk variants and accurate probabilities to inform decision-making.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-07: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 132 (Section: **Uncertainty Quantification** > Post-Hoc Calibration Methods > Temperature Scaling)
- Evidence: where $z_i$ are the logits (pre-softmax outputs) and $\hat{p}_i$ are the calibrated probabilities. When $T > 1$, the distribution becomes softer (more uniform), reducing overconfidence. When $T < 1$, the distribution becomes sharper, increasing confidence. The optimal temperature is learned by minimizing negative log-likelihood on a held-out calibration set, typically yielding $T$ between 1.5 and 3 for overconfident deep networks.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-08: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 217 (Section: **Uncertainty Quantification** > **Conformal Prediction**: Distribution-Free Guarantees)
- Evidence: [High] Workflow with examples. Steps: (1) Calibration: Score variants on held-out set; (2) Threshold: Find threshold for 90% coverage; (3) Prediction sets: Include classes above threshold. Example outputs: High confidence {Pathogenic}, moderate {Pathogenic, VUS}, low {P, VUS, B}, abstention {}. Key properties: Coverage guarantee (≥90% marginal); set size conveys uncertainty; no probability interpretation needed. Visualization: Score distributions; threshold line; set sizes. Limitation: Marginal not conditional coverage.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-09: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 224 (Section: **Uncertainty Quantification** > **Conformal Prediction**: Distribution-Free Guarantees > The Conformal Prediction Framework)
- Evidence: Conformal prediction offers something stronger: finite-sample coverage guarantees that hold under minimal assumptions. Instead of outputting a point prediction, conformal methods produce a prediction set guaranteed to contain the true label with probability at least $1 - \alpha$, where $\alpha$ is a user-specified error rate. If we request 90% coverage ($\alpha = 0.10$), the prediction set will contain the true label at least 90% of the time, regardless of the model's accuracy or calibration. This guarantee requires only that calibration and test examples are exchangeable (a condition weaker than independent and identically distributed), making conformal prediction robust to model misspecification.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-10: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 240 (Section: **Uncertainty Quantification** > **Conformal Prediction**: Distribution-Free Guarantees > Conformal Prediction for **Variant Effect Prediction**)
- Evidence: Adaptive set sizes convey uncertainty naturally. Confident predictions yield small sets ({pathogenic} alone), while uncertain predictions yield larger sets ({pathogenic, benign}). The set size itself communicates the model's confidence without requiring users to interpret numerical probabilities. A clinician seeing {pathogenic, benign} knows immediately that the model cannot distinguish between these possibilities, whereas a score of 0.55 might be misinterpreted as mild confidence in pathogenicity.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-11: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 248 (Section: **Uncertainty Quantification** > **Conformal Prediction**: Distribution-Free Guarantees > Limitations and Practical Considerations)
- Evidence: Conformal guarantees are marginal rather than conditional. The coverage guarantee holds on average across all test examples, not for each individual example. A model might achieve exact 90% coverage overall while dramatically undercovering some subgroups and overcovering others. Subgroup-conditional coverage requires additional assumptions or methods like stratified conformal prediction.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-12: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 307 (Section: **Uncertainty Quantification** > Selective Prediction and Abstention)
- Evidence: [Enhancing] Accuracy-coverage tradeoff. Main plot: Coverage (x) vs Accuracy (y); curve rising as coverage decreases (more selective = more accurate). Operating point selection: Clinical applications need different tradeoffs. Reject option: High uncertainty → abstain. Example: 90% coverage with 85% accuracy vs 70% coverage with 95% accuracy. Connection to clinical workflow: Rejected variants → expert review.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-13: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 312 (Section: **Uncertainty Quantification** > Selective Prediction and Abstention > When to Abstain)
- Evidence: A variant effect predictor achieving 95% accuracy overall provides more clinical value if it can identify which predictions are reliable. Selective prediction allows models to abstain on difficult cases, concentrating predictions on inputs where confidence is warranted. The trade-off between coverage (fraction of inputs receiving predictions) and accuracy (correctness among predictions made) defines the selective prediction problem.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-14: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 314 (Section: **Uncertainty Quantification** > Selective Prediction and Abstention > When to Abstain)
- Evidence: The coverage-accuracy trade-off reflects a fundamental tension. At 100% coverage, the model predicts on all inputs and achieves its baseline accuracy. As coverage decreases (more abstention), accuracy among predictions made typically increases because the model abstains on its most uncertain cases. The shape of this trade-off curve characterizes the model's ability to identify reliable predictions.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-15: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 332 (Section: **Uncertainty Quantification** > Selective Prediction and Abstention > Evaluating Selective Prediction)
- Evidence: Selective accuracy at fixed coverage specifies a coverage level (e.g., 80%) and reports accuracy among predictions made at that coverage. This metric directly answers practical questions: "If we let the model predict on its 80% most confident cases, how accurate will it be?"
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-16: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 334 (Section: **Uncertainty Quantification** > Selective Prediction and Abstention > Evaluating Selective Prediction)
- Evidence: Comparison across methods requires matched coverage levels. A method that achieves 99% accuracy at 50% coverage and 95% accuracy at 90% coverage may be preferable to a method achieving 97% accuracy at both levels, depending on operational requirements. Reporting full risk-coverage curves enables stakeholders to select operating points appropriate to their cost structures.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-17: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 363 (Section: **Uncertainty Quantification** > Uncertainty for Specific Genomic Tasks > Uncertainty Across Populations)
- Evidence: Transparent reporting of population-stratified uncertainty metrics enables informed decisions about model deployment. If a model abstains on 30% of variants in one population but only 10% in another, users can make informed choices about supplementary analyses for the higher-abstention population. Clinical laboratories might establish ancestry-specific thresholds for automated reporting versus expert review. Research applications might weight predictions by ancestry-specific confidence when aggregating across diverse cohorts. Ignoring these differences risks providing lower-quality predictions to already under-served populations while presenting a false appearance of uniform reliability, compounding existing disparities in genomic medicine.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-18: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 370 (Section: **Uncertainty Quantification** > Communicating Uncertainty to End Users > The Communication Challenge)
- Evidence: A pathogenicity score of $0.73 \pm 0.15$ may be statistically accurate but nearly useless to a clinician deciding whether to order confirmatory testing. The gap between statistical uncertainty and decision-relevant communication presents a persistent challenge for genomic AI deployment. Different users reason differently about probability and risk; effective communication requires understanding these differences.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-19: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 372 (Section: **Uncertainty Quantification** > Communicating Uncertainty to End Users > The Communication Challenge)
- Evidence: Cognitive biases complicate probability interpretation. Humans tend toward overconfidence in point estimates, treating 0.73 as more certain than warranted. Prediction intervals are frequently misunderstood: a 90% **confidence interval** does not mean the true value has a 90% chance of being in that specific interval (a Bayesian interpretation) but rather that 90% of such intervals would contain the true value (a frequentist interpretation). Base rate neglect leads users to interpret variant-level pathogenicity predictions without accounting for prior probability based on clinical presentation, family history, and phenotypic specificity.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-20: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 380 (Section: **Uncertainty Quantification** > Communicating Uncertainty to End Users > Categorical Reporting)
- Evidence: Uncertainty within categories can be conveyed through confidence qualifiers or numerical confidence scores attached to categorical calls. A "likely pathogenic" call with 95% confidence differs meaningfully from one with 60% confidence, even though both receive the same categorical label. Two-dimensional reporting combining category and confidence enables more nuanced interpretation without abandoning the categorical framework that clinicians expect.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-21: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 388 (Section: **Uncertainty Quantification** > Communicating Uncertainty to End Users > Visual Communication)
- Evidence: Risk ladders place the prediction in context by showing where it falls relative to other risks of varying magnitude. A variant with 0.73 probability of pathogenicity can be placed alongside risks from other genetic conditions, environmental exposures, or common medical procedures, enabling intuitive comparison.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-22: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 394 (Section: **Uncertainty Quantification** > Communicating Uncertainty to End Users > Decision-Theoretic Framing)
- Evidence: Rather than communicating probability alone, decision-theoretic framing presents expected outcomes under different actions. Instead of "this variant has 73% probability of being pathogenic," the report might state "if we assume this variant is pathogenic and proceed with surveillance, the expected outcomes are X; if we assume it is benign and decline surveillance, the expected outcomes are Y."
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

## Quick Fix Checklist
- [ ] Eliminate list-style scaffolding (bullets, numbered lists, “First/Second/Third” ordinals) in flowing prose.
- [ ] Remove meta-commentary (“This chapter…”, “In this chapter…”, “In this section…”).
- [ ] Audit numeric/statistical claims and add citations where needed.
- [ ] Convert final deliverable to `.md` per output requirements.

