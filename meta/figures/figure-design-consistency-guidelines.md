# Comprehensive Design and Consistency Guidelines

This document consolidates all design notes, cross-chapter consistency requirements, and visual standards for figures across *Genomic Foundation Models*.

---

## Global Visual Consistency Standards

### Core Color Palette

**By Domain:**
- **Genomics/DNA:** Blues (#2563eb, #3b82f6)
- **Proteins:** Purples (#7c3aed, #a855f7)
- **RNA:** Teals (#0891b2, #22d3d3)
- **Clinical/Application:** Greens (#16a34a, #22c55e)

**By Evaluation Context:**
- **Training/In-distribution:** Blues
- **Test/Deployment:** Greens
- **Confounders/Leakage/Warnings:** Reds/Oranges (#dc2626, #ea580c)
- **Uncertainty gradient:** Purples (low → high: #7c3aed → #c084fc)
- **Correct/Valid:** Green (#16a34a)
- **Incorrect/Invalid:** Red (#dc2626)

**By Model Family (Part III+):**
- **DNA Language Models:** Blue
- **Protein Language Models:** Purple
- **Regulatory/Sequence-to-Function:** Green
- **Multi-Omic:** Orange
- **Single-Cell:** Coral
- **3D Genome:** Indigo
- **Networks/Graphs:** Amber

### Ancestry Color Scheme
Establish in Figure 2.2 (Ancestry Representation) and reuse throughout:
- Consistent colors for continental ancestry groups
- Use in Figures 3.5 (PGS portability), 20.5 (cross-population benchmarks), 22.2 (population structure), 25.5 (fairness assessment)
- Consider: European (blue), African (orange), East Asian (green), South Asian (purple), Admixed (gray)

### Method/Model Colors
Assign consistent colors to specific methods for all comparison figures:
- CADD: Color A
- REVEL: Color B
- ESM: Color C
- AlphaMissense: Color D
- SpliceAI: Color E
- Enformer: Color F
- DNABERT: Color G

---

## Architecture Diagram Standards

### Layer Representations
- **Attention layers:** Orange blocks
- **Convolution layers:** Blue blocks
- **Feed-forward layers:** Gray blocks
- **Embedding layers:** Green blocks
- **Output/Task heads:** Colored by task type

### Dimension Annotations
- Always annotate tensor dimensions at each stage
- Format: (batch, sequence_length, hidden_dim) or simplified (L, D)
- Use consistent notation throughout book

### Connection Styles
- **Main data flow:** Solid arrows
- **Skip/Residual connections:** Dashed arrows
- **Attention connections:** Dotted or curved arrows
- **Leakage/spurious paths:** Red dashed arrows

---

## Genomic Feature Visualization

### Consistent Iconography
- **DNA/Genome:** Double helix icon
- **Protein:** Alpha helix icon
- **Variant:** SNP symbol (triangle or star)
- **Gene:** Arrow/box representation
- **Regulatory element:** Enhancer (curved arrow), Promoter (arrow at gene start)
- **Patient:** Silhouette in clinical blue
- **Clinician:** White coat silhouette
- **Laboratory:** Flask or sequencer icon

### Genomic Scale Annotations
- Use log scale for genomic distances
- Consistent tick marks at: 1bp, 10bp, 100bp, 1kb, 10kb, 100kb, 1Mb, 10Mb, 100Mb
- Annotate biologically relevant distances:
  - TF binding site: ~10-20bp
  - Promoter: ~1kb
  - Gene body: ~10-50kb
  - Enhancer-promoter: ~20-200kb
  - TAD: ~100kb-1Mb
  - Chromosome arm: ~100Mb

### Gene/Regulatory Element Colors
- **Exon:** Red or dark
- **Intron:** Blue or light
- **UTR:** Green
- **Promoter:** Orange
- **Enhancer:** Yellow/gold
- **Silencer:** Purple
- **CTCF/Insulator:** Gray

---

## Performance Visualization Standards

### Benchmark Plots
- **AUROC:** Always use 0.5-1.0 range (not 0-1)
- **Correlation:** Use -1 to 1 range
- **Include confidence intervals** where available
- **Annotate operating points** at clinically relevant thresholds

### Reliability Diagrams
- Always include diagonal reference line
- Include histogram of predictions at bottom
- Use consistent bin sizes
- Annotate ECE values

### ROC/PR Curves
- Include random baseline (diagonal for ROC, prevalence for PR)
- Annotate AUC/AUPRC values
- Mark operating points with specific thresholds

### Heatmaps
- Use diverging color scales for correlation matrices
- Use sequential scales for magnitude comparisons
- Include color bars with clear labels

---

## Data Structure Visualization

### Matrix Representations
- **Hi-C:** Triangular heatmap with log color scale
- **Expression:** Gene × Cell with sparse visualization
- **Attention:** Position × Position with softmax normalization indicated

### Network/Graph Standards
- **Node shapes:** Circles for entities, squares for observed variables
- **Node colors:** By type (gene, disease, drug, pathway)
- **Edge styles:** Solid for known relationships, dashed for predicted
- **Edge thickness:** Proportional to confidence/strength

### Embedding Space Visualizations
- **Use UMAP or t-SNE** consistently (note which)
- **Color coding:** By biological category (cell type, gene family, etc.)
- **Cluster labels:** Add where meaningful clusters exist
- **Include legend** explaining coloring

---

## Workflow and Pipeline Diagrams

### Flow Direction
- **Temporal/Sequential:** Left to right
- **Hierarchical:** Top to bottom
- **Clinical journey:** Left to right (patient → outcome)
- **Iterative cycles:** Circular with clear direction arrows

### Step Numbering
- Use numbered circles for sequential steps
- Consistent styling for decision nodes (diamonds)
- Terminal nodes with distinct styling

### Cost/Time Annotations
- Include compute cost where relevant
- Include wall-clock time estimates
- Note data requirements at each stage

---

## Part-Specific Guidelines

### Part I (Foundations)
**Key figures to connect:**
- Pipeline iconography from Figure 1.1 reused when referencing pipeline stages
- Ancestry scheme from Figure 2.2 used in GWAS portability (Figure 3.5)
- Funnel metaphor in Figure 4.1 should echo pipeline structure

**Design priorities:**
- Establish foundational visual vocabulary
- Ground abstract concepts in specific clinical examples
- Make numbers and scale visually dramatic

### Part II (Architectures)
**Key figures to connect:**
- Architecture color scheme (attention=orange, conv=blue, FFN=gray) persists through Chapters 6-7
- Attention visualization scheme established in Chapter 7 reused for specific models later
- Scale visualizations consistent across receptive field comparisons

**Design priorities:**
- Clear tensor dimension annotations
- Show information flow explicitly
- Connect architectural choices to biological consequences

### Part III (Foundation Model Families)
**Key figures to connect:**
- Model family colors (DNA-LM=blue, Protein-LM=purple, Regulatory=green, Multi-omic=orange)
- Timeline conventions (left-to-right chronology, innovations annotated above)
- Benchmark visualization with consistent axis ranges

**Design priorities:**
- Make paradigm shifts visually striking
- Show emergent capabilities clearly
- Connect to clinical applications throughout

### Part IV (Beyond Sequence)
**Key figures to connect:**
- Modality colors (RNA=teal, Single-cell=coral, 3D Genome=indigo, Networks=amber, Multi-omics=gray gradient)
- Integration diagrams use consistent encoder → shared space → head structure
- Graph conventions consistent with Part III

**Design priorities:**
- Show data structures clearly (matrices, graphs, hierarchies)
- Emphasize integration and complementarity
- Connect to clinical utility

### Part V (Evaluation and Interpretation)
**Key figures to connect:**
- Evaluation color scheme (training=blue, test=green, warnings=red/orange)
- Calibration diagram styling consistent throughout
- DAG notation standard for causal inference

**Design priorities:**
- Make abstract confounding concepts concrete
- Validation tests clearly visualized
- Warning callouts prominent

### Part VI (Clinical Translation)
**Key figures to connect:**
- Clinical workflow elements with consistent iconography
- Translation pipeline left-to-right
- Risk/benefit coloring (green=benefit, red=risk, yellow=uncertain)
- Regulatory styling formal and jurisdiction-specific

**Design priorities:**
- Clinical credibility through careful representation
- Regulatory complexity without getting outdated
- Balanced ethical framing

---

## Cross-Part Figure Connections

### Visual Echoes and References

**Part I → Part III:**
- Figure 1.1 (Pipeline) iconography reused when discussing where DL enters pipeline
- Figure 2.2 (Ancestry) scheme reused in Part III benchmark discussions
- Figure 4.1 (Funnel) structure echoed in clinical workflows

**Part II → Part III:**
- Figure 6.2 (Receptive Field) echoes Figure 1.1 genome representation
- Chapter 7 attention patterns form basis for model-specific attention in Part III
- Figure 8.4 (Multi-Task) references data resources from Figure 2.4

**Part III → Part IV:**
- Figure 13.5 (Missing 3D) motivates Chapter 17 (3D genome)
- Foundation model embeddings shown feeding into GNNs (Figure 18.1)

**Part III → Part V:**
- Benchmark figures in Part V use same model colors as Part III
- Uncertainty methods from Part III elaborated in Chapter 23

**Part IV → Part VI:**
- Figure 17.4 (TAD disruption) motivates rare disease SV interpretation
- Figure 18.4 (Disease gene prioritization) supports drug discovery
- Figure 19.5 (Clinical integration) sets up clinical risk prediction

**Part V → Part VI:**
- Evaluation principles from Part V applied in clinical validation hierarchies
- Confounding concerns inform fairness assessment
- Uncertainty quantification integrated into clinical decision support

---

## Figure Creation Checklist

Before finalizing any figure:

### Content
- [ ] Does the figure convey the key insight clearly?
- [ ] Are all necessary annotations included?
- [ ] Is the visual hierarchy appropriate?
- [ ] Are clinical/biological examples specific (gene names, numbers)?

### Consistency
- [ ] Colors match established scheme for this domain/part?
- [ ] Icons match established iconography?
- [ ] Scale annotations follow conventions?
- [ ] Dimension annotations follow format?

### Accessibility
- [ ] Distinguishable without color alone (patterns, labels)?
- [ ] Sufficient contrast?
- [ ] Legend complete and clear?
- [ ] Figure can be understood in black and white?

### Integration
- [ ] Cross-references to related figures noted?
- [ ] Visual echoes to earlier figures where appropriate?
- [ ] Consistent with figures in same chapter?

---

## Design Notes by Figure Type

### Comparison Figures
- Use side-by-side or overlaid layouts
- Highlight differences explicitly
- Include quantitative comparisons where possible
- Annotate "winner" or trade-offs clearly

### Pipeline/Workflow Figures
- Number steps clearly
- Show data types/formats at transitions
- Include timing/cost annotations
- Highlight decision points

### Anatomy/Mechanism Figures
- Step-by-step progression
- Mathematical notation alongside intuitive visualization
- Concrete examples (specific genes, variants)
- Scale bars where spatial

### Performance Figures
- Include baselines and reference lines
- Confidence intervals where available
- Stratification by relevant categories
- Annotation of clinically relevant thresholds

### Conceptual Figures
- Balance abstraction with concrete examples
- Use metaphors carefully (establish once, reuse)
- Highlight the key insight prominently
- Avoid excessive decoration

---

## Notes on Clinical Figures (Part VI)

### Clinical Credibility
- Workflow integration requires more than technical achievement
- Show validation evidence, not just prediction accuracy
- Equity considerations must be prominent

### Regulatory Complexity
- Focus on structure and principles, not specifics that will change
- Note that landscape is evolving
- Early engagement recommended

### Ethical Framing
- Present balanced perspectives
- Neither preachy nor dismissive of concerns
- Acknowledge open questions honestly

### Design Frontier
- Convey capability without overpromising
- Show iterative nature of development
- Connect to experimental validation

---

## Implementation Priority Summary

### Essential Figures (58)
Create first; chapters feel incomplete without them.

### High Priority (82)
Create for complete coverage; significantly aid comprehension.

### Enhancing (20)
Create if time permits; helpful but not critical; consider for online-only.

---

## Production Notes

### File Formats
- Vector formats (SVG, PDF) preferred for print
- Consider separate web-optimized versions
- Include source files for future updates

### Figure Sizing
- Full-width for complex architectures
- Half-width for simple comparisons
- Panel layouts for multi-part figures
- Consider fold-out for very complex figures (Figure 20.1 Benchmark Landscape)

### Caption Guidelines
- State the main insight first
- Include relevant cross-references
- Note data sources where applicable
- Keep brief but complete

### Update Considerations
- Design figures to be updateable as field evolves
- Note where specific numbers may change
- Avoid dates where possible (use relative timing)
- Maintain source files and documentation
