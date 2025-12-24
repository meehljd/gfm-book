# Instruction Compliance Report: Drug Discovery
## Source
- File: `p6-ch27-drug-discovery.qmd`
- Chapter title: Drug Discovery
- Total lines: 251

## Summary of Issues
- **CRITICAL**: 3
- **HIGH**: 10
- **MEDIUM**: 1
- **LOW**: 2

## Issues

### CRITICAL
#### CRITICAL-01: OUTPUT_FORMAT_QMD
- Location: Line 1 (Section: Drug Discovery)
- Evidence: Source file is `p6-ch27-drug-discovery.qmd` (Quarto .qmd), but project instructions require delivering chapter prose as `.md`.
- Recommendation: Convert final deliverable to `.md` (no YAML frontmatter) per project output requirements.

#### CRITICAL-02: META_COMMENTARY
- Location: Line 7 (Section: Drug Discovery)
- Evidence: …fy pathway relationships invisible in single-gene analyses. This chapter examines how these capabilities connect to drug discovery:…
- Recommendation: Remove self-referential framing (e.g., “This chapter…”, “In this chapter…”). State the substantive claims directly.

#### CRITICAL-03: META_COMMENTARY
- Location: Line 239 (Section: Drug Discovery > Connections to Molecular Design)
- Evidence: While this chapter focuses on target identification and indication selection,…
- Recommendation: Remove self-referential framing (e.g., “This chapter…”, “In this chapter…”). State the substantive claims directly.


### HIGH
#### HIGH-01: MALFORMED_IMAGE_LINK
- Location: Line 14 (Section: Drug Discovery > The Genetic Foundation of Target Selection)
- Evidence: ![**FIGURE PLACEHOLDER**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-02: ORDINAL_SCAFFOLDING
- Location: Line 19 (Section: Drug Discovery > The Genetic Foundation of Target Selection)
- Evidence: This empirical observation motivates building pipelines where genetic architecture serves as a first-class input to target identification. Genomic foundation models extend this logic in two directions. First, they provide richer biological context: instead of simple "variants near gene X," foundation models encode regulatory architecture, chromatin state, three-dimensional genome interactions, cell-type specificity, and perturbation responses. Second, they enable transfer across diseases and modalities: a single model trained on diverse genomic and multi-omic data can be reused for multiple diseases and therapeutic areas, analogous to how language models transfer across domains.
- Recommendation: Remove ordinal scaffolding (“First…, Second…”) and rewrite as prose without enumerative crutches (or use a table/callout if appropriate).

#### HIGH-03: MALFORMED_CITATION_SYNTAX
- Location: Line 25 (Section: Drug Discovery > The Genetic Foundation of Target Selection > From Variant-Level Predictions to Gene-Level Evidence)
- Evidence: Consider a typical workflow. Starting from GWAS summary statistics (see @sec-gwas), statistical fine-mapping methods identify credible sets of potentially causal variants at each locus. Sequence-based foundation models then score each candidate variant for regulatory or coding impact. Protein-centric variant effect predictors such as *AlphaMissense*, GPN-MSA, and the missense components of AlphaGenome combine protein language models, structural information, and evolutionary conservation to assess coding variants [@`cheng_alphamissense_2023`; @`benegas_gpn`-`msa_2024`; @`avsec_alphagenome_2025`; @`brandes_genome`-`wide_2023`]. Regulatory foundation models including *Enformer*, Borzoi, and long-context DNA language models predict the consequences of noncoding variants on chromatin accessibility, transcription factor binding, and gene expression [@`avsec_enformer_2021`; @`linder_borzoi_2025`; @dalla-torre_nucleotide_2023; @`nguyen_hyenadna_2023`].
- Recommendation: Fix citation syntax to standard Pandoc/Quarto form (e.g., `[@citekey]` or `Author et al. @citekey`) and remove backticks embedded in citekeys.

#### HIGH-04: MALFORMED_CITATION_SYNTAX
- Location: Line 27 (Section: Drug Discovery > The Genetic Foundation of Target Selection > From Variant-Level Predictions to Gene-Level Evidence)
- Evidence: The critical step is connecting variants to genes. For coding variants, this mapping is straightforward: the variant lies within a gene's coding sequence, and protein-level scores directly inform that gene's candidacy. For noncoding variants, the mapping requires integrating chromatin conformation data (Hi-C, promoter-capture Hi-C), enhancer-gene predictions from models like *Enformer*, and expression quantitative trait locus data that empirically links variants to gene expression changes. Fine-mapping approaches such as MIFM can help distinguish truly causal regulatory variants from correlated passengers, tightening the map from GWAS locus to variant to target gene [@`wu_genome`-`wide_2024`; @`rakowski_mifm_2025`].
- Recommendation: Fix citation syntax to standard Pandoc/Quarto form (e.g., `[@citekey]` or `Author et al. @citekey`) and remove backticks embedded in citekeys.

#### HIGH-05: MALFORMED_IMAGE_LINK
- Location: Line 52 (Section: Drug Discovery > Network-Aware Target Discovery and Repurposing > Propagating Genetic Signals Through Networks)
- Evidence: ![**FIGURE PLACEHOLDER**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-06: MALFORMED_IMAGE_LINK
- Location: Line 70 (Section: Drug Discovery > Drug-Target Interaction Prediction)
- Evidence: ![**FIGURE PLACEHOLDER**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-07: MALFORMED_CITATION_SYNTAX
- Location: Line 77 (Section: Drug Discovery > Drug-Target Interaction Prediction > Representing Targets for Binding Prediction)
- Evidence: Traditional drug-target interaction methods rely on sequence similarity, structural docking, or chemical fingerprint matching. Foundation model approaches replace these hand-crafted features with learned representations. Protein language model embeddings from ESM-2 or similar architectures capture evolutionary and structural information that correlates with binding site properties [@`lin_evolutionary`-`scale_2023`]. Ligand representations from chemical foundation models encode molecular properties relevant to binding affinity and selectivity.
- Recommendation: Fix citation syntax to standard Pandoc/Quarto form (e.g., `[@citekey]` or `Author et al. @citekey`) and remove backticks embedded in citekeys.

#### HIGH-08: MALFORMED_IMAGE_LINK
- Location: Line 116 (Section: Drug Discovery > Functional Genomics Screens and Perturbation Models)
- Evidence: ![**FIGURE PLACEHOLDER**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-09: MALFORMED_IMAGE_LINK
- Location: Line 150 (Section: Drug Discovery > Biomarker Development and Patient Stratification)
- Evidence: ![**FIGURE PLACEHOLDER**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-10: MALFORMED_CITATION_SYNTAX
- Location: Line 183 (Section: Drug Discovery > Industry Workflows and Infrastructure > Building Model Infrastructure)
- Evidence: In mature organizations, foundation models should be treated as shared infrastructure rather than ad hoc scripts developed by individual project teams. A well-organized model catalog contains DNA language models (Nucleotide Transformer, HyenaDNA, GENA-LM), sequence-to-function models (Enformer, Borzoi), and variant effect predictors (AlphaMissense, GPN-MSA, CADD) with documented capabilities, limitations, and appropriate use cases [@dalla-torre_nucleotide_2023; @`nguyen_hyenadna_2023`; @`fishman_gena`-`lm_2025`; @`avsec_enformer_2021`; @`linder_borzoi_2025`; @`cheng_alphamissense_2023`; @`benegas_gpn`-`msa_2024`; @`schubach_cadd_2024`].
- Recommendation: Fix citation syntax to standard Pandoc/Quarto form (e.g., `[@citekey]` or `Author et al. @citekey`) and remove backticks embedded in citekeys.


### MEDIUM
#### MEDIUM-01: POTENTIAL_MISSING_CITATION_FOR_NUMBER
- Location: Line 3 (Section: Drug Discovery)
- Evidence: More than 90% of drug candidates that enter clinical trials fail. They fail because they targeted the wrong gene. They fail because the patient population was too heterogeneous for a single mechanism to succeed. They fail because preclinical models predicted efficacy that did not translate to humans. They fail because safety signals emerged only at scale. The pharmaceutical industry spends billions of dollars on programs that will not produce approved therapies, and the cost of this attrition propagates to the drugs that do succeed: higher prices, longer development timelines, and reduced investment in diseases with smaller markets. The fundamental bottleneck is not generating drug candidates but identifying, early in the process, which targets and which patients offer the highest probability of success.
- Recommendation: If this number/metric comes from a source (not a purely illustrative example), add an appropriate citation.


### LOW
#### LOW-01: FALSE_ENTHUSIASM_WORD
- Location: Line 139 (Section: Drug Discovery > Functional Genomics Screens and Perturbation Models > Closing the Loop: Lab-in-the-Loop Refinement)
- Evidence: Perhaps the most powerful application of foundation models in functional genomics is…
- Recommendation: Replace with a more precise, neutral descriptor (e.g., “high-capacity”, “expressive”, “high-performing”) unless quoting a source.

#### LOW-02: FALSE_ENTHUSIASM_WORD
- Location: Line 193 (Section: Drug Discovery > Industry Workflows and Infrastructure > Strategic Choices: Build, Buy, or Fine-Tune)
- Evidence: …ning open-source foundation models on internal data retains powerful general representations while adapting to local data distri…
- Recommendation: Replace with a more precise, neutral descriptor (e.g., “high-capacity”, “expressive”, “high-performing”) unless quoting a source.

## Quick Fix Checklist
- [ ] Eliminate list-style scaffolding (bullets, numbered lists, “First/Second/Third” ordinals) in flowing prose.
- [ ] Remove meta-commentary (“This chapter…”, “In this chapter…”, “In this section…”).
- [ ] Fix malformed citations (remove backticks in citekeys; use standard `[@citekey]` form).
- [ ] Audit numeric/statistical claims and add citations where needed.
- [ ] Fix malformed image placeholder Markdown so Quarto renders figures correctly.
- [ ] Convert final deliverable to `.md` per output requirements.
- [ ] Replace vague enthusiasm adjectives (“powerful”, “impressive”, “remarkable”) with precise neutral language.

