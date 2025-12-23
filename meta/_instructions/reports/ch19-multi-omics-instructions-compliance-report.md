# Instructions Compliance Report: **Multi-Omics** Integration

**Source file:** `p4-ch19-multi-omics.qmd`  
**Reviewed against:** `claude-project-instructions.md`  
**Line count:** 303  

## Executive Summary

- **Blockers:** 2
- **Major issues:** 0
- **Minor issues:** 0

## Non-Negotiables Check

| Requirement | Status | Evidence |
|---|---|---|
| ZERO em-dashes (—) | FAIL | 3 occurrence(s) |
| ZERO bullet points in prose | PASS | 0 markdown list item(s) detected |
| ZERO meta-commentary | PASS | 0 flagged line(s) |
| Lead with Why | PASS | Opening starts with problem framing and stakes. |

## Issues

| Severity   | Rule                                           | Location                                                                                                                             | Evidence                                                                                                                                                                                                                                      | Recommendation                                                                      |
|:-----------|:-----------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| Blocker    | Output format must be markdown (.md), not .qmd | L1 (**Multi-Omics** Integration)                                                                                                     | <code>p4-ch19-multi-omics.qmd</code>                                                                                                                                                                                                          | Convert the chapter deliverable to a .md file (do not output .qmd).                 |
| Blocker    | ZERO em-dashes (—)                             | L181 (**Multi-Omics** Integration > Clinical Integration: EHR, Imaging, and Molecular Data > Multi-Modal Clinical Prediction Models) | <code>[High] Patient-level integration. Panel A (Data Modalities): EHR (diagnoses, procedures, medications, labs—longitudinal), imaging (CT, MRI, ... actical challenges callout: batch effects, temporal alignment, cost constraints.</code> | Replace em-dash with parentheses, commas, colon/semicolon, or split into sentences. |

## Notes for Downstream LLM

- Treat **Blockers** as required edits for this chapter to be instruction-compliant.
- Many issues are mechanical and can be fixed by systematic search-and-replace (for example, citation-key backticks).
