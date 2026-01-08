#!/usr/bin/env python3
"""
Figure 4.4: CADD Training Paradigm
Three-panel figure showing:
A) Proxy-neutral class
B) Proxy-deleterious class
C) Classification learning
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
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
})

# Colors
COLORS = {
    'neutral': '#2ca02c',
    'deleterious': '#d62728',
    'background': '#f7f7f7',
}

# ===== Panel A: Proxy-Neutral Class =====
def create_panel_a():
    fig, ax = plt.subplots(figsize=(5, 4))

    # Draw phylogenetic tree sketch
    ax.plot([0.1, 0.3], [0.5, 0.7], 'k-', linewidth=2)
    ax.plot([0.1, 0.3], [0.5, 0.3], 'k-', linewidth=2)
    ax.plot([0.3, 0.5], [0.7, 0.8], 'k-', linewidth=2)
    ax.plot([0.3, 0.5], [0.7, 0.6], 'k-', linewidth=2)
    ax.plot([0.3, 0.5], [0.3, 0.4], 'k-', linewidth=2)
    ax.plot([0.3, 0.5], [0.3, 0.2], 'k-', linewidth=2)

    # Labels
    ax.text(0.5, 0.8, 'Human', fontsize=9, va='center')
    ax.text(0.5, 0.6, 'Chimp', fontsize=9, va='center')
    ax.text(0.5, 0.4, 'Gorilla', fontsize=9, va='center')
    ax.text(0.5, 0.2, 'Orangutan', fontsize=9, va='center')
    ax.text(0.05, 0.5, 'Ancestor', fontsize=8, va='center', style='italic')

    # Highlight human branch
    ax.annotate('', xy=(0.5, 0.8), xytext=(0.3, 0.7),
                arrowprops=dict(arrowstyle='->', color=COLORS['neutral'], lw=2))

    # Add derived alleles box
    box = mpatches.FancyBboxPatch((0.55, 0.65), 0.4, 0.25,
                                   boxstyle='round,pad=0.02',
                                   facecolor=COLORS['neutral'], alpha=0.3,
                                   edgecolor=COLORS['neutral'], linewidth=2)
    ax.add_patch(box)
    ax.text(0.75, 0.77, 'Derived Alleles\n(High DAF in humans)',
            ha='center', va='center', fontsize=9, fontweight='bold')

    # Description
    ax.text(0.5, 0.02, 'Variants that survived\nmillions of years of selection',
            ha='center', va='bottom', fontsize=10, style='italic')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('A. Proxy-Neutral Class', fontweight='bold', color=COLORS['neutral'])

    plt.tight_layout()
    output_path = OUTPUT_DIR / '04-A-fig-cadd-training.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

# ===== Panel B: Proxy-Deleterious Class =====
def create_panel_b():
    fig, ax = plt.subplots(figsize=(5, 4))

    # Simulate mutation process
    np.random.seed(42)

    # Draw genome segment
    genome_y = 0.5
    segment_height = 0.1

    # Background segment
    ax.fill_between([0.1, 0.9], genome_y - segment_height, genome_y + segment_height,
                    color=COLORS['background'], edgecolor='#333333', linewidth=1.5)

    # Show simulated mutations
    mutation_positions = [0.2, 0.35, 0.5, 0.65, 0.8]
    for pos in mutation_positions:
        ax.plot(pos, genome_y, 'o', markersize=8, color=COLORS['deleterious'],
                markeredgecolor='white', markeredgewidth=1)

    # Arrow from "simulation"
    ax.annotate('', xy=(0.5, 0.6), xytext=(0.5, 0.75),
                arrowprops=dict(arrowstyle='->', color='#555555', lw=1.5))
    ax.text(0.5, 0.8, 'Simulate mutations\nmatching human\nmutational processes',
            ha='center', va='bottom', fontsize=9, style='italic')

    # CpG context note
    ax.text(0.35, 0.35, 'CpG\ntransition', fontsize=8, ha='center', color=COLORS['deleterious'])
    ax.annotate('', xy=(0.35, 0.45), xytext=(0.35, 0.38),
                arrowprops=dict(arrowstyle='->', color=COLORS['deleterious'], lw=1))

    # Description
    ax.text(0.5, 0.1, 'Variants that could occur\nbut are generally not observed',
            ha='center', va='center', fontsize=10, style='italic')

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('B. Proxy-Deleterious Class', fontweight='bold', color=COLORS['deleterious'])

    plt.tight_layout()
    output_path = OUTPUT_DIR / '04-B-fig-cadd-training.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

# ===== Panel C: Classification =====
def create_panel_c():
    fig, ax = plt.subplots(figsize=(6, 4))

    np.random.seed(42)

    # Two-class scatter in 2D feature space
    n_neutral = 100
    n_deleterious = 100

    # Neutral class (lower left)
    neutral_x = np.random.normal(2, 0.8, n_neutral)
    neutral_y = np.random.normal(2, 0.8, n_neutral)

    # Deleterious class (upper right)
    deleterious_x = np.random.normal(4, 0.8, n_deleterious)
    deleterious_y = np.random.normal(4, 0.8, n_deleterious)

    ax.scatter(neutral_x, neutral_y, c=COLORS['neutral'], s=30, alpha=0.6,
               label='Proxy-neutral', edgecolors='white', linewidths=0.5)
    ax.scatter(deleterious_x, deleterious_y, c=COLORS['deleterious'], s=30, alpha=0.6,
               label='Proxy-deleterious', edgecolors='white', linewidths=0.5)

    # Decision boundary
    x_line = np.linspace(0, 6, 100)
    y_line = x_line  # Diagonal
    ax.plot(x_line, y_line, 'k--', linewidth=2, label='Decision boundary')

    # Annotations
    ax.annotate('Tolerated by\nevolution',
                xy=(1.5, 1.5), fontsize=9, ha='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#cccccc'))
    ax.annotate('Depleted by\nselection',
                xy=(4.5, 4.5), fontsize=9, ha='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#cccccc'))

    ax.set_xlabel('Feature Dimension 1\n(e.g., conservation)', fontweight='bold')
    ax.set_ylabel('Feature Dimension 2\n(e.g., gene constraint)', fontweight='bold')
    ax.legend(loc='lower right', fontsize=8)
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)

    ax.set_title('C. Classifier Learns to Distinguish Classes', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '04-C-fig-cadd-training.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

# Generate all panels
if __name__ == '__main__':
    create_panel_a()
    create_panel_b()
    create_panel_c()
    print("All CADD training panels generated.")
