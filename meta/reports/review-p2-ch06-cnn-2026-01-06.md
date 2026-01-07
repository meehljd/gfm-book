# Chapter Review: Convolutional Networks (Chapter 6)

Generated: 2026-01-06
File: part_2/p2-ch06-cnn.qmd
Word count: ~4,200
Review mode: Standalone

## Executive Summary

Chapter 6 is a strong chapter that establishes the foundational paradigms of CNNs in genomics before attention mechanisms. The opening is excellent with a memorable hook about DeepSEA discovering JASPAR motifs through gradient descent. Four `[Citation Needed]` markers need resolution (all refer to findings in already-cited papers). The soft landing has minor redundancy in the final sentences.

## Overall Grade
- Content Quality: **A**
- Style Compliance: **A**
- Pedagogical Flow: **A**
- Cross-Chapter Consistency: N/A (standalone review)

---

## Opening Analysis

### Hook Assessment
- [x] Unique (not used elsewhere): Yes
- [x] Contains paradox/tension: Yes ("despite never seeing those motifs during training")
- [x] Concrete specificity in first 100 words: Yes (2015, ENCODE, JASPAR, gradient descent)
- [x] Memorable sentence present: Yes
- [x] No meta-commentary: Yes

**Opening paragraph:**
> In 2015, a **convolutional neural network** trained on ENCODE chromatin data learned to recognize transcription factor binding motifs that matched entries in the JASPAR database, despite never seeing those motifs during training. The network had discovered, through gradient descent on raw sequence, patterns that experimental biologists had spent decades cataloging.

**Memorable sentence:**
> "The network had discovered, through gradient descent on raw sequence, patterns that experimental biologists had spent decades cataloging."

**Assessment:** Excellent opening. Strong paradox, concrete details, memorable phrasing. Sets up the chapter's central themes effectively.

---

## Pedagogical Flow

### Concept Progression
- [x] Concepts introduced before use: Yes
- [x] Logical section progression: Yes (convolutions → DeepSEA → Basset/DanQ → ExPecto → SpliceAI → limitations → recurrence → specialization)
- [x] Appropriate depth for target audience: Yes

### Flow Issues
| Section | Issue | Suggestion |
|---------|-------|------------|
| None identified | — | — |

---

## Section-by-Section Analysis

### Convolutions as Sequence Pattern Detectors
- Opening quality: **Strong** (clinical vignette establishes stakes)
- Stakes established: Yes (familial hypercholesterolemia variant interpretation)
- Forbidden patterns: None

### *DeepSEA*: Regulatory Prediction from Sequence
- Opening quality: **Strong** (rare disease patient scenario)
- Stakes established: Yes ("is this variant pathogenic?")
- Forbidden patterns: None

### Cell-Type Specificity and Regulatory Grammar
- Opening quality: **Adequate**
- Stakes established: Yes (cardiac vs. neural cell-type specificity)
- Forbidden patterns: None

### *ExPecto*: From Chromatin to Expression
- Opening quality: **Strong** (tumor variant clinical question)
- Stakes established: Yes ("which gene? by how much? in which tissues?")
- Forbidden patterns: None

### *SpliceAI*: Clinical-Grade Splicing Prediction
- Opening quality: **Strong** (developmental delay case study with diagnostic delay)
- Stakes established: Yes (systematic blind spot in clinical genomics)
- Forbidden patterns: None

### Receptive Field Ceiling
- Opening quality: **Strong** (BRCA1 enhancer variant clinical case)
- Stakes established: Yes (architectural limitation preventing answer)
- Forbidden patterns: None

### Sequential Approaches and Their Costs
- Opening quality: **Adequate**
- Stakes established: Yes (intuitive solution to receptive field problem)
- Forbidden patterns: None

### Specialization and Its Limits (Soft Landing)
- Opening quality: **Strong**
- Stakes established: Yes (paradigms that persist)
- Forbidden patterns: None

---

## Soft Landing Analysis

### Final Section: "Specialization and Its Limits"
- [x] Tension-based heading (not "Summary"): Yes
- [x] Beat 1 - What established: Present (paradigms, end-to-end learning, multi-task training, in silico mutagenesis)
- [x] Beat 2 - Limitations acknowledged: Present (receptive field limitation)
- [x] Beat 3 - Forward connection: Present (foundation models, attention mechanisms)
- [ ] Memorable final sentence: **Issue** - final sentence repeats previous point
- [x] Max 2-3 forward references: Yes (3 refs: @sec-ch22-confounding, @sec-ch10-fm-principles ×2)

**Final paragraph:**
> Yet specialization retains value even as general-purpose models advance. *SpliceAI* achieves clinical-grade splice site prediction that broader foundation models have not matched. When the prediction target is well-defined, training data abundant, and the relevant context fits within architectural constraints, task-specific models remain competitive with or superior to general-purpose approaches. **This tension between specialized accuracy and general capability defines architectural choices across genomic AI.** For clinical deployment requiring high reliability on specific tasks, specialized architectures may remain preferred. For discovery applications requiring broad coverage across diverse molecular mechanisms, the foundation model paradigm (see @sec-ch10-fm-principles) offers different trade-offs. Attention mechanisms provide the architectural substrate for long-range modeling while inheriting the end-to-end learning principles that convolutional networks established. **The tension between specialized accuracy and general capability reappears throughout this book:** for splice prediction and motif detection where CNNs excel, task-specific architectures remain competitive; for regulatory prediction requiring long-range integration, the foundation model approaches in Part III offer different tradeoffs (@sec-ch10-fm-principles).

**Assessment:** The final two sentences (bolded above) express the same idea twice. The paragraph should end at "established" and delete the final redundant sentence. Also, @sec-ch10-fm-principles appears twice in the soft landing.

---

## Style Violations

### Em-Dashes (must be zero)
| Line | Context | Suggested Fix |
|------|---------|---------------|
| None | — | — |

### Long Sentences (> 40 words)
| Line | Word Count | Location | Assessment |
|------|------------|----------|------------|
| ~88 | 48 words | Basset section | Acceptable - complex technical content |
| ~177 | 54 words | Delta score formula context | Could split but acceptable for mathematical content |
| ~245 | 43 words | Final section | Part of redundant sentence to delete |

### Vague References
| Line | Found | Context | Suggestion |
|------|-------|---------|------------|
| None identified | — | — | — |

### Other Style Issues
| Line | Issue | Suggestion |
|------|-------|------------|
| 107 | Figure caption has unitalicized "Beluga" | Italicize as *Beluga* |

---

## Citation Issues

### [Citation Needed] Markers (4 found)

All four `[Citation Needed]` markers refer to findings contained within papers already cited in the chapter. The citations exist but need to be placed directly after the claims:

| Line | Claim | Source Paper | Fix |
|------|-------|--------------|-----|
| 71 | DeepSEA outperformed gkm-SVM | zhou_deepsea_2015 | Add citation after claim |
| 89 | Model-prioritized variants showed higher experimental confirmation rates | kelley_basset_2016 | Add citation after claim |
| 125 | ExPecto correctly predicted 92% of GTEx eQTLs; reporter assay validation | zhou_expecto_2018 | Add citation after claim |
| 186 | ~9% of pathogenic de novo mutations in ID from cryptic splicing | jaganathan_spliceai_2019 | Add citation after claim |

**Resolution:** These are NOT missing citations - they are attribution gaps. The cited papers contain these exact findings. Simply move/add the existing citations to the specific sentences.

---

## Specific Suggestions

### High Priority
1. **Line 71:** Replace `*[Citation Needed]*` with `[@zhou_deepsea_2015]` (finding is in the DeepSEA paper's comparison with gkm-SVM)

2. **Line 89:** Replace `*[Citation Needed]*` with `[@kelley_basset_2016]` (PICS analysis is in the original Basset paper)

3. **Line 125:** Replace `*[Citation Needed]*` with `[@zhou_expecto_2018]` (92% GTEx correlation and reporter assay validation are in the ExPecto paper)

4. **Line 186:** Replace `*[Citation Needed]*` with `[@jaganathan_spliceai_2019]` (the 9% figure comes from the SpliceAI paper's analysis of DDD cohort)

5. **Line 245:** Delete final redundant sentence starting "The tension between specialized accuracy..." - it repeats the point made three sentences earlier

### Medium Priority
1. **Line 107 (figure caption):** Italicize "Beluga" as "*Beluga*"

### Low Priority
1. Consider splitting the 54-word sentence around line 177 for readability

---

## Strengths
- Excellent opening hook with memorable phrasing
- Strong clinical vignettes establish stakes for each major section
- Clear progression from DeepSEA through limitations to architectural transitions
- Well-integrated cross-references (@sec-ch07-attention, @sec-ch13-regulatory, etc.)
- Accurate technical content on CNN architectures and their limitations
- Honest acknowledgment of receptive field ceiling
- Good balance between mathematical detail and intuition
- The MaxEntScan reference provides important historical context for SpliceAI's improvement

---

## Paper Log Status

The chapter's paper review log (`meta/paper-reviews/logs/ch06-paper-review-log.tsv`) shows 10 papers tracked:
- 5 flagged as placeholders needing DOI/URL (cho_learning_2014, hochreiter_long_1997, kelley_basset_2016, quang_danq_2016)
- 5 fully reviewed (jaganathan_spliceai_2019, kagda_encode_2025, kundaje_roadmap_2015, yeo_maxentscan_2004, zhou_deepsea_2015, zhou_expecto_2018)

**No new papers needed** - all [Citation Needed] claims are covered by existing citations.
