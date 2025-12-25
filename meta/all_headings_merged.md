# Headings from p1-ch01-ngs.qmd

# From Reads to Variants {#sec-ngs}
## NGS Data Challenges
## Targeting Strategies: Panels, Exomes, and Genomes
### Targeted and Panel Sequencing
### Whole-Exome Sequencing
### Whole-Genome Sequencing
### Long-Read Sequencing Technologies
## Classical Variant Calling Pipelines
### From Sequencer to Aligned Reads
### Per-Sample Variant Calling
### Cohort Calling and Filtering
### Sample-Level Quality Control
## Haplotype Phasing {#sec-phasing}
### Clinical and Analytical Importance
### Phasing Methods
### Genotype Imputation and Refinement
### Hybrid Sequencing and Coverage Boosting
## Sources of Error and Uncertainty
### Mapping Ambiguity and Reference Bias
### Systematic Sequencing Artifacts
### Coverage Gaps and Allelic Imbalance
### Complex Variants and Representation
## Difficult Regions: The Limits of Short-Read Calling
### Segmental Duplications and Gene Families
### Low-Complexity and Repetitive Sequence
### HLA Region Complexity
## Benchmarking and Ground Truth
### GIAB Reference Samples
### Metrics and Their Meaning
### Limitations of Benchmarks
## DeepVariant: Variant Calling as Image Classification {#sec-deepvar}
### Pileup Images as Input
### Architecture and Training
### Cohort Calling with *GLnexus*
### Comparison with Classical Approaches
## Implications for Genomic Deep Learning
### Variants as Atomic Units
### Inherited Biases and Blind Spots
### Effect Sizes Across the Frequency Spectrum
##  Reliability Landscape

# Headings from p1-ch02-data.qmd

#  Data Landscape {#sec-data}
## Reference Genomes and Gene Annotations
### Reference Assemblies
### Gene Models
## Population Variant Catalogs and Allele Frequencies
### dbSNP and Variant Identifiers
### 1000 Genomes and Early Reference Panels
### Genome Aggregation Database (gnomAD)
### Interpreting Constraint Metrics
## Biobanks and GWAS Data
### Large Population Cohorts
### GWAS Summary Statistics
## Functional Genomics and Regulatory Landscapes
### ENCODE, Roadmap, and Related Consortia
### Cistrome Data Browser
### From Assays to Training Labels
### Deep Mutational Scanning and Multiplexed Variant Assays
## Expression and eQTL Resources
### Bulk Expression Atlases
### Single-Cell and Context-Specific Expression
## Phenotype Definition and Data Quality
###  Problem of Binary Disease Definitions
### Electronic Health Record Quality and Completeness
### Coding Inconsistencies and Label Noise
### Deep Phenotyping Approaches
### Impact on Downstream Modeling
## Variant Interpretation Databases and Clinical Labels
### ClinVar and Clinical Assertions
### Complementary Clinical Databases
### ClinGen and Expert Curation
### Pharmacogenomics Resources
## Star-Allele Nomenclature
## Inherited Constraints

# Headings from p1-ch03-gwas.qmd

# GWAS and Polygenic Scores {#sec-gwas}
##  GWAS Framework
### Association Models for Quantitative Traits
### Association Models for Disease Outcomes
### Manhattan Plots and Q-Q Plots
### Population Structure Control
## Heritability: What Genetics Can Explain
### Pedigree Heritability
### SNP-Heritability and the Missing Heritability Problem
### Implications for GWAS and Polygenic Scores
## Linkage Disequilibrium and the Association-Causation Gap
###  Structure of Linkage Disequilibrium
### Causal Variants, Tag Variants, and GWAS Catalogs
## Fine-Mapping: From Loci to Causal Variants
###  Statistical Framework
### Functional Annotation Priors
### Multi-Ancestry Fine-Mapping
## Polygenic Score Construction
### Terminology: PGS versus PRS
### Clumping and Thresholding
### LD-Aware Bayesian Methods
### Fine-Mapping-Informed Scores
## Polygenic Score Interpretation
### Relative Risk and Percentiles
### Absolute Risk
### Explained Variance and Discrimination
## Ancestry, Portability, and Fairness
###  Portability Problem
### Fairness and Health Equity
## Phenome-Wide Association Studies
###  PheWAS Framework
### PheWAS for Polygenic Score Interpretation
### Phenotype Quality and PheWAS Power
### Deep Phenotyping and Embedding-Enhanced GWAS
## From Association to Mechanism

# Headings from p1-ch04-vep-classical.qmd

# Classical Variant Prediction {#sec-vep-classical}
## Conservation-Based Approaches
### Evolutionary Constraint Metrics
### What Conservation Measures Versus What Clinicians Need
### Clinical Application and Boundaries
###  ACMG-AMP Variant Classification Framework
## Protein-Level Predictors
### *SIFT*: Sequence Homology as Functional Constraint
### *PolyPhen-2*: Integrating Structure and Sequence
### From Sequence to Function
### Boundaries of Protein-Level Prediction
##  *CADD* Framework
### Evolutionary Proxy Training and Label Sources
### Feature Integration
### Model Architecture and Scoring
###  Evolutionary Proxy Problem
## Other Ensemble Methods
### *REVEL*
### *M-CAP*
### Comparison and Selection
## Circularity and Ascertainment Bias
###  Circularity Problem
### Ascertainment Bias
### Implications for Clinical Use
## Limitations of the Feature Engineering Paradigm
###  Feature Ceiling
### Limited Context
###  Persistent Gap Between Measurement and Need
### From Features to Representations

# Headings from p2-ch05-representations.qmd

# Tokens and Embeddings {#sec-representations}
## One-Hot Encoding: The CNN Foundation
## $K$-mer Tokenization: The DNABERT Approach
## Byte Pair Encoding: Learning the Vocabulary
## Single-Nucleotide Tokenization: Maximum Resolution
## Biologically-Informed Tokenization
## From Tokens to Embeddings: Learning Representations
## Position Encodings: Where Tokens Live
### Absolute Positional Embeddings
### Sinusoidal Positional Encodings
### Relative Positional Encodings
### Rotary Position Embeddings
### Attention with Linear Biases
### Genomic-Specific Considerations
## Special Considerations for Biological Sequences
## Trade-offs and Practical Guidance
### Resolution Versus Compression
### Vocabulary Size and Model Capacity
### Computational Efficiency
### Variant Interpretation Requirements
### Practical Heuristics
##  Compression-Resolution Trade-off

# Headings from p2-ch06-cnn.qmd

# Convolutional Networks {#sec-cnn}
## Convolutions as Sequence Pattern Detectors
## *DeepSEA*: Regulatory Prediction from Sequence {#sec-deepsea}
### Architecture and Training
### Learned Representations and Biological Validation
### Variant Effect Prediction
## Cell-Type Specificity and Regulatory Grammar {#sec-basset-danq}
## *ExPecto*: From Chromatin to Expression {#sec-expecto}
###  Modular Architecture
### Expression Prediction and Variant Effects
## *SpliceAI*: Clinical-Grade Splicing Prediction {#sec-spliceai}
### Architecture: Depth and Dilation
### Performance and Validation
### Clinical Impact
##  Receptive Field Ceiling {#sec-receptive-field}
## Sequential Processing and Its Costs {#sec-rnn}
###  Vanishing Gradient Problem
### *DanQ*: Combining Convolutions and Recurrence
###  Sequential Bottleneck
## Specialization and Its Limits

# Headings from p2-ch07-attention.qmd

# Transformers and Attention {#sec-attention}
##  Self-Attention Mechanism
### Query, Key, and Value Vectors
### Multi-Head Attention
## Positional Encoding {#sec-positional-encoding}
### Absolute Position Encodings
### Relative Position Encodings
### Genomic Position Considerations
##  Transformer Block
### Block Components
### Information Flow and Depth
## Scaling to Genomic Sequences
###  Quadratic Barrier
### Parameter Considerations
### Context Length Strategies
### Memory and Precision
## Architectural Variants for Genomics
### Encoder-Only Transformers
### Decoder-Only Transformers
### Encoder-Decoder Transformers
### Hybrid CNN-Transformer Models
## Training Dynamics
### Optimization
### Regularization
### Gradient Stability
### Distributed Training
## Limitations and Emerging Alternatives
###  Quadratic Ceiling
### State Space Models
### Choosing Architectures
## Architecture and Learning

# Headings from p2-ch08-pretraining.qmd

# Pretraining Strategies {#sec-pretraining}
## Masked Language Modeling
### Masking Strategies and Their Implications
### What Masked Language Models Learn
## Next-Token Prediction
### Genomic Applications
### MLM and Autoregressive Comparison
## Span Corruption and Denoising
### Biologically Motivated Corruption
## Contrastive Learning
### Augmentation Design for Genomic Sequences
### Cross-Species Contrastive Learning
## Multi-Task Pretraining
### Large-Scale Multi-Task Examples
### Multi-Task Tradeoffs
## Data Strategies for Pretraining
## Optimization and Scaling
## Training Diagnostics
## Strategy Selection
## Pretraining in Practice: Case Studies
## Open Questions
## From Sequence Statistics to Biological Knowledge

# Headings from p2-ch09-transfer.qmd

# Transfer and Adaptation {#sec-transfer}
## Source and Target Domains
###  Gap Between Pretraining and Deployment
### Recognizing Transfer Outcomes
## Feature Extraction with Frozen Backbones
### Linear Probing
### When Linear Probing Fails
## Parameter-Efficient Fine-Tuning
### Low-Rank Adaptation
### Alternative PEFT Approaches
## Full Fine-Tuning
### Making Full Fine-Tuning Work
###  Risks of Unconstrained Adaptation
## Probing Representations
### What Probing Reveals About Pretrained Models
### Probing Guides Adaptation Strategy
## Choosing an Adaptation Strategy
### Data Quantity Determines What Is Possible
### Task Similarity Determines What Is Necessary
## Domain Shift and Cross-Context Transfer
### Types of Domain Shift in Genomics
### Detecting and Mitigating Shift
## Few-Shot and Zero-Shot Learning
### Few-Shot Learning with Minimal Examples
### Zero-Shot Transfer Without Task-Specific Data
## When Transfer Fails
### Diagnosing Negative Transfer
### Remediation When Transfer Fails
## Case Studies in Transfer Learning
### *DNABERT* for Chromatin Accessibility
### *ESM* for Variant Pathogenicity
### *Enformer* for Cross-Tissue Expression
### Cross-Species Regulatory Prediction
## Validation and Common Pitfalls
### Sources of Spurious Success
### Evaluation Practices That Reveal True Performance
## Emerging Directions
### In-Context Learning
### Test-Time Adaptation
### Federated Learning Across Institutions
### Toward Theoretical Foundations
## Amplification and Its Risks

# Headings from p3-ch10-fm-principles.qmd

# Foundation Model Paradigm {#sec-fm-principles}
## From Task-Specific Models to Foundation Models
## Defining Genomic Foundation Models
### Essential Properties
### What Doesn't Count
###  Metaphor Itself
## Scaling Laws and Compute-Optimal Training
###  Scaling Law Framework
### Empirical Scaling in Genomic Models
### Compute-Optimal Decisions for Genomics
### Emergent Capabilities
## A Taxonomy of Genomic Foundation Models
### DNA Language Models
### Sequence-to-Function Foundation Models
### Variant Effect Prediction Models
### Multi-Omic Foundation Models
## Design Dimensions
### Data Composition
### Architecture Choices
### Context Length
### Tokenization
## Build Versus Use Decisions
### When to Use Existing Models
### When to Adapt Existing Models
### When to Train from Scratch
### Cost-Benefit Analysis
## Evaluation Principles
### Multi-Task Assessment
### Transfer Versus Pretraining Performance
##  Foundation Model Ecosystem
### Model Distribution
### Documentation Requirements
### Industry and Academic Contributions
## Open Questions
## Complementary Tools at Scale

# Headings from p3-ch11-dna-lm.qmd

# DNA Language Models {#sec-dna-lm}
## From Task-Specific CNNs to General-Purpose Language Models
## *DNABERT*: The First DNA Language Model
## *Nucleotide Transformer*: Scaling Data and Model Diversity
## *GPN*: Cross-Species Pretraining for Variant Effect Prediction
##  Long-Context Revolution
### *HyenaDNA*: Megabase Context via Implicit Convolutions
### *Caduceus*: Bidirectional Processing with Reverse-Complement Equivariance
### *Evo 2*: Genome-Scale Modeling Across the Tree of Life
## Training Data and What Models Learn
### Training Corpus Composition
### Probing What Models Learn
### What Models Do Not Learn
## Benchmark Performance and Evaluation
### Major Benchmark Suites
### Benchmark Limitations
## Annotation-Aware Extensions
## Using DNA Language Models in Practice
### Embeddings as Universal Features
### Fine-Tuning and Adaptation
### Zero-Shot and Few-Shot Scoring
## Limitations and Open Challenges
## Representations Without Predictions

# Headings from p3-ch12-protein-lm.qmd

# Protein Language Models {#sec-protein-lm}
##  *ESM* Model Family
### *ESM-1b*: Establishing the Paradigm
### Emergent Biological Knowledge
### *ESM-2*: Scaling Up
## Alternative Architectures
## Attention and Evolutionary Coupling
## *ESMFold*: Structure from Sequence
### Eliminating the Alignment Bottleneck
### What *ESMFold* Reveals About PLMs
## Function Prediction
## Variant Effect Prediction
## Integration with Structure Prediction
## Limitations
### Orphan and Dark Proteins
### Novel Folds
### Conformational Flexibility
### Epistasis
### Interpretability
## Lessons for Genomic Foundation Models
### Self-Supervision Captures Biological Knowledge
### Scale Yields Consistent Improvements
### Transfer Learning is Effective
### Architecture Choices Must Match Sequence Properties
### Integration Multiplies Capability
##  Paradigm That Generalized

# Headings from p3-ch13-regulatory.qmd

# Regulatory Models {#sec-regulatory}
##  Long-Range Regulation Problem
## *Enformer*: Attention Meets Regulatory Genomics
### Architecture
### Training Data and Cross-Species Learning
### Variant Effect Prediction
## *Borzoi*: From Chromatin to Transcriptome
### Motivation
### Architecture and Training
### Applications Beyond Expression Level
## *Sei*: A Regulatory Vocabulary from Sequence
### Approach
### Complementary to Track Prediction
## *AlphaGenome*: Unifying Modalities at Megabase Scale
### Architectural Extensions
### Access and Practical Considerations
## What Hybrid Architectures Accomplish
### Spanning Enhancer-Promoter Distances
### Multi-Task Regularization
### Cross-Species Constraints
### Unified Variant Effect Prediction
## Limitations and Open Challenges
### Training Data Constraints
### Finite Context
### Missing Three-Dimensional Context
### Correlation Versus Causation
### Interpretability Challenges
## Relationship to Foundation Models
## Prediction Without Explanation

# Headings from p3-ch14-vep-fm.qmd

# Variant Effect Prediction {#sec-vep-fm}
##  Foundation Model Paradigm for Variant Interpretation
### Zero-Shot and Supervised Approaches
## Protein-Based Variant Effect Prediction
### Zero-Shot Scoring with Protein Language Models
### Alignment-Based Models: EVE and popEVE
### *AlphaMissense*: Structure-Informed Pathogenicity Prediction
## DNA-Based Variant Effect Prediction
### Splice Variant Prediction with SpliceAI
### Regulatory Variant Prediction with Enformer
### DNA Language Models: GPN-MSA and Evo 2
### AlphaGenome: Unified Multi-Omic Variant Effect Prediction
## Combining Evidence Across Modalities
### Integration Strategies
### Avoiding Double-Counting
### Practical Workflow Design
## Calibration and Clinical Categories
### Assessing Calibration
### Calibration Methods
### Mapping to ACMG Categories
## Uncertainty Quantification
### Sources of Uncertainty
### Uncertainty Estimation Methods
### Out-of-Distribution Detection
## What Foundation Models Add
### Improved Discrimination
### Extended Coverage
### Mechanistic Interpretability
### Persistent Limitations
## Clinical Integration Considerations
### Laboratory Validation
### Workflow Integration
### Communication to Clinicians
## Open Challenges
### Complex Variant Types
### Combinatorial Effects
### Phenotype Specificity
### Temporal and Environmental Context
### Equity and Access
## Tools for Interpretation, Not Oracles

# Headings from p4-ch15-rna.qmd

# RNA Structure and Function {#sec-rna}
## RNA as Molecule Versus Transcriptome Readout
## Why Secondary Structure Creates a Distinct Modeling Challenge
###  Flat Energy Landscape Problem
### Base Pairing and Long-Range Dependencies
### Pseudoknots and Tertiary Complexity
## Classical Approaches to Structure Prediction
### rmodynamic Folding Models
### Comparative and Covariation Methods
## Deep Learning for Secondary Structure Prediction
### From Thermodynamics to Learned Patterns
### Structure Probing as Supervision
## RNA Foundation Models
###  Scale Gap with Protein Language Models
### Architectures and Objectives
### Downstream Applications
## Codon-Level Models for Coding RNA
### Beyond Nucleotide Tokenization
### What Codon Models Add
## UTR Models and Translation Regulation
### Why UTRs Dominate Expression Control
### Sequence-to-Expression Models
### Integration with mRNA Design
## mRNA Design and Optimization
### Design Objectives and Trade-offs
### Lessons from COVID-19 Vaccines
### Model-Based Design Strategies
## Noncoding RNA Classification and Function
###  Diversity of Noncoding RNA
### From Handcrafted Features to Learned Representations
## miRNA Target Prediction
## Splicing and Transcript Processing Models
### Beyond *SpliceAI*
## Limitations and Open Challenges
### Sparse Structural Data
### Functional Annotation Gaps
###  Maturity Gap
##  Bridge Between Sequence and Cell

# Headings from p4-ch16-single-cell.qmd

# Single-Cell Models {#sec-single-cell}
##  Single-Cell Data Landscape
### From Bulk to Single-Cell Resolution
### Technical Challenges and Data Characteristics
## Cellular Language Models
### Geneformer: Learning Network Biology
### *scGPT*: Generative Pretraining for Single-Cell Analysis
### *scFoundation* and Scaling Single-Cell Models
### *TranscriptFormer*: Cross-Species Cellular Models
## Perturbation Response Prediction
###  *In Silico* Experiment Promise
### Perturb-seq and Foundation Model Training
### Limitations of Current Approaches
## Epigenomic Foundation Models
### DNA Methylation and CpGPT
### Chromatin Accessibility Models
## Cross-Modality Integration
###  Unpaired Integration Challenge
### *GLUE*: Graph-Linked Unified Embedding
### Applications of Cross-Modal Integration
## Practical Challenges and Limitations
### Batch Effects and Technical Artifacts
### Cell Type Imbalance
### Evaluation Complexity
### Causality and Mechanism
## From Sequence to State

# Headings from p4-ch17-3d-genome.qmd

# 3D Genome Organization {#sec-3d-genome}
## Chromatin Organization Hierarchy {#sec-chromatin-hierarchy}
## Measuring the 3D Genome {#sec-3d-measurement}
## Predicting 3D Structure from Sequence {#sec-3d-prediction}
## 3D Structure and Gene Regulation {#sec-3d-regulation}
## Spatial Transcriptomics {#sec-spatial-transcriptomics}
## Limitations and Open Questions {#sec-3d-limitations}
## Structure as Context, Not Cause

# Headings from p4-ch18-networks.qmd

# Graph and Network Models {#sec-networks}
## Biological Networks and Data Resources
###  Landscape of Biological Graphs
### Biases and Limitations
## Graph Neural Network Fundamentals
### Why Message Passing?
### Canonical Architectures
## Foundation Model Embeddings as Node Features
###  Integration Principle
### Practical Integration Patterns
### Evidence for the Integration Benefit
## Applications
### Disease Gene Prioritization
### Drug-Target Interaction Prediction
### Knowledge Graph Reasoning and Drug Repurposing
### Pathway and Module Analysis
### Cell Type and State Annotation
## Practical Considerations
### Graph Construction Quality
### Scalability and Mini-Batching
### Robustness to Noise and Missingness
### Interpretation and Validation
## Limitations and Open Challenges
###  Study Bias Problem
### Causality Versus Association
### Negative Data and Class Imbalance
### Distribution Shift
## Relational Reasoning at a Different Scale

# Headings from p4-ch19-multi-omics.qmd

# Multi-Omics Integration {#sec-multi-omics}
##  Limits of Single-Modality Models
## Integration Strategies and Their Tradeoffs
### Early Fusion
### Late Fusion
### Intermediate Fusion
## Multi-Omics Foundation Models
### Factor-Based Integration
### Deep Generative Multi-Omics Models
### Contrastive Multi-Modal Learning
## Clinical Integration: EHR, Imaging, and Molecular Data
### Electronic Health Records as a Modality
### Imaging Integration
### Multi-Modal Clinical Prediction Models
##  Systems View: From Variant to Phenotype
###  Information Cascade
### Bottleneck Modalities
### Causal vs. Correlational Integration
## Handling Missing Modalities
### Training with Incomplete Data
### Cross-Modal Imputation
### Zero-Shot Cross-Modal Transfer
## Practical Challenges
### Batch Effects Across Modalities
### Sample Size and Power
### Interpretability Across Modalities
### Evaluation Complexity
## Integration as Means, Not End

# Headings from p5-ch20-benchmarks.qmd

# Benchmarks {#sec-benchmarks}
## Protein Language Model Benchmarks
### TAPE: Tasks Assessing Protein Embeddings
### FLIP: Function-Linked Protein Benchmark
### ProteinGym: Comprehensive Variant Effect Evaluation
### Structure Prediction Benchmarks
## DNA and Regulatory Benchmarks
### Classical Regulatory Prediction Tasks
### Quantitative Regulatory Prediction
### Genomic Benchmarks
### BEND: Benchmark for DNA Language Models
### Long-Range Benchmarks
### Cross-Species Evaluation
## Variant Effect Prediction Benchmarks
### Clinical Variant Databases
### CAGI: Critical Assessment of Genome Interpretation
### Deep Mutational Scanning Benchmarks
### Regulatory and Non-Coding Variant Benchmarks
## Trait and Population-Level Benchmarks
### Polygenic Score Evaluation
### TraitGym
### EmbedGEM Framework
## Benchmark Construction and Hidden Assumptions
### Data Sources and Label Provenance
### Splitting Strategies and Leakage
### Metric Selection and Aggregation
### Goodhart's Law and Benchmark Gaming
## Benchmark Saturation and Staleness
### Saturation: When Benchmarks Stop Discriminating
### Staleness: When Benchmarks Diverge from Practice
### Leakage from Scale
##  Benchmark-Deployment Gap
### Distribution Shift
### Calibration Requirements
### Metric Mismatch
### Practical Constraints
## Systematic Gaps in Current Benchmarks
## Incentives and Their Limits

# Headings from p5-ch21-eval.qmd

# Evaluation Principles {#sec-evaluation}
## Why Random Splits Fail
## Homology-Aware Splitting
### Clustering Tools and Workflows
# Cluster proteins at 40% identity
# Cluster nucleotides at 90% identity  
# Create database and cluster at 30% identity
### Practical Considerations
## Splitting by Biological Axis
### Splitting by Individual
### Splitting by Genomic Region
### Splitting by Gene or Protein Family
### Splitting by Experimental Context
### Splitting by Ancestry
### Splitting by Time
## Leakage Taxonomy and Detection
### Feature Leakage
### Label Leakage
### Benchmark Leakage
### Detection Strategies
## Metrics for Genomic Tasks
### Discrimination Metrics
### Regression and Correlation Metrics
### Ranking and Prioritization Metrics
### Calibration Metrics
### Clinical Utility Metrics
## Baseline Selection
### Strong Baselines, Not Straw Men
### Historical Baselines and Progress Tracking
### Non-Deep-Learning Baselines
## Ablation Studies
### Component Isolation
### Hyperparameter Sensitivity
### Architecture Search Confounds
### Reporting Standards
## Statistical Rigor
### Significance Testing
### Effect Sizes
### Confidence Intervals on Metrics
### Variance Across Random Seeds
## Evaluating Foundation Models
### Zero-Shot Evaluation
### Linear Probing
### Fine-Tuning Evaluation
### Transfer Across Tasks
## Calibration Essentials
### Assessing Calibration
### Recalibration Methods
## Putting It All Together
##  Question Behind the Metric

# Headings from p5-ch22-confounding.qmd

# Confounders and Leakage {#sec-confounding}
## Confounding, Bias, and Leakage
## Sources of Confounding in Genomic Data
## Population Structure as a Shortcut
## Technical Artifacts as Biological Signal
## Label Bias and Circularity
## Data Splitting
## Data Leakage
## Detecting Confounding
## Mitigation Strategies
### Causal Inference Approaches
## Fairness and External Validity
## A Practical Checklist
## Rigor as Response

# Headings from p5-ch23-uncertainty.qmd

# Uncertainty Quantification {#sec-uncertainty}
## Types of Uncertainty in Genomic Prediction {#sec-uncertainty-types}
### Why Uncertainty Matters
### Epistemic Uncertainty
### Aleatoric Uncertainty
### Decomposing Total Uncertainty
## Calibration: Do Confidence Scores Mean What They Say? {#sec-calibration}
###  Calibration Problem
### Measuring Calibration
### Why Foundation Models Are Often Miscalibrated
### Calibration Across Subgroups
## Post-Hoc Calibration Methods {#sec-post-hoc-calibration}
### Temperature Scaling
### Platt Scaling
### Isotonic Regression
### Calibrating Foundation Model Outputs
## Uncertainty Quantification Methods for Foundation Models {#sec-uq-methods}
### Deep Ensembles
### Monte Carlo Dropout
### Heteroscedastic Models
### Evidential Deep Learning
## Conformal Prediction: Distribution-Free Guarantees {#sec-conformal}
###  Conformal Prediction Framework
### Split Conformal Prediction
### Conformal Prediction for Variant Effect Prediction
### Limitations and Practical Considerations
## Out-of-Distribution Detection {#sec-ood-detection}
###  Out-of-Distribution Problem
### Likelihood-Based Detection and Its Failures
### Embedding-Based Detection
### Practical OOD Detection for Genomic Applications
## Selective Prediction and Abstention {#sec-selective-prediction}
### When to Abstain
### Selective Prediction Methods
### Evaluating Selective Prediction
## Uncertainty for Specific Genomic Tasks {#sec-genomic-uq}
### Variant Effect Prediction Uncertainty
### Regulatory Variant Uncertainty
### Uncertainty Across Populations
## Communicating Uncertainty to End Users {#sec-uncertainty-communication}
###  Communication Challenge
### Categorical Reporting
### Visual Communication
### Decision-Theoretic Framing
## Necessary but Insufficient

# Headings from p5-ch24-interpretability.qmd

# Interpretability {#sec-interpretability}
## Attribution Methods and Input Importance
### *In Silico* Mutagenesis
### Gradient-Based Attribution
### Reconciling Attribution Methods
## Interpreting Convolutional Filters
### From Filters to Position Weight Matrices
### Deeper Layers and Combinatorial Patterns
## Motif Discovery from Attributions
## Probing Learned Representations
### Probing Methodology
### Limitations of Probing
## Attention Patterns in Transformer Models
### What Attention Patterns Reveal
### Why Attention Weights Mislead
## Regulatory Vocabularies and Global Interpretability
### Sequence Classes from Sei
### Embedding Geometry and Regulatory Programs
## Mechanistic Interpretability
### Circuits and Features
### Applications to Genomic Models
## Validation: From Explanations to Experiments
### Faithfulness Testing
### Experimental Validation
## Interpretability in Clinical Variant Assessment
## Practical Approaches for Foundation Model Analysis
## Plausibility Is Not Faithfulness

# Headings from p6-ch25-clinical-risk.qmd

# Clinical Risk Prediction {#sec-clinical-risk}
## From Polygenic Scores to Foundation Model Features
## Defining Clinical Risk Prediction
## Feature Integration Architectures
## EHR Integration and Phenotype Embeddings
###  EEPRS Framework
### Understanding When Embeddings Help
### PRS-PheWAS for Clinical Interpretation
### Implementation Considerations
### Integration with Foundation Model Features
## Temporal Modeling Architectures
## Evaluation for Clinical Deployment
### Discrimination
### Calibration
### Clinical Utility
###  Validation Hierarchy
## Uncertainty Quantification
## Fairness and Health Equity
## Clinical Integration
### Workflow Integration Patterns
### System Architecture
### Post-Deployment Monitoring
## Regulatory and Quality Frameworks
## Case Studies
### Cardiometabolic Risk Stratification
### Oncology Prognosis
### Pharmacogenomic Adverse Event Prediction
## Translation as the Test

# Headings from p6-ch26-rare-disease.qmd

# Rare Disease Diagnosis {#sec-rare-disease}
##  Variant Prioritization Funnel
### Quality and Technical Filters
### Population Frequency Filters
### Consequence and Gene Filters
### Foundation Model Scoring
## ACMG-AMP Criteria and Computational Evidence
### Evidence Categories
### *PP3* and *BP4*: Computational Evidence
### Calibrating Predictions to Evidence Strength
## Family-Based Analysis
### *De Novo* Variants
### Compound Heterozygosity and Phasing
### Segregation Analysis
## Somatic Variant Interpretation in Cancer
### Germline versus Somatic Distinction
### Driver Classification
### rapeutic Biomarkers
## Laboratory Validation
### Types of Functional Assays
### Integrating Functional Evidence
### Closing the VUS Loop
## Practical Workflow Integration
### Laboratory Workflow
### Clinical Decision-Making
### Regulatory and Ethical Considerations
##  Interpretive Partnership

# Headings from p6-ch27-drug-discovery.qmd

# Drug Discovery {#sec-drug-discovery}
##  Genetic Foundation of Target Selection
### From Variant-Level Predictions to Gene-Level Evidence
### Linking Genetics to Target Safety and Efficacy
## Network-Aware Target Discovery and Repurposing
### Propagating Genetic Signals Through Networks
### Drug Repurposing Through Shared Representations
## Drug-Target Interaction Prediction
### Representing Targets for Binding Prediction
### Selectivity and Off-Target Prediction
## Toxicity Prediction from Genomic Context
### Genetic Evidence of Target Liabilities
### Expression-Based Toxicity Prediction
### Integrating Genomic Context with Chemical Properties
## Functional Genomics Screens and Perturbation Models
### Designing Informative Perturbation Libraries
### Perturb-seq and Transcriptomic Readouts
### Closing the Loop: Lab-in-the-Loop Refinement
## Biomarker Development and Patient Stratification
### From Polygenic Scores to Foundation Model Features
### Multi-Omic Biomarker Discovery
### Trial Design and Endpoint Selection
## Industry Workflows and Infrastructure
### Building Model Infrastructure
### Strategic Choices: Build, Buy, or Fine-Tune
### Industry Context: Timelines and Decision Gates
### Intellectual Property and Data Considerations
## Evaluation and Validation
### Benchmark Limitations
### From Prediction to Validation
## Connections to Molecular Design
## Acceleration Through Prioritization

# Headings from p6-ch28-design.qmd

# Sequence Design {#sec-design}
##  design formalism
## Protein design with language models
### Sequence generation from language model priors
### Structure-aware design with diffusion models
### Functional conditioning and multi-objective optimization
## Regulatory sequence design
### Promoter and enhancer engineering
### Splicing and RNA processing elements
## mRNA design and optimization
### Codon optimization principles
### Stability engineering and UTR design
### Immunogenicity considerations
## Antibody and vaccine design
### CDR optimization and humanization
### Vaccine antigen design
## Closed-loop design–build–test–learn cycles
### Active learning for efficient exploration
### Integration with high-throughput experimentation
## Validation requirements and failure modes
###  validation hierarchy
### Characteristic failure patterns
## Practical constraints on design
### Manufacturing and developability
### Safety and biosecurity considerations
## Algorithmic approaches to search and optimization
## From Understanding to Creating

# Headings from p6-ch29-future.qmd

# Ethics and Frontiers {#sec-future}
## Regulatory Frameworks for Genomic AI
###  Software as Medical Device Paradigm
### European and Global Regulatory Landscapes
### Validation Requirements for Clinical Genomic AI
## Data Governance and Consent
###  Consent Problem at Scale
### Biobank Governance Models
### Secondary Use and Data Futures
## Privacy and Genomic Data
###  Re-identification Challenge
### Family and Relational Privacy
## Intellectual Property and Ownership
### Who Owns Genomic Sequence Data?
### Model Weights as Assets
### Prediction Ownership and Liability
## Responsible Development Practices
### Transparency and Documentation
### Fairness and Performance Equity
### Human Oversight and Decision Support
## Dual Use and Biosecurity
### Generative Models and Pathogen Enhancement
### Access Controls and Responsible Release
## Open Technical Problems
### Scaling and Efficiency
### Context and Multi-Scale Integration
### Causality and Mechanism
## Emerging Directions
### Multimodal Integration
### Agentic and Closed-Loop Systems
### Clinical Integration and Learning Health Systems
##  Work Ahead