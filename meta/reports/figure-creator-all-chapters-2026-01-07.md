# Figure Generation Report - All Chapters
**Generated:** 2026-01-07

## Summary

All programmatic figures have been generated for the GFM textbook using Matplotlib and Graphviz.

| Part | Chapters | Figures | Description |
|------|----------|---------|-------------|
| Part 1 | Ch 1-4 | 31 | Data Foundations |
| Part 2 | Ch 5-12 | 91 | Learning & Evaluation |
| Part 3 | Ch 13-17 | 84 | Foundation Model Families |
| Part 4 | Ch 18-22 | 146 | Cellular Context |
| Part 5 | Ch 23-26 | 42 | Responsible Deployment |
| Part 6 | Ch 27-31 | 43 | Applications & Frontiers |
| **Total** | **31 chapters** | **437 SVGs** | |

## Figure Breakdown by Chapter

### Part 1: Data Foundations
- Ch 1: NGS variant pipeline, phasing, error sources, difficult regions, DeepVariant
- Ch 2: Data types, file formats, quality metrics
- Ch 3: GWAS Manhattan plots, LD structure, fine-mapping
- Ch 4: Classical VEP methods, conservation, functional prediction

### Part 2: Learning & Evaluation
- Ch 5: Sequence encodings, k-mer representations
- Ch 6: CNN architectures, motif detection, dilated convolutions
- Ch 7: Attention mechanisms, self-attention, multi-head
- Ch 8: Transformer architecture, positional encodings
- Ch 9: Transfer learning strategies
- Ch 10: Adaptation methods (fine-tuning, LoRA, prompting)
- Ch 11: Benchmark design, evaluation metrics, leaderboards
- Ch 12: Confounding factors, data leakage, batch effects

### Part 3: Foundation Model Families
- Ch 13: Foundation model paradigm, pretraining objectives
- Ch 14: DNA language models, tokenization, architectures
- Ch 15: Protein language models, ESM, structure prediction
- Ch 16: Regulatory models, enhancer prediction, cell-type specificity
- Ch 17: VEP foundation models, pathogenicity prediction

### Part 4: Cellular Context
- Ch 18: RNA models, splicing, expression prediction
- Ch 19: Single-cell models, embeddings, cell atlases
- Ch 20: 3D genome, Hi-C, chromatin architecture
- Ch 21: Network models, GNNs, pathway analysis
- Ch 22: Multi-omics integration, fusion strategies

### Part 5: Responsible Deployment
- Ch 23: Uncertainty quantification, calibration, conformal prediction
- Ch 24: Interpretability, attribution, TF-MoDISco
- Ch 25: Causal inference, ladder of causation, evidence hierarchy
- Ch 26: Regulatory/ethics, SaMD classification, consent models

### Part 6: Applications & Frontiers
- Ch 27: Clinical risk prediction, fairness assessment
- Ch 28: Rare disease diagnosis, ACMG-AMP, family analysis
- Ch 29: Drug discovery, target prioritization, biomarkers
- Ch 30: Sequence design, DBTL cycle, generative models
- Ch 31: Frontiers, scaling laws, agentic systems

## Technical Details

### Tools Used
- **Matplotlib**: Bar charts, scatter plots, line plots, heatmaps, multi-panel figures
- **Graphviz**: Flowcharts, pipelines, architecture diagrams, decision trees

### Color Palette (Consistent across all figures)
- DNA/Genomics: `#1f77b4` (blue)
- RNA/Transcriptomics: `#2ca02c` (green)
- Protein: `#ff7f0e` (orange)
- Model/AI: `#9467bd` (purple)
- Error/High-risk: `#d62728` (red)
- Supporting colors: `#aec7e8`, `#98df8a`, `#ffbb78`, `#c5b0d5`

### Output Format
- All figures exported as SVG for scalability
- Multi-panel figures saved as separate SVG files per panel

### Script Locations
All generation scripts are in `/root/gfm_book/scripts/figures/chXX/generate_all.py`

## Notes

1. Some figures may need manual adjustment for optimal text positioning
2. All figures follow the style guide at `meta/_instructions/figure-style-guide.md`
3. Figures are referenced in QMD files with the `@fig-` prefix
