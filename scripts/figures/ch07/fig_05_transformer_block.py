#!/usr/bin/env python3
"""
Figure 7.5: Transformer Block Architecture
Shows the pre-norm transformer block structure.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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

fig, ax = plt.subplots(figsize=(6, 8))

# Block components (bottom to top)
components = [
    ('Input', 0, '#aec7e8'),
    ('LayerNorm', 1, '#98df8a'),
    ('Multi-Head\nAttention', 2, '#1f77b4'),
    ('Add (Residual)', 3, '#ffbb78'),
    ('LayerNorm', 4, '#98df8a'),
    ('FFN', 5, '#9467bd'),
    ('Add (Residual)', 6, '#ffbb78'),
    ('Output', 7, '#aec7e8'),
]

for label, pos, color in components:
    y = pos * 0.9 + 0.5
    ax.add_patch(mpatches.FancyBboxPatch((1.5, y), 2, 0.6,
                                          boxstyle='round,pad=0.02',
                                          facecolor=color, alpha=0.7 if 'Add' not in label else 0.5,
                                          edgecolor='#333333', linewidth=1.5))
    ax.text(2.5, y + 0.3, label, ha='center', va='center', fontsize=10,
            fontweight='bold' if label in ['Input', 'Output'] else 'normal')

    if pos < 7:
        ax.annotate('', xy=(2.5, y + 0.7), xytext=(2.5, y + 0.6),
                    arrowprops=dict(arrowstyle='->', color='#555555', lw=1))

# Residual connections
# First residual (around attention)
ax.annotate('', xy=(4, 3.35), xytext=(4, 0.8),
            arrowprops=dict(arrowstyle='->', color='#d62728', lw=2,
                           connectionstyle='arc3,rad=0.3'))
ax.text(4.6, 2, 'Skip', ha='left', fontsize=9, color='#d62728')

# Second residual (around FFN)
ax.annotate('', xy=(4, 6.05), xytext=(4, 3.5),
            arrowprops=dict(arrowstyle='->', color='#d62728', lw=2,
                           connectionstyle='arc3,rad=0.3'))
ax.text(4.6, 4.7, 'Skip', ha='left', fontsize=9, color='#d62728')

# Add symbols in Add blocks
ax.text(2.5, 3.35, '+', ha='center', va='center', fontsize=14, fontweight='bold')
ax.text(2.5, 6.05, '+', ha='center', va='center', fontsize=14, fontweight='bold')

ax.text(2.5, 7.8, 'Pre-Norm Transformer Block', ha='center', fontsize=11, fontweight='bold')

ax.set_xlim(0, 5.5)
ax.set_ylim(0, 8.2)
ax.axis('off')

plt.tight_layout()
output_path = OUTPUT_DIR / '05-fig-transformer-block.svg'
plt.savefig(output_path, format='svg')
print(f"Saved: {output_path}")
plt.close()
