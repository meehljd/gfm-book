# Dropped glossary terms (from merged list)

Dropped terms: 339. Kept terms: 245.

These were deprioritized as likely familiar to advanced readers, too tool/implementation-specific, too niche, or redundant with chapter explanations.

**Ablation study** [Statistics]: An experiment that removes or alters a component (feature, data source, or model module) to measure its contribution to performance. Helps identify which ingredients actually drive benchmark gains.

**Actionable finding** [Clinical]: A result that can reasonably change patient care, such as guiding surveillance, treatment, or family testing. Genomic AI is most valuable when it increases the yield of actionable findings without raising false positives.

**Activation function** [ML]: A mathematical function applied to a neural network’s weighted sum to introduce nonlinearity, allowing the model to learn complex patterns beyond linear relationships. Common choices include ReLU, GELU, and sigmoid.

**Active learning** [ML]: A training strategy where the model selects informative unlabeled examples to be labeled next, improving performance with fewer labels. Useful in genomics where functional labels are expensive.

**Additive attention** [ML]: An attention scoring approach that uses a learned feed-forward network to combine query and key vectors before computing weights. Often contrasted with dot-product attention; see also: **scaled dot-product attention**.

**Adjacency matrix** [Computation]: A square matrix that encodes a graph’s edges, where entry (i, j) indicates whether nodes i and j are connected (and possibly with what weight). Common input for network analysis and some graph neural networks.

**Adversarial example** [ML]: A deliberately perturbed input that causes a model to change its prediction, often revealing brittleness. In biology, it can expose non-robust sequence features or artifacts in tokenization.

**AliBi (Attention with Linear Biases)** [ML]: A positional bias technique that adds a distance-dependent linear penalty to attention scores, encouraging locality without explicit positional embeddings. Helps transformers extrapolate to longer sequences than seen in training.

**Alignment** [Computation]: The process of mapping sequencing reads to a reference genome to determine where each read originated. Accurate alignment is foundational for **variant calling** and many downstream analyses. See also: **reference genome**, **read**.

**Allele** [Genomics]: One of the alternative DNA sequence states at a genomic position (e.g., A vs G at the same base). In diploid genomes, individuals typically carry two alleles per locus—one per chromosome copy.

**Allele frequency** [Genomics]: The proportion of chromosomes in a population carrying a particular allele at a locus. Used to distinguish common from rare variants and to flag likely sequencing artifacts. See also: **gnomAD**.

**Allelic series** [Genomics]: A set of variants in the same gene that produce a range of phenotypes or severities. Recognizing an allelic series can strengthen gene–disease evidence and improve variant interpretation.

**Alternative splicing** [Genomics]: Process where the same gene produces multiple RNA isoforms by including or skipping different exons. A major source of protein diversity and a frequent mechanism for disease when disrupted.

**Ambient RNA** [Genomics]: Free-floating RNA released from broken cells that can contaminate droplet-based single-cell assays. If uncorrected, it can create false expression signals, especially for highly expressed genes.

**Amino acid** [Genomics]: One of the 20 common building blocks of proteins, encoded by codons in mRNA. Protein language models treat amino acids like tokens in a sequence.

**Ancestry-informed interpretation** [Clinical]: Using population background to interpret variant frequency, LD structure, and risk estimates. Helps avoid misclassification and inequitable performance across populations.

**AnnData** [Computation]: A data structure widely used in Python single-cell workflows (e.g., Scanpy) for storing a sparse expression matrix plus metadata and embeddings. Helps standardize analysis and interoperability.

**Annotation** [Genomics]: A structured label or feature attached to a genomic position or variant, such as gene context, conservation, or regulatory marks. Variant scoring methods (e.g., **CADD**) combine many annotations into a single prioritization score.

**Annotation pipeline** [Computation]: A workflow that adds biological and clinical context to variants or features (genes, pathways, drug targets). Typically includes QC, functional annotation, and evidence aggregation.

**Assay development** [Clinical]: Designing and validating an experimental test (e.g., functional assay, biomarker assay) that supports clinical decisions. In drug discovery, assay quality determines the reliability of downstream modeling.

**Assay for Transposase-Accessible Chromatin using sequencing (ATAC-seq)** [Genomics]: An experimental method that measures chromatin accessibility by sequencing DNA fragments preferentially cut in open chromatin. Provides evidence for regulatory regions and is widely used in regulatory annotation resources.

**Assay transferability** [Statistics]: How well a model trained on one assay’s labels generalizes to another assay or protocol. Weak transferability can break translation from research datasets to clinical labs.

**Augmentation** [ML]: A technique that creates modified versions of training examples to improve generalization and robustness. In genomics, common augmentations include **reverse complement**, jittering, masking, and controlled noise injection.

**Auto-regressive modeling** [ML]: Training setup where a model predicts the next token given previous tokens, building sequences left-to-right (or in a chosen order). The basis of next-token prediction for many large language models; see also: **next-token prediction**.

**Backdoor confounding** [Statistics]: A spurious association introduced by an unobserved or uncontrolled variable that influences both inputs and labels. Can inflate benchmark performance without reflecting causal signal.

**Base rate** [Statistics]: The prevalence of the positive class (e.g., pathogenic variants) in a population or dataset. Base rates affect precision, calibration, and the real-world utility of a score.

**Baseline risk** [Clinical]: A person’s underlying probability of an outcome before considering additional predictors. Baseline risk anchors absolute risk estimates and is needed for clinical decision thresholds.

**Batch normalization (BatchNorm)** [ML]: A normalization layer that stabilizes training by normalizing activations using batch statistics, then scaling and shifting with learned parameters. Widely used in CNNs; see also: **layer normalization**.

**Bayesian optimization** [ML]: An approach for efficiently optimizing expensive functions (e.g., wet-lab experiments) using a probabilistic surrogate model and an acquisition rule. Common in design–build–test–learn loops.

**Bayesian uncertainty** [Statistics]: A way to represent uncertainty as a probability distribution over model parameters or predictions. Often approximated in deep learning using ensembles or variational methods to support risk-aware decisions. See also: **uncertainty quantification**.

**Benchmark** [Statistics]: A standardized dataset and evaluation protocol used to compare methods. Benchmarks help identify real progress but can also be gamed if models overfit to quirks of the benchmark data.

**Benefit–risk assessment** [Clinical]: Weighing expected therapeutic benefits against potential harms. Drug development and regulatory decisions often depend on benefit–risk trade-offs rather than accuracy metrics alone.

**Benjamini–Hochberg procedure** [Statistics]: A method to control the false discovery rate when testing many hypotheses. Common in omics evaluation when assessing thousands of genes, peaks, or variants.

**BERT-style model** [ML]: A transformer trained with masked language modeling, predicting masked tokens using both left and right context. Many DNA and protein foundation models use BERT-style objectives for representation learning.

**Bias–variance trade-off** [Statistics]: The tension between underfitting (high bias) and overfitting (high variance). Regularization, ensembling, and dataset size influence where a model sits on this trade-off.

**Bimodal distribution** [Statistics]: A distribution with two peaks, which in single-cell data can reflect mixtures of cell states or technical artifacts. Often motivates mixture models or careful gating/thresholding.

**Binarization** [Statistics]: Converting continuous values into 0/1 indicators, such as accessible vs inaccessible peaks in scATAC-seq. Can simplify models but risks losing quantitative information.

**Biobank** [Clinical]: A repository linking biological samples (often DNA) with phenotypes and longitudinal data. Biobanks enable discovery and validation but can introduce selection bias.

**Bioinformatics tokenization** [Genomics]: Rules for converting biological sequences (DNA/RNA/protein) into model inputs, such as characters, k-mers, or learned subwords. Choices affect model length, compute, and what biological patterns can be represented.

**Biomarker** [Clinical]: A measurable indicator of a biological state, such as a gene expression signature or protein marker. In multi-omic studies, biomarkers can combine modalities to improve diagnosis or prognosis.

**Biomarker qualification** [Clinical]: A regulatory-science process showing a biomarker is reliable for a specific context of use. Strong qualification can accelerate trials by enabling enrichment or surrogate endpoints.

**Biomarker stratification** [Clinical]: Dividing patients into subgroups based on biomarkers to predict response or risk. Supports precision medicine and can reduce sample sizes in trials.

**Bits per character (bpc)** [Statistics]: A likelihood-based metric (related to cross-entropy) that measures how well a model compresses or predicts sequences at the character/token level. Lower bpc indicates better predictive performance for the chosen tokenization.

**Blinded evaluation** [Statistics]: An evaluation setup where test labels are hidden to reduce overfitting to the benchmark and to discourage manual tuning on the test set. Encourages more trustworthy comparisons.

**Bootstrap** [Statistics]: A resampling method for estimating uncertainty (confidence intervals) of metrics by repeatedly sampling with replacement. Useful for reporting benchmark variability across finite test sets.

**Byte Pair Encoding (BPE)** [ML]: A data-driven tokenization method that iteratively merges frequent symbol pairs to form a subword vocabulary. Balances vocabulary size and sequence length; see also: **token**, **vocabulary**.

**Calibration curve (reliability diagram)** [Statistics]: A plot comparing predicted probabilities to empirical outcome rates in bins. Used to diagnose whether a model is overconfident or underconfident.

**Capture sequencing** [Genomics]: A targeted sequencing approach that enriches specific genomic regions (often the **exome** or gene panels) prior to sequencing. Reduces cost relative to **whole-genome sequencing** but misses off-target regions.

**Capture-C** [Genomics]: A targeted 3D genome assay that enriches contacts involving selected loci, providing higher resolution around regions of interest. Useful for enhancer–promoter mapping.

**Carrier screening** [Clinical]: Testing individuals for recessive disease variants to assess reproductive risk. Requires careful reporting and population-aware interpretation.

**Case–control study** [Statistics]: A study design comparing individuals with an outcome to those without to estimate associations. Common in genetic discovery and risk modeling but sensitive to selection bias.

**Causal attention mask** [ML]: A masking rule that prevents a token from attending to future tokens during training or inference. Ensures the model respects the directionality required for **auto-regressive modeling**.

**Causal effect** [Statistics]: The change in an outcome caused by an intervention or exposure, distinct from correlation. Translation often needs causal reasoning to choose targets and interventions.

**Causal graph** [Statistics]: A directed graph describing causal relationships between variables. Helps reason about confounding, selection bias, and what an evaluation split actually tests.

**Causal inference** [Statistics]: Methods for estimating causal effects from data, often using assumptions encoded in causal graphs. Helps avoid confounding when evaluating interventions or treatment effects.

**Cell atlas** [Genomics]: A reference map of cell types and states defined by molecular profiles, often single-cell transcriptomics and epigenomics. Atlases support annotation transfer and comparative studies.

**Cell cycle scoring** [Statistics]: Estimating a cell’s position in the cell cycle from expression of marker genes. Helps separate proliferative variation from cell-type biology in clustering and differential expression.

**Cell-type annotation** [Genomics]: Assigning biological labels to clusters or cells using marker genes, reference atlases, or classifiers. Accuracy is critical because downstream interpretations depend on these labels.

**Cell–cell communication (ligand–receptor analysis)** [Genomics]: Inference of signaling interactions between cell populations by combining ligand expression in sender cells with receptor expression in receiver cells. Often used to interpret tissue microenvironments.

**Censoring** [Statistics]: A survival analysis concept where the outcome time is only partially observed (e.g., patient lost to follow-up). Requires specialized metrics and models for time-to-event endpoints.

**Cherry-picking** [Statistics]: Selecting datasets, splits, or metrics that make a method look better while ignoring harder or contradictory evidence. A key risk in benchmark-driven papers.

**ChIA-PET (Chromatin Interaction Analysis by Paired-End Tag sequencing)** [Genomics]: A 3D genome assay that captures chromatin contacts mediated by a specific protein (e.g., CTCF) using ChIP enrichment. Provides protein-anchored interaction maps.

**ChIP-seq** [Genomics]: Chromatin immunoprecipitation followed by sequencing to map where DNA-binding proteins (e.g., transcription factors) or histone marks occur in the genome. A primary source of regulatory **annotations**.

**Chromatin conformation capture (3C)** [Genomics]: A family of assays that measure physical contacts between genomic regions via crosslinking, digestion, and ligation. Hi-C, Capture-C, and related methods are extensions of 3C.

**CITE-seq (Cellular Indexing of Transcriptomes and Epitopes by sequencing)** [Genomics]: A multi-modal single-cell assay that measures RNA and surface proteins using antibody-derived tags. Improves cell-type resolution when transcripts alone are ambiguous.

**Class token ([CLS])** [ML]: A special token prepended to an input sequence whose final representation is used as a summary for classification tasks. Common in BERT-style encoders; see also: **pooling**.

**Clinical decision threshold** [Clinical]: A score cutoff that triggers an action (e.g., confirmatory testing, reporting, or treatment). Thresholds depend on prevalence, costs of errors, and clinical context.

**Clinical grade model** [Clinical]: A model developed with controls, documentation, validation, and monitoring appropriate for patient care. Goes beyond research accuracy to include robustness, governance, and traceability.

**Clinical phenotype** [Clinical]: Observable characteristics (symptoms, signs, lab results) used to diagnose and manage disease. Accurate phenotyping is critical for rare disease gene discovery and matching.

**Clinical trial phase I** [Clinical]: First-in-human trials focused on safety, dosing, and pharmacokinetics. Models may aid dose selection and identify safety risks early.

**Clinical trial phase II** [Clinical]: Trials assessing efficacy signals and refining dose/regimen in target populations. Biomarker-based enrichment is often tested here.

**Clinical trial phase III** [Clinical]: Large confirmatory trials that test efficacy and safety for regulatory approval. Evidence standards are typically highest at this stage.

**CLS token** [ML]: A special token used by some transformer encoders whose final embedding is treated as a sequence-level summary. Often used for classification heads on DNA/protein sequences.

**Clustering (single-cell)** [ML]: Grouping cells by similarity in their molecular profiles to identify putative cell types or states. Common methods include graph-based clustering on nearest-neighbor graphs.

**Common variant** [Genomics]: A genetic variant with relatively high **allele frequency** in the population (definitions vary, often >1%). Common variants dominate standard **GWAS** discovery but usually have small individual effects.

**Companion diagnostic** [Clinical]: A test required or recommended to safely and effectively use a drug (e.g., selecting patients likely to respond). Creates strong incentives for high-quality predictive biomarkers.

**Compartment score** [Statistics]: A quantitative value (often derived from eigenvectors of the contact matrix) indicating whether a region belongs to A or B compartment. Used to compare chromatin organization across conditions.

**Compound heterozygous** [Genomics]: Having two different pathogenic variants in the same gene, one on each allele, causing a recessive disease. Often evaluated in rare disease trio analyses.

**Confidence interval (CI)** [Statistics]: A range of values that likely contains the true metric, reflecting uncertainty due to finite sample size. Helps prevent overinterpreting small benchmark differences.

**Confirmatory testing** [Clinical]: A follow-up test used to verify a finding, often using an orthogonal technology. Confirmatory steps reduce the risk of acting on false positives.

**Confounding by ancestry** [Clinical]: Systematic performance differences driven by population structure rather than true biology. Can cause inequitable variant classification and requires stratified evaluation and careful cohort design.

**Conservation score** [Genomics]: A numeric measure of evolutionary constraint at a genomic position inferred from multi-species alignments. High conservation suggests functional importance and is a key ingredient in **CADD**-style models. See also: **PhyloP**, **PhastCons**, **GERP**.

**Contact matrix** [Computation]: A matrix representation of Hi-C or Micro-C data where entries count contacts between genomic bins. Used for identifying compartments, domains, and loops.

**Contact probability decay** [Statistics]: The tendency for contact frequency to decrease as genomic distance increases. Deviations can indicate structural changes, compaction, or experimental artifacts.

**Context of use** [Clinical]: The specific setting, population, and decision where a model or biomarker is intended to be used. Translation and regulation depend on clearly defined context of use.

**Convolution** [Computation]: An operation that slides a kernel across an input and computes local weighted sums. In neural networks, it enables efficient pattern detection with shared parameters; see also: **convolutional neural network**.

**Corruption process** [ML]: A controlled way of perturbing inputs during self-supervised learning so the model can learn to reconstruct or predict missing information. Examples include masking tokens or adding noise; see also: **denoising**.

**Cost-effectiveness analysis** [Statistics]: A framework comparing interventions by cost per unit benefit (e.g., cost per QALY). Helps decide whether deploying a genomic model is worth it at scale.

**Counts matrix** [Computation]: A matrix of observed counts (genes × cells or peaks × cells) used as the starting point for most single-cell analyses. Usually sparse, noisy, and requires normalization.

**Credible set** [Statistics]: A set of variants from fine-mapping intended to contain the causal variant(s) with high probability (e.g., 95%). Used to narrow down **GWAS** signals for downstream functional follow-up.

**Cross-attention** [ML]: Attention where queries come from one sequence and keys/values from another, enabling information flow between modalities or between encoder and decoder. Used in encoder–decoder transformers; see also: **self-attention**.

**Cross-entropy loss** [Statistics]: A loss function that measures the negative log-likelihood of the true token or label under the model’s predicted distribution. Standard objective for training language models and many classifiers.

**Cross-validation** [Statistics]: A resampling evaluation method that rotates training/validation splits to estimate generalization. Useful when datasets are small, but must respect grouping (e.g., by gene, patient, or locus).

**Data audit** [Computation]: A structured check of dataset provenance, duplicates, label quality, and split integrity. Essential for trustworthy benchmarks in genomics and clinical ML.

**Data integration** [ML]: Combining datasets across batches, modalities, or studies into a shared representation. Integration is central to building coherent atlases and multi-omic models.

**Data sheet (dataset documentation)** [Computation]: A standardized description of a dataset’s motivation, collection process, labels, intended uses, and limitations. Improves transparency and reduces hidden confounding.

**Data-constrained regime** [ML]: A setting where the amount or diversity of training data limits performance more than model capacity. Common in genomics when labeled functional data are scarce.

**De novo variant** [Genomics]: A variant present in a child but absent in both parents, arising spontaneously. De novo variants are a major signal in rare disease and developmental disorders.

**Decision curve analysis** [Statistics]: A method that evaluates clinical utility by combining true/false positives with a range of risk thresholds. Helps translate model performance into net benefit.

**DeepVariant** [ML]: A deep learning-based variant caller that reframes variant calling as an image-like classification problem over read pileups. Often improves accuracy over classical pipelines, especially in challenging regions.

**Demographic parity** [Statistics]: A fairness criterion requiring equal positive prediction rates across groups. Often inappropriate in medicine when base rates differ, but useful as a diagnostic.

**Denoising objective** [ML]: A self-supervised training objective where the model reconstructs clean data from corrupted input. Encourages robust representations; see also: **masked language modeling**.

**Depthwise separable convolution** [ML]: A factorized convolution that splits spatial (depthwise) and channel-mixing (pointwise) operations to reduce computation. Useful for efficient sequence models; see also: **pointwise convolution**.

**Design–Build–Test–Learn (DBTL)** [Computation]: An iterative cycle for engineering biological systems: propose designs, build them, test experimentally, and update models. Foundation models can accelerate the design and learn steps.

**Differential accessibility** [Statistics]: Testing whether chromatin accessibility differs between cell groups or conditions, typically using peak counts. Helps identify regulatory elements driving cell-state differences.

**Differential privacy** [Computation]: A privacy framework that limits what can be inferred about any individual from released results. Useful for sharing model outputs or training on sensitive clinical data.

**Diploid** [Genomics]: Having two copies of each chromosome (and thus typically two alleles at each locus). Human autosomes are diploid, which affects genotype representation in **VCF** files.

**Dispersion** [Statistics]: A parameter describing variability beyond the mean in count models such as the negative binomial. Accurate dispersion modeling is key for valid differential expression.

**Domain tag** [Computation]: A bracketed label like [ML] or [Genomics] used in this glossary to indicate the primary domain of a term. Helps readers from different backgrounds quickly orient.

**Dot-product attention** [ML]: An attention mechanism that scores query–key similarity via a dot product. Efficient and widely used; see also: **scaled dot-product attention**.

**Droplet-based single-cell sequencing** [Genomics]: A class of assays that encapsulate individual cells in droplets with barcoded beads to capture RNA (and sometimes other modalities). Enables profiling of thousands to millions of cells.

**Dropout** [ML]: A regularization technique that randomly zeroes activations during training to reduce overfitting. When used at inference (MC dropout), it can approximate predictive uncertainty. See also: **uncertainty quantification**.

**Drug repurposing** [Clinical]: Finding new indications for existing drugs, leveraging known safety profiles. Computational methods often prioritize repurposing candidates via knowledge graphs and transcriptomic signatures.

**E-value** [Statistics]: A measure used in sequence alignment or motif scanning representing how many hits of similar score are expected by chance. Lower values indicate more significant matches; see also: **motif**.

**Early stopping** [ML]: Stopping training when validation performance stops improving to reduce overfitting. Needs careful split design to avoid tuning on leaked signals.

**Effect size** [Statistics]: A measure of practical magnitude (not just statistical significance), such as log-fold change or Cohen’s d. Effect sizes help interpret biological and clinical relevance.

**Eigenvector decomposition** [Computation]: A linear algebra operation used on contact matrices to derive compartment structure (A/B). Often the first principal eigenvector correlates with active vs inactive chromatin.

**Embedding dimension** [ML]: The size of an embedding vector (number of features) used to represent each token. Larger dimensions can encode richer information but increase compute and risk overfitting.

**Embedding pooling** [ML]: A method to aggregate token-level embeddings into a fixed-length vector (e.g., mean pooling, max pooling, attention pooling). Used to make sequence-level predictions from DNA/protein models.

**Emergent capability** [ML]: A qualitative jump in behavior that appears as models scale, such as improved long-range reasoning or better transfer to new tasks. In genomics, may show up as stronger zero-shot variant scoring or motif discovery.

**Encoder** [ML]: A model component that maps an input sequence to contextual representations, typically using self-attention or convolutions. In transformers, encoder outputs can be consumed by a decoder or task head.

**Encoder–decoder** [ML]: A two-part architecture where an encoder builds representations of the input and a decoder generates outputs, often using cross-attention. Common in translation and sequence-to-sequence tasks; see also: **cross-attention**.

**Endpoint** [Clinical]: A predefined outcome used to evaluate an intervention, such as survival, hospitalization, or biomarker change. Choice of endpoint determines what evidence a model must support.

**Enhancer grammar** [Genomics]: The idea that regulatory function depends on the composition, spacing, and orientation of motifs within an enhancer, not just the presence of individual motifs. Foundation models can sometimes learn aspects of this grammar from sequence data.

**Enrichment strategy** [Clinical]: Selecting trial participants more likely to have the event or respond to treatment, improving power and reducing costs. Biomarkers and genetic risk can support enrichment.

**Ensemble** [ML]: A set of models whose predictions are combined (e.g., averaged) to improve accuracy and robustness. Ensembles are also widely used to estimate predictive uncertainty. See also: **Bayesian uncertainty**.

**Epigenome** [Genomics]: The collection of chemical marks and chromatin states that influence gene regulation without changing DNA sequence. Multi-modal foundation models may integrate epigenomic tracks with sequence.

**Epigenomic track** [Genomics]: A genome-wide signal vector from an assay such as ATAC-seq or ChIP-seq. Used as model outputs or conditioning inputs in sequence-to-function and multi-modal models.

**Evolutionary conservation** [Genomics]: The tendency for important sequence positions to remain similar across species due to purifying selection. Many protein and variant models use conservation as a strong prior or training signal.

**Fairness evaluation** [Statistics]: Assessing whether model performance and errors differ across groups (ancestry, sex, age, site). Includes both metric stratification and consideration of downstream harms.

**False discovery rate (FDR)** [Statistics]: The expected proportion of false positives among discoveries declared significant. Commonly controlled in omics using procedures like Benjamini–Hochberg.

**Feature leakage** [Statistics]: A form of data leakage where inputs directly encode the label (e.g., post-treatment variables predicting outcome). Produces high accuracy with little causal value.

**Feature selection** [ML]: Choosing a subset of informative genes/peaks (e.g., highly variable genes) for downstream modeling. Reduces noise and compute but can bias analyses if done poorly.

**Federated evaluation** [Computation]: Evaluating models across multiple sites without centralizing raw data, often for privacy reasons. Can reveal site-specific failure modes while respecting governance.

**Federated learning** [Computation]: Training models across institutions without sharing raw data by aggregating model updates. Useful for clinical genomics where data sharing is constrained by privacy and governance.

**Fine-mapping** [Statistics]: A set of methods that attempt to localize causal variants within a **GWAS** locus by modeling **linkage disequilibrium** and association signals jointly. Outputs often include **credible sets** and **PIP** values.

**FlashAttention** [Computation]: An optimized attention algorithm that reduces memory overhead by computing attention in tiled blocks, enabling longer contexts and faster training/inference on GPUs. Particularly impactful for large transformers.

**Functional assay** [Genomics]: An experimental test measuring the molecular effect of a variant (e.g., reporter assays, splicing assays). Provides strong evidence for or against pathogenicity when well validated.

**Gene activity score** [Genomics]: An estimate of gene-level regulatory activity derived from ATAC peaks around a gene. Used to relate scATAC-seq data to expression-like features for integration.

**Genetic heterogeneity** [Genomics]: A condition where similar phenotypes arise from different genes or mechanisms. Common in rare disease and complicates diagnostic and predictive modeling.

**Genome binning** [Computation]: Partitioning the genome into fixed-size bins (e.g., 10 kb) for contact matrices or coverage tracks. Trade-off between resolution and sparsity/noise.

**Genome context** [Genomics]: The local and distal genomic environment around a position, including nearby motifs, chromatin state, and 3D contacts. Longer-context models aim to incorporate more genome context directly.

**Genome-wide pretraining corpus** [Genomics]: A large collection of sequences used to train DNA language models, typically including reference genomes and sometimes multiple species. Corpus composition strongly affects what the model learns.

**Genome-wide significance** [Statistics]: A stringent p-value threshold used in GWAS to control false positives across the genome (often around 5×10⁻⁸). Thresholds can vary with study design and variant set.

**Genotype** [Genomics]: The allele combination an individual carries at a locus (e.g., 0/0, 0/1, 1/1 for diploid biallelic variants). Genotypes are commonly represented in **VCF** files with accompanying quality metrics.

**Global average pooling** [ML]: A pooling operation that averages features across positions, producing a fixed-length vector regardless of sequence length. Often used as a lightweight alternative to a class token; see also: **pooling**.

**gnomAD** [Genomics]: A large population reference database of human genetic variation and allele frequencies. Commonly used to filter variants by population frequency and to provide evidence against pathogenicity for very common alleles.

**Gold standard** [Statistics]: A reference label assumed to be correct, such as expert-curated variant classifications. True gold standards are rare; label noise and disagreements must be acknowledged.

**Gradient checkpointing** [Computation]: A memory-saving technique that recomputes intermediate activations during backpropagation instead of storing them. Enables training longer-context genomic transformers on limited hardware.

**Gradient clipping** [ML]: A training stabilization technique that caps gradient norms or values to prevent exploding gradients. Common in training deep networks and transformers.

**Graph** [Computation]: A structure of nodes and edges used to represent relationships such as gene regulation, protein interactions, or cell neighborhoods. Provides a common language for networks and GNNs.

**Graph embedding** [ML]: A vector representation of nodes or whole graphs that preserves network structure. Enables downstream tasks like clustering, link prediction, or similarity search in networks.

**Ground truth** [Statistics]: A reference set of labels assumed to be correct for evaluation (e.g., high-confidence variant calls from **GIAB**). Ground truth is often imperfect; understanding its limitations is key to trustworthy benchmarking.

**Haplotype** [Genomics]: A set of variants inherited together on the same chromosome segment. Haplotype-aware modeling matters when multiple variants interact or when phasing changes functional impact.

**Haplotype phasing (Phasing)** [Computation]: The process of determining which alleles occur together on the same chromosome copy. Improves **imputation**, enables haplotype-based analyses, and helps interpret compound heterozygosity in rare disease settings.

**Harmony** [ML]: A popular batch correction and integration method that aligns embeddings across datasets while preserving biological structure. Often used in single-cell workflows for multi-dataset analysis.

**Heterogeneity** [Statistics]: Meaningful variation across patients, tissues, ancestries, or labs. Models must generalize across heterogeneity; evaluations should report stratified performance.

**Heterogeneous graph** [Computation]: A graph with multiple node or edge types (e.g., genes, proteins, phenotypes). Useful for knowledge graphs and multi-relational biological networks.

**Hidden state** [ML]: An internal vector representation at a specific layer and position in a network. Hidden states evolve through layers to become task-relevant features; see also: **representation**.

**Hit** [Clinical]: A compound showing desired activity in an initial screen. Hits are starting points; they require confirmation and optimization to become leads.

**Hyperparameter tuning** [ML]: Selecting settings like learning rate, regularization, or architecture details using validation data. Must be done without peeking at test sets to avoid optimistic bias.

**Imputation** [Statistics]: A method for inferring unobserved genotypes by leveraging **linkage disequilibrium** patterns from reference panels. Widely used in biobank-scale **GWAS** to increase variant density.

**In-context learning** [ML]: A model’s ability to adapt behavior from examples provided in the input prompt, without updating parameters. More common in text LLMs, but the concept informs prompt-like interfaces for biological models.

**Index variant** [Statistics]: The most strongly associated variant at a GWAS locus (often the lowest p-value), used as a starting point for locus definition. The index variant may not be causal due to **linkage disequilibrium**.

**Indication** [Clinical]: The disease or condition a drug or intervention is intended to treat. Indication affects trial endpoints, regulatory standards, and target populations.

**Inductive bias** [ML]: Built-in assumptions in a model architecture or training setup that make certain patterns easier to learn. CNN locality and translation equivariance are classic inductive biases; see also: **receptive field**.

**InfoNCE loss** [Statistics]: A contrastive objective that treats matching pairs as positives and other samples as negatives within a batch, encouraging separable representations. Common in contrastive self-supervised learning; see also: **contrastive learning**.

**Insulation score** [Statistics]: A metric computed from contact matrices to quantify how strongly a locus acts as a boundary between domains. Low insulation often marks TAD boundaries.

**Insulator** [Genomics]: A regulatory element that blocks enhancer–promoter communication or demarcates chromatin domains, often involving CTCF and cohesin. Important for interpreting long-range regulatory effects.

**Interactome** [Genomics]: The complete set of molecular interactions in a cell, including protein–protein and regulatory interactions. Interactomes provide scaffolds for network-based modeling.

**Intersectional evaluation** [Statistics]: Assessing performance across combinations of groups (e.g., ancestry × sex) to detect hidden disparities. Important when single-axis fairness checks miss worst-case subgroups.

**Isoform** [Genomics]: A specific RNA transcript produced from a gene, differing by splicing or transcription start/end. Isoform-level analysis can reveal regulatory mechanisms missed at gene level.

**Isotonic regression** [Statistics]: A non-parametric calibration method that fits a monotonic mapping from scores to probabilities. Useful when calibration curves show systematic bias. See also: **Platt scaling**.

**Joint embedding** [ML]: A shared latent space where multiple modalities or batches are represented together. Enables integrated clustering, visualization, and prediction across data sources.

**K-mer** [Genomics]: A length-k substring of a sequence (e.g., 6-mer). Many genomic models tokenize DNA into k-mers to reduce sequence length and capture local context. See also: **tokenization**.

**Knowledge graph** [Computation]: A graph that encodes entities and typed relationships, often integrating curated biology (genes–diseases–drugs). Supports reasoning, link prediction, and retrieval for models.

**Latent space** [ML]: A lower-dimensional representation learned by a model (e.g., PCA or VAE) intended to capture essential structure. Used for integration, clustering, and trajectory inference.

**Lead optimization** [Clinical]: Iterative chemical modifications to improve a lead’s potency, selectivity, and ADMET. ML can propose modifications and prioritize experiments.

**Learning curve** [Statistics]: A plot of performance versus training set size (or compute). Helps estimate whether collecting more data or changing the model is likely to improve results.

**Leiden algorithm** [Computation]: A community detection method used for clustering graphs, often applied to kNN graphs in single-cell analysis. Tends to produce well-connected clusters and is widely used in Scanpy/Seurat workflows.

**Ligand** [Genomics]: A signaling molecule (often a protein) secreted or displayed by cells that binds a receptor on another cell to trigger a response. Ligand expression helps infer intercellular communication.

**Likelihood ratio** [Statistics]: A ratio comparing how well two hypotheses explain data, often used for evidence weighting. In variant interpretation, likelihood ratios can align model outputs with evidence frameworks.

**Linear attention** [Computation]: A family of attention approximations that reduce the quadratic cost in sequence length to near-linear time. Enables long-context genomic transformers, though with potential trade-offs in fidelity.

**Linear probing** [ML]: A transfer-learning evaluation where the base model is frozen and only a simple classifier is trained on top of its representations. Measures representation quality; see also: **fine-tuning**.

**Link prediction** [ML]: A task in graph learning where the model predicts missing or future edges. Used to infer novel protein interactions, regulatory links, or gene–disease associations.

**Local receptive field** [ML]: The subset of input positions that can influence a neuron’s output. In CNNs, receptive fields grow with depth and dilation; see also: **dilation**.

**Locus** [Genomics]: A specific genomic region or coordinate (singular of loci). Often used to refer to a GWAS-associated region containing multiple correlated variants.

**Log-normalization** [Statistics]: A common single-cell preprocessing step that scales counts by library size and applies a log transform (often log1p). Stabilizes variance and makes distances more meaningful for clustering.

**Loss to follow-up** [Statistics]: When outcomes are not observed because participants drop out or data are missing. Can bias evaluations unless handled with censoring-aware methods.

**Louvain algorithm** [Computation]: A graph community detection method historically popular for single-cell clustering. Often replaced by Leiden due to improved guarantees, but still conceptually important.

**Manhattan plot** [Statistics]: A GWAS visualization plotting −log10(p-value) across genomic position, producing “skyscrapers” at associated loci. Useful for quickly assessing signal distribution and potential artifacts.

**Masking strategy** [ML]: Rules for which tokens/positions to hide or corrupt during training. In genomics, strategies can be biologically motivated (e.g., masking motifs or regulatory segments) to encourage meaningful learning.

**Matrix factorization** [ML]: Decomposing a matrix into low-rank factors (e.g., NMF) to learn latent programs. Used for topic-like interpretations of gene programs and some multi-omic integration methods.

**Matrix multiplication** [Computation]: A core linear algebra operation underlying most neural network layers, especially attention and dense layers. Efficient implementations strongly affect training speed; see also: **FlashAttention**.

**MERFISH** [Genomics]: A spatial transcriptomics method that uses multiplexed FISH to measure many RNAs in situ with spatial coordinates. Preserves tissue context and cell neighborhood structure.

**Message passing** [ML]: The core operation in many GNNs where each node updates its representation by aggregating information from neighbors. Enables local-to-global reasoning on biological graphs.

**Meta-analysis** [Statistics]: A framework that combines results across studies to estimate overall effects while accounting for heterogeneity. Useful when evaluating models across multiple cohorts.

**Metric gaming** [Statistics]: Optimizing a reported metric in ways that do not improve real-world utility, often by exploiting quirks of the benchmark. Mitigated by diverse metrics and robust evaluation.

**Micro-C** [Genomics]: A high-resolution 3D genome assay similar to Hi-C but using micrococcal nuclease digestion. Can reveal finer-scale chromatin contacts and nucleosome-level structure.

**Misdiagnosis** [Clinical]: An incorrect diagnosis, common in rare disease due to overlapping phenotypes and limited expertise. Genomic models aim to reduce diagnostic odysseys and misdiagnoses.

**Modality** [Genomics]: A type of measurement, such as RNA expression, chromatin accessibility, protein abundance, or methylation. Multi-omic modeling integrates multiple modalities to capture biology more completely.

**Model card** [Computation]: A standardized document describing a model’s intended use, training data, evaluation, limitations, and ethical considerations. Supports responsible deployment.

**Model head** [ML]: A task-specific module attached to a base model (e.g., classifier, regressor, or decoder). Heads are often small and can be trained with frozen backbones; see also: **linear probing**.

**Model scaling** [ML]: Increasing model size, data size, and/or training compute to improve performance following empirical trends. Scaling is central to the foundation model paradigm. See also: **scaling laws**.

**Molecular docking** [Computation]: A computational method that predicts how a small molecule binds to a protein binding site. Used in virtual screening and structure-based drug design.

**Molecular dynamics (MD)** [Computation]: Simulation of molecular motion over time to study stability and interactions. Can refine docking hypotheses and assess binding modes, though it is computationally expensive.

**Motif activity inference** [Genomics]: Estimating transcription factor activity from accessibility patterns at motif instances, often using chromVAR-like approaches. Links scATAC-seq peaks to regulatory programs.

**Multi-head attention** [ML]: An attention mechanism that runs several attention ‘heads’ in parallel, each learning different interaction patterns, then combines them. Improves expressiveness and stability; see also: **self-attention**.

**Multi-omic model** [ML]: A model that integrates multiple biological modalities (e.g., DNA, chromatin accessibility, expression, methylation). Can improve generalization by using complementary signals. See also: **epigenome**.

**Multi-omics integration** [ML]: Combining multiple omics modalities into a coherent model or representation. Helps connect regulatory state, expression, and phenotype and can improve robustness under missing data.

**Multiallelic variant** [Genomics]: A variant site with more than two alleles observed in the population (e.g., A/C/T). Multiallelic sites can complicate **variant calling**, annotation, and score construction.

**Multimodal patient representation** [ML]: A learned embedding that combines different data types (EHR, imaging, genomics, labs). Supports more accurate risk prediction and cohort stratification.

**Multiple testing correction** [Statistics]: Adjustments to control false positives when running many statistical tests, as in GWAS. Genome-wide significance thresholds reflect the large number of variants tested.

**Nearest-neighbor graph (kNN graph)** [Computation]: A graph connecting each cell to its k most similar neighbors in an embedding space. Forms the backbone for graph-based clustering and UMAP.

**Negative binomial model** [Statistics]: A count distribution that accommodates overdispersion relative to Poisson. Widely used for RNA-seq and single-cell differential expression because counts are noisy and variable.

**Negative control** [Statistics]: A test designed to detect confounding or leakage by checking that a model does not predict an outcome when it should not. Helps validate benchmark integrity.

**Network centrality** [Statistics]: Measures of node importance in a graph (degree, betweenness, PageRank). Used to identify hub genes or key regulators in interaction networks.

**Next-token prediction** [ML]: A training objective for autoregressive models where the model predicts the next token in a sequence. Used for sequence generation and likelihood scoring.

**Off-target effect** [Clinical]: An unintended interaction of a drug with a non-target molecule, potentially causing side effects. Also used in genome editing to describe edits at unintended loci.

**One-hot encoding** [ML]: A representation that maps a categorical symbol to a binary vector with a single 1 (e.g., A/C/G/T). Common for CNN genomics inputs; see also: **channel**.

**Optimization** [ML]: The process of adjusting model parameters to minimize a loss function, typically using gradient-based methods like SGD or Adam. Training stability often depends on learning-rate schedules, normalization, and batch size.

**Orphan drug** [Clinical]: A drug developed for a rare disease, often eligible for regulatory incentives. Rare disease drug programs benefit from precise patient identification and biomarkers.

**Ortholog** [Genomics]: A gene in a different species that descended from a common ancestral gene via speciation. Orthologs are commonly used in comparative genomics and conservation analyses.

**Overfitting** [ML]: When a model learns patterns specific to the training data that do not generalize. Benchmark overfitting can occur via repeated public leaderboard tuning.

**Overfitting** [Statistics]: When a model fits training data too closely and performs poorly on new data. Mitigated by regularization, more data, or better inductive bias; see also: **dropout**.

**p-value** [Statistics]: The probability, under a null hypothesis, of observing an association statistic at least as extreme as the one measured. In GWAS, very small p-values can reflect true associations or artifacts if confounding remains.

**Panel sequencing** [Genomics]: Targeted sequencing of a curated set of genes or regions relevant to a disease area. Enables very high depth but provides limited genome-wide context.

**Pareto frontier** [Statistics]: A set of solutions where improving one objective (e.g., accuracy) would worsen another (e.g., compute, latency, fairness). Useful for selecting models under real constraints.

**Pathway enrichment** [Statistics]: Testing whether a set of genes in a pathway is overrepresented among hits or DE genes. Used to interpret omics signatures and support target identification.

**PCA (principal component analysis)** [Statistics]: A linear dimensionality reduction method that projects data onto directions of maximal variance. Often used as a first step before building kNN graphs for single-cell analysis.

**Peak calling** [Computation]: Algorithms that identify enriched genomic regions (peaks) from sequencing reads. In single-cell workflows, peaks may be called per dataset or aggregated across cells.

**Penetrance** [Clinical]: The probability that a person with a pathogenic genotype expresses the phenotype. Incomplete penetrance complicates risk prediction and counseling.

**Perplexity** [Statistics]: A transformed measure of average negative log-likelihood for language models. Lower perplexity indicates better sequence prediction for the chosen tokenization and corpus.

**Phase II/III adaptive trial** [Clinical]: A trial design that modifies allocation or sample size based on interim results under pre-specified rules. Can reduce costs but requires careful statistical control.

**PhastCons** [Genomics]: A conservation score that estimates the probability a base lies in a conserved element using a hidden Markov model over multi-species alignments. Often used as an input **annotation** feature.

**Phenotype matching** [Clinical]: Comparing a patient’s phenotypes to known disease profiles to prioritize genes and diagnoses. Often uses HPO terms and similarity scoring.

**PhyloP** [Genomics]: A conservation/acceleration score that measures deviation from neutral evolution at single-nucleotide resolution. High positive values indicate constraint; negative values indicate faster-than-neutral evolution.

**PolyPhen-2** [Genomics]: A missense variant predictor that combines sequence and structural features to classify amino acid substitutions as benign or damaging. Commonly compared against integrated scores like **CADD**.

**Pooling** [ML]: An operation that aggregates information across positions (e.g., max, average, attention pooling) to create a fixed-size representation. Useful for classification on variable-length sequences.

**Population stratification** [Statistics]: Confounding in association studies caused by ancestry-related differences in allele frequencies correlated with the trait. Mitigated with covariates like **genetic PCs**, careful study design, and replication.

**Positional encoding** [ML]: A way to inject token order information into transformer models, since self-attention alone is permutation-invariant. Can be learned embeddings, sinusoidal functions, or attention biases; see also: **AliBi**.

**Post hoc explanation** [ML]: An explanatory method applied after training, such as saliency maps or SHAP. Can be informative but may not faithfully reflect the model’s internal reasoning.

**Pre-registration** [Statistics]: Documenting analysis plans and evaluation protocols before seeing results. Reduces p-hacking and benchmark overfitting, improving credibility.

**Precision** [Statistics]: The proportion of predicted positives that are true positives. Highly sensitive to base rate, making it crucial to report prevalence and use-case context.

**Precision medicine** [Clinical]: Tailoring prevention and treatment based on individual variability in genes, environment, and lifestyle. Genomic foundation models support precision medicine by improving interpretation and targeting.

**Precision–recall curve** [Statistics]: A plot of precision versus recall across thresholds, especially informative for rare positives. Often preferred over ROC curves in imbalanced genomics tasks.

**Preclinical model** [Clinical]: Non-human or in vitro systems (cell lines, organoids, animals) used to test drug hypotheses before human trials. Predictive validity varies by disease and mechanism.

**Predictive biomarker** [Clinical]: A biomarker that predicts response to a specific therapy. Often used to select patients and design enriched trials.

**Pretraining** [ML]: Training a model on a large, generic dataset with a self-supervised objective to learn transferable representations. Often followed by fine-tuning on task-specific data; see also: **fine-tuning**.

**Probability calibration** [Statistics]: Transforming model outputs so that predicted probabilities align with observed frequencies. Necessary when probabilities are used for decisions, not just ranking.

**Prompt tuning** [ML]: A PEFT approach that learns a small set of continuous ‘soft prompt’ vectors prepended to inputs while freezing the base model. Adapts behavior with minimal parameters; see also: **PEFT**.

**Prompting** [ML]: A way to steer a pre-trained model’s behavior by providing instructions and examples as input text (or tokens) instead of updating weights. Central to in-context learning; see also: **ICL**.

**Proper scoring rule** [Statistics]: A metric that is optimized when predicted probabilities match true outcome probabilities (e.g., log loss, Brier score). Encourages honest uncertainty estimates.

**Protein residue** [Genomics]: An amino acid at a specific position in a protein sequence. Many mutation effect scores are residue-level predictions.

**Proxy label** [Statistics]: A label that is easier to measure than the true target (e.g., billing codes for disease). Proxy labels can introduce confounding and limit clinical validity.

**Pseudo-likelihood** [Statistics]: An approximation to full sequence likelihood obtained by conditioning on partial context (e.g., masking one position at a time). Used to score sequences in masked language models.

**Pseudobulk** [Statistics]: Aggregating single-cell counts within groups (e.g., cell type × donor) to create bulk-like profiles. Often improves DE robustness and enables well-understood bulk RNA-seq methods.

**Pseudotime** [Statistics]: An inferred ordering of cells along a biological progression such as differentiation. Used in trajectory analysis to study dynamic gene programs.

**Purifying selection** [Genomics]: Evolutionary pressure that removes deleterious variants from a population, leading to conservation at important positions. Central to many variant effect signals.

**QQ plot** [Statistics]: A plot comparing observed to expected p-value distributions for association tests. Helps identify systematic inflation/deflation and assess whether signals exceed null expectations.

**Randomization** [Statistics]: Assigning interventions or splits randomly to reduce confounding. In evaluation, randomization helps ensure fair comparisons and prevents systematic leakage.

**Rare disease diagnostic odyssey** [Clinical]: The long period many patients spend seeking a correct diagnosis. Genomic sequencing and phenotype-driven prioritization aim to shorten this odyssey.

**Read** [Genomics]: A short DNA sequence produced by a sequencing instrument representing a fragment of the original genome. Reads carry base quality information and must be processed through **alignment** and QC.

**Read pileup** [Computation]: The stack of aligned reads overlapping a genomic position. Many variant callers—classical and deep learning—use pileups to infer genotype and assess evidence for variants. See also: **DeepVariant**.

**Reading frame** [Genomics]: The grouping of nucleotides into codons for translation into protein. Frame disruptions (e.g., frameshifts) typically have large functional consequences.

**Recall (sensitivity)** [Statistics]: The proportion of true positives correctly identified. In clinical contexts, high recall may be prioritized when missing positives is costly.

**Receptive field** [ML]: The span of input positions that can affect a model’s output at a given layer/position. CNN receptive fields grow with depth and dilation; transformers can attend globally in one layer.

**Receptor** [Genomics]: A molecule (often a membrane protein) that binds a ligand to initiate signaling. Receptor expression is used alongside ligands to infer cell–cell communication.

**Recombination** [Genomics]: A meiotic process that shuffles genetic material between homologous chromosomes, breaking down **linkage disequilibrium** over generations. Shapes haplotype blocks and fine-mapping resolution.

**Reference genome** [Genomics]: A standardized genome assembly used as the coordinate system for alignment and annotation (e.g., GRCh38). Choice of reference affects mapping, variant representation, and comparability across studies.

**Registry** [Clinical]: An organized system collecting data about patients with a disease or exposure. Registries are key for rare disease natural history studies and external validation.

**Regulatory element** [Genomics]: A DNA region (e.g., enhancer or promoter) that influences gene expression. Many disease-associated variants lie in regulatory elements identified through resources like **ENCODE**.

**Regulatory variant** [Genomics]: A variant that affects gene regulation rather than protein coding sequence, often by altering transcription factor binding or chromatin state. Regulatory FMs aim to predict these effects from sequence context.

**Regulon** [Genomics]: A set of genes regulated by a common transcription factor. Regulon activity scoring can summarize regulatory programs across cells.

**Relative positional encoding** [ML]: A positional method that represents relationships between tokens (distance or offsets) rather than absolute positions. Often improves length generalization; see also: **positional encoding**.

**Representation** [ML]: An internal feature encoding learned by a model that captures relevant structure in the input. Good representations transfer well across tasks; see also: **pretraining**.

**Reproducibility** [Computation]: The ability to obtain the same results when repeating an experiment with the same data and code. Requires versioning, fixed seeds, and well-documented pipelines.

**Reproducible pipeline** [Computation]: A workflow with versioned code, data provenance, and deterministic settings where possible. Required for clinical-grade audits and for re-running analyses during updates.

**Return of results** [Clinical]: The process of reporting findings to patients and clinicians, including incidental findings and uncertainties. Requires careful communication and policies for updates.

**Reverse complement** [Genomics]: The DNA sequence obtained by reversing a sequence and swapping each base for its complement (A↔T, C↔G). Many genomic tasks are strand-invariant, so models often use this symmetry in training; see also: **augmentation**.

**RNA velocity** [Statistics]: A method that uses spliced and unspliced RNA counts to infer the direction and speed of cell-state transitions. Adds dynamical information beyond static pseudotime.

**RNA-seq** [Genomics]: Sequencing-based measurement of RNA abundance, typically capturing mRNA expression across genes. Provides the primary signal for transcriptome profiling and many downstream analyses.

**Roadmap Epigenomics** [Genomics]: A consortium resource providing reference epigenomic maps (e.g., histone marks, methylation) across many tissues and cell types. Complements **ENCODE** for regulatory annotation.

**Robustness** [Statistics]: Stability of performance under perturbations such as noise, missing modalities, new sites, or different preprocessing. Robustness testing is essential for real-world trust.

**Sample-level QC** [Computation]: Quality checks applied to individuals (samples), such as missingness rate, heterozygosity outliers, sex mismatch, and relatedness. Prevents technical artifacts from contaminating GWAS and biobank analyses.

**Scaled dot-product attention** [ML]: Dot-product attention with scores scaled by the inverse square root of key dimension to stabilize gradients. The standard attention used in transformers; see also: **multi-head attention**.

**Selection bias** [Statistics]: Bias introduced when the training or evaluation sample differs from the target population, such as sequenced patients being sicker than the general population. Can distort both performance and fairness.

**Self-attention** [ML]: An operation where each token computes weighted combinations of other tokens in the same sequence, enabling context-dependent representations. Allows modeling of long-range dependencies; see also: **QKV**.

**Self-supervised learning** [ML]: Training where the supervision signal is derived from the data itself (e.g., masking tokens, predicting next tokens) rather than manual labels. Enables large-scale pretraining that transfers to downstream tasks; see also: **pretraining**.

**Sensitivity analysis** [Statistics]: A set of checks that vary assumptions (splits, thresholds, preprocessing) to see whether conclusions hold. Helps avoid brittle claims based on one protocol.

**seqFISH** [Genomics]: A spatial transcriptomics method using sequential rounds of FISH to measure many RNAs in place. Provides subcellular spatial information and preserves tissue architecture.

**Sequence read archive (SRA)** [Computation]: A public repository for raw sequencing data. Provides access to FASTQ-like read data for reproducibility and secondary analyses.

**Seurat** [Computation]: A widely used R toolkit for single-cell analysis that provides workflows for normalization, integration, clustering, and visualization. Frequently referenced alongside Scanpy/AnnData.

**Shared latent factors** [Statistics]: Latent variables that capture variation common across modalities or datasets in multi-omic models (e.g., MOFA). Useful for understanding cross-modal biology.

**Signal detection** [Statistics]: Methods to identify safety or efficacy signals in noisy real-world data, such as pharmacovigilance algorithms. Used in post-market surveillance and ADR monitoring.

**Signal-to-noise ratio** [Statistics]: A measure comparing the size of biological signal to technical noise. Low signal-to-noise in single-cell assays motivates careful QC, normalization, and integration.

**Silencer** [Genomics]: A regulatory element that decreases transcription when active, often via repressive factors. Silencers are harder to characterize than enhancers and benefit from multi-modal modeling.

**Single-cell multi-omics** [Genomics]: Technologies that measure multiple modalities at single-cell resolution (RNA, ATAC, protein, methylation). Provide richer views of cell state but increase integration complexity.

**Single-nucleus sequencing** [Genomics]: Profiling RNA or chromatin from isolated nuclei rather than whole cells, often used for frozen tissues. Can differ from whole-cell profiles and introduces nucleus-specific biases.

**Single-sequence embedding** [ML]: An embedding derived from a single protein or DNA sequence without explicit alignment information. Contrasts with MSA-based representations that include evolutionary context.

**Site effect** [Statistics]: Performance differences driven by where data were collected (hospital, lab, country). Site effects can reflect protocol differences and are a major source of shift.

**Softmax** [ML]: A function that converts a vector of scores into a probability distribution that sums to 1. Used to turn attention scores into weights and logits into class probabilities.

**Sparse matrix** [Computation]: A matrix where most entries are zero, stored efficiently by recording only non-zero values. Single-cell count matrices are typically sparse, enabling scalable computation.

**Spatial locality** [ML]: The assumption that nearby positions are more strongly related than distant ones. CNNs encode this inductive bias naturally; in genomics, locality reflects motifs and nearby regulatory interactions.

**Spatial transcriptomics** [Genomics]: Methods that measure gene expression while preserving spatial location in tissue sections. Enables mapping of cell types, niches, and gradients in situ.

**Splice junction** [Genomics]: The boundary between exons after introns are removed during splicing. Junction reads provide evidence for isoforms and splicing changes.

**Spliced / unspliced counts** [Genomics]: Counts of mature (spliced) and nascent (unspliced) RNA molecules derived from scRNA-seq reads. Used by RNA velocity to infer dynamics.

**Spurious correlation** [Statistics]: A correlation that arises from confounding or leakage rather than causal relationships. Benchmark design aims to minimize spurious correlations.

**Statistical power** [Statistics]: The probability of detecting a true effect given sample size and noise. Underpowered benchmarks can make model comparisons unstable and non-reproducible.

**Stratified split** [Statistics]: A data split that preserves label proportions or subgroup composition across train/validation/test sets. Helps reduce variance in estimates but must not create leakage.

**Stride** [ML]: The step size a convolution kernel moves across an input. Larger stride reduces sequence length (downsampling) and compute but may lose fine-grained resolution.

**Subgroup shift** [Statistics]: A distribution shift that affects certain groups disproportionately. Drives fairness concerns and motivates intersectional evaluation.

**Subword** [ML]: A token that represents a frequent character sequence shorter than a word, used in tokenization methods like BPE. For genomics, subwords can represent frequent k-mer-like patterns; see also: **BPE**.

**Survival analysis** [Statistics]: Methods for modeling time-to-event outcomes with censoring. Often used for prognosis tasks in clinical ML.

**Synthetic control arm** [Statistics]: A comparison group constructed from historical or real-world data instead of randomized controls. Can reduce trial burden but is sensitive to confounding and dataset mismatch.

**t-SNE (t-distributed stochastic neighbor embedding)** [ML]: A nonlinear visualization method that preserves local neighborhoods in 2D/3D. Common for single-cell plots but can distort global distances and cluster sizes.

**Target identification** [Clinical]: Selecting a biological target (gene, protein, pathway) likely to be causally involved in disease. Often uses genetics, multi-omics, and network evidence.

**Targeted sequencing** [Genomics]: Sequencing restricted to selected regions (panels or exomes) to increase depth and reduce cost. Trades off completeness relative to **whole-genome sequencing**.

**Task head** [ML]: See **model head**. A lightweight module that maps backbone representations to task outputs (e.g., phenotype prediction, binding classification).

**Temperature** [ML]: A scaling parameter that sharpens or smooths a probability distribution, often applied to softmax. Used in sampling, distillation, and contrastive learning; see also: **softmax**.

**Temperature scaling** [Statistics]: A calibration method that rescales logits by a single parameter (temperature) to adjust confidence without changing ranking. Popular for calibrating deep neural networks. See also: **Platt scaling**.

**Test set** [Statistics]: A held-out dataset used only for final evaluation to estimate generalization. Repeated reuse effectively turns it into a validation set and causes benchmark overfitting.

**TF footprinting** [Genomics]: A method to detect putative transcription factor binding from patterns of protection in accessibility assays. Can suggest TF occupancy but is sensitive to technical noise.

**Therapeutic index** [Clinical]: A measure of drug safety comparing toxic dose to effective dose. Higher therapeutic index generally indicates safer drugs.

**Training label** [ML]: The target output a model is trained to predict (e.g., a regulatory peak, a deleteriousness class, or an association statistic). Label choice determines what the model learns and how predictions should be interpreted.

**Trajectory inference** [ML]: Algorithms that infer developmental or state-transition paths from single-cell data, producing pseudotime and branch structure. Helps identify gene programs changing over progressions.

**Transcriptomic signature** [Genomics]: A pattern of gene expression associated with a state (disease, drug perturbation). Used for repurposing, mechanism inference, and patient stratification.

**Transfer learning** [ML]: Using knowledge learned on one dataset/task to improve performance on another, typically by pretraining then fine-tuning. Reduces labeled data needs and improves robustness; see also: **pretraining**.

**Trio sequencing** [Genomics]: Sequencing a child and both parents to identify de novo variants, inheritance patterns, and phasing. Often increases diagnostic yield in pediatric rare disease.

**UK Biobank** [Genomics]: A large population cohort with genotypes, phenotypes, and health records used extensively for GWAS and polygenic score development. Illustrates both the scale and the bias/ancestry challenges in modern genetics.

**Uncertainty under shift** [Statistics]: How uncertainty estimates behave when data distributions change. A good UQ method should become more uncertain on OOD inputs rather than staying overconfident.

**Validation set** [Statistics]: A dataset used during development for model selection and tuning. Must be separated from the test set and respect grouping to avoid leakage.

**Variant** [Genomics]: A DNA sequence difference relative to a reference genome, ranging from SNVs to large structural changes. Variant interpretation depends on context (gene, regulatory region, population frequency, and evidence).

**Variant calling** [Computation]: The process of detecting variants from sequencing reads by comparing observed read evidence to the reference genome. Outputs typically include a **VCF** with genotypes and quality metrics.

**Virtual screening** [Computation]: Computationally ranking large libraries of compounds to identify candidates likely to bind a target. Can be structure-based (docking) or ligand-based (similarity/QSAR).

**Visium** [Genomics]: A commercial spatial transcriptomics platform (10x Genomics) that measures gene expression in spots on a tissue section. Provides spatial patterns at near-cellular resolution depending on tissue density.

**Vocabulary** [ML]: The set of all tokens a model can represent. Larger vocabularies reduce sequence length but increase embedding size and sparsity; see also: **token**, **tokenization**.

**Weight decay** [ML]: A regularization method that penalizes large weights (often implemented as L2 regularization or decoupled weight decay). Helps reduce overfitting and improves generalization.

**Wet-lab validation** [Clinical]: Experimental confirmation that a computational prediction holds in a biological system. Required to translate model suggestions into trustworthy drug or diagnostic decisions.
