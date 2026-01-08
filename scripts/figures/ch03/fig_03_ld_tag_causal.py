#!/usr/bin/env python3
"""
Figure 3.3: Linkage Disequilibrium and Tag vs Causal Variants
Three-panel figure showing:
A) Haplotype structure
B) LD matrix
C) Population-specific LD patterns
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

# Output path
OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_1" / "ch03"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Style settings
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans'],
    'font.size': 10,
    'axes.titlesize': 11,
    'axes.titleweight': 'bold',
    'axes.labelsize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
})

# Colors
COLORS = {
    'causal': '#d62728',       # Red for causal variant
    'tag': '#1f77b4',          # Blue for tag variants
    'allele_A': '#1f77b4',     # Blue for reference allele
    'allele_B': '#ff7f0e',     # Orange for alternate allele
    'haplotype_bg': '#f7f7f7',
}

# ===== Panel A: Haplotype Structure =====
def create_panel_a():
    fig, ax = plt.subplots(figsize=(6, 4))

    n_haplotypes = 8
    n_variants = 10
    variant_positions = np.linspace(0.1, 0.9, n_variants)

    # Create haplotype patterns (causal variant at position 5, index 4)
    # Haplotypes in LD will share alleles
    np.random.seed(42)

    # Define causal variant and correlated tag variants
    causal_idx = 4  # Middle variant is causal

    # Create haplotype matrix
    haplotypes = np.zeros((n_haplotypes, n_variants))

    # Create two main haplotype blocks
    for i in range(n_haplotypes):
        if i < 4:  # First 4 haplotypes carry the risk allele
            haplotypes[i, 2:7] = 1  # LD block carrying causal allele
        else:  # Last 4 carry reference
            haplotypes[i, 2:7] = 0
        # Add some noise outside the block
        haplotypes[i, :2] = np.random.choice([0, 1], 2)
        haplotypes[i, 7:] = np.random.choice([0, 1], 3)

    # Draw haplotypes
    cell_height = 0.8 / n_haplotypes
    cell_width = 0.08

    for i in range(n_haplotypes):
        for j in range(n_variants):
            x = variant_positions[j] - cell_width/2
            y = 0.85 - i * (cell_height + 0.02)

            color = COLORS['allele_B'] if haplotypes[i, j] == 1 else COLORS['allele_A']
            rect = mpatches.FancyBboxPatch(
                (x, y), cell_width, cell_height,
                boxstyle='round,pad=0.01',
                facecolor=color, edgecolor='white', linewidth=1
            )
            ax.add_patch(rect)

    # Mark causal variant with star
    causal_x = variant_positions[causal_idx]
    ax.plot(causal_x, 0.92, marker='*', markersize=15, color=COLORS['causal'],
            markeredgecolor='white', markeredgewidth=1)
    ax.text(causal_x, 0.96, 'Causal', ha='center', fontsize=9, fontweight='bold', color=COLORS['causal'])

    # Mark LD block
    block_left = variant_positions[2] - cell_width
    block_right = variant_positions[6] + cell_width
    ax.annotate('', xy=(block_left, 0.05), xytext=(block_right, 0.05),
                arrowprops=dict(arrowstyle='<->', color='#555555', lw=1.5))
    ax.text((block_left + block_right)/2, 0.01, 'LD Block', ha='center', fontsize=9)

    # Labels
    ax.text(0.5, -0.05, 'Genomic Position', ha='center', fontsize=10, fontweight='bold')
    ax.text(-0.02, 0.5, 'Haplotypes', ha='right', va='center', fontsize=10, fontweight='bold', rotation=90)

    # Legend
    legend_elements = [
        mpatches.Patch(facecolor=COLORS['allele_A'], edgecolor='white', label='Reference allele'),
        mpatches.Patch(facecolor=COLORS['allele_B'], edgecolor='white', label='Alternate allele'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=8)

    ax.set_xlim(0, 1)
    ax.set_ylim(-0.1, 1)
    ax.axis('off')
    ax.set_title('A. Haplotype Structure', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '03-A-fig-ld-tag-causal.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

# ===== Panel B: LD Matrix =====
def create_panel_b():
    fig, ax = plt.subplots(figsize=(5, 5))

    n_variants = 10
    variant_labels = [f'SNP{i+1}' for i in range(n_variants)]
    variant_labels[4] = 'Causal'  # Mark causal variant

    # Create LD matrix with block structure
    np.random.seed(42)
    ld_matrix = np.eye(n_variants)

    # Strong LD in block (variants 2-6, indices 2-6)
    for i in range(2, 7):
        for j in range(2, 7):
            if i != j:
                ld_matrix[i, j] = 0.85 + np.random.uniform(-0.1, 0.1)

    # Moderate LD at edges
    for i in range(n_variants):
        for j in range(n_variants):
            if ld_matrix[i, j] == 0:
                distance = abs(i - j)
                ld_matrix[i, j] = max(0, 0.8 - distance * 0.15 + np.random.uniform(-0.1, 0.1))

    # Make symmetric
    ld_matrix = (ld_matrix + ld_matrix.T) / 2
    np.fill_diagonal(ld_matrix, 1)
    ld_matrix = np.clip(ld_matrix, 0, 1)

    # Plot heatmap
    im = ax.imshow(ld_matrix, cmap='Blues', vmin=0, vmax=1)

    # Add text annotations
    for i in range(n_variants):
        for j in range(n_variants):
            color = 'white' if ld_matrix[i, j] > 0.6 else 'black'
            ax.text(j, i, f'{ld_matrix[i, j]:.2f}', ha='center', va='center',
                    fontsize=7, color=color)

    # Highlight causal variant row/column
    ax.axhline(y=4.5, color=COLORS['causal'], linewidth=2)
    ax.axhline(y=3.5, color=COLORS['causal'], linewidth=2)
    ax.axvline(x=4.5, color=COLORS['causal'], linewidth=2)
    ax.axvline(x=3.5, color=COLORS['causal'], linewidth=2)

    ax.set_xticks(range(n_variants))
    ax.set_yticks(range(n_variants))
    ax.set_xticklabels(variant_labels, rotation=45, ha='right')
    ax.set_yticklabels(variant_labels)

    # Colorbar
    cbar = plt.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label('r² (LD)', fontweight='bold')

    ax.set_title('B. LD Matrix (Pairwise r²)', fontweight='bold', loc='left')

    plt.tight_layout()
    output_path = OUTPUT_DIR / '03-B-fig-ld-tag-causal.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

# ===== Panel C: Population-Specific LD =====
def create_panel_c():
    fig, axes = plt.subplots(1, 2, figsize=(8, 4))

    # Two populations with different LD patterns
    populations = ['European', 'African']
    n_variants = 8

    for ax_idx, (ax, pop) in enumerate(zip(axes, populations)):
        np.random.seed(42 + ax_idx)

        # Create different LD patterns
        ld_matrix = np.eye(n_variants)

        if pop == 'European':
            # Larger LD blocks
            for i in range(n_variants):
                for j in range(n_variants):
                    if i != j:
                        distance = abs(i - j)
                        ld_matrix[i, j] = max(0, 0.9 - distance * 0.12 + np.random.uniform(-0.05, 0.05))
        else:
            # Smaller LD blocks (faster decay)
            for i in range(n_variants):
                for j in range(n_variants):
                    if i != j:
                        distance = abs(i - j)
                        ld_matrix[i, j] = max(0, 0.9 - distance * 0.25 + np.random.uniform(-0.05, 0.05))

        # Make symmetric
        ld_matrix = (ld_matrix + ld_matrix.T) / 2
        np.fill_diagonal(ld_matrix, 1)
        ld_matrix = np.clip(ld_matrix, 0, 1)

        # Plot
        im = ax.imshow(ld_matrix, cmap='Blues', vmin=0, vmax=1)

        # Mark causal variant
        causal_idx = 3
        ax.axhline(y=causal_idx + 0.5, color=COLORS['causal'], linewidth=2, linestyle='--')
        ax.axhline(y=causal_idx - 0.5, color=COLORS['causal'], linewidth=2, linestyle='--')
        ax.axvline(x=causal_idx + 0.5, color=COLORS['causal'], linewidth=2, linestyle='--')
        ax.axvline(x=causal_idx - 0.5, color=COLORS['causal'], linewidth=2, linestyle='--')

        labels = [f'V{i+1}' for i in range(n_variants)]
        labels[causal_idx] = 'Causal'
        ax.set_xticks(range(n_variants))
        ax.set_yticks(range(n_variants))
        ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=8)
        ax.set_yticklabels(labels, fontsize=8)

        ax.set_title(f'{pop}\n({"extended" if pop == "European" else "shorter"} LD blocks)',
                     fontweight='bold', fontsize=10)

        # Count high-LD variants
        n_high_ld = np.sum(ld_matrix[causal_idx, :] > 0.5) - 1
        ax.text(0.5, -0.2, f'{n_high_ld} variants in high LD with causal',
                ha='center', transform=ax.transAxes, fontsize=9)

    # Shared colorbar
    fig.subplots_adjust(right=0.85)
    cbar_ax = fig.add_axes([0.88, 0.15, 0.03, 0.7])
    cbar = fig.colorbar(im, cax=cbar_ax)
    cbar.set_label('r²', fontweight='bold')

    fig.suptitle('C. Population-Specific LD Patterns', fontweight='bold', fontsize=12, y=1.02)

    plt.tight_layout()
    output_path = OUTPUT_DIR / '03-C-fig-ld-tag-causal.svg'
    plt.savefig(output_path, format='svg')
    print(f"Saved: {output_path}")
    plt.close()

# Generate all panels
if __name__ == '__main__':
    create_panel_a()
    create_panel_b()
    create_panel_c()
    print("All LD panels generated.")
