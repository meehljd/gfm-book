#!/usr/bin/env python3
"""Chapter 29: Drug Discovery Figures"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import graphviz

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_6" / "ch29"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family': 'sans-serif', 'font.sans-serif': ['Arial', 'DejaVu Sans'], 'font.size': 10,
    'axes.titlesize': 11, 'axes.titleweight': 'bold', 'figure.dpi': 150, 'savefig.dpi': 300,
    'savefig.bbox': 'tight', 'axes.spines.top': False, 'axes.spines.right': False})

def create_fig_01():  # Target prioritization pipeline
    dot = graphviz.Digraph('target', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='14,4!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    steps = [
        ('gwas', 'GWAS\nSignals', '#aec7e8'),
        ('genes', 'Candidate\nGenes', '#98df8a'),
        ('fm', 'FM\nScoring', '#9467bd'),
        ('druggable', 'Druggability\nFilter', '#ffbb78'),
        ('target', 'Priority\nTargets', '#2ca02c'),
    ]
    for nid, label, color in steps:
        fc = 'white' if nid in ['fm', 'target'] else 'black'
        dot.node(nid, label, fillcolor=color, fontcolor=fc, shape='box')
    for i in range(len(steps) - 1):
        dot.edge(steps[i][0], steps[i + 1][0])
    dot.render(OUTPUT_DIR / '01-fig-target-prioritization', cleanup=True)
    print("Saved: 01-fig-target-prioritization.svg")

def create_fig_02():  # Network-based target discovery
    dot = graphviz.Digraph('network', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='10,8!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    # Disease genes cluster
    dot.node('disease', 'Disease\nGenes', fillcolor='#d62728', fontcolor='white', shape='box')
    # Network neighbors
    for i in range(4):
        dot.node(f'n{i}', f'Neighbor {i+1}', fillcolor='#ff7f0e', shape='box')
        dot.edge('disease', f'n{i}')
    # Target candidates
    dot.node('candidate', 'Target\nCandidate', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.edge('n0', 'candidate')
    dot.edge('n1', 'candidate')
    # Add PPI annotation
    dot.node('ppi', 'PPI\nNetwork', fillcolor='#aec7e8', shape='box')
    dot.edge('ppi', 'disease', style='dashed')
    dot.render(OUTPUT_DIR / '02-fig-network-target-discovery', cleanup=True)
    print("Saved: 02-fig-network-target-discovery.svg")

def create_fig_03():  # Drug-target prediction with FMs
    dot = graphviz.Digraph('dti', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='10,8!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    # Drug input
    dot.node('drug', 'Drug\nMolecule', fillcolor='#1f77b4', fontcolor='white', shape='box')
    dot.node('drug_enc', 'Chemical\nEncoder', fillcolor='#aec7e8', shape='box')
    # Target input
    dot.node('target', 'Target\nProtein', fillcolor='#ff7f0e', shape='box')
    dot.node('target_enc', 'Protein FM\nEncoder', fillcolor='#ffbb78', shape='box')
    # Interaction prediction
    dot.node('interact', 'Interaction\nPredictor', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('score', 'Binding\nScore', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.edge('drug', 'drug_enc')
    dot.edge('target', 'target_enc')
    dot.edge('drug_enc', 'interact')
    dot.edge('target_enc', 'interact')
    dot.edge('interact', 'score')
    dot.render(OUTPUT_DIR / '03-fig-drug-target-prediction', cleanup=True)
    print("Saved: 03-fig-drug-target-prediction.svg")

def create_fig_04():  # Perturb-seq
    dot = graphviz.Digraph('perturbseq', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='14,4!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    steps = [
        ('guides', 'sgRNA\nLibrary', '#aec7e8'),
        ('perturb', 'Gene\nPerturbation', '#ff7f0e'),
        ('scrna', 'Single-cell\nRNA-seq', '#2ca02c'),
        ('embed', 'FM\nEmbedding', '#9467bd'),
        ('mech', 'Mechanism\nDiscovery', '#d62728'),
    ]
    for nid, label, color in steps:
        fc = 'white' if nid in ['embed', 'mech', 'perturb'] else 'black'
        dot.node(nid, label, fillcolor=color, fontcolor=fc, shape='box')
    for i in range(len(steps) - 1):
        dot.edge(steps[i][0], steps[i + 1][0])
    dot.render(OUTPUT_DIR / '04-fig-perturb-seq', cleanup=True)
    print("Saved: 04-fig-perturb-seq.svg")

def create_fig_05():  # Biomarker pipeline
    dot = graphviz.Digraph('biomarker', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='10,10!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    # Data sources
    with dot.subgraph(name='cluster_data') as c:
        c.attr(label='Multi-omic Data', style='rounded')
        c.node('genomics', 'Genomics', fillcolor='#1f77b4', fontcolor='white', shape='box')
        c.node('transcriptomics', 'Transcriptomics', fillcolor='#2ca02c', fontcolor='white', shape='box')
        c.node('proteomics', 'Proteomics', fillcolor='#ff7f0e', shape='box')
    # FM processing
    dot.node('fm', 'Foundation\nModels', fillcolor='#9467bd', fontcolor='white', shape='box')
    # Biomarker outputs
    with dot.subgraph(name='cluster_out') as c:
        c.attr(label='Biomarker Applications', style='rounded')
        c.node('response', 'Response\nPrediction', fillcolor='#98df8a', shape='box')
        c.node('stratify', 'Patient\nStratification', fillcolor='#98df8a', shape='box')
        c.node('monitor', 'Treatment\nMonitoring', fillcolor='#98df8a', shape='box')
    for n in ['genomics', 'transcriptomics', 'proteomics']:
        dot.edge(n, 'fm')
    for n in ['response', 'stratify', 'monitor']:
        dot.edge('fm', n)
    dot.render(OUTPUT_DIR / '05-fig-biomarker-pipeline', cleanup=True)
    print("Saved: 05-fig-biomarker-pipeline.svg")

if __name__ == '__main__':
    create_fig_01()
    create_fig_02()
    create_fig_03()
    create_fig_04()
    create_fig_05()
    print("All Chapter 29 figures generated.")
