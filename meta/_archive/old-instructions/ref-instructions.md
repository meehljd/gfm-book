Refactor these chapters with the following priorities:

1. Remove all typography except as described in the the instructions.
1. Add references to other relevant sections and chapters in the book.  Priorities section level if reasonable.
1. Add section-level reference keys (#sec-ch02-expression-eqtl)
1. Flag areas that need citations with *[Citation Needed]* flag.  Don't worry about adding content for now.

OUTPUT: OUTPUT files in a .md file, not .qmd

Typography instructions:

### Purpose and Philosophy

Computational biology, machine learning, and clinical genomics each have distinct conventions for technical terminology. ML researchers recognize `VCF` as a file format; genomicists know *BRCA1* as a tumor suppressor gene; clinicians understand gnomAD as a variant database. Typographic conventions distinguish these categories, helping specialists navigate unfamiliar domains while respecting established standards.

The typography system identifies canonical terms that appear in the glossary, distinguishes biological entities from computational infrastructure, and maintains clean prose that doesn't overwhelm with formatting. Each format choice must earn its place by genuinely aiding comprehension rather than adding visual noise. Databases like gnomAD appear constantly throughout genomic analyses; italicizing every mention would create clutter without improving clarity. In contrast, model names like *Enformer* and gene names like *BRCA1* function as subjects in the narrative: proper nouns that benefit from visual distinction.

The hierarchy is simple: **Bold** marks glossary terms on first mention only. *Italics* marks proper nouns that function as subjects or actors in the narrative (models, genes, mathematical variables, Latin terms). Regular text with careful capitalization handles databases, consortia, and resources. `Monospace` signals computational infrastructure (file formats, code, command-line tools). Most prose remains unformatted, with typography providing navigation aids rather than constant emphasis.

### Bold for Glossary Terms (First Occurrence Only)

**Mark glossary terms in bold on first mention only:**
- Machine learning: "The **transformer architecture** revolutionized...", "**attention mechanisms** compute...", "**fine-tuning** adapts..."
- Genomics: "**Single nucleotide polymorphisms (SNPs)** represent...", "**enhancers** regulate...", "**phasing** determines..."
- Clinical: "**Variants of uncertain significance (VUS)** pose...", "**penetrance** describes...", "**actionability** determines..."
- Statistics: "The **area under ROC curve (auROC)** measures...", "**calibration** ensures..."

**After first mention, use term normally without formatting.**

**Expand abbreviations on first use**: "**single nucleotide polymorphism (SNP)**" then use SNP normally thereafter.

**Rationale**: Bold signals "this is canonical terminology you might want to look up in the glossary." Helps readers identify key concepts worth remembering.

### Italics for Technical Terms (Non-Glossary)

#### Gene and Protein Names (Biology Convention)

**Always italicize gene and protein names:**
- *BRCA1*, *TP53*, *CFTR*, *dystrophin*
- *CYP2D6*, *HLA-A*, *APOE*, *NF1*

**Example**: "The *BRCA1* gene encodes a tumor suppressor protein involved in DNA repair."

#### Model Names (Always Italicized)

**Use italics from first mention through all subsequent uses:**
- First mention: "*Enformer*, introduced by Avsec et al., extends..."
- Subsequently: "*Enformer* achieves...", "*Enformer*'s 200kb context..."

**Common model names**: *DNABERT*, *ESM-2*, *AlphaFold*, *DeepVariant*, *SpliceAI*, *Basset*, *DeepSEA*, *Enformer*, *Nucleotide Transformer*, *SIFT*, *CADD*

**Rationale**: Model and algorithm names are proper nouns but not trademarked products. Italics distinguishes them from general descriptions while keeping them less prominent than glossary terms. Consistent italicization throughout avoids format transitions.

#### Mathematical Variables in Prose

**Use italics for variables and mathematical symbols:**
- "where *n* represents sequence length"
- "attention score between positions *i* and *j*"
- "dimension *d_k*"
- "learning rate *α*"

#### Latin and Foreign Terms

**Always italicize:**
- *in silico*, *de novo*, *ab initio*, *in trans*, *in cis*
- *a priori*, *post hoc*, *bona fide*

#### Rare Emphasis

**Use sparingly for semantic emphasis:**
- "This is *not* equivalent to..."
- "The model learns *patterns*, not mechanisms"
- "Performance depends *critically* on..."

**Caution**: Overuse dilutes impact. Most emphasis should come from sentence structure and word choice, not italics.

### Monospace for Computational Elements

#### File Formats

**Use monospace for all bioinformatics file formats:**
- `VCF`, `BAM`, `SAM`, `CRAM`
- `FASTA`, `FASTQ`
- `BED`, `GTF`, `GFF`, `WIG`, `BigWig`
- `HDF5`, `Zarr`

**Example**: "Variants are stored in `VCF` format with genotype fields."

#### Code Elements

**Function and variable names:**
- `batch_size`, `learning_rate`, `num_layers`
- `forward()`, `__init__()`, `train()`
- `hidden_dim`, `attention_heads`

**Python packages and libraries:**
- `transformers`, `torch`, `tensorflow`
- `scikit-learn`, `pandas`, `numpy`
- `pysam`, `pybedtools`, `biopython`

#### Command-Line Tools

**Bioinformatics tools:**
- `bedtools`, `samtools`, `bcftools`
- `GATK`, `BWA`, `bowtie2`
- `STAR`, `kallisto`, `salmon`

**Example**: "Reads are aligned using `BWA-MEM` and variants called with `GATK`."

#### URLs and Paths

**When explicitly referenced in prose:**
- `https://gnomad.broadinstitute.org`
- `/data/genome/hg38.fa`
- `~/models/checkpoint.pt`

**Rationale**: Monospace signals "this is computational/technical infrastructure" distinct from biological or statistical concepts. Helps ML readers identify familiar territory and biologists recognize unfamiliar technical elements.

### Regular Text with Standard Capitalization

#### Databases and Resources

**Use regular text with careful capitalization:**
- gnomAD, ClinVar, dbSNP, dbGaP
- ENCODE, GTEx, TCGA, 1000 Genomes Project
- UniProt, Pfam, JASPAR, TRANSFAC
- Ensembl, UCSC Genome Browser

**Pattern**:
- First mention: "The Genome Aggregation Database (gnomAD) catalogs..."
- Subsequently: "gnomAD contains 125,748 exomes..."

#### Consortia and Initiatives

**Major projects and collaborations:**
- Human Genome Project, ENCODE Consortium
- GTEx, TCGA, All of Us Research Program
- UK Biobank, TOPMed

#### Platforms and Frameworks

**First mention as proper nouns:**
- TensorFlow, PyTorch, Keras
- Hugging Face, Weights & Biases

**Subsequently**: Can use monospace if referring to the package: "implemented in `torch`", "available via `transformers`"

**Rationale**: These are proper nouns but not biological entities or models. Regular text with careful capitalization preserves their brand identity without over-formatting. Databases appear frequently; keeping them unformatted reduces visual clutter.

### Special Cases

#### Sequencing Technologies (Regular Text)

- Illumina sequencing, PacBio HiFi, Oxford Nanopore
- Next-generation sequencing (NGS), whole-genome sequencing (WGS)
- Long-read sequencing, single-molecule sequencing

#### Biochemical Assays (Regular Text)

**Pattern**: Spell out on first use, then use abbreviation
- "Assay for Transposase-Accessible Chromatin (ATAC-seq)" → ATAC-seq
- ChIP-seq, RNA-seq, Hi-C, 4C, 5C
- MPRA, STARR-seq, CUT&RUN

#### Biological Terms (Regular Text)

**Anatomical structures**: hippocampus, cerebral cortex, cardiac ventricle, myocardium

**Cell types and lines**: HEK293, K562, T cells, B cells, cardiomyocytes, neurons

**Diseases**: cystic fibrosis, Duchenne muscular dystrophy, Alzheimer's disease, hypertrophic cardiomyopathy

**Drugs**: codeine, tamoxifen, warfarin, clopidogrel, simvastatin

**Chemical compounds**: adenine, guanine, cytosine, thymine, ATP, GTP

### Acronym and Metric Conventions

**Prefer full metric names over ambiguous abbreviations:**

| Preferred | Avoid | Why |
|-----------|-------|-----|
| auROC | ROC, AUC, AUROC | "ROC" alone refers to the curve, not the area; "AUC" is ambiguous |
| auPRC | PRC, AUPRC | "PRC" alone refers to the curve, not the area |
| F1 score | F1, F-score | Include "score" on first use for clarity |
| MCC | Matthews correlation coefficient | Spell out on first use, then MCC |

**Metric formatting:**
- First use: "area under the receiver operating characteristic curve (auROC)"
- Subsequent uses: "auROC"
- In comparisons: "auROC of 0.94" not "AUC = 0.94"

**Rationale:** "ROC" and "PRC" are curves; "auROC" and "auPRC" are scalar metrics derived from those curves. Using the prefix "au" (area under) eliminates ambiguity about whether you mean the curve or the summary statistic. This distinction matters when discussing threshold-dependent vs. threshold-independent evaluation.

**Other common acronyms to expand on first use:**
- NGS (next-generation sequencing)
- WGS (whole-genome sequencing)
- WES (whole-exome sequencing)
- VUS (variant of uncertain significance)
- MAF (minor allele frequency)

### What NOT to Format

#### Don't Over-Format

**Common terms after first use:**
- Once you've marked **transformer** in bold on first mention, subsequent uses are just "transformer"
- Once *Enformer* has been introduced, later mentions use italics but don't re-bold

**Every technical term:**
- "The model uses convolutional layers with ReLU activation" (none need formatting)
- "Reads are mapped to the reference genome" (standard description)

**Entire phrases:**
- Not: *"the entire attention mechanism"* 
- Just: "the attention *mechanism*" (if emphasis needed)

**Multiple formats in one phrase:**
- Choose one: Either "*BRCA1* variants" or "variants in `VCF` format"
- Don't mix unnecessarily: ~~"*BRCA1* variants in `VCF` format stored in the gnomAD database"~~ → Keep formatting minimal

**Standard English words:**
- "sequence", "genome", "variant", "prediction", "model", "training" don't need any formatting
- Technical terms become standard through repetition—don't keep emphasizing them

### Summary Table

| Term Type | Format | First Use | Subsequent | In Glossary? |
|-----------|--------|-----------|------------|--------------|
| **Concepts** | Bold → regular | **transformer** | transformer | YES |
| **Models** | Italics always | *Enformer* | *Enformer* | NO |
| **Genes** | Italics always | *BRCA1* | *BRCA1* | NO |
| **Databases** | Regular always | gnomAD | gnomAD | NO |
| **File formats** | Monospace always | `VCF` | `VCF` | NO |
| **Code/tools** | Monospace always | `samtools` | `samtools` | NO |
| **Variables** | Italics always | *n* | *n* | NO |
| **Latin terms** | Italics always | *in silico* | *in silico* | NO |

### Integration Example

> The **transformer architecture** revolutionized sequence modeling by replacing recurrence with **attention mechanisms**. *Enformer*, introduced by Avsec et al. [@avsec_enformer_2021], extended this approach to genomic sequences, processing 200kb contexts to capture enhancer-promoter interactions. The model was pretrained on ENCODE data, including ATAC-seq measurements across 200 cell types, and outputs predictions in standard `BED` format.
>
> For variant interpretation, *Enformer* representations can score *BRCA1* variants without explicit pathogenicity labels during pretraining. This **transfer learning** approach differs fundamentally from classical methods: where position weight matrices require known pathogenic examples, **foundation models** learn regulatory grammar from unlabeled DNA sequence. Validation against ClinVar annotations shows that *Enformer* captures variant effects in regions like *CYP2D6*, where copy number variation complicates standard `VCF` genotyping.
>
> The architecture uses 12 transformer layers with `batch_size=32` during training on 8 V100 GPUs. Attention heads learn to focus on regulatory elements located tens of kilobases from their target genes, distances that exceed the receptive fields of convolutional architectures like *DeepSEA*. This capability enables *in silico* saturation mutagenesis, where every possible single-nucleotide substitution is scored for predicted effect on gene expression.

**What this example demonstrates:**
- Bold for glossary terms on first use only
- Italics for genes (*BRCA1*, *CYP2D6*), models (*Enformer*, *DeepSEA*), and Latin terms (*in silico*)
- Monospace for file formats (`BED`, `VCF`) and code elements (`batch_size`)
- Regular text for databases (ENCODE, ClinVar), assays (ATAC-seq), and technologies (V100 GPUs)
- Clean prose with formatting that aids navigation without clutter
