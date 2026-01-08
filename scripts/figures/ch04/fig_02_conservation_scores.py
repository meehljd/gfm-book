#!/usr/bin/env python3
"""
Figure 4.2: Conservation Scores
Three-panel figure showing:
A) Multiple sequence alignment
B) Genome-wide phyloP distribution
C) Conservation in annotation-sparse region
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

# Output path
OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_1" / "ch04"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Style settings
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans'],
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.titleweight': 'bold',
    'axes.labelsize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 9,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# Colors
COLORS = {
    'conserved': '#1f77b4',
    'neutral': '#7f7f7f',
    'variable': '#d62728',
}

# ===== Panel A: Multiple Sequence Alignment =====
def create_panel_a():
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))

    species = ['Human', 'Chimp', 'Mouse', 'Dog', 'Chicken', 'Zebrafish']
    n_species = len(species)

    # Conserved position (left)
    ax = axes[0]
    conserved_seq = ['A', 'A', 'A', 'A', 'A', 'A']
    colors_cons = [COLORS['conserved']] * n_species

    for i, (sp, base, color) in enumerate(zip(species, conserved_seq, colors_cons)):
        ax.add_patch(mpatches.FancyBboxPatch(
            (0.3, n_species - i - 0.4), 0.4, 0.8,
            boxstyle='round,pad=0.02',
            facecolor=color, edgecolor='white', linewidth=2
        ))
        ax.text(0.5, n_species - i, base, ha='center', va='center',
                fontsize=14, fontweight='bold', color='white')
        ax.text(0.0, n_species - i, sp, ha='right', va='center', fontsize=9)

    ax.set_xlim(-0.5, 1)
    ax.set_ylim(0, n_species + 0.5)
    ax.axis('off')
    ax.set_title('Conserved Position\n(phyloP = 4.2)', fontweight='bold')

    # Variable position (right)
    ax = axes[1]
    variable_seq = ['G', 'G', 'A', 'T', 'C', 'A']
    base_colors = {'A': '#2ca02c', 'T': '#d62728', 'G': '#ff7f0e', 'C': '#1f77b4'}

    for i, (sp, base) in enumerate(zip(species, variable_seq)):
        color = base_colors[base]
        ax.add_patch(mpatches.FancyBboxPatch(
            (0.3, n_species - i - 0.4), 0.4, 0.8,
            boxstyle='round,pad=0.02',
            facecolor=color, edgecolor='white', linewidth=2
        ))
        ax.text(0.5, n_species - i, base, ha='center', va='center',
                fontsize=14, fontweight='bold', color='white')
        ax.text(0.0, n_species - i, sp, ha='right', va='center', fontsize=9)

    ax.set_xlim(-0.5, 1)
    ax.set_ylim(0, n_species + 0.5)
    ax.axis('off')
    ax.set_title('Neutrally Evolving Position\n(phyloP = -0.2)', fontweight='bold')

    fig.suptitle('A. Multiple Sequence Alignment', fontweight='bold', fontsize=12, y=1.02)
    plt.tight_layout()
    output_path = OUTPUT_DIR / '02-A-fig-conservation-scores.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

# ===== Panel B: Genome-wide phyloP Distribution =====
def create_panel_b():
    fig, ax = plt.subplots(figsize=(6, 4))

    np.random.seed(42)

    # Simulate phyloP distribution (mostly near zero, long right tail)
    neutral = np.random.normal(0, 0.5, 80000)
    conserved = np.random.exponential(1.5, 15000) + 1
    accelerated = -np.random.exponential(0.5, 5000)

    all_scores = np.concatenate([neutral, conserved, accelerated])
    all_scores = np.clip(all_scores, -3, 6)

    # Histogram
    bins = np.linspace(-3, 6, 50)
    ax.hist(all_scores, bins=bins, color=COLORS['conserved'], alpha=0.7, edgecolor='white')

    # Add threshold lines
    ax.axvline(x=0, color='black', linestyle='-', linewidth=1, alpha=0.5)
    ax.axvline(x=2, color=COLORS['variable'], linestyle='--', linewidth=1.5,
               label='phyloP = 2 (strong constraint)')

    # Labels
    ax.set_xlabel('phyloP Score', fontweight='bold')
    ax.set_ylabel('Number of Positions', fontweight='bold')

    # Annotations
    ax.annotate('Neutral\n(most positions)',
                xy=(0, 20000), xytext=(-1.5, 25000),
                fontsize=9, ha='center',
                arrowprops=dict(arrowstyle='->', color='#555555', lw=0.8))

    ax.annotate('Constrained\n(long right tail)',
                xy=(3, 3000), xytext=(4.5, 8000),
                fontsize=9, ha='center',
                arrowprops=dict(arrowstyle='->', color='#555555', lw=0.8))

    ax.legend(loc='upper right', fontsize=8)
    ax.set_title('B. Genome-Wide phyloP Distribution', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '02-B-fig-conservation-scores.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

# ===== Panel C: Conservation in Annotation-Sparse Region =====
def create_panel_c():
    fig, ax = plt.subplots(figsize=(8, 4))

    np.random.seed(42)
    n_positions = 100
    positions = np.arange(n_positions)

    # Simulate conservation scores with one highly conserved element
    conservation = np.random.uniform(-0.5, 0.5, n_positions)
    # Add a conserved element
    conservation[40:60] = np.random.uniform(2.5, 4.5, 20)

    # Plot conservation track
    colors = ['#d62728' if c > 2 else '#1f77b4' if c > 0 else '#7f7f7f' for c in conservation]
    ax.bar(positions, conservation, color=colors, width=0.8, edgecolor='none')

    # Add horizontal line
    ax.axhline(y=0, color='black', linewidth=0.5)
    ax.axhline(y=2, color='#d62728', linestyle='--', linewidth=1, alpha=0.7)

    # Add annotation tracks (empty)
    ax.fill_between([0, 100], -1.5, -1.0, color='#f7f7f7', label='No regulatory annotations')
    ax.text(50, -1.25, 'No ENCODE/Roadmap annotations in this intronic region',
            ha='center', va='center', fontsize=9, style='italic', color='#555555')

    # Mark variant position
    variant_pos = 50
    ax.plot(variant_pos, conservation[variant_pos], 'v', markersize=12, color='#d62728',
            markeredgecolor='white', markeredgewidth=1.5)
    ax.annotate('Variant at\nconserved position',
                xy=(variant_pos, conservation[variant_pos]),
                xytext=(variant_pos + 15, 3.5),
                fontsize=9, ha='left',
                arrowprops=dict(arrowstyle='->', color='#333333', lw=1),
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#cccccc'))

    ax.set_xlabel('Genomic Position', fontweight='bold')
    ax.set_ylabel('phyloP Score', fontweight='bold')
    ax.set_ylim(-2, 5)
    ax.set_xlim(-5, 105)

    ax.set_title('C. Conservation Reveals Function in Annotation-Sparse Region', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '02-C-fig-conservation-scores.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

# Generate all panels
if __name__ == '__main__':
    create_panel_a()
    create_panel_b()
    create_panel_c()
    print("All conservation score panels generated.")
