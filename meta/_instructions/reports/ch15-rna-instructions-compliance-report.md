# Instructions Compliance Report: RNA Structure and Function

**Source file:** `p4-ch15-rna.qmd`  
**Reviewed against:** `claude-project-instructions.md`  
**Line count:** 275  

## Executive Summary

- **Blockers:** 4
- **Major issues:** 0
- **Minor issues:** 2

## Non-Negotiables Check

| Requirement | Status | Evidence |
|---|---|---|
| ZERO em-dashes (—) | FAIL | 2 occurrence(s) |
| ZERO bullet points in prose | PASS | 0 markdown list item(s) detected |
| ZERO meta-commentary | FAIL | 2 flagged line(s) |
| Lead with Why | PASS | Opening starts with problem framing and stakes. |

## Issues

| Severity   | Rule                                                          | Location                                                                                                                             | Evidence                                                                                                                                                                                                                                       | Recommendation                                                                           |
|:-----------|:--------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| Blocker    | Output format must be markdown (.md), not .qmd                | L1 (RNA Structure and Function)                                                                                                      | <code>p4-ch15-rna.qmd</code>                                                                                                                                                                                                                   | Convert the chapter deliverable to a .md file (do not output .qmd).                      |
| Blocker    | ZERO meta-commentary / structural telegraphing                | L7 (RNA Structure and Function)                                                                                                      | <code>This chapter examines RNA-specific modeling as a bridge between the sequence-level foundation models of Part 3 and the cellular and systems ... ation, while confronting the data limitations that constrain current approaches.</code>  | Remove self-referential framing; state the content directly without narrating structure. |
| Blocker    | ZERO meta-commentary / structural telegraphing                | L14 (RNA Structure and Function > RNA as Molecule Versus Transcriptome Readout)                                                      | <code>Models that predict transcriptomic signals from DNA sequence (Enformer, Borzoi, and related architectures covered in @sec-regulatory) operat ... NA sequence itself and whose outputs concern RNA structure, function, or design.</code> | Remove self-referential framing; state the content directly without narrating structure. |
| Blocker    | ZERO em-dashes (—)                                            | L32 (RNA Structure and Function > Why Secondary Structure Creates a Distinct Modeling Challenge > The Flat Energy Landscape Problem) | <code>[Essential] Two-panel comparison. Panel A (Protein Folding): 3D surface with deep funnel topology; clear global minimum (native state); stee ... RNA sequence adopting different structures; riboswitch example; RNA thermometer.</code> | Replace em-dash with parentheses, commas, colon/semicolon, or split into sentences.      |
| Minor      | Avoid false enthusiasm / marketing tone                       | L72 (RNA Structure and Function > Classical Approaches to Structure Prediction > Comparative and Covariation Methods)                | <code>Comparative methods are powerful but require multiple sequence alignments of homologous RNAs. Novel RNAs, rapidly evolving regulatory elemen ... ve diverged in function or that adopt condition-specific alternative structures.</code> | Use neutral academic phrasing; attribute assessments to sources if needed.               |
| Minor      | Avoid transition clichés as sentence starters (use sparingly) | L159 (RNA Structure and Function > Codon-Level Models for Coding RNA > What Codon Models Add)                                        | <code>However, codon models typically ignore mRNA secondary structure and modifications. Local structure affects ribosome access and translation r ... ure than the parallel integration of sequence and structure in protein modeling.</code> | Revise to a more specific transition or integrate contrast/addition mid-sentence.        |

## Notes for Downstream LLM

- Treat **Blockers** as required edits for this chapter to be instruction-compliant.
- Many issues are mechanical and can be fixed by systematic search-and-replace (for example, citation-key backticks).
