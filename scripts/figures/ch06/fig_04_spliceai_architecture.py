#!/usr/bin/env python3
"""
Figure 6.4: SpliceAI Architecture
Two-panel figure showing dilated convolutions and residual blocks.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_2" / "ch06"
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
    """Dilated convolutions"""
    fig, ax = plt.subplots(figsize=(8, 5))

    # Show sequence positions
    n_positions = 16
    for i in range(n_positions):
        ax.add_patch(mpatches.Rectangle((i * 0.5, 3), 0.4, 0.4,
                                          facecolor='#aec7e8', edgecolor='#1f77b4', linewidth=1))

    ax.text(4, 3.6, 'Input Sequence', ha='center', fontsize=10, fontweight='bold')

    # Dilation rate 1 (normal conv)
    for i in [4, 5, 6]:
        ax.add_patch(mpatches.Rectangle((i * 0.5, 2.3), 0.4, 0.4,
                                          facecolor='#1f77b4', edgecolor='white', linewidth=1.5))
        ax.plot([i * 0.5 + 0.2, i * 0.5 + 0.2], [2.7, 3], 'k-', linewidth=0.8)
    ax.text(8, 2.5, 'Dilation = 1 (standard)', ha='left', fontsize=9)

    # Dilation rate 2
    for i in [3, 5, 7]:
        ax.add_patch(mpatches.Rectangle((i * 0.5, 1.6), 0.4, 0.4,
                                          facecolor='#2ca02c', edgecolor='white', linewidth=1.5))
        ax.plot([i * 0.5 + 0.2, i * 0.5 + 0.2], [2.0, 2.3], 'k-', linewidth=0.8)
    ax.text(8, 1.8, 'Dilation = 2', ha='left', fontsize=9)

    # Dilation rate 4
    for i in [1, 5, 9]:
        ax.add_patch(mpatches.Rectangle((i * 0.5, 0.9), 0.4, 0.4,
                                          facecolor='#ff7f0e', edgecolor='white', linewidth=1.5))
        ax.plot([i * 0.5 + 0.2, i * 0.5 + 0.2], [1.3, 1.6], 'k-', linewidth=0.8)
    ax.text(8, 1.1, 'Dilation = 4', ha='left', fontsize=9)

    # Output
    ax.add_patch(mpatches.Rectangle((2.3, 0.2), 0.6, 0.4,
                                      facecolor='#d62728', edgecolor='white', linewidth=1.5))
    ax.text(2.6, 0.4, 'Out', ha='center', va='center', fontsize=9, color='white')
    ax.plot([2.6, 2.6], [0.6, 0.9], 'k-', linewidth=0.8)

    ax.text(4, -0.2, 'Exponentially increasing dilation = exponential receptive field growth',
            ha='center', fontsize=9, style='italic')

    ax.set_xlim(-0.5, 10)
    ax.set_ylim(-0.5, 4)
    ax.axis('off')
    ax.set_title('A. Dilated Convolutions', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '04-A-fig-spliceai-architecture.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

def create_panel_b():
    """Residual block structure"""
    fig, ax = plt.subplots(figsize=(6, 5))

    # Main path
    blocks = [
        ('Input', 0, 4, '#aec7e8'),
        ('BatchNorm', 0, 3.2, '#98df8a'),
        ('ReLU', 0, 2.6, '#ffbb78'),
        ('Conv', 0, 2, '#1f77b4'),
        ('BatchNorm', 0, 1.4, '#98df8a'),
        ('ReLU', 0, 0.8, '#ffbb78'),
        ('Conv', 0, 0.2, '#1f77b4'),
    ]

    for label, x, y, color in blocks:
        ax.add_patch(mpatches.FancyBboxPatch((x + 0.8, y), 1.5, 0.4,
                                              boxstyle='round,pad=0.02',
                                              facecolor=color, edgecolor='#333333', linewidth=1.5))
        ax.text(x + 1.55, y + 0.2, label, ha='center', va='center', fontsize=9)

        if y > 0.2:
            ax.annotate('', xy=(x + 1.55, y), xytext=(x + 1.55, y + 0.2 - 0.3),
                        arrowprops=dict(arrowstyle='->', color='#555555', lw=1))

    # Skip connection
    ax.annotate('', xy=(3, 0.4), xytext=(3, 4.2),
                arrowprops=dict(arrowstyle='->', color='#d62728', lw=2, connectionstyle='arc3,rad=0.3'))
    ax.text(3.8, 2.2, 'Skip\nConnection', ha='left', va='center', fontsize=9, color='#d62728')

    # Addition
    ax.add_patch(mpatches.Circle((1.55, -0.3), 0.15, facecolor='white', edgecolor='#333333', linewidth=1.5))
    ax.text(1.55, -0.3, '+', ha='center', va='center', fontsize=12, fontweight='bold')

    ax.annotate('', xy=(1.55, -0.1), xytext=(1.55, 0.2),
                arrowprops=dict(arrowstyle='->', color='#555555', lw=1))
    ax.plot([3, 1.7], [0.4, -0.3], 'k-', linewidth=1)

    # Output
    ax.add_patch(mpatches.FancyBboxPatch((0.8, -0.8), 1.5, 0.4,
                                          boxstyle='round,pad=0.02',
                                          facecolor='#d62728', edgecolor='#333333', linewidth=1.5))
    ax.text(1.55, -0.6, 'Output', ha='center', va='center', fontsize=9, color='white')

    ax.annotate('', xy=(1.55, -0.5), xytext=(1.55, -0.45),
                arrowprops=dict(arrowstyle='->', color='#555555', lw=1))

    ax.set_xlim(0, 5)
    ax.set_ylim(-1.2, 4.8)
    ax.axis('off')
    ax.set_title('B. Residual Block Structure', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '04-B-fig-spliceai-architecture.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

if __name__ == '__main__':
    create_panel_a()
    create_panel_b()
    print("All SpliceAI architecture panels generated.")
