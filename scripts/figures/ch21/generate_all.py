#!/usr/bin/env python3
"""
Chapter 21: Network Models Figures
Generates all figures for this chapter.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import graphviz

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_4" / "ch21"
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

# Fig 01 A-B: Biological Networks
def create_fig_01():
    # Panel A: Network types
    fig, ax = plt.subplots(figsize=(8, 5))

    networks = [
        ('PPI', 'Protein-Protein\nInteraction', '#1f77b4'),
        ('GRN', 'Gene Regulatory\nNetwork', '#2ca02c'),
        ('Metabolic', 'Metabolic\nNetwork', '#ff7f0e'),
        ('Signaling', 'Signaling\nPathway', '#9467bd'),
        ('KG', 'Knowledge\nGraph', '#d62728'),
    ]

    for i, (name, desc, color) in enumerate(networks):
        ax.add_patch(mpatches.FancyBboxPatch((i * 1.5 + 0.1, 0.3), 1.3, 1.8,
                                              boxstyle='round,pad=0.02',
                                              facecolor=color, alpha=0.7,
                                              edgecolor='white', linewidth=2))
        ax.text(i * 1.5 + 0.75, 1.5, name, ha='center', va='center', fontsize=11,
                fontweight='bold', color='white')
        ax.text(i * 1.5 + 0.75, 0.8, desc, ha='center', va='center', fontsize=8,
                color='white')

    ax.set_xlim(-0.2, 7.8)
    ax.set_ylim(-0.1, 2.5)
    ax.axis('off')
    ax.set_title('A. Types of Biological Networks', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-A-fig-biological-networks.svg', format='svg')
    plt.close()
    print("Saved: 01-A-fig-biological-networks.svg")

    # Panel B: Network statistics
    fig, ax = plt.subplots(figsize=(6, 4))

    networks = ['STRING', 'BioGRID', 'KEGG', 'Reactome']
    nodes = [19000, 16000, 8000, 11000]
    edges = [11700000, 1900000, 30000, 85000]

    x = np.arange(len(networks))
    width = 0.35

    ax.bar(x - width/2, np.array(nodes)/1000, width, label='Nodes (k)', color='#1f77b4', edgecolor='white')
    ax.bar(x + width/2, np.array(edges)/100000, width, label='Edges (100k)', color='#2ca02c', edgecolor='white')

    ax.set_ylabel('Count', fontweight='bold')
    ax.set_title('B. Network Statistics', fontweight='bold', loc='left')
    ax.set_xticks(x)
    ax.set_xticklabels(networks)
    ax.legend(fontsize=9)
    ax.set_yscale('log')
    ax.set_ylim(0.1, 200)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-B-fig-biological-networks.svg', format='svg')
    plt.close()
    print("Saved: 01-B-fig-biological-networks.svg")

# Fig 02 A-B: Message Passing
def create_fig_02():
    # Panel A: GNN message passing
    dot = graphviz.Digraph('message_passing', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='10,4!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    # Central node
    dot.node('v', 'Node v\n(update)', fillcolor='#d62728', fontcolor='white', shape='circle')

    # Neighbors
    dot.node('n1', 'Neighbor 1', fillcolor='#1f77b4', fontcolor='white', shape='circle')
    dot.node('n2', 'Neighbor 2', fillcolor='#1f77b4', fontcolor='white', shape='circle')
    dot.node('n3', 'Neighbor 3', fillcolor='#1f77b4', fontcolor='white', shape='circle')

    dot.edge('n1', 'v', label='Message')
    dot.edge('n2', 'v', label='Message')
    dot.edge('n3', 'v', label='Message')

    dot.node('agg', 'Aggregate\n& Update', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.edge('v', 'agg')

    dot.render(OUTPUT_DIR / '02-A-fig-message-passing', cleanup=True)
    print("Saved: 02-A-fig-message-passing.svg")

    # Panel B: Layer depth
    fig, ax = plt.subplots(figsize=(6, 4))
    np.random.seed(42)

    layers = np.arange(1, 11)
    performance = 0.6 + 0.3 * (1 - np.exp(-layers / 3)) - 0.1 * (layers > 5) * (layers - 5) / 5
    performance += np.random.randn(10) * 0.02

    ax.plot(layers, performance, 'o-', color='#1f77b4', linewidth=2, markersize=8)
    ax.axvline(x=3, color='#2ca02c', linestyle='--', alpha=0.7)
    ax.text(3.2, 0.65, 'Optimal\ndepth', fontsize=9, color='#2ca02c')

    ax.fill_between(layers[layers > 5], performance[layers > 5], 0.95, alpha=0.2, color='#d62728')
    ax.text(7, 0.95, 'Over-\nsmoothing', fontsize=9, color='#d62728')

    ax.set_xlabel('GNN Layers', fontweight='bold')
    ax.set_ylabel('Performance', fontweight='bold')
    ax.set_title('B. Layer Depth and Over-smoothing', fontweight='bold', loc='left')
    ax.set_ylim(0.5, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '02-B-fig-message-passing.svg', format='svg')
    plt.close()
    print("Saved: 02-B-fig-message-passing.svg")

# Fig 03 A-B: GNN Integration
def create_fig_03():
    # Panel A: Multi-modal integration
    dot = graphviz.Digraph('integration', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='8,6!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('seq', 'Sequence\nEmbeddings', fillcolor='#1f77b4', fontcolor='white', shape='box')
    dot.node('struct', 'Structure\nFeatures', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.node('network', 'Network\nTopology', fillcolor='#ff7f0e', shape='box')

    dot.node('gnn', 'Graph Neural\nNetwork', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('output', 'Integrated\nPrediction', fillcolor='#98df8a', shape='box')

    dot.edge('seq', 'gnn', label='Node features')
    dot.edge('struct', 'gnn', label='Edge features')
    dot.edge('network', 'gnn', label='Graph structure')
    dot.edge('gnn', 'output')

    dot.render(OUTPUT_DIR / '03-A-fig-gnn-integration', cleanup=True)
    print("Saved: 03-A-fig-gnn-integration.svg")

    # Panel B: Feature fusion
    fig, ax = plt.subplots(figsize=(6, 4))

    features = ['Sequence\nOnly', 'Network\nOnly', 'Early\nFusion', 'Late\nFusion', 'GNN\nIntegration']
    performance = [0.75, 0.70, 0.82, 0.80, 0.88]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#2ca02c', '#9467bd']

    bars = ax.bar(features, performance, color=colors, edgecolor='white')
    ax.axhline(y=0.5, color='#555555', linestyle='--', alpha=0.5)

    ax.set_ylabel('auROC', fontweight='bold')
    ax.set_title('B. Feature Fusion Strategies', fontweight='bold', loc='left')
    ax.set_ylim(0.5, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '03-B-fig-gnn-integration.svg', format='svg')
    plt.close()
    print("Saved: 03-B-fig-gnn-integration.svg")

# Fig 04 A-B: Disease Gene Prioritization
def create_fig_04():
    # Panel A: Network propagation
    dot = graphviz.Digraph('propagation', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='10,4!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('seed', 'Seed Genes\n(known disease)', fillcolor='#d62728', fontcolor='white', shape='box')
    dot.node('network', 'PPI\nNetwork', fillcolor='#aec7e8', shape='box')
    dot.node('propagate', 'Random Walk\nPropagation', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('rank', 'Ranked\nCandidates', fillcolor='#98df8a', shape='box')

    dot.edge('seed', 'network')
    dot.edge('network', 'propagate')
    dot.edge('propagate', 'rank')

    dot.render(OUTPUT_DIR / '04-A-fig-disease-gene-prioritization', cleanup=True)
    print("Saved: 04-A-fig-disease-gene-prioritization.svg")

    # Panel B: Prioritization performance
    fig, ax = plt.subplots(figsize=(6, 4))
    np.random.seed(42)

    methods = ['Random', 'PageRank', 'PRINCE', 'GNN']
    top_100 = [5, 15, 22, 35]
    colors = ['#aec7e8', '#ff7f0e', '#2ca02c', '#9467bd']

    bars = ax.bar(methods, top_100, color=colors, edgecolor='white')
    ax.axhline(y=5, color='#555555', linestyle='--', alpha=0.5)
    ax.text(3.5, 7, 'Random expectation', fontsize=8, alpha=0.7)

    ax.set_ylabel('True Positives in Top 100', fontweight='bold')
    ax.set_title('B. Gene Prioritization Performance', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-B-fig-disease-gene-prioritization.svg', format='svg')
    plt.close()
    print("Saved: 04-B-fig-disease-gene-prioritization.svg")

# Fig 05 A-B: Knowledge Graph Drug Repurposing
def create_fig_05():
    # Panel A: KG structure
    dot = graphviz.Digraph('kg', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='10,4!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('drug', 'Drug', fillcolor='#1f77b4', fontcolor='white', shape='box')
    dot.node('target', 'Target\nProtein', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.node('pathway', 'Pathway', fillcolor='#ff7f0e', shape='box')
    dot.node('disease', 'Disease', fillcolor='#d62728', fontcolor='white', shape='box')
    dot.node('gene', 'Gene', fillcolor='#9467bd', fontcolor='white', shape='box')

    dot.edge('drug', 'target', label='binds')
    dot.edge('target', 'pathway', label='participates')
    dot.edge('pathway', 'disease', label='associated')
    dot.edge('gene', 'disease', label='causes')
    dot.edge('gene', 'target', label='encodes')

    dot.render(OUTPUT_DIR / '05-A-fig-kg-drug-repurposing', cleanup=True)
    print("Saved: 05-A-fig-kg-drug-repurposing.svg")

    # Panel B: Link prediction
    fig, ax = plt.subplots(figsize=(6, 4))

    methods = ['TransE', 'DistMult', 'ComplEx', 'RotatE', 'GNN-KG']
    hits_10 = [0.45, 0.50, 0.55, 0.60, 0.68]
    colors = ['#aec7e8', '#aec7e8', '#ffbb78', '#ffbb78', '#2ca02c']

    bars = ax.bar(methods, hits_10, color=colors, edgecolor='white')
    ax.axhline(y=0.1, color='#555555', linestyle='--', alpha=0.5)

    ax.set_ylabel('Hits@10', fontweight='bold')
    ax.set_title('B. Drug-Disease Link Prediction', fontweight='bold', loc='left')
    ax.set_ylim(0, 0.8)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '05-B-fig-kg-drug-repurposing.svg', format='svg')
    plt.close()
    print("Saved: 05-B-fig-kg-drug-repurposing.svg")

# Fig 06: Network Bias
def create_fig_06():
    fig, ax = plt.subplots(figsize=(8, 5))

    biases = [
        ('Study Bias', 'Well-studied genes\nover-represented', '#d62728'),
        ('Degree Bias', 'Hub genes dominate\npredictions', '#ff7f0e'),
        ('Annotation Bias', 'Annotated functions\nover-predicted', '#ffbb78'),
        ('Disease Bias', 'Common diseases\nbetter covered', '#2ca02c'),
    ]

    for i, (name, desc, color) in enumerate(biases):
        ax.add_patch(mpatches.FancyBboxPatch((i * 2 + 0.1, 0.3), 1.8, 1.8,
                                              boxstyle='round,pad=0.02',
                                              facecolor=color, alpha=0.7,
                                              edgecolor='white', linewidth=2))
        ax.text(i * 2 + 1, 1.5, name, ha='center', va='center', fontsize=10,
                fontweight='bold', color='white')
        ax.text(i * 2 + 1, 0.8, desc, ha='center', va='center', fontsize=8,
                color='white')

    ax.set_xlim(-0.2, 8.2)
    ax.set_ylim(-0.1, 2.5)
    ax.axis('off')
    ax.set_title('Sources of Bias in Biological Networks', fontweight='bold')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '06-fig-network-bias.svg', format='svg')
    plt.close()
    print("Saved: 06-fig-network-bias.svg")

if __name__ == '__main__':
    create_fig_01()
    create_fig_02()
    create_fig_03()
    create_fig_04()
    create_fig_05()
    create_fig_06()
    print("All Chapter 21 figures generated.")
