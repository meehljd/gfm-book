#!/usr/bin/env python3
"""Chapter 27: Clinical Risk Prediction Figures"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import graphviz

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_6" / "ch27"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
plt.rcParams.update({'font.family': 'sans-serif', 'font.sans-serif': ['Arial', 'DejaVu Sans'], 'font.size': 10,
    'axes.titlesize': 11, 'axes.titleweight': 'bold', 'figure.dpi': 150, 'savefig.dpi': 300,
    'savefig.bbox': 'tight', 'axes.spines.top': False, 'axes.spines.right': False})

def create_fig_01():  # Feature integration - 3 panels
    panels = [
        ('A', 'DNA Foundation Models', ['Regulatory\nvariants', 'Promoter\neffects', 'Splicing\nimpact'], '#1f77b4'),
        ('B', 'Expression Foundation Models', ['Cell state\nembeddings', 'Pathway\nactivity', 'Expression\npatterns'], '#2ca02c'),
        ('C', 'Protein Foundation Models', ['Pathogenicity\nscores', 'Structural\neffects', 'Stability\nchanges'], '#ff7f0e'),
    ]
    for panel_id, title, features, color in panels:
        dot = graphviz.Digraph(f'integration_{panel_id}', format='svg')
        dot.attr(rankdir='TB', splines='polyline', size='6,4!', ratio='compress')
        dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
        dot.node('fm', title.replace(' ', '\n'), fillcolor=color, fontcolor='white', shape='box')
        for i, feat in enumerate(features):
            dot.node(f'f{i}', feat, fillcolor='#aec7e8', shape='box')
            dot.edge('fm', f'f{i}')
        dot.node('risk', 'Risk\nScore', fillcolor='#9467bd', fontcolor='white', shape='box')
        for i in range(len(features)):
            dot.edge(f'f{i}', 'risk')
        dot.render(OUTPUT_DIR / f'01-{panel_id}-fig-feature-integration', cleanup=True)
        print(f"Saved: 01-{panel_id}-fig-feature-integration.svg")

def create_fig_02():  # Temporal modeling - 3 panels
    # Panel A: Static vs dynamic risk
    fig, ax = plt.subplots(figsize=(6, 4))
    ages = np.linspace(30, 80, 100)
    static = np.ones_like(ages) * 0.35
    dynamic = 0.1 + 0.3 * (1 - np.exp(-0.05 * (ages - 30))) + 0.1 * np.sin(ages / 10)
    ax.plot(ages, static, '--', color='#d62728', linewidth=2, label='Static (PRS only)')
    ax.plot(ages, dynamic, '-', color='#2ca02c', linewidth=2, label='Dynamic (FM-enhanced)')
    ax.fill_between(ages, dynamic - 0.05, dynamic + 0.05, alpha=0.2, color='#2ca02c')
    ax.set_xlabel('Age (years)', fontweight='bold')
    ax.set_ylabel('Risk Probability', fontweight='bold')
    ax.set_title('A. Static vs Dynamic Risk', fontweight='bold', loc='left')
    ax.legend(fontsize=9)
    ax.set_ylim(0, 0.7)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '02-A-fig-temporal-modeling.svg', format='svg')
    plt.close()
    print("Saved: 02-A-fig-temporal-modeling.svg")

    # Panel B: Longitudinal trajectories
    fig, ax = plt.subplots(figsize=(6, 4))
    np.random.seed(42)
    time = np.arange(0, 10, 0.5)
    for i, (color, style) in enumerate([('#d62728', '-'), ('#ff7f0e', '--'), ('#2ca02c', ':')]):
        base = 0.2 + i * 0.15
        trajectory = base + np.cumsum(np.random.randn(len(time)) * 0.02)
        ax.plot(time, trajectory, style, color=color, linewidth=2, label=f'Patient {i+1}')
        ax.scatter([time[-1]], [trajectory[-1]], color=color, s=80, zorder=5)
    ax.set_xlabel('Years of Follow-up', fontweight='bold')
    ax.set_ylabel('Cumulative Risk', fontweight='bold')
    ax.set_title('B. Longitudinal Trajectories', fontweight='bold', loc='left')
    ax.legend(fontsize=9)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '02-B-fig-temporal-modeling.svg', format='svg')
    plt.close()
    print("Saved: 02-B-fig-temporal-modeling.svg")

    # Panel C: Bayesian updating
    fig, ax = plt.subplots(figsize=(6, 4))
    updates = ['Prior', 'Lab 1', 'Lab 2', 'Imaging', 'FM Score']
    means = [0.3, 0.35, 0.40, 0.45, 0.55]
    stds = [0.15, 0.12, 0.10, 0.08, 0.05]
    for i, (u, m, s) in enumerate(zip(updates, means, stds)):
        x = np.linspace(0, 1, 100)
        y = np.exp(-0.5 * ((x - m) / s) ** 2)
        y = y / max(y) + i * 1.2
        ax.fill_between(x, i * 1.2, y, alpha=0.4, color=plt.cm.viridis(i / len(updates)))
        ax.plot(x, y, color=plt.cm.viridis(i / len(updates)), linewidth=2)
    ax.set_yticks([i * 1.2 + 0.5 for i in range(len(updates))])
    ax.set_yticklabels(updates)
    ax.set_xlabel('Risk Probability', fontweight='bold')
    ax.set_title('C. Bayesian Updating', fontweight='bold', loc='left')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '02-C-fig-temporal-modeling.svg', format='svg')
    plt.close()
    print("Saved: 02-C-fig-temporal-modeling.svg")

def create_fig_03():  # Validation hierarchy
    dot = graphviz.Digraph('validation', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='8,8!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    levels = [
        ('internal', 'Internal\nHoldout', '#aec7e8'),
        ('external', 'External\nValidation', '#98df8a'),
        ('temporal', 'Temporal\nValidation', '#ffbb78'),
        ('prospective', 'Prospective\nTrial', '#2ca02c'),
    ]
    for i, (nid, label, color) in enumerate(levels):
        dot.node(nid, label, fillcolor=color, shape='box', fontcolor='white' if i == 3 else 'black')
    for i in range(len(levels) - 1):
        dot.edge(levels[i][0], levels[i + 1][0], label='Higher\nevidence' if i == 0 else '')
    dot.render(OUTPUT_DIR / '03-fig-validation-hierarchy', cleanup=True)
    print("Saved: 03-fig-validation-hierarchy.svg")

def create_fig_04():  # Clinical uncertainty
    fig, ax = plt.subplots(figsize=(8, 5))
    categories = ['Low Risk\n(Reassure)', 'Intermediate\n(Monitor)', 'High Risk\n(Intervene)']
    widths = [0.3, 0.35, 0.35]
    starts = [0, 0.3, 0.65]
    colors = ['#2ca02c', '#ff7f0e', '#d62728']
    for cat, w, s, c in zip(categories, widths, starts, colors):
        ax.barh(0, w, left=s, color=c, edgecolor='white', height=0.4, alpha=0.7)
        ax.text(s + w / 2, 0, cat, ha='center', va='center', fontsize=9, fontweight='bold')
    # Add confidence intervals
    for x, w in [(0.15, 0.08), (0.475, 0.12), (0.825, 0.1)]:
        ax.plot([x - w, x + w], [0.3, 0.3], 'k-', linewidth=2)
        ax.plot([x - w, x - w], [0.28, 0.32], 'k-', linewidth=2)
        ax.plot([x + w, x + w], [0.28, 0.32], 'k-', linewidth=2)
        ax.scatter([x], [0.3], color='black', s=50, zorder=5)
    ax.text(0.5, 0.45, 'Prediction with 95% CI', ha='center', fontsize=10)
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.3, 0.6)
    ax.axis('off')
    ax.set_title('Communicating Uncertainty in Clinical Risk', fontweight='bold')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-fig-clinical-uncertainty.svg', format='svg')
    plt.close()
    print("Saved: 04-fig-clinical-uncertainty.svg")

def create_fig_05():  # Fairness assessment - 4 panels
    # Panel A: Ancestry-stratified performance
    fig, ax = plt.subplots(figsize=(6, 4))
    ancestries = ['European', 'African', 'East Asian', 'Hispanic', 'South Asian']
    aucs = [0.85, 0.72, 0.78, 0.75, 0.73]
    colors = ['#2ca02c' if a > 0.80 else '#ff7f0e' if a > 0.75 else '#d62728' for a in aucs]
    bars = ax.barh(ancestries, aucs, color=colors, edgecolor='white')
    ax.axvline(x=0.80, color='#555555', linestyle='--', alpha=0.7)
    ax.text(0.81, 4.5, 'Threshold', fontsize=8)
    ax.set_xlabel('auROC', fontweight='bold')
    ax.set_title('A. Ancestry-Stratified Performance', fontweight='bold', loc='left')
    ax.set_xlim(0.5, 0.95)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '05-A-fig-fairness-assessment.svg', format='svg')
    plt.close()
    print("Saved: 05-A-fig-fairness-assessment.svg")

    # Panel B: Calibration by group
    fig, ax = plt.subplots(figsize=(6, 4))
    pred = np.linspace(0, 1, 10)
    ax.plot([0, 1], [0, 1], 'k--', alpha=0.5, label='Perfect calibration')
    ax.plot(pred, pred * 0.95, 'o-', color='#2ca02c', label='Majority group')
    ax.plot(pred, pred * 1.15, 's-', color='#d62728', label='Underrepresented')
    ax.fill_between(pred, pred * 0.9, pred * 1.2, alpha=0.1, color='#d62728')
    ax.set_xlabel('Predicted Probability', fontweight='bold')
    ax.set_ylabel('Observed Frequency', fontweight='bold')
    ax.set_title('B. Calibration by Group', fontweight='bold', loc='left')
    ax.legend(fontsize=8)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1.1)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '05-B-fig-fairness-assessment.svg', format='svg')
    plt.close()
    print("Saved: 05-B-fig-fairness-assessment.svg")

    # Panel C: Bias accumulation
    dot = graphviz.Digraph('bias', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='10,3!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    stages = [('data', 'Training\nData'), ('model', 'Model\nBias'), ('deploy', 'Deployment\nBias'), ('outcome', 'Outcome\nDisparity')]
    for i, (nid, label) in enumerate(stages):
        color = '#d62728' if i > 0 else '#ff7f0e'
        dot.node(nid, label, fillcolor=color, fontcolor='white', shape='box')
    for i in range(len(stages) - 1):
        dot.edge(stages[i][0], stages[i + 1][0], label='Amplifies' if i == 1 else '')
    dot.render(OUTPUT_DIR / '05-C-fig-fairness-assessment', cleanup=True)
    print("Saved: 05-C-fig-fairness-assessment.svg")

    # Panel D: Mitigation strategies
    fig, ax = plt.subplots(figsize=(6, 4))
    strategies = ['Reweighting', 'Data\naugmentation', 'Adversarial\ndebiasing', 'Calibration\nadjustment']
    effectiveness = [0.6, 0.7, 0.75, 0.65]
    colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd']
    ax.bar(strategies, effectiveness, color=colors, edgecolor='white')
    ax.set_ylabel('Bias Reduction', fontweight='bold')
    ax.set_title('D. Mitigation Strategies', fontweight='bold', loc='left')
    ax.set_ylim(0, 1)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '05-D-fig-fairness-assessment.svg', format='svg')
    plt.close()
    print("Saved: 05-D-fig-fairness-assessment.svg")

def create_fig_06():  # Clinical workflow
    dot = graphviz.Digraph('workflow', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='14,4!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    steps = [
        ('patient', 'Patient\nData', '#aec7e8'),
        ('ehr', 'EHR\nIntegration', '#98df8a'),
        ('fm', 'Foundation\nModel', '#9467bd'),
        ('risk', 'Risk\nScore', '#ffbb78'),
        ('decision', 'Clinical\nDecision', '#2ca02c'),
    ]
    for nid, label, color in steps:
        fc = 'white' if nid in ['fm', 'decision'] else 'black'
        dot.node(nid, label, fillcolor=color, fontcolor=fc, shape='box')
    for i in range(len(steps) - 1):
        dot.edge(steps[i][0], steps[i + 1][0])
    dot.render(OUTPUT_DIR / '06-fig-clinical-workflow', cleanup=True)
    print("Saved: 06-fig-clinical-workflow.svg")

def create_fig_07():  # Cardio case study
    dot = graphviz.Digraph('cardio', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='10,8!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    with dot.subgraph(name='cluster_inputs') as c:
        c.attr(label='Inputs', style='rounded', color='#555555')
        c.node('prs', 'PRS\n(Traditional)', fillcolor='#aec7e8', shape='box')
        c.node('dna', 'DNA-FM\nScores', fillcolor='#1f77b4', fontcolor='white', shape='box')
        c.node('clinical', 'Clinical\nFeatures', fillcolor='#98df8a', shape='box')
    dot.node('integrate', 'Integration\nModel', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('risk', 'CVD Risk\nScore', fillcolor='#ff7f0e', shape='box')
    with dot.subgraph(name='cluster_outputs') as c:
        c.attr(label='Actions', style='rounded', color='#555555')
        c.node('screen', 'Enhanced\nScreening', fillcolor='#2ca02c', fontcolor='white', shape='box')
        c.node('therapy', 'Preventive\nTherapy', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.edge('prs', 'integrate')
    dot.edge('dna', 'integrate')
    dot.edge('clinical', 'integrate')
    dot.edge('integrate', 'risk')
    dot.edge('risk', 'screen')
    dot.edge('risk', 'therapy')
    dot.render(OUTPUT_DIR / '07-fig-cardio-case-study', cleanup=True)
    print("Saved: 07-fig-cardio-case-study.svg")

if __name__ == '__main__':
    create_fig_01()
    create_fig_02()
    create_fig_03()
    create_fig_04()
    create_fig_05()
    create_fig_06()
    create_fig_07()
    print("All Chapter 27 figures generated.")
