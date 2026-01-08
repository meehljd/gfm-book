#!/usr/bin/env python3
"""
Figure 1.5: DeepVariant Pileup Tensor (v2)
Clean subplots showing pileup concept, channels, and CNN output.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle
import matplotlib.colors as mcolors
import numpy as np
from pathlib import Path

# Style configuration
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
    'A': '#2ca02c',
    'C': '#1f77b4',
    'G': '#ff7f0e',
    'T': '#d62728',
    'match': '#e0e0e0',
    'ref': '#aec7e8',
    'model': '#9467bd',
}

OUTPUT_DIR = Path('/root/gfm_book/figs/part_1/ch01')
OUTPUT_FILE = OUTPUT_DIR / '05-fig-deepvariant-pileup.svg'


def create_figure():
    """Create the DeepVariant figure with clean subplots."""

    fig = plt.figure(figsize=(12, 6))

    # Create layout: 3 panels
    gs = fig.add_gridspec(1, 3, width_ratios=[1.5, 1, 1], wspace=0.3)

    # === PANEL A: Pileup Visualization ===
    ax_pileup = fig.add_subplot(gs[0])
    ax_pileup.set_xlim(0, 1)
    ax_pileup.set_ylim(0, 1)
    ax_pileup.axis('off')
    ax_pileup.set_title('(A) Pileup at Candidate Site', loc='left', pad=10)

    # Reference sequence
    ref_seq = 'ACGTACGTACA'
    ref_y = 0.92
    n_pos = len(ref_seq)
    cell_w = 0.08
    cell_h = 0.055
    start_x = 0.1

    ax_pileup.text(0.02, ref_y, 'Ref:', ha='left', va='center', fontsize=9, fontweight='bold')

    for i, base in enumerate(ref_seq):
        x = start_x + i * cell_w
        rect = Rectangle((x, ref_y - cell_h/2), cell_w - 0.005, cell_h,
                         facecolor=COLORS['ref'], edgecolor='#333', linewidth=0.8)
        ax_pileup.add_patch(rect)
        ax_pileup.text(x + cell_w/2 - 0.002, ref_y, base, ha='center', va='center',
                      fontsize=9, fontweight='bold', family='monospace')

    # Variant position indicator
    var_pos = 5
    var_x = start_x + var_pos * cell_w + cell_w/2 - 0.002
    ax_pileup.annotate('', xy=(var_x, ref_y - cell_h/2 - 0.015),
                      xytext=(var_x, ref_y - cell_h/2 - 0.06),
                      arrowprops=dict(arrowstyle='->', color='#d62728', lw=2))
    ax_pileup.text(var_x, ref_y - cell_h/2 - 0.08, 'C→G', ha='center', va='top',
                  fontsize=9, color='#d62728', fontweight='bold')

    # Reads (heterozygous example)
    np.random.seed(42)
    n_reads = 8
    read_y_start = 0.75
    read_spacing = 0.075

    ax_pileup.text(0.02, read_y_start, 'Reads:', ha='left', va='center', fontsize=9, fontweight='bold')

    for read_idx in range(n_reads):
        y = read_y_start - read_idx * read_spacing
        is_alt = read_idx < n_reads // 2  # First half alt, second half ref

        for i, base in enumerate(ref_seq):
            x = start_x + i * cell_w

            # Color by position
            if i == var_pos:
                if is_alt:
                    color = COLORS['G']
                    display_base = 'G'
                else:
                    color = COLORS['match']
                    display_base = 'C'
            else:
                color = COLORS['match']
                display_base = ''

            # Quality affects alpha
            alpha = 0.5 + 0.4 * np.random.random()

            rect = Rectangle((x, y - cell_h*0.4), cell_w - 0.005, cell_h*0.8,
                             facecolor=color, edgecolor='#888', linewidth=0.5, alpha=alpha)
            ax_pileup.add_patch(rect)

            if display_base:
                ax_pileup.text(x + cell_w/2 - 0.002, y, display_base,
                              ha='center', va='center', fontsize=8,
                              fontweight='bold', family='monospace',
                              color='white' if is_alt and i == var_pos else '#333')

    # Allele count annotation
    ax_pileup.text(0.95, 0.55, '4 Alt (G)\n4 Ref (C)', ha='right', va='center',
                  fontsize=9, bbox=dict(boxstyle='round', facecolor='#f0f0f0', edgecolor='#ccc'))

    # === PANEL B: Tensor Channels ===
    ax_channels = fig.add_subplot(gs[1])
    ax_channels.set_xlim(0, 1)
    ax_channels.set_ylim(0, 1)
    ax_channels.axis('off')
    ax_channels.set_title('(B) Tensor Channels', loc='left', pad=10)

    channels = [
        ('Base Identity', COLORS['match'], 'A/C/G/T encoding'),
        ('Base Quality', '#aec7e8', 'Phred scores'),
        ('Mapping Quality', '#98df8a', 'Alignment confidence'),
        ('Strand', '#ffbb78', '+/- orientation'),
        ('Allele Support', '#c5b0d5', 'Ref/Alt indication'),
    ]

    for i, (name, color, desc) in enumerate(channels):
        y = 0.88 - i * 0.16

        # Channel box
        box = FancyBboxPatch((0.05, y - 0.05), 0.35, 0.10,
                              boxstyle="round,pad=0.02,rounding_size=0.02",
                              facecolor=color, edgecolor='#333', linewidth=1)
        ax_channels.add_patch(box)

        ax_channels.text(0.225, y, name, ha='center', va='center',
                        fontsize=9, fontweight='bold')
        ax_channels.text(0.45, y, desc, ha='left', va='center',
                        fontsize=8, color='#555')

    # Arrow indicating stacking
    ax_channels.annotate('', xy=(0.225, 0.06), xytext=(0.225, 0.12),
                        arrowprops=dict(arrowstyle='->', color='#333', lw=1.5))
    ax_channels.text(0.5, 0.03, '5 channels × H × W', ha='center', va='center',
                    fontsize=10, fontweight='bold',
                    bbox=dict(boxstyle='round', facecolor='#e0e0e0', edgecolor='#999'))

    # === PANEL C: CNN Output ===
    ax_output = fig.add_subplot(gs[2])
    ax_output.set_xlim(0, 1)
    ax_output.set_ylim(0, 1)
    ax_output.axis('off')
    ax_output.set_title('(C) Genotype Classification', loc='left', pad=10)

    # CNN box
    cnn = FancyBboxPatch((0.15, 0.70), 0.7, 0.18,
                          boxstyle="round,pad=0.02,rounding_size=0.03",
                          facecolor=COLORS['model'], edgecolor='#333', linewidth=1.5)
    ax_output.add_patch(cnn)
    ax_output.text(0.5, 0.79, 'Inception CNN', ha='center', va='center',
                  fontsize=11, fontweight='bold', color='white')

    # Arrow
    ax_output.annotate('', xy=(0.5, 0.58), xytext=(0.5, 0.68),
                      arrowprops=dict(arrowstyle='->', color='#333', lw=2))

    # Softmax output
    ax_output.text(0.5, 0.52, 'Softmax Output', ha='center', va='center',
                  fontsize=10, fontweight='bold')

    # Genotype probabilities
    genotypes = ['0/0 (Ref)', '0/1 (Het)', '1/1 (Alt)']
    probs = [0.02, 0.96, 0.02]
    colors = ['#aec7e8', '#2ca02c', '#d62728']

    bar_y = 0.40
    bar_h = 0.06
    bar_spacing = 0.10

    for i, (gt, prob, color) in enumerate(zip(genotypes, probs, colors)):
        y = bar_y - i * bar_spacing

        # Background
        bg = Rectangle((0.15, y - bar_h/2), 0.55, bar_h,
                       facecolor='#f0f0f0', edgecolor='#ccc', linewidth=0.5)
        ax_output.add_patch(bg)

        # Probability bar
        prob_bar = Rectangle((0.15, y - bar_h/2), 0.55 * prob, bar_h,
                             facecolor=color, edgecolor='none')
        ax_output.add_patch(prob_bar)

        # Labels
        ax_output.text(0.12, y, gt, ha='right', va='center', fontsize=9)
        ax_output.text(0.72, y, f'{prob:.0%}', ha='left', va='center',
                      fontsize=9, fontweight='bold' if prob > 0.5 else 'normal')

    # Called genotype box
    result = FancyBboxPatch((0.15, 0.04), 0.70, 0.10,
                             boxstyle="round,pad=0.02,rounding_size=0.02",
                             facecolor='#d4edda', edgecolor='#28a745', linewidth=2)
    ax_output.add_patch(result)
    ax_output.text(0.5, 0.09, 'Called: 0/1 (Heterozygous)', ha='center', va='center',
                  fontsize=10, fontweight='bold', color='#155724')

    return fig


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    fig = create_figure()
    fig.savefig(OUTPUT_FILE, format='svg', bbox_inches='tight', pad_inches=0.15)
    plt.close()
    print(f"Saved: {OUTPUT_FILE}")


if __name__ == '__main__':
    main()
