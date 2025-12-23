# Instruction Compliance Report: **Interpretability**
## Source
- File: `p5-ch24-interpretability.qmd`
- Chapter title: **Interpretability**
- Total lines: 255

## Summary of Issues
- **CRITICAL**: 2
- **HIGH**: 1
- **MEDIUM**: 2
- **LOW**: 0

## Issues

### CRITICAL
#### CRITICAL-01: OUTPUT_FORMAT_QMD
- Location: Line 1 (Section: **Interpretability**)
- Evidence: Source file is `p5-ch24-interpretability.qmd` (Quarto .qmd), but project instructions require delivering chapter prose as `.md`.
- Recommendation: Convert final deliverable to `.md` (no YAML frontmatter) per project output requirements.

#### CRITICAL-02: META_COMMENTARY
- Location: Line 7 (Section: **Interpretability**)
- Evidence: This chapter examines methods for understanding what genomic foundation…
- Recommendation: Remove self-referential framing (e.g., “This chapter…”, “In this chapter…”). State the substantive claims directly.


### HIGH
#### HIGH-01: NO_CITATIONS_DETECTED
- Location: Line 1 (Section: **Interpretability**)
- Evidence: No citation keys of the form [@citekey] or @citekey were detected in this chapter.
- Recommendation: Add citations for technical claims (performance numbers, dataset sizes, benchmark results, historical facts) using the project’s citation style.


### MEDIUM
#### MEDIUM-01: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 35 (Section: **Interpretability** > Attribution Methods and Input Importance > *In Silico* Mutagenesis)
- Evidence: ISM provides true **counterfactual** information rather than approximations. When ISM shows that mutating position 47 from A to G reduces the predicted accessibility by 0.3 log-fold, that is a direct observation about model behavior, not an estimate derived from gradients or attention weights. This directness makes ISM the gold standard for faithfulness: if ISM identifies a position as important, perturbing that position genuinely changes the output.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

#### MEDIUM-02: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 232 (Section: **Interpretability** > Interpretability in Clinical Variant Assessment)
- Evidence: [Enhancing] Clinical workflow integration. ACMG evidence framework: *PP3* (computational supports pathogenicity), *BP4* (supports benign). Evidence strength depends on interpretability: Weak (score only, 0.85, no mechanism, limited ACMG weight); Moderate (score + attribution: disrupts splice site; SpliceAI supports; can evaluate against transcript data); Strong (score + validated mechanism: disrupts CTCF binding; ChIP confirms; 3D genome shows contact; minigene assay confirms). Clinical report elements: Annotation, score with uncertainty, mechanistic hypothesis, supporting/conflicting evidence, recommended follow-up.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.

## Quick Fix Checklist
- [ ] Remove meta-commentary (“This chapter…”, “In this chapter…”, “In this section…”).
- [ ] Audit numeric/statistical claims and add citations where needed.
- [ ] Convert final deliverable to `.md` per output requirements.

