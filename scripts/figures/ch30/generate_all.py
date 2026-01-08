#!/usr/bin/env python3
"""Chapter 30: Sequence Design Figures"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import graphviz

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_6" / "ch30"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family': 'sans-serif', 'font.sans-serif': ['Arial', 'DejaVu Sans'], 'font.size': 10,
    'axes.titlesize': 11, 'axes.titleweight': 'bold', 'figure.dpi': 150, 'savefig.dpi': 300,
    'savefig.bbox': 'tight', 'axes.spines.top': False, 'axes.spines.right': False})

def create_fig_01():  # Design formalism - 2 panels
    # Panel A: Forward prediction
    dot = graphviz.Digraph('forward', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='8,3!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    dot.node('seq', 'Sequence', fillcolor='#1f77b4', fontcolor='white', shape='box')
    dot.node('fm', 'Foundation\nModel', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('func', 'Function', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.edge('seq', 'fm', label='Forward')
    dot.edge('fm', 'func')
    dot.render(OUTPUT_DIR / '01-A-fig-design-formalism', cleanup=True)
    print("Saved: 01-A-fig-design-formalism.svg")

    # Panel B: Inverse design
    fig, ax = plt.subplots(figsize=(8, 5))
    # Draw fitness landscape
    np.random.seed(42)
    x = np.linspace(0, 10, 100)
    y = np.sin(x) * 0.5 + np.random.randn(100) * 0.1 + 1
    ax.fill_between(x, 0, y, alpha=0.3, color='#9467bd')
    ax.plot(x, y, color='#9467bd', linewidth=2)
    # Mark optimal region
    ax.axvspan(7, 8.5, alpha=0.3, color='#2ca02c')
    ax.annotate('Target\nFunction', xy=(7.75, 1.5), fontsize=10, ha='center',
                fontweight='bold', color='#2ca02c')
    ax.annotate('Vast sequence\nspace', xy=(3, 0.5), fontsize=9, ha='center')
    ax.set_xlabel('Sequence Space', fontweight='bold')
    ax.set_ylabel('Fitness', fontweight='bold')
    ax.set_title('B. Inverse Design: Function → Sequence', fontweight='bold', loc='left')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 2)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-B-fig-design-formalism.svg', format='svg')
    plt.close()
    print("Saved: 01-B-fig-design-formalism.svg")

def create_fig_02():  # Protein design - 2 panels
    # Panel A: Directed evolution in silico
    dot = graphviz.Digraph('evolution', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='8,6!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    dot.node('parent', 'Parent\nSequence', fillcolor='#aec7e8', shape='box')
    dot.node('mutate', 'Mutate', fillcolor='#ff7f0e', shape='box')
    dot.node('score', 'FM\nScore', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('select', 'Select\nTop', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.node('iterate', 'Iterate', fillcolor='#d62728', fontcolor='white', shape='box')
    dot.edge('parent', 'mutate')
    dot.edge('mutate', 'score')
    dot.edge('score', 'select')
    dot.edge('select', 'iterate')
    dot.edge('iterate', 'mutate', constraint='false')
    dot.render(OUTPUT_DIR / '02-A-fig-protein-design', cleanup=True)
    print("Saved: 02-A-fig-protein-design.svg")

    # Panel B: Generative design
    dot = graphviz.Digraph('generative', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='10,4!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    dot.node('prior', 'FM\nPrior', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('condition', 'Property\nCondition', fillcolor='#ff7f0e', shape='box')
    dot.node('sample', 'Sample', fillcolor='#1f77b4', fontcolor='white', shape='box')
    dot.node('novel', 'Novel\nSequences', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.edge('prior', 'sample')
    dot.edge('condition', 'sample')
    dot.edge('sample', 'novel')
    dot.render(OUTPUT_DIR / '02-B-fig-protein-design', cleanup=True)
    print("Saved: 02-B-fig-protein-design.svg")

def create_fig_03():  # Regulatory element design
    dot = graphviz.Digraph('regulatory', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='10,10!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    with dot.subgraph(name='cluster_input') as c:
        c.attr(label='Design Inputs', style='rounded')
        c.node('cell', 'Target\nCell Type', fillcolor='#aec7e8', shape='box')
        c.node('expr', 'Expression\nLevel', fillcolor='#98df8a', shape='box')
        c.node('spec', 'Specificity', fillcolor='#ffbb78', shape='box')
    dot.node('dna_fm', 'DNA\nFoundation Model', fillcolor='#1f77b4', fontcolor='white', shape='box')
    dot.node('optimize', 'Gradient\nOptimization', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('promoter', 'Designed\nPromoter', fillcolor='#2ca02c', fontcolor='white', shape='box')
    for n in ['cell', 'expr', 'spec']:
        dot.edge(n, 'dna_fm')
    dot.edge('dna_fm', 'optimize')
    dot.edge('optimize', 'promoter')
    dot.render(OUTPUT_DIR / '03-fig-regulatory-design', cleanup=True)
    print("Saved: 03-fig-regulatory-design.svg")

def create_fig_04():  # mRNA optimization
    dot = graphviz.Digraph('mrna', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='14,4!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    steps = [
        ('protein', 'Target\nProtein', '#aec7e8'),
        ('codon', 'Codon\nOptimization', '#98df8a'),
        ('utr', 'UTR\nDesign', '#ffbb78'),
        ('fm', 'FM\nScoring', '#9467bd'),
        ('mrna', 'Optimized\nmRNA', '#2ca02c'),
    ]
    for nid, label, color in steps:
        fc = 'white' if nid in ['fm', 'mrna'] else 'black'
        dot.node(nid, label, fillcolor=color, fontcolor=fc, shape='box')
    for i in range(len(steps) - 1):
        dot.edge(steps[i][0], steps[i + 1][0])
    dot.render(OUTPUT_DIR / '04-fig-mrna-optimization', cleanup=True)
    print("Saved: 04-fig-mrna-optimization.svg")

def create_fig_05():  # Antibody design
    dot = graphviz.Digraph('antibody', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='10,8!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    with dot.subgraph(name='cluster_structure') as c:
        c.attr(label='Antibody Structure', style='rounded')
        c.node('vh', 'VH\nDomain', fillcolor='#1f77b4', fontcolor='white', shape='box')
        c.node('vl', 'VL\nDomain', fillcolor='#2ca02c', fontcolor='white', shape='box')
        c.node('cdr', 'CDR\nLoops', fillcolor='#d62728', fontcolor='white', shape='box')
    dot.node('fm', 'Protein FM', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('design', 'CDR\nDesign', fillcolor='#ff7f0e', shape='box')
    dot.node('affinity', 'Affinity\nMaturation', fillcolor='#ffbb78', shape='box')
    dot.edge('vh', 'fm')
    dot.edge('vl', 'fm')
    dot.edge('cdr', 'fm')
    dot.edge('fm', 'design')
    dot.edge('design', 'affinity')
    dot.render(OUTPUT_DIR / '05-fig-antibody-design', cleanup=True)
    print("Saved: 05-fig-antibody-design.svg")

def create_fig_06():  # DBTL cycle
    dot = graphviz.Digraph('dbtl', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='8,8!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    stages = [
        ('design', 'Design', '#1f77b4'),
        ('build', 'Build', '#2ca02c'),
        ('test', 'Test', '#ff7f0e'),
        ('learn', 'Learn', '#9467bd'),
    ]
    for nid, label, color in stages:
        dot.node(nid, label, fillcolor=color, fontcolor='white', shape='box')
    dot.edge('design', 'build')
    dot.edge('build', 'test')
    dot.edge('test', 'learn')
    dot.edge('learn', 'design', label='FM\nUpdate')
    dot.render(OUTPUT_DIR / '06-fig-dbtl-cycle', cleanup=True)
    print("Saved: 06-fig-dbtl-cycle.svg")

def create_fig_07():  # Generative evaluation
    fig, ax = plt.subplots(figsize=(8, 5))
    metrics = ['Novelty', 'Diversity', 'Validity', 'Property\nMatch', 'Synthesiz-\nability']
    model_a = [0.85, 0.70, 0.95, 0.75, 0.60]
    model_b = [0.60, 0.85, 0.90, 0.80, 0.75]
    x = np.arange(len(metrics))
    width = 0.35
    ax.bar(x - width / 2, model_a, width, label='VAE-based', color='#1f77b4', edgecolor='white')
    ax.bar(x + width / 2, model_b, width, label='FM-based', color='#2ca02c', edgecolor='white')
    ax.set_ylabel('Score', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(metrics, fontsize=9)
    ax.legend(fontsize=9)
    ax.set_ylim(0, 1)
    ax.set_title('Evaluating Generative Sequence Models', fontweight='bold')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '07-fig-generative-evaluation.svg', format='svg')
    plt.close()
    print("Saved: 07-fig-generative-evaluation.svg")

if __name__ == '__main__':
    create_fig_01()
    create_fig_02()
    create_fig_03()
    create_fig_04()
    create_fig_05()
    create_fig_06()
    create_fig_07()
    print("All Chapter 30 figures generated.")
