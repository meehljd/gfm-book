# Instructions Compliance Report: Single-Cell Models

**Source file:** `p4-ch16-single-cell.qmd`  
**Reviewed against:** `claude-project-instructions.md`  
**Line count:** 236  

## Executive Summary

- **Blockers:** 2
- **Major issues:** 0
- **Minor issues:** 4

## Non-Negotiables Check

| Requirement | Status | Evidence |
|---|---|---|
| ZERO em-dashes (—) | PASS | 0 occurrence(s) |
| ZERO bullet points in prose | PASS | 0 markdown list item(s) detected |
| ZERO meta-commentary | FAIL | 1 flagged line(s) |
| Lead with Why | PASS | Opening starts with problem framing and stakes. |

## Issues

| Severity   | Rule                                           | Location                                                                                          | Evidence                                                                                                                                                                                                                                       | Recommendation                                                                                    |
|:-----------|:-----------------------------------------------|:--------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|
| Blocker    | Output format must be markdown (.md), not .qmd | L1 (Single-Cell Models)                                                                           | <code>p4-ch16-single-cell.qmd</code>                                                                                                                                                                                                           | Convert the chapter deliverable to a .md file (do not output .qmd).                               |
| Blocker    | ZERO meta-commentary / structural telegraphing | L7 (Single-Cell Models)                                                                           | <code>This chapter examines foundation models for single-cell and epigenomic data across three interconnected scales. Cellular language models tre ... e **transfer learning** successes that protein and DNA models have demonstrated.</code> | Remove self-referential framing; state the content directly without narrating structure.          |
| Minor      | Avoid anthropomorphization                     | L110 (Single-Cell Models > Perturbation Response Prediction > The *In Silico* Experiment Promise) | <code>One of the most compelling applications of cellular foundation models is predicting how cells will respond to perturbations. If a model trul ... or cancer therapy, and suggest targets for diseases without known interventions.</code> | Rephrase in operational terms (predict, represent, encode, optimize) rather than cognition verbs. |
| Minor      | Avoid anthropomorphization                     | L112 (Single-Cell Models > Perturbation Response Prediction > The *In Silico* Experiment Promise) | <code>The perturbation prediction task requires more than memorizing co-expression patterns. The model must understand directional relationships: ... same perturbation may have different effects in different cell types or states.</code>   | Rephrase in operational terms (predict, represent, encode, optimize) rather than cognition verbs. |
| Minor      | Avoid false enthusiasm / marketing tone        | L136 (Single-Cell Models > Perturbation Response Prediction > Limitations of Current Approaches)  | <code>Despite promising results, current perturbation prediction models face fundamental limitations. Most training data come from immortalized ce ... es across perturbed cells rather than the heterogeneity of individual responses.</code> | Use neutral academic phrasing; attribute assessments to sources if needed.                        |
| Minor      | Avoid false enthusiasm / marketing tone        | L236 (Single-Cell Models > From Sequence to State)                                                | <code>The ultimate goal extends beyond prediction to explanation: models that identify the regulatory mechanisms underlying cellular state, the va ... onnecting the patterns that models learn to the mechanisms that biology employs.</code> | Use neutral academic phrasing; attribute assessments to sources if needed.                        |

## Notes for Downstream LLM

- Treat **Blockers** as required edits for this chapter to be instruction-compliant.
- Many issues are mechanical and can be fixed by systematic search-and-replace (for example, citation-key backticks).
