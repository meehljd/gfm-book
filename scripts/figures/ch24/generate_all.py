#!/usr/bin/env python3
"""
Chapter 24: Interpretability Figures
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import graphviz

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_5" / "ch24"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    'font.family': 'sans-serif', 'font.sans-serif': ['Arial', 'DejaVu Sans'], 'font.size': 10,
    'axes.titlesize': 11, 'axes.titleweight': 'bold', 'figure.dpi': 150, 'savefig.dpi': 300,
    'savefig.bbox': 'tight', 'axes.spines.top': False, 'axes.spines.right': False,
})

def create_fig_01():  # Attribution comparison
    fig, ax = plt.subplots(figsize=(8, 5))
    methods = [('Saliency', 'Gradient magnitude', '#1f77b4'),
               ('Integrated\nGradients', 'Path integral', '#2ca02c'),
               ('DeepLIFT', 'Reference comparison', '#ff7f0e'),
               ('SHAP', 'Shapley values', '#9467bd'),
               ('Attention', 'Attention weights', '#d62728')]
    for i, (name, desc, color) in enumerate(methods):
        ax.add_patch(mpatches.FancyBboxPatch((i * 1.5 + 0.1, 0.3), 1.3, 1.8,
                                              boxstyle='round,pad=0.02', facecolor=color, alpha=0.7, edgecolor='white'))
        ax.text(i * 1.5 + 0.75, 1.5, name, ha='center', va='center', fontsize=9, fontweight='bold', color='white')
        ax.text(i * 1.5 + 0.75, 0.8, desc, ha='center', va='center', fontsize=8, color='white')
    ax.set_xlim(-0.2, 7.8)
    ax.set_ylim(-0.1, 2.5)
    ax.axis('off')
    ax.set_title('Attribution Methods Comparison', fontweight='bold')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-fig-attribution-comparison.svg', format='svg')
    plt.close()
    print("Saved: 01-fig-attribution-comparison.svg")

def create_fig_02():  # In silico mutagenesis
    np.random.seed(42)
    for panel, title in [('A', 'Reference Sequence'), ('B', 'Effect Scores')]:
        fig, ax = plt.subplots(figsize=(6, 4))
        if panel == 'A':
            seq = 'ATCGATCGATCG'
            for i, nt in enumerate(seq):
                color = {'A': '#2ca02c', 'T': '#d62728', 'G': '#ff7f0e', 'C': '#1f77b4'}[nt]
                ax.add_patch(mpatches.Rectangle((i, 0), 0.8, 0.8, facecolor=color, edgecolor='white'))
                ax.text(i + 0.4, 0.4, nt, ha='center', va='center', fontsize=12, color='white', fontweight='bold')
            ax.set_xlim(-0.5, 12.5)
            ax.set_ylim(-0.5, 1.5)
        else:
            positions = np.arange(12)
            effects = np.random.randn(12) * 2
            colors = ['#2ca02c' if e > 0 else '#d62728' for e in effects]
            ax.bar(positions, effects, color=colors, edgecolor='white')
            ax.axhline(y=0, color='#555555', linewidth=1)
            ax.set_xlabel('Position', fontweight='bold')
            ax.set_ylabel('Effect Score', fontweight='bold')
        ax.set_title(f'{panel}. {title}', fontweight='bold', loc='left')
        ax.axis('off' if panel == 'A' else 'on')
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / f'02-{panel}-fig-in-silico-mutagenesis.svg', format='svg')
        plt.close()
        print(f"Saved: 02-{panel}-fig-in-silico-mutagenesis.svg")

def create_fig_03():  # TF-MoDISco
    dot = graphviz.Digraph('tfmodisco', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='10,3!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    dot.node('attr', 'Attribution\nScores', fillcolor='#aec7e8', shape='box')
    dot.node('seqlets', 'Extract\nSeqlets', fillcolor='#98df8a', shape='box')
    dot.node('cluster', 'Cluster\nSeqlets', fillcolor='#ffbb78', shape='box')
    dot.node('motifs', 'Discovered\nMotifs', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.edge('attr', 'seqlets')
    dot.edge('seqlets', 'cluster')
    dot.edge('cluster', 'motifs')
    dot.render(OUTPUT_DIR / '03-fig-tfmodisco', cleanup=True)
    print("Saved: 03-fig-tfmodisco.svg")

def create_fig_04():  # Attention visualization
    np.random.seed(42)
    for panel, title in [('A', 'Self-Attention'), ('B', 'Cross-Attention'), ('C', 'Multi-Head')]:
        fig, ax = plt.subplots(figsize=(4, 4))
        attn = np.random.rand(8, 8)
        attn = attn / attn.sum(axis=1, keepdims=True)
        im = ax.imshow(attn, cmap='Blues', aspect='equal')
        ax.set_xlabel('Key Position', fontweight='bold')
        ax.set_ylabel('Query Position', fontweight='bold')
        ax.set_title(f'{panel}. {title}', fontweight='bold', loc='left')
        plt.colorbar(im, ax=ax)
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / f'04-{panel}-fig-attention-visualization.svg', format='svg')
        plt.close()
        print(f"Saved: 04-{panel}-fig-attention-visualization.svg")

def create_fig_05():  # Plausible vs faithful
    fig, ax = plt.subplots(figsize=(6, 5))
    categories = ['Saliency', 'Integrated\nGradients', 'Attention', 'LIME', 'SHAP']
    plausibility = [0.7, 0.8, 0.9, 0.75, 0.85]
    faithfulness = [0.5, 0.85, 0.4, 0.6, 0.78]
    x = np.arange(len(categories))
    width = 0.35
    ax.bar(x - width/2, plausibility, width, label='Plausibility', color='#1f77b4', edgecolor='white')
    ax.bar(x + width/2, faithfulness, width, label='Faithfulness', color='#2ca02c', edgecolor='white')
    ax.set_ylabel('Score', fontweight='bold')
    ax.set_title('Plausible vs Faithful Explanations', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=9)
    ax.legend(fontsize=9)
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '05-fig-plausible-vs-faithful.svg', format='svg')
    plt.close()
    print("Saved: 05-fig-plausible-vs-faithful.svg")

def create_fig_06():  # Validation pipeline
    dot = graphviz.Digraph('validation', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='8,6!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    dot.node('attr', 'Attribution\nScores', fillcolor='#aec7e8', shape='box')
    dot.node('motif', 'Motif\nMatch', fillcolor='#98df8a', shape='box')
    dot.node('perturb', 'Perturbation\nTests', fillcolor='#ffbb78', shape='box')
    dot.node('exper', 'Experimental\nValidation', fillcolor='#c5b0d5', shape='box')
    dot.node('valid', 'Validated\nExplanation', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.edge('attr', 'motif')
    dot.edge('attr', 'perturb')
    dot.edge('motif', 'valid')
    dot.edge('perturb', 'valid')
    dot.edge('exper', 'valid')
    dot.render(OUTPUT_DIR / '06-fig-validation-pipeline', cleanup=True)
    print("Saved: 06-fig-validation-pipeline.svg")

def create_fig_07():  # Clinical interpretability
    fig, ax = plt.subplots(figsize=(8, 5))
    stakeholders = [('Researcher', 'Mechanism discovery', '#1f77b4'),
                    ('Clinician', 'Decision support', '#2ca02c'),
                    ('Patient', 'Understanding risk', '#ff7f0e'),
                    ('Regulator', 'Audit trail', '#9467bd')]
    for i, (role, need, color) in enumerate(stakeholders):
        ax.add_patch(mpatches.FancyBboxPatch((i * 2 + 0.1, 0.3), 1.8, 1.5, boxstyle='round,pad=0.02',
                                              facecolor=color, alpha=0.7, edgecolor='white'))
        ax.text(i * 2 + 1, 1.3, role, ha='center', va='center', fontsize=10, fontweight='bold', color='white')
        ax.text(i * 2 + 1, 0.7, need, ha='center', va='center', fontsize=8, color='white')
    ax.set_xlim(-0.2, 8.2)
    ax.set_ylim(-0.1, 2)
    ax.axis('off')
    ax.set_title('Interpretability Needs by Stakeholder', fontweight='bold')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '07-fig-clinical-interpretability.svg', format='svg')
    plt.close()
    print("Saved: 07-fig-clinical-interpretability.svg")

if __name__ == '__main__':
    create_fig_01()
    create_fig_02()
    create_fig_03()
    create_fig_04()
    create_fig_05()
    create_fig_06()
    create_fig_07()
    print("All Chapter 24 figures generated.")
