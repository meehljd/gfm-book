#!/usr/bin/env python3
"""Chapter 25: Causal Inference Figures"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import graphviz

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_5" / "ch25"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family': 'sans-serif', 'font.sans-serif': ['Arial', 'DejaVu Sans'], 'font.size': 10,
    'axes.titlesize': 11, 'axes.titleweight': 'bold', 'figure.dpi': 150, 'savefig.dpi': 300,
    'savefig.bbox': 'tight', 'axes.spines.top': False, 'axes.spines.right': False})

def create_fig_01():  # Ladder of causation
    dot = graphviz.Digraph('ladder', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='8,8!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    dot.node('l3', 'Counterfactual\n"What if...?"', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.node('l2', 'Intervention\n"What happens if...?"', fillcolor='#ff7f0e', shape='box')
    dot.node('l1', 'Association\n"What is...?"', fillcolor='#1f77b4', fontcolor='white', shape='box')
    dot.edge('l1', 'l2', label='Causal\nmodeling')
    dot.edge('l2', 'l3', label='Counterfactual\nreasoning')
    dot.render(OUTPUT_DIR / '01-fig-ladder-causation', cleanup=True)
    print("Saved: 01-fig-ladder-causation.svg")

def create_fig_02():  # GWAS to gene
    dot = graphviz.Digraph('gwas', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='12,4!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    dot.node('gwas', 'GWAS\nSignal', fillcolor='#aec7e8', shape='box')
    dot.node('finemapping', 'Statistical\nFine-mapping', fillcolor='#98df8a', shape='box')
    dot.node('colocalization', 'eQTL\nColocalization', fillcolor='#ffbb78', shape='box')
    dot.node('gene', 'Causal\nGene', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.edge('gwas', 'finemapping')
    dot.edge('finemapping', 'colocalization')
    dot.edge('colocalization', 'gene')
    dot.render(OUTPUT_DIR / '02-fig-gwas-to-gene', cleanup=True)
    print("Saved: 02-fig-gwas-to-gene.svg")

def create_fig_03():  # Closed loop causal
    dot = graphviz.Digraph('closedloop', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='10,6!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    dot.node('obs', 'Observational\nData', fillcolor='#aec7e8', shape='box')
    dot.node('model', 'Causal\nModel', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('predict', 'Predicted\nIntervention', fillcolor='#ffbb78', shape='box')
    dot.node('exp', 'Experimental\nValidation', fillcolor='#98df8a', shape='box')
    dot.node('refine', 'Model\nRefinement', fillcolor='#d62728', fontcolor='white', shape='box')
    dot.edge('obs', 'model')
    dot.edge('model', 'predict')
    dot.edge('predict', 'exp')
    dot.edge('exp', 'refine')
    dot.edge('refine', 'model')
    dot.render(OUTPUT_DIR / '03-fig-closed-loop-causal', cleanup=True)
    print("Saved: 03-fig-closed-loop-causal.svg")

def create_fig_04():  # Evidence hierarchy
    fig, ax = plt.subplots(figsize=(8, 5))
    evidence = [('In silico\nprediction', 0.3, '#d62728'),
                ('Observational\nassociation', 0.5, '#ff7f0e'),
                ('Natural\nexperiment', 0.7, '#ffbb78'),
                ('Functional\nassay', 0.85, '#2ca02c'),
                ('Randomized\ntrial', 1.0, '#1f77b4')]
    for i, (name, strength, color) in enumerate(evidence):
        ax.barh(i, strength, color=color, edgecolor='white', height=0.6)
        ax.text(strength + 0.02, i, f'{strength:.0%}', va='center', fontsize=9)
    ax.set_yticks(range(len(evidence)))
    ax.set_yticklabels([e[0] for e in evidence], fontsize=9)
    ax.set_xlabel('Causal Evidence Strength', fontweight='bold')
    ax.set_title('Hierarchy of Causal Evidence', fontweight='bold')
    ax.set_xlim(0, 1.15)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-fig-evidence-hierarchy.svg', format='svg')
    plt.close()
    print("Saved: 04-fig-evidence-hierarchy.svg")

if __name__ == '__main__':
    create_fig_01()
    create_fig_02()
    create_fig_03()
    create_fig_04()
    print("All Chapter 25 figures generated.")
