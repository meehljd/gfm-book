#!/usr/bin/env python3
"""Chapter 26: Regulatory and Ethics Figures"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import graphviz

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_5" / "ch26"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family': 'sans-serif', 'font.sans-serif': ['Arial', 'DejaVu Sans'], 'font.size': 10,
    'axes.titlesize': 11, 'axes.titleweight': 'bold', 'figure.dpi': 150, 'savefig.dpi': 300,
    'savefig.bbox': 'tight', 'axes.spines.top': False, 'axes.spines.right': False})

def create_fig_01():  # SaMD classification
    fig, ax = plt.subplots(figsize=(8, 5))
    classes = [('Class I', 'Low Risk\nGeneral wellness', '#2ca02c'),
               ('Class II', 'Moderate Risk\nAssist diagnosis', '#ff7f0e'),
               ('Class III', 'High Risk\nDrive treatment', '#d62728')]
    for i, (cls, desc, color) in enumerate(classes):
        ax.add_patch(mpatches.FancyBboxPatch((i * 2.5 + 0.5, 0.3), 2, 1.8, boxstyle='round,pad=0.02',
                                              facecolor=color, alpha=0.7, edgecolor='white', linewidth=2))
        ax.text(i * 2.5 + 1.5, 1.5, cls, ha='center', va='center', fontsize=11, fontweight='bold', color='white')
        ax.text(i * 2.5 + 1.5, 0.8, desc, ha='center', va='center', fontsize=9, color='white')
    ax.set_xlim(0, 8)
    ax.set_ylim(-0.1, 2.5)
    ax.axis('off')
    ax.set_title('FDA SaMD Risk Classification', fontweight='bold')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-fig-samd-classification.svg', format='svg')
    plt.close()
    print("Saved: 01-fig-samd-classification.svg")

def create_fig_02():  # Consent models
    dot = graphviz.Digraph('consent', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='8,6!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    dot.node('broad', 'Broad\nConsent', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.node('tiered', 'Tiered\nConsent', fillcolor='#ff7f0e', shape='box')
    dot.node('dynamic', 'Dynamic\nConsent', fillcolor='#1f77b4', fontcolor='white', shape='box')
    dot.node('specific', 'Specific\nConsent', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.edge('broad', 'tiered', label='More control')
    dot.edge('tiered', 'dynamic')
    dot.edge('dynamic', 'specific', label='Most control')
    dot.render(OUTPUT_DIR / '02-fig-consent-models', cleanup=True)
    print("Saved: 02-fig-consent-models.svg")

def create_fig_03():  # Data governance
    for panel, title in [('A', 'Centralized'), ('B', 'Federated')]:
        dot = graphviz.Digraph(f'governance_{panel}', format='svg')
        dot.attr(rankdir='TB', splines='polyline', size='5,4!', ratio='compress')
        dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
        if panel == 'A':
            dot.node('data1', 'Site 1', fillcolor='#aec7e8', shape='box')
            dot.node('data2', 'Site 2', fillcolor='#aec7e8', shape='box')
            dot.node('central', 'Central\nRepository', fillcolor='#d62728', fontcolor='white', shape='box')
            dot.node('model', 'Model', fillcolor='#9467bd', fontcolor='white', shape='box')
            dot.edge('data1', 'central')
            dot.edge('data2', 'central')
            dot.edge('central', 'model')
        else:
            dot.node('site1', 'Site 1\n+ Local Model', fillcolor='#2ca02c', fontcolor='white', shape='box')
            dot.node('site2', 'Site 2\n+ Local Model', fillcolor='#2ca02c', fontcolor='white', shape='box')
            dot.node('agg', 'Aggregate\nWeights', fillcolor='#9467bd', fontcolor='white', shape='box')
            dot.edge('site1', 'agg', label='Weights only')
            dot.edge('site2', 'agg')
        dot.render(OUTPUT_DIR / f'03-{panel}-fig-data-governance', cleanup=True)
        print(f"Saved: 03-{panel}-fig-data-governance.svg")

def create_fig_04():  # Liability chain
    dot = graphviz.Digraph('liability', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='12,3!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    dot.node('dev', 'Model\nDeveloper', fillcolor='#1f77b4', fontcolor='white', shape='box')
    dot.node('vendor', 'Software\nVendor', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.node('provider', 'Healthcare\nProvider', fillcolor='#ff7f0e', shape='box')
    dot.node('clinician', 'Clinician', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('patient', 'Patient\nOutcome', fillcolor='#d62728', fontcolor='white', shape='box')
    dot.edge('dev', 'vendor')
    dot.edge('vendor', 'provider')
    dot.edge('provider', 'clinician')
    dot.edge('clinician', 'patient')
    dot.render(OUTPUT_DIR / '04-fig-liability-chain', cleanup=True)
    print("Saved: 04-fig-liability-chain.svg")

def create_fig_05():  # Dual use governance
    fig, ax = plt.subplots(figsize=(8, 5))
    applications = [('Diagnostic\nimprovement', 1.0, '#2ca02c'),
                    ('Drug\ndiscovery', 0.9, '#2ca02c'),
                    ('Pathogen\ndetection', 0.7, '#ff7f0e'),
                    ('Bioweapon\ndesign', 0.1, '#d62728'),
                    ('Discrimination', 0.05, '#d62728')]
    for i, (app, benefit, color) in enumerate(applications):
        ax.barh(i, benefit, color=color, edgecolor='white', height=0.6)
    ax.set_yticks(range(len(applications)))
    ax.set_yticklabels([a[0] for a in applications], fontsize=9)
    ax.axvline(x=0.5, color='#555555', linestyle='--', alpha=0.7)
    ax.text(0.52, 4.2, 'Benefit threshold', fontsize=9, alpha=0.7)
    ax.set_xlabel('Net Societal Benefit', fontweight='bold')
    ax.set_title('Dual-Use Technology Governance', fontweight='bold')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '05-fig-dual-use-governance.svg', format='svg')
    plt.close()
    print("Saved: 05-fig-dual-use-governance.svg")

if __name__ == '__main__':
    create_fig_01()
    create_fig_02()
    create_fig_03()
    create_fig_04()
    create_fig_05()
    print("All Chapter 26 figures generated.")
