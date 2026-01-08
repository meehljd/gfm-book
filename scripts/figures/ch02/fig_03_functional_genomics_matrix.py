#!/usr/bin/env python3
"""
Figure 2.3: Functional Genomics Coverage Matrix
Heatmap showing ENCODE/Roadmap data availability across cell types and assays.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

# Output path
OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_1" / "ch02"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Style settings
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans'],
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.titleweight': 'bold',
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# Cell types (rows) - mix of well-covered and sparse
cell_types = [
    'K562 (Tier 1)',
    'GM12878 (Tier 1)',
    'HepG2 (Tier 1)',
    'H1-hESC',
    'HUVEC',
    'IMR90',
    'A549',
    'MCF-7',
    'Primary Brain',
    'Primary Heart',
    'Primary Liver',
    'Pancreatic Islets',
    'Primary Muscle',
    'Primary Kidney',
    'Adipose Tissue',
]

# Assay types (columns)
assays = [
    'DNase-seq',
    'ATAC-seq',
    'H3K4me3',
    'H3K27ac',
    'H3K4me1',
    'H3K27me3',
    'CTCF',
    'RNA-seq',
    'ChIP-seq\n(TFs)',
    'Hi-C',
]

# Coverage data (0-4 scale: 0=none, 1=minimal, 2=moderate, 3=good, 4=comprehensive)
# Tier 1 cell lines have best coverage
coverage = np.array([
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # K562
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # GM12878
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 3],  # HepG2
    [4, 3, 4, 4, 4, 4, 4, 4, 3, 3],  # H1-hESC
    [3, 3, 3, 3, 3, 3, 3, 4, 2, 2],  # HUVEC
    [3, 2, 3, 3, 3, 3, 3, 3, 2, 2],  # IMR90
    [3, 3, 3, 3, 3, 3, 3, 3, 2, 1],  # A549
    [3, 2, 3, 3, 3, 3, 2, 3, 2, 1],  # MCF-7
    [2, 2, 2, 2, 2, 2, 1, 3, 1, 2],  # Primary Brain
    [2, 2, 2, 2, 2, 2, 1, 3, 1, 1],  # Primary Heart
    [2, 2, 2, 2, 2, 2, 1, 3, 1, 1],  # Primary Liver
    [1, 1, 1, 2, 1, 1, 0, 2, 0, 0],  # Pancreatic Islets
    [2, 1, 2, 2, 2, 2, 1, 2, 1, 1],  # Primary Muscle
    [2, 1, 2, 2, 2, 2, 1, 2, 1, 0],  # Primary Kidney
    [1, 1, 2, 2, 2, 2, 1, 2, 0, 0],  # Adipose
])

# Create figure
fig, ax = plt.subplots(figsize=(10, 8))

# Custom colormap: white to dark blue
from matplotlib.colors import LinearSegmentedColormap
colors_cmap = ['#ffffff', '#d4e6f1', '#7fb3d5', '#2980b9', '#1a5276']
cmap = LinearSegmentedColormap.from_list('coverage', colors_cmap, N=5)

# Plot heatmap
im = ax.imshow(coverage, cmap=cmap, aspect='auto', vmin=0, vmax=4)

# Set ticks
ax.set_xticks(np.arange(len(assays)))
ax.set_yticks(np.arange(len(cell_types)))
ax.set_xticklabels(assays)
ax.set_yticklabels(cell_types)

# Rotate x labels
plt.setp(ax.get_xticklabels(), rotation=45, ha='right', rotation_mode='anchor')

# Add gridlines
ax.set_xticks(np.arange(len(assays)+1)-0.5, minor=True)
ax.set_yticks(np.arange(len(cell_types)+1)-0.5, minor=True)
ax.grid(which='minor', color='white', linestyle='-', linewidth=2)
ax.tick_params(which='minor', bottom=False, left=False)

# Add horizontal line separating Tier 1 from others
ax.axhline(y=2.5, color='#d62728', linewidth=2, linestyle='--')
ax.text(len(assays)-0.3, 1.5, 'Tier 1\nCell Lines', fontsize=8, ha='left', va='center', color='#d62728', fontweight='bold')

# Add horizontal line separating cell lines from primary tissues
ax.axhline(y=7.5, color='#555555', linewidth=1.5, linestyle=':')
ax.text(len(assays)-0.3, 6.5, 'Cell Lines', fontsize=8, ha='left', va='center', color='#555555')
ax.text(len(assays)-0.3, 11, 'Primary\nTissues', fontsize=8, ha='left', va='center', color='#555555')

# Colorbar
cbar = plt.colorbar(im, ax=ax, shrink=0.6, aspect=20, pad=0.15)
cbar.set_ticks([0, 1, 2, 3, 4])
cbar.set_ticklabels(['None', 'Minimal', 'Moderate', 'Good', 'Comprehensive'])
cbar.ax.set_ylabel('Data Availability', fontweight='bold')

# Title
ax.set_title('ENCODE/Roadmap Functional Genomics Coverage', fontweight='bold', pad=15)

# Labels
ax.set_xlabel('Assay Type', fontweight='bold')
ax.set_ylabel('Cell Type / Tissue', fontweight='bold')

plt.tight_layout()

# Save
output_path = OUTPUT_DIR / '03-fig-functional-genomics-matrix.svg'
plt.savefig(output_path, format='svg')
print(f"Saved: {output_path}")
plt.close()
