#!/usr/bin/env python3
"""Chapter 28: Rare Disease Diagnosis Figures"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import graphviz

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_6" / "ch28"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family': 'sans-serif', 'font.sans-serif': ['Arial', 'DejaVu Sans'], 'font.size': 10,
    'axes.titlesize': 11, 'axes.titleweight': 'bold', 'figure.dpi': 150, 'savefig.dpi': 300,
    'savefig.bbox': 'tight', 'axes.spines.top': False, 'axes.spines.right': False})

def create_fig_01():  # Rare disease funnel
    fig, ax = plt.subplots(figsize=(8, 6))
    stages = [
        ('All Variants', 5000000, '#aec7e8'),
        ('Rare (AF < 1%)', 100000, '#98df8a'),
        ('Coding/Splice', 5000, '#ffbb78'),
        ('Predicted Damaging', 500, '#ff7f0e'),
        ('Gene Match', 50, '#d62728'),
        ('Diagnostic', 1, '#9467bd'),
    ]
    max_width = 0.9
    y_positions = np.linspace(0.85, 0.1, len(stages))
    for i, (label, count, color) in enumerate(stages):
        width = max_width * (np.log10(count + 1) / np.log10(stages[0][1] + 1))
        rect = mpatches.FancyBboxPatch(
            (0.5 - width / 2, y_positions[i] - 0.05), width, 0.08,
            boxstyle='round,pad=0.01', facecolor=color, edgecolor='white', linewidth=2
        )
        ax.add_patch(rect)
        ax.text(0.5, y_positions[i], f'{label}\n({count:,})', ha='center', va='center', fontsize=9, fontweight='bold')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    ax.set_title('Variant Filtering Pipeline for Rare Disease', fontweight='bold')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-fig-rare-disease-funnel.svg', format='svg')
    plt.close()
    print("Saved: 01-fig-rare-disease-funnel.svg")

def create_fig_02():  # ACMG-AMP framework
    dot = graphviz.Digraph('acmg', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='10,10!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    with dot.subgraph(name='cluster_evidence') as c:
        c.attr(label='Evidence Categories', style='rounded')
        c.node('pvs', 'Very Strong\n(PVS1)', fillcolor='#d62728', fontcolor='white', shape='box')
        c.node('ps', 'Strong\n(PS1-4)', fillcolor='#ff7f0e', shape='box')
        c.node('pm', 'Moderate\n(PM1-6)', fillcolor='#ffbb78', shape='box')
        c.node('pp', 'Supporting\n(PP1-5)', fillcolor='#98df8a', shape='box')
    with dot.subgraph(name='cluster_benign') as c:
        c.attr(label='Benign Evidence', style='rounded')
        c.node('ba', 'Stand-alone\n(BA1)', fillcolor='#2ca02c', fontcolor='white', shape='box')
        c.node('bs', 'Strong\n(BS1-4)', fillcolor='#aec7e8', shape='box')
        c.node('bp', 'Supporting\n(BP1-7)', fillcolor='#c5b0d5', shape='box')
    dot.node('combine', 'Evidence\nCombination', fillcolor='#9467bd', fontcolor='white', shape='box')
    classes = ['Pathogenic', 'Likely\nPathogenic', 'VUS', 'Likely\nBenign', 'Benign']
    for i, cls in enumerate(classes):
        color = '#d62728' if i < 2 else '#2ca02c' if i > 2 else '#ff7f0e'
        fc = 'white' if i != 2 else 'black'
        dot.node(f'class{i}', cls, fillcolor=color, fontcolor=fc, shape='box')
    for n in ['pvs', 'ps', 'pm', 'pp', 'ba', 'bs', 'bp']:
        dot.edge(n, 'combine')
    for i in range(5):
        dot.edge('combine', f'class{i}')
    dot.render(OUTPUT_DIR / '02-fig-acmg-amp', cleanup=True)
    print("Saved: 02-fig-acmg-amp.svg")

def create_fig_03():  # Family analysis - 3 panels
    # Panel A: Inheritance patterns
    patterns = [
        ('Autosomal\nDominant', 'AD'),
        ('Autosomal\nRecessive', 'AR'),
        ('X-linked', 'XL'),
        ('De novo', 'DN'),
    ]
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#d62728']
    for i, ((label, abbr), color) in enumerate(zip(patterns, colors)):
        ax.add_patch(mpatches.FancyBboxPatch(
            (i * 2 + 0.2, 0.3), 1.6, 1.5, boxstyle='round,pad=0.02',
            facecolor=color, alpha=0.7, edgecolor='white', linewidth=2
        ))
        ax.text(i * 2 + 1, 1.3, label, ha='center', va='center', fontsize=10, fontweight='bold', color='white')
        ax.text(i * 2 + 1, 0.7, abbr, ha='center', va='center', fontsize=14, fontweight='bold', color='white')
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 2.2)
    ax.axis('off')
    ax.set_title('A. Inheritance Patterns', fontweight='bold', loc='left')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '03-A-fig-family-analysis.svg', format='svg')
    plt.close()
    print("Saved: 03-A-fig-family-analysis.svg")

    # Panel B: Trio analysis
    dot = graphviz.Digraph('trio', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='6,5!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    dot.node('father', 'Father\n(WT/WT)', fillcolor='#aec7e8', shape='box')
    dot.node('mother', 'Mother\n(WT/WT)', fillcolor='#ffcccb', shape='box')
    dot.node('child', 'Proband\n(WT/MUT)', fillcolor='#d62728', fontcolor='white', shape='box')
    dot.edge('father', 'child')
    dot.edge('mother', 'child')
    dot.node('denovo', 'De novo\nConfirmed', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.edge('child', 'denovo')
    dot.render(OUTPUT_DIR / '03-B-fig-family-analysis', cleanup=True)
    print("Saved: 03-B-fig-family-analysis.svg")

    # Panel C: Segregation in extended pedigree
    dot = graphviz.Digraph('segregation', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='8,6!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    # Generation 1
    dot.node('g1m', 'I-1\nAffected', fillcolor='#d62728', fontcolor='white', shape='box')
    dot.node('g1f', 'I-2\nUnaffected', fillcolor='#98df8a', shape='box')
    # Generation 2
    dot.node('g2a', 'II-1\nAffected', fillcolor='#d62728', fontcolor='white', shape='box')
    dot.node('g2b', 'II-2\nUnaffected', fillcolor='#98df8a', shape='box')
    dot.node('g2c', 'II-3\nAffected', fillcolor='#d62728', fontcolor='white', shape='box')
    dot.edge('g1m', 'g2a')
    dot.edge('g1f', 'g2a')
    dot.edge('g1m', 'g2b')
    dot.edge('g1f', 'g2b')
    dot.edge('g1m', 'g2c')
    dot.edge('g1f', 'g2c')
    dot.render(OUTPUT_DIR / '03-C-fig-family-analysis', cleanup=True)
    print("Saved: 03-C-fig-family-analysis.svg")

def create_fig_04():  # Somatic vs germline - 2 panels
    # Panel A: Origins
    dot = graphviz.Digraph('origins', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='10,4!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    dot.node('zygote', 'Zygote', fillcolor='#aec7e8', shape='box')
    dot.node('germline', 'Germline\nCells', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.node('somatic', 'Somatic\nCells', fillcolor='#ff7f0e', shape='box')
    dot.node('inherited', 'Inherited\nVariants', fillcolor='#1f77b4', fontcolor='white', shape='box')
    dot.node('acquired', 'Acquired\nVariants', fillcolor='#d62728', fontcolor='white', shape='box')
    dot.edge('zygote', 'germline')
    dot.edge('zygote', 'somatic')
    dot.edge('germline', 'inherited')
    dot.edge('somatic', 'acquired')
    dot.render(OUTPUT_DIR / '04-A-fig-somatic-germline', cleanup=True)
    print("Saved: 04-A-fig-somatic-germline.svg")

    # Panel B: Diagnostic implications
    fig, ax = plt.subplots(figsize=(6, 4))
    implications = [
        ('Germline', ['Family testing', 'Recurrence risk', 'Inheritance counseling'], '#2ca02c'),
        ('Somatic', ['Tumor-specific', 'Treatment selection', 'No family risk'], '#ff7f0e'),
    ]
    for i, (vtype, items, color) in enumerate(implications):
        ax.add_patch(mpatches.FancyBboxPatch(
            (i * 3.5 + 0.2, 0.2), 3, 2.5, boxstyle='round,pad=0.02',
            facecolor=color, alpha=0.3, edgecolor=color, linewidth=2
        ))
        ax.text(i * 3.5 + 1.7, 2.4, vtype, ha='center', fontsize=11, fontweight='bold', color=color)
        for j, item in enumerate(items):
            ax.text(i * 3.5 + 1.7, 1.8 - j * 0.5, f'• {item}', ha='center', fontsize=9)
    ax.set_xlim(0, 7)
    ax.set_ylim(0, 3)
    ax.axis('off')
    ax.set_title('B. Diagnostic Implications', fontweight='bold', loc='left')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-B-fig-somatic-germline.svg', format='svg')
    plt.close()
    print("Saved: 04-B-fig-somatic-germline.svg")

def create_fig_05():  # Functional validation hierarchy
    fig, ax = plt.subplots(figsize=(8, 5))
    evidence = [
        ('In silico\nprediction', 0.3, '#d62728'),
        ('Population\nfrequency', 0.4, '#ff7f0e'),
        ('Functional\nassay', 0.7, '#ffbb78'),
        ('Patient\nphenotype', 0.8, '#98df8a'),
        ('Model\norganism', 0.9, '#2ca02c'),
    ]
    for i, (name, strength, color) in enumerate(evidence):
        ax.barh(i, strength, color=color, edgecolor='white', height=0.6)
        ax.text(strength + 0.02, i, f'{strength:.0%}', va='center', fontsize=9)
    ax.set_yticks(range(len(evidence)))
    ax.set_yticklabels([e[0] for e in evidence], fontsize=9)
    ax.set_xlabel('Evidence Weight', fontweight='bold')
    ax.set_title('Functional Validation Evidence Hierarchy', fontweight='bold')
    ax.set_xlim(0, 1.1)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '05-fig-functional-validation.svg', format='svg')
    plt.close()
    print("Saved: 05-fig-functional-validation.svg")

def create_fig_06():  # Human-AI partnership
    dot = graphviz.Digraph('partnership', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='12,5!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    # AI contributions
    with dot.subgraph(name='cluster_ai') as c:
        c.attr(label='AI/FM Contributions', style='rounded')
        c.node('filter', 'Variant\nFiltering', fillcolor='#1f77b4', fontcolor='white', shape='box')
        c.node('predict', 'Pathogenicity\nPrediction', fillcolor='#1f77b4', fontcolor='white', shape='box')
        c.node('prioritize', 'Candidate\nPrioritization', fillcolor='#1f77b4', fontcolor='white', shape='box')
    # Human contributions
    with dot.subgraph(name='cluster_human') as c:
        c.attr(label='Human Expert Contributions', style='rounded')
        c.node('phenotype', 'Phenotype\nMatching', fillcolor='#2ca02c', fontcolor='white', shape='box')
        c.node('context', 'Clinical\nContext', fillcolor='#2ca02c', fontcolor='white', shape='box')
        c.node('interpret', 'Final\nInterpretation', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.node('diagnosis', 'Diagnostic\nReport', fillcolor='#9467bd', fontcolor='white', shape='box')
    for n in ['filter', 'predict', 'prioritize', 'phenotype', 'context', 'interpret']:
        dot.edge(n, 'diagnosis')
    dot.render(OUTPUT_DIR / '06-fig-interpretive-partnership', cleanup=True)
    print("Saved: 06-fig-interpretive-partnership.svg")

if __name__ == '__main__':
    create_fig_01()
    create_fig_02()
    create_fig_03()
    create_fig_04()
    create_fig_05()
    create_fig_06()
    print("All Chapter 28 figures generated.")
