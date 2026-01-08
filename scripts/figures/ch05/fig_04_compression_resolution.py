#!/usr/bin/env python3
"""
Figure 5.4: Compression-Resolution Tradeoff
Shows the tradeoff between token vocabulary size and sequence resolution.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_2" / "ch05"
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

# Panel 1: Vocabulary size vs sequence length tradeoff
ax = axes[0]

vocab_sizes = [4, 16, 64, 256, 1024, 4096]
token_lengths = [1, 2, 3, 4, 5, 6]  # approximate average token length in nucleotides
sequence_lengths = [1000 / tl for tl in token_lengths]  # tokens needed for 1000bp

ax.plot(vocab_sizes, sequence_lengths, 'o-', color='#1f77b4', linewidth=2, markersize=8)

for vs, sl, tl in zip(vocab_sizes, sequence_lengths, token_lengths):
    ax.annotate(f'{tl}-mer', xy=(vs, sl), xytext=(vs*1.3, sl*1.1),
                fontsize=8, color='#555555')

ax.set_xscale('log')
ax.set_xlabel('Vocabulary Size', fontweight='bold')
ax.set_ylabel('Tokens per 1kb Sequence', fontweight='bold')
ax.set_title('Compression vs. Vocabulary Size', fontweight='bold')

# Add annotations
ax.annotate('Small vocab\nLong sequences\nHigh resolution',
            xy=(4, 1000), xytext=(10, 700),
            fontsize=8, ha='left',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#98df8a', edgecolor='#2ca02c', alpha=0.7))

ax.annotate('Large vocab\nShort sequences\nLower resolution',
            xy=(4096, 166), xytext=(1000, 300),
            fontsize=8, ha='right',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#ffbb78', edgecolor='#ff7f0e', alpha=0.7))

# Panel 2: Visual representation
ax = axes[1]

# Show same sequence with different tokenizations
sequence = "ATCGATCGATCGATCG"

tokenizations = [
    ('1-mer (vocab=4)', list(sequence), '#2ca02c'),
    ('3-mer (vocab=64)', [sequence[i:i+3] for i in range(0, 15, 3)], '#1f77b4'),
    ('6-mer (vocab=4096)', [sequence[i:i+6] for i in range(0, 12, 6)], '#ff7f0e'),
]

for row, (label, tokens, color) in enumerate(tokenizations):
    y = 2.5 - row * 0.8

    ax.text(-0.1, y, label, ha='right', va='center', fontsize=9, fontweight='bold')

    x = 0
    for token in tokens:
        width = len(token) * 0.15
        rect = mpatches.FancyBboxPatch((x, y - 0.15), width, 0.3,
                                        boxstyle='round,pad=0.02',
                                        facecolor=color, alpha=0.5,
                                        edgecolor=color, linewidth=1)
        ax.add_patch(rect)
        if len(token) <= 3:
            ax.text(x + width/2, y, token, ha='center', va='center',
                    fontsize=8, fontfamily='monospace')
        x += width + 0.05

ax.set_xlim(-1.5, 3.5)
ax.set_ylim(0, 3)
ax.axis('off')
ax.set_title('Same Sequence, Different Resolutions', fontweight='bold')

plt.tight_layout()
output_path = OUTPUT_DIR / '04-fig-ch05-compression-resolution.svg'
plt.savefig(output_path, format='svg')
print(f"Saved: {output_path}")
plt.close()
