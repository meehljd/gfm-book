#!/usr/bin/env python3
"""
Chapter 12: Confounding and Data Leakage Figures
Generates all 11 figures for this chapter.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import graphviz

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_2" / "ch12"
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

# Fig 01: Confounding DAG
def create_fig_01():
    dot = graphviz.Digraph('confounding_dag', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='10,6!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='10', style='filled,rounded', penwidth='1.5')

    # Left panel: Confounded
    with dot.subgraph(name='cluster_left') as c:
        c.attr(label='Confounded (Spurious Path)', labelloc='t', fontsize='11', fontname='Arial Bold')
        c.node('ancestry1', 'Ancestry', fillcolor='#ff7f0e', shape='ellipse')
        c.node('features1', 'Genomic\nFeatures', fillcolor='#aec7e8', shape='box')
        c.node('outcome1', 'Disease\nOutcome', fillcolor='#98df8a', shape='box')
        c.edge('ancestry1', 'features1', label='Allele\nfreq', color='#d62728', penwidth='2')
        c.edge('ancestry1', 'outcome1', label='Healthcare\naccess', color='#d62728', penwidth='2')
        c.edge('features1', 'outcome1', style='dashed', color='#555555', label='?')

    # Right panel: Adjusted
    with dot.subgraph(name='cluster_right') as c:
        c.attr(label='Adjusted (Blocked Spurious Path)', labelloc='t', fontsize='11', fontname='Arial Bold')
        c.node('ancestry2', 'Ancestry\n(conditioned)', fillcolor='#cccccc', shape='ellipse')
        c.node('features2', 'Genomic\nFeatures', fillcolor='#aec7e8', shape='box')
        c.node('outcome2', 'Disease\nOutcome', fillcolor='#98df8a', shape='box')
        c.edge('ancestry2', 'features2', style='dashed', color='#cccccc')
        c.edge('ancestry2', 'outcome2', style='dashed', color='#cccccc')
        c.edge('features2', 'outcome2', color='#2ca02c', penwidth='2', label='Genuine\neffect?')

    dot.render(OUTPUT_DIR / '01-fig-confounding-dag', cleanup=True)
    print("Saved: 01-fig-confounding-dag.svg")

# Fig 02 A-D: Population Structure as Shortcut
def create_fig_02():
    panels = [
        ('A', 'Population Structure in Genetic Data', 'pca'),
        ('B', 'Ancestry Encoded in Local Sequence', 'kmer'),
        ('C', 'Ancestry Creates Shortcut Pathways', 'dag'),
        ('D', 'Shortcuts Fail Across Populations', 'bar'),
    ]

    for panel_id, title, plot_type in panels:
        if plot_type == 'dag':
            dot = graphviz.Digraph(f'shortcut_{panel_id}', format='svg')
            dot.attr(rankdir='TB', splines='polyline', size='6,4!', ratio='compress')
            dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

            dot.node('ancestry', 'Ancestry', fillcolor='#ff7f0e', shape='ellipse')
            dot.node('features', 'Genomic\nFeatures', fillcolor='#aec7e8', shape='box')
            dot.node('labels', 'Disease\nLabels', fillcolor='#98df8a', shape='box')
            dot.node('model', 'Model\nPrediction', fillcolor='#9467bd', fontcolor='white', shape='box')

            dot.edge('ancestry', 'features', color='#d62728', penwidth='2')
            dot.edge('ancestry', 'labels', color='#d62728', penwidth='2', label='Healthcare')
            dot.edge('features', 'model')
            dot.edge('model', 'labels', style='dashed', label='Exploits\nshortcut')

            dot.render(OUTPUT_DIR / f'02-{panel_id}-fig-population-structure-shortcut', cleanup=True)
            print(f"Saved: 02-{panel_id}-fig-population-structure-shortcut.svg")
        else:
            fig, ax = plt.subplots(figsize=(5, 4))
            np.random.seed(42 + ord(panel_id))

            if plot_type == 'pca':
                # PCA showing ancestry clusters
                populations = ['European', 'East Asian', 'African']
                colors = ['#1f77b4', '#2ca02c', '#d62728']
                for i, (pop, color) in enumerate(zip(populations, colors)):
                    x = np.random.randn(30) + i * 3
                    y = np.random.randn(30) + (i % 2) * 2
                    ax.scatter(x, y, c=color, s=40, alpha=0.6, label=pop)
                ax.legend(fontsize=8)
                ax.set_xlabel('PC1', fontweight='bold')
                ax.set_ylabel('PC2', fontweight='bold')

            elif plot_type == 'kmer':
                # K-mer frequency differences
                kmers = ['ATAT', 'GCGC', 'TATA', 'CGCG']
                eur_freq = [0.05, 0.08, 0.04, 0.07]
                afr_freq = [0.03, 0.06, 0.06, 0.09]
                x = np.arange(len(kmers))
                width = 0.35
                ax.bar(x - width/2, eur_freq, width, label='European', color='#1f77b4')
                ax.bar(x + width/2, afr_freq, width, label='African', color='#d62728')
                ax.set_xticks(x)
                ax.set_xticklabels(kmers)
                ax.set_ylabel('K-mer Frequency', fontweight='bold')
                ax.legend(fontsize=8)

            elif plot_type == 'bar':
                # Performance degradation
                pops = ['EUR\n(train)', 'EAS', 'SAS', 'AFR']
                performance = [1.0, 0.7, 0.6, 0.4]
                colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#d62728']
                bars = ax.bar(pops, performance, color=colors, edgecolor='white')
                ax.axhline(y=0.5, color='#555555', linestyle='--', alpha=0.5)
                ax.set_ylabel('Relative Performance', fontweight='bold')
                ax.set_ylim(0, 1.2)
                # Add drop annotations
                for i, (bar, perf) in enumerate(zip(bars[1:], performance[1:]), 1):
                    drop = (1 - perf) * 100
                    ax.text(i, perf + 0.05, f'-{drop:.0f}%', ha='center', fontsize=9, color='#d62728')

            ax.set_title(f'{panel_id}. {title}', fontweight='bold', loc='left')
            plt.tight_layout()
            plt.savefig(OUTPUT_DIR / f'02-{panel_id}-fig-population-structure-shortcut.svg', format='svg')
            plt.close()
            print(f"Saved: 02-{panel_id}-fig-population-structure-shortcut.svg")

# Fig 03 A-C: Batch Effects
def create_fig_03():
    panels = [
        ('A', 'Embeddings Cluster by Batch', 'scatter'),
        ('B', 'Coverage Varies by Center', 'line'),
        ('C', 'Batch-Phenotype Confounding', 'bar'),
    ]

    for panel_id, title, plot_type in panels:
        fig, ax = plt.subplots(figsize=(5, 4))
        np.random.seed(42 + ord(panel_id))

        if plot_type == 'scatter':
            # Embeddings clustering by batch
            for i, (batch, color) in enumerate(zip(['Center A', 'Center B', 'Center C'],
                                                    ['#1f77b4', '#2ca02c', '#d62728'])):
                x = np.random.randn(30) + i * 2.5
                y = np.random.randn(30) + (i % 2) * 1.5
                ax.scatter(x, y, c=color, s=40, alpha=0.6, label=batch)
            ax.legend(fontsize=8, title='Sequencing Center')
            ax.set_xlabel('Embedding Dim 1', fontweight='bold')
            ax.set_ylabel('Embedding Dim 2', fontweight='bold')

        elif plot_type == 'line':
            # Coverage patterns by center
            positions = np.arange(0, 100)
            for i, (center, color) in enumerate(zip(['Center A', 'Center B'],
                                                     ['#1f77b4', '#d62728'])):
                baseline = 30 + i * 10
                coverage = baseline + np.sin(positions / 10 + i) * 5 + np.random.randn(100) * 2
                ax.plot(positions, coverage, color=color, alpha=0.8, label=center)
            ax.legend(fontsize=8)
            ax.set_xlabel('Genomic Position', fontweight='bold')
            ax.set_ylabel('Coverage', fontweight='bold')

        else:  # bar
            # Batch-phenotype correlation
            centers = ['Center A', 'Center B']
            cases = [85, 20]
            controls = [15, 80]
            x = np.arange(len(centers))
            width = 0.35
            ax.bar(x - width/2, cases, width, label='Cases', color='#d62728')
            ax.bar(x + width/2, controls, width, label='Controls', color='#1f77b4')
            ax.set_xticks(x)
            ax.set_xticklabels(centers)
            ax.set_ylabel('Percentage', fontweight='bold')
            ax.legend(fontsize=8)
            ax.text(0.5, 0.95, 'Confounded!', ha='center', transform=ax.transAxes,
                    fontsize=11, fontweight='bold', color='#d62728')

        ax.set_title(f'{panel_id}. {title}', fontweight='bold', loc='left')
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / f'03-{panel_id}-fig-batch-effects.svg', format='svg')
        plt.close()
        print(f"Saved: 03-{panel_id}-fig-batch-effects.svg")

# Fig 04: Label Circularity
def create_fig_04():
    dot = graphviz.Digraph('circularity', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='8,8!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='10', style='filled,rounded', penwidth='1.5')

    # The circular dependency
    dot.node('lab', 'Clinical\nLaboratory', fillcolor='#aec7e8', shape='box')
    dot.node('tools', 'Computational\nTools\n(CADD, REVEL)', fillcolor='#ff7f0e', shape='box')
    dot.node('clinvar', 'ClinVar\nDatabase', fillcolor='#98df8a', shape='box')
    dot.node('new_model', 'New Model\n(training)', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('eval', 'Evaluation\n(inflated)', fillcolor='#d62728', fontcolor='white', shape='box')

    # Edges showing circularity
    dot.edge('lab', 'tools', label='Uses for\nevidence')
    dot.edge('tools', 'clinvar', label='Influences\nannotations', color='#d62728', penwidth='2')
    dot.edge('clinvar', 'new_model', label='Training\nlabels')
    dot.edge('new_model', 'eval')
    dot.edge('eval', 'clinvar', style='dashed', label='Appears\naccurate', color='#d62728')

    dot.render(OUTPUT_DIR / '04-fig-label-circularity', cleanup=True)
    print("Saved: 04-fig-label-circularity.svg")

# Fig 05: Confounding Detection Toolkit
def create_fig_05():
    fig, ax = plt.subplots(figsize=(10, 6))

    diagnostics = [
        ('1. Confounder-only\nBaseline', 'If ancestry PCs alone\napproach model performance'),
        ('2. Stratified\nAnalysis', 'Performance gaps\nacross subgroups'),
        ('3. Residual\nAssociation', 'Predictions correlate\nwith ancestry'),
        ('4. Split\nSensitivity', 'Performance drops\nunder strict splits'),
        ('5. Negative\nControls', 'Model predicts\nunrelated outcomes'),
    ]

    colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd', '#d62728']

    for i, ((name, desc), color) in enumerate(zip(diagnostics, colors)):
        y = len(diagnostics) - i - 1
        ax.add_patch(mpatches.FancyBboxPatch((0.5, y - 0.35), 2.5, 0.7,
                                              boxstyle='round,pad=0.02',
                                              facecolor=color, alpha=0.7,
                                              edgecolor='white', linewidth=2))
        ax.text(1.75, y, name, ha='center', va='center', fontsize=10, color='white', fontweight='bold')

        ax.text(3.5, y, desc, ha='left', va='center', fontsize=9,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#cccccc'))

    ax.set_xlim(0, 8)
    ax.set_ylim(-0.5, len(diagnostics))
    ax.axis('off')
    ax.set_title('Diagnostic Toolkit for Detecting Confounding', fontweight='bold')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '05-fig-confounding-detection.svg', format='svg')
    plt.close()
    print("Saved: 05-fig-confounding-detection.svg")

# Fig 06: Mitigation Strategies
def create_fig_06():
    dot = graphviz.Digraph('mitigation', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='12,6!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    # Stages
    dot.node('design', 'Study\nDesign', fillcolor='#1f77b4', fontcolor='white', shape='box')
    dot.node('training', 'Model\nTraining', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.node('eval', 'Evaluation', fillcolor='#ff7f0e', fontcolor='white', shape='box')

    # Strategies
    dot.node('match', 'Matching\nBalanced Sampling', fillcolor='#aec7e8', shape='box')
    dot.node('adjust', 'Covariate\nAdjustment', fillcolor='#98df8a', shape='box')
    dot.node('adv', 'Adversarial\nInvariance', fillcolor='#98df8a', shape='box')
    dot.node('dro', 'Group\nDRO', fillcolor='#98df8a', shape='box')
    dot.node('multi', 'Multi-site\nTraining', fillcolor='#98df8a', shape='box')
    dot.node('temporal', 'Temporal\nSplits', fillcolor='#ffbb78', shape='box')
    dot.node('stratified', 'Stratified\nEvaluation', fillcolor='#ffbb78', shape='box')

    dot.edge('design', 'match')
    dot.edge('training', 'adjust')
    dot.edge('training', 'adv')
    dot.edge('training', 'dro')
    dot.edge('training', 'multi')
    dot.edge('eval', 'temporal')
    dot.edge('eval', 'stratified')

    dot.render(OUTPUT_DIR / '06-fig-mitigation-strategies', cleanup=True)
    print("Saved: 06-fig-mitigation-strategies.svg")

if __name__ == '__main__':
    create_fig_01()
    create_fig_02()
    create_fig_03()
    create_fig_04()
    create_fig_05()
    create_fig_06()
    print("All Chapter 12 figures generated.")
