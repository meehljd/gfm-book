#!/usr/bin/env python3
"""
Figure 3.2: Heritability Decomposition
Nested ring diagram showing variance decomposition for height.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

# Output path
OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_1" / "ch03"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Style settings
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans'],
    'font.size': 10,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
})

# Create figure
fig, ax = plt.subplots(figsize=(10, 8))

# Colors
colors = {
    'genetic': '#1f77b4',
    'environmental': '#2ca02c',
    'additive': '#4292c6',
    'nonadditive': '#9ecae1',
    'snp_h2': '#6baed6',
    'missing': '#c6dbef',
    'gwas_hits': '#08519c',
    'polygenic_gap': '#3182bd',
}

# Helper function for pie wedges
def add_ring(ax, inner_radius, outer_radius, fractions, colors, labels=None, startangle=90):
    """Add a ring (annulus) with segments."""
    width = outer_radius - inner_radius
    wedges = []
    angles = startangle
    for i, (frac, color) in enumerate(zip(fractions, colors)):
        theta1 = angles
        theta2 = angles + frac * 360
        wedge = mpatches.Wedge(
            center=(0, 0),
            r=outer_radius,
            theta1=theta1,
            theta2=theta2,
            width=width,
            facecolor=color,
            edgecolor='white',
            linewidth=2
        )
        ax.add_patch(wedge)
        wedges.append((wedge, (theta1 + theta2) / 2, frac))
        angles = theta2
    return wedges

# Ring 1: Total variance (genetic vs environmental)
fractions1 = [0.80, 0.20]  # 80% genetic, 20% environmental
colors1 = [colors['genetic'], colors['environmental']]
wedges1 = add_ring(ax, 0.7, 1.0, fractions1, colors1)

# Ring 2: Genetic breakdown (additive vs non-additive)
# Narrow-sense h2 is ~0.80, most is additive
fractions2 = [0.75, 0.05, 0.20]  # additive, non-additive, environmental
colors2 = [colors['additive'], colors['nonadditive'], colors['environmental']]
wedges2 = add_ring(ax, 0.45, 0.68, fractions2, colors2)

# Ring 3: SNP-heritability breakdown
# SNP-h2 ~0.55, missing ~0.25, environmental ~0.20
fractions3 = [0.25, 0.30, 0.25, 0.20]  # GWAS hits, polygenic gap, hidden h2, environmental
colors3 = [colors['gwas_hits'], colors['polygenic_gap'], colors['missing'], colors['environmental']]
wedges3 = add_ring(ax, 0.20, 0.43, fractions3, colors3)

ax.set_xlim(-1.3, 1.3)
ax.set_ylim(-1.3, 1.3)
ax.set_aspect('equal')
ax.axis('off')

# Add labels with lines
# Ring 1 labels
ax.annotate('Genetic\n(h² ≈ 80%)', xy=(0.85 * np.cos(np.radians(130)), 0.85 * np.sin(np.radians(130))),
            xytext=(1.15, 0.8), fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='-', color='#333333', lw=1),
            ha='left', color=colors['genetic'])

ax.annotate('Environmental\n(≈ 20%)', xy=(0.85 * np.cos(np.radians(-30)), 0.85 * np.sin(np.radians(-30))),
            xytext=(1.1, -0.3), fontsize=10, fontweight='bold',
            arrowprops=dict(arrowstyle='-', color='#333333', lw=1),
            ha='left', color=colors['environmental'])

# Ring 2 labels
ax.annotate('Additive\n(narrow-sense h²)', xy=(0.55 * np.cos(np.radians(150)), 0.55 * np.sin(np.radians(150))),
            xytext=(-1.2, 0.5), fontsize=9,
            arrowprops=dict(arrowstyle='-', color='#555555', lw=0.8),
            ha='right')

ax.annotate('Non-additive\n(dominance,\nepistasis)', xy=(0.55 * np.cos(np.radians(75)), 0.55 * np.sin(np.radians(75))),
            xytext=(-0.9, 1.0), fontsize=9,
            arrowprops=dict(arrowstyle='-', color='#555555', lw=0.8),
            ha='right')

# Ring 3 labels
ax.annotate('GWAS hits\n(~25%)', xy=(0.32 * np.cos(np.radians(135)), 0.32 * np.sin(np.radians(135))),
            xytext=(-1.15, -0.3), fontsize=9,
            arrowprops=dict(arrowstyle='-', color='#555555', lw=0.8),
            ha='right', color=colors['gwas_hits'])

ax.annotate('Polygenic gap\n(sub-threshold\nvariants)', xy=(0.32 * np.cos(np.radians(90)), 0.32 * np.sin(np.radians(90))),
            xytext=(-1.2, 0.0), fontsize=9,
            arrowprops=dict(arrowstyle='-', color='#555555', lw=0.8),
            ha='right')

ax.annotate('Hidden h²\n(rare variants,\nSVs, poor tagging)', xy=(0.32 * np.cos(np.radians(45)), 0.32 * np.sin(np.radians(45))),
            xytext=(1.1, 0.3), fontsize=9,
            arrowprops=dict(arrowstyle='-', color='#555555', lw=0.8),
            ha='left')

# Center text
ax.text(0, 0, 'Height\nVariance', ha='center', va='center', fontsize=11, fontweight='bold')

# Title
ax.set_title('Decomposition of Phenotypic Variance', fontweight='bold', fontsize=14, pad=20)

# Legend
legend_elements = [
    mpatches.Patch(facecolor=colors['gwas_hits'], edgecolor='white', label='Explained by GWAS hits (~25%)'),
    mpatches.Patch(facecolor=colors['polygenic_gap'], edgecolor='white', label='Polygenic gap (~30%)'),
    mpatches.Patch(facecolor=colors['missing'], edgecolor='white', label='Hidden heritability (~25%)'),
    mpatches.Patch(facecolor=colors['environmental'], edgecolor='white', label='Environmental (~20%)'),
]
ax.legend(handles=legend_elements, loc='lower center', bbox_to_anchor=(0.5, -0.08),
          ncol=2, fontsize=9, frameon=True, framealpha=0.95)

plt.tight_layout()

# Save
output_path = OUTPUT_DIR / '02-fig-heritability-decomposition.svg'
plt.savefig(output_path, format='svg')
print(f"Saved: {output_path}")
plt.close()
