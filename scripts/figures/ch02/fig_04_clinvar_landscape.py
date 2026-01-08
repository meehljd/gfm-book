#!/usr/bin/env python3
"""
Figure 2.4: ClinVar Variant Interpretation Landscape
Three-panel figure showing:
A) Classification distribution (VUS dominance)
B) Gene coverage (uneven classification density)
C) Classification evolution over time
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

# Output path
OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_1" / "ch02"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Style settings
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans'],
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.titleweight': 'bold',
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 8,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# Colors
COLORS = {
    'pathogenic': '#d62728',      # Red
    'likely_path': '#ff7f0e',     # Orange
    'vus': '#7f7f7f',             # Gray
    'likely_benign': '#98df8a',   # Light green
    'benign': '#2ca02c',          # Green
    'conflicting': '#9467bd',     # Purple
}

# ===== Panel A: Classification Distribution =====
def create_panel_a():
    fig, ax = plt.subplots(figsize=(5, 4))

    categories = ['Pathogenic', 'Likely\nPathogenic', 'VUS', 'Likely\nBenign', 'Benign', 'Conflicting']
    counts = [85000, 95000, 650000, 120000, 180000, 75000]  # Approximate based on ClinVar stats
    colors = [COLORS['pathogenic'], COLORS['likely_path'], COLORS['vus'],
              COLORS['likely_benign'], COLORS['benign'], COLORS['conflicting']]

    bars = ax.bar(categories, counts, color=colors, edgecolor='white', linewidth=0.5)

    # Highlight VUS
    bars[2].set_edgecolor('#333333')
    bars[2].set_linewidth(2)

    ax.set_ylabel('Number of Variants', fontweight='bold')
    ax.set_xlabel('')
    ax.set_ylim(0, 750000)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x/1000:.0f}K'))

    # Add percentage labels on bars
    total = sum(counts)
    for bar, count in zip(bars, counts):
        pct = count / total * 100
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 15000,
                f'{pct:.0f}%', ha='center', va='bottom', fontsize=8, fontweight='bold')

    # Annotation for VUS
    ax.annotate('VUS comprises >50%\nof all classifications',
                xy=(2, 650000), xytext=(3.5, 550000),
                fontsize=9, ha='center',
                arrowprops=dict(arrowstyle='->', color='#333333', lw=1),
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#cccccc'))

    ax.set_title('A. Classification Distribution', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '04-A-fig-clinvar-landscape.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

# ===== Panel B: Gene Coverage Distribution =====
def create_panel_b():
    fig, ax = plt.subplots(figsize=(5, 4))

    # Simulated gene coverage data (log-scale distribution)
    np.random.seed(42)
    # Most genes have few variants, some have many (power law)
    n_genes = 5000
    variant_counts = np.random.pareto(1.5, n_genes) * 10 + 1
    variant_counts = np.sort(variant_counts)[::-1]

    # Plot as rank vs count
    ranks = np.arange(1, len(variant_counts) + 1)
    ax.plot(ranks, variant_counts, color='#1f77b4', linewidth=1.5)
    ax.fill_between(ranks, variant_counts, alpha=0.3, color='#1f77b4')

    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel('Gene Rank (by variant count)', fontweight='bold')
    ax.set_ylabel('Classified Variants per Gene', fontweight='bold')

    # Highlight regions
    ax.axvline(x=100, color='#d62728', linestyle='--', alpha=0.7)
    ax.text(70, 1000, 'Top 100\ngenes', fontsize=8, ha='right', color='#d62728')

    ax.axvline(x=1000, color='#ff7f0e', linestyle=':', alpha=0.7)
    ax.text(700, 50, 'Top 1000', fontsize=8, ha='right', color='#ff7f0e')

    # Annotation
    ax.annotate('BRCA1, BRCA2, TP53, etc.\ndominate variant catalogs',
                xy=(10, 3000), xytext=(50, 500),
                fontsize=8, ha='left',
                arrowprops=dict(arrowstyle='->', color='#555555', lw=1),
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#cccccc'))

    # Add text about long tail
    ax.text(3000, 3, 'Long tail:\n>4000 genes\nwith <10 variants',
            fontsize=8, ha='center', color='#555555',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f7f7f7', edgecolor='#cccccc'))

    ax.set_title('B. Gene Coverage Distribution', fontweight='bold', loc='left')
    ax.set_xlim(1, 6000)
    ax.set_ylim(1, 10000)

    plt.tight_layout()
    output_path = OUTPUT_DIR / '04-B-fig-clinvar-landscape.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

# ===== Panel C: Classification Evolution Over Time =====
def create_panel_c():
    fig, ax = plt.subplots(figsize=(5, 4))

    years = np.arange(2015, 2025)

    # Simulated data showing growth in classifications over time
    # VUS grows fastest, resolved classifications grow but slower
    pathogenic = np.array([40, 50, 62, 75, 85, 98, 115, 135, 160, 180])
    likely_path = np.array([30, 42, 55, 68, 80, 95, 115, 140, 170, 200])
    vus = np.array([100, 150, 220, 310, 420, 530, 680, 870, 1100, 1350])
    benign = np.array([80, 100, 125, 155, 185, 220, 260, 310, 370, 440])

    ax.stackplot(years, pathogenic, likely_path, vus, benign,
                 labels=['Pathogenic', 'Likely Path.', 'VUS', 'Benign/Likely Benign'],
                 colors=[COLORS['pathogenic'], COLORS['likely_path'], COLORS['vus'], COLORS['benign']],
                 alpha=0.85)

    ax.set_xlabel('Year', fontweight='bold')
    ax.set_ylabel('Cumulative Variants (thousands)', fontweight='bold')
    ax.set_xlim(2015, 2024)
    ax.set_ylim(0, 2200)

    # Legend
    ax.legend(loc='upper left', frameon=True, framealpha=0.95)

    # Annotation
    ax.annotate('VUS growth outpaces\nresolved classifications',
                xy=(2021, 1200), xytext=(2017, 1600),
                fontsize=8, ha='center',
                arrowprops=dict(arrowstyle='->', color='#333333', lw=1),
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#cccccc'))

    ax.set_title('C. Classification Growth Over Time', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '04-C-fig-clinvar-landscape.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

# Generate all panels
if __name__ == '__main__':
    create_panel_a()
    create_panel_b()
    create_panel_c()
    print("All ClinVar landscape panels generated.")
