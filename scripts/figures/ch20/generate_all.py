#!/usr/bin/env python3
"""
Chapter 20: 3D Genome Models Figures
Generates all figures for this chapter.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import graphviz

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_4" / "ch20"
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

# Fig 01 A-B: TAD Disruption
def create_fig_01():
    np.random.seed(42)

    # Panel A: Normal TAD structure
    fig, ax = plt.subplots(figsize=(6, 5))

    # Create contact map
    n = 50
    contact = np.zeros((n, n))
    # TAD 1
    for i in range(20):
        for j in range(20):
            contact[i, j] = np.exp(-abs(i-j) / 5)
    # TAD 2
    for i in range(20, 50):
        for j in range(20, 50):
            contact[i, j] = np.exp(-abs(i-j) / 5)

    im = ax.imshow(contact, cmap='Reds', aspect='equal')
    ax.axvline(x=20, color='#1f77b4', linestyle='--', linewidth=2)
    ax.axhline(y=20, color='#1f77b4', linestyle='--', linewidth=2)
    ax.text(10, -3, 'TAD 1', ha='center', fontsize=10, fontweight='bold')
    ax.text(35, -3, 'TAD 2', ha='center', fontsize=10, fontweight='bold')

    ax.set_xlabel('Genomic Position', fontweight='bold')
    ax.set_ylabel('Genomic Position', fontweight='bold')
    ax.set_title('A. Normal TAD Structure', fontweight='bold', loc='left')
    plt.colorbar(im, ax=ax, label='Contact Frequency')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-A-fig-tad-disruption.svg', format='svg')
    plt.close()
    print("Saved: 01-A-fig-tad-disruption.svg")

    # Panel B: Disrupted TAD
    fig, ax = plt.subplots(figsize=(6, 5))

    # Disrupted contact map (boundary deleted)
    contact_disrupted = np.zeros((n, n))
    for i in range(50):
        for j in range(50):
            contact_disrupted[i, j] = np.exp(-abs(i-j) / 8)

    im = ax.imshow(contact_disrupted, cmap='Reds', aspect='equal')
    ax.scatter([20], [20], s=200, c='yellow', marker='*', zorder=5, edgecolors='black')
    ax.text(25, 15, 'Boundary\ndeletion', fontsize=9, color='#d62728', fontweight='bold')

    ax.set_xlabel('Genomic Position', fontweight='bold')
    ax.set_ylabel('Genomic Position', fontweight='bold')
    ax.set_title('B. Disrupted TAD (Boundary Deletion)', fontweight='bold', loc='left')
    plt.colorbar(im, ax=ax, label='Contact Frequency')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-B-fig-tad-disruption.svg', format='svg')
    plt.close()
    print("Saved: 01-B-fig-tad-disruption.svg")

# Fig 02 A-B: Chromatin Hierarchy
def create_fig_02():
    # Panel A: Hierarchical organization
    dot = graphviz.Digraph('hierarchy', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='8,8!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('chromosome', 'Chromosome\n(~100 Mb)', fillcolor='#d62728', fontcolor='white', shape='box')
    dot.node('compartment', 'A/B Compartments\n(~10 Mb)', fillcolor='#ff7f0e', shape='box')
    dot.node('tad', 'TADs\n(~1 Mb)', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.node('loop', 'Loops\n(~100 kb)', fillcolor='#1f77b4', fontcolor='white', shape='box')
    dot.node('nucleosome', 'Nucleosomes\n(~200 bp)', fillcolor='#9467bd', fontcolor='white', shape='box')

    dot.edge('chromosome', 'compartment')
    dot.edge('compartment', 'tad')
    dot.edge('tad', 'loop')
    dot.edge('loop', 'nucleosome')

    dot.render(OUTPUT_DIR / '02-A-fig-chromatin-hierarchy', cleanup=True)
    print("Saved: 02-A-fig-chromatin-hierarchy.svg")

    # Panel B: Scale comparison
    fig, ax = plt.subplots(figsize=(6, 4))

    levels = ['Nucleosomes', 'Loops', 'TADs', 'Compartments', 'Chromosomes']
    sizes = [0.2, 100, 1000, 10000, 100000]  # in kb
    colors = ['#9467bd', '#1f77b4', '#2ca02c', '#ff7f0e', '#d62728']

    ax.barh(levels, sizes, color=colors, edgecolor='white')
    ax.set_xlabel('Scale (kb)', fontweight='bold')
    ax.set_title('B. Chromatin Organization Scales', fontweight='bold', loc='left')
    ax.set_xscale('log')
    ax.set_xlim(0.1, 200000)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '02-B-fig-chromatin-hierarchy.svg', format='svg')
    plt.close()
    print("Saved: 02-B-fig-chromatin-hierarchy.svg")

# Fig 03 A-B: Loop Extrusion
def create_fig_03():
    # Panel A: Loop extrusion mechanism
    fig, ax = plt.subplots(figsize=(8, 5))

    # DNA strand
    ax.plot([1, 9], [2, 2], color='#555555', linewidth=4, zorder=1)

    # CTCF sites
    ax.scatter([2], [2], s=200, c='#d62728', marker='>', zorder=5, label='CTCF')
    ax.scatter([8], [2], s=200, c='#d62728', marker='<', zorder=5)

    # Cohesin ring
    theta = np.linspace(0, 2*np.pi, 100)
    r = 0.8
    ax.plot(5 + r*np.cos(theta), 3 + r*np.sin(theta), color='#2ca02c', linewidth=3)
    ax.text(5, 3, 'Cohesin', ha='center', va='center', fontsize=9, fontweight='bold')

    # Loop visualization
    loop_x = np.linspace(2, 8, 100)
    loop_y = 2 + 1.5 * np.sin((loop_x - 2) * np.pi / 6)
    ax.plot(loop_x, loop_y, color='#1f77b4', linewidth=2, linestyle='--', alpha=0.7)

    ax.text(2, 1.3, 'CTCF', ha='center', fontsize=9, color='#d62728')
    ax.text(8, 1.3, 'CTCF', ha='center', fontsize=9, color='#d62728')

    ax.set_xlim(0, 10)
    ax.set_ylim(0.5, 4.5)
    ax.axis('off')
    ax.set_title('A. Loop Extrusion Mechanism', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '03-A-fig-loop-extrusion.svg', format='svg')
    plt.close()
    print("Saved: 03-A-fig-loop-extrusion.svg")

    # Panel B: CTCF motif orientation
    fig, ax = plt.subplots(figsize=(6, 4))

    orientations = ['Convergent\n(►◄)', 'Tandem\n(►►)', 'Divergent\n(◄►)']
    loop_strength = [1.0, 0.3, 0.1]
    colors = ['#2ca02c', '#ff7f0e', '#d62728']

    bars = ax.bar(orientations, loop_strength, color=colors, edgecolor='white')
    ax.set_ylabel('Loop Strength', fontweight='bold')
    ax.set_title('B. CTCF Orientation and Loop Formation', fontweight='bold', loc='left')
    ax.set_ylim(0, 1.2)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '03-B-fig-loop-extrusion.svg', format='svg')
    plt.close()
    print("Saved: 03-B-fig-loop-extrusion.svg")

# Fig 04 A-B: 3D Genome Models
def create_fig_04():
    # Panel A: Model types
    fig, ax = plt.subplots(figsize=(8, 5))

    models = [
        ('Hi-C\nPrediction', 'Akita, Orca', '#1f77b4'),
        ('Contact\nReconstruction', 'DeepC', '#2ca02c'),
        ('Loop\nCalling', 'Peakachu', '#ff7f0e'),
        ('TAD\nBoundary', 'TADbreak', '#9467bd'),
        ('3D Structure', 'PHi-C2', '#d62728'),
    ]

    for i, (task, model, color) in enumerate(models):
        ax.add_patch(mpatches.FancyBboxPatch((i * 1.5 + 0.1, 0.3), 1.3, 1.8,
                                              boxstyle='round,pad=0.02',
                                              facecolor=color, alpha=0.7,
                                              edgecolor='white', linewidth=2))
        ax.text(i * 1.5 + 0.75, 1.5, task, ha='center', va='center', fontsize=9,
                fontweight='bold', color='white')
        ax.text(i * 1.5 + 0.75, 0.8, model, ha='center', va='center', fontsize=8,
                color='white')

    ax.set_xlim(-0.2, 7.8)
    ax.set_ylim(-0.1, 2.5)
    ax.axis('off')
    ax.set_title('A. 3D Genome Model Types', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-A-fig-3d-models.svg', format='svg')
    plt.close()
    print("Saved: 04-A-fig-3d-models.svg")

    # Panel B: Sequence-to-structure
    dot = graphviz.Digraph('seq2struct', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='10,3!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('seq', 'DNA\nSequence', fillcolor='#aec7e8', shape='box')
    dot.node('model', 'Akita /\nOrca', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('contact', 'Predicted\nHi-C Map', fillcolor='#ffbb78', shape='box')
    dot.node('variant', 'Variant\nEffect', fillcolor='#98df8a', shape='box')

    dot.edge('seq', 'model')
    dot.edge('model', 'contact')
    dot.edge('contact', 'variant', label='In silico\nmutagenesis')

    dot.render(OUTPUT_DIR / '04-B-fig-3d-models', cleanup=True)
    print("Saved: 04-B-fig-3d-models.svg")

# Fig 05 A-B: Spatial Transcriptomics
def create_fig_05():
    np.random.seed(42)

    # Panel A: Spatial gene expression
    fig, ax = plt.subplots(figsize=(6, 5))

    n_spots = 100
    x = np.random.rand(n_spots) * 10
    y = np.random.rand(n_spots) * 10
    expression = np.exp(-((x - 5)**2 + (y - 5)**2) / 10)

    scatter = ax.scatter(x, y, c=expression, cmap='viridis', s=60, edgecolors='white')
    plt.colorbar(scatter, ax=ax, label='Gene Expression')

    ax.set_xlabel('X Position', fontweight='bold')
    ax.set_ylabel('Y Position', fontweight='bold')
    ax.set_title('A. Spatial Gene Expression', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '05-A-fig-spatial-transcriptomics.svg', format='svg')
    plt.close()
    print("Saved: 05-A-fig-spatial-transcriptomics.svg")

    # Panel B: Integration workflow
    dot = graphviz.Digraph('spatial', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='10,3!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('spatial', 'Spatial\nTranscriptomics', fillcolor='#aec7e8', shape='box')
    dot.node('hic', 'Hi-C\nData', fillcolor='#98df8a', shape='box')
    dot.node('integrate', 'Multi-modal\nIntegration', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('insight', 'Structure-\nFunction Link', fillcolor='#ff7f0e', shape='box')

    dot.edge('spatial', 'integrate')
    dot.edge('hic', 'integrate')
    dot.edge('integrate', 'insight')

    dot.render(OUTPUT_DIR / '05-B-fig-spatial-transcriptomics', cleanup=True)
    print("Saved: 05-B-fig-spatial-transcriptomics.svg")

if __name__ == '__main__':
    create_fig_01()
    create_fig_02()
    create_fig_03()
    create_fig_04()
    create_fig_05()
    print("All Chapter 20 figures generated.")
