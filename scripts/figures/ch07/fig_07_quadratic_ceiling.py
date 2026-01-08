#!/usr/bin/env python3
"""
Figure 7.7: Quadratic Complexity Ceiling
Shows how O(n²) attention limits context length.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_2" / "ch07"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans'],
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.titleweight': 'bold',
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
})

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Panel 1: Memory scaling
ax = axes[0]

context_lengths = np.array([512, 1024, 2048, 4096, 8192, 16384, 32768])
memory_gb = (context_lengths ** 2 * 4) / (1024 ** 3)  # 4 bytes per float

ax.plot(context_lengths / 1000, memory_gb, 'o-', color='#d62728', linewidth=2, markersize=8)

# GPU memory lines
ax.axhline(y=16, color='#2ca02c', linestyle='--', linewidth=1, alpha=0.7)
ax.text(35, 17, 'V100 (16GB)', fontsize=8, color='#2ca02c')

ax.axhline(y=40, color='#1f77b4', linestyle='--', linewidth=1, alpha=0.7)
ax.text(35, 42, 'A100 (40GB)', fontsize=8, color='#1f77b4')

ax.axhline(y=80, color='#9467bd', linestyle='--', linewidth=1, alpha=0.7)
ax.text(35, 85, 'A100 (80GB)', fontsize=8, color='#9467bd')

ax.set_xlabel('Context Length (thousands of tokens)', fontweight='bold')
ax.set_ylabel('Attention Memory (GB)', fontweight='bold')
ax.set_yscale('log')
ax.set_ylim(0.001, 500)

ax.set_title('Attention Memory: O(n²) Growth', fontweight='bold')

# Panel 2: Compute scaling
ax = axes[1]

compute_flops = (context_lengths ** 2 * 768 * 2) / 1e12  # Approximate FLOPs for attention

ax.plot(context_lengths / 1000, compute_flops, 's-', color='#1f77b4', linewidth=2, markersize=8)

# Practical context lengths
practical_contexts = {
    'BERT (512)': 0.512,
    'DNABERT-2 (10k)': 10,
    'Evo (131k)': 131,
}

for label, ctx in practical_contexts.items():
    if ctx <= 33:
        flops = (ctx * 1000) ** 2 * 768 * 2 / 1e12
        ax.plot(ctx, flops, 'o', markersize=12, color='#ff7f0e',
                markeredgecolor='white', markeredgewidth=1.5)
        ax.annotate(label, xy=(ctx, flops), xytext=(ctx + 2, flops * 1.5),
                    fontsize=8, arrowprops=dict(arrowstyle='->', color='#555555', lw=0.8))

ax.set_xlabel('Context Length (thousands of tokens)', fontweight='bold')
ax.set_ylabel('Compute (TFLOPs)', fontweight='bold')
ax.set_yscale('log')

ax.set_title('Compute Scaling with Context Length', fontweight='bold')

plt.tight_layout()
output_path = OUTPUT_DIR / '07-fig-quadratic-ceiling.svg'
plt.savefig(output_path, format='svg')
print(f"Saved: {output_path}")
plt.close()
