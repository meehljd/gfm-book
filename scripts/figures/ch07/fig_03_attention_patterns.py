#!/usr/bin/env python3
"""
Figure 7.3: Attention Patterns in Genomics
Three-panel figure showing different attention pattern types.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_2" / "ch07"
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

def create_panel_a():
    """Enhancer-promoter attention"""
    fig, ax = plt.subplots(figsize=(6, 4))

    # Draw genomic region
    ax.fill_between([0, 8], 1.8, 2.2, color='#aec7e8', alpha=0.5)

    # Enhancer
    ax.add_patch(mpatches.FancyBboxPatch((0.5, 1.85), 0.8, 0.3,
                                          boxstyle='round,pad=0.02',
                                          facecolor='#ff7f0e', edgecolor='#333333', linewidth=1.5))
    ax.text(0.9, 2, 'E', ha='center', va='center', fontsize=10, fontweight='bold')

    # Promoter
    ax.add_patch(mpatches.FancyBboxPatch((6.5, 1.85), 1, 0.3,
                                          boxstyle='round,pad=0.02',
                                          facecolor='#2ca02c', edgecolor='#333333', linewidth=1.5))
    ax.text(7, 2, 'TSS', ha='center', va='center', fontsize=10, fontweight='bold')

    # Attention arc
    arc = mpatches.FancyArrowPatch((0.9, 2.2), (7, 2.2),
                                     connectionstyle='arc3,rad=-0.5',
                                     arrowstyle='<->',
                                     color='#d62728', linewidth=3,
                                     mutation_scale=10)
    ax.add_patch(arc)

    # Attention heatmap strip
    np.random.seed(42)
    attn = np.zeros((1, 16))
    attn[0, 1:3] = 0.8  # Enhancer region
    attn[0, 13:15] = 0.8  # Promoter region
    attn[0, 5:7] = 0.3  # Some intermediate attention

    for i in range(16):
        color = plt.cm.Reds(attn[0, i])
        ax.add_patch(mpatches.Rectangle((i * 0.5, 0.8), 0.45, 0.3,
                                          facecolor=color, edgecolor='white', linewidth=0.5))

    ax.text(4, 0.5, 'Attention weights (from TSS)', ha='center', fontsize=9)
    ax.text(4, 2.8, 'Long-range enhancer-promoter interaction', ha='center', fontsize=10, color='#d62728')

    ax.set_xlim(-0.5, 8.5)
    ax.set_ylim(0.2, 3.2)
    ax.axis('off')
    ax.set_title('A. Enhancer-Promoter Attention', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '03-A-fig-attention-patterns.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

def create_panel_b():
    """Genomic context overlay"""
    fig, ax = plt.subplots(figsize=(6, 4))

    # Draw attention heatmap
    np.random.seed(42)
    n = 8
    attn = np.random.rand(n, n) * 0.3
    # Add structure
    for i in range(n):
        for j in range(n):
            if abs(i - j) <= 1:
                attn[i, j] = 0.7 + np.random.rand() * 0.2

    # Long-range interaction
    attn[1, 6] = attn[6, 1] = 0.9

    for i in range(n):
        for j in range(n):
            color = plt.cm.Blues(attn[i, j])
            ax.add_patch(mpatches.Rectangle((j * 0.6 + 0.3, (n - 1 - i) * 0.6 + 0.5),
                                              0.55, 0.55,
                                              facecolor=color, edgecolor='white', linewidth=0.5))

    # Context labels
    contexts = ['P', 'E1', 'I', 'I', 'I', 'I', 'E2', 'I']  # Promoter, Exon, Intron
    for i, ctx in enumerate(contexts):
        ax.text(i * 0.6 + 0.57, (n) * 0.6 + 0.6, ctx, ha='center', fontsize=8)
        ax.text(0.1, (n - 1 - i) * 0.6 + 0.77, ctx, ha='center', fontsize=8)

    ax.text(2.7, 0.15, 'Attention reveals functional relationships\nbeyond linear sequence', ha='center', fontsize=9, style='italic')

    ax.set_xlim(0, 5.5)
    ax.set_ylim(-0.1, 5.5)
    ax.axis('off')
    ax.set_title('B. Attention with Genomic Context', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '03-B-fig-attention-patterns.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

def create_panel_c():
    """Local attention head"""
    fig, ax = plt.subplots(figsize=(6, 4))

    # Local attention pattern (diagonal-dominant)
    np.random.seed(42)
    n = 10
    attn = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            dist = abs(i - j)
            if dist <= 2:
                attn[i, j] = np.exp(-dist * 0.5) + np.random.rand() * 0.1

    for i in range(n):
        for j in range(n):
            color = plt.cm.Purples(attn[i, j] / attn.max())
            ax.add_patch(mpatches.Rectangle((j * 0.45 + 0.2, (n - 1 - i) * 0.45 + 0.5),
                                              0.42, 0.42,
                                              facecolor=color, edgecolor='white', linewidth=0.3))

    ax.text(2.5, 0.15, 'Local head focuses on nearby positions\n(k-mer like patterns)', ha='center', fontsize=9, style='italic')

    ax.set_xlim(0, 5)
    ax.set_ylim(-0.1, 5.3)
    ax.axis('off')
    ax.set_title('C. Local Attention Head', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '03-C-fig-attention-patterns.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

if __name__ == '__main__':
    create_panel_a()
    create_panel_b()
    create_panel_c()
    print("All attention pattern panels generated.")
