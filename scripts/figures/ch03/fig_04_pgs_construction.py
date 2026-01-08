#!/usr/bin/env python3
"""
Figure 3.4: Polygenic Score Construction Methods
Two-panel comparison of C+T vs Bayesian methods.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

# Output path
OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_1" / "ch03"
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
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
})

# Colors
COLORS = {
    'included': '#1f77b4',
    'excluded': '#d3d3d3',
    'significant': '#d62728',
    'shrunken': '#2ca02c',
}

# ===== Panel A: Clumping and Thresholding =====
def create_panel_a():
    fig, ax = plt.subplots(figsize=(6, 5))

    np.random.seed(42)

    # Simulate GWAS results for a region
    n_variants = 50
    positions = np.sort(np.random.uniform(0, 100, n_variants))

    # Effect sizes (most small, a few large)
    effects = np.random.normal(0, 0.1, n_variants)
    # Add a few significant hits
    significant_idx = [10, 25, 40]
    for idx in significant_idx:
        effects[idx] = np.random.uniform(0.3, 0.5) * np.random.choice([-1, 1])

    # P-values (derived from effects, with noise)
    pvals = 10 ** (-np.abs(effects) * 20 + np.random.uniform(-2, 2, n_variants))
    pvals = np.clip(pvals, 1e-15, 1)

    # Apply C+T
    p_threshold = 5e-8
    ld_window = 15  # positions within this distance are "in LD"

    # Step 1: Threshold
    passed_threshold = pvals < p_threshold

    # Step 2: Clumping (simplified - keep lowest p-value in each window)
    included = np.zeros(n_variants, dtype=bool)
    sorted_idx = np.argsort(pvals)

    for idx in sorted_idx:
        if passed_threshold[idx]:
            # Check if any already-included variant is within LD window
            in_ld = False
            for inc_idx in np.where(included)[0]:
                if abs(positions[idx] - positions[inc_idx]) < ld_window:
                    in_ld = True
                    break
            if not in_ld:
                included[idx] = True

    # Plot
    # All variants
    ax.scatter(positions[~included], -np.log10(pvals[~included]),
               c=COLORS['excluded'], s=50, alpha=0.5, label='Excluded', zorder=1)
    ax.scatter(positions[included], -np.log10(pvals[included]),
               c=COLORS['included'], s=100, marker='*', edgecolors='white',
               linewidths=1, label='Included (lead SNPs)', zorder=2)

    # Threshold line
    ax.axhline(y=-np.log10(p_threshold), color=COLORS['significant'],
               linestyle='--', linewidth=1.5, label=f'P = 5×10⁻⁸')

    # Annotations
    ax.annotate('Clumped\n(in LD with\nlead SNP)',
                xy=(positions[11], -np.log10(pvals[11])),
                xytext=(positions[11] - 15, -np.log10(pvals[11]) + 3),
                fontsize=8, ha='center',
                arrowprops=dict(arrowstyle='->', color='#555555', lw=0.8))

    ax.set_xlabel('Genomic Position', fontweight='bold')
    ax.set_ylabel('-log₁₀(P-value)', fontweight='bold')
    ax.legend(loc='upper right', fontsize=8)
    ax.set_xlim(-5, 105)

    # Add summary box
    n_total = n_variants
    n_included = np.sum(included)
    summary_text = f'Total variants: {n_total}\nAfter threshold: {np.sum(passed_threshold)}\nAfter clumping: {n_included}'
    ax.text(0.02, 0.98, summary_text, transform=ax.transAxes, fontsize=9,
            va='top', ha='left', bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#cccccc'))

    ax.set_title('A. Clumping + Thresholding (C+T)', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '04-A-fig-pgs-construction.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

# ===== Panel B: Bayesian Method (LDpred/PRS-CS) =====
def create_panel_b():
    fig, ax = plt.subplots(figsize=(6, 5))

    np.random.seed(42)

    # Same variants as Panel A
    n_variants = 50
    positions = np.sort(np.random.uniform(0, 100, n_variants))

    # Original effect sizes
    original_effects = np.random.normal(0, 0.15, n_variants)
    significant_idx = [10, 25, 40]
    for idx in significant_idx:
        original_effects[idx] = np.random.uniform(0.3, 0.5) * np.random.choice([-1, 1])

    # Posterior effects (shrunk toward zero, but all contribute)
    # Strong signals shrunk less, weak signals shrunk more
    shrinkage = 1 / (1 + 0.5 / (np.abs(original_effects) + 0.01))
    posterior_effects = original_effects * shrinkage

    # Plot effect sizes as bars
    bar_width = 1.5

    # Show original (faded) and posterior (solid)
    ax.bar(positions, original_effects, width=bar_width, color=COLORS['excluded'],
           alpha=0.4, label='GWAS effect (βₘₐᵣginal)', zorder=1)
    ax.bar(positions, posterior_effects, width=bar_width, color=COLORS['shrunken'],
           alpha=0.8, label='Posterior effect (βposterior)', zorder=2)

    ax.axhline(y=0, color='#333333', linewidth=0.5)

    # Annotations
    ax.annotate('Strong signal:\nminimal shrinkage',
                xy=(positions[25], posterior_effects[25]),
                xytext=(positions[25] + 20, posterior_effects[25] + 0.1),
                fontsize=8, ha='left',
                arrowprops=dict(arrowstyle='->', color='#555555', lw=0.8))

    ax.annotate('Weak signal:\nstrong shrinkage\ntoward zero',
                xy=(positions[30], posterior_effects[30]),
                xytext=(positions[30] + 15, 0.2),
                fontsize=8, ha='left',
                arrowprops=dict(arrowstyle='->', color='#555555', lw=0.8))

    ax.set_xlabel('Genomic Position', fontweight='bold')
    ax.set_ylabel('Effect Size (β)', fontweight='bold')
    ax.legend(loc='upper left', fontsize=8)
    ax.set_xlim(-5, 105)

    # Add summary box
    summary_text = f'All {n_variants} variants contribute\nWeights modulated by\nevidence strength'
    ax.text(0.98, 0.98, summary_text, transform=ax.transAxes, fontsize=9,
            va='top', ha='right', bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#cccccc'))

    ax.set_title('B. Bayesian Methods (LDpred, PRS-CS)', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '04-B-fig-pgs-construction.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

# Generate all panels
if __name__ == '__main__':
    create_panel_a()
    create_panel_b()
    print("All PGS construction panels generated.")
