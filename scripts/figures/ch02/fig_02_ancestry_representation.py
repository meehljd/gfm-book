#!/usr/bin/env python3
"""
Figure 2.2: Ancestry Representation Disparity
Stacked bar chart showing ancestry proportions across major genomic resources.
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
    'legend.fontsize': 9,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# Color palette for ancestry groups (colorblind-safe)
ANCESTRY_COLORS = {
    'European': '#1f77b4',      # Blue
    'East Asian': '#ff7f0e',    # Orange
    'African': '#2ca02c',       # Green
    'South Asian': '#d62728',   # Red
    'Hispanic/Latino': '#9467bd', # Purple
    'Other/Mixed': '#7f7f7f',   # Gray
}

# Data: Ancestry proportions (approximate, based on published literature)
# Sources: Martin et al. 2019, Sirugo et al. 2019
resources = [
    'Global\nPopulation',
    'GWAS\nCatalog',
    'gnomAD\nv4',
    'UK\nBiobank',
    'ClinVar\nSubmissions',
    'GTEx\nv8',
]

# Proportions for each ancestry (rows) across resources (columns)
# Order: European, East Asian, African, South Asian, Hispanic, Other
data = np.array([
    [16, 78, 54, 94, 72, 85],   # European
    [22, 10, 25, 2, 5, 5],      # East Asian
    [17, 3, 9, 2, 8, 5],        # African
    [26, 2, 6, 1, 3, 2],        # South Asian
    [9, 4, 4, 1, 8, 2],         # Hispanic/Latino
    [10, 3, 2, 0, 4, 1],        # Other/Mixed
])

ancestries = list(ANCESTRY_COLORS.keys())
colors = list(ANCESTRY_COLORS.values())

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Create stacked bars
x = np.arange(len(resources))
width = 0.7
bottom = np.zeros(len(resources))

bars = []
for i, (ancestry, color) in enumerate(zip(ancestries, colors)):
    bar = ax.bar(x, data[i], width, bottom=bottom, label=ancestry, color=color, edgecolor='white', linewidth=0.5)
    bars.append(bar)
    bottom += data[i]

# Customize
ax.set_ylabel('Percentage of Samples', fontweight='bold')
ax.set_xlabel('')
ax.set_xticks(x)
ax.set_xticklabels(resources)
ax.set_ylim(0, 105)
ax.set_yticks([0, 25, 50, 75, 100])

# Add a reference line at global population proportions
ax.axhline(y=16, color=ANCESTRY_COLORS['European'], linestyle='--', alpha=0.5, linewidth=1)
ax.text(len(resources)-0.5, 18, 'Global European %', fontsize=8, color=ANCESTRY_COLORS['European'], alpha=0.7, ha='right')

# Legend
ax.legend(loc='upper right', frameon=True, framealpha=0.95, ncol=2, fontsize=8)

# Title
ax.set_title('Ancestry Representation Across Genomic Resources', fontweight='bold', pad=10)

# Add annotation
ax.annotate(
    'European ancestry comprises ~16% of\nglobal population but ~78% of GWAS',
    xy=(1, 78), xytext=(2.5, 55),
    fontsize=8, ha='center',
    arrowprops=dict(arrowstyle='->', color='#555555', lw=1),
    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#cccccc', alpha=0.9)
)

plt.tight_layout()

# Save
output_path = OUTPUT_DIR / '02-fig-ancestry-representation.svg'
plt.savefig(output_path, format='svg')
print(f"Saved: {output_path}")
plt.close()
