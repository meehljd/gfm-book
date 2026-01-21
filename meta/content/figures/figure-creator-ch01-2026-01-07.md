# Figure Creator Report: Chapter 1

Generated: 2026-01-07
Chapter: From Reads to Variants (p1-ch01-ngs)
Figures processed: 7
Figures created: 7
Figures needing review: 0

## Summary

All 7 figures in Chapter 1 were placeholder SVGs containing only descriptive text. Each has been replaced with a proper programmatic visualization using Matplotlib. All figures render successfully and match their specifications from the chapter captions.

| Figure ID | Tool | Iterations | Status | Notes |
|-----------|------|------------|--------|-------|
| 01-fig-variant-pipeline | Matplotlib | 1 | Success | Flowchart of variant calling pipeline |
| 02-A-fig-phasing-compound-het | Matplotlib | 1 | Success | Panel A: Unphased view |
| 02-B-fig-phasing-compound-het | Matplotlib | 1 | Success | Panel B: Cis configuration |
| 02-C-fig-phasing-compound-het | Matplotlib | 1 | Success | Panel C: Trans configuration |
| 03-fig-error-sources | Matplotlib | 1 | Success | Taxonomy of error sources |
| 04-fig-difficult-regions | Matplotlib | 1 | Success | Genome ideogram with insets |
| 05-fig-deepvariant-pileup | Matplotlib | 1 | Success | Pileup tensor + CNN diagram |

---

## Figure Details

### 01-fig-variant-pipeline

**Output**: `figs/part_1/ch01/01-fig-variant-pipeline.svg` (106 KB)
**Script**: `scripts/figures/ch01/fig_01_variant_pipeline.py`
**Tool**: Matplotlib

**Description**: End-to-end flowchart showing the variant calling pipeline from DNA sample to VCF file. Shows both short-read and long-read sequencing paths converging at alignment, through post-processing, variant calling (HaplotypeCaller/DeepVariant), joint genotyping (GLnexus), and filtering (VQSR).

**Elements**:
- Color-coded boxes for each processing stage
- File format labels (FASTQ, BAM, gVCF, VCF)
- Approximate file sizes for 30× WGS
- Section groupings for major pipeline phases

**Evaluation**: PASS
- All pipeline stages present
- Clear left-to-right/top-to-bottom flow
- Readable labels
- Consistent genomics color palette

---

### 02-A/B/C-fig-phasing-compound-het

**Output**: `figs/part_1/ch01/02-{A,B,C}-fig-phasing-compound-het.svg` (~43 KB each)
**Script**: `scripts/figures/ch01/fig_02_phasing_compound_het.py`
**Tool**: Matplotlib

**Description**: Three-panel figure explaining compound heterozygosity and the clinical importance of phasing:
- Panel A: Unphased genotypes (phase unknown)
- Panel B: Cis configuration (carrier, unaffected)
- Panel C: Trans configuration (affected with CF)

**Elements**:
- Maternal/paternal chromosomes with distinct colors
- CFTR gene region highlighted
- Variant markers (F508del, G551D)
- VCF notation examples (0/1 vs 0|1)
- Clinical outcome boxes

**Evaluation**: PASS
- All three panels clearly differentiated
- Cis vs trans distinction visually obvious
- Clinical implications clearly labeled
- Color coding consistent

---

### 03-fig-error-sources

**Output**: `figs/part_1/ch01/03-fig-error-sources.svg` (99 KB)
**Script**: `scripts/figures/ch01/fig_03_error_sources.py`
**Tool**: Matplotlib

**Description**: Hierarchical taxonomy organizing variant calling errors into three major categories with their consequences.

**Elements**:
- Root node: "Variant Call Errors"
- Three branches: Sequencing Artifacts, Alignment Artifacts, Biological Complexity
- FP/FN consequence badges
- Example items under each category
- Legend explaining FP = False Positive, FN = False Negative

**Evaluation**: PASS
- Clear hierarchical structure
- FP/FN distinctions visible
- Examples aid understanding
- Color-coded by error type

---

### 04-fig-difficult-regions

**Output**: `figs/part_1/ch01/04-fig-difficult-regions.svg` (123 KB)
**Script**: `scripts/figures/ch01/fig_04_difficult_regions.py`
**Tool**: Matplotlib

**Description**: Human genome ideogram showing regions where short-read variant calling systematically fails.

**Elements**:
- All 24 chromosomes (1-22, X, Y) in two columns
- Highlighted regions: segmental duplications, HLA, CYP2D6, tandem repeat disorders
- Centromeres marked on each chromosome
- Annotations for specific disease loci (HTT, FMR1)
- Pie chart inset showing genome fraction by callability
- Long read comparison inset

**Evaluation**: PASS
- All chromosomes visible and properly sized
- Difficult regions highlighted with correct colors
- Insets provide additional context
- Legend explains region types

---

### 05-fig-deepvariant-pileup

**Output**: `figs/part_1/ch01/05-fig-deepvariant-pileup.svg` (114 KB)
**Script**: `scripts/figures/ch01/fig_05_deepvariant_pileup.py`
**Tool**: Matplotlib

**Description**: Visualization of DeepVariant's pileup tensor representation and CNN classification architecture.

**Elements**:
- Reference sequence with variant position marked
- 12 simulated reads showing heterozygous pattern (~50/50 allele split)
- Base quality indicated by color intensity
- Strand orientation (+/-) indicators
- CNN architecture diagram (Conv → Pool → FC)
- Genotype probability output with bar chart
- Called genotype result (0/1)

**Evaluation**: PASS
- Tensor concept clearly illustrated
- Heterozygous pattern visible in reads
- CNN flow understandable
- Probability output intuitive

---

## Files Created

### Scripts
- `scripts/figures/ch01/fig_01_variant_pipeline.py`
- `scripts/figures/ch01/fig_02_phasing_compound_het.py`
- `scripts/figures/ch01/fig_03_error_sources.py`
- `scripts/figures/ch01/fig_04_difficult_regions.py`
- `scripts/figures/ch01/fig_05_deepvariant_pileup.py`

### Figures
- `figs/part_1/ch01/01-fig-variant-pipeline.svg` (106 KB)
- `figs/part_1/ch01/02-A-fig-phasing-compound-het.svg` (43 KB)
- `figs/part_1/ch01/02-B-fig-phasing-compound-het.svg` (44 KB)
- `figs/part_1/ch01/02-C-fig-phasing-compound-het.svg` (42 KB)
- `figs/part_1/ch01/03-fig-error-sources.svg` (99 KB)
- `figs/part_1/ch01/04-fig-difficult-regions.svg` (123 KB)
- `figs/part_1/ch01/05-fig-deepvariant-pileup.svg` (114 KB)

### Auxiliary Files
- `figs/part_1/ch01/01-fig-variant-pipeline.mmd` (Mermaid source, not rendered due to missing browser dependencies)

---

## Notes

1. **Tool Selection**: Matplotlib was used for all figures because the Mermaid CLI (mmdc) requires Puppeteer/Chrome browser dependencies not available in this environment. Matplotlib provides equivalent or better control for scientific figures.

2. **Color Palette**: All figures use the genomics color palette from the book's style guide:
   - DNA/sequence: Blues (#1f77b4, #aec7e8)
   - RNA: Greens (#2ca02c, #98df8a)
   - Protein: Oranges (#ff7f0e)
   - Model components: Purple (#9467bd)

3. **Regeneration**: To regenerate any figure, run the corresponding Python script:
   ```bash
   python3 scripts/figures/ch01/fig_XX_name.py
   ```

4. **All figures passed evaluation on first iteration** - no refinement loops were needed.
