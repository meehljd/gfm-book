#!/usr/bin/env python3
"""
Figure 7.2: Multi-Head Attention
Shows how multiple heads capture diverse relationships.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_2" / "ch07"
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

fig, ax = plt.subplots(figsize=(10, 5))

n_heads = 4
head_colors = ['#d62728', '#2ca02c', '#1f77b4', '#ff7f0e']
head_labels = ['Local patterns', 'GC content', 'Splice signals', 'TF motifs']

# Draw heads
for i in range(n_heads):
    x = i * 2.2 + 0.5
    y = 2

    # Head box
    ax.add_patch(mpatches.FancyBboxPatch((x, y), 1.5, 1.2,
                                          boxstyle='round,pad=0.02',
                                          facecolor=head_colors[i], alpha=0.3,
                                          edgecolor=head_colors[i], linewidth=2))
    ax.text(x + 0.75, y + 0.9, f'Head {i+1}', ha='center', va='center',
            fontsize=10, fontweight='bold')
    ax.text(x + 0.75, y + 0.4, head_labels[i], ha='center', va='center',
            fontsize=8, style='italic')

# Input
ax.add_patch(mpatches.FancyBboxPatch((3.5, 3.8), 2, 0.6,
                                      boxstyle='round,pad=0.02',
                                      facecolor='#aec7e8', edgecolor='#1f77b4', linewidth=1.5))
ax.text(4.5, 4.1, 'Input X', ha='center', va='center', fontsize=11)

# Arrows from input to heads
for i in range(n_heads):
    x = i * 2.2 + 1.25
    ax.annotate('', xy=(x, 3.2), xytext=(4.5, 3.7),
                arrowprops=dict(arrowstyle='->', color='#555555', lw=1))

# Concatenation
ax.add_patch(mpatches.FancyBboxPatch((3, 0.5), 3, 0.8,
                                      boxstyle='round,pad=0.02',
                                      facecolor='#c5b0d5', edgecolor='#9467bd', linewidth=1.5))
ax.text(4.5, 0.9, 'Concat + Linear', ha='center', va='center', fontsize=10)

# Arrows from heads to concat
for i in range(n_heads):
    x = i * 2.2 + 1.25
    ax.annotate('', xy=(4.5, 1.4), xytext=(x, 2),
                arrowprops=dict(arrowstyle='->', color='#555555', lw=1))

# Output
ax.add_patch(mpatches.FancyBboxPatch((3.5, -0.5), 2, 0.6,
                                      boxstyle='round,pad=0.02',
                                      facecolor='#98df8a', edgecolor='#2ca02c', linewidth=1.5))
ax.text(4.5, -0.2, 'Output', ha='center', va='center', fontsize=11)

ax.annotate('', xy=(4.5, 0), xytext=(4.5, 0.4),
            arrowprops=dict(arrowstyle='->', color='#555555', lw=1))

ax.text(4.5, -1, 'Multiple heads enable diverse biological relationships in parallel',
        ha='center', fontsize=10, style='italic')

ax.set_xlim(-0.5, 9.5)
ax.set_ylim(-1.3, 4.8)
ax.axis('off')
ax.set_title('Multi-Head Attention Captures Diverse Biological Relationships', fontweight='bold')

plt.tight_layout()
output_path = OUTPUT_DIR / '02-fig-multihead-attention.svg'
plt.savefig(output_path, format='svg')
print(f"Saved: {output_path}")
plt.close()
