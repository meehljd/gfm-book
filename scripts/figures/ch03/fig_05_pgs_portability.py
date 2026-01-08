#!/usr/bin/env python3
"""
Figure 3.5: Polygenic Score Portability Across Ancestries
Bar chart showing relative performance when applying European-derived PGS to other populations.
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
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'figure.dpi': 150,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# Data based on published literature (Martin et al. 2019, Duncan et al. 2019)
populations = ['European\n(reference)', 'East Asian', 'Hispanic/\nLatino', 'South Asian', 'African']
relative_accuracy = [100, 70, 60, 50, 35]  # Approximate percentages
colors = ['#1f77b4', '#ff7f0e', '#9467bd', '#d62728', '#2ca02c']

# Create figure
fig, ax = plt.subplots(figsize=(8, 5))

bars = ax.bar(populations, relative_accuracy, color=colors, edgecolor='white', linewidth=1.5)

# Add value labels on bars
for bar, val in zip(bars, relative_accuracy):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 2,
            f'{val}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Reference line at 100%
ax.axhline(y=100, color='#1f77b4', linestyle='--', linewidth=1, alpha=0.5)

# Labels
ax.set_ylabel('Relative Prediction Accuracy (%)', fontweight='bold')
ax.set_xlabel('Population', fontweight='bold')
ax.set_ylim(0, 115)

# Title
ax.set_title('Portability of European-Derived Polygenic Scores', fontweight='bold', pad=15)

# Annotation
ax.annotate('40-75% reduction\nin accuracy for\nAfrican ancestry',
            xy=(4, 35), xytext=(3.2, 60),
            fontsize=9, ha='center',
            arrowprops=dict(arrowstyle='->', color='#333333', lw=1),
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#fff8dc', edgecolor='#cccccc'))

# Add explanation text at bottom
explanation = (
    "Factors contributing to portability gap:\n"
    "• Different LD patterns across populations\n"
    "• Allele frequency differences\n"
    "• Training data bias (78% European)"
)
ax.text(0.02, 0.02, explanation, transform=ax.transAxes, fontsize=8,
        va='bottom', ha='left', bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor='#cccccc'))

plt.tight_layout()

# Save
output_path = OUTPUT_DIR / '05-fig-pgs-portability.svg'
plt.savefig(output_path, format='svg')
print(f"Saved: {output_path}")
plt.close()
