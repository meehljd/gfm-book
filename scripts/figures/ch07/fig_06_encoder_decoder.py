#!/usr/bin/env python3
"""
Figure 7.6: Encoder vs Decoder Architectures
Three-panel figure comparing architecture variants.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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
    """Encoder-only architecture"""
    fig, ax = plt.subplots(figsize=(5, 5))

    # Input
    ax.add_patch(mpatches.FancyBboxPatch((1, 0.5), 2.5, 0.6,
                                          boxstyle='round,pad=0.02',
                                          facecolor='#aec7e8', edgecolor='#1f77b4', linewidth=1.5))
    ax.text(2.25, 0.8, 'Input Sequence', ha='center', va='center', fontsize=10)

    # Encoder blocks
    for i in range(3):
        y = 1.5 + i * 0.9
        ax.add_patch(mpatches.FancyBboxPatch((1, y), 2.5, 0.7,
                                              boxstyle='round,pad=0.02',
                                              facecolor='#1f77b4', alpha=0.6,
                                              edgecolor='#1f77b4', linewidth=1.5))
        ax.text(2.25, y + 0.35, f'Encoder Block {i+1}', ha='center', va='center', fontsize=9, color='white')

        if i < 2:
            ax.annotate('', xy=(2.25, y + 0.8), xytext=(2.25, y + 0.7),
                        arrowprops=dict(arrowstyle='->', color='#555555', lw=1))

    ax.annotate('', xy=(2.25, 1.4), xytext=(2.25, 1.1),
                arrowprops=dict(arrowstyle='->', color='#555555', lw=1))

    # Output
    ax.add_patch(mpatches.FancyBboxPatch((1, 4.4), 2.5, 0.6,
                                          boxstyle='round,pad=0.02',
                                          facecolor='#98df8a', edgecolor='#2ca02c', linewidth=1.5))
    ax.text(2.25, 4.7, 'Contextual Embeddings', ha='center', va='center', fontsize=10)

    ax.annotate('', xy=(2.25, 4.3), xytext=(2.25, 4.1),
                arrowprops=dict(arrowstyle='->', color='#555555', lw=1))

    # Bidirectional arrows
    ax.annotate('', xy=(0.7, 2.6), xytext=(0.7, 1.9),
                arrowprops=dict(arrowstyle='<->', color='#d62728', lw=2))
    ax.text(0.5, 2.25, 'Bi-\ndirectional', ha='center', fontsize=8, color='#d62728')

    ax.text(2.25, 0.1, 'BERT-like: sees all tokens', ha='center', fontsize=9, style='italic')

    ax.set_xlim(0, 4.5)
    ax.set_ylim(-0.2, 5.3)
    ax.axis('off')
    ax.set_title('A. Encoder-Only', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '06-A-fig-encoder-decoder.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

def create_panel_b():
    """Decoder-only architecture"""
    fig, ax = plt.subplots(figsize=(5, 5))

    # Input
    ax.add_patch(mpatches.FancyBboxPatch((1, 0.5), 2.5, 0.6,
                                          boxstyle='round,pad=0.02',
                                          facecolor='#aec7e8', edgecolor='#1f77b4', linewidth=1.5))
    ax.text(2.25, 0.8, 'Input Sequence', ha='center', va='center', fontsize=10)

    # Decoder blocks
    for i in range(3):
        y = 1.5 + i * 0.9
        ax.add_patch(mpatches.FancyBboxPatch((1, y), 2.5, 0.7,
                                              boxstyle='round,pad=0.02',
                                              facecolor='#9467bd', alpha=0.6,
                                              edgecolor='#9467bd', linewidth=1.5))
        ax.text(2.25, y + 0.35, f'Decoder Block {i+1}', ha='center', va='center', fontsize=9, color='white')

        if i < 2:
            ax.annotate('', xy=(2.25, y + 0.8), xytext=(2.25, y + 0.7),
                        arrowprops=dict(arrowstyle='->', color='#555555', lw=1))

    ax.annotate('', xy=(2.25, 1.4), xytext=(2.25, 1.1),
                arrowprops=dict(arrowstyle='->', color='#555555', lw=1))

    # Output
    ax.add_patch(mpatches.FancyBboxPatch((1, 4.4), 2.5, 0.6,
                                          boxstyle='round,pad=0.02',
                                          facecolor='#ffbb78', edgecolor='#ff7f0e', linewidth=1.5))
    ax.text(2.25, 4.7, 'Next Token Prediction', ha='center', va='center', fontsize=10)

    ax.annotate('', xy=(2.25, 4.3), xytext=(2.25, 4.1),
                arrowprops=dict(arrowstyle='->', color='#555555', lw=1))

    # Causal arrow
    ax.annotate('', xy=(3.8, 2.6), xytext=(3.8, 1.9),
                arrowprops=dict(arrowstyle='->', color='#d62728', lw=2))
    ax.text(4, 2.25, 'Causal\n(left-to-\nright)', ha='left', fontsize=8, color='#d62728')

    ax.text(2.25, 0.1, 'GPT-like: autoregressive', ha='center', fontsize=9, style='italic')

    ax.set_xlim(0, 5)
    ax.set_ylim(-0.2, 5.3)
    ax.axis('off')
    ax.set_title('B. Decoder-Only', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '06-B-fig-encoder-decoder.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

def create_panel_c():
    """Hybrid CNN-Transformer"""
    fig, ax = plt.subplots(figsize=(5, 5))

    # Input
    ax.add_patch(mpatches.FancyBboxPatch((1, 0.3), 2.5, 0.5,
                                          boxstyle='round,pad=0.02',
                                          facecolor='#aec7e8', edgecolor='#1f77b4', linewidth=1.5))
    ax.text(2.25, 0.55, 'Input Sequence', ha='center', va='center', fontsize=10)

    # CNN layers
    ax.add_patch(mpatches.FancyBboxPatch((1, 1), 2.5, 0.6,
                                          boxstyle='round,pad=0.02',
                                          facecolor='#ff7f0e', alpha=0.6,
                                          edgecolor='#ff7f0e', linewidth=1.5))
    ax.text(2.25, 1.3, 'CNN Layers\n(local patterns)', ha='center', va='center', fontsize=9)

    ax.annotate('', xy=(2.25, 0.9), xytext=(2.25, 0.8),
                arrowprops=dict(arrowstyle='->', color='#555555', lw=1))

    # Pooling
    ax.add_patch(mpatches.FancyBboxPatch((1, 1.8), 2.5, 0.4,
                                          boxstyle='round,pad=0.02',
                                          facecolor='#98df8a', alpha=0.6,
                                          edgecolor='#2ca02c', linewidth=1.5))
    ax.text(2.25, 2, 'Pool / Downsample', ha='center', va='center', fontsize=9)

    ax.annotate('', xy=(2.25, 1.7), xytext=(2.25, 1.6),
                arrowprops=dict(arrowstyle='->', color='#555555', lw=1))

    # Transformer
    ax.add_patch(mpatches.FancyBboxPatch((1, 2.4), 2.5, 1.0,
                                          boxstyle='round,pad=0.02',
                                          facecolor='#1f77b4', alpha=0.6,
                                          edgecolor='#1f77b4', linewidth=1.5))
    ax.text(2.25, 2.9, 'Transformer\n(long-range)', ha='center', va='center', fontsize=9, color='white')

    ax.annotate('', xy=(2.25, 2.3), xytext=(2.25, 2.2),
                arrowprops=dict(arrowstyle='->', color='#555555', lw=1))

    # Output
    ax.add_patch(mpatches.FancyBboxPatch((1, 3.6), 2.5, 0.5,
                                          boxstyle='round,pad=0.02',
                                          facecolor='#c5b0d5', edgecolor='#9467bd', linewidth=1.5))
    ax.text(2.25, 3.85, 'Task Output', ha='center', va='center', fontsize=10)

    ax.annotate('', xy=(2.25, 3.5), xytext=(2.25, 3.4),
                arrowprops=dict(arrowstyle='->', color='#555555', lw=1))

    ax.text(2.25, -0.1, 'Enformer-like: best of both', ha='center', fontsize=9, style='italic')

    ax.set_xlim(0, 4.5)
    ax.set_ylim(-0.4, 4.4)
    ax.axis('off')
    ax.set_title('C. Hybrid CNN-Transformer', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '06-C-fig-encoder-decoder.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

if __name__ == '__main__':
    create_panel_a()
    create_panel_b()
    create_panel_c()
    print("All architecture panels generated.")
