# Figure Style Guide

Style standards for all figures in the GFM Book. All programmatic figures must follow these guidelines.

## Color Palette

### Primary Semantic Colors

| Element | Hex | RGB | Usage |
|---------|-----|-----|-------|
| DNA/Sequence | `#1f77b4` | rgb(31,119,180) | DNA sequences, genomic data, short reads |
| DNA Light | `#aec7e8` | rgb(174,199,232) | DNA backgrounds, secondary DNA elements |
| RNA | `#2ca02c` | rgb(44,160,44) | RNA sequences, transcripts, long reads |
| RNA Light | `#98df8a` | rgb(152,223,138) | RNA backgrounds, success states |
| Protein | `#ff7f0e` | rgb(255,127,14) | Proteins, amino acids, outputs |
| Protein Light | `#ffbb78` | rgb(255,187,120) | Protein backgrounds, highlights |
| Model/Compute | `#9467bd` | rgb(148,103,189) | Neural networks, algorithms, processing |
| Model Light | `#c5b0d5` | rgb(197,176,213) | Model backgrounds |

### Status Colors

| Status | Hex | Usage |
|--------|-----|-------|
| Error/Pathogenic | `#d62728` | Errors, pathogenic variants, failures |
| Warning | `#ff7f0e` | Caution, uncertain |
| Success/Benign | `#2ca02c` | Success, benign variants |
| Neutral | `#7f7f7f` | Neutral, unknown, background |

### Grayscale Alternatives

For print compatibility, every color distinction must also be achievable through:
- **Shape** (rectangle vs oval vs diamond)
- **Pattern** (solid vs hatched vs dotted fill)
- **Line style** (solid vs dashed vs dotted)

## Typography

### Fonts

| Context | Font | Fallback |
|---------|------|----------|
| Labels | Arial | Helvetica, sans-serif |
| Code/Sequence | Courier New | monospace |
| Math | STIX Two Math | serif |

### Font Sizes (in points)

| Element | Size | Weight |
|---------|------|--------|
| Figure title | 14pt | Bold |
| Section labels | 12pt | Bold |
| Primary labels | 11pt | Regular |
| Secondary labels | 10pt | Regular |
| Annotations | 9pt | Italic |
| Minimum readable | 8pt | - |

**Rule**: No text smaller than 8pt. Prefer 10pt minimum for all labels.

## Node Shapes (for Graphviz/flowcharts)

| Concept | Shape | Example |
|---------|-------|---------|
| Data/File | Rectangle with rounded corners | FASTQ, BAM, VCF |
| Process/Algorithm | Rectangle | Alignment, Calling |
| Decision | Diamond | Filter pass? |
| Database/Reference | Cylinder | Reference genome |
| Input/Output | Parallelogram | DNA sample, Results |
| Start/End | Oval/Ellipse | Start, End |

## Layout Principles

### Spacing

- **Minimum node spacing**: 0.5 inches
- **Minimum edge length**: 0.3 inches
- **Margin around figure**: 0.25 inches
- **Text padding inside nodes**: 0.1 inches

### Flow Direction

- **Pipelines/Processes**: Top-to-bottom (TB) or Left-to-right (LR)
- **Hierarchies/Trees**: Top-to-bottom (TB)
- **Timelines**: Left-to-right (LR)
- **Comparisons**: Side-by-side with clear alignment

### Alignment

- **Text in nodes**: Center-aligned
- **Standalone labels**: Left-aligned
- **Numbers/values**: Right-aligned
- **Multiple elements**: Grid-aligned (use subgraphs in Graphviz)

## Graphviz Settings

### Default Graph Attributes

```dot
digraph {
    // Layout
    rankdir=TB          // Top-to-bottom flow
    splines=ortho       // Orthogonal (right-angle) edges
    nodesep=0.5         // Horizontal spacing
    ranksep=0.6         // Vertical spacing

    // Global node style
    node [
        fontname="Arial"
        fontsize=11
        style="filled,rounded"
        fillcolor="#f7f7f7"
        color="#333333"
        penwidth=1.5
        margin="0.15,0.1"
    ]

    // Global edge style
    edge [
        fontname="Arial"
        fontsize=9
        color="#555555"
        penwidth=1.2
        arrowsize=0.8
    ]
}
```

### Node Style Classes

```dot
// Data files (rounded rectangles)
node [shape=box, style="filled,rounded", fillcolor="#aec7e8"]

// Processes (rectangles)
node [shape=box, style=filled, fillcolor="#f0f0f0"]

// Models/Algorithms (purple)
node [shape=box, style=filled, fillcolor="#c5b0d5"]

// Key outputs (green)
node [shape=box, style="filled,rounded", fillcolor="#98df8a"]

// Databases (cylinder approximation - use HTML labels)
node [shape=cylinder, fillcolor="#e0e0e0"]
```

## Matplotlib Settings

### Figure Configuration

```python
import matplotlib.pyplot as plt

# Default figure settings
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans'],
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'axes.labelsize': 11,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.titlesize': 14,
    'figure.titleweight': 'bold',
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.15,
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# Color palette as named constants
COLORS = {
    'dna': '#1f77b4',
    'dna_light': '#aec7e8',
    'rna': '#2ca02c',
    'rna_light': '#98df8a',
    'protein': '#ff7f0e',
    'protein_light': '#ffbb78',
    'model': '#9467bd',
    'model_light': '#c5b0d5',
    'error': '#d62728',
    'success': '#2ca02c',
    'neutral': '#7f7f7f',
    'background': '#f7f7f7',
}
```

### Subplot Guidelines

For complex figures, use subplots rather than cramming everything into one panel:

```python
# Good: Multiple clear subplots
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Main Title', fontsize=14, fontweight='bold')

# Add panel labels
for ax, label in zip(axes.flat, ['A', 'B', 'C', 'D']):
    ax.text(-0.1, 1.05, label, transform=ax.transAxes,
            fontsize=14, fontweight='bold', va='top')
```

## Figure Types and Tools

| Type | Primary Tool | When to Use |
|------|--------------|-------------|
| Pipeline/Flowchart | Graphviz | Process flows, data pipelines |
| Hierarchy/Tree | Graphviz | Taxonomies, error categories |
| Network/Graph | Graphviz | Gene networks, relationships |
| Heatmap | Matplotlib | Attention matrices, expression |
| Bar/Line Chart | Matplotlib | Quantitative comparisons |
| Schematic | Matplotlib subplots | Complex concepts split into parts |
| Sequence | Matplotlib | DNA/RNA/protein sequences |
| Chromosome | Matplotlib | Ideograms, genomic regions |

## Anti-Patterns to Avoid

### Layout
- ❌ Overlapping text or elements
- ❌ Inconsistent spacing
- ❌ Text smaller than 8pt
- ❌ Crowded single-panel figures

### Color
- ❌ Relying solely on color to convey meaning
- ❌ Red/green combinations without alternatives
- ❌ Low-contrast color combinations
- ❌ More than 6-7 distinct colors in one figure

### Content
- ❌ Chartjunk (unnecessary decoration)
- ❌ 3D effects on 2D data
- ❌ Multiple competing focal points
- ❌ Missing legends or labels

## Quality Checklist

Before finalizing any figure:

1. [ ] All text ≥8pt (preferably ≥10pt)
2. [ ] No overlapping elements
3. [ ] Clear visual hierarchy
4. [ ] Follows semantic color palette
5. [ ] Works in grayscale (shape/pattern backup)
6. [ ] Consistent with other book figures
7. [ ] Caption is self-contained
8. [ ] Referenced in chapter text
