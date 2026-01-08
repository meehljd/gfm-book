#!/usr/bin/env python3
"""
Figure 5.3: Embedding Space Organization
Three-panel figure showing how embeddings organize by different properties.
"""

import matplotlib.pyplot as plt
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
    'axes.spines.top': False,
    'axes.spines.right': False,
})

np.random.seed(42)

def create_panel_a():
    """GC content organization"""
    fig, ax = plt.subplots(figsize=(5, 4))

    n_points = 200

    # Low GC (AT-rich) cluster
    low_gc_x = np.random.normal(-1.5, 0.4, n_points // 2)
    low_gc_y = np.random.normal(-0.5, 0.4, n_points // 2)
    low_gc_values = np.random.uniform(0.2, 0.4, n_points // 2)

    # High GC cluster
    high_gc_x = np.random.normal(1.5, 0.4, n_points // 2)
    high_gc_y = np.random.normal(0.5, 0.4, n_points // 2)
    high_gc_values = np.random.uniform(0.6, 0.8, n_points // 2)

    x = np.concatenate([low_gc_x, high_gc_x])
    y = np.concatenate([low_gc_y, high_gc_y])
    gc = np.concatenate([low_gc_values, high_gc_values])

    scatter = ax.scatter(x, y, c=gc, cmap='RdYlBu_r', s=30, alpha=0.7, edgecolors='white', linewidths=0.5)

    cbar = plt.colorbar(scatter, ax=ax, shrink=0.8)
    cbar.set_label('GC Content', fontweight='bold')

    ax.annotate('AT-rich\nsequences', xy=(-1.5, -0.5), fontsize=9, ha='center',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#cccccc'))
    ax.annotate('GC-rich\nsequences', xy=(1.5, 0.5), fontsize=9, ha='center',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#cccccc'))

    ax.set_xlabel('Embedding Dimension 1', fontweight='bold')
    ax.set_ylabel('Embedding Dimension 2', fontweight='bold')
    ax.set_title('A. GC Content Organization', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '03-A-fig-ch05-embedding-space.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

def create_panel_b():
    """Token frequency organization"""
    fig, ax = plt.subplots(figsize=(5, 4))

    n_points = 200

    # Common tokens (center, tight cluster)
    common_x = np.random.normal(0, 0.3, n_points // 2)
    common_y = np.random.normal(0, 0.3, n_points // 2)
    common_freq = np.random.uniform(0.7, 1.0, n_points // 2)

    # Rare tokens (periphery, spread out)
    angles = np.random.uniform(0, 2*np.pi, n_points // 2)
    radii = np.random.uniform(1.5, 2.5, n_points // 2)
    rare_x = radii * np.cos(angles)
    rare_y = radii * np.sin(angles)
    rare_freq = np.random.uniform(0.0, 0.3, n_points // 2)

    x = np.concatenate([common_x, rare_x])
    y = np.concatenate([common_y, rare_y])
    freq = np.concatenate([common_freq, rare_freq])

    scatter = ax.scatter(x, y, c=freq, cmap='viridis', s=30, alpha=0.7, edgecolors='white', linewidths=0.5)

    cbar = plt.colorbar(scatter, ax=ax, shrink=0.8)
    cbar.set_label('Token Frequency', fontweight='bold')

    ax.annotate('Common\ntokens', xy=(0, 0), fontsize=9, ha='center',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#cccccc'))
    ax.annotate('Rare tokens\n(periphery)', xy=(2, 1.5), fontsize=9, ha='center',
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#cccccc'))

    ax.set_xlabel('Embedding Dimension 1', fontweight='bold')
    ax.set_ylabel('Embedding Dimension 2', fontweight='bold')
    ax.set_title('B. Token Frequency Organization', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '03-B-fig-ch05-embedding-space.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

def create_panel_c():
    """Genomic context organization"""
    fig, ax = plt.subplots(figsize=(5, 4))

    n_per_class = 50

    # Different genomic contexts
    contexts = {
        'Promoter': (np.random.normal(-1.5, 0.3, n_per_class), np.random.normal(1.5, 0.3, n_per_class), '#d62728'),
        'Exon': (np.random.normal(1.5, 0.3, n_per_class), np.random.normal(1.5, 0.3, n_per_class), '#1f77b4'),
        'Intron': (np.random.normal(0, 0.5, n_per_class), np.random.normal(-0.5, 0.4, n_per_class), '#7f7f7f'),
        'Intergenic': (np.random.normal(1, 0.4, n_per_class), np.random.normal(-1.5, 0.3, n_per_class), '#2ca02c'),
    }

    for context, (x, y, color) in contexts.items():
        ax.scatter(x, y, c=color, s=40, alpha=0.7, label=context, edgecolors='white', linewidths=0.5)

    ax.legend(loc='lower left', fontsize=8, frameon=True)

    ax.set_xlabel('Embedding Dimension 1', fontweight='bold')
    ax.set_ylabel('Embedding Dimension 2', fontweight='bold')
    ax.set_title('C. Genomic Context Organization', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '03-C-fig-ch05-embedding-space.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

if __name__ == '__main__':
    create_panel_a()
    create_panel_b()
    create_panel_c()
    print("All embedding space panels generated.")
