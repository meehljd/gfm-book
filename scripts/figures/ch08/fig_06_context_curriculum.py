#!/usr/bin/env python3
"""
Figure 8.6: Context Length Curriculum
Shows how context length is gradually increased during pretraining.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_2" / "ch08"
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

# Panel 1: Context length schedule
ax = axes[0]

training_steps = np.array([0, 50000, 100000, 150000, 200000, 250000])
context_lengths = np.array([1024, 2048, 4096, 8192, 16384, 32768])

ax.step(training_steps / 1000, context_lengths / 1000, where='post', color='#1f77b4', linewidth=2.5)

# Annotations
stages = [
    (25, 1, 'Stage 1:\n1k tokens'),
    (75, 2, 'Stage 2:\n2k tokens'),
    (125, 4, 'Stage 3:\n4k tokens'),
    (175, 8, 'Stage 4:\n8k tokens'),
]

for step, ctx, label in stages:
    ax.annotate(label, xy=(step, ctx), xytext=(step + 15, ctx + 3),
                fontsize=8, arrowprops=dict(arrowstyle='->', color='#555555', lw=0.8))

ax.set_xlabel('Training Steps (thousands)', fontweight='bold')
ax.set_ylabel('Context Length (thousands of tokens)', fontweight='bold')
ax.set_title('Context Length Curriculum', fontweight='bold')

# Panel 2: Training loss
ax = axes[1]

np.random.seed(42)
steps = np.linspace(0, 250, 500)
loss = 3.5 * np.exp(-steps / 100) + 0.8 + np.random.randn(500) * 0.05

# Add bumps at context increases
increase_points = [50, 100, 150, 200]
for ip in increase_points:
    mask = (steps > ip) & (steps < ip + 10)
    loss[mask] += 0.15 * np.exp(-(steps[mask] - ip) / 5)

ax.plot(steps, loss, color='#d62728', linewidth=1.5, alpha=0.8)

# Mark context increases
for ip in increase_points:
    ax.axvline(x=ip, color='#2ca02c', linestyle='--', linewidth=1, alpha=0.7)

ax.text(75, 2.5, 'Small bumps at\ncontext increases', fontsize=9, color='#2ca02c')

ax.set_xlabel('Training Steps (thousands)', fontweight='bold')
ax.set_ylabel('Training Loss', fontweight='bold')
ax.set_title('Loss During Curriculum Training', fontweight='bold')

plt.tight_layout()
output_path = OUTPUT_DIR / '06-fig-context-curriculum.svg'
plt.savefig(output_path, format='svg')
print(f"Saved: {output_path}")
plt.close()
