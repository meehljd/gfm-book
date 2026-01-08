#!/usr/bin/env python3
"""
Figure 8.1: Pretraining Objectives
Three-panel figure showing MLM, NTP, and contrastive learning.
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
    'mask': '#7f7f7f', 'positive': '#2ca02c', 'negative': '#d62728',
}

def create_panel_a():
    """Masked language modeling"""
    fig, ax = plt.subplots(figsize=(7, 4))

    sequence = ['A', 'T', '[M]', 'G', 'A', 'T', '[M]', 'G']
    original = ['A', 'T', 'C', 'G', 'A', 'T', 'C', 'G']

    # Draw input (masked)
    for i, token in enumerate(sequence):
        if token == '[M]':
            color = COLORS['mask']
            text_color = 'white'
        else:
            color = COLORS[token]
            text_color = 'white'

        ax.add_patch(mpatches.FancyBboxPatch((i * 0.7 + 0.3, 2), 0.5, 0.5,
                                              boxstyle='round,pad=0.02',
                                              facecolor=color, edgecolor='white', linewidth=1.5))
        ax.text(i * 0.7 + 0.55, 2.25, token if token != '[M]' else '?',
                ha='center', va='center', fontsize=12, fontweight='bold', color=text_color)

    ax.text(3.3, 2.8, 'Input (15% masked)', ha='center', fontsize=10)

    # Arrow to model
    ax.annotate('', xy=(3.3, 1.5), xytext=(3.3, 1.9),
                arrowprops=dict(arrowstyle='->', color='#555555', lw=1.5))

    # Model
    ax.add_patch(mpatches.FancyBboxPatch((2.3, 1.1), 2, 0.4,
                                          boxstyle='round,pad=0.02',
                                          facecolor='#9467bd', edgecolor='#333333', linewidth=1.5))
    ax.text(3.3, 1.3, 'Encoder Model', ha='center', va='center', fontsize=10, color='white')

    # Arrow to predictions
    ax.annotate('', xy=(3.3, 0.6), xytext=(3.3, 1.0),
                arrowprops=dict(arrowstyle='->', color='#555555', lw=1.5))

    # Predictions
    ax.text(3.3, 0.4, 'Predict: C (pos 2), C (pos 6)', ha='center', fontsize=10)
    ax.text(3.3, 0.1, 'Loss: cross-entropy on masked positions', ha='center', fontsize=9, style='italic')

    ax.set_xlim(0, 6.5)
    ax.set_ylim(-0.2, 3.2)
    ax.axis('off')
    ax.set_title('A. Masked Language Modeling (MLM)', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '01-A-fig-pretraining-objectives.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

def create_panel_b():
    """Next-token prediction"""
    fig, ax = plt.subplots(figsize=(7, 4))

    sequence = ['A', 'T', 'C', 'G', 'A', 'T', 'C', '?']

    # Draw sequence
    for i, token in enumerate(sequence):
        if token == '?':
            color = COLORS['mask']
        else:
            color = COLORS[token]

        ax.add_patch(mpatches.FancyBboxPatch((i * 0.7 + 0.3, 2), 0.5, 0.5,
                                              boxstyle='round,pad=0.02',
                                              facecolor=color, edgecolor='white', linewidth=1.5))
        ax.text(i * 0.7 + 0.55, 2.25, token,
                ha='center', va='center', fontsize=12, fontweight='bold', color='white')

        # Causal mask arrows (each position only sees left)
        if i > 0 and i < 7:
            for j in range(i):
                ax.annotate('', xy=(j * 0.7 + 0.55, 1.95), xytext=(i * 0.7 + 0.55, 2),
                            arrowprops=dict(arrowstyle='->', color='#cccccc', lw=0.5, alpha=0.5))

    ax.text(3.3, 2.8, 'Left-to-right generation', ha='center', fontsize=10)

    # Arrow to prediction
    ax.annotate('', xy=(5.35, 1.5), xytext=(5.35, 1.9),
                arrowprops=dict(arrowstyle='->', color='#d62728', lw=2))

    ax.text(5.35, 1.3, 'Predict next: G', ha='center', fontsize=10, fontweight='bold')
    ax.text(3.3, 0.8, 'Each position predicts the next token', ha='center', fontsize=9, style='italic')

    ax.set_xlim(0, 7)
    ax.set_ylim(0.5, 3.2)
    ax.axis('off')
    ax.set_title('B. Next-Token Prediction (Autoregressive)', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '01-B-fig-pretraining-objectives.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

def create_panel_c():
    """Contrastive learning"""
    fig, ax = plt.subplots(figsize=(7, 4))

    # Anchor sequence
    ax.add_patch(mpatches.FancyBboxPatch((0.5, 2), 1.5, 0.6,
                                          boxstyle='round,pad=0.02',
                                          facecolor='#1f77b4', edgecolor='#333333', linewidth=1.5))
    ax.text(1.25, 2.3, 'Anchor\n(human)', ha='center', va='center', fontsize=9, color='white')

    # Positive (ortholog)
    ax.add_patch(mpatches.FancyBboxPatch((3.5, 2.8), 1.5, 0.6,
                                          boxstyle='round,pad=0.02',
                                          facecolor=COLORS['positive'], edgecolor='#333333', linewidth=1.5))
    ax.text(4.25, 3.1, 'Positive\n(mouse ortholog)', ha='center', va='center', fontsize=9, color='white')

    # Connection to positive
    ax.annotate('', xy=(3.4, 3.1), xytext=(2.1, 2.3),
                arrowprops=dict(arrowstyle='->', color=COLORS['positive'], lw=2))
    ax.text(2.8, 2.9, 'pull close', fontsize=8, color=COLORS['positive'])

    # Negatives
    for i in range(3):
        y = 1.3 - i * 0.6
        ax.add_patch(mpatches.FancyBboxPatch((3.5, y), 1.5, 0.5,
                                              boxstyle='round,pad=0.02',
                                              facecolor=COLORS['negative'], alpha=0.5,
                                              edgecolor='#333333', linewidth=1.5))
        ax.text(4.25, y + 0.25, f'Negative {i+1}', ha='center', va='center', fontsize=9)

        # Push away
        ax.annotate('', xy=(2.1, 2.1), xytext=(3.4, y + 0.25),
                    arrowprops=dict(arrowstyle='->', color=COLORS['negative'], lw=1, alpha=0.5))

    ax.text(2.5, -0.1, 'push apart', fontsize=8, color=COLORS['negative'])

    ax.text(3, 3.8, 'Learn similar embeddings for functional equivalents',
            ha='center', fontsize=9, style='italic')

    ax.set_xlim(0, 5.5)
    ax.set_ylim(-0.5, 4.1)
    ax.axis('off')
    ax.set_title('C. Contrastive Learning', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '01-C-fig-pretraining-objectives.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

if __name__ == '__main__':
    create_panel_a()
    create_panel_b()
    create_panel_c()
    print("All pretraining objective panels generated.")
