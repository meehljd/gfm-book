#!/usr/bin/env python3
"""
Figure 8.4: Cross-Species Contrastive Learning
Shows how orthologs from different species are used for contrastive pretraining.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_2" / "ch08"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans'],
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.titleweight': 'bold',
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
})

fig, ax = plt.subplots(figsize=(9, 5))

# Species
species = ['Human', 'Mouse', 'Dog', 'Chicken']
colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#d62728']

# Draw embedding space
np.random.seed(42)

# Central cluster for orthologous gene
for i, (sp, color) in enumerate(zip(species, colors)):
    angle = i * np.pi / 2 + np.pi / 4
    x = 3 + 0.8 * np.cos(angle)
    y = 2 + 0.8 * np.sin(angle)

    ax.add_patch(mpatches.Circle((x, y), 0.3, facecolor=color, alpha=0.7, edgecolor='white', linewidth=2))
    ax.text(x, y, sp[:2], ha='center', va='center', fontsize=10, fontweight='bold', color='white')

# Lines connecting orthologs
for i in range(len(species)):
    for j in range(i + 1, len(species)):
        angle_i = i * np.pi / 2 + np.pi / 4
        angle_j = j * np.pi / 2 + np.pi / 4
        x_i = 3 + 0.8 * np.cos(angle_i)
        y_i = 2 + 0.8 * np.sin(angle_i)
        x_j = 3 + 0.8 * np.cos(angle_j)
        y_j = 2 + 0.8 * np.sin(angle_j)
        ax.plot([x_i, x_j], [y_i, y_j], 'k-', linewidth=1, alpha=0.3)

# Label the ortholog cluster
ax.text(3, 0.7, 'Gene X orthologs\n(pulled together)', ha='center', fontsize=10, fontweight='bold')

# Non-ortholog (pushed away)
ax.add_patch(mpatches.Circle((6, 3.5), 0.3, facecolor='#7f7f7f', alpha=0.5, edgecolor='#333333', linewidth=1))
ax.text(6, 3.5, '?', ha='center', va='center', fontsize=12, color='white')
ax.text(6.5, 3.5, 'Non-ortholog\n(pushed away)', ha='left', fontsize=9)

# Push arrow
ax.annotate('', xy=(5.7, 3.3), xytext=(4.2, 2.5),
            arrowprops=dict(arrowstyle='->', color='#d62728', lw=2))

# Another ortholog cluster
for i, (sp, color) in enumerate(zip(species[:3], colors[:3])):
    angle = i * 2 * np.pi / 3
    x = 7 + 0.6 * np.cos(angle)
    y = 1.5 + 0.6 * np.sin(angle)
    ax.add_patch(mpatches.Circle((x, y), 0.25, facecolor=color, alpha=0.5, edgecolor='white', linewidth=1))

ax.text(7, 0.5, 'Gene Y orthologs', ha='center', fontsize=9)

# Title and explanation
ax.text(4.5, 4.3, 'Cross-Species Contrastive Learning', ha='center', fontsize=12, fontweight='bold')
ax.text(4.5, 3.9, 'Orthologs share function → similar embeddings', ha='center', fontsize=10, style='italic')

ax.set_xlim(0, 9)
ax.set_ylim(0, 4.6)
ax.axis('off')

plt.tight_layout()
output_path = OUTPUT_DIR / '04-fig-cross-species-contrastive.svg'
plt.savefig(output_path, format='svg')
print(f"Saved: {output_path}")
plt.close()
