#!/usr/bin/env python3
"""
Figure 5.1: Tokenization Comparison
Four-panel figure comparing tokenization strategies.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_2" / "ch05"
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

# Shared sequence
SEQUENCE = "ATCGATCG"
COLORS = {
    'A': '#2ca02c', 'T': '#d62728', 'C': '#1f77b4', 'G': '#ff7f0e',
    'token': '#9467bd', 'embed': '#c5b0d5',
}

def create_panel_a():
    """One-hot encoding"""
    fig, ax = plt.subplots(figsize=(7, 4))

    bases = ['A', 'T', 'C', 'G']
    seq_len = len(SEQUENCE)

    # Create matrix visualization
    matrix = np.zeros((4, seq_len))
    for i, base in enumerate(SEQUENCE):
        matrix[bases.index(base), i] = 1

    # Draw matrix
    for i in range(4):
        for j in range(seq_len):
            color = '#1f77b4' if matrix[i, j] == 1 else '#f0f0f0'
            rect = mpatches.FancyBboxPatch((j*0.8 + 0.1, (3-i)*0.8 + 0.1), 0.7, 0.7,
                                            boxstyle='round,pad=0.02',
                                            facecolor=color, edgecolor='white', linewidth=1.5)
            ax.add_patch(rect)
            text = '1' if matrix[i, j] == 1 else '0'
            ax.text(j*0.8 + 0.45, (3-i)*0.8 + 0.45, text,
                    ha='center', va='center', fontsize=11, fontweight='bold',
                    color='white' if matrix[i, j] == 1 else '#888888')

    # Row labels
    for i, base in enumerate(bases):
        ax.text(-0.1, (3-i)*0.8 + 0.45, base, ha='right', va='center',
                fontsize=12, fontweight='bold', color=COLORS[base])

    # Column labels
    for j, base in enumerate(SEQUENCE):
        ax.text(j*0.8 + 0.45, 3.5, base, ha='center', va='bottom',
                fontsize=12, fontweight='bold', color=COLORS[base])

    ax.set_xlim(-0.3, seq_len * 0.8 + 0.1)
    ax.set_ylim(-0.1, 4)
    ax.axis('off')

    ax.text(3.2, -0.4, 'Dimension: 4 × sequence length', ha='center', fontsize=9, style='italic')
    ax.set_title('A. One-Hot Encoding', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '01-A-fig-ch05-tokenization-comparison.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

def create_panel_b():
    """Overlapping k-mers"""
    fig, ax = plt.subplots(figsize=(7, 4))

    k = 3  # 3-mers for simplicity in visualization
    kmers = [SEQUENCE[i:i+k] for i in range(len(SEQUENCE) - k + 1)]

    # Draw sequence
    for i, base in enumerate(SEQUENCE):
        ax.text(i * 0.6 + 0.3, 2.5, base, ha='center', va='center',
                fontsize=14, fontweight='bold', color=COLORS[base],
                bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor=COLORS[base], linewidth=1.5))

    # Draw k-mer windows
    for i, kmer in enumerate(kmers):
        y = 1.5 - i * 0.35
        # Window bracket
        x_start = i * 0.6 + 0.1
        x_end = (i + k - 1) * 0.6 + 0.5

        ax.plot([x_start, x_end], [y, y], 'k-', linewidth=2)
        ax.plot([x_start, x_start], [y, y + 0.1], 'k-', linewidth=2)
        ax.plot([x_end, x_end], [y, y + 0.1], 'k-', linewidth=2)

        ax.text(x_end + 0.3, y, f'→ {kmer}', ha='left', va='center',
                fontsize=10, fontfamily='monospace', color=COLORS['token'])

    ax.set_xlim(-0.2, 6)
    ax.set_ylim(-0.5, 3)
    ax.axis('off')

    ax.text(2.5, -0.3, f'Overlapping {k}-mers: {len(kmers)} tokens', ha='center', fontsize=9, style='italic')
    ax.set_title('B. Overlapping K-mers', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '01-B-fig-ch05-tokenization-comparison.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

def create_panel_c():
    """BPE tokenization"""
    fig, ax = plt.subplots(figsize=(7, 4))

    # Draw original sequence
    for i, base in enumerate(SEQUENCE):
        ax.text(i * 0.5 + 0.25, 2.5, base, ha='center', va='center',
                fontsize=14, fontweight='bold', color=COLORS[base])

    ax.text(-0.5, 2.5, 'Input:', ha='right', va='center', fontsize=10)

    # Show BPE merge process
    stages = [
        list(SEQUENCE),
        ['AT', 'C', 'G', 'AT', 'C', 'G'],
        ['ATC', 'G', 'ATC', 'G'],
        ['ATCG', 'ATCG'],
    ]

    for stage_idx, stage in enumerate(stages):
        y = 1.8 - stage_idx * 0.5
        x_offset = 0

        ax.text(-0.5, y, f'Step {stage_idx}:', ha='right', va='center', fontsize=9, color='#555555')

        for token in stage:
            width = len(token) * 0.4
            rect = mpatches.FancyBboxPatch((x_offset, y - 0.15), width, 0.3,
                                            boxstyle='round,pad=0.02',
                                            facecolor=COLORS['token'], alpha=0.3,
                                            edgecolor=COLORS['token'], linewidth=1)
            ax.add_patch(rect)
            ax.text(x_offset + width/2, y, token, ha='center', va='center',
                    fontsize=10, fontfamily='monospace')
            x_offset += width + 0.2

    ax.set_xlim(-1, 5)
    ax.set_ylim(-0.3, 3)
    ax.axis('off')

    ax.text(2, -0.1, 'BPE merges frequent pairs → variable-length tokens',
            ha='center', fontsize=9, style='italic')
    ax.set_title('C. Byte-Pair Encoding (BPE)', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '01-C-fig-ch05-tokenization-comparison.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

def create_panel_d():
    """Single-nucleotide with learned embeddings"""
    fig, ax = plt.subplots(figsize=(7, 4))

    # Draw sequence tokens
    for i, base in enumerate(SEQUENCE):
        ax.text(i * 0.7 + 0.35, 2.5, base, ha='center', va='center',
                fontsize=14, fontweight='bold', color=COLORS[base],
                bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor=COLORS[base], linewidth=1.5))

    # Arrow to embeddings
    ax.annotate('', xy=(3.2, 1.8), xytext=(3.2, 2.2),
                arrowprops=dict(arrowstyle='->', color='#555555', lw=1.5))
    ax.text(3.2, 2.0, 'Embedding\nLookup', ha='center', va='center', fontsize=8)

    # Draw embedding vectors
    np.random.seed(42)
    for i in range(len(SEQUENCE)):
        # Draw small bar chart representing embedding vector
        x_start = i * 0.7 + 0.1
        embed_vals = np.random.randn(4) * 0.15

        for j, val in enumerate(embed_vals):
            color = '#1f77b4' if val > 0 else '#d62728'
            ax.bar(x_start + j*0.12, val, width=0.1, bottom=1.0,
                   color=color, alpha=0.7, edgecolor='white', linewidth=0.5)

    ax.axhline(y=1.0, xmin=0.05, xmax=0.95, color='#cccccc', linestyle='-', linewidth=0.5)

    ax.text(3.2, 0.5, 'Each nucleotide → d-dimensional learned vector',
            ha='center', fontsize=9, style='italic')

    ax.set_xlim(-0.2, 6.5)
    ax.set_ylim(0.3, 3)
    ax.axis('off')
    ax.set_title('D. Single-Nucleotide with Learned Embeddings', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '01-D-fig-ch05-tokenization-comparison.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

if __name__ == '__main__':
    create_panel_a()
    create_panel_b()
    create_panel_c()
    create_panel_d()
    print("All tokenization comparison panels generated.")
