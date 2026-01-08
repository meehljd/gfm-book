#!/usr/bin/env python3
"""Chapter 31: Frontiers Figures"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import graphviz

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_6" / "ch31"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family': 'sans-serif', 'font.sans-serif': ['Arial', 'DejaVu Sans'], 'font.size': 10,
    'axes.titlesize': 11, 'axes.titleweight': 'bold', 'figure.dpi': 150, 'savefig.dpi': 300,
    'savefig.bbox': 'tight', 'axes.spines.top': False, 'axes.spines.right': False})

def create_fig_01():  # Multiscale integration
    dot = graphviz.Digraph('multiscale', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='12,10!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    scales = [
        ('nucleotide', 'Nucleotide\n(1 bp)', '#1f77b4'),
        ('motif', 'Motif\n(10-20 bp)', '#2ca02c'),
        ('element', 'Element\n(100-1000 bp)', '#ff7f0e'),
        ('gene', 'Gene\n(1-100 kb)', '#9467bd'),
        ('chromosome', 'Chromosome\n(Mb-Gb)', '#d62728'),
    ]
    for nid, label, color in scales:
        dot.node(nid, label, fillcolor=color, fontcolor='white', shape='box')
    for i in range(len(scales) - 1):
        dot.edge(scales[i][0], scales[i + 1][0], label='↑ Scale')
    dot.node('unified', 'Unified\nFoundation Model', fillcolor='#555555', fontcolor='white', shape='box')
    for nid, _, _ in scales:
        dot.edge(nid, 'unified', style='dashed')
    dot.render(OUTPUT_DIR / '01-fig-multiscale-integration', cleanup=True)
    print("Saved: 01-fig-multiscale-integration.svg")

def create_fig_02():  # Agentic systems
    dot = graphviz.Digraph('agentic', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='10,10!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    with dot.subgraph(name='cluster_agent') as c:
        c.attr(label='Agentic Scientific System', style='rounded')
        c.node('hypothesis', 'Hypothesis\nGeneration', fillcolor='#1f77b4', fontcolor='white', shape='box')
        c.node('experiment', 'Experiment\nDesign', fillcolor='#2ca02c', fontcolor='white', shape='box')
        c.node('analysis', 'Data\nAnalysis', fillcolor='#ff7f0e', shape='box')
        c.node('synthesis', 'Knowledge\nSynthesis', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('fm', 'Genomic FM', fillcolor='#d62728', fontcolor='white', shape='box')
    dot.node('lab', 'Automated\nLab', fillcolor='#aec7e8', shape='box')
    dot.edge('hypothesis', 'experiment')
    dot.edge('experiment', 'lab')
    dot.edge('lab', 'analysis')
    dot.edge('analysis', 'synthesis')
    dot.edge('synthesis', 'hypothesis')
    dot.edge('fm', 'hypothesis')
    dot.edge('fm', 'analysis')
    dot.render(OUTPUT_DIR / '02-fig-agentic-systems', cleanup=True)
    print("Saved: 02-fig-agentic-systems.svg")

def create_fig_03():  # Learning health system
    dot = graphviz.Digraph('lhs', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='12,8!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    with dot.subgraph(name='cluster_clinical') as c:
        c.attr(label='Clinical Care', style='rounded')
        c.node('patient', 'Patient\nData', fillcolor='#aec7e8', shape='box')
        c.node('decision', 'Clinical\nDecision', fillcolor='#98df8a', shape='box')
        c.node('outcome', 'Outcome', fillcolor='#ffbb78', shape='box')
    with dot.subgraph(name='cluster_learning') as c:
        c.attr(label='Learning System', style='rounded')
        c.node('aggregate', 'Aggregate\nData', fillcolor='#1f77b4', fontcolor='white', shape='box')
        c.node('fm', 'Foundation\nModel', fillcolor='#9467bd', fontcolor='white', shape='box')
        c.node('update', 'Model\nUpdate', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.edge('patient', 'decision')
    dot.edge('decision', 'outcome')
    dot.edge('outcome', 'aggregate')
    dot.edge('aggregate', 'fm')
    dot.edge('fm', 'update')
    dot.edge('update', 'decision')
    dot.render(OUTPUT_DIR / '03-fig-learning-health-system', cleanup=True)
    print("Saved: 03-fig-learning-health-system.svg")

def create_fig_04():  # Scaling laws
    fig, ax = plt.subplots(figsize=(8, 5))
    np.random.seed(42)
    params = np.array([1e6, 1e7, 1e8, 1e9, 1e10, 1e11])
    loss = 2.0 * (params / 1e6) ** -0.1 + np.random.randn(6) * 0.02
    downstream = 0.6 + 0.15 * np.log10(params / 1e6) + np.random.randn(6) * 0.01
    ax.loglog(params, loss, 'o-', color='#d62728', linewidth=2, markersize=8, label='Pretraining Loss')
    ax2 = ax.twinx()
    ax2.semilogx(params, downstream, 's-', color='#2ca02c', linewidth=2, markersize=8, label='Downstream Perf.')
    ax.set_xlabel('Model Parameters', fontweight='bold')
    ax.set_ylabel('Pretraining Loss', fontweight='bold', color='#d62728')
    ax2.set_ylabel('Downstream Performance', fontweight='bold', color='#2ca02c')
    ax.tick_params(axis='y', labelcolor='#d62728')
    ax2.tick_params(axis='y', labelcolor='#2ca02c')
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, fontsize=9, loc='center right')
    ax.set_title('Scaling Laws for Genomic Foundation Models', fontweight='bold')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-fig-scaling-laws.svg', format='svg')
    plt.close()
    print("Saved: 04-fig-scaling-laws.svg")

def create_fig_05():  # Correlation vs causation
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    np.random.seed(42)
    # Panel A: Correlation
    ax = axes[0]
    x = np.random.randn(50)
    y = 0.8 * x + np.random.randn(50) * 0.3
    ax.scatter(x, y, c='#1f77b4', alpha=0.6, s=50)
    ax.plot(np.linspace(-3, 3, 10), 0.8 * np.linspace(-3, 3, 10), 'r--', linewidth=2)
    ax.set_xlabel('Predicted Effect', fontweight='bold')
    ax.set_ylabel('Observed Association', fontweight='bold')
    ax.set_title('A. Correlation', fontweight='bold', loc='left')
    # Panel B: Causation requires intervention
    ax = axes[1]
    # Confounded
    x_conf = np.random.randn(25) + 1
    y_conf = 0.5 * x_conf + np.random.randn(25) * 0.5 + 1
    # Intervened
    x_int = np.random.randn(25) - 1
    y_int = 0.8 * x_int + np.random.randn(25) * 0.2 - 1
    ax.scatter(x_conf, y_conf, c='#d62728', alpha=0.6, s=50, label='Observational')
    ax.scatter(x_int, y_int, c='#2ca02c', alpha=0.6, s=50, label='Interventional')
    ax.legend(fontsize=9)
    ax.set_xlabel('Gene Expression', fontweight='bold')
    ax.set_ylabel('Phenotype', fontweight='bold')
    ax.set_title('B. Causation', fontweight='bold', loc='left')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '05-fig-correlation-causation.svg', format='svg')
    plt.close()
    print("Saved: 05-fig-correlation-causation.svg")

def create_fig_06():  # Translation gap
    fig, ax = plt.subplots(figsize=(8, 5))
    stages = ['Benchmark\nPerformance', 'Research\nValidation', 'Clinical\nTrial', 'Real-world\nImpact']
    performance = [0.95, 0.80, 0.65, 0.45]
    colors = ['#2ca02c', '#98df8a', '#ffbb78', '#d62728']
    bars = ax.bar(stages, performance, color=colors, edgecolor='white')
    ax.axhline(y=0.5, color='#555555', linestyle='--', alpha=0.5)
    ax.text(3.5, 0.52, 'Minimum useful', fontsize=8)
    for bar, p in zip(bars, performance):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02,
                f'{p:.0%}', ha='center', fontsize=10, fontweight='bold')
    # Draw translation gap annotation
    ax.annotate('', xy=(3, 0.45), xytext=(0, 0.95),
                arrowprops=dict(arrowstyle='->', color='#555555', lw=2, ls='--'))
    ax.text(1.5, 0.75, 'Translation\nGap', fontsize=10, ha='center', color='#555555')
    ax.set_ylabel('Performance', fontweight='bold')
    ax.set_ylim(0, 1.1)
    ax.set_title('Translation Gap: Benchmarks to Clinical Impact', fontweight='bold')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '06-fig-translation-gap.svg', format='svg')
    plt.close()
    print("Saved: 06-fig-translation-gap.svg")

if __name__ == '__main__':
    create_fig_01()
    create_fig_02()
    create_fig_03()
    create_fig_04()
    create_fig_05()
    create_fig_06()
    print("All Chapter 31 figures generated.")
