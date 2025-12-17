# Genomic Foundation Models: Restructured Book Outline

## Overview of Changes

This document outlines the restructured book organization, tracks content migration, and establishes clear pedagogical goals for each chapter. The restructuring addresses several key issues:

1. **Pedagogical flow**: Concrete examples now precede abstract principles
2. **VEP integration**: Variant effect prediction is now a capstone chapter in Part III rather than buried in evaluation
3. **Scaling and UQ coverage**: New dedicated content for scaling laws and uncertainty quantification
4. **Network/GNN framing**: Repositioned as consumers of FM embeddings, not competing paradigm
5. **3D genome coverage**: New chapter fills significant gap
6. **Regulatory/ethical expansion**: Expanded treatment in final chapter

**Final count**: 29 chapters + 6 appendices across 6 parts

---

## Change Summary Table

| Old Chapter | Old Location | New Chapter | New Location | Change Type |
|-------------|--------------|-------------|--------------|-------------|
| Ch 1: NGS | Part I | Ch 1: NGS | Part I | Unchanged |
| Ch 2: Data | Part I | Ch 2: Data | Part I | Unchanged |
| Ch 3: PGS | Part I | Ch 3: GWAS/PGS | Part I | Renamed |
| Ch 4: CADD | Part I | Ch 4: Classical VEP | Part I | Scope narrowed |
| Ch 5: Tokens | Part II | Ch 5: Representations | Part II | Expanded |
| Ch 6: Transformers | Part II | Ch 7: Attention | Part II | Reordered |
| Ch 7: Foundation | Part II | Ch 10: FM Paradigm | Part III | Moved, expanded |
| Ch 8: Pretrain | Part II | Ch 8: Pretraining | Part II | Minor rename |
| Ch 9: Transfer | Part II | Ch 9: Transfer | Part II | Unchanged |
| Ch 10: CNN | Part III | Ch 6: CNN | Part II | **Moved earlier** |
| Ch 11: DNA LM | Part III | Ch 11: DNA LM | Part III | Renumbered |
| Ch 12: RNA | Part III | Ch 15: RNA | Part IV | **Moved to Part IV** |
| Ch 13: PLM | Part III | Ch 12: Protein LM | Part III | Renumbered |
| Ch 14: Hybrid | Part III | Ch 13: Regulatory | Part III | Renamed |
| Ch 15: SC/Epi | Part IV | Ch 16: Single-cell | Part IV | Renumbered |
| Ch 16: Networks | Part IV | Ch 18: Networks | Part IV | **Reframed** |
| Ch 17: Systems | Part IV | Ch 19: Multi-omics | Part IV | Renamed |
| Ch 18: Benchmarks | Part V | Ch 20: Benchmarks | Part V | Renumbered |
| Ch 19: Eval | Part V | Ch 21: Eval | Part V | Renumbered |
| Ch 20: VEP | Part V | Ch 14: VEP-FM | Part III | **Moved to Part III** |
| Ch 21: Confound | Part V | Ch 22: Confounding | Part V | Renumbered |
| Ch 22: Interp | Part V | Ch 24: Interpretability | Part V | Renumbered |
| Ch 23: Clinical | Part VI | Ch 25: Clinical | Part VI | Renumbered |
| Ch 24: Variants | Part VI | Ch 26: Rare Disease | Part VI | Renumbered |
| Ch 25: Drugs | Part VI | Ch 27: Drug Discovery | Part VI | Renumbered |
| Ch 26: Design | Part VI | Ch 28: Design | Part VI | Renumbered |
| Ch 27: Future | Part VI | Ch 29: Future | Part VI | Expanded |
| — | — | Ch 17: 3D Genome | Part IV | **NEW** |
| — | — | Ch 23: Uncertainty | Part V | **NEW** |
| App B: Deployment | Appendix | App B: Compute | Appendix | Renamed |
| — | — | App C: Data Curation | Appendix | **NEW** |

---

## Part I: Genomic Foundations

**Part theme**: What data exists, how it's generated, and what classical methods could do with it. Establishes the "before" picture against which foundation models are measured.

**Pedagogical goal**: Readers from ML backgrounds gain sufficient genomics context; readers from genomics backgrounds see the landscape they know framed as a machine learning problem.

**Prerequisites assumed**: Basic molecular biology (DNA → RNA → protein), introductory statistics

---

### Chapter 1: Sequencing and Variant Calling
**Label**: `@sec-ngs`  
**Old source**: p1-ch01-ngs.qmd (unchanged)

**Conceptual goals**:
- Understand how raw sequence data is generated and its error characteristics
- Recognize that variant calling is a probabilistic inference problem, not simple string matching
- Appreciate that every downstream model assumes this upstream problem is solved

**Key concepts**:
- NGS technologies (Illumina short-read, PacBio HiFi, ONT long-read)
- Read alignment and the reference genome assumption
- Variant calling pipelines: GATK, DeepVariant transition
- Error profiles by technology; systematic vs. random errors
- VCF format and variant representation
- The "difficult regions" problem: repeats, HLA, structural variants

**Pedagogical arc**:
1. Open with the paradox: cheap sequencing, expensive interpretation
2. Show the data generation process and where errors enter
3. Introduce classical variant calling as probabilistic reasoning
4. Preview DeepVariant as a taste of what's coming (learned features beat hand-crafted)
5. Close with: every model in this book inherits errors from this step

**Connections**:
- Forward to Ch 4 (classical VEP depends on accurate variant calls)
- Forward to Ch 6 (DeepVariant architecture previews CNN discussion)
- Forward to Ch 14 (VEP accuracy limited by variant calling accuracy)

---

### Chapter 2: Genomic Data Resources
**Label**: `@sec-data`  
**Old source**: p1-ch02-data.qmd (unchanged)

**Conceptual goals**:
- Know the major data resources that serve as training sets and evaluation benchmarks
- Understand the biases and limitations built into these resources
- Recognize that "ground truth" labels are often noisy or circular

**Key concepts**:
- Reference genomes: GRCh38, T2T, pangenome references
- Population variation: gnomAD, dbSNP, 1000 Genomes
- Clinical variant databases: ClinVar, HGMD, LOVD
- Functional genomics: ENCODE, Roadmap Epigenomics, GTEx
- Biobanks: UK Biobank, All of Us, FinnGen, deCODE
- Training data vs. evaluation data vs. deployment distribution

**Pedagogical arc**:
1. Open with the question: where do training labels come from?
2. Survey reference genomes and their limitations (single individual, not population)
3. Cover population variation catalogs and ascertainment bias
4. Explain functional genomics resources as "molecular phenotype" labels
5. Discuss biobanks as the bridge to clinical phenotypes
6. Close with: these resources shape what models can learn

**Connections**:
- Forward to Ch 3 (biobanks enable GWAS)
- Forward to Ch 11-12 (training corpora for DNA/protein LMs)
- Forward to Ch 20 (benchmarks built from these resources)
- Forward to Ch 22 (confounding from data resource biases)

**Migration notes**: Consider moving some training corpus detail to Ch 11-12 to avoid redundancy. This chapter should focus on "what exists and why it matters" rather than exhaustive enumeration.

---

### Chapter 3: Statistical Genetics and Polygenic Scores
**Label**: `@sec-gwas`  
**Old source**: p1-ch03-pgs.qmd (renamed from sec-gwas)

**Conceptual goals**:
- Understand GWAS as the dominant paradigm for variant-to-trait mapping
- Recognize the distinction between association and causation
- Appreciate PGS capabilities and fundamental limitations

**Key concepts**:
- GWAS methodology: association testing, multiple testing correction, Manhattan plots
- Linkage disequilibrium and why lead SNPs often aren't causal
- Fine-mapping: statistical and functional approaches
- Heritability: SNP-heritability vs. pedigree heritability, missing heritability
- Polygenic score construction: C+T, LDpred, PRS-CS
- PGS portability problems across ancestry
- Clinical PGS: current applications and limitations

**Pedagogical arc**:
1. Open with the promise: genome → disease risk prediction
2. Explain GWAS as a massive hypothesis test across the genome
3. Introduce LD as the reason associations don't equal causation
4. Cover fine-mapping as the attempt to identify causal variants
5. Build PGS as weighted sums of variant effects
6. Confront portability failure across populations
7. Close with: GWAS finds associations; we need mechanism

**Connections**:
- Back to Ch 2 (biobanks enable GWAS)
- Forward to Ch 4 (fine-mapping uses functional scores)
- Forward to Ch 13 (regulatory models predict variant effects for fine-mapping)
- Forward to Ch 14 (VEP combined with GWAS for causal variant ID)
- Forward to Ch 22 (ancestry confounding in GWAS/PGS)
- Forward to Ch 25 (clinical PGS deployment)

---

### Chapter 4: Classical Variant Effect Prediction
**Label**: `@sec-vep-classical`  
**Old source**: p1-ch04-cadd.qmd (scope narrowed, renamed)

**Conceptual goals**:
- Understand the pre-deep-learning approach to variant effect prediction
- Recognize the feature engineering paradigm and its limitations
- Identify sources of circularity and data leakage in classical scores

**Key concepts**:
- Conservation-based scores: GERP, PhyloP, phastCons
- Protein-level predictors: SIFT, PolyPhen-2
- Ensemble methods: CADD, REVEL, M-CAP
- Feature categories: sequence, conservation, protein structure, annotation
- Label sources: ClinVar pathogenic/benign, derived allele frequency
- Circularity problem: training on databases that use these scores
- Ascertainment bias: enrichment for coding, well-studied genes

**Pedagogical arc**:
1. Open with the clinical need: which variants matter?
2. Show the intuition: conservation implies constraint implies function
3. Build up from single features to ensemble predictors
4. Reveal the circularity: CADD trained on annotations that assume CADD-like scores
5. Discuss what these scores actually measure vs. what we want
6. Close with: feature engineering ceiling motivates learned representations

**Connections**:
- Forward to Ch 6 (CNNs learn features directly from sequence)
- Forward to Ch 12 (protein LMs provide learned conservation)
- Forward to Ch 14 (FM-based VEP vs. classical VEP comparison)
- Forward to Ch 22 (confounding issues continue in FM era)
- Forward to Ch 26 (clinical variant interpretation uses these scores)

**Migration notes**: This chapter should NOT cover FM-based VEP methods (ESM-1v, AlphaMissense). Those belong in Ch 14. The split is: Ch 4 = pre-2018 feature engineering; Ch 14 = foundation model era.

---

## Part II: Deep Learning for Sequences

**Part theme**: The architectural evolution from CNNs to transformers, taught through genomic examples. Principles emerge from concrete models rather than preceding them.

**Pedagogical goal**: Readers understand why each architectural advance was motivated by limitations of the previous approach. The progression CNN → attention → self-supervision feels inevitable rather than arbitrary.

**Prerequisites assumed**: Part I content; basic neural network familiarity (or Appendix A)

---

### Chapter 5: Sequence Representations
**Label**: `@sec-representations`  
**Old source**: p2-ch05-tokens.qmd (expanded, renamed)

**Conceptual goals**:
- Understand that representation choices constrain what models can learn
- Compare tradeoffs across tokenization schemes for biological sequence
- Recognize that position encoding is a design choice with consequences

**Key concepts**:
- One-hot encoding: the simplest representation and its limitations
- k-mer tokenization: vocabulary size vs. context capture tradeoffs
- Byte-pair encoding and subword tokenization for genomes
- Learned embeddings: from discrete tokens to continuous space
- Position encodings: absolute, relative, rotary, ALiBi
- Special considerations for biological sequence (strand, circularity, coordinates)

**Pedagogical arc**:
1. Open with the question: how does a neural network see DNA?
2. Start with one-hot as the obvious approach; show its sparsity
3. Introduce k-mers as a middle ground with tradeoffs
4. Explain BPE and why it works differently for genomes vs. text
5. Cover embeddings as learned representations
6. Address position: why it matters more for biology than text
7. Close with: representation choices propagate through entire model

**Connections**:
- Forward to Ch 6 (CNNs implicitly learn k-mer-like filters)
- Forward to Ch 7 (transformers require explicit position encoding)
- Forward to Ch 11 (DNA LM tokenization choices)
- Forward to Ch 12 (protein tokenization: amino acids vs. structure)

**Migration notes**: Expanded from old tokens chapter to include more on embeddings and position encodings. Some position encoding detail may also appear in Ch 7; coordinate to avoid redundancy.

---

### Chapter 6: Convolutional Models
**Label**: `@sec-cnn`  
**Old source**: p3-ch10-cnn.qmd (**MOVED from Part III to Part II**)

**Conceptual goals**:
- Understand CNNs as the first successful deep learning approach for genomics
- See that learned filters discover motif-like patterns without hand-engineering
- Recognize the receptive field limitation that motivates attention

**Key concepts**:
- Convolutional filters as motif detectors
- DeepSEA: predicting chromatin marks from sequence
- Basset, DanQ: architectural variations
- ExPecto: expression prediction from regulatory sequence
- SpliceAI: dilated convolutions for splicing; clinical deployment
- Receptive field: what CNNs can and cannot see
- The long-range dependency problem: enhancers 50kb away

**Pedagogical arc**:
1. Open with DeepSEA's 2015 result: learned filters beat PWMs
2. Explain convolution as sliding window pattern matching
3. Show that learned filters resemble known TF motifs (interpretability)
4. Cover SpliceAI as an example with clear clinical utility
5. Build to the limitation: receptive field ceiling
6. Quantify the problem: typical enhancer-promoter distances vs. CNN reach
7. Close with: we need an architecture that sees further

**Connections**:
- Back to Ch 4 (CNNs replace feature engineering)
- Forward to Ch 7 (attention solves long-range problem)
- Forward to Ch 13 (Enformer combines CNN + attention)
- Forward to Ch 14 (SpliceAI as clinical-grade VEP)
- Forward to Ch 24 (interpretability: filter visualization)

**Migration notes**: This is the major structural change. Moving CNNs before transformers allows the "why attention?" question to arise naturally from CNN limitations. The chapter should end with a clear statement of what CNNs cannot do.

---

### Chapter 7: Attention and Transformers
**Label**: `@sec-attention`  
**Old source**: p2-ch06-transformers.qmd (reordered, renamed)

**Conceptual goals**:
- Understand attention as a mechanism for dynamic, content-dependent weighting
- See transformers as attention + feedforward in a modular architecture
- Recognize computational costs and the quadratic attention problem

**Key concepts**:
- Self-attention: queries, keys, values, and the attention matrix
- Multi-head attention: parallel attention patterns
- Position encodings revisited: absolute, relative, rotary
- Transformer blocks: attention + FFN + residuals + layer norm
- Encoder vs. decoder vs. encoder-decoder architectures
- Computational complexity: O(n²) attention and its implications
- Efficient attention variants: linear attention, sparse attention, state space models

**Pedagogical arc**:
1. Open with the CNN limitation from Ch 6: fixed receptive field
2. Introduce attention as "dynamic routing" based on content
3. Build up self-attention mathematically but with intuition
4. Show multi-head attention as parallel pattern detection
5. Assemble the full transformer block
6. Confront the quadratic cost and genomic sequence lengths
7. Survey efficient alternatives
8. Close with: attention enables long-range modeling but costs scale

**Connections**:
- Back to Ch 5 (position encodings)
- Back to Ch 6 (attention solves CNN limitations)
- Forward to Ch 8 (transformers enable self-supervised pretraining at scale)
- Forward to Ch 11-13 (transformer architectures in DNA/protein LMs)
- Forward to Ch 13 (Enformer's 200kb attention span)

---

### Chapter 8: Self-Supervision and Pretraining
**Label**: `@sec-pretraining`  
**Old source**: p2-ch08-pretrain.qmd (minor rename)

**Conceptual goals**:
- Understand self-supervision as learning from structure in unlabeled data
- Compare pretraining objectives and what they teach models
- Recognize that pretraining objective shapes learned representations

**Key concepts**:
- Masked language modeling (MLM): BERT-style pretraining
- Next-token prediction: autoregressive/GPT-style pretraining
- Contrastive learning: SimCLR, CLIP-style objectives
- Span corruption and T5-style objectives
- Multi-task pretraining: combining objectives
- What different objectives teach: bidirectional context vs. generation
- Scaling and emergent capabilities

**Pedagogical arc**:
1. Open with the data abundance problem: labels are scarce, sequence is abundant
2. Introduce MLM: predict masked tokens from context
3. Contrast with autoregressive: predict next token
4. Explain contrastive learning: pull similar, push dissimilar
5. Compare what models learn from each objective
6. Discuss scaling: more data + more parameters → emergent capabilities
7. Close with: self-supervision unlocks scale; objective shapes representation

**Connections**:
- Forward to Ch 9 (pretrained models → downstream tasks)
- Forward to Ch 10 (scaling laws formalize these observations)
- Forward to Ch 11 (DNA LMs use MLM/autoregressive)
- Forward to Ch 12 (protein LMs use MLM; evolutionary signal)

---

### Chapter 9: Transfer Learning and Adaptation
**Label**: `@sec-transfer`  
**Old source**: p2-ch09-transfer.qmd (unchanged)

**Conceptual goals**:
- Understand mechanisms for adapting pretrained models to new tasks
- Recognize when transfer succeeds and when it fails
- Make practical decisions about fine-tuning vs. probing vs. adapters

**Key concepts**:
- Feature extraction: frozen backbone + trained head
- Fine-tuning: updating all or part of the model
- Parameter-efficient methods: adapters, LoRA, prefix tuning
- Probing: what do representations encode?
- Domain shift: when source and target distributions differ
- Few-shot and zero-shot inference
- Negative transfer: when pretraining hurts

**Pedagogical arc**:
1. Open with the promise: train once, use everywhere
2. Explain the fine-tuning spectrum from frozen to full update
3. Introduce efficient adaptation methods (LoRA, adapters)
4. Cover probing as a diagnostic tool
5. Confront domain shift: different species, tissues, assays
6. Discuss few-shot learning and prompting
7. Address negative transfer: when pretrained features don't help
8. Close with: transfer is powerful but not automatic; match method to task

**Connections**:
- Forward to Ch 10 (foundation models assume transfer works)
- Forward to Ch 11-14 (transfer results for specific model families)
- Forward to Ch 21 (evaluation must account for distribution shift)
- Forward to Ch 22 (confounding can masquerade as transfer success)

---

## Part III: Foundation Models for Biology

**Part theme**: The major foundation model families, organized by modality. This part shows what current models can do and establishes VEP as the integrating application.

**Pedagogical goal**: Readers understand the landscape of genomic foundation models, their training data, architectures, capabilities, and limitations. VEP serves as a capstone that integrates concepts across model families.

**Prerequisites assumed**: Parts I-II content

---

### Chapter 10: The Foundation Model Paradigm
**Label**: `@sec-fm-principles`  
**Old source**: p2-ch07-foundation.qmd (**MOVED from Part II, expanded with scaling laws**)

**Conceptual goals**:
- Define what makes a model a "foundation model" vs. task-specific model
- Understand scaling laws and their implications for model development
- Make informed build-vs-use decisions

**Key concepts**:
- Foundation model definition: pretrained, broadly applicable, adaptable
- Taxonomy: by modality (DNA, RNA, protein), by objective, by scale
- Scaling laws: Chinchilla-style compute-optimal training
- Emergent capabilities: what appears at scale that wasn't present before
- The "foundation" metaphor: benefits and limitations
- Build vs. use decisions: when to train from scratch vs. adapt existing
- Compute and data requirements: practical constraints

**Pedagogical arc**:
1. Open with the paradigm shift: from task-specific to general-purpose
2. Define foundation models precisely; contrast with earlier approaches
3. Introduce scaling laws: the relationship between parameters, data, compute
4. Discuss emergence: capabilities that appear discontinuously at scale
5. Survey the current landscape of genomic FMs
6. Address practical decisions: when FMs help vs. overkill
7. Close with: FMs are tools with costs and benefits; match to problem

**Connections**:
- Back to Ch 8-9 (pretraining + transfer enable the FM paradigm)
- Forward to Ch 11-14 (specific FM families)
- Forward to Ch 20-21 (evaluating FM claims requires rigor)
- Forward to App B (compute requirements)

**Migration notes**: This chapter moved from Part II to Part III because it makes more sense after readers have seen concrete architectures. **New content**: scaling laws section is entirely new, addressing a gap in the original outline.

---

### Chapter 11: DNA Language Models
**Label**: `@sec-dna-lm`  
**Old source**: p3-ch11-dna.qmd (renamed)

**Conceptual goals**:
- Understand how language model approaches adapt to DNA sequence
- Compare major DNA LM architectures and their design choices
- Recognize what DNA LMs learn and what they struggle with

**Key concepts**:
- DNABERT: BERT-style MLM on k-mer tokenized DNA
- Nucleotide Transformer: scaling DNA LMs with varied tokenization
- HyenaDNA: long-context modeling with state space models
- Evo: autoregressive DNA modeling at genome scale
- Training corpora: reference genomes, metagenomes, multi-species
- What DNA LMs learn: motifs, regulatory grammar, species signatures
- Benchmarks: Genomic Benchmarks, BEND, nucleotide-level tasks
- Limitations: context length, cross-species transfer, interpretability

**Pedagogical arc**:
1. Open with the analogy: DNA as a language with grammar
2. Cover DNABERT as the straightforward BERT adaptation
3. Discuss tokenization choices and their consequences
4. Introduce long-context approaches (HyenaDNA, Evo)
5. Examine training data: what sequence, from which species
6. Analyze what these models actually learn via probing
7. Survey benchmark performance and limitations
8. Close with: DNA LMs capture sequence patterns; regulatory function requires more

**Connections**:
- Back to Ch 5 (tokenization choices)
- Back to Ch 7-8 (transformer architecture, self-supervision)
- Forward to Ch 13 (regulatory models add expression/epigenome supervision)
- Forward to Ch 14 (DNA LMs for variant effect prediction)
- Forward to Ch 20 (benchmarks for evaluation)

---

### Chapter 12: Protein Language Models
**Label**: `@sec-protein-lm`  
**Old source**: p3-ch13-plm.qmd (renumbered, renamed)

**Conceptual goals**:
- Understand protein LMs as the most mature genomic FM family
- See that evolutionary sequences provide implicit structural supervision
- Connect protein LMs to structure prediction and variant effects

**Key concepts**:
- ESM-1b, ESM-2: scaling protein LMs
- ProtTrans, ProtBERT: alternative architectures
- Training data: UniRef, evolutionary sequence databases
- Emergent structure: contact prediction, secondary structure from sequence alone
- ESMFold: structure prediction from single-sequence embeddings
- Attention patterns and evolutionary coupling
- Protein LMs for function prediction
- Limitations: rare proteins, novel folds, conformational flexibility

**Pedagogical arc**:
1. Open with the evolution as teacher: millions of years of natural experiments
2. Introduce ESM as masked language modeling on protein sequence
3. Show emergent structure: contacts emerge without structure labels
4. Explain the connection to evolutionary coupling and MSAs
5. Cover ESMFold as structure prediction from embeddings
6. Discuss function prediction applications
7. Address limitations: training data bias, rare sequences
8. Close with: protein LMs learn physics from evolution; they're the FM success story

**Connections**:
- Back to Ch 2 (UniRef and protein databases)
- Back to Ch 8 (MLM pretraining)
- Forward to Ch 14 (ESM-1v, AlphaMissense for variant effects)
- Forward to Ch 15 (RNA LMs as intermediate case)
- Forward to Ch 28 (protein design with generative PLMs)

---

### Chapter 13: Long-Context Regulatory Models
**Label**: `@sec-regulatory`  
**Old source**: p3-ch14-hybrid.qmd (renamed to clarify focus)

**Conceptual goals**:
- Understand how hybrid architectures span the CNN-transformer divide
- See regulatory prediction as the key application for long-context models
- Recognize the connection between model architecture and biological question

**Key concepts**:
- Enformer: 200kb context for expression prediction
- Borzoi: extending to longer contexts
- Sei: sequence → regulatory vocabulary
- Architecture: CNN stem + transformer body (why this combination)
- Training targets: CAGE, histone ChIP, ATAC (connecting to Ch 2)
- Predicting variant effects on expression
- Cross-cell-type and cross-species transfer
- Limitations: training on bulk assays, missing 3D context

**Pedagogical arc**:
1. Open with the enhancer-promoter problem: regulation spans tens of kb
2. Explain why pure CNNs fail and pure transformers are expensive
3. Introduce Enformer's hybrid architecture
4. Cover training targets: what molecular phenotypes serve as supervision
5. Show variant effect prediction on expression
6. Discuss transfer across tissues and species
7. Address limitations: bulk resolution, 3D structure, causality
8. Close with: these models predict regulatory effects but don't explain mechanism

**Connections**:
- Back to Ch 6 (CNN limitations motivate hybrids)
- Back to Ch 7 (transformer attention for long range)
- Forward to Ch 14 (regulatory VEP integration)
- Forward to Ch 17 (3D genome context these models miss)
- Forward to Ch 24 (interpreting regulatory model predictions)

---

### Chapter 14: Variant Effect Prediction with Foundation Models
**Label**: `@sec-vep-fm`  
**Old source**: p5-ch20-vep.qmd (**MOVED from Part V to Part III as capstone**)

**Conceptual goals**:
- See VEP as the central application that integrates foundation model capabilities
- Compare protein-based and DNA-based VEP approaches
- Understand calibration, uncertainty, and clinical readiness

**Key concepts**:
- Protein-based VEP: ESM-1v log-likelihood ratios, AlphaMissense, EVE
- DNA-based VEP: regulatory variant effects from Enformer, splicing from SpliceAI
- Combining evidence across modalities
- Zero-shot vs. fine-tuned VEP
- Calibration: do model scores map to clinical categories?
- Uncertainty quantification for VEP
- Comparison to classical methods (Ch 4): what did FMs add?
- Clinical integration: ACMG criteria, evidence weighting

**Pedagogical arc**:
1. Open with the clinical question: is this variant pathogenic?
2. Review protein-based approaches: ESM-1v, AlphaMissense
3. Cover DNA-based approaches: regulatory, splicing
4. Discuss how to combine evidence across modalities
5. Address calibration: model scores vs. clinical categories
6. Introduce uncertainty and when models don't know
7. Compare to classical methods: improvements and remaining gaps
8. Close with: FM-based VEP advances the field but doesn't solve it

**Connections**:
- Back to Ch 4 (classical VEP baseline)
- Back to Ch 6 (SpliceAI CNN)
- Back to Ch 11-13 (foundation models being applied)
- Forward to Ch 23 (uncertainty quantification in depth)
- Forward to Ch 26 (rare disease variant interpretation workflow)

**Migration notes**: This is the second major structural change. Moving VEP from Part V (evaluation) to Part III (foundation models) positions it as the capstone application that integrates the model families. The chapter should synthesize Ch 11-13 rather than introducing new architectures.

---

## Part IV: Multi-Scale and Systems Modeling

**Part theme**: From sequence representations to cellular and network context. Foundation model principles extend beyond 1D sequence to embrace the hierarchy of biological organization.

**Pedagogical goal**: Readers understand that sequence is necessary but not sufficient; cellular context, 3D structure, and network relationships provide additional explanatory power. Foundation model embeddings become inputs to higher-level reasoning.

**Prerequisites assumed**: Parts I-III content

---

### Chapter 15: RNA Models
**Label**: `@sec-rna`  
**Old source**: p3-ch12-rna.qmd (**MOVED from Part III to Part IV**)

**Conceptual goals**:
- Understand RNA as the neglected middle layer between DNA and protein
- See that RNA secondary structure creates a distinct modeling challenge
- Recognize RNA FMs as less mature than DNA/protein LMs

**Key concepts**:
- RNA secondary structure: base pairing, pseudoknots, tertiary structure
- Structure prediction approaches: thermodynamic vs. learned
- RNA-FM and RNA language models
- mRNA modeling: UTRs, stability, translation efficiency
- Non-coding RNA: lncRNA, miRNA function prediction
- Splicing models beyond SpliceAI
- Limitations: sparse structural data, functional annotation gaps

**Pedagogical arc**:
1. Open with the central dogma gap: RNA is more than a messenger
2. Explain RNA secondary structure and why it matters
3. Cover structure prediction approaches
4. Introduce RNA language models
5. Discuss mRNA-specific modeling (UTRs, stability)
6. Address non-coding RNA function prediction
7. Acknowledge limitations: less data, less mature than protein LMs
8. Close with: RNA modeling is a frontier with clear opportunities

**Connections**:
- Back to Ch 6 (splicing models)
- Back to Ch 12 (contrast with protein LM maturity)
- Forward to Ch 16 (RNA in single-cell contexts)
- Forward to Ch 28 (mRNA design for therapeutics)

**Migration notes**: Moved from Part III to Part IV because RNA sits at the cellular/molecular interface. It bridges sequence-level modeling (Part III) and cellular context (Part IV). The chapter should explicitly position RNA as transitional.

---

### Chapter 16: Single-Cell and Epigenomic Models
**Label**: `@sec-single-cell`  
**Old source**: p4-ch15-sc-epi.qmd (renamed)

**Conceptual goals**:
- Understand that identical genomes produce different cell types through regulation
- See single-cell data as revealing heterogeneity invisible to bulk assays
- Recognize foundation model approaches for cell state representation

**Key concepts**:
- Single-cell RNA-seq and the cell-as-document analogy
- scGPT, Geneformer, scFoundation: cell embedding models
- Cell type classification and annotation
- Perturbation prediction: in silico gene knockouts
- Epigenomic models: ATAC-seq, methylation
- Cross-modality alignment: linking scRNA to scATAC
- Limitations: dropout noise, batch effects, training data bias

**Pedagogical arc**:
1. Open with the question: same genome, different cells—how?
2. Introduce single-cell data and its challenges (sparsity, noise)
3. Cover scGPT and related cell embedding models
4. Show applications: cell type annotation, perturbation prediction
5. Extend to epigenomic data: ATAC, methylation
6. Discuss cross-modality integration
7. Address limitations: technical artifacts, well-studied cell types
8. Close with: single-cell FMs capture cell state; causality remains elusive

**Connections**:
- Back to Ch 13 (bulk regulatory models as baseline)
- Forward to Ch 17 (spatial context for single cells)
- Forward to Ch 18 (cell embeddings as node features in networks)
- Forward to Ch 19 (multi-omics integration)

---

### Chapter 17: 3D Genome and Spatial Models
**Label**: `@sec-3d-genome`  
**Old source**: **NEW CHAPTER**

**Conceptual goals**:
- Understand that the genome folds into 3D structures that affect regulation
- See that long-range contacts explain enhancer-gene relationships
- Recognize emerging spatial transcriptomics foundation models

**Key concepts**:
- Chromatin organization: A/B compartments, TADs, loops
- Hi-C and chromosome conformation capture
- Predicting 3D contacts from sequence: Akita, Orca, C.Origami
- TAD boundaries and their sequence determinants
- Connecting 3D structure to expression: the "missing link" in regulatory models
- Spatial transcriptomics: tissue context for expression
- Spatial foundation models: emerging approaches
- Limitations: resolution, population averaging, causality

**Pedagogical arc**:
1. Open with the folding problem: 2 meters of DNA in a 10 micron nucleus
2. Explain chromatin organization levels
3. Introduce Hi-C and what it measures
4. Cover sequence → 3D structure prediction models
5. Connect 3D structure to regulatory models from Ch 13
6. Introduce spatial transcriptomics as tissue-level context
7. Survey emerging spatial foundation models
8. Close with: 3D structure is the missing link between sequence and regulation

**Connections**:
- Back to Ch 13 (what Enformer is missing: 3D context)
- Forward to Ch 18 (chromatin contacts as edges in networks)
- Forward to Ch 19 (multi-omics includes spatial data)
- Forward to Ch 24 (interpreting predictions through 3D structure)

**Content sources**: This is new content. Draw on: Akita [@fudenberg_predicting_2020], Orca, C.Origami papers, recent spatial transcriptomics FMs.

---

### Chapter 18: Networks and Graph-Based Reasoning
**Label**: `@sec-networks`  
**Old source**: p4-ch16-networks.qmd (**REFRAMED: FM embeddings as inputs, not competing paradigm**)

**Conceptual goals**:
- Understand biological networks as a level of abstraction above sequence
- See that FM embeddings provide rich node features for graph models
- Recognize GNNs as consumers of foundation model representations

**Key concepts**:
- Biological networks: PPI, regulatory, metabolic, knowledge graphs
- Network data sources: STRING, BioGRID, Reactome, pathway databases
- GNN architectures: message passing, graph attention, heterogeneous graphs
- FM embeddings as node features: using ESM, Enformer, scGPT representations
- Applications: gene function prediction, drug-target interaction, pathway analysis
- Gene prioritization for GWAS
- Limitations: network incompleteness, bias toward well-studied genes, causality

**Pedagogical arc**:
1. Open with the abstraction hierarchy: sequence → molecule → network → phenotype
2. Explain biological networks and their data sources
3. Introduce GNN architectures for relational reasoning
4. **Key section**: FM embeddings as node features—this is the integration point
5. Show applications that combine FM representations with network structure
6. Discuss gene prioritization and pathway enrichment
7. Address limitations: incomplete networks favor well-studied genes
8. Close with: networks provide relational context that sequence alone lacks

**Connections**:
- Back to Ch 11-12 (FM embeddings as node features)
- Back to Ch 16 (cell embeddings in network context)
- Forward to Ch 19 (networks as one integration modality)
- Forward to Ch 27 (drug-target networks in discovery)

**Migration notes**: The key reframing is that GNNs and networks are not alternatives to foundation models but rather operate at a higher level of abstraction using FM embeddings as inputs. The chapter should make this architectural relationship explicit.

---

### Chapter 19: Multi-Omics Integration
**Label**: `@sec-multi-omics`  
**Old source**: p4-ch17-systems.qmd (renamed)

**Conceptual goals**:
- Understand that no single modality captures biology
- Compare integration strategies: early, intermediate, late fusion
- See clinical multi-omics as the path to actionable predictions

**Key concepts**:
- Integration paradigms: early fusion, late fusion, intermediate fusion
- Cross-modal alignment: shared embedding spaces
- Genomics + transcriptomics + proteomics + metabolomics
- Clinical integration: EHR + genomics + imaging
- The systems view: variant → molecular → cellular → tissue → phenotype
- Missing modality problems: imputation and robustness
- Limitations: sample matching, batch effects, interpretability

**Pedagogical arc**:
1. Open with the phenotype prediction goal: sequence to outcome
2. Explain why single modalities are insufficient
3. Cover integration strategies and their tradeoffs
4. Show examples of multi-omics foundation models
5. Extend to clinical data: EHR, imaging, genomics
6. Discuss the systems biology perspective
7. Address practical challenges: missing data, batch effects
8. Close with: integration is necessary but technically challenging

**Connections**:
- Back to Ch 15-18 (component modalities being integrated)
- Forward to Ch 21 (evaluating multi-modal models)
- Forward to Ch 25 (clinical risk prediction using integrated data)
- Forward to Ch 27 (multi-omics in drug discovery)

---

## Part V: Evaluation and Reliability

**Part theme**: How to know if models work and when they fail. Rigorous evaluation is not optional; it determines whether models are useful or dangerous.

**Pedagogical goal**: Readers develop critical evaluation skills and can identify when published results are misleading. Uncertainty and interpretability become practical tools, not academic abstractions.

**Prerequisites assumed**: Parts I-IV content

---

### Chapter 20: Benchmarks for Genomic AI
**Label**: `@sec-benchmarks`  
**Old source**: p5-ch18-benchmarks.qmd (renumbered)

**Conceptual goals**:
- Survey the benchmark landscape for genomic foundation models
- Recognize benchmark limitations and potential for gaming
- Understand the gap between benchmark performance and real-world utility

**Key concepts**:
- Protein benchmarks: TAPE, FLIP, ProteinGym
- DNA benchmarks: Genomic Benchmarks, BEND
- Variant effect benchmarks: CAGI, ProteinGym DMS
- Clinical benchmarks: ClinVar-derived evaluations
- Benchmark construction: data sources, splits, metrics
- Benchmark limitations: saturation, leakage, distribution shift
- The benchmark → deployment gap

**Pedagogical arc**:
1. Open with the question: how do we know if a model is good?
2. Survey protein benchmarks and what they measure
3. Survey DNA and regulatory benchmarks
4. Cover variant effect and clinical benchmarks
5. Analyze benchmark construction and hidden assumptions
6. Discuss saturation: when benchmarks stop discriminating
7. Address the gap between benchmark scores and deployment value
8. Close with: benchmarks are necessary but insufficient; understand their limits

**Connections**:
- Back to Ch 11-14 (benchmark results for specific models)
- Forward to Ch 21 (evaluation methodology beyond benchmarks)
- Forward to Ch 22 (confounding in benchmark construction)

---

### Chapter 21: Evaluation Methodology
**Label**: `@sec-eval`  
**Old source**: p5-ch19-eval.qmd (renumbered)

**Conceptual goals**:
- Design proper evaluation protocols for genomic models
- Choose appropriate metrics for different task types
- Avoid common evaluation pitfalls

**Key concepts**:
- Train/validation/test splits in genomic contexts
- Cross-chromosome, cross-gene-family, temporal splits
- Homology-aware clustering (MMseqs2, CD-HIT)
- Metrics: discrimination (AUROC, AUPRC), calibration, clinical utility
- Decision curves and net benefit analysis
- Baseline selection: what to compare against
- Ablation studies: what model components contribute
- Statistical significance and effect sizes

**Pedagogical arc**:
1. Open with the ease of fooling yourself with genomic data
2. Explain why random splits fail (homology leakage)
3. Cover proper splitting strategies
4. Introduce metrics and their appropriate uses
5. Discuss baseline selection: strong baselines, not straw men
6. Cover ablation studies for understanding model components
7. Address statistical considerations
8. Close with: rigorous evaluation is hard; shortcuts produce misleading results

**Connections**:
- Back to Ch 20 (benchmarks as one evaluation approach)
- Forward to Ch 22 (confounding complicates evaluation)
- Forward to Ch 23 (uncertainty in predictions)
- Forward to Ch 25 (clinical evaluation requirements)

---

### Chapter 22: Confounding and Bias
**Label**: `@sec-confounding`  
**Old source**: p5-ch21-confound.qmd (renumbered)

**Conceptual goals**:
- Identify sources of confounding in genomic data and models
- Recognize data leakage patterns specific to genomics
- Apply strategies for detection and mitigation

**Key concepts**:
- Ancestry and population structure confounding
- Batch effects in sequencing and functional genomics
- Technical artifacts masquerading as biology
- Data leakage: label leakage, feature leakage, temporal leakage
- Training data contamination: overlap with evaluation
- Ascertainment bias: well-studied genes, European ancestry enrichment
- Detection strategies: confounder analysis, matched controls
- Mitigation: stratification, correction, causal approaches

**Pedagogical arc**:
1. Open with examples of published models that learned confounders
2. Explain ancestry confounding and why it's pervasive
3. Cover batch effects and technical artifacts
4. Introduce data leakage taxonomy
5. Discuss ascertainment bias in genomic databases
6. Present detection strategies
7. Cover mitigation approaches
8. Close with: confounding is the norm, not the exception; assume it's present

**Connections**:
- Back to Ch 3 (GWAS confounding)
- Back to Ch 4 (circularity in classical VEP)
- Back to Ch 20-21 (confounding in benchmarks and evaluation)
- Forward to Ch 25 (fairness implications of confounding)

---

### Chapter 23: Uncertainty Quantification
**Label**: `@sec-uncertainty`  
**Old source**: **NEW CHAPTER**

**Conceptual goals**:
- Distinguish types of uncertainty in genomic predictions
- Understand calibration and why it matters for decisions
- Apply practical UQ methods to foundation models

**Key concepts**:
- Epistemic vs. aleatoric uncertainty
- Calibration: do confidence scores mean what they say?
- Calibration metrics: ECE, reliability diagrams
- Approaches: ensembles, MC dropout, temperature scaling, conformal prediction
- Out-of-distribution detection: when models don't know
- Selective prediction: abstaining when uncertain
- Communicating uncertainty to users (clinicians, researchers)

**Pedagogical arc**:
1. Open with the clinical need: not just "pathogenic" but "how confident?"
2. Distinguish epistemic (model uncertainty) from aleatoric (data uncertainty)
3. Explain calibration and why most models are miscalibrated
4. Cover calibration assessment methods
5. Introduce UQ approaches for foundation models
6. Discuss OOD detection: recognizing unfamiliar inputs
7. Address selective prediction and abstention
8. Cover communication challenges
9. Close with: uncertainty is essential for trustworthy deployment

**Connections**:
- Back to Ch 14 (VEP uncertainty)
- Back to Ch 21 (calibration metrics in evaluation)
- Forward to Ch 25 (UQ in clinical risk prediction)
- Forward to Ch 26 (uncertainty in variant interpretation)

**Content sources**: This is new content. Draw on: conformal prediction literature, temperature scaling [@guo_calibration_2017], ensemble methods, recent work on LLM calibration.

---

### Chapter 24: Interpretability and Mechanism
**Label**: `@sec-interpretability`  
**Old source**: p5-ch22-interp.qmd (renumbered)

**Conceptual goals**:
- Apply interpretability tools to genomic foundation models
- Distinguish genuine biological insight from pattern matching
- Recognize when interpretability helps vs. provides false comfort

**Key concepts**:
- Attribution methods: saliency maps, integrated gradients
- Attention visualization: what attention weights do and don't mean
- Motif discovery: TF-MoDISco, filter analysis
- Probing classifiers: what representations encode
- Mechanistic interpretability: circuits, features, superposition
- Validation: experimental testing of interpretability claims
- Limitations: post-hoc rationalization, confirmation bias

**Pedagogical arc**:
1. Open with the black box problem and why it matters
2. Cover attribution methods and their genomic applications
3. Discuss attention weights: overinterpreted and underinformative
4. Present motif discovery approaches
5. Introduce probing as diagnostic tool
6. Cover emerging mechanistic interpretability
7. Emphasize validation: interpretability claims need experimental test
8. Close with: interpretability is a tool, not an answer; validate claims

**Connections**:
- Back to Ch 6 (CNN filter interpretation)
- Back to Ch 11-13 (what do FM representations encode?)
- Forward to Ch 26 (interpretability for variant classification)
- Forward to Ch 28 (interpretability for sequence design)

---

## Part VI: Translation

**Part theme**: From models to decisions in research and clinical practice. The goal is impact, not just performance.

**Pedagogical goal**: Readers understand the path from research model to deployed system, including the non-technical barriers (regulatory, organizational, ethical) that determine whether models create value.

**Prerequisites assumed**: Parts I-V content

---

### Chapter 25: Clinical Risk Prediction
**Label**: `@sec-clinical-risk`  
**Old source**: p6-ch23-clinical.qmd (renumbered)

**Conceptual goals**:
- Integrate GFM features into clinical risk models
- Apply rigorous evaluation for clinical deployment
- Address fairness and health equity considerations

**Key concepts**:
- Feature integration: GFM embeddings + clinical variables
- Risk model architectures: survival models, longitudinal models
- Evaluation: discrimination, calibration, decision curves
- External validation: multi-site, prospective studies
- Fairness: equitable performance across populations
- Deployment infrastructure: EHR integration, real-time scoring
- Model monitoring and drift detection

**Pedagogical arc**:
1. Open with the clinical promise: personalized risk stratification
2. Explain how GFM features integrate with clinical data
3. Cover appropriate model architectures
4. Emphasize evaluation: internal, external, prospective
5. Address fairness: the clinical consequences of ancestry bias
6. Discuss deployment practicalities
7. Cover monitoring and maintenance
8. Close with: clinical deployment requires more than good benchmarks

**Connections**:
- Back to Ch 3 (PGS as clinical risk tool)
- Back to Ch 19 (multi-omics integration)
- Back to Ch 21-23 (evaluation, confounding, uncertainty)
- Forward to Ch 26 (variant interpretation in clinical workflow)

---

### Chapter 26: Rare Disease and Variant Interpretation
**Label**: `@sec-rare-disease`  
**Old source**: p6-ch24-variants.qmd (renumbered)

**Conceptual goals**:
- Apply foundation models to rare disease variant prioritization
- Understand ACMG criteria and how computational evidence fits
- Design laboratory validation workflows

**Key concepts**:
- Rare disease diagnostic workflow: exome/genome → candidate variants
- Variant prioritization with FM scores
- ACMG-AMP criteria: computational evidence categories (PP3, BP4)
- Combining evidence: FM scores + population frequency + inheritance
- De novo variant analysis
- Family-based analysis: segregation, compound heterozygosity
- Cancer: somatic variant interpretation
- Laboratory validation: functional assays, CRISPR screens

**Pedagogical arc**:
1. Open with a diagnostic odyssey: the rare disease patient
2. Explain the variant prioritization funnel
3. Show how FM-based VEP fits the workflow
4. Cover ACMG criteria and evidence weighting
5. Discuss family-based analysis approaches
6. Extend to cancer somatic interpretation
7. Address laboratory validation: closing the loop
8. Close with: FMs accelerate prioritization; humans make decisions

**Connections**:
- Back to Ch 4, Ch 14 (VEP methods)
- Back to Ch 23 (uncertainty in variant calls)
- Forward to Ch 29 (regulatory considerations for diagnostics)

---

### Chapter 27: Drug Discovery and Target Identification
**Label**: `@sec-drug-discovery`  
**Old source**: p6-ch25-drugs.qmd (renumbered)

**Conceptual goals**:
- Apply GFMs to drug discovery workflows
- Understand the pharmaceutical industry context
- Navigate build-vs-buy decisions

**Key concepts**:
- Target identification: from GWAS to druggable target
- Functional genomics screens: CRISPR, Perturb-seq
- Biomarker development for patient stratification
- Drug-target interaction prediction
- Toxicity prediction from genomics
- Industry workflows: biotech vs. pharma, timelines, decision gates
- Build vs. buy: when to train in-house vs. use commercial/academic models
- IP and data considerations

**Pedagogical arc**:
1. Open with the drug discovery pipeline and where genomics fits
2. Cover target identification from genetic evidence
3. Discuss functional genomics screens
4. Address biomarker development
5. Extend to DTI and toxicity prediction
6. Explain industry context: different from academic research
7. Discuss build-vs-buy decisions
8. Close with: FMs are tools in a complex pipeline; context matters

**Connections**:
- Back to Ch 3 (GWAS for target ID)
- Back to Ch 16, 18 (perturbation prediction, networks)
- Forward to Ch 28 (sequence design for therapeutics)

---

### Chapter 28: Sequence Design and Engineering
**Label**: `@sec-design`  
**Old source**: p6-ch26-design.qmd (renumbered)

**Conceptual goals**:
- Apply generative foundation models to biological design
- Understand the shift from prediction to generation
- Recognize validation requirements for designed sequences

**Key concepts**:
- Generative models for proteins: ESM-IF, RFdiffusion, generative PLMs
- Protein design: therapeutic proteins, enzymes, binding proteins
- Regulatory element design: promoters, enhancers
- mRNA design: codon optimization, stability engineering
- Antibody and vaccine design
- Closed-loop optimization: design → test → iterate
- Validation: computational → in vitro → in vivo
- Failure modes: mode collapse, distribution shift, unintended properties

**Pedagogical arc**:
1. Open with the paradigm shift: from reading genomes to writing them
2. Cover protein design with generative models
3. Discuss regulatory element design
4. Address mRNA engineering
5. Extend to therapeutic modalities: antibodies, vaccines
6. Explain closed-loop optimization
7. Emphasize validation: computational predictions are hypotheses
8. Close with: generative FMs enable design; biology validates

**Connections**:
- Back to Ch 12 (protein LMs as basis for design)
- Back to Ch 15 (RNA design)
- Back to Ch 24 (interpretability for design guidance)
- Forward to Ch 29 (safety and ethics of designed sequences)

---

### Chapter 29: Regulatory, Ethical, and Future Considerations
**Label**: `@sec-future`  
**Old source**: p6-ch27-future.qmd (**EXPANDED**)

**Conceptual goals**:
- Understand regulatory pathways for genomic AI in clinical settings
- Consider ethical dimensions of genomic foundation models
- Identify open problems and future directions

**Key concepts**:
- Regulatory frameworks: FDA (Software as Medical Device), CE marking, global landscape
- Clinical validation requirements for AI diagnostics
- Data governance: consent, biobank terms, secondary use
- Privacy: genomic data, re-identification, family implications
- IP issues: who owns sequence data, model weights, predictions?
- Responsible AI: transparency, accountability, fairness
- Dual use concerns: biosecurity for generative models
- Open problems: scaling, context, causality, efficiency
- Emerging directions: multimodal, agentic, closed-loop systems

**Pedagogical arc**:
1. Open with the deployment reality: models face non-technical barriers
2. Cover regulatory pathways for clinical AI
3. Discuss data governance and consent
4. Address privacy and genomic data
5. Consider IP and ownership questions
6. Discuss responsible development practices
7. Acknowledge dual use and biosecurity
8. Survey open problems for the field
9. Close with: technical capability is necessary but not sufficient

**Connections**:
- Back to Ch 25-26 (clinical deployment context)
- Back to Ch 28 (generative model risks)

**Migration notes**: Expanded significantly from original "future" chapter to include regulatory and ethical content that was previously missing entirely.

---

## Appendices

### Appendix A: Deep Learning Primer
**Label**: `@sec-apx-dl`  
**Old source**: app-a-dl.qmd (unchanged)

**Purpose**: Provide sufficient ML background for genomics-first readers

**Content**:
- Neural network fundamentals
- Backpropagation and optimization
- Regularization and generalization
- CNN architecture details
- Transformer architecture details
- Training practicalities

---

### Appendix B: Computational Infrastructure
**Label**: `@sec-apx-compute`  
**Old source**: app-b-deployment.qmd (renamed)

**Purpose**: Practical guidance on compute requirements and deployment

**Content**:
- Hardware requirements for training vs. inference
- GPU/TPU considerations
- Cloud vs. on-premise tradeoffs
- Deployment patterns: batch, real-time, embedded
- Cost estimation

---

### Appendix C: Training Data Curation
**Label**: `@sec-apx-data-curation`  
**Old source**: **NEW**

**Purpose**: Guide to constructing training sets for genomic FMs

**Content**:
- Data sources and access
- Quality filtering strategies
- Deduplication and redundancy reduction
- Contamination detection
- Data provenance and versioning
- Bias assessment

---

### Appendix D: Model Reference
**Label**: `@sec-apx-models`  
**Old source**: app-c-model-list.qmd (unchanged)

**Purpose**: Comprehensive reference table of models

**Content**:
- Model name, architecture, scale
- Training data and objective
- Key capabilities and limitations
- Original citation
- Decision guide: which model for which task

---

### Appendix E: Resources
**Label**: `@sec-apx-resources`  
**Old source**: app-d-resources.qmd (unchanged)

**Purpose**: Curated pointers for further learning

**Content**:
- Datasets and data portals
- Software libraries and tools
- Courses and tutorials
- Key papers by topic

---

### Appendix F: Glossary
**Label**: `@sec-apx-glossary`  
**Old source**: app-e-glossary.qmd (unchanged)

**Purpose**: Term definitions spanning all three domains

**Content**:
- Genomics terms
- ML terms
- Clinical terms
- Cross-reference format

---

## Implementation Notes

### Priority Order for Writing

**High priority (structural changes)**:
1. Ch 6: CNN chapter must establish "receptive field ceiling" narrative
2. Ch 10: FM Paradigm needs scaling laws content
3. Ch 14: VEP capstone must synthesize Ch 11-13
4. Ch 17: 3D Genome is entirely new
5. Ch 18: Networks needs FM-as-input reframing
6. Ch 23: Uncertainty is entirely new
7. Ch 29: Regulatory/ethical expansion

**Medium priority (content migration)**:
1. Introduction: update all forward references to new numbering
2. Part introductions: rewrite for new chapter groupings
3. Cross-references throughout: update @sec- labels

**Lower priority (minor updates)**:
1. Renumbered chapters: update internal references
2. Appendix C: new content but lower urgency

### Cross-Reference Updates Required

All chapter cross-references need updating. Key patterns:

| Old Reference | New Reference |
|---------------|---------------|
| @sec-cnn | @sec-cnn (but now Ch 6, not Ch 10) |
| @sec-transformers | @sec-attention |
| @sec-foundation | @sec-fm-principles |
| @sec-pretrain | @sec-pretraining |
| @sec-dna | @sec-dna-lm |
| @sec-prot | @sec-protein-lm |
| @sec-hybrid | @sec-regulatory |
| @sec-epi | @sec-single-cell |
| @sec-systems | @sec-multi-omics |
| @sec-vep | @sec-vep-fm |
| @sec-confound | @sec-confounding |
| @sec-interp | @sec-interpretability |
| @sec-clinical | @sec-clinical-risk |
| @sec-variants | @sec-rare-disease |
| @sec-drugs | @sec-drug-discovery |

### File Naming Convention

Recommended new file names to match structure:

```
p1-ch01-ngs.qmd
p1-ch02-data.qmd
p1-ch03-gwas.qmd
p1-ch04-vep-classical.qmd

p2-ch05-representations.qmd
p2-ch06-cnn.qmd
p2-ch07-attention.qmd
p2-ch08-pretraining.qmd
p2-ch09-transfer.qmd

p3-ch10-fm-principles.qmd
p3-ch11-dna-lm.qmd
p3-ch12-protein-lm.qmd
p3-ch13-regulatory.qmd
p3-ch14-vep-fm.qmd

p4-ch15-rna.qmd
p4-ch16-single-cell.qmd
p4-ch17-3d-genome.qmd
p4-ch18-networks.qmd
p4-ch19-multi-omics.qmd

p5-ch20-benchmarks.qmd
p5-ch21-eval.qmd
p5-ch22-confounding.qmd
p5-ch23-uncertainty.qmd
p5-ch24-interpretability.qmd

p6-ch25-clinical-risk.qmd
p6-ch26-rare-disease.qmd
p6-ch27-drug-discovery.qmd
p6-ch28-design.qmd
p6-ch29-future.qmd

app-a-dl.qmd
app-b-compute.qmd
app-c-data-curation.qmd
app-d-models.qmd
app-e-resources.qmd
app-f-glossary.qmd
```