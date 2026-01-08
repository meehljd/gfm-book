#!/usr/bin/env python3
"""
Figure 1.4: Difficult Genomic Regions (v2)
Simplified with clear subplots and better layout.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, Polygon
import numpy as np
from pathlib import Path

# Style configuration
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans'],
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.titleweight': 'bold',
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.15,
})

COLORS = {
    'chrom': '#e8e8e8',
    'centromere': '#7f7f7f',
    'segdup': '#ffbb78',
    'hla': '#ff7f0e',
    'repeat': '#d62728',
    'cyp': '#9467bd',
    'short_read': '#aec7e8',
    'long_read': '#98df8a',
    'high_conf': '#2ca02c',
}

OUTPUT_DIR = Path('/root/gfm_book/figs/part_1/ch01')
OUTPUT_FILE = OUTPUT_DIR / '04-fig-difficult-regions.svg'


def draw_chromosome_example(ax, y, chrom_id, length, regions, cent_pos, annotations=None):
    """Draw a single chromosome with highlighted difficult regions."""
    x_start = 0.15
    x_width = length * 0.7

    # Chromosome body
    chrom = FancyBboxPatch((x_start, y - 0.03), x_width, 0.06,
                            boxstyle="round,pad=0.005,rounding_size=0.03",
                            facecolor=COLORS['chrom'], edgecolor='#666',
                            linewidth=1)
    ax.add_patch(chrom)

    # Centromere
    cent_x = x_start + cent_pos * x_width
    centromere = Rectangle((cent_x - 0.015, y - 0.025), 0.03, 0.05,
                           facecolor=COLORS['centromere'], edgecolor='none')
    ax.add_patch(centromere)

    # Chromosome label
    ax.text(0.08, y, f'Chr {chrom_id}', ha='right', va='center',
            fontsize=10, fontweight='bold')

    # Difficult regions
    for region_type, start, end, label in regions:
        region_x = x_start + start * x_width
        region_w = (end - start) * x_width
        region = Rectangle((region_x, y - 0.025), region_w, 0.05,
                           facecolor=COLORS[region_type], edgecolor='none', alpha=0.9)
        ax.add_patch(region)

        # Region label
        if label:
            ax.annotate(label,
                       xy=(region_x + region_w/2, y + 0.04),
                       ha='center', va='bottom', fontsize=9,
                       bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                                edgecolor=COLORS[region_type], alpha=0.95))


def create_figure():
    """Create the difficult regions figure with subplots."""

    fig = plt.figure(figsize=(11, 7))

    # Create grid: top row for chromosomes, bottom row for comparison
    gs = fig.add_gridspec(2, 2, height_ratios=[1.5, 1], width_ratios=[2, 1],
                          hspace=0.35, wspace=0.25)

    # === PANEL A: Example Chromosomes ===
    ax_chrom = fig.add_subplot(gs[0, :])
    ax_chrom.set_xlim(0, 1)
    ax_chrom.set_ylim(0, 1)
    ax_chrom.axis('off')
    ax_chrom.set_title('(A) Example Difficult Regions by Chromosome', loc='left', pad=10)

    # Draw example chromosomes with difficult regions
    chromosomes = [
        # (chrom_id, length, regions, cent_pos)
        ('4', 0.77, [('repeat', 0.02, 0.06, 'HTT\n(Huntington)')], 0.25),
        ('6', 0.69, [('hla', 0.28, 0.38, 'HLA Complex')], 0.35),
        ('22', 0.21, [('cyp', 0.55, 0.68, 'CYP2D6'),
                      ('segdup', 0.15, 0.25, None)], 0.35),
        ('X', 0.63, [('repeat', 0.85, 0.92, 'FMR1\n(Fragile X)')], 0.38),
    ]

    y_positions = [0.82, 0.58, 0.34, 0.10]
    for (chrom_id, length, regions, cent_pos), y in zip(chromosomes, y_positions):
        draw_chromosome_example(ax_chrom, y, chrom_id, length, regions, cent_pos)

    # Legend for region types
    legend_elements = [
        mpatches.Patch(facecolor=COLORS['repeat'], edgecolor='#333', label='Tandem Repeats'),
        mpatches.Patch(facecolor=COLORS['hla'], edgecolor='#333', label='HLA/Immune'),
        mpatches.Patch(facecolor=COLORS['cyp'], edgecolor='#333', label='Pharmacogenes'),
        mpatches.Patch(facecolor=COLORS['segdup'], edgecolor='#333', label='Segmental Dups'),
    ]
    ax_chrom.legend(handles=legend_elements, loc='upper right', fontsize=9,
                   framealpha=0.95, ncol=2)

    # === PANEL B: Short vs Long Read Comparison ===
    ax_compare = fig.add_subplot(gs[1, 0])
    ax_compare.set_xlim(0, 1)
    ax_compare.set_ylim(0, 1)
    ax_compare.axis('off')
    ax_compare.set_title('(B) Short-Read vs Long-Read Resolution', loc='left', pad=10)

    # Difficult region bar
    region = FancyBboxPatch((0.2, 0.55), 0.6, 0.15,
                             boxstyle="round,pad=0.01,rounding_size=0.02",
                             facecolor=COLORS['segdup'], edgecolor='#666',
                             linewidth=1.5, alpha=0.7)
    ax_compare.add_patch(region)
    ax_compare.text(0.5, 0.625, 'Repetitive Region (~10 kb)', ha='center', va='center',
                   fontsize=10, fontweight='bold')

    # Short reads (fragmented)
    ax_compare.text(0.05, 0.40, 'Short\nreads:', ha='left', va='center', fontsize=10)
    for i, x in enumerate(np.linspace(0.22, 0.76, 8)):
        read = Rectangle((x, 0.36), 0.06, 0.08,
                         facecolor=COLORS['short_read'], edgecolor='#1f77b4',
                         linewidth=0.8)
        ax_compare.add_patch(read)
        # Question marks for ambiguous mapping
        if 0.35 < x < 0.65:
            ax_compare.text(x + 0.03, 0.33, '?', ha='center', va='top',
                           fontsize=10, color='#d62728', fontweight='bold')

    ax_compare.text(0.85, 0.40, 'Ambiguous\nmapping', ha='left', va='center',
                   fontsize=9, color='#d62728', fontstyle='italic')

    # Long read (spans region)
    ax_compare.text(0.05, 0.15, 'Long\nread:', ha='left', va='center', fontsize=10)
    long_read = FancyBboxPatch((0.20, 0.11), 0.62, 0.08,
                                boxstyle="round,pad=0.005,rounding_size=0.02",
                                facecolor=COLORS['long_read'], edgecolor='#2ca02c',
                                linewidth=1.5)
    ax_compare.add_patch(long_read)
    ax_compare.text(0.85, 0.15, 'Unambiguous\nresolution', ha='left', va='center',
                   fontsize=9, color='#2ca02c', fontweight='bold')

    # === PANEL C: Genome Fraction Statistics ===
    ax_stats = fig.add_subplot(gs[1, 1])
    ax_stats.set_title('(C) Callability by Region', loc='left', pad=10)

    categories = ['High\nconfidence', 'Seg. dups', 'Low\ncomplexity',
                  'HLA/KIR', 'Centro-\nmeres']
    values = [85, 5, 4, 3, 3]
    colors = [COLORS['high_conf'], COLORS['segdup'], '#d0d0d0',
              COLORS['hla'], COLORS['centromere']]

    bars = ax_stats.barh(categories, values, color=colors, edgecolor='#333', linewidth=0.8)
    ax_stats.set_xlabel('% of Genome', fontsize=10)
    ax_stats.set_xlim(0, 100)

    # Add value labels
    for bar, val in zip(bars, values):
        ax_stats.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2,
                     f'{val}%', ha='left', va='center', fontsize=9)

    # Clean up axes
    ax_stats.spines['top'].set_visible(False)
    ax_stats.spines['right'].set_visible(False)
    ax_stats.tick_params(axis='y', labelsize=9)

    plt.tight_layout()
    return fig


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    fig = create_figure()
    fig.savefig(OUTPUT_FILE, format='svg', bbox_inches='tight', pad_inches=0.15)
    plt.close()
    print(f"Saved: {OUTPUT_FILE}")


if __name__ == '__main__':
    main()
