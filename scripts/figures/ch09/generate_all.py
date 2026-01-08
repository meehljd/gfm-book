#!/usr/bin/env python3
"""
Chapter 9: Transfer Learning Figures
Generates all 7 figures for this chapter.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import graphviz

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_2" / "ch09"
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

# Fig 01: Domain Alignment
def create_fig_01():
    fig, ax = plt.subplots(figsize=(8, 4))

    np.random.seed(42)

    # Source domain
    source_x = np.random.normal(-1.5, 0.5, 50)
    source_y = np.random.normal(0, 0.5, 50)

    # Target domain (shifted)
    target_x = np.random.normal(1.5, 0.5, 50)
    target_y = np.random.normal(0.5, 0.5, 50)

    ax.scatter(source_x, source_y, c='#1f77b4', s=40, alpha=0.6, label='Source (pretraining)', edgecolors='white')
    ax.scatter(target_x, target_y, c='#d62728', s=40, alpha=0.6, label='Target (downstream)', edgecolors='white')

    # Arrow showing shift
    ax.annotate('', xy=(0.8, 0.3), xytext=(-0.8, 0),
                arrowprops=dict(arrowstyle='->', color='#555555', lw=2))
    ax.text(0, 0.5, 'Domain\nShift', ha='center', fontsize=10)

    ax.set_xlabel('Feature Dimension 1', fontweight='bold')
    ax.set_ylabel('Feature Dimension 2', fontweight='bold')
    ax.legend(loc='upper right', fontsize=9)
    ax.set_title('Domain Shift in Genomic Transfer Learning', fontweight='bold')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-fig-domain-alignment.svg', format='svg')
    plt.close()
    print("Saved: 01-fig-domain-alignment.svg")

# Fig 02 A-D: Four Factors
def create_fig_02():
    panels = [
        ('A', 'Task Relatedness', 'High relatedness\n→ More transferable'),
        ('B', 'Data Quantity', 'Less data\n→ More reliance on pretrained'),
        ('C', 'Model Expressiveness', 'High capacity\n→ Higher overfitting risk'),
        ('D', 'Distribution Overlap', 'More overlap\n→ Better transfer'),
    ]

    for panel_id, title, note in panels:
        fig, ax = plt.subplots(figsize=(5, 4))
        np.random.seed(42)

        x = np.linspace(0, 1, 100)
        y = 1 - 0.5 * x + np.random.randn(100) * 0.1 if 'B' in panel_id else 0.3 + 0.5 * x + np.random.randn(100) * 0.1

        ax.plot(x, y, 'o-', color='#1f77b4', markersize=3, alpha=0.5)
        ax.fill_between(x, y - 0.15, y + 0.15, alpha=0.2, color='#1f77b4')

        ax.text(0.5, 0.1, note, ha='center', transform=ax.transAxes, fontsize=9, style='italic',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#cccccc'))

        ax.set_xlabel(title, fontweight='bold')
        ax.set_ylabel('Transfer Performance', fontweight='bold')
        ax.set_title(f'{panel_id}. {title}', fontweight='bold', loc='left')

        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / f'02-{panel_id}-fig-four-factors.svg', format='svg')
        plt.close()
        print(f"Saved: 02-{panel_id}-fig-four-factors.svg")

# Fig 03: Conservative Escalation
def create_fig_03():
    dot = graphviz.Digraph('escalation', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='6,8!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='10', style='filled,rounded', penwidth='1.5')

    dot.node('start', 'Start with\nFrozen Encoder', fillcolor='#aec7e8', shape='box')
    dot.node('probe', 'Linear Probe\nTest', fillcolor='#98df8a', shape='box')
    dot.node('check1', 'Performance\nSufficient?', fillcolor='#fff8dc', shape='diamond')
    dot.node('partial', 'Unfreeze\nTop Layers', fillcolor='#ffbb78', shape='box')
    dot.node('check2', 'Improved?', fillcolor='#fff8dc', shape='diamond')
    dot.node('full', 'Full\nFine-tuning', fillcolor='#d62728', fontcolor='white', shape='box')
    dot.node('done', 'Done', fillcolor='#2ca02c', fontcolor='white', shape='box')

    dot.edge('start', 'probe')
    dot.edge('probe', 'check1')
    dot.edge('check1', 'done', label='Yes')
    dot.edge('check1', 'partial', label='No')
    dot.edge('partial', 'check2')
    dot.edge('check2', 'done', label='Yes')
    dot.edge('check2', 'full', label='No')
    dot.edge('full', 'done')

    dot.render(OUTPUT_DIR / '03-fig-conservative-escalation', cleanup=True)
    print("Saved: 03-fig-conservative-escalation.svg")

# Fig 04: Linear Probing Workflow
def create_fig_04():
    dot = graphviz.Digraph('probing', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='10,4!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='10', style='filled,rounded', penwidth='1.5')

    dot.node('input', 'Downstream\nData', fillcolor='#aec7e8', shape='box')
    dot.node('encoder', 'Frozen\nEncoder', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('embed', 'Fixed\nEmbeddings', fillcolor='#c5b0d5', shape='box')
    dot.node('probe', 'Trainable\nLinear Layer', fillcolor='#ff7f0e', shape='box')
    dot.node('output', 'Predictions', fillcolor='#2ca02c', fontcolor='white', shape='box')

    dot.edge('input', 'encoder')
    dot.edge('encoder', 'embed', label='Forward pass\n(no gradients)')
    dot.edge('embed', 'probe')
    dot.edge('probe', 'output', label='Trained\n(gradients)')

    dot.render(OUTPUT_DIR / '04-fig-linear-probing-workflow', cleanup=True)
    print("Saved: 04-fig-linear-probing-workflow.svg")

if __name__ == '__main__':
    create_fig_01()
    create_fig_02()
    create_fig_03()
    create_fig_04()
    print("All Chapter 9 figures generated.")
