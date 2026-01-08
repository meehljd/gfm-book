#!/usr/bin/env python3
"""
Figure 3.1: Anatomy of a Manhattan Plot
Simulated GWAS results showing genome-wide association pattern.
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
    'axes.titlesize': 12,
    'axes.titleweight': 'bold',
    'axes.labelsize': 10,
    'xtick.labelsize': 8,
    'ytick.labelsize': 9,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
})

np.random.seed(42)

# Create figure with gridspec for main plot + inset Q-Q plot
fig = plt.figure(figsize=(12, 6))
gs = fig.add_gridspec(1, 2, width_ratios=[4, 1], wspace=0.15)
ax_main = fig.add_subplot(gs[0])
ax_qq = fig.add_subplot(gs[1])

# Simulate GWAS data
n_variants = 100000
n_chromosomes = 22

# Generate positions per chromosome
chrom_lengths = np.array([250, 243, 198, 191, 181, 171, 159, 146, 141, 136,
                          135, 133, 115, 107, 102, 90, 81, 78, 59, 63, 47, 51])  # Mb approx
chrom_lengths = chrom_lengths / chrom_lengths.sum() * n_variants

chromosomes = []
positions = []
current_pos = 0
chrom_starts = [0]

for chrom in range(1, n_chromosomes + 1):
    n_snps = int(chrom_lengths[chrom-1])
    chromosomes.extend([chrom] * n_snps)
    chrom_positions = np.sort(np.random.uniform(0, chrom_lengths[chrom-1] * 1e6, n_snps))
    positions.extend(current_pos + chrom_positions)
    current_pos += chrom_lengths[chrom-1] * 1e6 + 10e6  # 10Mb gap between chromosomes
    chrom_starts.append(current_pos)

chromosomes = np.array(chromosomes)
positions = np.array(positions)
n_actual = len(chromosomes)  # Actual number of variants generated

# Generate p-values (mostly null, some signals)
pvals = np.random.uniform(0, 1, n_actual)

# Add some real signals (peaks)
signal_chroms = [2, 6, 9, 11, 15, 19]
signal_positions_relative = [0.4, 0.3, 0.6, 0.5, 0.7, 0.4]

for sig_chr, sig_rel in zip(signal_chroms, signal_positions_relative):
    # Find variants near this position
    chr_mask = chromosomes == sig_chr
    chr_positions = positions[chr_mask]
    target_pos = chrom_starts[sig_chr-1] + sig_rel * (chrom_starts[sig_chr] - chrom_starts[sig_chr-1])

    # Add signal to nearby variants
    distances = np.abs(positions - target_pos)
    nearby_mask = distances < 5e6  # 5Mb window
    n_nearby = np.sum(nearby_mask)

    # Strong signal at center, decaying with distance
    signal_strength = np.exp(-distances[nearby_mask] / 1e6) * (10 + np.random.exponential(5, n_nearby))
    pvals[nearby_mask] = 10 ** (-signal_strength)

# Compute -log10(p)
neglog10p = -np.log10(pvals)

# Colors alternating by chromosome
colors = []
for chrom in chromosomes:
    if chrom % 2 == 0:
        colors.append('#1f77b4')
    else:
        colors.append('#aec7e8')
colors = np.array(colors)

# Main Manhattan plot
ax_main.scatter(positions, neglog10p, c=colors, s=3, alpha=0.7, rasterized=True)

# Significance threshold
sig_threshold = -np.log10(5e-8)
ax_main.axhline(y=sig_threshold, color='#d62728', linestyle='--', linewidth=1.5, label='P = 5×10⁻⁸')

# Suggestive threshold
sug_threshold = -np.log10(1e-5)
ax_main.axhline(y=sug_threshold, color='#ff7f0e', linestyle=':', linewidth=1, alpha=0.7, label='P = 10⁻⁵')

# Chromosome labels
chrom_centers = []
for i in range(n_chromosomes):
    center = (chrom_starts[i] + chrom_starts[i+1]) / 2
    chrom_centers.append(center)

ax_main.set_xticks(chrom_centers)
ax_main.set_xticklabels([str(i) for i in range(1, 23)], fontsize=7)
ax_main.set_xlabel('Chromosome', fontweight='bold')
ax_main.set_ylabel('-log₁₀(P-value)', fontweight='bold')
ax_main.set_ylim(0, max(neglog10p) * 1.1)
ax_main.set_xlim(0, max(positions) * 1.02)

# Annotate a peak
peak_idx = np.argmax(neglog10p)
peak_chr = chromosomes[peak_idx]
ax_main.annotate(
    f'Lead SNP\nChr {peak_chr}',
    xy=(positions[peak_idx], neglog10p[peak_idx]),
    xytext=(positions[peak_idx] + max(positions)*0.05, neglog10p[peak_idx] - 2),
    fontsize=8,
    arrowprops=dict(arrowstyle='->', color='#333333', lw=1),
    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#cccccc')
)

# Add annotation about LD block
ax_main.annotate(
    'LD block with\nmultiple correlated\nvariants',
    xy=(positions[peak_idx] - 2e6, neglog10p[peak_idx] - 3),
    xytext=(positions[peak_idx] - max(positions)*0.1, neglog10p[peak_idx] - 6),
    fontsize=8, ha='center',
    arrowprops=dict(arrowstyle='->', color='#555555', lw=0.8),
    bbox=dict(boxstyle='round,pad=0.3', facecolor='#fff8dc', edgecolor='#cccccc')
)

ax_main.legend(loc='upper right', fontsize=8)
ax_main.set_title('Manhattan Plot: Genome-Wide Association Study', fontweight='bold', loc='left')

# Q-Q Plot inset
observed = np.sort(neglog10p)
expected = -np.log10(np.linspace(1/n_actual, 1, n_actual))

ax_qq.scatter(expected, observed, s=2, alpha=0.5, c='#1f77b4', rasterized=True)
ax_qq.plot([0, max(expected)], [0, max(expected)], 'r--', linewidth=1, label='Expected')
ax_qq.set_xlabel('Expected -log₁₀(P)', fontsize=9)
ax_qq.set_ylabel('Observed -log₁₀(P)', fontsize=9)
ax_qq.set_title('Q-Q Plot', fontweight='bold', fontsize=10)

# Add lambda annotation
# Calculate genomic inflation factor
median_chi2 = np.median(-2 * np.log(pvals))
lambda_gc = median_chi2 / 0.455  # chi2 with 1 df
ax_qq.text(0.05, 0.95, f'λ = {lambda_gc:.2f}', transform=ax_qq.transAxes,
           fontsize=9, va='top', ha='left',
           bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#cccccc'))

ax_qq.set_xlim(0, 5)
ax_qq.set_ylim(0, max(observed) * 1.05)

plt.tight_layout()

# Save
output_path = OUTPUT_DIR / '01-fig-manhattan-anatomy.svg'
plt.savefig(output_path, format='svg')
print(f"Saved: {output_path}")
plt.close()
