#!/usr/bin/env python3
"""
Figure 8.2: Masking Strategies
Two-panel figure showing random vs span masking.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_2" / "ch08"
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
    'A': '#2ca02c', 'T': '#d62728', 'C': '#1f77b4', 'G': '#ff7f0e',
    'mask': '#7f7f7f',
}

def create_panel_a():
    """Random token masking"""
    fig, ax = plt.subplots(figsize=(8, 3))

    sequence = list('ATCGATCGATCGATCG')
    mask_positions = [2, 7, 11, 14]  # Random positions

    for i, token in enumerate(sequence):
        if i in mask_positions:
            color = COLORS['mask']
            display = '?'
        else:
            color = COLORS[token]
            display = token

        ax.add_patch(mpatches.FancyBboxPatch((i * 0.5 + 0.1, 1), 0.4, 0.5,
                                              boxstyle='round,pad=0.02',
                                              facecolor=color, edgecolor='white', linewidth=1))
        ax.text(i * 0.5 + 0.3, 1.25, display,
                ha='center', va='center', fontsize=10, fontweight='bold', color='white')

    ax.text(4, 0.6, 'Random 15% tokens masked independently', ha='center', fontsize=9, style='italic')

    ax.set_xlim(-0.1, 8.5)
    ax.set_ylim(0.3, 1.8)
    ax.axis('off')
    ax.set_title('A. Random Token Masking', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '02-A-fig-masking-strategies.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

def create_panel_b():
    """Span masking"""
    fig, ax = plt.subplots(figsize=(8, 3))

    sequence = list('ATCGATCGATCGATCG')
    mask_spans = [(2, 5), (10, 13)]  # Contiguous spans

    mask_positions = []
    for start, end in mask_spans:
        mask_positions.extend(range(start, end))

    for i, token in enumerate(sequence):
        if i in mask_positions:
            color = COLORS['mask']
            display = '?'
        else:
            color = COLORS[token]
            display = token

        ax.add_patch(mpatches.FancyBboxPatch((i * 0.5 + 0.1, 1), 0.4, 0.5,
                                              boxstyle='round,pad=0.02',
                                              facecolor=color, edgecolor='white', linewidth=1))
        ax.text(i * 0.5 + 0.3, 1.25, display,
                ha='center', va='center', fontsize=10, fontweight='bold', color='white')

    # Highlight spans
    for start, end in mask_spans:
        ax.add_patch(mpatches.FancyBboxPatch((start * 0.5 + 0.05, 0.9), (end - start) * 0.5 + 0.1, 0.7,
                                              boxstyle='round,pad=0.02',
                                              facecolor='none', edgecolor='#d62728', linewidth=2, linestyle='--'))
        ax.text((start + end) / 2 * 0.5 + 0.1, 0.75, 'span', ha='center', fontsize=8, color='#d62728')

    ax.text(4, 0.4, 'Contiguous spans masked together (e.g., span length ~ Poisson(3))',
            ha='center', fontsize=9, style='italic')

    ax.set_xlim(-0.1, 8.5)
    ax.set_ylim(0.2, 1.8)
    ax.axis('off')
    ax.set_title('B. Span Masking', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '02-B-fig-masking-strategies.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

if __name__ == '__main__':
    create_panel_a()
    create_panel_b()
    print("All masking strategy panels generated.")
