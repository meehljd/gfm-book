#!/usr/bin/env python3
"""
Chapter 23: Uncertainty Quantification Figures
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import graphviz

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_5" / "ch23"
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

def create_fig_01():  # Uncertainty types
    for panel, (title, desc) in [('A', ('Aleatoric', 'Irreducible data noise')),
                                   ('B', ('Epistemic', 'Model knowledge gaps'))]:
        fig, ax = plt.subplots(figsize=(5, 4))
        np.random.seed(42)
        x = np.linspace(0, 10, 100)
        if panel == 'A':
            y = np.sin(x) + np.random.randn(100) * 0.5
            ax.scatter(x, y, c='#1f77b4', alpha=0.5, s=20)
            ax.plot(x, np.sin(x), 'r-', linewidth=2, label='True function')
            ax.fill_between(x, np.sin(x) - 0.5, np.sin(x) + 0.5, alpha=0.2, color='#1f77b4')
        else:
            y = np.sin(x)
            ax.plot(x, y, 'r-', linewidth=2, label='True function')
            ax.plot(x[::10], y[::10], 'ko', markersize=8, label='Training points')
            ax.fill_between(x[30:70], y[30:70] - 1, y[30:70] + 1, alpha=0.3, color='#d62728')
            ax.text(5, -0.5, 'High epistemic\nuncertainty', ha='center', fontsize=9)
        ax.set_xlabel('Input', fontweight='bold')
        ax.set_ylabel('Output', fontweight='bold')
        ax.set_title(f'{panel}. {title} Uncertainty: {desc}', fontweight='bold', loc='left')
        ax.legend(fontsize=8)
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / f'01-{panel}-fig-uncertainty-types.svg', format='svg')
        plt.close()
        print(f"Saved: 01-{panel}-fig-uncertainty-types.svg")

def create_fig_02():  # Calibration diagrams
    np.random.seed(42)
    for panel, desc in [('A', 'Well-calibrated'), ('B', 'Over-confident')]:
        fig, ax = plt.subplots(figsize=(5, 5))
        predicted = np.linspace(0, 1, 10)
        if panel == 'A':
            observed = predicted + np.random.randn(10) * 0.05
        else:
            observed = 0.3 + 0.4 * predicted + np.random.randn(10) * 0.05
        ax.plot([0, 1], [0, 1], 'k--', linewidth=2, label='Perfect')
        ax.plot(predicted, np.clip(observed, 0, 1), 'o-', color='#1f77b4', linewidth=2, markersize=8)
        ax.set_xlabel('Predicted Probability', fontweight='bold')
        ax.set_ylabel('Observed Frequency', fontweight='bold')
        ax.set_title(f'{panel}. {desc} Model', fontweight='bold', loc='left')
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / f'02-{panel}-fig-calibration-diagrams.svg', format='svg')
        plt.close()
        print(f"Saved: 02-{panel}-fig-calibration-diagrams.svg")

def create_fig_03():  # Calibration methods
    methods = [('A', 'Temperature Scaling'), ('B', 'Platt Scaling'), ('C', 'Isotonic Regression')]
    for panel, method in methods:
        dot = graphviz.Digraph(f'calib_{panel}', format='svg')
        dot.attr(rankdir='LR', splines='polyline', size='6,2!', ratio='compress')
        dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
        dot.node('logits', 'Raw\nLogits', fillcolor='#aec7e8', shape='box')
        dot.node('calib', method, fillcolor='#9467bd', fontcolor='white', shape='box')
        dot.node('probs', 'Calibrated\nProbabilities', fillcolor='#98df8a', shape='box')
        dot.edge('logits', 'calib')
        dot.edge('calib', 'probs')
        dot.render(OUTPUT_DIR / f'03-{panel}-fig-calibration-methods', cleanup=True)
        print(f"Saved: 03-{panel}-fig-calibration-methods.svg")

def create_fig_04():  # UQ methods overview
    fig, ax = plt.subplots(figsize=(10, 5))
    methods = [('Ensemble', 'Multiple models', '#1f77b4'),
               ('MC Dropout', 'Stochastic inference', '#2ca02c'),
               ('Deep Ensemble', 'Diverse training', '#ff7f0e'),
               ('Bayesian NN', 'Weight uncertainty', '#9467bd'),
               ('Conformal', 'Distribution-free', '#d62728')]
    for i, (name, desc, color) in enumerate(methods):
        ax.add_patch(mpatches.FancyBboxPatch((i * 1.9 + 0.1, 0.3), 1.7, 1.8,
                                              boxstyle='round,pad=0.02',
                                              facecolor=color, alpha=0.7, edgecolor='white', linewidth=2))
        ax.text(i * 1.9 + 0.95, 1.5, name, ha='center', va='center', fontsize=10, fontweight='bold', color='white')
        ax.text(i * 1.9 + 0.95, 0.8, desc, ha='center', va='center', fontsize=8, color='white')
    ax.set_xlim(-0.2, 9.8)
    ax.set_ylim(-0.1, 2.5)
    ax.axis('off')
    ax.set_title('Uncertainty Quantification Methods', fontweight='bold')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-fig-uq-methods.svg', format='svg')
    plt.close()
    print("Saved: 04-fig-uq-methods.svg")

def create_fig_05():  # Conformal prediction
    dot = graphviz.Digraph('conformal', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='10,3!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')
    dot.node('calib', 'Calibration\nSet', fillcolor='#aec7e8', shape='box')
    dot.node('scores', 'Conformity\nScores', fillcolor='#98df8a', shape='box')
    dot.node('quantile', 'Quantile\nThreshold', fillcolor='#ffbb78', shape='box')
    dot.node('test', 'Test\nPrediction', fillcolor='#c5b0d5', shape='box')
    dot.node('interval', 'Prediction\nSet', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.edge('calib', 'scores')
    dot.edge('scores', 'quantile')
    dot.edge('quantile', 'interval')
    dot.edge('test', 'interval')
    dot.render(OUTPUT_DIR / '05-fig-conformal-prediction', cleanup=True)
    print("Saved: 05-fig-conformal-prediction.svg")

def create_fig_06():  # OOD detection
    np.random.seed(42)
    for panel, title in [('A', 'In-Distribution'), ('B', 'Near-OOD'), ('C', 'Far-OOD')]:
        fig, ax = plt.subplots(figsize=(4, 4))
        if panel == 'A':
            x = np.random.randn(100)
            y = np.random.randn(100)
        elif panel == 'B':
            x = np.random.randn(100) + 3
            y = np.random.randn(100) + 1
        else:
            x = np.random.randn(100) + 6
            y = np.random.randn(100) + 4
        color = '#2ca02c' if panel == 'A' else '#ff7f0e' if panel == 'B' else '#d62728'
        ax.scatter(x, y, c=color, s=30, alpha=0.6)
        if panel != 'A':
            ax.scatter(np.random.randn(50), np.random.randn(50), c='#1f77b4', s=30, alpha=0.3, label='Training')
            ax.legend(fontsize=8)
        ax.set_xlabel('Feature 1', fontweight='bold')
        ax.set_ylabel('Feature 2', fontweight='bold')
        ax.set_title(f'{panel}. {title}', fontweight='bold', loc='left')
        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / f'06-{panel}-fig-ood-detection.svg', format='svg')
        plt.close()
        print(f"Saved: 06-{panel}-fig-ood-detection.svg")

def create_fig_07():  # Selective prediction
    fig, ax = plt.subplots(figsize=(6, 4))
    np.random.seed(42)
    coverage = np.linspace(0.5, 1, 20)
    accuracy = 0.98 - 0.3 * (coverage - 0.5) ** 2 + np.random.randn(20) * 0.01
    ax.plot(coverage, accuracy, 'o-', color='#1f77b4', linewidth=2, markersize=6)
    ax.axhline(y=0.9, color='#d62728', linestyle='--', alpha=0.7)
    ax.text(0.55, 0.91, 'Clinical threshold', fontsize=9, color='#d62728')
    ax.set_xlabel('Coverage (% predictions made)', fontweight='bold')
    ax.set_ylabel('Accuracy', fontweight='bold')
    ax.set_title('Selective Prediction: Accuracy vs Coverage', fontweight='bold')
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '07-fig-selective-prediction.svg', format='svg')
    plt.close()
    print("Saved: 07-fig-selective-prediction.svg")

if __name__ == '__main__':
    create_fig_01()
    create_fig_02()
    create_fig_03()
    create_fig_04()
    create_fig_05()
    create_fig_06()
    create_fig_07()
    print("All Chapter 23 figures generated.")
