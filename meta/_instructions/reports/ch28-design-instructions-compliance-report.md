# Instruction Compliance Report: Sequence Design
## Source
- File: `p6-ch28-design.qmd`
- Chapter title: Sequence Design
- Total lines: 245

## Summary of Issues
- **CRITICAL**: 3
- **HIGH**: 12
- **MEDIUM**: 2
- **LOW**: 3

## Issues

### CRITICAL
#### CRITICAL-01: OUTPUT_FORMAT_QMD
- Location: Line 1 (Section: Sequence Design)
- Evidence: Source file is `p6-ch28-design.qmd` (Quarto .qmd), but project instructions require delivering chapter prose as `.md`.
- Recommendation: Convert final deliverable to `.md` (no YAML frontmatter) per project output requirements.

#### CRITICAL-02: META_COMMENTARY
- Location: Line 7 (Section: Sequence Design)
- Evidence: …these capabilities are transforming biological engineering. This chapter examines the methods, applications, and limitations of foun…
- Recommendation: Remove self-referential framing (e.g., “This chapter…”, “In this chapter…”). State the substantive claims directly.

#### CRITICAL-03: EM_DASH
- Location: Line 19 (Section: Sequence Design > The design formalism)
- Evidence: …tein possibilities, 4^500 regulatory; "Exhaustive impossible—intelligent search required." FM roles: Generative prior, di…
- Recommendation: Replace the em-dash (—) with a colon, semicolon, parentheses, or split into separate sentences.


### HIGH
#### HIGH-01: MALFORMED_IMAGE_LINK
- Location: Line 15 (Section: Sequence Design > The design formalism)
- Evidence: ![**FIGURE PLACEHOLDER A**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER%20A``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-02: MALFORMED_IMAGE_LINK
- Location: Line 17 (Section: Sequence Design > The design formalism)
- Evidence: ![**FIGURE PLACEHOLDER B**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER%20B``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-03: MALFORMED_IMAGE_LINK
- Location: Line 32 (Section: Sequence Design > Protein design with language models)
- Evidence: ![**FIGURE PLACEHOLDER A**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER%20A``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-04: MALFORMED_IMAGE_LINK
- Location: Line 34 (Section: Sequence Design > Protein design with language models)
- Evidence: ![**FIGURE PLACEHOLDER B**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER%20B``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-05: MALFORMED_CITATION_SYNTAX
- Location: Line 41 (Section: Sequence Design > Protein design with language models > Sequence generation from language model priors)
- Evidence: Autoregressive protein language models such as ProGen and ProtGPT2 generate novel protein sequences by sampling tokens sequentially from learned distributions [@`madani_progen_2023`; @`ferruz_protgpt2_2022`]. Given a partial sequence, the model predicts probability distributions over the next amino acid, enabling iterative extension until a complete protein emerges. This generation process can be unconditional (sampling from the full learned distribution) or conditional on control signals such as protein family annotations, organism of origin, or functional keywords.
- Recommendation: Fix citation syntax to standard Pandoc/Quarto form (e.g., `[@citekey]` or `Author et al. @citekey`) and remove backticks embedded in citekeys.

#### HIGH-06: MALFORMED_CITATION_SYNTAX
- Location: Line 53 (Section: Sequence Design > Protein design with language models > Structure-aware design with diffusion models)
- Evidence: RFdiffusion exemplifies this approach by generating protein backbones through a diffusion process in three-dimensional coordinate space [@`watson_rfdiffusion_2023`]. Starting from random noise, the model iteratively denoises toward plausible backbone geometries, conditioned on design specifications such as target binding interfaces, desired topology, or symmetric assembly requirements. The resulting backbones represent novel structures not observed in nature but predicted to be physically realizable.
- Recommendation: Fix citation syntax to standard Pandoc/Quarto form (e.g., `[@citekey]` or `Author et al. @citekey`) and remove backticks embedded in citekeys.

#### HIGH-07: MALFORMED_CITATION_SYNTAX
- Location: Line 55 (Section: Sequence Design > Protein design with language models > Structure-aware design with diffusion models)
- Evidence: Converting designed backbones to sequences requires inverse folding models that predict amino acid sequences likely to adopt a given structure. ProteinMPNN and *ESM*-IF operate on this principle, taking backbone coordinates as input and outputting probability distributions over sequences predicted to fold onto that backbone [@`dauparas_proteinmpnn_2022`; @`hsu_learning_2022`]. *ESM*-IF leverages the representations learned by ESM-2 to condition sequence generation on structural constraints, connecting the inverse folding task directly to the protein language model paradigm. The model can generate thousands of candidate sequences for a single backbone, enabling selection based on additional criteria such as expression likelihood or immunogenicity.
- Recommendation: Fix citation syntax to standard Pandoc/Quarto form (e.g., `[@citekey]` or `Author et al. @citekey`) and remove backticks embedded in citekeys.

#### HIGH-08: MALFORMED_IMAGE_LINK
- Location: Line 73 (Section: Sequence Design > Regulatory sequence design)
- Evidence: ![**FIGURE PLACEHOLDER**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-09: MALFORMED_CITATION_SYNTAX
- Location: Line 80 (Section: Sequence Design > Regulatory sequence design > Promoter and enhancer engineering)
- Evidence: Massively parallel reporter assays (MPRAs) have generated training data for models that predict expression levels from promoter and enhancer sequences [@`deboer_deciphering_2020`]. These models learn sequence determinants of regulatory activity, including transcription factor binding sites, spacing constraints between elements, and context-dependent interactions. Once trained, the same models serve as oracles for design: by evaluating expression predictions across millions of candidate sequences, optimization algorithms can identify synthetic regulatory elements with desired properties.
- Recommendation: Fix citation syntax to standard Pandoc/Quarto form (e.g., `[@citekey]` or `Author et al. @citekey`) and remove backticks embedded in citekeys.

#### HIGH-10: MALFORMED_IMAGE_LINK
- Location: Line 102 (Section: Sequence Design > mRNA design and optimization)
- Evidence: ![**FIGURE PLACEHOLDER**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-11: MALFORMED_IMAGE_LINK
- Location: Line 136 (Section: Sequence Design > Antibody and vaccine design)
- Evidence: ![**FIGURE PLACEHOLDER**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.

#### HIGH-12: MALFORMED_IMAGE_LINK
- Location: Line 164 (Section: Sequence Design > Closed-loop design–build–test–learn cycles)
- Evidence: ![**FIGURE PLACEHOLDER**](`https:`//placehold.co/300x200?text=FIGURE%20PLACEHOLDER``)
- Recommendation: Fix Markdown image syntax by removing stray backticks and restoring a valid URL, e.g., `![](https://placehold.co/300x200?text=...)`.


### MEDIUM
#### MEDIUM-01: TRANSITION_STARTER
- Location: Line 112 (Section: Sequence Design > mRNA design and optimization > Codon optimization principles)
- Evidence: …imization strategies that maximize use of preferred codons. However, this approach oversimplifies the complex relationship betw…
- Recommendation: Rephrase to avoid starting a sentence with this transition word, or reduce frequency.

#### MEDIUM-02: TRANSITION_STARTER
- Location: Line 221 (Section: Sequence Design > Practical constraints on design > Safety and biosecurity considerations)
- Evidence: …res capabilities far beyond predicting sequence properties. However, as models improve and integrate with automated synthesis a…
- Recommendation: Rephrase to avoid starting a sentence with this transition word, or reduce frequency.


### LOW
#### LOW-01: FALSE_ENTHUSIASM_WORD
- Location: Line 29 (Section: Sequence Design > Protein design with language models)
- Evidence: …ry sequence databases (see @sec-protein-lm) have emerged as powerful tools for protein design, providing both generative samplin…
- Recommendation: Replace with a more precise, neutral descriptor (e.g., “high-capacity”, “expressive”, “high-performing”) unless quoting a source.

#### LOW-02: FALSE_ENTHUSIASM_WORD
- Location: Line 57 (Section: Sequence Design > Protein design with language models > Structure-aware design with diffusion models)
- Evidence: …xperimentally. The key insight is that structure provides a powerful intermediate representation: rather than searching directly…
- Recommendation: Replace with a more precise, neutral descriptor (e.g., “high-capacity”, “expressive”, “high-performing”) unless quoting a source.

#### LOW-03: FALSE_ENTHUSIASM_WORD
- Location: Line 57 (Section: Sequence Design > Protein design with language models > Structure-aware design with diffusion models)
- Evidence: …ure diffusion followed by inverse folding) has demonstrated remarkable success in creating novel proteins. Designed binders target…
- Recommendation: Replace with a more precise, neutral descriptor (e.g., “high-capacity”, “expressive”, “high-performing”) unless quoting a source.

## Quick Fix Checklist
- [ ] Search for and remove all em-dashes (—).
- [ ] Remove meta-commentary (“This chapter…”, “In this chapter…”, “In this section…”).
- [ ] Fix malformed citations (remove backticks in citekeys; use standard `[@citekey]` form).
- [ ] Fix malformed image placeholder Markdown so Quarto renders figures correctly.
- [ ] Convert final deliverable to `.md` per output requirements.
- [ ] Reduce sentence-start transitions (e.g., “However,”).
- [ ] Replace vague enthusiasm adjectives (“powerful”, “impressive”, “remarkable”) with precise neutral language.

