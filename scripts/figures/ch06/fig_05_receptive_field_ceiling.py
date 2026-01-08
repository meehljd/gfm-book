#!/usr/bin/env python3
"""
Figure 6.5: Receptive Field Ceiling
Shows the limitation of convolutional receptive fields for long-range interactions.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_2" / "ch06"
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
    'axes.spines.top': False,
    'axes.spines.right': False,
})

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Panel 1: Receptive field growth
ax = axes[0]

layers = np.arange(1, 11)

# Standard CNN
standard_rf = layers * 3  # Each layer adds ~3 positions

# Dilated CNN
dilated_rf = 3 * (2 ** layers - 1)  # Exponential growth

ax.plot(layers, standard_rf, 'o-', color='#1f77b4', linewidth=2, markersize=6, label='Standard Conv')
ax.plot(layers, dilated_rf, 's-', color='#d62728', linewidth=2, markersize=6, label='Dilated Conv')

# Add horizontal lines for biological context
ax.axhline(y=1000, color='#2ca02c', linestyle='--', linewidth=1, alpha=0.7)
ax.text(10.2, 1000, 'Typical promoter window', fontsize=8, va='center', color='#2ca02c')

ax.axhline(y=10000, color='#ff7f0e', linestyle='--', linewidth=1, alpha=0.7)
ax.text(10.2, 10000, 'Enhancer-promoter interactions', fontsize=8, va='center', color='#ff7f0e')

ax.set_xlabel('Number of Layers', fontweight='bold')
ax.set_ylabel('Receptive Field (bp)', fontweight='bold')
ax.set_yscale('log')
ax.set_xlim(0.5, 12)
ax.set_ylim(1, 50000)
ax.legend(loc='upper left', fontsize=9)
ax.set_title('Receptive Field Growth', fontweight='bold')

# Panel 2: Long-range interaction illustration
ax = axes[1]

# Draw genomic region
ax.fill_between([0, 10], 1.8, 2.2, color='#aec7e8', alpha=0.5)
ax.text(5, 2.5, 'Genomic Region (10kb)', ha='center', fontsize=10, fontweight='bold')

# Enhancer and promoter
ax.add_patch(mpatches.FancyBboxPatch((0.5, 1.85), 0.8, 0.3,
                                      boxstyle='round,pad=0.02',
                                      facecolor='#ff7f0e', edgecolor='#333333', linewidth=1.5))
ax.text(0.9, 2, 'Enhancer', ha='center', va='center', fontsize=8, color='white')

ax.add_patch(mpatches.FancyBboxPatch((8.5, 1.85), 1, 0.3,
                                      boxstyle='round,pad=0.02',
                                      facecolor='#2ca02c', edgecolor='#333333', linewidth=1.5))
ax.text(9, 2, 'Promoter', ha='center', va='center', fontsize=8, color='white')

# Long-range interaction arc
arc = mpatches.FancyArrowPatch((0.9, 2.2), (9, 2.2),
                                 connectionstyle='arc3,rad=-0.5',
                                 arrowstyle='<->',
                                 color='#d62728', linewidth=2,
                                 mutation_scale=10)
ax.add_patch(arc)
ax.text(5, 3.2, 'Long-range interaction\n(8kb distance)', ha='center', fontsize=9, color='#d62728')

# CNN receptive field
ax.add_patch(mpatches.FancyBboxPatch((3.5, 0.8), 3, 0.5,
                                      boxstyle='round,pad=0.02',
                                      facecolor='#1f77b4', alpha=0.3,
                                      edgecolor='#1f77b4', linewidth=2, linestyle='--'))
ax.text(5, 1.05, 'Typical CNN\nReceptive Field\n(~1-2kb)', ha='center', va='center', fontsize=8)

ax.set_xlim(-0.5, 11)
ax.set_ylim(0.5, 3.8)
ax.axis('off')
ax.set_title('CNNs Miss Long-Range Interactions', fontweight='bold')

plt.tight_layout()
output_path = OUTPUT_DIR / '05-fig-receptive-field-ceiling.svg'
plt.savefig(output_path, format='svg')
print(f"Saved: {output_path}")
plt.close()
