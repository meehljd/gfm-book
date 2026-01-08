#!/usr/bin/env python3
"""
Chapter 15: Protein Language Models Figures
Generates all figures for this chapter.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import graphviz

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_3" / "ch15"
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

# Fig 01 A-B: PLM Emergent Capabilities
def create_fig_01():
    np.random.seed(42)

    # Panel A: Emergent structure prediction
    fig, ax = plt.subplots(figsize=(6, 4))

    params = np.logspace(6, 10, 20)
    structure_capability = np.zeros(20)
    threshold = 1e9
    structure_capability[params > threshold] = 0.3 + 0.6 * (1 - np.exp(-(params[params > threshold] - threshold) / 1e10))
    structure_capability += np.random.randn(20) * 0.02

    ax.semilogx(params, structure_capability, 'o-', color='#2ca02c', linewidth=2, markersize=6)
    ax.axvline(x=threshold, color='#d62728', linestyle='--', linewidth=2, alpha=0.7)
    ax.text(threshold * 2, 0.1, 'Emergence\nthreshold', fontsize=9, color='#d62728')

    ax.set_xlabel('Model Parameters', fontweight='bold')
    ax.set_ylabel('Structure Prediction Quality', fontweight='bold')
    ax.set_title('A. Emergent Structure Understanding', fontweight='bold', loc='left')
    ax.set_ylim(-0.05, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-A-fig-plm-emergent.svg', format='svg')
    plt.close()
    print("Saved: 01-A-fig-plm-emergent.svg")

    # Panel B: Zero-shot capabilities
    fig, ax = plt.subplots(figsize=(6, 4))

    capabilities = ['Contact\nPrediction', 'Secondary\nStructure', 'Variant\nEffect', 'Function\nAnnotation']
    small_model = [0.2, 0.4, 0.3, 0.25]
    large_model = [0.85, 0.92, 0.78, 0.72]

    x = np.arange(len(capabilities))
    width = 0.35

    ax.bar(x - width/2, small_model, width, label='150M params', color='#aec7e8', edgecolor='white')
    ax.bar(x + width/2, large_model, width, label='15B params', color='#1f77b4', edgecolor='white')

    ax.set_ylabel('Zero-Shot Performance', fontweight='bold')
    ax.set_title('B. Scale Enables Zero-Shot Capabilities', fontweight='bold', loc='left')
    ax.set_xticks(x)
    ax.set_xticklabels(capabilities)
    ax.legend(fontsize=9)
    ax.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-B-fig-plm-emergent.svg', format='svg')
    plt.close()
    print("Saved: 01-B-fig-plm-emergent.svg")

# Fig 02 A-C: ESM-2 Scaling
def create_fig_02():
    np.random.seed(42)

    # Panel A: Scaling parameters
    fig, ax = plt.subplots(figsize=(5, 4))

    versions = ['ESM-1b\n650M', 'ESM-2\n650M', 'ESM-2\n3B', 'ESM-2\n15B']
    params = [650, 650, 3000, 15000]
    performance = [0.78, 0.82, 0.88, 0.93]

    ax.bar(versions, performance, color=['#ff7f0e', '#1f77b4', '#1f77b4', '#1f77b4'], edgecolor='white')
    ax.set_ylabel('Contact Prediction Accuracy', fontweight='bold')
    ax.set_title('A. ESM Family Scaling', fontweight='bold', loc='left')
    ax.set_ylim(0.5, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '02-A-fig-esm2-scaling.svg', format='svg')
    plt.close()
    print("Saved: 02-A-fig-esm2-scaling.svg")

    # Panel B: Training data
    fig, ax = plt.subplots(figsize=(5, 4))

    datasets = ['UniRef50', 'UniRef90', 'UniRef100', 'BFD']
    size = [50, 90, 220, 2500]  # millions of sequences
    colors = ['#aec7e8', '#1f77b4', '#1f77b4', '#2ca02c']

    ax.bar(datasets, size, color=colors, edgecolor='white')
    ax.set_ylabel('Sequences (millions)', fontweight='bold')
    ax.set_title('B. Training Data Scale', fontweight='bold', loc='left')
    ax.set_yscale('log')
    ax.set_ylim(10, 5000)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '02-B-fig-esm2-scaling.svg', format='svg')
    plt.close()
    print("Saved: 02-B-fig-esm2-scaling.svg")

    # Panel C: Layer-wise representations
    fig, ax = plt.subplots(figsize=(5, 4))

    layers = np.arange(1, 34)
    contact_info = 0.3 + 0.5 * np.sin((layers - 15) * np.pi / 33) + np.random.randn(33) * 0.03
    contact_info = np.clip(contact_info, 0, 1)

    ax.plot(layers, contact_info, 'o-', color='#9467bd', linewidth=2, markersize=4)
    best_layer = layers[np.argmax(contact_info)]
    ax.axvline(x=best_layer, color='#d62728', linestyle='--', alpha=0.7)
    ax.text(best_layer + 1, 0.9, f'Best: L{best_layer}', fontsize=9, color='#d62728')

    ax.set_xlabel('Layer Number', fontweight='bold')
    ax.set_ylabel('Contact Information', fontweight='bold')
    ax.set_title('C. Layer-wise Contact Encoding', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '02-C-fig-esm2-scaling.svg', format='svg')
    plt.close()
    print("Saved: 02-C-fig-esm2-scaling.svg")

# Fig 03 A-B: ESMFold
def create_fig_03():
    # Panel A: Architecture
    dot = graphviz.Digraph('esmfold', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='10,4!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('seq', 'Protein\nSequence', fillcolor='#aec7e8', shape='box')
    dot.node('esm', 'ESM-2\n(15B)', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('embed', 'Embeddings +\nAttention Maps', fillcolor='#c5b0d5', shape='box')
    dot.node('fold', 'Folding\nModule', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.node('struct', '3D Structure', fillcolor='#98df8a', shape='box')

    dot.edge('seq', 'esm')
    dot.edge('esm', 'embed')
    dot.edge('embed', 'fold')
    dot.edge('fold', 'struct')

    dot.render(OUTPUT_DIR / '03-A-fig-esmfold', cleanup=True)
    print("Saved: 03-A-fig-esmfold.svg")

    # Panel B: Speed vs accuracy
    fig, ax = plt.subplots(figsize=(6, 4))

    methods = ['MSA-based\nAlphaFold2', 'ESMFold', 'OmegaFold', 'RoseTTAFold']
    accuracy = [0.95, 0.88, 0.86, 0.85]
    speed = [60, 2, 5, 15]  # seconds per structure
    colors = ['#2ca02c', '#1f77b4', '#ff7f0e', '#9467bd']

    for method, acc, spd, color in zip(methods, accuracy, speed, colors):
        ax.scatter(spd, acc, s=200, c=color, label=method, edgecolors='white', linewidth=2)

    ax.set_xlabel('Time per Structure (seconds)', fontweight='bold')
    ax.set_ylabel('Structure Accuracy (GDT-TS)', fontweight='bold')
    ax.set_title('B. Speed vs. Accuracy Trade-off', fontweight='bold', loc='left')
    ax.legend(fontsize=8)
    ax.set_xscale('log')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '03-B-fig-esmfold.svg', format='svg')
    plt.close()
    print("Saved: 03-B-fig-esmfold.svg")

# Fig 04 A-B: PLM Variant Scoring
def create_fig_04():
    np.random.seed(42)

    # Panel A: Likelihood ratio scoring
    fig, ax = plt.subplots(figsize=(6, 5))

    # Create score distributions
    benign = np.random.normal(-0.5, 1, 500)
    pathogenic = np.random.normal(-3, 1.5, 500)

    ax.hist(benign, bins=30, alpha=0.7, color='#2ca02c', label='Benign', density=True)
    ax.hist(pathogenic, bins=30, alpha=0.7, color='#d62728', label='Pathogenic', density=True)

    ax.axvline(x=-1.5, color='#555555', linestyle='--', linewidth=2)
    ax.text(-1.4, 0.35, 'Threshold', fontsize=9, rotation=90, va='bottom')

    ax.set_xlabel('Log-Likelihood Ratio Score', fontweight='bold')
    ax.set_ylabel('Density', fontweight='bold')
    ax.set_title('A. Zero-Shot Variant Scoring', fontweight='bold', loc='left')
    ax.legend(fontsize=9)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-A-fig-plm-variant-scoring.svg', format='svg')
    plt.close()
    print("Saved: 04-A-fig-plm-variant-scoring.svg")

    # Panel B: Benchmark comparison
    fig, ax = plt.subplots(figsize=(6, 4))

    methods = ['SIFT', 'PolyPhen-2', 'CADD', 'ESM-1v', 'AlphaMissense']
    auroc = [0.75, 0.78, 0.82, 0.85, 0.90]
    colors = ['#aec7e8', '#aec7e8', '#ff7f0e', '#1f77b4', '#2ca02c']

    bars = ax.bar(methods, auroc, color=colors, edgecolor='white')
    ax.axhline(y=0.5, color='#555555', linestyle='--', alpha=0.5)

    ax.set_ylabel('auROC (ClinVar)', fontweight='bold')
    ax.set_title('B. Variant Effect Prediction Benchmark', fontweight='bold', loc='left')
    ax.set_ylim(0.5, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-B-fig-plm-variant-scoring.svg', format='svg')
    plt.close()
    print("Saved: 04-B-fig-plm-variant-scoring.svg")

# Fig 05: PLM Limitations
def create_fig_05():
    fig, ax = plt.subplots(figsize=(8, 5))

    limitations = [
        ('Single Sequence\nOnly', 'No MSA context'),
        ('No Ligand\nBinding', 'Ignores cofactors'),
        ('Static Structure', 'No dynamics'),
        ('Domain\nBoundaries', 'Struggles with\nmulti-domain'),
        ('Membrane\nProteins', 'Limited training\ndata'),
    ]

    colors = ['#d62728', '#ff7f0e', '#ff7f0e', '#ffbb78', '#ffbb78']

    for i, ((name, desc), color) in enumerate(zip(limitations, colors)):
        ax.add_patch(mpatches.FancyBboxPatch((i * 1.5 + 0.1, 0.5), 1.3, 1.2,
                                              boxstyle='round,pad=0.02',
                                              facecolor=color, alpha=0.7,
                                              edgecolor='white', linewidth=2))
        ax.text(i * 1.5 + 0.75, 1.3, name, ha='center', va='center', fontsize=9, fontweight='bold')
        ax.text(i * 1.5 + 0.75, 0.8, desc, ha='center', va='center', fontsize=8, style='italic')

    ax.set_xlim(-0.2, 7.7)
    ax.set_ylim(0, 2)
    ax.axis('off')
    ax.set_title('Current Limitations of Protein Language Models', fontweight='bold')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '05-fig-plm-limitations.svg', format='svg')
    plt.close()
    print("Saved: 05-fig-plm-limitations.svg")

if __name__ == '__main__':
    create_fig_01()
    create_fig_02()
    create_fig_03()
    create_fig_04()
    create_fig_05()
    print("All Chapter 15 figures generated.")
