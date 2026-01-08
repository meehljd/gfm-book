#!/usr/bin/env python3
"""
Figure 7.1: Self-Attention Mechanism
Five-panel figure showing the self-attention computation steps.
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

def draw_matrix(ax, matrix, x_offset, y_offset, cell_size=0.3, cmap='Blues', show_values=True, title=None):
    """Helper to draw a matrix visualization."""
    n_rows, n_cols = matrix.shape
    for i in range(n_rows):
        for j in range(n_cols):
            color = plt.cm.get_cmap(cmap)(matrix[i, j] / matrix.max())
            rect = mpatches.Rectangle((x_offset + j * cell_size, y_offset - i * cell_size),
                                        cell_size * 0.9, cell_size * 0.9,
                                        facecolor=color, edgecolor='white', linewidth=0.5)
            ax.add_patch(rect)
            if show_values and n_cols <= 4:
                ax.text(x_offset + j * cell_size + cell_size * 0.45,
                        y_offset - i * cell_size + cell_size * 0.45,
                        f'{matrix[i, j]:.1f}', ha='center', va='center', fontsize=7)
    if title:
        ax.text(x_offset + n_cols * cell_size / 2, y_offset + 0.3, title,
                ha='center', fontsize=9, fontweight='bold')

def create_panel_a():
    """Input embeddings"""
    fig, ax = plt.subplots(figsize=(6, 4))

    # Show sequence tokens with embeddings
    tokens = ['A', 'T', 'C', 'G']
    colors = ['#2ca02c', '#d62728', '#1f77b4', '#ff7f0e']

    for i, (token, color) in enumerate(zip(tokens, colors)):
        # Token
        ax.text(i * 1.2 + 0.3, 2.5, token, ha='center', va='center',
                fontsize=14, fontweight='bold', color=color,
                bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor=color, linewidth=1.5))

        # Arrow
        ax.annotate('', xy=(i * 1.2 + 0.3, 1.8), xytext=(i * 1.2 + 0.3, 2.2),
                    arrowprops=dict(arrowstyle='->', color='#555555', lw=1))

        # Embedding vector (vertical bar representation)
        np.random.seed(i)
        embed = np.random.randn(4)
        for j, val in enumerate(embed):
            c = '#1f77b4' if val > 0 else '#d62728'
            ax.bar(i * 1.2 + 0.3 + (j - 1.5) * 0.12, abs(val) * 0.3, bottom=1.2,
                   width=0.1, color=c, alpha=0.7)

    ax.text(2.1, 0.8, 'Each token → d-dimensional embedding', ha='center', fontsize=9, style='italic')

    ax.set_xlim(-0.5, 5)
    ax.set_ylim(0.5, 3)
    ax.axis('off')
    ax.set_title('A. Input Embeddings', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '01-A-fig-self-attention.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

def create_panel_b():
    """Query, Key, Value projections"""
    fig, ax = plt.subplots(figsize=(7, 4))

    # Input embedding
    ax.add_patch(mpatches.FancyBboxPatch((0.5, 1.3), 1.2, 0.6,
                                          boxstyle='round,pad=0.02',
                                          facecolor='#aec7e8', edgecolor='#1f77b4', linewidth=1.5))
    ax.text(1.1, 1.6, 'Input X', ha='center', va='center', fontsize=10)

    # Three projections
    projections = [('Query Q', '#d62728', 3), ('Key K', '#2ca02c', 4.5), ('Value V', '#9467bd', 6)]

    for label, color, y_pos in projections:
        ax.annotate('', xy=(y_pos - 1, 1.6), xytext=(1.8, 1.6),
                    arrowprops=dict(arrowstyle='->', color='#555555', lw=1))
        ax.add_patch(mpatches.FancyBboxPatch((y_pos - 0.6, 1.3), 1.2, 0.6,
                                              boxstyle='round,pad=0.02',
                                              facecolor=color, alpha=0.3,
                                              edgecolor=color, linewidth=1.5))
        ax.text(y_pos, 1.6, label, ha='center', va='center', fontsize=10, fontweight='bold')
        ax.text(y_pos, 0.9, f'W{label[0]}', ha='center', fontsize=9, style='italic')

    ax.text(3.5, 0.5, 'Linear projections: Q = XWQ, K = XWK, V = XWV', ha='center', fontsize=9, style='italic')

    ax.set_xlim(0, 7)
    ax.set_ylim(0.2, 2.3)
    ax.axis('off')
    ax.set_title('B. Query, Key, Value Projections', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '01-B-fig-self-attention.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

def create_panel_c():
    """Attention score matrix"""
    fig, ax = plt.subplots(figsize=(5, 4))

    np.random.seed(42)
    scores = np.random.randn(4, 4)

    draw_matrix(ax, scores, 0.5, 2.8, cell_size=0.5, cmap='RdBu_r', show_values=True, title='QKᵀ / √d')

    # Labels
    tokens = ['A', 'T', 'C', 'G']
    for i, token in enumerate(tokens):
        ax.text(0.3, 2.55 - i * 0.5, token, ha='center', va='center', fontsize=10, fontweight='bold')
        ax.text(0.75 + i * 0.5, 3.1, token, ha='center', va='center', fontsize=10, fontweight='bold')

    ax.text(1.5, 0.5, 'Raw attention scores\n(before softmax)', ha='center', fontsize=9, style='italic')

    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3.5)
    ax.axis('off')
    ax.set_title('C. Attention Score Matrix', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '01-C-fig-self-attention.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

def create_panel_d():
    """Attention weight matrix"""
    fig, ax = plt.subplots(figsize=(5, 4))

    np.random.seed(42)
    scores = np.random.randn(4, 4)
    weights = np.exp(scores) / np.exp(scores).sum(axis=1, keepdims=True)

    draw_matrix(ax, weights, 0.5, 2.8, cell_size=0.5, cmap='Blues', show_values=True, title='softmax(QKᵀ / √d)')

    tokens = ['A', 'T', 'C', 'G']
    for i, token in enumerate(tokens):
        ax.text(0.3, 2.55 - i * 0.5, token, ha='center', va='center', fontsize=10, fontweight='bold')
        ax.text(0.75 + i * 0.5, 3.1, token, ha='center', va='center', fontsize=10, fontweight='bold')

    ax.text(1.5, 0.5, 'Normalized weights\n(rows sum to 1)', ha='center', fontsize=9, style='italic')

    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3.5)
    ax.axis('off')
    ax.set_title('D. Attention Weight Matrix', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '01-D-fig-self-attention.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

def create_panel_e():
    """Weighted value aggregation"""
    fig, ax = plt.subplots(figsize=(6, 4))

    # Attention weights × Values = Output
    ax.add_patch(mpatches.FancyBboxPatch((0.3, 1.2), 0.8, 0.8,
                                          boxstyle='round,pad=0.02',
                                          facecolor='#1f77b4', alpha=0.3,
                                          edgecolor='#1f77b4', linewidth=1.5))
    ax.text(0.7, 1.6, 'Attn\nWeights', ha='center', va='center', fontsize=9)

    ax.text(1.4, 1.6, '×', ha='center', va='center', fontsize=16, fontweight='bold')

    ax.add_patch(mpatches.FancyBboxPatch((1.7, 1.2), 0.8, 0.8,
                                          boxstyle='round,pad=0.02',
                                          facecolor='#9467bd', alpha=0.3,
                                          edgecolor='#9467bd', linewidth=1.5))
    ax.text(2.1, 1.6, 'Values', ha='center', va='center', fontsize=9)

    ax.text(2.8, 1.6, '=', ha='center', va='center', fontsize=16, fontweight='bold')

    ax.add_patch(mpatches.FancyBboxPatch((3.1, 1.2), 0.8, 0.8,
                                          boxstyle='round,pad=0.02',
                                          facecolor='#2ca02c', alpha=0.3,
                                          edgecolor='#2ca02c', linewidth=1.5))
    ax.text(3.5, 1.6, 'Output', ha='center', va='center', fontsize=9)

    ax.text(2.1, 0.8, 'Each output = weighted sum of all values', ha='center', fontsize=9, style='italic')

    ax.set_xlim(0, 4.5)
    ax.set_ylim(0.5, 2.5)
    ax.axis('off')
    ax.set_title('E. Weighted Value Aggregation', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '01-E-fig-self-attention.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

if __name__ == '__main__':
    create_panel_a()
    create_panel_b()
    create_panel_c()
    create_panel_d()
    create_panel_e()
    print("All self-attention panels generated.")
