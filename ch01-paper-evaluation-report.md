# Chapter 01 Paper Evaluation Report
Reviewed papers cited in Chapter 1 (from `p1-ch01.bib`) using the project evaluation framework.

## Summary
Total papers: 31

- INCLUDE: 31
- CITED: 0
- MONITOR: 0
- EXCLUDE: 0

All BibTeX entries contained a DOI and/or URL, so none were flagged as missing-PDF based on metadata alone.
## Preprints and publication status checks
- `@song_t1k_2022`: published as *Genome Research* (2023), doi: 10.1101/gr.277585.122.
- `@li_bwa-mem_2013`: remains an arXiv preprint (1303.3997) used as the canonical BWA-MEM reference.
## Per-paper evaluation table (sorted by citation key)
| Cite_Key | Year | Venue | Status | Repro | Valid | Claims | Pedagogy | Longevity | Book_Location | Title | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| @browning_beagle_2021 | 2021 | Am J Hum Genet | INCLUDE | 3 | 3 | OK | H | + | Ch01-HaplotypePhasing/Imputation | Fast two-stage phasing of large-scale sequence data | Two-stage phasing; cohort-scale speed/accuracy evidence |
| @bycroft_ukbiobank_2018 | 2018 | Nature | INCLUDE | 2 | 2 | OK | M | + | Ch01-CohortCalling/GLnexus | UK Biobank resource w/ deep phenotyping & genomic data | Canonical biobank-scale cohort + QC/imputation context |
| @dabernig_ont_2024 | 2024 | J Clin Microbiol | INCLUDE | 2 | 3 | OK | H | ? | Ch01-LongReadTech | Multicenter ONT genotyping accuracy & reproducibility | Multi-lab ONT study; strain-specific errors; mitigations via models/polish |
| @depristo_gatk_2011 | 2011 | Nat Genet | INCLUDE | 2 | 3 | OK | H | + | Ch01-ClassicalPipelines/CohortFiltering | Framework for variation discovery & genotyping (NGS) | Foundational pipeline stages + validation across technologies/designs |
| @garrison_vgtool_2018 | 2018 | Nat Biotechnol | INCLUDE | 3 | 3 | OK | H | + | Ch01-HLA/ComplexRegions | Variation graph toolkit improves read mapping (vg) | Graph references reduce mapping bias; practical human-scale toolkit |
| @goodwin_10year_2016 | 2016 | Nat Rev Genet | INCLUDE | 1 | 1-2 | OK | H | ? | Ch01-NGSChallenge | Coming of age: ten years of next-generation sequencing technologies | High-level tech evolution + limitations; good framing citation |
| @jiang_cutesv_2020 | 2020 | Genome Biology | INCLUDE | 3 | 2-3 | OK | H | ? | Ch01-LongReadSV | Long-read-based human genomic structural variation detection with cuteSV | cuteSV signatures + clustering/refinement; benchmarked on sim+real data |
| @karczewski_gnomad_2020 | 2020 | Nature | INCLUDE | 2 | 3 | OK (caution) | H | + | Ch01-PopResources/Interpretation | Mutational constraint spectrum from variation in 141,456 humans (gnomAD) | Constraint metrics; addendum highlights pLoF artefact risk and need for curation |
| @krusche_happy_2019 | 2019 | Nat Biotechnol | INCLUDE | 3 | 3 | OK | H | + | Ch01-Evaluation/Benchmarks | Best practices for benchmarking germline small-variant calls in human genomes | GA4GH benchmarking framework; standard metrics/stratification; hap.py ecosystem |
| @li_bwa-mem_2013 | 2013 | arXiv | INCLUDE | 3 | 2 | OK | H | + | Ch01-Alignment | Aligning sequence reads, clone sequences and assembly contigs with BWA-MEM | SMEM seeding + re-seeding; banded affine-gap DP; chimeric/PE rescue; sim benchmarking + runtimes |
| @li_mapping_2014 | 2014 | Bioinformatics | INCLUDE | 3 | 2 | OK (preprint) | M | ? | Ch01-Foundations | Towards {Better} {Understanding} of {Artifacts} in {Variant} {Calling} from {High}-{Coverage} {Samples} |  |
| @li_minimap2_2018 | 2018 | Bioinformatics | INCLUDE | 3 | 2 | OK | M | ? | Ch01-Alignment | Minimap2: pairwise alignment for nucleotide sequences |  |
| @liao_pangenome_2023 | 2023 | Nature | INCLUDE | 3 | 3 | OK | H | + | Ch01-Foundations | A draft human pangenome reference |  |
| @loh_eagle_2016 | 2016 | Nature Genetics | INCLUDE | 3 | 3 | OK | H | + | Ch01-Phasing | Reference-based phasing using the {Haplotype} {Reference} {Consortium} panel |  |
| @mallal_abacavir_2008 | 2008 | New England Journal of Medicine | INCLUDE | 1 | 3 | OK | M | + | Ch01-Foundations | {HLA}-{B}*5701 {Screening} for {Hypersensitivity} to {Abacavir} |  |
| @nielsen_error_2011 | 2011 | Nature Reviews. Genetics | INCLUDE | 2 | 2 | OK | M | + | Ch01-Foundations | Genotype and {SNP} calling from next-generation sequencing data |  |
| @noauthor_pbsv_2025 | 2025 | PacBio | INCLUDE | 3 | 2 | OK | M | ? | Ch01-StructuralVariants | {PacificBiosciences}/pbsv |  |
| @noauthor_rtg-core_2025 | 2025 | Real Time Genomics | INCLUDE | 3 | 2 | OK | M | ? | Ch01-Foundations | {RealTimeGenomics}/rtg-core |  |
| @nurk_complete_2022 | 2022 | Science | INCLUDE | 2 | 3 | OK | M | ? | Ch01-Foundations | The complete sequence of a human genome |  |
| @oconnell_shapeit2_2014 | 2014 | PLOS Genetics | INCLUDE | 3 | 3 | OK | M | + | Ch01-Phasing | A {General} {Approach} for {Haplotype} {Phasing} across the {Full} {Spectrum} of {Relatedness} |  |
| @poplin_deepvariant_2018 | 2018 | Nature Biotechnology | INCLUDE | 2 | 2 | OK | M | ? | Ch01-VariantCallingDL | [{DeepVariant}] {A} universal {SNP} and small-indel variant caller using deep neural networks |  |
| @robinson_hla-db_2020 | 2020 | Nucleic Acids Research | INCLUDE | 3 | 3 | OK | H | + | Ch01-Foundations | {IPD}-{IMGT}/{HLA} {Database} |  |
| @sakaue_hla_2023 | 2023 | Nature Protocols | INCLUDE | 3 | 3 | OK | M | ? | Ch01-Foundations | Tutorial: a statistical genetics guide to identifying {HLA} alleles driving complex disease |  |
| @shafin_pepper_2021 | 2021 | Nature Methods | INCLUDE | 3 | 2 | OK | M | ? | Ch01-VariantCallingDL | Haplotype-aware variant calling with {PEPPER}-{Margin}-{DeepVariant} enables high accuracy in nanopore long-reads |  |
| @smolka_sniffles2_2024 | 2024 | Nature Biotechnology | INCLUDE | 3 | 3 | OK | M | ? | Ch01-StructuralVariants | Detection of mosaic and population-level structural variants with {Sniffles2} |  |
| @song_t1k_2022 | 2022 | bioRxiv | INCLUDE | 1 | 3 | OK (preprint) | M | ? | Ch01-Foundations | {T1K}: efficient and accurate {KIR} and {HLA} genotyping with next-generation sequencing data | Preprint now published (Genome Res 2023, doi:10.1101/gr.277585.122) |
| @van_der_auwera_gatk_best_2018 | 2018 | Current Protocols in Bioinformatics | INCLUDE | 3 | 2 | OK | M | ? | Ch01-Foundations | From {FastQ} {Data} to {High}-{Confidence} {Variant} {Calls}: {The} {Genome} {Analysis} {Toolkit} {Best} {Practices} {Pipeline} |  |
| @wenger_pacbiohifi_2019 | 2019 | Nature Biotechnology | INCLUDE | 2 | 3 | OK | M | ? | Ch01-Foundations | Accurate circular consensus long-read sequencing improves variant detection and assembly of a human genome |  |
| @yun_accurate_2021 | 2021 | Bioinformatics | INCLUDE | 3 | 3 | OK | M | ? | Ch01-Foundations | Accurate, scalable cohort variant calls using {DeepVariant} and {GLnexus} |  |
| @zheng_clair3_2022 | 2022 | Nature Computational Science | INCLUDE | 3 | 2 | OK | M | ? | Ch01-VariantCallingDL | Symphonizing pileup and full-alignment for deep learning-based long-read variant calling |  |
| @zook_giab_2019 | 2019 | Nature biotechnology | INCLUDE | 3 | 3 | OK | H | + | Ch01-Resources | An open resource for accurately benchmarking small variant and reference calls |  |
