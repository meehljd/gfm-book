# Summary: Selected Figures by Chapter

| Chapter | Title | Essential | High | Enhancing | Total |
|---------|-------|-----------|------|-----------|-------|
| 1 | NGS | 2 | 2 | 1 | 5 |
| 2 | Data | 1 | 3 | 0 | 4 |
| 3 | GWAS | 2 | 3 | 0 | 5 |
| 4 | VEP Classical | 2 | 3 | 0 | 5 |
| 5 | Representations | 2 | 2 | 1 | 5 |
| 6 | CNNs | 2 | 2 | 1 | 5 |
| 7 | Attention | 2 | 3 | 1 | 6 |
| 8 | Pretraining | 2 | 2 | 1 | 5 |
| 9 | Transfer | 2 | 3 | 0 |5 |
| 10 | Foundation Model Paradigm | 3 | 2 | 0 | 5 |
| 11 | DNA Language Models | 2 | 3 | 1 | 6 |
| 12 | Protein Language Models | 2 | 2 | 1 | 5 |
| 13 | Regulatory Models | 2 | 2 | 1 | 5 |
| 14 | Variant Effect Prediction | 3 | 2 | 1 | 6 |
| 15 | RNA Structure and Function | 2 | 3 | 0 | 5 |
| 16 | Single-Cell Models | 2 | 3 | 0 | 5 |
| 17 | 3D Genome Organization | 2 | 2 | 1 | 5 |
| 18 | Graph and Network Models | 2 | 3 | 1 | 6 |
| 19 | Multi-Omics Integration | 2 | 3 | 0 | 5 |
| 20 | Benchmarks | 2 | 3 | 0 | 5 |
| 21 | Evaluation | 2 | 3 | 1 | 6 |
| 22 | Confounding | 2 | 3 | 1 | 6 |
| 23 | Uncertainty | 2 | 4 | 1 | 7 |
| 24 | Interpretability | 2 | 4 | 1 | 7 |
| 25 | Clinical Risk | 2 | 4 | 1 | 7 |
| 26 | Rare Disease | 2 | 3 | 1 | 6 |
| 27 | Drug Discovery | 1 | 3 | 1 | 5 |
| 28 | Sequence Design | 3 | 3 | 0 | 6 |
| 29 | Ethics & Frontiers | 1 | 4 | 1 | 6 |
| **Total** | | **59** | **80** | **24** | **163** |

---

## Cumulative Book Statistics

| Part | Chapters | Essential | High | Enhancing | Total |
|------|----------|-----------|------|-----------|-------|
| I | 1-4 | 8 | 10 | 4 | 22 |
| II | 5-10 | 12 | 14 | 6 | 32 |
| III | 11-14 | 10 | 8 | 4 | 22 |
| IV | 15-19 | 10 | 14 | 2 | 26 |
| V | 20-24 | 10 | 17 | 4 | 31 |
| VI | 25-29 | 9 | 17 | 4 | 30 |
| **Total** | **29** | **59** | **80** | **24** | **163** |

---

## Cross-Chapter Consistency Notes

1. **Ancestry color scheme**: Establish in Figure 2.2, reuse in Figure 3.5 and throughout the book.
2. **Pipeline iconography**: Establish sequencing/alignment/calling icons in Figure 1.1, reuse when referencing pipeline stages.
3. **Method colors**: Assign consistent colors to CADD, REVEL, ESM, AlphaMissense, etc. for all comparison figures.
4. **Constraint metrics**: Use consistent visualization for pLI/LOEUF across chapters.
5. **Clinical workflow**: The funnel metaphor (Figure 4.1) should echo the pipeline structure (Figure 1.1) to show how variant calling feeds into interpretation.


## Cross-Chapter Consistency Notes

1. **Architecture color scheme**: Establish consistent colors for CNN layers (blue), attention layers (orange), feed-forward layers (green) that persist across Chapters 6-7.

2. **Genomic feature annotations**: Use consistent visual language for promoters, enhancers, TF binding sites, splice sites across all figures.

3. **Scale visualization**: Maintain consistent approach to showing genomic distances (log scale, consistent tick marks at 1kb, 10kb, 100kb, 1Mb).

4. **Model family colors**: Assign consistent colors to model families (DNABERT=blue, Enformer=green, ESM=purple, HyenaDNA=orange) for use in comparison figures.

5. **Attention visualization**: Establish heatmap color scheme for attention weights that will be reused when discussing specific models in Part III.

6. **Clinical relevance callouts**: Use consistent visual element (e.g., stethoscope icon or clinical red) when figures connect to clinical applications.

## Connections to Part I Figures

- Figure 6.2 (Receptive Field Ceiling) should visually echo Figure 1.1 (Pipeline) by using consistent genome representation
- Figure 9.4 (Domain Shift) connects to Figure 2.2 (Ancestry Representation) through the population bias theme
- Figure 8.4 (Multi-Task Pretraining) references data resources from Figure 2.4 (Functional Genomics Matrix)

**Cross-Chapter Visual Consistency for Part III:**
- Model family colors: DNA-LM (blue), Protein-LM (purple), Regulatory (green), Multi-omic (orange)
- Architecture schematics: Consistent layer representations (attention=orange blocks, convolution=blue blocks, FFN=gray)
- Scale annotations: Log scale for parameters (M/B), sequence length (bp/kb/Mb), compute (FLOPs)
- Benchmark visualization: Consistent axis ranges for AUROC (0.5-1.0), correlation (-1 to 1)
- Timeline conventions: Left-to-right chronology, architectural innovations annotated above timeline

**Cross-Chapter Visual Consistency for Part IV:**
- Modality colors: RNA (teal), Single-cell (coral), 3D Genome (indigo), Networks (amber), Multi-omics (gray gradient)
- Data representation: Consistent matrix/heatmap styling for Hi-C, expression, accessibility
- Integration diagrams: Encoder boxes → shared latent space → decoder/classifier heads
- Graph conventions: Nodes as circles with foundation model embeddings indicated, edges as biological relationships
- Scale annotations: Cells (single vs. population), Resolution (kb/Mb), Samples (n)

**Visual consistency for Part V:**
- Color scheme: Use a consistent palette distinguishing concepts:
  - Training/in-distribution: blue tones
  - Test/deployment: green tones
  - Confounders/leakage: red/orange warning tones
  - Uncertainty: purple gradient (low to high)
  - Correct vs. incorrect: green vs. red
- Diagram conventions: DAGs use standard causal inference notation (arrows for causation, boxes for observed, circles for latent)
- Performance visualizations: Consistent axis labeling (AUROC 0-1, calibration 0-1)
- Benchmark representations: Consistent iconography for protein (helix), DNA (double helix), variant (SNP symbol)

**Visual consistency for Part VI:**
- Clinical workflow elements: Use consistent iconography (patient silhouette, EHR screen, clinician, laboratory)
- Translation pipeline: Left-to-right flow from model to clinic
- Risk/benefit: Green (benefit), red (risk), yellow (uncertainty)
- Regulatory: Formal document styling, jurisdiction color coding
- Design cycles: Circular/iterative diagrams with clear iteration arrows

## Visual Consistency Guidelines for Part V

### Color Palette
- **In-distribution/Training:** Blues (#2563eb, #3b82f6)
- **Test/Deployment:** Greens (#16a34a, #22c55e)
- **Confounders/Leakage/Warnings:** Reds/Oranges (#dc2626, #ea580c)
- **Uncertainty gradient:** Purples (#7c3aed low → #c084fc high)
- **Correct/Valid:** Green (#16a34a)
- **Incorrect/Invalid:** Red (#dc2626)

### Diagram Conventions
- **DAGs:** Standard causal inference notation (arrows, boxes for observed, circles for latent)
- **Reliability diagrams:** Always include diagonal reference, histogram of predictions
- **Embedding spaces:** UMAP/t-SNE with consistent styling, cluster labels
- **Workflow diagrams:** Left-to-right flow, numbered steps, consistent box styling

### Annotation Standards
- **Equations:** LaTeX formatting, define all variables
- **Performance metrics:** Always include confidence intervals or ranges
- **Warnings:** Red callout boxes with exclamation icon
- **Key insights:** Bold or highlighted text

### Cross-Chapter Connections
- Fig 21.4 (Leakage taxonomy) connects to Fig 20.4 (Leakage pathways)
- Fig 22.5 (Detecting confounding) implements diagnostics from Ch 21
- Fig 23.2 (Calibration) extends evaluation metrics from Ch 21
- Fig 24.5 (Plausible vs. faithful) addresses validation concerns from Ch 21
- Fig 22.2 (Population structure) explains benchmark gaps in Fig 20.5

## Visual Consistency Guidelines for Part VI

### Color Palette
- **Clinical elements:** Blues (calming, professional)
- **Validation/Evidence:** Greens (verified) to Reds (unvalidated)
- **Risk/Benefit:** Green (benefit), Red (risk), Yellow (uncertain)
- **Regulatory:** Formal grays with jurisdiction-specific accents

### Diagram Conventions
- **Clinical workflows:** Left-to-right patient journey
- **Validation hierarchies:** Pyramid or staircase (bottom = weak, top = strong)
- **Design cycles:** Circular with clear iteration arrows
- **Regulatory comparisons:** Column format for jurisdiction comparison

### Iconography Standards
- **Patient:** Silhouette in clinical blue
- **Clinician:** White coat silhouette
- **Laboratory:** Flask or sequencer icon
- **Model:** Neural network diagram
- **Regulatory:** Document/stamp icon

### Cross-Chapter Connections
- Fig 25.2 (Validation hierarchy) connects to evaluation principles (Ch 21)
- Fig 26.2 (ACMG-AMP) references confounding (Ch 22) for circularity
- Fig 27.4 (Perturb-seq) connects to single-cell models (Ch 11)
- Fig 28.5 (DBTL) connects to interpretability (Ch 24) for model refinement
- Fig 29.1 (Regulatory) references clinical integration (Ch 25)


---

## Part VI Design Notes

Part VI figures face unique challenges as the "translation" section of the book:

1. **Clinical credibility**: Figures must convey that clinical translation requires more than technical achievement; workflow integration, validation evidence, and equity considerations are equally important.

2. **Regulatory complexity**: Jurisdiction-specific details change; figures should convey structure and principles rather than specifics that will become outdated.

3. **Ethical framing**: Dual-use and governance figures should present balanced perspectives without being preachy or dismissive of concerns.

4. **Design excitement**: Sequence design represents the frontier; figures should convey capability without overpromising or underplaying limitations.

5. **Future uncertainty**: Chapter 29 figures should acknowledge open questions without appearing naive about challenges or pessimistic about progress.

These figures complete the pedagogical arc from foundations through applications to clinical impact and societal considerations.
