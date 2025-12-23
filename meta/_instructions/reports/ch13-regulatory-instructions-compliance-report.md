# Instructions Compliance Report: Regulatory Models

**Source file:** `p3-ch13-regulatory.qmd`  
**Reviewed against:** `claude-project-instructions.md`  
**Line count:** 227  

## Executive Summary

- **Blockers:** 4
- **Major issues:** 7
- **Minor issues:** 1

## Non-Negotiables Check

| Requirement | Status | Evidence |
|---|---|---|
| ZERO em-dashes (—) | FAIL | 2 occurrence(s) |
| ZERO bullet points in prose | PASS | 0 markdown list item(s) detected |
| ZERO meta-commentary | FAIL | 1 flagged line(s) |
| Lead with Why | PASS | Opening starts with problem framing and stakes. |

## Issues

| Severity   | Rule                                                             | Location                                                                                              | Evidence                                                                                                                                                                                                                                            | Recommendation                                                                                            |
|:-----------|:-----------------------------------------------------------------|:------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------|
| Blocker    | Output format must be markdown (.md), not .qmd                   | L1 (Regulatory Models)                                                                                | <code>p3-ch13-regulatory.qmd</code>                                                                                                                                                                                                                 | Convert the chapter deliverable to a .md file (do not output .qmd).                                       |
| Blocker    | ZERO meta-commentary / structural telegraphing                   | L7 (Regulatory Models)                                                                                | <code>Hybrid architectures resolve this tension by combining the strengths of both paradigms. A convolutional front-end efficiently extracts local ... g and assessing what these models reveal about the grammar of gene *regulation*.</code>      | Remove self-referential framing; state the content directly without narrating structure.                  |
| Blocker    | ZERO em-dashes (—)                                               | L52 (Regulatory Models > *Enformer*: Attention Meets Regulatory Genomics > Architecture)              | <code>[Essential] Detailed three-stage architecture. Stage 1 (Convolutional Stem): 200kb one-hot input → conv blocks with residual connections → p ... representations.&quot; Inset: Why Hybrid Works—quadratic on 1,500 vs 200,000 tokens.</code>  | Replace em-dash with parentheses, commas, colon/semicolon, or split into sentences.                       |
| Blocker    | ZERO em-dashes (—)                                               | L76 (Regulatory Models > *Enformer*: Attention Meets Regulatory Genomics > Variant Effect Prediction) | <code>[High] Workflow diagram. Step 1: Variant position → extract 200kb window centered; reference and alternative versions. Step 2: Parallel forw ... ion inset: Correlation with GTEx eQTLs; performance on distal variants (50+ kb).</code>      | Replace em-dash with parentheses, commas, colon/semicolon, or split into sentences.                       |
| Major      | Citation key formatting: avoid backticks inside [@...] citations | L14 (Regulatory Models > The Long-Range Regulation Problem)                                           | <code>Short-context models face an information-theoretic barrier in this setting. A model with a 2 kilobase **receptive field** cannot distinguish ... to propagate information across hundreds of kilobases without impractical depth.</code>      | Use standard citation syntax like [@avsec_enformer_2021] or in-prose 'Avsec et al. @avsec_enformer_2021'. |
| Major      | Citation key formatting: avoid @`...` forms                      | L16 (Regulatory Models > The Long-Range Regulation Problem)                                           | <code>The scale of the problem becomes concrete when examining enhancer-promoter distances in the human genome. Median enhancer-promoter distances ... span these distances cannot fully capture the regulatory grammar of the genome.</code>       | Remove backticks around citation keys.                                                                    |
| Major      | Citation key formatting: avoid backticks inside [@...] citations | L35 (Regulatory Models > *Enformer*: Attention Meets Regulatory Genomics)                             | <code>*Enformer* [@`avsec_enformer_2021`] demonstrated that combining convolutional compression with transformer attention could dramatically impr ... ecies, establishing a template that subsequent models have extended and refined.</code>      | Use standard citation syntax like [@avsec_enformer_2021] or in-prose 'Avsec et al. @avsec_enformer_2021'. |
| Major      | Citation key formatting: avoid backticks inside [@...] citations | L71 (Regulatory Models > *Enformer*: Attention Meets Regulatory Genomics > Variant Effect Prediction) | <code>Validation against GTEx expression quantitative trait loci (eQTLs) demonstrated that *Enformer*&#x27;s predictions correlate with observed geneti ... t models and validates the architectural investment in extended context windows.</code> | Use standard citation syntax like [@avsec_enformer_2021] or in-prose 'Avsec et al. @avsec_enformer_2021'. |
| Major      | Citation key formatting: avoid backticks inside [@...] citations | L82 (Regulatory Models > Borzoi: From Chromatin to Transcriptome)                                     | <code>While *Enformer* predicts transcription initiation through CAGE, RNA-seq captures a richer picture of gene *expression*: not just where tran ... ified view of how sequence variation affects the entire transcriptional program.</code>      | Use standard citation syntax like [@avsec_enformer_2021] or in-prose 'Avsec et al. @avsec_enformer_2021'. |
| Major      | Citation key formatting: avoid backticks inside [@...] citations | L119 (Regulatory Models > Sei: A Regulatory Vocabulary from Sequence)                                 | <code>While *Enformer* and Borzoi predict continuous coverage tracks, Sei [@`chen_deepsea_2022`] takes a complementary approach: learning a discre ... tates, each associated with characteristic chromatin and transcription patterns.</code>      | Use standard citation syntax like [@avsec_enformer_2021] or in-prose 'Avsec et al. @avsec_enformer_2021'. |
| Major      | Citation key formatting: avoid backticks inside [@...] citations | L136 (Regulatory Models > AlphaGenome: Unifying Modalities at Megabase Scale)                         | <code>AlphaGenome [@`avsec_alphagenome_2025`] extends the hybrid modeling paradigm in two directions: longer context windows (approximately one me ... that provides a comprehensive view of how sequence determines regulatory state.</code>       | Use standard citation syntax like [@avsec_enformer_2021] or in-prose 'Avsec et al. @avsec_enformer_2021'. |
| Minor      | Avoid false enthusiasm / marketing tone                          | L216 (Regulatory Models > Relationship to Foundation Models)                                          | <code>*Enformer* and its descendants can be viewed as highly specialized foundation models, pre-trained on the specific task of regulatory predict ... ct prediction is an active area of development, explored further in @sec-vep-fm.</code>      | Use neutral academic phrasing; attribute assessments to sources if needed.                                |

## Notes for Downstream LLM

- Treat **Blockers** as required edits for this chapter to be instruction-compliant.
- Many issues are mechanical and can be fixed by systematic search-and-replace (for example, citation-key backticks).
