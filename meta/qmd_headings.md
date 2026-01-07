
### appendix/app-a-dl.qmd
# Deep Learning Primer {#sec-apx-a-dl}
## Neural Networks as Function Approximators {#sec-apx-a-nn-basics}
### The Perceptron and Linear Layers
### Activation Functions
### Depth and Width
## Training Neural Networks {#sec-apx-a-training}
### Loss Functions
### Gradient Descent and Backpropagation
### Stochastic Gradient Descent and Minibatches
### Optimizers
### Regularization
## Convolutional Neural Networks {#sec-apx-a-cnn}
### Convolution Operation
### Key CNN Components
### CNNs for Genomics
## Recurrent Neural Networks {#sec-apx-a-rnn}
### LSTM and GRU
### Limitations
## Attention and Transformers {#sec-apx-a-attention}
### Self-Attention
### Multi-Head Attention
### Transformer Architecture
### Positional Encoding
### Encoder vs. Decoder
### Computational Complexity
## Embeddings and Representations {#sec-apx-a-embeddings}
### Token Embeddings
### Contextual Embeddings
## Pretraining and Transfer Learning {#sec-apx-a-pretraining}
### Self-Supervised Objectives
### Transfer Learning
## Practical Considerations {#sec-apx-a-practical}
### Hardware Requirements
### Software Frameworks
### Common Pitfalls
## Further Reading {#sec-apx-a-further}

### appendix/app-b-compute.qmd
# Deployment and Compute {#sec-apx-b-compute}
## Hardware Landscape {#sec-apx-b-hardware}
### GPU Computing
### Consumer vs. Data Center GPUs
### TPUs
### Multi-GPU and Distributed Training
### CPU Inference
## Cloud Platforms {#sec-apx-b-cloud}
### Major Providers
### Cost Considerations
### Managed ML Platforms
## Model Deployment {#sec-apx-b-deployment}
### Inference Servers
### API Design
# Request
# Response
### Containerization
### Kubernetes Deployment
## Inference Optimization {#sec-apx-b-optimization}
### Quantization
### Model Pruning
### Knowledge Distillation
### ONNX and TensorRT
### Caching and Batching
## Benchmarking and Monitoring {#sec-apx-b-monitoring}
### Performance Metrics
### Monitoring Stack
### Load Testing
# Example with locust
## Cost Optimization {#sec-apx-b-cost}
### Right-Sizing
### Autoscaling
# Kubernetes HPA example
### Batch Processing
### Model Selection
## Security Considerations {#sec-apx-b-security}
### Data Privacy
### Model Security
### Federated Learning
## Reference Architecture {#sec-apx-b-architecture}
## Checklist for Production Deployment {#sec-apx-b-checklist}

### appendix/app-c-data-curation.qmd
# Data Curation {#sec-apx-c-data-curation}
## Data Sources {#sec-apx-c-sources}
### Reference Genomes and Assemblies
### Population-Scale Sequencing
### Protein Sequence Databases
### Functional Annotation
### Clinical Variant Databases
### Access and Licensing
## Quality Filtering {#sec-apx-c-quality}
### Sequence Quality Filters
### Variant Quality Filters
### Annotation Quality
### Handling Missing Data
## Deduplication {#sec-apx-c-dedup}
### Exact Deduplication
### Near-Duplicate Detection
# Cluster at 90% sequence identity
# Cluster at 50% identity (requires different word size)
### Redundancy Levels
### Train-Test Deduplication
## Contamination Detection {#sec-apx-c-contamination}
### Types of Contamination
### Screening Approaches
# Screen against human genome for non-human samples
### Benchmark Contamination
## Data Provenance {#sec-apx-c-provenance}
### Metadata Requirements
### Documentation Template
# data_manifest.yaml
### Version Control
## Bias Assessment {#sec-apx-c-bias}
### Population Bias
### Gene Coverage Bias
### Ascertainment Bias
### Label Bias
## Building Training Sets {#sec-apx-c-building}
### Step 1: Define Scope
### Step 2: Identify Sources
### Step 3: Download and Verify
# Download with verification
# Document in manifest
### Step 4: Quality Filter
### Step 5: Deduplicate
### Step 6: Split Data
### Step 7: Assess Bias
### Step 8: Document
## Data Cards {#sec-apx-c-datacards}
# Dataset: VariantBench-v2
## Overview
## Sources
## Curation
## Known Biases
## Intended Use
## Updates
## Checklist {#sec-apx-c-checklist}

### appendix/app-d-models.qmd
# Model Reference {#sec-apx-d-models}
## DNA Language Models {#sec-apx-d-dna-lm}
### Model Access
## Protein Language Models {#sec-apx-d-plm}
### Model Access
## Sequence-to-Function Models {#sec-apx-d-seq2func}
### Model Access
## Splice Prediction Models {#sec-apx-d-splice}
### Model Access
## Variant Effect Predictors {#sec-apx-d-vep}
### Integrative Scores
### Protein Language Model–Based
### Conservation-Based
### Model Access
## Structure Prediction {#sec-apx-d-structure}
### Model Access
## Single-Cell and Multi-Omics Models {#sec-apx-d-singlecell}
## Polygenic and Clinical Models {#sec-apx-d-clinical}
## Category Definitions {#sec-apx-d-categories}
## Practical Considerations {#sec-apx-d-practical}
### Selecting a Model
### Model Versioning

### appendix/app-e-resources.qmd
# Resources {#sec-apx-e-resources}
## Textbooks {#sec-apx-e-textbooks}
### Genomics and Human Genetics
### Immunology
### Machine Learning and Deep Learning
### Bioinformatics and Computational Biology
## Online Courses {#sec-apx-e-courses}
### Machine Learning and Deep Learning
### Genomics and Bioinformatics
### Applied Genomic ML
## Genomic Databases {#sec-apx-e-databases}
### Variant and Population Databases
### Functional Annotation Databases
### Protein Databases
### Gene and Pathway Databases
### Single-Cell Databases
## Software Tools {#sec-apx-e-software}
### Sequence Analysis
### Variant Annotation
### Deep Learning Frameworks
### Genomic ML Libraries
### Workflow Management
## Benchmarks and Datasets {#sec-apx-e-benchmarks}
### Genomic Benchmarks
### Variant Datasets
## Community and Forums {#sec-apx-e-community}
### Discussion Forums
### Preprint Servers
### Conferences
### Key Research Groups
## Keeping Current {#sec-apx-e-current}

### appendix/app-f-glossary.qmd
# Glossary {#sec-apx-f-glossary}
## Terms (A–Z)

### bib/references.qmd
# References {.unnumbered}

### index.qmd
# Introduction {.unnumbered}
## Why Foundation Models for Genomics?
## Recurring Themes
## Typography and Formatting {.unnumbered}
## Structure and Organization
## A Framework, Not a Snapshot

### preface.qmd
# Preface {.unnumbered}
## Why I Wrote This Book
## How This Book Came Together
## How to Read This Book
## What This Book Assumes (and What It Does Not)
## A Note on Scope and Opinions
## Acknowledgements

### part_1/p1--foundations.qmd
# Part I: Data Foundations {.unnumbered}

### part_1/p1-ch01-ngs.qmd
# From Reads to Variants {#sec-ch01-ngs}
## NGS Data Challenges {#sec-ch01-challenges}
## Targeting Strategies: Panels, Exomes, and Genomes {#sec-ch01-targeting}
### Targeted and Panel Sequencing {#sec-ch01-panels}
### Whole-Exome Sequencing {#sec-ch01-wes}
### Whole-Genome Sequencing {#sec-ch01-wgs}
### Long-Read Sequencing Technologies {#sec-ch01-longread}
## Classical Variant Calling Pipelines {#sec-ch01-classical}
### From Sequencer to Aligned Reads {#sec-ch01-alignment}
### Per-Sample Variant Calling {#sec-ch01-persample}
### Cohort Calling and Filtering {#sec-ch01-cohort}
### Sample-Level Quality Control {#sec-ch01-qc}
## Haplotype Phasing {#sec-ch01-phasing}
### Clinical and Analytical Importance {#sec-ch01-phasing-importance}
### Phasing Methods {#sec-ch01-phasing-methods}
### Phasing Approaches {#sec-ch01-phasing-approaches}
### Genotype Imputation and Refinement {#sec-ch01-imputation}
### Hybrid Sequencing and Coverage Boosting {#sec-ch01-hybrid}
## Sources of Error and Uncertainty {#sec-ch01-errors}
### Mapping Ambiguity and Reference Bias {#sec-ch01-mapping-bias}
### Systematic Sequencing Artifacts {#sec-ch01-artifacts}
### Coverage Gaps and Allelic Imbalance {#sec-ch01-coverage}
### Complex Variants and Representation {#sec-ch01-complex}
## Difficult Regions: The Limits of Short-Read Calling {#sec-ch01-difficult}
### Segmental Duplications and Gene Families {#sec-ch01-segdup}
### Low-Complexity and Repetitive Sequence {#sec-ch01-repeats}
### HLA Region Complexity {#sec-ch01-hla}
## Benchmarking and Ground Truth {#sec-ch01-benchmarks}
### GIAB Reference Samples {#sec-ch01-giab}
### Metrics and Their Meaning {#sec-ch01-metrics}
### Limitations of Benchmarks {#sec-ch01-benchmark-limits}
## DeepVariant: Variant Calling as Image Classification {#sec-ch01-deepvariant}
### Pileup Images as Input {#sec-ch01-pileup}
### Architecture and Training {#sec-ch01-deepvariant-arch}
### Cohort Calling with GLnexus {#sec-ch01-glnexus}
### Comparison with Classical Approaches {#sec-ch01-deepvariant-comparison}
## Implications for Genomic Deep Learning {#sec-ch01-implications}
### Variants as Atomic Units {#sec-ch01-atomic}
### Inherited Biases and Blind Spots {#sec-ch01-inherited}
### Effect Sizes Across the Frequency Spectrum {#sec-ch01-effect-sizes}
## Reliability Landscape {#sec-ch01-reliability}

### part_1/p1-ch02-data.qmd
# Data Landscape {#sec-ch02-data}
## Reference Genomes and Gene Annotations {#sec-ch02-reference}
### Reference Assemblies {#sec-ch02-reference-assemblies}
### Gene Models {#sec-ch02-gene-models}
## Population Variant Catalogs and Allele Frequencies {#sec-ch02-population}
### dbSNP and Variant Identifiers {#sec-ch02-dbsnp}
### 1000 Genomes and Early Reference Panels {#sec-ch02-1000genomes}
### Genome Aggregation Database (gnomAD) {#sec-ch02-gnomad}
## Biobanks and GWAS Data {#sec-ch02-biobanks}
### Large Population Cohorts {#sec-ch02-cohorts}
### GWAS Summary Statistics {#sec-ch02-gwas-summary}
## Functional Genomics and Regulatory Landscapes {#sec-ch02-functional}
### ENCODE, Roadmap, and Related Consortia {#sec-ch02-encode}
### Cistrome Data Browser {#sec-ch02-cistrome}
### From Assays to Training Labels {#sec-ch02-assays-labels}
### Deep Mutational Scanning and Multiplexed Variant Assays {#sec-ch02-dms}
## Expression and eQTL Resources {#sec-ch02-expression}
### Bulk Expression Atlases {#sec-ch02-gtex}
### Single-Cell and Context-Specific Expression {#sec-ch02-single-cell}
## Protein Databases {#sec-ch02-protein-databases}
### Sequence Databases {#sec-ch02-protein-sequence}
### Structure Databases {#sec-ch02-protein-structure}
## Phenotype Definition and Data Quality {#sec-ch02-phenotypes}
### Problem of Binary Disease Definitions {#sec-ch02-binary-phenotypes}
### Electronic Health Record Quality and Completeness {#sec-ch02-ehr}
### Coding Inconsistencies and Label Noise {#sec-ch02-label-noise}
### Deep Phenotyping Approaches {#sec-ch02-deep-phenotyping}
### Impact on Downstream Modeling {#sec-ch02-phenotype-impact}
## Variant Interpretation Databases and Clinical Labels {#sec-ch02-clinical}
### ClinVar and Clinical Assertions {#sec-ch02-clinvar}
### Complementary Clinical Databases {#sec-ch02-clinical-other}
### ClinGen and Expert Curation {#sec-ch02-clingen}
### Pharmacogenomics Resources {#sec-ch02-pharmacogenomics}
## Inherited Constraints {#sec-ch02-constraints}

### part_1/p1-ch03-gwas.qmd
# GWAS and Polygenic Scores {#sec-ch03-gwas}
## GWAS Framework {#sec-ch03-gwas-framework}
### Association Models for Quantitative Traits {#sec-ch03-linear-models}
### Association Models for Disease Outcomes {#sec-ch03-logistic-models}
### Manhattan Plots and Q-Q Plots {#sec-ch03-visualization}
### Population Structure Control {#sec-ch03-population-structure}
## Heritability: What Genetics Can Explain {#sec-ch03-heritability}
### Pedigree Heritability {#sec-ch03-pedigree-heritability}
### SNP-Heritability and the Missing Heritability Problem {#sec-ch03-snp-heritability}
### Implications for GWAS and Polygenic Scores {#sec-ch03-heritability-implications}
## Linkage Disequilibrium and the Association-Causation Gap {#sec-ch03-ld}
### Structure of Linkage Disequilibrium {#sec-ch03-ld-structure}
### Causal Variants, Tag Variants, and GWAS Catalogs {#sec-ch03-causal-vs-tag}
## Fine-Mapping: From Loci to Causal Variants {#sec-ch03-fine-mapping}
### Statistical Framework {#sec-ch03-fine-mapping-stats}
### Functional Annotation Priors {#sec-ch03-functional-priors}
### Multi-Ancestry Fine-Mapping {#sec-ch03-multi-ancestry-fine-mapping}
## Polygenic Score Construction {#sec-ch03-pgs-construction}
### Clumping and Thresholding {#sec-ch03-clumping-thresholding}
### LD-Aware Bayesian Methods {#sec-ch03-bayesian-pgs}
### Fine-Mapping-Informed Scores {#sec-ch03-fine-mapping-informed-pgs}
## Polygenic Score Interpretation {#sec-ch03-pgs-interpretation}
### Relative Risk and Percentiles {#sec-ch03-relative-risk}
### Absolute Risk {#sec-ch03-absolute-risk}
### Explained Variance and Discrimination {#sec-ch03-variance-discrimination}
## Ancestry, Portability, and Fairness {#sec-ch03-portability}
### Portability Problem {#sec-ch03-portability-problem}
### Fairness and Health Equity {#sec-ch03-fairness}
## Phenome-Wide Association Studies {#sec-ch03-phewas}
### PheWAS Framework {#sec-ch03-phewas-framework}
### PheWAS for Polygenic Score Interpretation {#sec-ch03-prs-phewas}
### Phenotype Quality and PheWAS Power {#sec-ch03-phenotype-quality}
### Deep Phenotyping and Embedding-Enhanced GWAS {#sec-ch03-deep-phenotyping}
## From Association to Mechanism {#sec-ch03-mechanism}

### part_1/p1-ch04-vep-classical.qmd
# Classical Variant Prediction {#sec-ch04-vep-classical}
## Conservation-Based Approaches {#sec-ch04-conservation}
### Evolutionary Constraint Metrics {#sec-ch04-constraint-metrics}
### What Conservation Measures Versus What Clinicians Need {#sec-ch04-conservation-clinical-gap}
### Clinical Application and Boundaries {#sec-ch04-conservation-boundaries}
### ACMG-AMP Variant Classification Framework
## Protein-Level Predictors {#sec-ch04-protein-predictors}
### *SIFT*: Sequence Homology as Functional Constraint {#sec-ch04-sift}
### *PolyPhen-2*: Integrating Structure and Sequence {#sec-ch04-polyphen}
### From Sequence to Function {#sec-ch04-sequence-to-function}
### Boundaries of Protein-Level Prediction {#sec-ch04-protein-boundaries}
## *CADD* Framework {#sec-ch04-cadd}
### Evolutionary Proxy Training and Label Sources {#sec-ch04-cadd-training}
### Feature Integration {#sec-ch04-cadd-features}
### Model Architecture and Scoring {#sec-ch04-cadd-scoring}
### Evolutionary Proxy Problem {#sec-ch04-proxy-problem}
## Other Ensemble Methods {#sec-ch04-ensemble-methods}
### *REVEL* {#sec-ch04-revel}
### *M-CAP* {#sec-ch04-mcap}
### Comparison and Selection {#sec-ch04-ensemble-comparison}
## Circularity and Ascertainment Bias {#sec-ch04-circularity}
### Circularity Problem {#sec-ch04-circularity-definition}
### Ascertainment Bias {#sec-ch04-ascertainment}
### Implications for Clinical Use {#sec-ch04-clinical-implications}
## Limitations of the Feature Engineering Paradigm {#sec-ch04-feature-limitations}
### Feature Ceiling {#sec-ch04-feature-ceiling}
### Limited Context {#sec-ch04-limited-context}
### Persistent Gap Between Measurement and Need {#sec-ch04-measurement-gap}
### From Features to Representations {#sec-ch04-features-to-representations}

### part_2/p2--principles.qmd
# Part II: Sequence Architectures {.unnumbered}

### part_2/p2-ch05-representations.qmd
# Tokens and Embeddings {#sec-ch05-representations}
## One-Hot Encoding: The CNN Foundation {#sec-ch05-onehot}
## *K*-mer Tokenization: The DNABERT Approach {#sec-ch05-kmer}
## Byte Pair Encoding: Learning the Vocabulary {#sec-ch05-bpe}
## Single-Nucleotide Tokenization: Maximum Resolution {#sec-ch05-single-nucleotide}
## Biologically-Informed Tokenization {#sec-ch05-biological-tokenization}
## From Tokens to Embeddings: Learning Representations {#sec-ch05-embeddings}
### Position in Sequence {#sec-ch05-position}
## Special Considerations for Biological Sequences {#sec-ch05-biological-special}
## Tradeoffs and Practical Guidance {#sec-ch05-tradeoffs}
### Resolution Versus Compression {#sec-ch05-resolution-compression}
### Vocabulary Size and Model Capacity {#sec-ch05-vocabulary-capacity}
### Computational Efficiency {#sec-ch05-computational-efficiency}
### Variant Interpretation Requirements {#sec-ch05-variant-interpretation}
### Practical Heuristics {#sec-ch05-heuristics}
## Representation as Foundation {#sec-ch05-foundation}

### part_2/p2-ch06-cnn.qmd
# Convolutional Networks {#sec-ch06-cnn}
## Convolutions as Sequence Pattern Detectors {#sec-ch06-convolutions}
## *DeepSEA*: Regulatory Prediction from Sequence {#sec-ch06-deepsea}
### Architecture and Training {#sec-ch06-deepsea-architecture}
### Learned Representations and Biological Validation {#sec-ch06-deepsea-validation}
### Variant Effect Prediction {#sec-ch06-deepsea-vep}
## Cell-Type Specificity and Regulatory Grammar {#sec-ch06-basset}
## *ExPecto*: From Chromatin to Expression {#sec-ch06-expecto}
### Modular Architecture {#sec-ch06-expecto-architecture}
### Expression Prediction and Variant Effects {#sec-ch06-expecto-validation}
## *SpliceAI*: Clinical-Grade Splicing Prediction {#sec-ch06-spliceai}
### Architecture: Depth and Dilation {#sec-ch06-spliceai-architecture}
### Performance and Validation {#sec-ch06-spliceai-performance}
### Clinical Impact {#sec-ch06-spliceai-clinical}
## Receptive Field Ceiling {#sec-ch06-receptive-field}
## Sequential Approaches and Their Costs {#sec-ch06-sequential}
### Vanishing Gradient Problem {#sec-ch06-vanishing-gradient}
### *DanQ*: Combining Convolutions and Recurrence {#sec-ch06-danq}
### Sequential Bottleneck {#sec-ch06-sequential-bottleneck}
## Specialization and Its Limits {#sec-ch06-specialization}

### part_2/p2-ch07-attention.qmd
# Transformers and Attention {#sec-ch07-attention}
## Self-Attention Mechanism {#sec-ch07-self-attention}
### Query, Key, and Value Vectors {#sec-ch07-qkv}
### Multi-Head Attention {#sec-ch07-multihead}
## Positional Encoding {#sec-ch07-positional-encoding}
### Absolute Position Encodings {#sec-ch07-absolute-position}
### Relative Position Encodings {#sec-ch07-relative-position}
### Genomic Position Considerations {#sec-ch07-genomic-position}
## Transformer Block {#sec-ch07-transformer-block}
### Block Components {#sec-ch07-block-components}
### Information Flow and Depth {#sec-ch07-depth}
## Scaling to Genomic Sequences {#sec-ch07-scaling}
### Quadratic Barrier {#sec-ch07-quadratic-barrier}
### Parameter Considerations {#sec-ch07-parameters}
### Context Length Strategies {#sec-ch07-context-strategies}
### Memory and Precision {#sec-ch07-memory}
## Architectural Variants for Genomics {#sec-ch07-variants}
### Encoder-Only Transformers {#sec-ch07-encoder-only}
### Decoder-Only Transformers {#sec-ch07-decoder-only}
### Encoder-Decoder Transformers {#sec-ch07-encoder-decoder}
### Hybrid CNN-Transformer Models {#sec-ch07-hybrid}
## Training Dynamics {#sec-ch07-training}
### Optimization {#sec-ch07-optimization}
### Regularization {#sec-ch07-regularization}
### Gradient Stability {#sec-ch07-gradients}
### Distributed Training {#sec-ch07-distributed}
## Limitations and Emerging Alternatives {#sec-ch07-limitations}
### Quadratic Ceiling {#sec-ch07-quadratic-ceiling}
### State Space Models {#sec-ch07-ssm}
### Choosing Architectures {#sec-ch07-choosing}
## Capacity Without Direction {#sec-ch07-conclusion}

### part_2/p2-ch08-pretraining.qmd
# Pretraining Strategies {#sec-ch08-pretraining}
## Masked Language Modeling {#sec-ch08-mlm}
### Masking Strategies and Their Implications {#sec-ch08-mlm-strategies}
### What Masked Language Models Learn {#sec-ch08-mlm-learning}
## Next-Token Prediction {#sec-ch08-autoregressive}
### Genomic Applications {#sec-ch08-autoregressive-genomics}
## MLM and Autoregressive Comparison {#sec-ch08-comparison}
### Hybrid Architectures {#sec-ch08-hybrid}
## Span Corruption and Denoising {#sec-ch08-denoising}
### Corruption Beyond Masking {#sec-ch08-corruption}
### Biologically Motivated Corruption {#sec-ch08-biological-corruption}
## Contrastive Learning {#sec-ch08-contrastive}
### Augmentation Design for Genomic Sequences {#sec-ch08-augmentation}
### Cross-Species Contrastive Learning {#sec-ch08-cross-species}
## Multi-Task Pretraining {#sec-ch08-multitask}
### Task Selection and Architecture {#sec-ch08-task-selection}
### Loss Weighting and Balancing {#sec-ch08-loss-weighting}
### Large-Scale Multi-Task Examples {#sec-ch08-multitask-examples}
### When Multi-Task Learning Fails {#sec-ch08-multitask-failure}
## Staged Pretraining Strategies {#sec-ch08-staged}
### Context Length Curricula {#sec-ch08-context-curriculum}
### Domain-Adaptive Pretraining {#sec-ch08-domain-adaptive}
### Continued Pretraining on Expanded Data {#sec-ch08-continued-pretraining}
### Multi-Objective Schedules {#sec-ch08-multiobjective-schedule}
### Data Complexity Curricula {#sec-ch08-data-complexity}
### Practical Considerations {#sec-ch08-staged-practical}
## Data Strategies for Pretraining {#sec-ch08-data}
### Reference Genomes and Population Diversity {#sec-ch08-reference-genomes}
### Repeat Handling {#sec-ch08-repeats}
### Multi-Species and Augmentation Strategies {#sec-ch08-multispecies}
## Optimization and Scaling {#sec-ch08-optimization}
### Optimization Hyperparameters {#sec-ch08-hyperparameters}
### Scaling Laws and Emergence {#sec-ch08-scaling}
## Training Diagnostics {#sec-ch08-diagnostics}
### Monitoring Loss and Gradients {#sec-ch08-monitoring}
### Functional Probing {#sec-ch08-probing}
## Strategy Selection {#sec-ch08-selection}
## Pretraining in Practice: Case Studies {#sec-ch08-case-studies}
### DNABERT {#sec-ch08-dnabert}
### HyenaDNA {#sec-ch08-hyenadna}
### Enformer {#sec-ch08-enformer}
### ESM-2 {#sec-ch08-esm2}
## Open Questions {#sec-ch08-open-questions}
## From Sequence Statistics to Biological Knowledge {#sec-ch08-sequence-to-knowledge}

### part_2/p2-ch09-transfer.qmd
# Transfer Learning Foundations {#sec-ch09-transfer}
## Source and Target Domains {#sec-ch09-source-target}
### Gap Between Pretraining and Deployment {#sec-ch09-pretraining-deployment-gap}
### Recognizing Transfer Outcomes {#sec-ch09-transfer-outcomes}
## Factors Determining Transfer Success {#sec-ch09-transfer-factors}
### Task Relatedness {#sec-ch09-task-relatedness}
### Target Data Quantity {#sec-ch09-target-data-quantity}
### Model Expressiveness {#sec-ch09-model-expressiveness}
### Distribution Overlap {#sec-ch09-distribution-overlap}
### Factor Interactions
## Feature Extraction and Representation Analysis {#sec-ch09-feature-extraction}
### Linear Probing {#sec-ch09-linear-probing}
### When Linear Probing Fails {#sec-ch09-linear-probing-limits}
### Probing Representations {#sec-ch09-probing-representations}
### What Probing Reveals About Pretrained Models {#sec-ch09-probing-results}
### Probe-Guided Adaptation {#sec-ch09-probe-guided-adaptation}
## Summary {#sec-ch09-summary}

### part_2/p2-ch10-adaptation.qmd
# Adaptation Strategies {#sec-ch10-adaptation}
## Parameter-Efficient Fine-Tuning {#sec-ch10-peft}
### Low-Rank Adaptation {#sec-ch10-lora}
### Configuring Low-Rank Adaptation {#sec-ch10-lora-config}
## Layer Selection for Embedding Extraction {#sec-ch10-layer-selection}
### The Encoder Advantage
### The Decoder Dilemma
### Practical Consequences
### Layer Averaging and Weighted Combinations
### Systematic Layer Probing
### Implications for Model Selection
### Cross-Reference to Pretraining Objectives
## Full Fine-Tuning {#sec-ch10-full-finetuning}
### Making Full Fine-Tuning Work {#sec-ch10-full-finetuning-practice}
### The `[CLS]` Token and Sequence Aggregation {#sec-ch10-cls-token}
### Mean Pooling and Alternatives
### Practical Considerations for Genomic Sequences
## Choosing an Adaptation Strategy {#sec-ch10-choosing-strategy}
## Domain Shift and Cross-Context Transfer {#sec-ch10-domain-shift}
### Types of Domain Shift in Genomics {#sec-ch10-domain-shift-types}
### Detecting and Mitigating Shift {#sec-ch10-detecting-shift}
## Minimal-Data and Emerging Transfer Paradigms {#sec-ch10-minimal-data}
### Few-Shot Learning with Minimal Examples {#sec-ch10-few-shot}
### Zero-Shot Transfer Without Task-Specific Data {#sec-ch10-zero-shot}
### Emerging Approaches {#sec-ch10-emerging-approaches}
### Toward Theoretical Foundations {#sec-ch10-theory}
## Label and Class Imbalance {#sec-ch10-label-imbalance}
### Manifestations During Transfer
### Mitigation Strategies
### Evaluation Under Imbalance
### Imbalance as Fundamental Constraint
## Diagnosing Transfer: Validation and Failure Modes {#sec-ch10-diagnosing-transfer}
### Diagnosing Negative Transfer {#sec-ch10-negative-transfer}
### Validation and Common Pitfalls {#sec-ch10-validation-pitfalls}
### Sources of Spurious Success {#sec-ch10-spurious-success}
## Case Studies in Transfer Learning {#sec-ch10-case-studies}
### Successful Transfer: Alignment Between Pretraining and Task {#sec-ch10-case-success}
### When Transfer Fails: Cross-Species Prediction {#sec-ch10-case-failure}
## What Transfers, What Breaks {#sec-ch10-conclusion}

### part_2/p2-ch11-benchmarks.qmd
# Benchmarks and Evaluation {#sec-ch11-benchmarks}
## Protein Language Model Benchmarks {#sec-ch11-protein-benchmarks}
### TAPE: Tasks Assessing Protein Embeddings {#sec-ch11-tape}
### FLIP: Function-Linked Protein Benchmark {#sec-ch11-flip}
### ProteinGym: Comprehensive Variant Effect Evaluation {#sec-ch11-proteingym}
### Structure Prediction Benchmarks {#sec-ch11-structure-benchmarks}
## DNA and Regulatory Benchmarks {#sec-ch11-dna-benchmarks}
### Classical Regulatory Prediction Tasks {#sec-ch11-classical-regulatory}
### Quantitative Regulatory Prediction {#sec-ch11-quantitative-regulatory}
### Genomic Benchmarks {#sec-ch11-genomic-benchmarks}
### BEND: Benchmark for DNA Language Models {#sec-ch11-bend}
### Long-Range Benchmarks {#sec-ch11-long-range}
### Cross-Species Evaluation {#sec-ch11-cross-species}
## Variant Effect Prediction Benchmarks {#sec-ch11-vep-benchmarks}
### Clinical Variant Databases {#sec-ch11-clinical-databases}
### CAGI: Critical Assessment of Genome Interpretation {#sec-ch11-cagi}
### Deep Mutational Scanning Benchmarks {#sec-ch11-dms-benchmarks}
### Regulatory and Non-Coding Variant Benchmarks {#sec-ch11-noncoding-benchmarks}
## Trait and Population-Level Benchmarks {#sec-ch11-trait-benchmarks}
### Polygenic Score Evaluation {#sec-ch11-pgs-evaluation}
### TraitGym {#sec-ch11-traitgym}
### EmbedGEM Framework {#sec-ch11-embedgem}
## Benchmark Construction and Hidden Assumptions {#sec-ch11-benchmark-construction}
### Data Sources and Label Provenance {#sec-ch11-label-provenance}
### Splitting Strategies and Leakage {#sec-ch11-splitting}
### Metric Selection and Aggregation {#sec-ch11-metrics}
### Goodhart's Law and Benchmark Gaming {#sec-ch11-goodhart}
## Benchmark Saturation and Staleness {#sec-ch11-saturation-staleness}
### Saturation: When Benchmarks Stop Discriminating {#sec-ch11-saturation}
### Staleness: When Benchmarks Diverge from Practice {#sec-ch11-staleness}
### Leakage from Scale {#sec-ch11-leakage-scale}
## Benchmark-Deployment Gap {#sec-ch11-deployment-gap}
### Distribution Shift {#sec-ch11-distribution-shift}
### Calibration Requirements {#sec-ch11-calibration-requirements}
### Metric Mismatch {#sec-ch11-metric-mismatch}
### Practical Constraints {#sec-ch11-practical-constraints}
## Systematic Gaps in Current Benchmarks {#sec-ch11-systematic-gaps}
## The Proxy Problem {#sec-ch11-proxy-problem}
## Evaluation Methodology {#sec-ch11-evaluation-methodology}
# Evaluation Principles {#sec-ch11-eval}
## Why Random Splits Fail {#sec-ch11-random-splits-fail}
## Homology-Aware Splitting {#sec-ch11-homology-aware-splitting}
### Clustering Tools and Workflows {#sec-ch11-clustering-tools}
### Practical Considerations {#sec-ch11-homology-practical}
## Splitting by Biological Axis {#sec-ch11-splitting-biological-axis}
### Splitting by Individual {#sec-ch11-splitting-individual}
### Splitting by Genomic Region {#sec-ch11-splitting-genomic-region}
### Splitting by Gene or Protein Family {#sec-ch11-splitting-gene-family}
### Splitting by Experimental Context {#sec-ch11-splitting-experimental-context}
### Splitting by Ancestry {#sec-ch11-splitting-ancestry}
### Splitting by Time {#sec-ch11-splitting-time}
## Leakage Taxonomy and Detection {#sec-ch11-leakage-detection}
### Label Leakage {#sec-ch11-label-leakage}
### Feature Leakage {#sec-ch11-feature-leakage}
### Temporal Leakage {#sec-ch11-temporal-leakage}
### Benchmark Leakage {#sec-ch11-benchmark-leakage}
### Detecting Leakage {#sec-ch11-detecting-leakage}
## Metrics for Genomic Tasks {#sec-ch11-metrics-genomic-tasks}
### Discrimination Metrics {#sec-ch11-discrimination-metrics}
### Regression and Correlation Metrics {#sec-ch11-regression-correlation-metrics}
### Ranking and Prioritization Metrics {#sec-ch11-ranking-prioritization-metrics}
### Clinical Utility Metrics {#sec-ch11-clinical-utility-metrics}
## Baseline Selection {#sec-ch11-baseline-selection}
### Strong Baselines, Not Straw Men {#sec-ch11-strong-baselines}
### Historical Baselines and Progress Tracking {#sec-ch11-historical-baselines}
### Non-Deep-Learning Baselines {#sec-ch11-non-dl-baselines}
## Ablation Studies {#sec-ch11-ablation-studies}
### Component Isolation {#sec-ch11-component-isolation}
### Hyperparameter Sensitivity {#sec-ch11-hyperparameter-sensitivity}
### Architecture Search Confounds {#sec-ch11-architecture-search-confounds}
### Reporting Standards {#sec-ch11-reporting-standards}
## Statistical Rigor {#sec-ch11-statistical-rigor}
### Significance Testing {#sec-ch11-significance-testing}
### Effect Sizes {#sec-ch11-effect-sizes}
### Confidence Intervals on Metrics {#sec-ch11-confidence-intervals}
### Variance Across Random Seeds {#sec-ch11-variance-random-seeds}
## Evaluating Foundation Models {#sec-ch11-evaluating-fm}
### Zero-Shot Evaluation {#sec-ch11-zero-shot-eval}
### Linear Probing {#sec-ch11-linear-probing}
### Fine-Tuning Evaluation {#sec-ch11-fine-tuning-eval}
### Transfer Across Tasks {#sec-ch11-transfer-tasks}
## Calibration Essentials {#sec-ch11-calibration}
### Assessing Calibration {#sec-ch11-assessing-calibration}
### Recalibration Methods {#sec-ch11-recalibration-methods}
### Calibration in Model Comparison {#sec-ch11-calibration-comparison}
## Putting It All Together {#sec-ch11-putting-together}
## The Question Behind the Metric {#sec-ch11-question-behind-metric}

### part_2/p2-ch12-confounding.qmd
# Confounding and Data Leakage {#sec-ch12-confounding}
## Confounding, Bias, and Leakage {#sec-ch12-terminology}
## Sources of Confounding in Genomic Data {#sec-ch12-sources}
### Population Structure and Relatedness {#sec-ch12-ancestry-confounding}
### Technical Batch Effects {#sec-ch12-batch-effects}
### Institutional and Recruitment Confounding {#sec-ch12-institutional-confounding}
### Label Generation Bias {#sec-ch12-label-bias}
### Temporal Drift {#sec-ch12-temporal-drift}
### Resource Overlap and Indirect Leakage {#sec-ch12-resource-overlap}
## Population Structure as a Shortcut {#sec-ch12-population-shortcut}
## Technical Artifacts as Biological Signal {#sec-ch12-technical-artifacts}
## Label Bias and Circularity {#sec-ch12-label-circularity}
## Data Splitting {#sec-ch12-data-splitting}
### Random Individual-Level Splits {#sec-ch12-random-splits}
### Family-Aware Splits {#sec-ch12-family-splits}
### Locus-Level Splits {#sec-ch12-locus-splits}
### Region and Chromosome Splits {#sec-ch12-region-splits}
### Cohort and Site Splits {#sec-ch12-cohort-splits}
### Temporal Splits {#sec-ch12-temporal-splits}
### Indirect Leakage Across Resources {#sec-ch12-indirect-leakage}
## Data Leakage as Confounding {#sec-ch12-leakage-confounding}
### Causal Structure of Leakage {#sec-ch12-leakage-causal}
### Compounding Effects {#sec-ch12-compounding}
### Implications for Confounding Analysis {#sec-ch12-leakage-implications}
## Detecting Confounding {#sec-ch12-detection}
### Confounder-Only Baselines {#sec-ch12-confounder-baselines}
### Stratified Performance Analysis {#sec-ch12-stratified-performance}
### Residual Confounder Associations {#sec-ch12-residual-associations}
### Split Sensitivity Analysis {#sec-ch12-split-sensitivity}
### Negative Control Outcomes {#sec-ch12-negative-controls}
## Mitigation Strategies {#sec-ch12-mitigation}
### Study Design and Cohort Construction {#sec-ch12-study-design}
### Covariate Adjustment {#sec-ch12-covariate-adjustment}
### Domain Adaptation and Invariance Learning {#sec-ch12-domain-adaptation}
### Data Curation and Benchmark Design {#sec-ch12-benchmark-design}
### Causal Inference Approaches {#sec-ch12-causal-inference}
## Fairness and External Validity {#sec-ch12-fairness}
## A Practical Checklist {#sec-ch12-checklist}
## Rigor as Response {#sec-ch12-rigor}

### part_3/p3--architectures.qmd
# Part III: Foundation Model Families {.unnumbered}

### part_3/p3-ch13-fm-principles.qmd
# Foundation Model Paradigm {#sec-ch13-fm-principles}
## From Task-Specific Models to Foundation Models {#sec-ch13-task-specific}
## Defining Genomic Foundation Models {#sec-ch13-defining}
### Essential Properties {#sec-ch13-essential-properties}
### What does not Count {#sec-ch13-what-doesnt-count}
### Limitations of the Foundation Model Concept {#sec-ch13-concept-limitations}
## Scaling Laws and Compute-Optimal Training {#sec-ch13-scaling}
### Chinchilla Framework and Genomic Constraints {#sec-ch13-scaling-framework}
### Empirical Scaling in Genomic Models {#sec-ch13-empirical-scaling}
### Emergent Capabilities {#sec-ch13-emergence}
## A Taxonomy of Genomic Foundation Models {#sec-ch13-taxonomy}
### DNA Language Models {#sec-ch13-dna-lm}
### Sequence-to-Function Foundation Models {#sec-ch13-seq-to-func}
### Variant Effect Prediction Models {#sec-ch13-vep-models}
### Multi-Omic Foundation Models {#sec-ch13-multi-omic}
## Design Dimensions {#sec-ch13-design-dimensions}
### Data Composition {#sec-ch13-data-composition}
### Architecture Choices {#sec-ch13-architecture}
### Context Length {#sec-ch13-context-length}
### Tokenization {#sec-ch13-tokenization}
## Build Versus Use Decisions {#sec-ch13-build-vs-use}
### When to Use Existing Models {#sec-ch13-use-existing}
### When to Adapt Existing Models {#sec-ch13-adapt-existing}
### When to Train from Scratch {#sec-ch13-train-scratch}
### Cost-Benefit Analysis {#sec-ch13-cost-benefit}
## Evaluation Principles {#sec-ch13-evaluation}
### Multi-Task Assessment {#sec-ch13-multi-task}
### Transfer Versus Pretraining Performance {#sec-ch13-transfer-eval}
## Foundation Model Ecosystem {#sec-ch13-ecosystem}
### Model Distribution {#sec-ch13-distribution}
### Documentation Requirements {#sec-ch13-documentation}
### Industry and Academic Contributions {#sec-ch13-contributions}
## Open Questions {#sec-ch13-open-questions}
## Convergence Without Consolidation {#sec-ch13-convergence}

### part_3/p3-ch14-dna-lm.qmd
# DNA Language Models {#sec-ch14-dna-lm}
## From Task-Specific CNNs to General-Purpose Language Models {#sec-ch14-task-specific-to-general}
## *DNABERT*: The First DNA Language Model {#sec-ch14-dnabert}
## *Nucleotide Transformer*: Scaling Data and Model Diversity {#sec-ch14-nucleotide-transformer}
## *GPN*: Cross-Species Pretraining for Variant Effect Prediction {#sec-ch14-gpn}
## Long-Context Revolution {#sec-ch14-long-context}
### *HyenaDNA*: Megabase Context via Implicit Convolutions {#sec-ch14-hyenadna}
### *Caduceus*: Bidirectional Processing with Reverse-Complement Equivariance {#sec-ch14-caduceus}
### *Evo 2*: Genome-Scale Modeling Across the Tree of Life {#sec-ch14-evo2}
## Training Data and What Models Learn {#sec-ch14-training-data}
### Training Corpus Composition {#sec-ch14-corpus-composition}
### Probing What Models Learn {#sec-ch14-probing}
### What Models Do Not Learn {#sec-ch14-limitations-learned}
## Benchmark Performance and Evaluation {#sec-ch14-benchmarks}
### Major Benchmark Suites {#sec-ch14-benchmark-suites}
### Benchmark Limitations {#sec-ch14-benchmark-limitations}
## Annotation-Aware Extensions {#sec-ch14-annotation-aware}
## Using DNA Language Models in Practice {#sec-ch14-practical-use}
### Embeddings as Universal Features {#sec-ch14-embeddings}
### Fine-Tuning and Adaptation {#sec-ch14-fine-tuning}
### Zero-Shot and Few-Shot Scoring {#sec-ch14-zero-shot}
## Limitations and Open Challenges {#sec-ch14-open-challenges}
## Representations Without Predictions {#sec-ch14-soft-landing}

### part_3/p3-ch15-protein-lm.qmd
# Protein Language Models {#sec-ch15-protein-lm}
## ESM Model Family {#sec-ch15-esm-family}
### ESM-1b: Establishing the Paradigm {#sec-ch15-esm1b}
### Emergent Biological Knowledge {#sec-ch15-emergent-knowledge}
### ESM-2: Scaling Up {#sec-ch15-esm2}
## Alternative Architectures {#sec-ch15-alternative-architectures}
## Attention and Evolutionary Coupling {#sec-ch15-attention-coupling}
## ESMFold: Structure from Sequence {#sec-ch15-esmfold}
### Alignment-Free Prediction {#sec-ch15-alignment-free}
### What ESMFold Reveals About PLMs {#sec-ch15-esmfold-implications}
## Function Prediction {#sec-ch15-function-prediction}
## Variant Effect Prediction {#sec-ch15-variant-effects}
## Integration with Structure Prediction {#sec-ch15-structure-integration}
## Limitations {#sec-ch15-limitations}
### Orphan and Dark Proteins {#sec-ch15-orphan-proteins}
### Novel Folds {#sec-ch15-novel-folds}
### Conformational Flexibility {#sec-ch15-conformational-flexibility}
### Epistasis {#sec-ch15-epistasis}
### Interpretability {#sec-ch15-interpretability}
## Lessons for Genomic Foundation Models {#sec-ch15-lessons}
### Self-Supervised Biological Knowledge {#sec-ch15-self-supervised}
### Scaling Benefits {#sec-ch15-scaling}
### Effective Transfer Learning {#sec-ch15-transfer}
### Architecture-Sequence Matching {#sec-ch15-architecture-matching}
### Integration Benefits {#sec-ch15-integration}
## Paradigm That Generalized {#sec-ch15-conclusion}

### part_3/p3-ch16-regulatory.qmd
# Regulatory Models {#sec-ch16-regulatory}
## Long-Range Regulation Problem {#sec-ch16-long-range}
## *Enformer*: Attention Meets Regulatory Genomics {#sec-ch16-enformer}
### Architecture {#sec-ch16-enformer-architecture}
### Training Data and Cross-Species Learning {#sec-ch16-enformer-training}
### Variant Effect Prediction {#sec-ch16-enformer-vep}
## *Borzoi*: From Chromatin to Transcriptome {#sec-ch16-borzoi}
### Beyond Transcription Initiation {#sec-ch16-borzoi-transcription}
### Predicting Coverage at Nucleotide Resolution {#sec-ch16-borzoi-coverage}
### Applications Beyond Expression Level {#sec-ch16-borzoi-applications}
## *Sei*: A Regulatory Vocabulary from Sequence {#sec-ch16-sei}
### Discrete Regulatory States {#sec-ch16-sei-states}
### Complementary to Track Prediction {#sec-ch16-sei-complementary}
## *AlphaGenome*: Unifying Modalities at Megabase Scale {#sec-ch16-alphagenome}
### From 200kb to One Megabase {#sec-ch16-alphagenome-scale}
### Closed Weights, Open Questions {#sec-ch16-alphagenome-access}
## What Hybrid Architectures Accomplish {#sec-ch16-accomplishments}
### Spanning Enhancer-Promoter Distances {#sec-ch16-spanning}
### Multi-Task Regularization {#sec-ch16-multitask}
### Cross-Species Constraints {#sec-ch16-cross-species}
### Unified Variant Effect Prediction {#sec-ch16-unified-vep}
## Limitations and Open Challenges {#sec-ch16-limitations}
### Training Data Constraints {#sec-ch16-training-bias}
### Finite Context {#sec-ch16-finite-context}
### Missing Three-Dimensional Context {#sec-ch16-missing-3d}
### Correlation Versus Causation {#sec-ch16-correlation}
### Interpretability Challenges {#sec-ch16-interpretability}
## Relationship to Foundation Models {#sec-ch16-foundation-models}
## Prediction Without Explanation {#sec-ch16-prediction-explanation}

### part_3/p3-ch17-vep-fm.qmd
# Variant Effect Prediction {#sec-ch17-vep-fm}
## Foundation Model Paradigm for Variant Interpretation {#sec-ch17-fm-paradigm}
### Zero-Shot and Supervised Approaches {#sec-ch17-zeroshot-supervised}
## Protein-Based Variant Effect Prediction {#sec-ch17-protein-vep}
### Zero-Shot Scoring with Protein Language Models {#sec-ch17-zeroshot-plm}
### Alignment-Based Models: EVE and popEVE {#sec-ch17-alignment-models}
### AlphaMissense: Structure-Informed Pathogenicity Prediction {#sec-ch17-alphamissense}
## DNA-Based Variant Effect Prediction {#sec-ch17-dna-vep}
### Splice Variant Prediction with SpliceAI {#sec-ch17-spliceai}
### Regulatory Variant Prediction with Enformer {#sec-ch17-enformer-vep}
### DNA Language Models: GPN-MSA and Evo 2 {#sec-ch17-dna-lm-vep}
### AlphaGenome: Unified Multi-Omic Variant Effect Prediction {#sec-ch17-alphagenome}
## Combining Evidence Across Modalities {#sec-ch17-combining-evidence}
### Integration Strategies {#sec-ch17-integration-strategies}
### Avoiding Double-Counting {#sec-ch17-double-counting}
### Practical Workflow Design {#sec-ch17-workflow-design}
## Calibration and Clinical Categories {#sec-ch17-calibration}
### Assessing Calibration {#sec-ch17-assessing-calibration}
### Calibration Methods for Variant Effect Prediction {#sec-ch17-calibration-methods}
### Mapping to ACMG Categories {#sec-ch17-acmg-mapping}
### The Challenge of Uncertain Significance {#sec-ch17-vus-challenge}
## Uncertainty Quantification {#sec-ch17-uncertainty}
### Sources of Uncertainty {#sec-ch17-uncertainty-sources}
### Uncertainty Estimation Methods {#sec-ch17-uncertainty-methods}
### Out-of-Distribution Detection {#sec-ch17-ood-detection}
## What Foundation Models Add {#sec-ch17-fm-gains}
### Improved Discrimination {#sec-ch17-improved-discrimination}
### Extended Coverage {#sec-ch17-extended-coverage}
### Mechanistic Interpretability {#sec-ch17-mechanistic-interpretability}
### Persistent Limitations {#sec-ch17-persistent-limitations}
## Clinical Integration Considerations {#sec-ch17-clinical-integration}
### Laboratory Validation {#sec-ch17-lab-validation}
### Workflow Integration {#sec-ch17-workflow-integration}
### Communication to Clinicians {#sec-ch17-clinical-communication}
## Open Challenges {#sec-ch17-open-challenges}
### Complex Variant Types {#sec-ch17-complex-variants}
### Combinatorial Effects {#sec-ch17-combinatorial}
### Phenotype Specificity {#sec-ch17-phenotype-specificity}
### Temporal and Environmental Context {#sec-ch17-temporal-context}
### Equity and Access {#sec-ch17-equity}
## Tools for Interpretation, Not Oracles {#sec-ch17-conclusion}

### part_4/p4--multi-modal.qmd
# Part IV: Systems and Scale {.unnumbered}

### part_4/p4-ch18-rna.qmd
# RNA Structure and Function {#sec-ch18-rna}
## RNA as Molecule Versus Transcriptome Readout {#sec-ch18-perspectives}
## Why Secondary Structure Creates a Distinct Modeling Challenge {#sec-ch18-structure-challenge}
### Flat Energy Landscape Problem {#sec-ch18-energy-landscape}
### Base Pairing and Long-Range Dependencies {#sec-ch18-base-pairing}
### Pseudoknots and Tertiary Complexity {#sec-ch18-pseudoknots}
## Classical Approaches to Structure Prediction {#sec-ch18-classical}
### Thermodynamic Folding Models {#sec-ch18-thermodynamic}
### Comparative and Covariation Methods {#sec-ch18-comparative}
## Deep Learning for Secondary Structure Prediction {#sec-ch18-dl-structure}
### From Thermodynamics to Learned Patterns {#sec-ch18-learned-patterns}
### Structure Probing as Supervision {#sec-ch18-structure-probing}
## RNA Foundation Models {#sec-ch18-foundation}
### Scale Gap with Protein Language Models {#sec-ch18-scale-gap}
### Architectures and Objectives {#sec-ch18-architectures}
### Downstream Applications {#sec-ch18-downstream}
## Codon-Level Models for Coding RNA {#sec-ch18-codon}
### Beyond Nucleotide Tokenization {#sec-ch18-codon-tokenization}
### What Codon Models Add {#sec-ch18-codon-advantages}
## UTR Models and Translation Regulation {#sec-ch18-utr}
### Why UTRs Dominate Expression Control {#sec-ch18-utr-control}
### Sequence-to-Expression Models {#sec-ch18-expression-models}
### Integration with mRNA Design {#sec-ch18-utr-design}
## mRNA Design and Optimization {#sec-ch18-mrna-design}
### Design Objectives and Trade-offs {#sec-ch18-design-objectives}
### Lessons from COVID-19 Vaccines {#sec-ch18-covid-vaccines}
### Model-Based Design Strategies {#sec-ch18-model-design}
## Noncoding RNA Classification and Function {#sec-ch18-ncrna}
### Diversity of Noncoding RNA {#sec-ch18-ncrna-diversity}
### From Handcrafted Features to Learned Representations {#sec-ch18-ncrna-features}
## miRNA Target Prediction {#sec-ch18-mirna}
## Splicing and Transcript Processing Models {#sec-ch18-splicing}
### Beyond SpliceAI {#sec-ch18-beyond-spliceai}
## Limitations and Open Challenges {#sec-ch18-limitations}
### Sparse Structural Data {#sec-ch18-sparse-data}
### Functional Annotation Gaps {#sec-ch18-annotation-gaps}
### Maturity Gap {#sec-ch18-maturity-gap}
## Bridge Between Sequence and Cell {#sec-ch18-bridge}

### part_4/p4-ch19-single-cell.qmd
# Single-Cell Models {#sec-ch19-single-cell}
## Single-Cell Data Landscape {#sec-ch19-data}
### From Bulk to Single-Cell Resolution {#sec-ch19-bulk-to-sc}
### Technical Challenges and Data Characteristics {#sec-ch19-technical}
## Cellular Language Models {#sec-ch19-clm}
### *Geneformer*: Learning Network Biology {#sec-ch19-geneformer}
### *scGPT*: Generative Pretraining for Single-Cell Analysis {#sec-ch19-scgpt}
### *scFoundation* and Scaling Single-Cell Models {#sec-ch19-scfoundation}
### *TranscriptFormer*: Cross-Species Cellular Models {#sec-ch19-transcriptformer}
## Perturbation Response Prediction {#sec-ch19-perturbation}
### *In Silico* Experiment Promise {#sec-ch19-in-silico}
### Perturb-seq and Foundation Model Training {#sec-ch19-perturb-seq}
### Limitations of Current Approaches {#sec-ch19-perturbation-limits}
## Epigenomic Foundation Models {#sec-ch19-epigenomic}
### DNA Methylation and *CpGPT* {#sec-ch19-methylation}
### Chromatin Accessibility Models {#sec-ch19-accessibility}
## Cross-Modality Integration {#sec-ch19-integration}
### Unpaired Integration Challenge {#sec-ch19-unpaired}
### *GLUE*: Graph-Linked Unified Embedding {#sec-ch19-glue}
### Applications of Cross-Modal Integration {#sec-ch19-cross-modal-apps}
## Practical Challenges and Limitations {#sec-ch19-limitations}
### Batch Effects and Technical Artifacts {#sec-ch19-batch-effects}
### Cell Type Imbalance {#sec-ch19-imbalance}
### Evaluation Complexity {#sec-ch19-evaluation}
### Causality and Mechanism {#sec-ch19-causality}
## From Sequence to State {#sec-ch19-conclusion}

### part_4/p4-ch20-3d-genome.qmd
# 3D Genome Organization {#sec-ch20-3d-genome}
## Chromatin Organization Hierarchy {#sec-ch20-chromatin-hierarchy}
### Chromosome Territories and Compartments {#sec-ch20-territories-compartments}
### Topologically Associating Domains {#sec-ch20-tads}
### Loop Extrusion Mechanism {#sec-ch20-loop-extrusion}
### Fine-Scale Chromatin Loops {#sec-ch20-fine-scale-loops}
## Measuring the 3D Genome {#sec-ch20-3d-measurement}
### Hi-C and Contact Matrices {#sec-ch20-hic-matrices}
### Resolution and Data Resources {#sec-ch20-3d-data-resources}
## Predicting 3D Structure from Sequence {#sec-ch20-3d-prediction}
### *Akita* and Dilated Convolutions {#sec-ch20-akita}
### *Orca* and Multiscale Prediction {#sec-ch20-orca}
### *C.Origami* and Cross-Cell-Type Transfer {#sec-ch20-c-origami}
### Learned Sequence Determinants {#sec-ch20-3d-interpretability}
## 3D Structure and Gene Regulation {#sec-ch20-3d-regulation}
### Beyond One-Dimensional Models {#sec-ch20-beyond-1d}
### Structural Variant Interpretation {#sec-ch20-sv-interpretation}
### Causality and Permissive Architecture {#sec-ch20-3d-causality}
## Spatial Transcriptomics {#sec-ch20-spatial-transcriptomics}
### Measurement Technologies {#sec-ch20-spatial-technologies}
### Computational Challenges {#sec-ch20-spatial-computation}
### Spatial Foundation Models {#sec-ch20-spatial-models}
## Limitations and Open Questions {#sec-ch20-3d-limitations}
## Structure as Context, Not Cause {#sec-ch20-structure-context}

### part_4/p4-ch21-networks.qmd
# Graph and Network Models {#sec-ch21-networks}
## Biological Networks and Data Resources {#sec-ch21-biological-networks}
### Landscape of Biological Graphs {#sec-ch21-landscape}
### Biases and Limitations {#sec-ch21-network-biases}
## Graph Neural Network Fundamentals {#sec-ch21-gnn-fundamentals}
### Message Passing Principles {#sec-ch21-message-passing}
### Canonical Architectures {#sec-ch21-canonical-architectures}
## Foundation Model Embeddings as Node Features {#sec-ch21-fm-embeddings}
### Integration Principle {#sec-ch21-integration-principle}
### Practical Integration Patterns {#sec-ch21-practical-patterns}
### Evidence for the Integration Benefit {#sec-ch21-integration-evidence}
## Applications {#sec-ch21-applications}
### Disease Gene Prioritization {#sec-ch21-disease-gene}
### Drug-Target Interaction Prediction {#sec-ch21-drug-target}
### Knowledge Graph Reasoning and Drug Repurposing {#sec-ch21-kg-reasoning}
### Pathway and Module Analysis {#sec-ch21-pathway-analysis}
### Cell Type and State Annotation {#sec-ch21-cell-annotation}
## Practical Considerations {#sec-ch21-practical}
### Graph Construction Quality {#sec-ch21-graph-construction}
### Scalability and Mini-Batching {#sec-ch21-scalability}
### Robustness to Noise and Missingness {#sec-ch21-robustness}
### Interpretation and Validation {#sec-ch21-interpretation}
## Limitations and Open Challenges {#sec-ch21-limitations}
### Study Bias Problem {#sec-ch21-study-bias}
### Causality Versus Association {#sec-ch21-causality}
### Negative Data and Class Imbalance {#sec-ch21-negative-data}
### Distribution Shift {#sec-ch21-distribution-shift}
## Sequence Encodes, Structure Connects {#sec-ch21-conclusion}

### part_4/p4-ch22-multi-omics.qmd
# Multi-Omics Integration {#sec-ch22-multi-omics}
## Limits of Single-Modality Models {#sec-ch22-limits}
## Integration Strategies and Their Tradeoffs {#sec-ch22-strategies}
### Early Fusion {#sec-ch22-early-fusion}
### Late Fusion {#sec-ch22-late-fusion}
### Intermediate Fusion {#sec-ch22-intermediate-fusion}
## Multi-Omics Foundation Models {#sec-ch22-foundation-models}
### Factor-Based Integration {#sec-ch22-factor-integration}
### Deep Generative Multi-Omics Models {#sec-ch22-deep-generative}
### Contrastive Multi-Modal Learning {#sec-ch22-contrastive}
## Clinical Integration: EHR, Imaging, and Molecular Data {#sec-ch22-clinical-integration}
### Electronic Health Records as a Modality {#sec-ch22-ehr}
### Imaging Integration {#sec-ch22-imaging}
### Multi-Modal Clinical Prediction Models {#sec-ch22-multimodal-clinical}
## Systems View: From Variant to Phenotype {#sec-ch22-systems-view}
### Information Cascade {#sec-ch22-information-cascade}
### Bottleneck Modalities {#sec-ch22-bottleneck}
### Causal vs. Correlational Integration {#sec-ch22-causal-correlational}
## Handling Missing Modalities {#sec-ch22-missing-modalities}
### Training with Incomplete Data {#sec-ch22-incomplete-training}
### Cross-Modal Imputation {#sec-ch22-imputation}
### Zero-Shot Cross-Modal Transfer {#sec-ch22-zero-shot}
## Practical Challenges {#sec-ch22-practical-challenges}
### Batch Effects Across Modalities {#sec-ch22-batch-effects}
### Sample Size and Power {#sec-ch22-sample-size}
### Interpretability Across Modalities {#sec-ch22-interpretability}
### Evaluation Complexity {#sec-ch22-evaluation}
## Integration as Means, Not End {#sec-ch22-conclusion}

### part_5/p5--responsible-deployment.qmd
# Part V: Evaluation and Trust {.unnumbered}

### part_5/p5-ch23-uncertainty.qmd
# Uncertainty Quantification {#sec-ch23-uncertainty}
## Types of Uncertainty in Genomic Prediction {#sec-ch23-types}
### Why Uncertainty Matters {#sec-ch23-why-uncertainty}
### Epistemic Uncertainty {#sec-ch23-epistemic}
### Aleatoric Uncertainty {#sec-ch23-aleatoric}
### Decomposing Total Uncertainty {#sec-ch23-decomposition}
## Calibration and Confidence Interpretation {#sec-ch23-calibration}
### The Calibration Problem {#sec-ch23-calibration-problem}
### Measuring Calibration {#sec-ch23-measuring-calibration}
### Why Foundation Models Are Often Miscalibrated {#sec-ch23-fm-miscalibration}
### Calibration Across Subgroups {#sec-ch23-subgroup-calibration}
## Post-Hoc Calibration Methods {#sec-ch23-post-hoc-calibration}
### Temperature Scaling {#sec-ch23-temperature-scaling}
### Platt Scaling {#sec-ch23-platt-scaling}
### Isotonic Regression {#sec-ch23-isotonic-regression}
### Calibrating Foundation Model Outputs {#sec-ch23-calibrating-fm}
## Uncertainty Quantification Methods for Foundation Models {#sec-ch23-uq-methods}
### Deep Ensembles {#sec-ch23-deep-ensembles}
### Monte Carlo Dropout {#sec-ch23-mc-dropout}
### Heteroscedastic Models {#sec-ch23-heteroscedastic}
### Evidential Deep Learning {#sec-ch23-evidential}
### Selecting Uncertainty Quantification Methods {#sec-ch23-selecting-uq}
## Conformal Prediction: Distribution-Free Guarantees {#sec-ch23-conformal}
### Split Conformal Prediction {#sec-ch23-split-conformal}
### Conformal Prediction for Variant Classification {#sec-ch23-conformal-variant}
### Limitations and Practical Considerations {#sec-ch23-conformal-limitations}
### Integration with Clinical Workflows {#sec-ch23-conformal-clinical}
## Out-of-Distribution Detection {#sec-ch23-ood-detection}
### Out-of-Distribution Problem {#sec-ch23-ood-problem}
### Likelihood-Based Detection and Its Failures {#sec-ch23-likelihood-ood}
### Embedding-Based Detection {#sec-ch23-embedding-ood}
### Practical OOD Detection for Genomic Applications {#sec-ch23-practical-ood}
## Selective Prediction and Abstention {#sec-ch23-selective-prediction}
### When to Abstain {#sec-ch23-when-abstain}
### Selective Prediction Methods {#sec-ch23-selective-methods}
### Evaluating Selective Prediction {#sec-ch23-selective-eval}
## Uncertainty for Specific Genomic Tasks {#sec-ch23-genomic-uq}
### Variant Effect Prediction Uncertainty {#sec-ch23-vep-uncertainty}
### Regulatory Variant Uncertainty {#sec-ch23-regulatory-uncertainty}
### Uncertainty Across Populations {#sec-ch23-population-uncertainty}
## Communicating Uncertainty to End Users {#sec-ch23-communication}
### Communication Challenge {#sec-ch23-communication-challenge}
### Categorical Reporting {#sec-ch23-categorical-reporting}
### Visual Communication {#sec-ch23-visual-communication}
### Decision-Theoretic Framing {#sec-ch23-decision-framing}
## Necessary but Insufficient {#sec-ch23-conclusion}

### part_5/p5-ch24-interpretability.qmd
# Interpretability {#sec-ch24-interpretability}
## Attribution Methods and Input Importance {#sec-ch24-attribution}
### *In Silico* Mutagenesis {#sec-ch24-ism}
### Gradient-Based Attribution {#sec-ch24-gradient}
### Reconciling Attribution Methods {#sec-ch24-reconciling}
## Interpreting Convolutional Filters {#sec-ch24-cnn-filters}
### From Filters to Position Weight Matrices {#sec-ch24-filter-pwm}
### Deeper Layers and Combinatorial Patterns {#sec-ch24-deeper-layers}
## Motif Discovery from Attributions {#sec-ch24-motif-discovery}
## Probing Learned Representations {#sec-ch24-probing}
### Probing Methodology {#sec-ch24-probing-methods}
### Limitations of Probing {#sec-ch24-probing-limits}
## Attention Patterns in Transformer Models {#sec-ch24-attention}
### What Attention Patterns Reveal {#sec-ch24-attention-patterns}
### Why Attention Weights Mislead {#sec-ch24-attention-caution}
## Regulatory Vocabularies and Global Interpretability {#sec-ch24-global}
### Sequence Classes from *Sei* {#sec-ch24-sei}
### Embedding Geometry and Regulatory Programs {#sec-ch24-embedding-geometry}
## Mechanistic Interpretability {#sec-ch24-mechanistic}
### Circuits and Features {#sec-ch24-circuits}
### Applications to Genomic Models {#sec-ch24-mechanistic-genomics}
## Validation: From Explanations to Experiments {#sec-ch24-validation}
### Faithfulness Testing {#sec-ch24-faithfulness}
### Experimental Validation {#sec-ch24-experimental}
## Interpretability in Clinical Variant Assessment {#sec-ch24-clinical}
## Practical Approaches for Foundation Model Analysis {#sec-ch24-practical}
## Plausibility Is Not Faithfulness {#sec-ch24-conclusion}

### part_5/p5-ch25-causal.qmd
# Causal Inference with Foundation Models {#sec-ch25-causal}
## Prediction vs. Causation {#sec-ch25-prediction-vs-causation}
### The Ladder of Causation {#sec-ch25-ladder}
### Why Predictive Accuracy ≠ Causal Understanding {#sec-ch25-prediction-not-causation}
### The Clinical Stakes {#sec-ch25-clinical-stakes}
## Causal Methods in Genomics {#sec-ch25-causal-methods}
### Mendelian Randomization {#sec-ch25-mendelian-randomization}
### Fine-Mapping for Causal Variants {#sec-ch25-fine-mapping}
### From GWAS to Causal Genes {#sec-ch25-gwas-to-genes}
## Foundation Models and Causality {#sec-ch25-fm-causality}
### Can Foundation Models Learn Causal Structure? {#sec-ch25-fm-causal-structure}
### In-Silico Perturbation Prediction {#sec-ch25-in-silico-perturbation}
### Counterfactual Reasoning Limitations {#sec-ch25-counterfactual-limits}
## Intervention Prediction {#sec-ch25-intervention-prediction}
### CRISPR Screen Analysis with Foundation Models {#sec-ch25-crispr-screens}
### Drug Response Prediction {#sec-ch25-drug-response}
### Closed-Loop Experimental Validation {#sec-ch25-closed-loop}
## Causal Discovery {#sec-ch25-causal-discovery}
### Learning Regulatory Networks {#sec-ch25-regulatory-networks}
### Temporal Causality {#sec-ch25-temporal-causality}
### Multi-Omics Causal Structure {#sec-ch25-multi-omics-causal}
## Clinical Implications {#sec-ch25-clinical-implications}
### Drug Target Validation Evidence Hierarchy {#sec-ch25-target-validation}
### Regulatory Requirements for Causal Claims {#sec-ch25-regulatory-requirements}
## Looking Forward {#sec-ch25-conclusion}

### part_5/p5-ch26-regulatory.qmd
# Regulatory and Governance {#sec-ch26-regulatory}
## Regulatory Frameworks for Genomic AI {#sec-ch26-regulatory}
### Software as Medical Device Paradigm {#sec-ch26-samd}
### European and Global Regulatory Landscapes {#sec-ch26-global-regulation}
### Validation Requirements for Clinical Genomic AI {#sec-ch26-validation}
## Data Governance and Consent {#sec-ch26-governance}
### Consent Problem at Scale {#sec-ch26-consent}
### Biobank Governance Models {#sec-ch26-biobanks}
### Secondary Use and Data Futures {#sec-ch26-secondary-use}
## Privacy and Genomic Data {#sec-ch26-privacy}
### Re-identification Challenge {#sec-ch26-reidentification}
### Family and Relational Privacy {#sec-ch26-family-privacy}
## Intellectual Property and Ownership {#sec-ch26-ip}
### Genomic Data Ownership {#sec-ch26-data-ownership}
### Model Weights as Assets {#sec-ch26-model-weights}
### Prediction Ownership and Liability {#sec-ch26-liability}
## Responsible Development Practices {#sec-ch26-responsible}
### Transparency and Documentation {#sec-ch26-transparency}
### Fairness and Performance Equity {#sec-ch26-fairness}
### Human Oversight and Decision Support {#sec-ch26-oversight}
## Dual Use and Biosecurity {#sec-ch26-biosecurity}
### Generative Models and Pathogen Enhancement {#sec-ch26-pathogen}
### Access Controls and Responsible Release {#sec-ch26-access}

### part_6/p6--applications.qmd
# Part VI: Clinical Translation {.unnumbered}

### part_6/p6-ch27-clinical-risk.qmd
# Clinical Risk Prediction {#sec-ch27-clinical-risk}
## From Polygenic Scores to Foundation Model Features {#sec-ch27-pgs-to-fm}
## Defining Clinical Risk Prediction {#sec-ch27-defining-risk}
## Feature Integration Architectures {#sec-ch27-feature-integration}
## EHR Integration and Phenotype Embeddings {#sec-ch27-ehr-integration}
### EEPRS Framework {#sec-ch27-eeprs}
### Understanding When Embeddings Help {#sec-ch27-embeddings-help}
### PRS-PheWAS for Clinical Interpretation {#sec-ch27-prs-phewas}
### Implementation Considerations {#sec-ch27-eeprs-implementation}
### Integration with Foundation Model Features {#sec-ch27-eeprs-fm}
## Temporal Modeling Architectures {#sec-ch27-temporal-modeling}
## Evaluation for Clinical Deployment {#sec-ch27-evaluation}
### Discrimination {#sec-ch27-discrimination}
### Calibration {#sec-ch27-calibration}
### Clinical Utility {#sec-ch27-clinical-utility}
### Validation Hierarchy {#sec-ch27-validation-hierarchy}
## Uncertainty Quantification {#sec-ch27-uncertainty}
## Fairness and Health Equity {#sec-ch27-fairness}
## Clinical Integration {#sec-ch27-clinical-integration}
### Workflow Integration Patterns {#sec-ch27-workflow-patterns}
### System Architecture {#sec-ch27-system-architecture}
### Post-Deployment Monitoring {#sec-ch27-monitoring}
## Regulatory and Quality Frameworks {#sec-ch27-regulatory}
## Case Studies {#sec-ch27-case-studies}
### Cardiometabolic Risk Stratification {#sec-ch27-case-cardio}
### Oncology Prognosis {#sec-ch27-case-oncology}
### Pharmacogenomic Adverse Event Prediction {#sec-ch27-case-pharmacogenomics}
## Translation as the Test {#sec-ch27-translation-test}

### part_6/p6-ch28-rare-disease.qmd
# Rare Disease Diagnosis {#sec-ch28-rare-disease}
## Variant Prioritization Funnel {#sec-ch28-prioritization-funnel}
### Quality and Technical Filters {#sec-ch28-quality-filters}
### Population Frequency Filters {#sec-ch28-frequency-filters}
### Consequence and Gene Filters {#sec-ch28-consequence-filters}
### Foundation Model Scoring {#sec-ch28-fm-scoring}
## ACMG-AMP Criteria and Computational Evidence {#sec-ch28-acmg-amp}
### Evidence Categories {#sec-ch28-evidence-categories}
### PP3 and BP4: Computational Evidence {#sec-ch28-pp3-bp4}
### Calibrating Predictions to Evidence Strength {#sec-ch28-calibration}
## Family-Based Analysis {#sec-ch28-family-analysis}
### *De Novo* Variants {#sec-ch28-de-novo}
### Compound Heterozygosity and Phasing {#sec-ch28-compound-het}
### Segregation Analysis {#sec-ch28-segregation}
## Somatic Variant Interpretation in Cancer {#sec-ch28-somatic}
### Germline versus Somatic Distinction {#sec-ch28-germline-somatic}
### Driver Classification {#sec-ch28-driver}
### Therapeutic Biomarkers {#sec-ch28-biomarkers}
## Laboratory Validation {#sec-ch28-validation}
### Types of Functional Assays {#sec-ch28-assay-types}
### Integrating Functional Evidence {#sec-ch28-functional-integration}
### Closing the VUS Loop {#sec-ch28-vus-loop}
## Practical Workflow Integration {#sec-ch28-workflow}
### Laboratory Workflow {#sec-ch28-lab-workflow}
### Clinical Decision-Making {#sec-ch28-clinical-decisions}
### Regulatory and Ethical Considerations {#sec-ch28-regulatory}
## Interpretive Partnership {#sec-ch28-partnership}

### part_6/p6-ch29-drug-discovery.qmd
# Drug Discovery {#sec-ch29-drug-discovery}
## Genetic Foundation of Target Selection {#sec-ch29-genetic-foundation}
### From Variant-Level Predictions to Gene-Level Evidence {#sec-ch29-variant-to-gene}
### Linking Genetics to Target Safety and Efficacy {#sec-ch29-safety-efficacy}
## Network-Aware Target Discovery and Repurposing {#sec-ch29-network-discovery}
### Propagating Genetic Signals Through Networks {#sec-ch29-network-propagation}
### Drug Repurposing Through Shared Representations {#sec-ch29-repurposing}
## Drug-Target Interaction Prediction {#sec-ch29-dti-prediction}
### Representing Targets for Binding Prediction {#sec-ch29-binding-prediction}
### Selectivity and Off-Target Prediction {#sec-ch29-selectivity}
## Toxicity Prediction from Genomic Context {#sec-ch29-toxicity}
### Genetic Evidence of Target Liabilities {#sec-ch29-genetic-liabilities}
### Expression-Based Toxicity Prediction {#sec-ch29-expression-toxicity}
### Integrating Genomic Context with Chemical Properties {#sec-ch29-integrated-toxicity}
## Functional Genomics Screens and Perturbation Models {#sec-ch29-functional-screens}
### Designing Informative Perturbation Libraries {#sec-ch29-library-design}
### Perturb-seq and Transcriptomic Readouts {#sec-ch29-perturb-seq}
### Closing the Loop: Lab-in-the-Loop Refinement {#sec-ch29-lab-in-loop}
## Biomarker Development and Patient Stratification {#sec-ch29-biomarkers}
### Foundation Model Features for Stratification {#sec-ch29-stratification-features}
### Multi-Omic Biomarker Discovery {#sec-ch29-multi-omic-biomarkers}
### Trial Design and Endpoint Selection {#sec-ch29-trial-design}
## Industry Workflows and Infrastructure {#sec-ch29-industry-workflows}
### Building Model Infrastructure {#sec-ch29-model-infrastructure}
### Strategic Choices: Build, Buy, or Fine-Tune {#sec-ch29-build-buy-finetune}
### Industry Context: Timelines and Decision Gates {#sec-ch29-timelines}
### Intellectual Property and Data Considerations {#sec-ch29-ip-data}
## Evaluation and Validation {#sec-ch29-evaluation}
### Benchmark Limitations {#sec-ch29-benchmark-limits}
### From Prediction to Validation {#sec-ch29-prediction-validation}
## Connections to Molecular Design {#sec-ch29-molecular-design}
## Prioritization, Not Automation {#sec-ch29-conclusion}

### part_6/p6-ch30-design.qmd
# Sequence Design {#sec-ch30-design}
## Design Formalism {#sec-ch30-formalism}
## Protein Design with Language Models {#sec-ch30-protein-design}
### Sequence Generation from Language Model Priors {#sec-ch30-plm-generation}
### Structure-Aware Design with Diffusion Models {#sec-ch30-structure-diffusion}
### Functional Conditioning and Multi-Objective Optimization {#sec-ch30-multi-objective}
## Regulatory Sequence Design {#sec-ch30-regulatory-design}
### Promoter and Enhancer Engineering {#sec-ch30-promoter-enhancer}
### Splicing and RNA Processing Elements {#sec-ch30-splicing-design}
## mRNA Design and Optimization {#sec-ch30-mrna-design}
### Codon Optimization Principles {#sec-ch30-codon-optimization}
### Stability Engineering and UTR Design {#sec-ch30-utr-design}
### Immunogenicity Considerations {#sec-ch30-mrna-immunogenicity}
## Antibody and Vaccine Design {#sec-ch30-antibody-vaccine}
### CDR Optimization and Humanization {#sec-ch30-cdr-optimization}
### Vaccine Antigen Design {#sec-ch30-vaccine-design}
## Closed-Loop Design-Build-Test-Learn Cycles {#sec-ch30-dbtl}
### Active Learning for Efficient Exploration {#sec-ch30-active-learning}
### High-Throughput Experimentation Integration {#sec-ch30-high-throughput}
## Validation Requirements and Failure Modes {#sec-ch30-validation}
### Validation Hierarchy {#sec-ch30-validation-hierarchy}
### Characteristic Failure Patterns {#sec-ch30-failure-patterns}
## Practical Design Constraints {#sec-ch30-practical-constraints}
### Manufacturing and Developability {#sec-ch30-manufacturing}
### Safety and Biosecurity Considerations {#sec-ch30-biosecurity}
## Algorithmic Search and Optimization {#sec-ch30-algorithms}
## From Understanding to Creating {#sec-ch30-conclusion}

### part_6/p6-ch31-frontiers.qmd
# Frontiers and Synthesis {#sec-ch31-frontiers}
## Open Technical Problems {#sec-ch31-technical}
### Scaling and Efficiency {#sec-ch31-scaling}
### Context and Multi-Scale Integration {#sec-ch31-multiscale}
### Causality and Mechanism {#sec-ch31-causality}
## Emerging Directions {#sec-ch31-emerging}
### Multimodal Integration {#sec-ch31-multimodal}
### Agentic and Closed-Loop Systems {#sec-ch31-agentic}
### Clinical Integration and Learning Health Systems {#sec-ch31-learning-health}
## Work Ahead {#sec-ch31-conclusion}
