#!/usr/bin/env python3
"""
Chapter 13: Foundation Model Paradigm Figures
Generates all figures for this chapter.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import graphviz

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_3" / "ch13"
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

# Fig 01 A-B: Paradigm Shift
def create_fig_01():
    # Panel A: Task-specific paradigm
    dot = graphviz.Digraph('taskspecific', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='6,6!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('data1', 'ChIP-seq\nData', fillcolor='#aec7e8', shape='box')
    dot.node('data2', 'RNA-seq\nData', fillcolor='#aec7e8', shape='box')
    dot.node('data3', 'Splice\nData', fillcolor='#aec7e8', shape='box')

    dot.node('model1', 'TF Binding\nModel', fillcolor='#d62728', fontcolor='white', shape='box')
    dot.node('model2', 'Expression\nModel', fillcolor='#d62728', fontcolor='white', shape='box')
    dot.node('model3', 'Splice\nModel', fillcolor='#d62728', fontcolor='white', shape='box')

    dot.node('task1', 'TF Binding\nPrediction', fillcolor='#98df8a', shape='box')
    dot.node('task2', 'Expression\nPrediction', fillcolor='#98df8a', shape='box')
    dot.node('task3', 'Splice\nPrediction', fillcolor='#98df8a', shape='box')

    dot.edge('data1', 'model1')
    dot.edge('data2', 'model2')
    dot.edge('data3', 'model3')
    dot.edge('model1', 'task1')
    dot.edge('model2', 'task2')
    dot.edge('model3', 'task3')

    dot.render(OUTPUT_DIR / '01-A-fig-paradigm-shift', cleanup=True)
    print("Saved: 01-A-fig-paradigm-shift.svg")

    # Panel B: Foundation model paradigm
    dot = graphviz.Digraph('foundation', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='6,6!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('genome', 'Unlabeled\nGenomes', fillcolor='#aec7e8', shape='box')
    dot.node('pretrain', 'Foundation\nModel\n(Pretrained)', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('embed', 'General\nEmbeddings', fillcolor='#c5b0d5', shape='box')

    dot.node('adapt1', 'Adapter 1', fillcolor='#ff7f0e', shape='box')
    dot.node('adapt2', 'Adapter 2', fillcolor='#ff7f0e', shape='box')
    dot.node('adapt3', 'Adapter 3', fillcolor='#ff7f0e', shape='box')

    dot.node('task1', 'TF Binding', fillcolor='#98df8a', shape='box')
    dot.node('task2', 'Expression', fillcolor='#98df8a', shape='box')
    dot.node('task3', 'Splicing', fillcolor='#98df8a', shape='box')

    dot.edge('genome', 'pretrain', label='Self-supervised')
    dot.edge('pretrain', 'embed')
    dot.edge('embed', 'adapt1')
    dot.edge('embed', 'adapt2')
    dot.edge('embed', 'adapt3')
    dot.edge('adapt1', 'task1')
    dot.edge('adapt2', 'task2')
    dot.edge('adapt3', 'task3')

    dot.render(OUTPUT_DIR / '01-B-fig-paradigm-shift', cleanup=True)
    print("Saved: 01-B-fig-paradigm-shift.svg")

# Fig 02 A-C: Scaling Laws
def create_fig_02():
    np.random.seed(42)

    # Panel A: Loss vs model size
    fig, ax = plt.subplots(figsize=(5, 4))
    params = np.logspace(6, 10, 20)
    loss = 3.5 * (params / 1e6) ** (-0.3) + 1.5 + np.random.randn(20) * 0.05
    ax.loglog(params, loss, 'o-', color='#1f77b4', linewidth=2, markersize=6)
    ax.set_xlabel('Parameters', fontweight='bold')
    ax.set_ylabel('Pretraining Loss', fontweight='bold')
    ax.set_title('A. Loss vs. Model Size', fontweight='bold', loc='left')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '02-A-fig-scaling-laws.svg', format='svg')
    plt.close()
    print("Saved: 02-A-fig-scaling-laws.svg")

    # Panel B: Downstream performance
    fig, ax = plt.subplots(figsize=(5, 4))
    params = np.logspace(6, 10, 20)
    perf = 0.5 + 0.4 * (1 - np.exp(-params / 1e8)) + np.random.randn(20) * 0.02
    ax.semilogx(params, perf, 'o-', color='#2ca02c', linewidth=2, markersize=6)
    ax.set_xlabel('Parameters', fontweight='bold')
    ax.set_ylabel('Downstream Performance', fontweight='bold')
    ax.set_title('B. Transfer Performance vs. Scale', fontweight='bold', loc='left')
    ax.set_ylim(0.4, 1.0)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '02-B-fig-scaling-laws.svg', format='svg')
    plt.close()
    print("Saved: 02-B-fig-scaling-laws.svg")

    # Panel C: Compute-optimal allocation
    fig, ax = plt.subplots(figsize=(5, 4))
    compute = np.logspace(18, 22, 20)
    params_opt = (compute / 120) ** 0.5
    data_opt = 20 * params_opt
    ax.loglog(compute, params_opt / 1e9, 'o-', color='#1f77b4', linewidth=2, markersize=6, label='Params (B)')
    ax.loglog(compute, data_opt / 1e9, 's-', color='#d62728', linewidth=2, markersize=6, label='Tokens (B)')
    ax.set_xlabel('Compute (FLOPs)', fontweight='bold')
    ax.set_ylabel('Optimal Allocation (Billions)', fontweight='bold')
    ax.set_title('C. Compute-Optimal Scaling', fontweight='bold', loc='left')
    ax.legend(fontsize=8)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '02-C-fig-scaling-laws.svg', format='svg')
    plt.close()
    print("Saved: 02-C-fig-scaling-laws.svg")

# Fig 03: Model Taxonomy
def create_fig_03():
    dot = graphviz.Digraph('taxonomy', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='10,8!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    # Root
    dot.node('root', 'Genomic\nFoundation\nModels', fillcolor='#fff8dc', shape='box')

    # Four families
    dot.node('dna', 'DNA Language\nModels', fillcolor='#1f77b4', fontcolor='white', shape='box')
    dot.node('protein', 'Protein Language\nModels', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.node('s2f', 'Sequence-to-\nFunction Models', fillcolor='#ff7f0e', fontcolor='white', shape='box')
    dot.node('multi', 'Multi-Modal\nModels', fillcolor='#9467bd', fontcolor='white', shape='box')

    # Examples for each
    dot.node('dnabert', 'DNABERT', fillcolor='#aec7e8', shape='box')
    dot.node('nt', 'Nucleotide\nTransformer', fillcolor='#aec7e8', shape='box')
    dot.node('hyena', 'HyenaDNA', fillcolor='#aec7e8', shape='box')

    dot.node('esm', 'ESM-2', fillcolor='#98df8a', shape='box')
    dot.node('prot', 'ProtTrans', fillcolor='#98df8a', shape='box')

    dot.node('enformer', 'Enformer', fillcolor='#ffbb78', shape='box')
    dot.node('sei', 'Sei', fillcolor='#ffbb78', shape='box')

    dot.node('af', 'AlphaFold2', fillcolor='#c5b0d5', shape='box')
    dot.node('omni', 'Omni-DNA', fillcolor='#c5b0d5', shape='box')

    # Edges
    dot.edge('root', 'dna')
    dot.edge('root', 'protein')
    dot.edge('root', 's2f')
    dot.edge('root', 'multi')

    dot.edge('dna', 'dnabert')
    dot.edge('dna', 'nt')
    dot.edge('dna', 'hyena')
    dot.edge('protein', 'esm')
    dot.edge('protein', 'prot')
    dot.edge('s2f', 'enformer')
    dot.edge('s2f', 'sei')
    dot.edge('multi', 'af')
    dot.edge('multi', 'omni')

    dot.render(OUTPUT_DIR / '03-fig-model-taxonomy', cleanup=True)
    print("Saved: 03-fig-model-taxonomy.svg")

# Fig 04: Design Dimensions (Radar chart)
def create_fig_04():
    fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(projection='polar'))

    categories = ['Context\nLength', 'Parameters', 'Training\nCompute', 'Generation\nCapability', 'Transfer\nBreadth', 'Single-nt\nResolution']
    n_cats = len(categories)
    angles = np.linspace(0, 2 * np.pi, n_cats, endpoint=False).tolist()
    angles += angles[:1]

    models = {
        'ESM-2': [0.2, 0.9, 0.8, 0.3, 0.8, 0.9],
        'Enformer': [0.6, 0.6, 0.7, 0.2, 0.5, 0.8],
        'HyenaDNA': [1.0, 0.2, 0.4, 0.4, 0.6, 1.0],
        'Evo 2': [1.0, 1.0, 1.0, 0.9, 0.9, 1.0],
    }
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#9467bd']

    for (name, values), color in zip(models.items(), colors):
        values = values + values[:1]
        ax.plot(angles, values, 'o-', linewidth=2, label=name, color=color)
        ax.fill(angles, values, alpha=0.1, color=color)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=9)
    ax.set_ylim(0, 1)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1), fontsize=9)
    ax.set_title('Design Dimensions for Genomic Foundation Models', fontweight='bold', pad=20)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-fig-design-dimensions.svg', format='svg')
    plt.close()
    print("Saved: 04-fig-design-dimensions.svg")

# Fig 05: Build vs Use Decision
def create_fig_05():
    dot = graphviz.Digraph('buildvsuse', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='8,10!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('start', 'New Task', fillcolor='#fff8dc', shape='box')
    dot.node('q1', 'Novel domain?', fillcolor='#fff8dc', shape='diamond')
    dot.node('q2', 'Labeled data\navailable?', fillcolor='#fff8dc', shape='diamond')
    dot.node('q3', 'Compute\nbudget?', fillcolor='#fff8dc', shape='diamond')

    dot.node('build', 'Train from\nScratch', fillcolor='#d62728', fontcolor='white', shape='box')
    dot.node('finetune', 'Fine-tune\nExisting', fillcolor='#ff7f0e', shape='box')
    dot.node('adapt', 'LoRA/\nAdapters', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.node('use', 'Use Frozen\nEmbeddings', fillcolor='#1f77b4', fontcolor='white', shape='box')

    dot.edge('start', 'q1')
    dot.edge('q1', 'build', label='Yes')
    dot.edge('q1', 'q2', label='No')
    dot.edge('q2', 'q3', label='Yes')
    dot.edge('q2', 'use', label='No')
    dot.edge('q3', 'finetune', label='High')
    dot.edge('q3', 'adapt', label='Medium')

    dot.render(OUTPUT_DIR / '05-fig-build-vs-use', cleanup=True)
    print("Saved: 05-fig-build-vs-use.svg")

if __name__ == '__main__':
    create_fig_01()
    create_fig_02()
    create_fig_03()
    create_fig_04()
    create_fig_05()
    print("All Chapter 13 figures generated.")
