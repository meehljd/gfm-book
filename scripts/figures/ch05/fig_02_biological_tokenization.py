#!/usr/bin/env python3
"""
Figure 5.2: Biologically-Informed Tokenization
Shows codon-aware and structure-aware tokenization strategies.
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
    'axes.titlesize': 11,
    'axes.titleweight': 'bold',
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
})

COLORS = {
    'codon': '#2ca02c',
    'amino': '#ff7f0e',
    'exon': '#1f77b4',
    'intron': '#7f7f7f',
    'splice': '#d62728',
}

fig, axes = plt.subplots(2, 1, figsize=(10, 6))

# Panel 1: Codon-aware tokenization
ax = axes[0]
sequence = "ATG GCT AAA TGC TAA"
codons = sequence.split()
amino_acids = ['Met', 'Ala', 'Lys', 'Cys', 'Stop']

x_offset = 0.1
for i, (codon, aa) in enumerate(zip(codons, amino_acids)):
    # Draw codon
    rect = mpatches.FancyBboxPatch((x_offset, 0.5), 0.8, 0.35,
                                    boxstyle='round,pad=0.02',
                                    facecolor=COLORS['codon'], alpha=0.3,
                                    edgecolor=COLORS['codon'], linewidth=1.5)
    ax.add_patch(rect)
    ax.text(x_offset + 0.4, 0.67, codon, ha='center', va='center',
            fontsize=11, fontweight='bold', fontfamily='monospace')

    # Arrow to amino acid
    ax.annotate('', xy=(x_offset + 0.4, 0.25), xytext=(x_offset + 0.4, 0.45),
                arrowprops=dict(arrowstyle='->', color='#555555', lw=1))

    # Amino acid
    circle = mpatches.Circle((x_offset + 0.4, 0.12), 0.12,
                              facecolor=COLORS['amino'], alpha=0.5,
                              edgecolor=COLORS['amino'], linewidth=1.5)
    ax.add_patch(circle)
    ax.text(x_offset + 0.4, 0.12, aa, ha='center', va='center',
            fontsize=8, fontweight='bold')

    x_offset += 1.0

ax.set_xlim(0, 5.5)
ax.set_ylim(-0.1, 1.0)
ax.axis('off')
ax.set_title('Codon-Aware Tokenization (3-nucleotide blocks → amino acids)', fontweight='bold', loc='left')

# Panel 2: Exon/intron boundary tokenization
ax = axes[1]

# Draw gene structure
regions = [
    ('Exon 1', 0, 1.2, COLORS['exon']),
    ('Intron', 1.2, 2.5, COLORS['intron']),
    ('Exon 2', 2.5, 4.0, COLORS['exon']),
    ('Intron', 4.0, 5.2, COLORS['intron']),
    ('Exon 3', 5.2, 6.5, COLORS['exon']),
]

for label, start, end, color in regions:
    height = 0.3 if 'Exon' in label else 0.15
    y_offset = 0.5 - height/2
    rect = mpatches.FancyBboxPatch((start, y_offset), end - start, height,
                                    boxstyle='round,pad=0.01',
                                    facecolor=color, alpha=0.5,
                                    edgecolor=color, linewidth=1.5)
    ax.add_patch(rect)
    ax.text((start + end)/2, 0.5, label, ha='center', va='center',
            fontsize=9, fontweight='bold', color='white' if 'Exon' in label else '#333333')

# Mark splice sites
splice_sites = [1.2, 2.5, 4.0, 5.2]
for ss in splice_sites:
    ax.plot([ss, ss], [0.25, 0.75], color=COLORS['splice'], linewidth=2, linestyle='--')
    ax.plot(ss, 0.8, 'v', markersize=8, color=COLORS['splice'])

ax.text(1.2, 0.9, "5' SS", ha='center', fontsize=8, color=COLORS['splice'])
ax.text(2.5, 0.9, "3' SS", ha='center', fontsize=8, color=COLORS['splice'])

ax.text(3.25, 0.1, 'Splice-aware tokenization preserves biological boundaries',
        ha='center', fontsize=9, style='italic')

ax.set_xlim(-0.2, 7)
ax.set_ylim(-0.1, 1.1)
ax.axis('off')
ax.set_title('Splice-Aware Tokenization (respects exon/intron boundaries)', fontweight='bold', loc='left')

plt.tight_layout()
output_path = OUTPUT_DIR / '02-fig-ch05-biological-tokenization.svg'
plt.savefig(output_path, format='svg')
print(f"Saved: {output_path}")
plt.close()
