#!/usr/bin/env python3
"""
Figure 7.4: Position Encodings
Four-panel figure comparing different positional encoding strategies.
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
    'axes.spines.top': False,
    'axes.spines.right': False,
})

def create_panel_a():
    """Learned absolute positional embeddings"""
    fig, ax = plt.subplots(figsize=(6, 4))

    np.random.seed(42)
    n_positions = 8
    embed_dim = 4

    embeddings = np.random.randn(n_positions, embed_dim)

    for i in range(n_positions):
        for j in range(embed_dim):
            color = plt.cm.RdBu_r((embeddings[i, j] + 2) / 4)
            ax.add_patch(mpatches.Rectangle((j * 0.6 + 0.5, (n_positions - 1 - i) * 0.5 + 0.5),
                                              0.55, 0.45,
                                              facecolor=color, edgecolor='white', linewidth=0.5))

    # Position labels
    for i in range(n_positions):
        ax.text(0.3, (n_positions - 1 - i) * 0.5 + 0.72, f'pos {i}', ha='right', fontsize=8)

    # Dimension labels
    for j in range(embed_dim):
        ax.text(j * 0.6 + 0.77, n_positions * 0.5 + 0.6, f'd{j+1}', ha='center', fontsize=8)

    ax.text(1.8, 0.1, 'Each position gets unique learned vector', ha='center', fontsize=9, style='italic')

    ax.set_xlim(0, 3.5)
    ax.set_ylim(-0.1, 5)
    ax.axis('off')
    ax.set_title('A. Learned Absolute Embeddings', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '04-A-fig-position-encodings.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

def create_panel_b():
    """Sinusoidal positional encoding"""
    fig, ax = plt.subplots(figsize=(6, 4))

    positions = np.arange(50)
    d_model = 64
    pe = np.zeros((50, d_model))

    for pos in positions:
        for i in range(0, d_model, 2):
            pe[pos, i] = np.sin(pos / (10000 ** (i / d_model)))
            if i + 1 < d_model:
                pe[pos, i + 1] = np.cos(pos / (10000 ** (i / d_model)))

    # Show first 4 dimensions
    for i in range(4):
        ax.plot(positions, pe[:, i * 8], label=f'dim {i * 8}', linewidth=1.5, alpha=0.8)

    ax.set_xlabel('Position', fontweight='bold')
    ax.set_ylabel('Encoding Value', fontweight='bold')
    ax.legend(loc='upper right', fontsize=8)
    ax.set_xlim(0, 50)

    ax.text(25, -1.3, 'Sinusoidal waves at different frequencies', ha='center', fontsize=9, style='italic')

    ax.set_title('B. Sinusoidal Positional Encoding', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '04-B-fig-position-encodings.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

def create_panel_c():
    """ALiBi attention bias"""
    fig, ax = plt.subplots(figsize=(6, 4))

    n = 8
    # ALiBi bias matrix (linear decay with distance)
    bias = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            bias[i, j] = -abs(i - j) * 0.5

    for i in range(n):
        for j in range(n):
            color = plt.cm.RdBu_r((bias[i, j] + 4) / 8)
            ax.add_patch(mpatches.Rectangle((j * 0.5 + 0.3, (n - 1 - i) * 0.5 + 0.5),
                                              0.45, 0.45,
                                              facecolor=color, edgecolor='white', linewidth=0.5))

    ax.text(2.3, 0.1, 'Bias = -m × |query_pos - key_pos|', ha='center', fontsize=9, style='italic')
    ax.text(2.3, 4.7, 'Closer positions get higher attention', ha='center', fontsize=9)

    ax.set_xlim(0, 4.6)
    ax.set_ylim(-0.2, 5)
    ax.axis('off')
    ax.set_title('C. ALiBi (Attention with Linear Biases)', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '04-C-fig-position-encodings.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

def create_panel_d():
    """Rotary Position Embeddings (RoPE)"""
    fig, ax = plt.subplots(figsize=(6, 4))

    # Conceptual illustration of rotation
    theta = np.linspace(0, 2*np.pi, 100)

    # Draw rotation circles for different positions
    for pos in range(4):
        radius = 0.8
        center_x = pos * 1.3 + 0.8
        center_y = 1.5

        # Draw circle
        ax.plot(center_x + radius * np.cos(theta), center_y + radius * np.sin(theta),
                'k-', linewidth=0.5, alpha=0.3)

        # Draw vector at position-dependent angle
        angle = pos * np.pi / 6  # Rotation increases with position
        ax.annotate('', xy=(center_x + radius * np.cos(angle), center_y + radius * np.sin(angle)),
                    xytext=(center_x, center_y),
                    arrowprops=dict(arrowstyle='->', color='#d62728', lw=2))

        ax.text(center_x, 0.4, f'pos {pos}', ha='center', fontsize=9)

    ax.text(2.8, 2.8, 'Each position rotates embedding vectors by θ × position',
            ha='center', fontsize=9, style='italic')

    ax.set_xlim(0, 5.8)
    ax.set_ylim(0, 3.2)
    ax.axis('off')
    ax.set_title('D. Rotary Position Embeddings (RoPE)', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '04-D-fig-position-encodings.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

if __name__ == '__main__':
    create_panel_a()
    create_panel_b()
    create_panel_c()
    create_panel_d()
    print("All position encoding panels generated.")
