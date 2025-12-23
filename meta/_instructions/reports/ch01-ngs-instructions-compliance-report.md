# Compliance Review: `p1-ch01-ngs` vs Project Instructions

Date: 2025-12-23

## Inputs
- Instructions: `claude-project-instructions.md`
- Chapter: `p1-ch01-ngs.qmd` (305 lines)

## Automated Rule Checks

| Check | Result | Evidence |
|---|---:|---|
| Em-dash character (U+2014 (em dash)) count | 0 | PASS |
| Bullet list lines (`-`, `*`, `+`, `•`) | 0 | PASS |
| Meta-commentary triggers ('This chapter…', 'scope of this chapter…') | 2 | FAIL (lines 5, 17) |
| Figure blocks present | 5 | PASS (fig-variant-calling-pipeline, fig-phasing-compound-het, fig-error-sources, fig-difficult-regions, fig-deepvariant-pileup) |
| In-text figure references (`@fig-*`) | 0 | WARN |
| Citation brackets (`[@...]`) | 37 | INFO |

## Issues

### ISSUE-001 (critical)
- Type: output_format
- Rule: All content must be delivered as markdown files (.md); never create .qmd files.
- Location: `/mnt/data/p1-ch01-ngs.qmd` lines 1-1
- Heading path: From Reads to Variants
- Evidence: File name is p1-ch01-ngs.qmd (Quarto .qmd).
- Recommendation: Convert/rename to .md. Ensure any Quarto-only constructs remain Pandoc-compatible (fenced divs, cross-ref ids) or adjust accordingly.

### ISSUE-002 (major)
- Type: style_meta_commentary
- Rule: Zero meta-commentary (avoid 'This chapter examines...', 'The focus is...', etc.).
- Location: `/mnt/data/p1-ch01-ngs.qmd` lines 5-6
- Heading path: From Reads to Variants
- Evidence: This chapter examines the technical foundations of variant calling, from raw sequencing signal to the `VCF` files that serve as input to every model in this book. The focus is not on operational details of running pipelines but on the inferential challenges that determine when variant calls can be trusted and when...
- Recommendation: Rewrite opening paragraph(s) to remove self-referential framing. State stakes/arc directly without narrating what the chapter will do.

### ISSUE-003 (major)
- Type: style_meta_commentary
- Rule: Avoid chapter-structure narration ('The scope of this chapter...').
- Location: `/mnt/data/p1-ch01-ngs.qmd` lines 17-17
- Heading path: From Reads to Variants > The Challenge of NGS Data
- Evidence: The scope of this chapter centers on germline variant calling in human whole-exome sequencing (WES) and whole-genome sequencing (WGS) data, the core technical challenge underlying most genomic deep learning applications. Somatic variant calling in cancer and RNA-seq-specific...
- Recommendation: Integrate scope constraints implicitly (e.g., motivate germline WES/WGS focus by relevance to downstream models) rather than stating 'scope of this chapter'.

### ISSUE-004 (moderate)
- Type: structure_why_first
- Rule: Lead with why at subsection openings (stakes/motivation before mechanism).
- Location: `/mnt/data/p1-ch01-ngs.qmd` lines 55-59
- Heading path: From Reads to Variants > Classical Variant Calling Pipelines > From Sequencer to Aligned Reads
- Evidence: ### From Sequencer to Aligned Reads The journey from DNA sample to variant calls begins when instrument software converts fluorescent images or electrical signals to base calls and quality scores through **base calling**. Reads are demultiplexed by sample barcode into `FASTQ` files, each containing millions of short...
- Recommendation: Add 1-2 sentences at the start linking base calling/alignment to downstream error modes (e.g., how miscalls and misalignments create false variants) before describing steps.

### ISSUE-005 (moderate)
- Type: structure_why_first
- Rule: Avoid opening a subsection with pure definitions; motivate first.
- Location: `/mnt/data/p1-ch01-ngs.qmd` lines 219-223
- Heading path: From Reads to Variants > Benchmarking and Ground Truth > Metrics and Their Meaning
- Evidence: ### Metrics and Their Meaning Standard metrics for variant calling include **recall (sensitivity)**, the fraction of true variants in the benchmark successfully identified by the caller; **precision (positive predictive value)**, the fraction of called variants that are present in the benchmark truth set; and **F1...
- Recommendation: Open with the evaluative pitfall (benchmarks can mislead; small deltas may not matter) then define recall/precision/F1.

### ISSUE-006 (moderate)
- Type: structure_why_first
- Rule: Subsection openings should establish why the mechanism matters before details.
- Location: `/mnt/data/p1-ch01-ngs.qmd` lines 237-241
- Heading path: From Reads to Variants > DeepVariant: Variant Calling as Image Classification > Pileup Images as Input
- Evidence: ### Pileup Images as Input Around each candidate variant site, *DeepVariant* constructs a multi-channel tensor resembling an image. Each row corresponds to a read overlapping the site, with columns indexing positions relative to the candidate variant. Channels encode multiple features: match or mismatch with the...
- Recommendation: Add a hook sentence about why representing reads as an 'image' helps (captures local context/quality signals in a learnable form) before describing tensor channels.

### ISSUE-007 (moderate)
- Type: structure_why_first
- Rule: Subsection openings should establish motivation before listing architecture/training details.
- Location: `/mnt/data/p1-ch01-ngs.qmd` lines 249-253
- Heading path: From Reads to Variants > DeepVariant: Variant Calling as Image Classification > Architecture and Training
- Evidence: ### Architecture and Training *DeepVariant* uses an Inception-style CNN architecture originally developed for natural image classification. The convolutional architecture that makes this possible is examined in detail in @sec-cnn. The network processes the pileup tensor through multiple convolutional layers, pooling...
- Recommendation: Prepend a sentence tying architecture choice and training regime to the earlier 'reformulation' (what the CNN must learn, why calibration matters), then proceed.

### ISSUE-008 (moderate)
- Type: structure_why_first
- Rule: Lead with why: explain why joint genotyping is required before describing GLnexus mechanics.
- Location: `/mnt/data/p1-ch01-ngs.qmd` lines 257-261
- Heading path: From Reads to Variants > DeepVariant: Variant Calling as Image Classification > Cohort Calling with GLnexus
- Evidence: ### Cohort Calling with GLnexus *DeepVariant* operates primarily at the per-sample level, producing a `gVCF` of genotype likelihoods for each individual sample. To generate a multi-sample `VCF` suitable for population-scale analysis, these per-sample results must be combined through joint genotyping.
- Recommendation: Start with the problem (per-sample calls are incomparable; cohort consistency and rare variant sensitivity require joint genotyping) then describe GLnexus.

### ISSUE-009 (minor)
- Type: citations_style
- Rule: Avoid mid-sentence bracket citations that break flow; prefer end-of-sentence or in-prose citations.
- Location: `/mnt/data/p1-ch01-ngs.qmd` lines 47-47
- Heading path: From Reads to Variants > Targeting Strategies: Panels, Exomes, and Genomes > Long-Read Sequencing Technologies
- Evidence: Long reads transform variant calling by traversing low-complexity and repetitive regions essentially invisible to short-read technologies. Dedicated variant callers such as PEPPER-Margin-DeepVariant [@shafin_haplotype-aware_2021], Clair3 [@zheng_symphonizing_2022], Sniffles2 [@smolka_detection_2024], `pbsv`...
- Recommendation: Move the tool citations to the end of the sentence (single bracket with multiple refs) or use in-prose attribution (e.g., 'Zheng et al. introduced Clair3...').

### ISSUE-010 (minor)
- Type: cross_references
- Rule: Use cross-references to figures/sections liberally to reinforce cohesion.
- Location: `/mnt/data/p1-ch01-ngs.qmd` lines 61-247
- Heading path: (multiple figure blocks)
- Evidence: Figure blocks exist (fig-variant-calling-pipeline, fig-phasing-compound-het, fig-error-sources, fig-difficult-regions, fig-deepvariant-pileup) but no '@fig-*' references appear in prose.
- Recommendation: Add in-text references where the figures are discussed (e.g., 'Figure @fig-variant-calling-pipeline summarizes...').

### ISSUE-011 (minor)
- Type: headings_style
- Rule: Avoid leading articles in headings; prefer concise noun phrases.
- Location: `/mnt/data/p1-ch01-ngs.qmd` lines 9-299
- Heading path: (headings)
- Evidence: Headings starting with 'The': line 9 'The Challenge of NGS Data'; line 199 'The HLA Region: A Case Study in Complexity'; line 299 'The Reliability Landscape'.
- Recommendation: Drop leading 'The' (e.g., 'NGS Data Challenges', 'HLA Region Complexity', 'Reliability Landscape').

### ISSUE-012 (minor)
- Type: headings_style
- Rule: Heading length guidelines: ## headings typically 3-5 words; ### headings 2-4 words.
- Location: `/mnt/data/p1-ch01-ngs.qmd` lines 19-289
- Heading path: (headings)
- Evidence: ## outside 3-5 words: line 19 (6 words), line 104 (2), line 179 (8), line 233 (6). ### outside 2-4 words: lines 55, 155, 167, 189, 195, 199, 283, 289.
- Recommendation: If enforcing strict heading compactness, rename to shorter noun phrases while preserving meaning.

### ISSUE-013 (minor)
- Type: typography
- Rule: Avoid multiple emphasized words in the same sentence (creates noise).
- Location: `/mnt/data/p1-ch01-ngs.qmd` lines 37-221
- Heading path: (multiple paragraphs)
- Evidence: Multiple bold segments in one sentence at lines 37, 67, 112, 140, 217, 221.
- Recommendation: Consider limiting bold to the single key glossary term per sentence or distribute definitions across sentences.

### ISSUE-014 (minor)
- Type: style_hedging
- Rule: Hedging adverbs (including 'rather') should be used sparingly when not adding meaning.
- Location: `/mnt/data/p1-ch01-ngs.qmd` lines 53-279
- Heading path: (multiple paragraphs)
- Evidence: Occurrences of 'rather' at lines: 53, 142, 165, 205, 235, 241, 269, 279.
- Recommendation: Review each usage and delete when it functions as filler; keep when expressing a real contrast ('not X but rather Y').