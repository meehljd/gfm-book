# Instructions Compliance Report: 3D Genome Organization

**Source file:** `p4-ch17-3d-genome.qmd`  
**Reviewed against:** `claude-project-instructions.md`  
**Line count:** 158  

## Executive Summary

- **Blockers:** 2
- **Major issues:** 0
- **Minor issues:** 1

## Non-Negotiables Check

| Requirement | Status | Evidence |
|---|---|---|
| ZERO em-dashes (—) | PASS | 0 occurrence(s) |
| ZERO bullet points in prose | PASS | 0 markdown list item(s) detected |
| ZERO meta-commentary | FAIL | 1 flagged line(s) |
| Lead with Why | PASS | Opening starts with problem framing and stakes. |

## Issues

| Severity   | Rule                                           | Location                                                        | Evidence                                                                                                                                                                                                                                       | Recommendation                                                                           |
|:-----------|:-----------------------------------------------|:----------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| Blocker    | Output format must be markdown (.md), not .qmd | L1 (3D Genome Organization)                                     | <code>p4-ch17-3d-genome.qmd</code>                                                                                                                                                                                                             | Convert the chapter deliverable to a .md file (do not output .qmd).                      |
| Blocker    | ZERO meta-commentary / structural telegraphing | L19 (3D Genome Organization)                                    | <code>This chapter examines how the genome folds, what determines that folding, and how computational models predict 3D structure from sequence. W ... latory models: what does spatial context add that sequence alone cannot provide?</code> | Remove self-referential framing; state the content directly without narrating structure. |
| Minor      | Avoid false enthusiasm / marketing tone        | L30 (3D Genome Organization > Chromatin Organization Hierarchy) | <code>Below the megabase scale of compartments, the genome organizes into topologically associating domains, or TADs: sub-megabase regions (median ... causing brachydactyly and other limb malformations [@lupiañez_disruptions_2015].</code> | Use neutral academic phrasing; attribute assessments to sources if needed.               |

## Notes for Downstream LLM

- Treat **Blockers** as required edits for this chapter to be instruction-compliant.
- Many issues are mechanical and can be fixed by systematic search-and-replace (for example, citation-key backticks).
