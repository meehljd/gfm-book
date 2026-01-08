#!/usr/bin/env python3
"""
Chapter 16: Regulatory Sequence Models Figures
Generates all figures for this chapter.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import graphviz

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_3" / "ch16"
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

# Fig 01 A-B: Long-Range Regulation
def create_fig_01():
    # Panel A: Enhancer-promoter distances
    fig, ax = plt.subplots(figsize=(8, 4))

    # Draw genomic region
    ax.axhline(y=1, color='#555555', linewidth=3, alpha=0.5)

    # Promoter
    ax.add_patch(mpatches.Rectangle((1, 0.8), 0.3, 0.4, facecolor='#1f77b4', edgecolor='white'))
    ax.text(1.15, 0.5, 'Promoter', ha='center', fontsize=9)

    # Enhancers at various distances
    enhancer_positions = [3, 5, 7]
    for pos in enhancer_positions:
        ax.add_patch(mpatches.Rectangle((pos, 0.8), 0.2, 0.4, facecolor='#2ca02c', edgecolor='white'))

    ax.text(5, 0.4, 'Enhancers (10-100+ kb away)', ha='center', fontsize=9)

    # Arrows showing interaction
    for pos in enhancer_positions:
        ax.annotate('', xy=(1.15, 1.3), xytext=(pos + 0.1, 1.2),
                    arrowprops=dict(arrowstyle='->', color='#d62728', lw=1.5,
                                    connectionstyle='arc3,rad=0.3'))

    ax.set_xlim(0, 9)
    ax.set_ylim(0, 2)
    ax.axis('off')
    ax.set_title('A. Long-Range Regulatory Interactions', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-A-fig-long-range-regulation.svg', format='svg')
    plt.close()
    print("Saved: 01-A-fig-long-range-regulation.svg")

    # Panel B: Context requirements
    fig, ax = plt.subplots(figsize=(6, 4))

    features = ['Motifs', 'Splice\nSites', 'Proximal\nRegulation', 'Enhancer-\nPromoter', 'TAD\nStructure']
    context_needed = [0.1, 1, 10, 100, 1000]  # in kb
    colors = ['#2ca02c', '#2ca02c', '#ff7f0e', '#d62728', '#d62728']

    bars = ax.bar(features, context_needed, color=colors, edgecolor='white')
    ax.set_ylabel('Context Required (kb)', fontweight='bold')
    ax.set_title('B. Context Requirements by Feature', fontweight='bold', loc='left')
    ax.set_yscale('log')
    ax.set_ylim(0.05, 3000)

    # Model context lines
    ax.axhline(y=6, color='#1f77b4', linestyle='--', linewidth=2, label='Nucleotide Transformer')
    ax.axhline(y=200, color='#ff7f0e', linestyle='--', linewidth=2, label='Enformer')
    ax.legend(fontsize=8)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-B-fig-long-range-regulation.svg', format='svg')
    plt.close()
    print("Saved: 01-B-fig-long-range-regulation.svg")

# Fig 02: Enformer Architecture
def create_fig_02():
    dot = graphviz.Digraph('enformer', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='10,8!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('input', '196,608 bp\nSequence', fillcolor='#aec7e8', shape='box')
    dot.node('conv', 'Convolutional\nStem', fillcolor='#98df8a', shape='box')
    dot.node('tf1', 'Transformer\nBlock 1', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('tf2', 'Transformer\nBlock 2', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('tf11', 'Transformer\nBlock 11', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('head', 'Prediction\nHeads', fillcolor='#ff7f0e', shape='box')

    dot.node('tracks', '5,313 Tracks\n(896 bins)', fillcolor='#d62728', fontcolor='white', shape='box')

    dot.edge('input', 'conv', label='One-hot')
    dot.edge('conv', 'tf1', label='128 bp resolution')
    dot.edge('tf1', 'tf2')
    dot.edge('tf2', 'tf11', style='dashed', label='...')
    dot.edge('tf11', 'head')
    dot.edge('head', 'tracks')

    # Side notes
    dot.node('note1', 'CAGE (RNA)\nATAC (chromatin)\nDNase\nHistone marks\nChIP-seq', fillcolor='#fff8dc', shape='note', fontsize='8')
    dot.edge('tracks', 'note1', style='dashed')

    dot.render(OUTPUT_DIR / '02-fig-enformer-architecture', cleanup=True)
    print("Saved: 02-fig-enformer-architecture.svg")

# Fig 03: Regulatory Assays
def create_fig_03():
    fig, ax = plt.subplots(figsize=(10, 5))

    assays = [
        ('ChIP-seq', 'TF Binding', '#1f77b4'),
        ('ATAC-seq', 'Accessibility', '#2ca02c'),
        ('DNase-seq', 'Open Chromatin', '#ff7f0e'),
        ('CAGE', 'Transcription Start', '#d62728'),
        ('Hi-C', '3D Contacts', '#9467bd'),
        ('CUT&RUN', 'Histone Marks', '#8c564b'),
    ]

    for i, (name, function, color) in enumerate(assays):
        ax.add_patch(mpatches.FancyBboxPatch((i * 1.6 + 0.1, 0.5), 1.4, 1.5,
                                              boxstyle='round,pad=0.02',
                                              facecolor=color, alpha=0.7,
                                              edgecolor='white', linewidth=2))
        ax.text(i * 1.6 + 0.8, 1.5, name, ha='center', va='center', fontsize=10,
                fontweight='bold', color='white')
        ax.text(i * 1.6 + 0.8, 0.9, function, ha='center', va='center', fontsize=9,
                color='white', style='italic')

    ax.set_xlim(-0.2, 10)
    ax.set_ylim(0, 2.5)
    ax.axis('off')
    ax.set_title('Regulatory Assays Predicted by Sequence-to-Function Models', fontweight='bold')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '03-fig-regulatory-assays.svg', format='svg')
    plt.close()
    print("Saved: 03-fig-regulatory-assays.svg")

# Fig 04: Regulatory VEP Workflow
def create_fig_04():
    dot = graphviz.Digraph('reg_vep', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='12,4!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('var', 'Variant +\nContext', fillcolor='#aec7e8', shape='box')
    dot.node('ref', 'Reference\nSequence', fillcolor='#98df8a', shape='box')
    dot.node('alt', 'Alternate\nSequence', fillcolor='#ffbb78', shape='box')

    dot.node('model', 'Enformer /\nBorzoi', fillcolor='#9467bd', fontcolor='white', shape='box')

    dot.node('pred_ref', 'Reference\nPredictions', fillcolor='#c5b0d5', shape='box')
    dot.node('pred_alt', 'Alternate\nPredictions', fillcolor='#c5b0d5', shape='box')

    dot.node('diff', 'Δ Prediction\n(per track)', fillcolor='#d62728', fontcolor='white', shape='box')
    dot.node('score', 'Variant\nEffect Score', fillcolor='#2ca02c', fontcolor='white', shape='box')

    dot.edge('var', 'ref')
    dot.edge('var', 'alt')
    dot.edge('ref', 'model')
    dot.edge('alt', 'model')
    dot.edge('model', 'pred_ref')
    dot.edge('model', 'pred_alt')
    dot.edge('pred_ref', 'diff')
    dot.edge('pred_alt', 'diff')
    dot.edge('diff', 'score', label='Aggregate')

    dot.render(OUTPUT_DIR / '04-fig-regulatory-vep-workflow', cleanup=True)
    print("Saved: 04-fig-regulatory-vep-workflow.svg")

# Fig 05 A-B: Borzoi RNA-seq
def create_fig_05():
    np.random.seed(42)

    # Panel A: Multi-tissue expression prediction
    fig, ax = plt.subplots(figsize=(6, 4))

    tissues = ['Brain', 'Heart', 'Liver', 'Muscle', 'Kidney']
    correlation = [0.82, 0.78, 0.85, 0.76, 0.80]
    colors = ['#1f77b4', '#d62728', '#2ca02c', '#ff7f0e', '#9467bd']

    bars = ax.bar(tissues, correlation, color=colors, edgecolor='white')
    ax.axhline(y=0.5, color='#555555', linestyle='--', alpha=0.5)

    ax.set_ylabel('Pearson Correlation', fontweight='bold')
    ax.set_title('A. RNA-seq Prediction by Tissue', fontweight='bold', loc='left')
    ax.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '05-A-fig-borzoi-rnaseq.svg', format='svg')
    plt.close()
    print("Saved: 05-A-fig-borzoi-rnaseq.svg")

    # Panel B: Enformer vs Borzoi
    fig, ax = plt.subplots(figsize=(6, 4))

    models = ['Basenji2', 'Enformer', 'Borzoi']
    metrics = ['RNA-seq\nPrediction', 'eQTL\nDetection', 'Splice\nVariants']

    performance = np.array([
        [0.65, 0.72, 0.85],
        [0.55, 0.68, 0.78],
        [0.60, 0.75, 0.82],
    ])

    x = np.arange(len(metrics))
    width = 0.25
    colors = ['#aec7e8', '#1f77b4', '#2ca02c']

    for i, (model, color) in enumerate(zip(models, colors)):
        ax.bar(x + i * width, performance[:, i], width, label=model, color=color, edgecolor='white')

    ax.set_ylabel('Performance', fontweight='bold')
    ax.set_title('B. Model Comparison', fontweight='bold', loc='left')
    ax.set_xticks(x + width)
    ax.set_xticklabels(metrics)
    ax.legend(fontsize=9)
    ax.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '05-B-fig-borzoi-rnaseq.svg', format='svg')
    plt.close()
    print("Saved: 05-B-fig-borzoi-rnaseq.svg")

# Fig 06: Sei Vocabulary
def create_fig_06():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Sei sequence classes
    classes = [
        ('CTCF', 'Insulator', '#1f77b4'),
        ('Enhancer\n(Strong)', 'Active Enhancer', '#2ca02c'),
        ('Enhancer\n(Weak)', 'Poised', '#98df8a'),
        ('Promoter', 'TSS-proximal', '#ff7f0e'),
        ('Transcribed', 'Gene body', '#9467bd'),
        ('Polycomb', 'Repressed', '#d62728'),
        ('Quiescent', 'Low signal', '#7f7f7f'),
    ]

    for i, (name, desc, color) in enumerate(classes):
        ax.add_patch(mpatches.FancyBboxPatch((i * 1.4 + 0.1, 0.3), 1.2, 1.8,
                                              boxstyle='round,pad=0.02',
                                              facecolor=color, alpha=0.7,
                                              edgecolor='white', linewidth=2))
        ax.text(i * 1.4 + 0.7, 1.5, name, ha='center', va='center', fontsize=9,
                fontweight='bold', color='white')
        ax.text(i * 1.4 + 0.7, 0.7, desc, ha='center', va='center', fontsize=8,
                color='white', style='italic')

    ax.set_xlim(-0.2, 10)
    ax.set_ylim(-0.1, 2.5)
    ax.axis('off')
    ax.set_title('Sei Regulatory Vocabulary: Sequence Classes', fontweight='bold')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '06-fig-sei-vocabulary.svg', format='svg')
    plt.close()
    print("Saved: 06-fig-sei-vocabulary.svg")

# Fig 07 A-B: Regulatory Limitations
def create_fig_07():
    # Panel A: Cell-type specificity challenge
    fig, ax = plt.subplots(figsize=(6, 4))
    np.random.seed(42)

    cell_types = ['K562\n(trained)', 'HepG2\n(trained)', 'iPSC\n(novel)', 'Neuron\n(novel)']
    performance = [0.88, 0.85, 0.62, 0.55]
    colors = ['#2ca02c', '#2ca02c', '#d62728', '#d62728']

    bars = ax.bar(cell_types, performance, color=colors, edgecolor='white')
    ax.axhline(y=0.7, color='#555555', linestyle='--', alpha=0.5)
    ax.text(3.3, 0.72, 'Useful threshold', fontsize=8, alpha=0.7)

    ax.set_ylabel('Prediction Quality', fontweight='bold')
    ax.set_title('A. Cell-Type Generalization Gap', fontweight='bold', loc='left')
    ax.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '07-A-fig-regulatory-limitations.svg', format='svg')
    plt.close()
    print("Saved: 07-A-fig-regulatory-limitations.svg")

    # Panel B: Missing modalities
    fig, ax = plt.subplots(figsize=(6, 4))

    modalities = ['Sequence', 'Chromatin', 'Methylation', '3D Structure', 'TF Levels']
    availability = [1, 0.5, 0.3, 0.2, 0.1]
    colors = ['#2ca02c', '#ff7f0e', '#d62728', '#d62728', '#d62728']

    bars = ax.barh(modalities, availability, color=colors, edgecolor='white')

    ax.set_xlabel('Information Available to Model', fontweight='bold')
    ax.set_title('B. Missing Regulatory Context', fontweight='bold', loc='left')
    ax.set_xlim(0, 1.1)

    # Labels
    for bar, avail in zip(bars, availability):
        ax.text(bar.get_width() + 0.02, bar.get_y() + bar.get_height()/2,
                f'{avail:.0%}', va='center', fontsize=9)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '07-B-fig-regulatory-limitations.svg', format='svg')
    plt.close()
    print("Saved: 07-B-fig-regulatory-limitations.svg")

if __name__ == '__main__':
    create_fig_01()
    create_fig_02()
    create_fig_03()
    create_fig_04()
    create_fig_05()
    create_fig_06()
    create_fig_07()
    print("All Chapter 16 figures generated.")
