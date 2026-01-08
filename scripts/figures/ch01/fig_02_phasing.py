#!/usr/bin/env python3
"""
Figure 1.2: Haplotype Phasing and Compound Heterozygosity (v2)
Improved with better color scheme and accessibility.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, Polygon
import numpy as np
from pathlib import Path

# Style configuration following the style guide
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans'],
    'font.size': 11,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.15,
})

# Colors - avoiding gender-coded pink/blue
COLORS = {
    'parent1': '#1f77b4',       # Blue (Parent 1 / Haplotype A)
    'parent1_light': '#aec7e8',
    'parent2': '#ff7f0e',       # Orange (Parent 2 / Haplotype B)
    'parent2_light': '#ffbb78',
    'pathogenic': '#d62728',    # Red for pathogenic variants
    'normal': '#2ca02c',        # Green for normal/wildtype
    'gene': '#e0e0e0',          # Light gray for gene region
    'unknown': '#7f7f7f',       # Gray for unphased
}

OUTPUT_DIR = Path('/root/gfm_book/figs/part_1/ch01')


def draw_chromosome(ax, y, color, label, hatch=None):
    """Draw a chromosome bar with label."""
    # Main chromosome body
    chrom = FancyBboxPatch((0.12, y - 0.035), 0.76, 0.07,
                            boxstyle="round,pad=0.01,rounding_size=0.035",
                            facecolor=color, edgecolor='#333',
                            linewidth=1.5, alpha=0.8, hatch=hatch)
    ax.add_patch(chrom)

    # Gene region (CFTR)
    gene = Rectangle((0.38, y - 0.025), 0.24, 0.05,
                      facecolor=COLORS['gene'], edgecolor='#555',
                      linewidth=1, alpha=0.95)
    ax.add_patch(gene)
    ax.text(0.50, y, 'CFTR', ha='center', va='center', fontsize=10,
            fontweight='bold', color='#333')

    # Label on left
    ax.text(0.03, y, label, ha='left', va='center', fontsize=10,
            fontweight='bold', color=color)


def draw_variant_marker(ax, x, y, color, label=None, above=True):
    """Draw a triangular variant marker."""
    # Triangle pointing down into chromosome
    if above:
        triangle = Polygon([(x, y + 0.045), (x - 0.025, y + 0.09), (x + 0.025, y + 0.09)],
                          facecolor=color, edgecolor='#333', linewidth=1)
        label_y = y + 0.11
    else:
        triangle = Polygon([(x, y - 0.045), (x - 0.025, y - 0.09), (x + 0.025, y - 0.09)],
                          facecolor=color, edgecolor='#333', linewidth=1)
        label_y = y - 0.11
    ax.add_patch(triangle)

    if label:
        ax.text(x, label_y, label, ha='center', va='center' if above else 'center',
                fontsize=9, fontweight='bold', color=color)


def draw_normal_marker(ax, x, y, above=True):
    """Draw a circular normal allele marker."""
    offset = 0.065 if above else -0.065
    circle = plt.Circle((x, y + offset), 0.02,
                        facecolor=COLORS['normal'], edgecolor='#333', linewidth=1)
    ax.add_patch(circle)


def create_panel_a(ax):
    """Panel A: Unphased view."""
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # Title
    ax.text(0.50, 0.95, '(A) Unphased Genotypes', ha='center', va='top',
            fontsize=12, fontweight='bold')

    # Subtitle
    ax.text(0.50, 0.87, 'VCF shows: 0/1, 0/1', ha='center', va='top',
            fontsize=10, color='#555', family='monospace')
    ax.text(0.50, 0.81, '(phase unknown)', ha='center', va='top',
            fontsize=10, color='#555', fontstyle='italic')

    # Draw chromosomes (both gray for unknown phase)
    draw_chromosome(ax, 0.60, COLORS['unknown'], 'Haplotype ?')
    draw_chromosome(ax, 0.38, COLORS['unknown'], 'Haplotype ?')

    # Variant positions (shown on both as unknown)
    pos1, pos2 = 0.42, 0.54

    # Markers on top chromosome
    draw_variant_marker(ax, pos1, 0.60, COLORS['pathogenic'], 'F508del')
    draw_variant_marker(ax, pos2, 0.60, COLORS['pathogenic'], 'G551D')

    # Question marks between chromosomes
    ax.text(0.48, 0.49, '?', ha='center', va='center', fontsize=24,
            fontweight='bold', color='#d62728')

    # Bottom text
    ax.text(0.50, 0.18, 'Which variants are inherited together?',
            ha='center', va='center', fontsize=10, fontstyle='italic', color='#555')
    ax.text(0.50, 0.10, 'Phase determines clinical outcome',
            ha='center', va='center', fontsize=10, fontweight='bold', color='#333')


def create_panel_b(ax):
    """Panel B: Cis configuration."""
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # Title
    ax.text(0.50, 0.95, '(B) Cis Configuration', ha='center', va='top',
            fontsize=12, fontweight='bold')

    # Subtitle with phased notation
    ax.text(0.50, 0.87, 'Phased VCF: 1|0, 1|0', ha='center', va='top',
            fontsize=10, color='#555', family='monospace')
    ax.text(0.50, 0.81, '(both variants on same haplotype)', ha='center', va='top',
            fontsize=10, color='#555', fontstyle='italic')

    # Variant positions
    pos1, pos2 = 0.42, 0.54

    # Haplotype A (blue) - carries both variants
    draw_chromosome(ax, 0.60, COLORS['parent1'], 'Haplotype A', hatch='')
    draw_variant_marker(ax, pos1, 0.60, COLORS['pathogenic'], 'F508del')
    draw_variant_marker(ax, pos2, 0.60, COLORS['pathogenic'], 'G551D')

    # Haplotype B (orange) - normal at both positions
    draw_chromosome(ax, 0.38, COLORS['parent2'], 'Haplotype B', hatch='///')
    draw_normal_marker(ax, pos1, 0.38, above=False)
    draw_normal_marker(ax, pos2, 0.38, above=False)

    # Outcome box
    outcome = FancyBboxPatch((0.15, 0.08), 0.70, 0.12,
                              boxstyle="round,pad=0.02,rounding_size=0.02",
                              facecolor='#d4edda', edgecolor='#28a745', linewidth=2)
    ax.add_patch(outcome)
    ax.text(0.50, 0.14, 'CARRIER (Unaffected)', ha='center', va='center',
            fontsize=11, fontweight='bold', color='#155724')
    ax.text(0.50, 0.06, 'One functional CFTR copy preserved',
            ha='center', va='top', fontsize=9, color='#155724')


def create_panel_c(ax):
    """Panel C: Trans configuration."""
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # Title
    ax.text(0.50, 0.95, '(C) Trans Configuration', ha='center', va='top',
            fontsize=12, fontweight='bold')

    # Subtitle with phased notation
    ax.text(0.50, 0.87, 'Phased VCF: 1|0, 0|1', ha='center', va='top',
            fontsize=10, color='#555', family='monospace')
    ax.text(0.50, 0.81, '(variants on opposite haplotypes)', ha='center', va='top',
            fontsize=10, color='#555', fontstyle='italic')

    # Variant positions
    pos1, pos2 = 0.42, 0.54

    # Haplotype A (blue) - carries F508del, normal at G551D
    draw_chromosome(ax, 0.60, COLORS['parent1'], 'Haplotype A', hatch='')
    draw_variant_marker(ax, pos1, 0.60, COLORS['pathogenic'], 'F508del')
    draw_normal_marker(ax, pos2, 0.60, above=True)

    # Haplotype B (orange) - normal at F508del, carries G551D
    draw_chromosome(ax, 0.38, COLORS['parent2'], 'Haplotype B', hatch='///')
    draw_normal_marker(ax, pos1, 0.38, above=False)
    draw_variant_marker(ax, pos2, 0.38, COLORS['pathogenic'], 'G551D', above=False)

    # Outcome box
    outcome = FancyBboxPatch((0.15, 0.08), 0.70, 0.12,
                              boxstyle="round,pad=0.02,rounding_size=0.02",
                              facecolor='#f8d7da', edgecolor='#dc3545', linewidth=2)
    ax.add_patch(outcome)
    ax.text(0.50, 0.14, 'AFFECTED (Cystic Fibrosis)', ha='center', va='center',
            fontsize=11, fontweight='bold', color='#721c24')
    ax.text(0.50, 0.06, 'No functional CFTR copies',
            ha='center', va='top', fontsize=9, color='#721c24')


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    panels = [
        ('A', create_panel_a),
        ('B', create_panel_b),
        ('C', create_panel_c),
    ]

    for suffix, create_func in panels:
        fig, ax = plt.subplots(figsize=(5.5, 4.5))
        create_func(ax)

        output_file = OUTPUT_DIR / f'02-{suffix}-fig-phasing-compound-het.svg'
        plt.savefig(output_file, format='svg', bbox_inches='tight', pad_inches=0.1)
        plt.close()
        print(f"Saved: {output_file}")


if __name__ == '__main__':
    main()
