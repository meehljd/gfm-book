#!/usr/bin/env python3
"""
Figure 6.1: Convolutional Pattern Detection
Three-panel figure showing CNN as motif scanner.
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

COLORS = {
    'A': '#2ca02c', 'T': '#d62728', 'C': '#1f77b4', 'G': '#ff7f0e',
    'filter': '#9467bd', 'activation': '#d62728',
}

def create_panel_a():
    """Sliding convolution"""
    fig, ax = plt.subplots(figsize=(8, 4))

    sequence = "ATCGATCGATCG"

    # Draw sequence
    for i, base in enumerate(sequence):
        ax.text(i * 0.5 + 0.25, 2.5, base, ha='center', va='center',
                fontsize=12, fontweight='bold', color=COLORS[base],
                bbox=dict(boxstyle='round,pad=0.1', facecolor='white', edgecolor=COLORS[base], linewidth=1.5))

    # Draw sliding filter window at multiple positions
    filter_width = 4
    positions = [0, 2, 4]

    for pos_idx, pos in enumerate(positions):
        y = 1.5 - pos_idx * 0.5
        x_start = pos * 0.5 + 0.05
        x_end = (pos + filter_width) * 0.5 + 0.45

        # Filter window
        rect = mpatches.FancyBboxPatch((x_start, y - 0.15), x_end - x_start, 0.3,
                                        boxstyle='round,pad=0.02',
                                        facecolor=COLORS['filter'], alpha=0.3,
                                        edgecolor=COLORS['filter'], linewidth=2)
        ax.add_patch(rect)

        # Arrow and output
        ax.annotate('', xy=(6.5, y), xytext=(x_end + 0.1, y),
                    arrowprops=dict(arrowstyle='->', color='#555555', lw=1))

        # Output value (simulated activation)
        activation = np.random.uniform(0.2, 0.9)
        ax.text(7, y, f'{activation:.2f}', ha='center', va='center',
                fontsize=10, color=COLORS['activation'] if activation > 0.5 else '#555555',
                fontweight='bold' if activation > 0.5 else 'normal')

    ax.text(7, 0.2, 'Activation', ha='center', fontsize=9, style='italic')

    ax.set_xlim(-0.2, 8)
    ax.set_ylim(-0.1, 3)
    ax.axis('off')
    ax.set_title('A. Sliding Convolution', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '01-A-fig-conv-pattern-detector.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

def create_panel_b():
    """Learned filter as sequence logo"""
    fig, ax = plt.subplots(figsize=(6, 4))

    # Simulate a PWM for a motif like TATA box
    bases = ['A', 'T', 'C', 'G']
    positions = 6

    # TATA-like motif weights
    weights = np.array([
        [0.1, 0.7, 0.1, 0.1],  # mostly T
        [0.8, 0.1, 0.05, 0.05],  # mostly A
        [0.1, 0.7, 0.1, 0.1],  # mostly T
        [0.8, 0.1, 0.05, 0.05],  # mostly A
        [0.3, 0.3, 0.2, 0.2],  # mixed
        [0.3, 0.3, 0.2, 0.2],  # mixed
    ])

    # Draw simplified logo
    for pos in range(positions):
        # Sort by weight for stacking
        sorted_idx = np.argsort(weights[pos])

        y_offset = 0
        for idx in sorted_idx:
            height = weights[pos, idx] * 2  # Scale for visibility
            if height > 0.1:
                ax.text(pos + 0.5, y_offset + height/2, bases[idx],
                        ha='center', va='center',
                        fontsize=int(height * 20) + 8, fontweight='bold',
                        color=COLORS[bases[idx]], alpha=0.8)
                y_offset += height

    ax.set_xlim(0, positions)
    ax.set_ylim(0, 2.5)
    ax.set_xlabel('Position in Filter', fontweight='bold')
    ax.set_ylabel('Information (bits)', fontweight='bold')

    ax.text(3, 2.3, 'Learned filter weights ≈ Position Weight Matrix',
            ha='center', fontsize=9, style='italic')

    ax.set_title('B. Learned Filter as Sequence Logo', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '01-B-fig-conv-pattern-detector.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

def create_panel_c():
    """Multiple filter diversity"""
    fig, ax = plt.subplots(figsize=(7, 5))

    np.random.seed(42)
    n_filters = 6
    motif_names = ['TATA box', 'GC box', 'CAAT box', 'E-box', 'AP-1', 'Unknown']

    for i in range(n_filters):
        y = (n_filters - i - 1) * 0.7 + 0.3

        # Filter representation as colored bars
        filter_vals = np.random.rand(8)
        for j, val in enumerate(filter_vals):
            color = plt.cm.Blues(val)
            rect = mpatches.Rectangle((j * 0.3 + 0.1, y), 0.28, 0.5,
                                        facecolor=color, edgecolor='white', linewidth=0.5)
            ax.add_patch(rect)

        ax.text(2.8, y + 0.25, f'Filter {i+1}', ha='left', va='center', fontsize=9)
        ax.text(4.5, y + 0.25, f'→ {motif_names[i]}', ha='left', va='center',
                fontsize=9, style='italic', color='#555555')

    ax.set_xlim(0, 6.5)
    ax.set_ylim(0, n_filters * 0.7 + 0.5)
    ax.axis('off')

    ax.text(3, 0, 'Different filters learn different sequence patterns',
            ha='center', fontsize=9, style='italic')

    ax.set_title('C. Multiple Filter Diversity', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '01-C-fig-conv-pattern-detector.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

if __name__ == '__main__':
    create_panel_a()
    create_panel_b()
    create_panel_c()
    print("All conv pattern detector panels generated.")
