


# CH 10 (part_3/p3-ch10-fm-principles.qmd) Foundation Model Paradigm {#sec-ch10-fm-principles}
## From Task-Specific Models to Foundation Models {#sec-ch10-task-specific}
## Defining Genomic Foundation Models {#sec-ch10-defining}
### Essential Properties {#sec-ch10-essential-properties}
### What Doesn't Count {#sec-ch10-what-doesnt-count}
### Limitations of the Foundation Model Concept {#sec-ch10-concept-limitations}
## Scaling Laws and Compute-Optimal Training {#sec-ch10-scaling}
### Scaling Law Framework {#sec-ch10-scaling-framework}
 - For variant scaling, add https://www.biorxiv.org/content/10.1101/2025.10.26.684578v1
### Empirical Scaling in Genomic Models {#sec-ch10-empirical-scaling}
### Compute-Optimal Decisions for Genomics {#sec-ch10-compute-optimal}
### Emergent Capabilities {#sec-ch10-emergence}
## A Taxonomy of Genomic Foundation Models {#sec-ch10-taxonomy}
### DNA Language Models {#sec-ch10-dna-lm}
### Sequence-to-Function Foundation Models {#sec-ch10-seq-to-func}
### Variant Effect Prediction Models {#sec-ch10-vep-models}
### Multi-Omic Foundation Models {#sec-ch10-multi-omic}
## Design Dimensions {#sec-ch10-design-dimensions}
 - each subsection is only 1 paragraph; either combine, extend, or x-ref to other existing sections.
### Data Composition {#sec-ch10-data-composition}
### Architecture Choices {#sec-ch10-architecture}
### Context Length {#sec-ch10-context-length}
### Tokenization {#sec-ch10-tokenization}
## Build Versus Use Decisions {#sec-ch10-build-vs-use}
 - section title is ambiguous - use clearer language
### When to Use Existing Models {#sec-ch10-use-existing}
### When to Adapt Existing Models {#sec-ch10-adapt-existing}
### When to Train from Scratch {#sec-ch10-train-scratch}
### Cost-Benefit Analysis {#sec-ch10-cost-benefit}
## Evaluation Principles {#sec-ch10-evaluation}
### Multi-Task Assessment {#sec-ch10-multi-task}
### Transfer Versus Pretraining Performance {#sec-ch10-transfer-eval}
## Foundation Model Ecosystem {#sec-ch10-ecosystem}
### Model Distribution {#sec-ch10-distribution}
### Documentation Requirements {#sec-ch10-documentation}
### Industry and Academic Contributions {#sec-ch10-contributions}
## Open Questions {#sec-ch10-open-questions}
## Convergence Without Consolidation {#sec-ch10-convergence}



# CH 11 (part_3/p3-ch11-dna-lm.qmd) DNA Language Models {#sec-ch11-dna-lm}
## From Task-Specific CNNs to General-Purpose Language Models {#sec-ch11-task-specific-to-general}
 - "Protein language models demonstrated an alternative. ESM and related models trained on massive corpora of protein sequences using masked language modeling (predicting held-out amino acids from context) or autoregressive objectives (predicting the next amino acid)." - Give 1 specific model for MLM and another for Autoregressiev.
## *DNABERT*: The First DNA Language Model {#sec-ch11-dnabert}
## *Nucleotide Transformer*: Scaling Data and Model Diversity {#sec-ch11-nucleotide-transformer}
## *GPN*: Cross-Species Pretraining for Variant Effect Prediction {#sec-ch11-gpn}
## Long-Context Revolution {#sec-ch11-long-context}
### *HyenaDNA*: Megabase Context via Implicit Convolutions {#sec-ch11-hyenadna}
### *Caduceus*: Bidirectional Processing with Reverse-Complement Equivariance {#sec-ch11-caduceus}
### *Evo 2*: Genome-Scale Modeling Across the Tree of Life {#sec-ch11-evo2}
## Training Data and What Models Learn {#sec-ch11-training-data}
### Training Corpus Composition {#sec-ch11-corpus-composition}
### Probing What Models Learn {#sec-ch11-probing}
### What Models Do Not Learn {#sec-ch11-limitations-learned}
## Benchmark Performance and Evaluation {#sec-ch11-benchmarks}
 - X-ref with CH20 where possible.  
### Major Benchmark Suites {#sec-ch11-benchmark-suites}
 - Briefly describe each benchmark suite, but have the details in CH20.  All these benchmarks need to be in cH20
### Benchmark Limitations {#sec-ch11-benchmark-limitations}
## Annotation-Aware Extensions {#sec-ch11-annotation-aware}
## Using DNA Language Models in Practice {#sec-ch11-practical-use}
 - Many of this is in CH5 - CH9.  X-ref to those as the primary source of truth.
### Embeddings as Universal Features {#sec-ch11-embeddings}
### Fine-Tuning and Adaptation {#sec-ch11-fine-tuning}
### Zero-Shot and Few-Shot Scoring {#sec-ch11-zero-shot}
## Limitations and Open Challenges {#sec-ch11-open-challenges}
## Representations Without Predictions {#sec-ch11-soft-landing}


# CH 12 (part_3/p3-ch12-protein-lm.qmd) Protein Language Models {#sec-ch12-protein-lm}
## ESM Model Family {#sec-ch12-esm-family}
 - "Meta AI Research" - should we drop this and other corporate and lab names?
### ESM-1b: Establishing the Paradigm {#sec-ch12-esm1b}
### Emergent Biological Knowledge {#sec-ch12-emergent-knowledge}
### ESM-2: Scaling Up {#sec-ch12-esm2}
 - The ESM-2 table is not helpful as-is.  Likely remove.
## Alternative Architectures {#sec-ch12-alternative-architectures}
 - Call out BFD - is this from AlphaFold or another model.  Mention why it was compiled.
 - For both T5 and XLNet, explain in better details how these models work and differ from BERT 
## Attention and Evolutionary Coupling {#sec-ch12-attention-coupling}
## ESMFold: Structure from Sequence {#sec-ch12-esmfold}
### Alignment-Free Prediction {#sec-ch12-alignment-free}
### What ESMFold Reveals About PLMs {#sec-ch12-esmfold-implications}
 - For the AlphaFold: Structure Prediction Without Foundation Models callout:
   - For SE(3) equivariant - explain what SE(3) means or drop the group theory term
   - It calls out ESMFold only needing 1 sequence while AlphaFold needs MSA.  Validate if ESMFold is trained on MSAs or is truely MSA-free.  Also clarify that AlphaFold can also predict from single sequences, but with lower accuracy.  AlphaFold also uses crystal templates, so mention that as well.
   - Make sure content outside of sidebar doesn't repeat what's in the sidebar.
   - Drop the meta-commentary, like "this book".

## Function Prediction {#sec-ch12-function-prediction}
 - 1st paragraph, 2nd sentence: "Function prediction ..." - this is a very long sentence.  Break it up.
## Variant Effect Prediction {#sec-ch12-variant-effects}
## Integration with Structure Prediction {#sec-ch12-structure-integration}
## Limitations {#sec-ch12-limitations}
 - Each subsection is only 1 paragraph; either combine, extend, or x-ref to other existing sections.
### Orphan and Dark Proteins {#sec-ch12-orphan-proteins}
### Novel Folds {#sec-ch12-novel-folds}
### Conformational Flexibility {#sec-ch12-conformational-flexibility}
### Epistasis {#sec-ch12-epistasis}
### Interpretability {#sec-ch12-interpretability}
## Lessons for Genomic Foundation Models {#sec-ch12-lessons}
### Self-Supervised Biological Knowledge {#sec-ch12-self-supervised}
### Scaling Benefits {#sec-ch12-scaling}
### Effective Transfer Learning {#sec-ch12-transfer}
### Architecture-Sequence Matching {#sec-ch12-architecture-matching}
### Integration Benefits {#sec-ch12-integration}
## Paradigm That Generalized {#sec-ch12-conclusion}


# CH 13 (part_3/p3-ch13-regulatory.qmd) Regulatory Models {#sec-ch13-regulatory}
 - These paragraphs are just confusing to read: "A model that processes sequences in kilobase windows treats regulatory elements tens of kilobases away as if they do not exist. For understanding human gene regulation, they effectively do not."

 - using "regulatory model" here, while in other places we use "sequence-to-function model" (e.g ch10) - be consistent.  If regulatory model is a subset of sequence-to-function model, clarify that.  Maybe call out the sequence -> molecular function -> cellular function -> clinical phenotype hierarchy again???

 - Somewhere in the chapter, add a sidebar on regulatory genomics experimental assays (ChIP-seq, ATAC-seq, Hi-C, STARR-seq, etc) and what they measure.  This is only briefly mentioned in CH4, but would be helpful to have a more complete overview here.  Draw from CH4 content, but expand it.  Don't get too deep, just a high-level overview.


## Long-Range Regulation Problem {#sec-ch13-long-range}
 - Attention scaling repeated here from previous chapters, but probably bears repeating in this context.  Validate
## *Enformer*: Attention Meets Regulatory Genomics {#sec-ch13-enformer}
### Architecture {#sec-ch13-enformer-architecture}
### Training Data and Cross-Species Learning {#sec-ch13-enformer-training}
### Variant Effect Prediction {#sec-ch13-enformer-vep}
## *Borzoi*: From Chromatin to Transcriptome {#sec-ch13-borzoi}
### Beyond Transcription Initiation {#sec-ch13-borzoi-transcription}
### Predicting Coverage at Nucleotide Resolution {#sec-ch13-borzoi-coverage}
### Applications Beyond Expression Level {#sec-ch13-borzoi-applications}
## *Sei*: A Regulatory Vocabulary from Sequence {#sec-ch13-sei}
### Discrete Regulatory States {#sec-ch13-sei-states}
### Complementary to Track Prediction {#sec-ch13-sei-complementary}
## *AlphaGenome*: Unifying Modalities at Megabase Scale {#sec-ch13-alphagenome}
### From 200kb to One Megabase {#sec-ch13-alphagenome-scale}
### Closed Weights, Open Questions {#sec-ch13-alphagenome-access}
 - call out that API also doesn't provide embeddings for downstream use
## What Hybrid Architectures Accomplish {#sec-ch13-accomplishments}
### Spanning Enhancer-Promoter Distances {#sec-ch13-spanning}
### Multi-Task Regularization {#sec-ch13-multitask}
### Cross-Species Constraints {#sec-ch13-cross-species}
### Unified Variant Effect Prediction {#sec-ch13-unified-vep}
## Limitations and Open Challenges {#sec-ch13-limitations}
### Training Data Constraints {#sec-ch13-training-bias}
### Finite Context {#sec-ch13-finite-context}
### Missing Three-Dimensional Context {#sec-ch13-missing-3d}
### Correlation Versus Causation {#sec-ch13-correlation}
### Interpretability Challenges {#sec-ch13-interpretability}
## Relationship to Foundation Models {#sec-ch13-foundation-models}
## Prediction Without Explanation {#sec-ch13-prediction-explanation}


# CH 14 (part_3/p3-ch14-vep-fm.qmd) Variant Effect Prediction {#sec-ch14-vep-fm}
## Foundation Model Paradigm for Variant Interpretation {#sec-ch14-fm-paradigm} 
 - cite CADD
 - use a different term than "developers".  Maybe "researchers" or "model builders".
### Zero-Shot and Supervised Approaches {#sec-ch14-zeroshot-supervised}
## Protein-Based Variant Effect Prediction {#sec-ch14-protein-vep}
 - "evolution has already tested billions of amino acid substitutions across millions of years" - shouldn't this be trillions of substitutions over billions of years?
### Zero-Shot Scoring with Protein Language Models {#sec-ch14-zeroshot-plm}
 - Be sure not to repeat ch12 and ch09 on zero-shot prediciton.  X-ref to those chapters as primary source of truth.
 - I would like to have a deep dive (maybe as a sidebar) into zero-shot likelihood calculations.  Meier et al. (ESM-1v) hase a suplemental section A on Extraction Methods that goes over many likelihood calculation methods (maskde marginal; mutant marginal; wildtype marginal; pseudolikelihood).  Also see if other paper have different methods.
### Alignment-Based Models: EVE and popEVE {#sec-ch14-alignment-models}
### AlphaMissense: Structure-Informed Pathogenicity Prediction {#sec-ch14-alphamissense}
 - referes to a "PLM" used for training.  Do we know what this is? ESM?  custom PLM like ESM?
## DNA-Based Variant Effect Prediction {#sec-ch14-dna-vep}
### Splice Variant Prediction with SpliceAI {#sec-ch14-spliceai}
 - Refer to 14.5.3 (Mapping to ACMG Categories) when discussing how SpliceAI scores are mapped to clinical categories.
### Regulatory Variant Prediction with Enformer {#sec-ch14-enformer-vep}
### DNA Language Models: GPN-MSA and Evo 2 {#sec-ch14-dna-lm-vep}
### AlphaGenome: Unified Multi-Omic Variant Effect Prediction {#sec-ch14-alphagenome}
## Combining Evidence Across Modalities {#sec-ch14-combining-evidence}
### Integration Strategies {#sec-ch14-integration-strategies}
### Avoiding Double-Counting {#sec-ch14-double-counting}
 - Reference ACMG to 14.5.3 as well.  Reduce redundancy.
### Practical Workflow Design {#sec-ch14-workflow-design}
## Calibration and Clinical Categories {#sec-ch14-calibration}
### Assessing Calibration {#sec-ch14-assessing-calibration}
### Calibration Methods for Variant Effect Prediction {#sec-ch14-calibration-methods}
### Mapping to ACMG Categories {#sec-ch14-acmg-mapping}
 - For Pejaver et al, select models from this that are discussed most in the book (e.g CADD, REVEL, etc.:): CADD,14 Evolutionary Action (EA),15 FATHMM,16 GERP++,17 MPC,18 MutPred2,19 PhyloP,20 PolyPhen-2 (HumVar model),21 PrimateAI,22 REVEL,23 SIFT,24 and VEST4.25 

  - At some point in the book, add a ACMG sidebar that summarizes the ACMG guidelines for clinical variant interpretation.  This can be referenced in multiple chapters.  Double check I haven't already done this.
### The Challenge of Uncertain Significance {#sec-ch14-vus-challenge}
## Uncertainty Quantification {#sec-ch14-uncertainty}
 - Make sure this section doesn't repeat content from CH23 on uncertainty quantification.  X-ref to that chapter as primary source of truth.
### Sources of Uncertainty {#sec-ch14-uncertainty-sources}
### Uncertainty Estimation Methods {#sec-ch14-uncertainty-methods}
 - Clarify terms like "calibration set", "large prediciton set", single-element sets.
### Out-of-Distribution Detection {#sec-ch14-ood-detection}
 - define or clarify "low embedding density"
## What Foundation Models Add {#sec-ch14-fm-gains}
### Improved Discrimination {#sec-ch14-improved-discrimination}
 - cite "better performance"
### Extended Coverage {#sec-ch14-extended-coverage}
### Mechanistic Interpretability {#sec-ch14-mechanistic-interpretability}
### Persistent Limitations {#sec-ch14-persistent-limitations}
## Clinical Integration Considerations {#sec-ch14-clinical-integration}
### Laboratory Validation {#sec-ch14-lab-validation}
 - 1st paragraph is organized weird with 3 parenthetical questions.
### Workflow Integration {#sec-ch14-workflow-integration}
### Communication to Clinicians {#sec-ch14-clinical-communication}
## Open Challenges {#sec-ch14-open-challenges}
### Complex Variant Types {#sec-ch14-complex-variants}
### Combinatorial Effects {#sec-ch14-combinatorial}
### Phenotype Specificity {#sec-ch14-phenotype-specificity}
### Temporal and Environmental Context {#sec-ch14-temporal-context}
### Equity and Access {#sec-ch14-equity}
- "Training data composition determines which patients foundation models serve well. " is a clunking sentence.  Rephrase..
- "diverse urban" - is this the best way to describe this?  Could be misinterpreted.  Maybe "cosmopolitan" or "heterogeneous"?
## Tools for Interpretation, Not Oracles {#sec-ch14-conclusion}


# CH 15 (part_4/p4-ch15-rna.qmd) RNA Structure and Function {#sec-ch15-rna}
## RNA as Molecule Versus Transcriptome Readout {#sec-ch15-perspectives}
## Why Secondary Structure Creates a Distinct Modeling Challenge {#sec-ch15-structure-challenge}
### Flat Energy Landscape Problem {#sec-ch15-energy-landscape}
### Base Pairing and Long-Range Dependencies {#sec-ch15-base-pairing}
### Pseudoknots and Tertiary Complexity {#sec-ch15-pseudoknots}
## Classical Approaches to Structure Prediction {#sec-ch15-classical}
### Thermodynamic Folding Models {#sec-ch15-thermodynamic}
### Comparative and Covariation Methods {#sec-ch15-comparative}
## Deep Learning for Secondary Structure Prediction {#sec-ch15-dl-structure}
### From Thermodynamics to Learned Patterns {#sec-ch15-learned-patterns}
### Structure Probing as Supervision {#sec-ch15-structure-probing}
## RNA Foundation Models {#sec-ch15-foundation}
### Scale Gap with Protein Language Models {#sec-ch15-scale-gap}
### Architectures and Objectives {#sec-ch15-architectures}
### Downstream Applications {#sec-ch15-downstream}
## Codon-Level Models for Coding RNA {#sec-ch15-codon}
### Beyond Nucleotide Tokenization {#sec-ch15-codon-tokenization}
### What Codon Models Add {#sec-ch15-codon-advantages}
## UTR Models and Translation Regulation {#sec-ch15-utr}
### Why UTRs Dominate Expression Control {#sec-ch15-utr-control}
### Sequence-to-Expression Models {#sec-ch15-expression-models}
### Integration with mRNA Design {#sec-ch15-utr-design}
## mRNA Design and Optimization {#sec-ch15-mrna-design}
### Design Objectives and Trade-offs {#sec-ch15-design-objectives}
### Lessons from COVID-19 Vaccines {#sec-ch15-covid-vaccines}
### Model-Based Design Strategies {#sec-ch15-model-design}
## Noncoding RNA Classification and Function {#sec-ch15-ncrna}
### Diversity of Noncoding RNA {#sec-ch15-ncrna-diversity}
### From Handcrafted Features to Learned Representations {#sec-ch15-ncrna-features}
## miRNA Target Prediction {#sec-ch15-mirna}
## Splicing and Transcript Processing Models {#sec-ch15-splicing}
### Beyond SpliceAI {#sec-ch15-beyond-spliceai}
## Limitations and Open Challenges {#sec-ch15-limitations}
### Sparse Structural Data {#sec-ch15-sparse-data}
### Functional Annotation Gaps {#sec-ch15-annotation-gaps}
### Maturity Gap {#sec-ch15-maturity-gap}
## Bridge Between Sequence and Cell {#sec-ch15-bridge}


# CH 16 (part_4/p4-ch16-single-cell.qmd) Single-Cell Models {#sec-ch16-single-cell}
## Single-Cell Data Landscape {#sec-ch16-data}
### From Bulk to Single-Cell Resolution {#sec-ch16-bulk-to-sc}
### Technical Challenges and Data Characteristics {#sec-ch16-technical}
## Cellular Language Models {#sec-ch16-clm}
### *Geneformer*: Learning Network Biology {#sec-ch16-geneformer}
### *scGPT*: Generative Pretraining for Single-Cell Analysis {#sec-ch16-scgpt}
### *scFoundation* and Scaling Single-Cell Models {#sec-ch16-scfoundation}
### *TranscriptFormer*: Cross-Species Cellular Models {#sec-ch16-transcriptformer}
## Perturbation Response Prediction {#sec-ch16-perturbation}
### *In Silico* Experiment Promise {#sec-ch16-in-silico}
### Perturb-seq and Foundation Model Training {#sec-ch16-perturb-seq}
### Limitations of Current Approaches {#sec-ch16-perturbation-limits}
## Epigenomic Foundation Models {#sec-ch16-epigenomic}
### DNA Methylation and *CpGPT* {#sec-ch16-methylation}
### Chromatin Accessibility Models {#sec-ch16-accessibility}
## Cross-Modality Integration {#sec-ch16-integration}
### Unpaired Integration Challenge {#sec-ch16-unpaired}
### *GLUE*: Graph-Linked Unified Embedding {#sec-ch16-glue}
### Applications of Cross-Modal Integration {#sec-ch16-cross-modal-apps}
## Practical Challenges and Limitations {#sec-ch16-limitations}
### Batch Effects and Technical Artifacts {#sec-ch16-batch-effects}
### Cell Type Imbalance {#sec-ch16-imbalance}
### Evaluation Complexity {#sec-ch16-evaluation}
### Causality and Mechanism {#sec-ch16-causality}
## From Sequence to State {#sec-ch16-conclusion}


# CH 17 (part_4/p4-ch17-3d-genome.qmd) 3D Genome Organization {#sec-ch17-3d-genome}
## Chromatin Organization Hierarchy {#sec-ch17-chromatin-hierarchy}
### Chromosome Territories and Compartments {#sec-ch17-territories-compartments}
### Topologically Associating Domains {#sec-ch17-tads}
### Loop Extrusion Mechanism {#sec-ch17-loop-extrusion}
### Fine-Scale Chromatin Loops {#sec-ch17-fine-scale-loops}
## Measuring the 3D Genome {#sec-ch17-3d-measurement}
### Hi-C and Contact Matrices {#sec-ch17-hic-matrices}
### Resolution and Data Resources {#sec-ch17-3d-data-resources}
## Predicting 3D Structure from Sequence {#sec-ch17-3d-prediction}
### *Akita* and Dilated Convolutions {#sec-ch17-akita}
### *Orca* and Multiscale Prediction {#sec-ch17-orca}
### *C.Origami* and Cross-Cell-Type Transfer {#sec-ch17-c-origami}
### Learned Sequence Determinants {#sec-ch17-3d-interpretability}
## 3D Structure and Gene Regulation {#sec-ch17-3d-regulation}
### Beyond One-Dimensional Models {#sec-ch17-beyond-1d}
### Structural Variant Interpretation {#sec-ch17-sv-interpretation}
### Causality and Permissive Architecture {#sec-ch17-3d-causality}
## Spatial Transcriptomics {#sec-ch17-spatial-transcriptomics}
### Measurement Technologies {#sec-ch17-spatial-technologies}
### Computational Challenges {#sec-ch17-spatial-computation}
### Spatial Foundation Models {#sec-ch17-spatial-models}
## Limitations and Open Questions {#sec-ch17-3d-limitations}
## Structure as Context, Not Cause {#sec-ch17-structure-context}


# CH 18 (part_4/p4-ch18-networks.qmd) Graph and Network Models {#sec-ch18-networks}
## Biological Networks and Data Resources {#sec-ch18-biological-networks}
### Landscape of Biological Graphs {#sec-ch18-landscape}
### Biases and Limitations {#sec-ch18-network-biases}
## Graph Neural Network Fundamentals {#sec-ch18-gnn-fundamentals}
### Message Passing Principles {#sec-ch18-message-passing}
### Canonical Architectures {#sec-ch18-canonical-architectures}
## Foundation Model Embeddings as Node Features {#sec-ch18-fm-embeddings}
### Integration Principle {#sec-ch18-integration-principle}
### Practical Integration Patterns {#sec-ch18-practical-patterns}
### Evidence for the Integration Benefit {#sec-ch18-integration-evidence}
## Applications {#sec-ch18-applications}
### Disease Gene Prioritization {#sec-ch18-disease-gene}
### Drug-Target Interaction Prediction {#sec-ch18-drug-target}
### Knowledge Graph Reasoning and Drug Repurposing {#sec-ch18-kg-reasoning}
### Pathway and Module Analysis {#sec-ch18-pathway-analysis}
### Cell Type and State Annotation {#sec-ch18-cell-annotation}
## Practical Considerations {#sec-ch18-practical}
### Graph Construction Quality {#sec-ch18-graph-construction}
### Scalability and Mini-Batching {#sec-ch18-scalability}
### Robustness to Noise and Missingness {#sec-ch18-robustness}
### Interpretation and Validation {#sec-ch18-interpretation}
## Limitations and Open Challenges {#sec-ch18-limitations}
### Study Bias Problem {#sec-ch18-study-bias}
### Causality Versus Association {#sec-ch18-causality}
### Negative Data and Class Imbalance {#sec-ch18-negative-data}
### Distribution Shift {#sec-ch18-distribution-shift}
## Sequence Encodes, Structure Connects {#sec-ch18-conclusion}


# CH 19 (part_4/p4-ch19-multi-omics.qmd) Multi-Omics Integration {#sec-ch19-multi-omics}
## Limits of Single-Modality Models {#sec-ch19-limits}
## Integration Strategies and Their Tradeoffs {#sec-ch19-strategies}
### Early Fusion {#sec-ch19-early-fusion}
### Late Fusion {#sec-ch19-late-fusion}
### Intermediate Fusion {#sec-ch19-intermediate-fusion}
## Multi-Omics Foundation Models {#sec-ch19-foundation-models}
### Factor-Based Integration {#sec-ch19-factor-integration}
### Deep Generative Multi-Omics Models {#sec-ch19-deep-generative}
### Contrastive Multi-Modal Learning {#sec-ch19-contrastive}
## Clinical Integration: EHR, Imaging, and Molecular Data {#sec-ch19-clinical-integration}
### Electronic Health Records as a Modality {#sec-ch19-ehr}
### Imaging Integration {#sec-ch19-imaging}
### Multi-Modal Clinical Prediction Models {#sec-ch19-multimodal-clinical}
## Systems View: From Variant to Phenotype {#sec-ch19-systems-view}
### Information Cascade {#sec-ch19-information-cascade}
### Bottleneck Modalities {#sec-ch19-bottleneck}
### Causal vs. Correlational Integration {#sec-ch19-causal-correlational}
## Handling Missing Modalities {#sec-ch19-missing-modalities}
### Training with Incomplete Data {#sec-ch19-incomplete-training}
### Cross-Modal Imputation {#sec-ch19-imputation}
### Zero-Shot Cross-Modal Transfer {#sec-ch19-zero-shot}
## Practical Challenges {#sec-ch19-practical-challenges}
### Batch Effects Across Modalities {#sec-ch19-batch-effects}
### Sample Size and Power {#sec-ch19-sample-size}
### Interpretability Across Modalities {#sec-ch19-interpretability}
### Evaluation Complexity {#sec-ch19-evaluation}
## Integration as Means, Not End {#sec-ch19-conclusion}


# CH 20 (part_5/p5-ch20-benchmarks.qmd) Benchmarks {#sec-ch20-benchmarks}
## Protein Language Model Benchmarks {#sec-ch20-protein-benchmarks}
### TAPE: Tasks Assessing Protein Embeddings {#sec-ch20-tape}
### FLIP: Function-Linked Protein Benchmark {#sec-ch20-flip}
### ProteinGym: Comprehensive Variant Effect Evaluation {#sec-ch20-proteingym}
### Structure Prediction Benchmarks {#sec-ch20-structure-benchmarks}
## DNA and Regulatory Benchmarks {#sec-ch20-dna-benchmarks}
### Classical Regulatory Prediction Tasks {#sec-ch20-classical-regulatory}
### Quantitative Regulatory Prediction {#sec-ch20-quantitative-regulatory}
### Genomic Benchmarks {#sec-ch20-genomic-benchmarks}
### BEND: Benchmark for DNA Language Models {#sec-ch20-bend}
### Long-Range Benchmarks {#sec-ch20-long-range}
### Cross-Species Evaluation {#sec-ch20-cross-species}
## Variant Effect Prediction Benchmarks {#sec-ch20-vep-benchmarks}
### Clinical Variant Databases {#sec-ch20-clinical-databases}
### CAGI: Critical Assessment of Genome Interpretation {#sec-ch20-cagi}
### Deep Mutational Scanning Benchmarks {#sec-ch20-dms-benchmarks}
### Regulatory and Non-Coding Variant Benchmarks {#sec-ch20-noncoding-benchmarks}
## Trait and Population-Level Benchmarks {#sec-ch20-trait-benchmarks}
### Polygenic Score Evaluation {#sec-ch20-pgs-evaluation}
### TraitGym {#sec-ch20-traitgym}
### EmbedGEM Framework {#sec-ch20-embedgem}
## Benchmark Construction and Hidden Assumptions {#sec-ch20-benchmark-construction}
### Data Sources and Label Provenance {#sec-ch20-label-provenance}
### Splitting Strategies and Leakage {#sec-ch20-splitting}
### Metric Selection and Aggregation {#sec-ch20-metrics}
### Goodhart's Law and Benchmark Gaming {#sec-ch20-goodhart}
## Benchmark Saturation and Staleness {#sec-ch20-saturation-staleness}
### Saturation: When Benchmarks Stop Discriminating {#sec-ch20-saturation}
### Staleness: When Benchmarks Diverge from Practice {#sec-ch20-staleness}
### Leakage from Scale {#sec-ch20-leakage-scale}
## Benchmark-Deployment Gap {#sec-ch20-deployment-gap}
### Distribution Shift {#sec-ch20-distribution-shift}
### Calibration Requirements {#sec-ch20-calibration-requirements}
### Metric Mismatch {#sec-ch20-metric-mismatch}
### Practical Constraints {#sec-ch20-practical-constraints}
## Systematic Gaps in Current Benchmarks {#sec-ch20-systematic-gaps}
## The Proxy Problem {#sec-ch20-proxy-problem}