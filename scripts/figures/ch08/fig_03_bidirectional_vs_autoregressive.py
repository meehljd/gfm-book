#!/usr/bin/env python3
"""
Figure 8.3: Bidirectional vs Autoregressive
Two-panel figure comparing context access patterns.
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

COLORS = {'A': '#2ca02c', 'T': '#d62728', 'C': '#1f77b4', 'G': '#ff7f0e', 'mask': '#7f7f7f'}

def create_panel_a():
    """Bidirectional context in MLM"""
    fig, ax = plt.subplots(figsize=(7, 4))

    sequence = ['A', 'T', '?', 'G', 'A']
    target_pos = 2

    for i, token in enumerate(sequence):
        if token == '?':
            color = COLORS['mask']
        else:
            color = COLORS[token]

        ax.add_patch(mpatches.FancyBboxPatch((i * 1.2 + 0.5, 2), 0.8, 0.6,
                                              boxstyle='round,pad=0.02',
                                              facecolor=color, edgecolor='white', linewidth=1.5))
        ax.text(i * 1.2 + 0.9, 2.3, token,
                ha='center', va='center', fontsize=14, fontweight='bold', color='white')

    # Arrows from all positions to target
    for i in range(len(sequence)):
        if i != target_pos:
            if i < target_pos:
                ax.annotate('', xy=(target_pos * 1.2 + 0.5, 2.3), xytext=(i * 1.2 + 1.3, 2.3),
                            arrowprops=dict(arrowstyle='->', color='#1f77b4', lw=2, alpha=0.7))
            else:
                ax.annotate('', xy=(target_pos * 1.2 + 1.3, 2.3), xytext=(i * 1.2 + 0.5, 2.3),
                            arrowprops=dict(arrowstyle='->', color='#1f77b4', lw=2, alpha=0.7))

    ax.text(3, 1.4, 'All surrounding context informs prediction', ha='center', fontsize=10)
    ax.text(3, 1.0, 'Optimal for understanding / embedding tasks', ha='center', fontsize=9, style='italic')

    ax.set_xlim(0, 6.5)
    ax.set_ylim(0.7, 3)
    ax.axis('off')
    ax.set_title('A. Bidirectional Context (MLM)', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '03-A-fig-bidirectional-vs-autoregressive.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

def create_panel_b():
    """Causal context in autoregressive models"""
    fig, ax = plt.subplots(figsize=(7, 4))

    sequence = ['A', 'T', 'C', 'G', '?']
    target_pos = 4

    for i, token in enumerate(sequence):
        if token == '?':
            color = COLORS['mask']
        else:
            color = COLORS[token]

        ax.add_patch(mpatches.FancyBboxPatch((i * 1.2 + 0.5, 2), 0.8, 0.6,
                                              boxstyle='round,pad=0.02',
                                              facecolor=color, edgecolor='white', linewidth=1.5))
        ax.text(i * 1.2 + 0.9, 2.3, token,
                ha='center', va='center', fontsize=14, fontweight='bold', color='white')

    # Arrows only from left positions to target
    for i in range(target_pos):
        ax.annotate('', xy=(target_pos * 1.2 + 0.5, 2.3), xytext=(i * 1.2 + 1.3, 2.3),
                    arrowprops=dict(arrowstyle='->', color='#d62728', lw=2, alpha=0.7))

    # X over right side
    ax.text(5.8, 2.3, '✗', fontsize=20, ha='center', va='center', color='#d62728')
    ax.text(5.8, 1.8, 'No future\ncontext', ha='center', fontsize=8, color='#d62728')

    ax.text(3, 1.2, 'Only past tokens visible (causal mask)', ha='center', fontsize=10)
    ax.text(3, 0.8, 'Optimal for generation / sampling tasks', ha='center', fontsize=9, style='italic')

    ax.set_xlim(0, 7)
    ax.set_ylim(0.5, 3)
    ax.axis('off')
    ax.set_title('B. Causal Context (Autoregressive)', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '03-B-fig-bidirectional-vs-autoregressive.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

if __name__ == '__main__':
    create_panel_a()
    create_panel_b()
    print("All bidirectional vs autoregressive panels generated.")
