# Instructions Compliance Report: Graph and Network Models

**Source file:** `p4-ch18-networks.qmd`  
**Reviewed against:** `claude-project-instructions.md`  
**Line count:** 311  

## Executive Summary

- **Blockers:** 2
- **Major issues:** 0
- **Minor issues:** 3

## Non-Negotiables Check

| Requirement | Status | Evidence |
|---|---|---|
| ZERO em-dashes (—) | PASS | 0 occurrence(s) |
| ZERO bullet points in prose | PASS | 0 markdown list item(s) detected |
| ZERO meta-commentary | FAIL | 1 flagged line(s) |
| Lead with Why | PASS | Opening starts with problem framing and stakes. |

## Issues

| Severity   | Rule                                           | Location                                                                                                     | Evidence                                                                                                                                                                                                                                       | Recommendation                                                                                    |
|:-----------|:-----------------------------------------------|:-------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------|
| Blocker    | Output format must be markdown (.md), not .qmd | L1 (Graph and Network Models)                                                                                | <code>p4-ch18-networks.qmd</code>                                                                                                                                                                                                              | Convert the chapter deliverable to a .md file (do not output .qmd).                               |
| Blocker    | ZERO meta-commentary / structural telegraphing | L7 (Graph and Network Models)                                                                                | <code>The practical implications are substantial. Disease gene prioritization leverages the observation that genes causing similar diseases cluste ... undation model representations with graph structure across genomic applications.</code> | Remove self-referential framing; state the content directly without narrating structure.          |
| Minor      | Avoid false enthusiasm / marketing tone        | L3 (Graph and Network Models)                                                                                | <code>Graph neural networks are not alternatives to foundation models; they are consumers of them. The foundation models explored in earlier chapt ... cture. The combination yields capabilities that neither approach achieves alone.</code> | Use neutral academic phrasing; attribute assessments to sources if needed.                        |
| Minor      | Avoid anthropomorphization                     | L14 (Graph and Network Models > Biological Networks and Data Resources > The Landscape of Biological Graphs) | <code>Before examining **graph neural network** architectures, it is essential to understand what biological networks exist and where they come fr ... ases inherent in network construction propagate through all downstream analyses.</code> | Rephrase in operational terms (predict, represent, encode, optimize) rather than cognition verbs. |
| Minor      | Avoid false enthusiasm / marketing tone        | L207 (Graph and Network Models > Applications > Knowledge Graph Reasoning and Drug Repurposing)              | <code>The integration of knowledge graphs with foundation models exemplifies the broader theme of this chapter: relational reasoning over rich ent ... op reasoning across the full landscape of biological and clinical relationships.</code> | Use neutral academic phrasing; attribute assessments to sources if needed.                        |

## Notes for Downstream LLM

- Treat **Blockers** as required edits for this chapter to be instruction-compliant.
- Many issues are mechanical and can be fixed by systematic search-and-replace (for example, citation-key backticks).
