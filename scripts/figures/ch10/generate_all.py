#!/usr/bin/env python3
"""
Chapter 10: Adaptation Strategies Figures
Generates figures for this chapter.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import graphviz

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_2" / "ch10"
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

# Fig 01: LoRA Architecture
def create_fig_01():
    fig, ax = plt.subplots(figsize=(6, 5))

    # Original weight matrix
    ax.add_patch(mpatches.FancyBboxPatch((1, 2), 2, 2.5,
                                          boxstyle='round,pad=0.02',
                                          facecolor='#1f77b4', alpha=0.5,
                                          edgecolor='#1f77b4', linewidth=2))
    ax.text(2, 3.25, 'W\n(frozen)', ha='center', va='center', fontsize=11, fontweight='bold')

    # Low-rank matrices
    ax.add_patch(mpatches.FancyBboxPatch((4, 2.5), 0.5, 1.5,
                                          boxstyle='round,pad=0.02',
                                          facecolor='#d62728', alpha=0.7,
                                          edgecolor='#d62728', linewidth=2))
    ax.text(4.25, 3.25, 'A\n(r×d)', ha='center', va='center', fontsize=9, color='white')

    ax.add_patch(mpatches.FancyBboxPatch((5, 2.5), 1.5, 0.5,
                                          boxstyle='round,pad=0.02',
                                          facecolor='#2ca02c', alpha=0.7,
                                          edgecolor='#2ca02c', linewidth=2))
    ax.text(5.75, 2.75, 'B (d×r)', ha='center', va='center', fontsize=9, color='white')

    # Plus sign
    ax.text(3.5, 3.25, '+', ha='center', va='center', fontsize=20, fontweight='bold')

    # LoRA update
    ax.annotate('', xy=(6, 3.25), xytext=(4.6, 3.25),
                arrowprops=dict(arrowstyle='->', color='#555555', lw=1.5))
    ax.text(5.3, 3.6, 'ΔW = BA', ha='center', fontsize=10, fontweight='bold')

    # Legend
    ax.text(3.5, 1.5, 'LoRA: W + ΔW = W + BA', ha='center', fontsize=11, fontweight='bold')
    ax.text(3.5, 1.0, 'Train only A, B (r << d)', ha='center', fontsize=10, style='italic')
    ax.text(3.5, 0.5, 'Reduces trainable params by 100-1000x', ha='center', fontsize=9)

    ax.set_xlim(0, 7)
    ax.set_ylim(0, 5)
    ax.axis('off')
    ax.set_title('Low-Rank Adaptation (LoRA)', fontweight='bold')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-fig-lora-architecture.svg', format='svg')
    plt.close()
    print("Saved: 01-fig-lora-architecture.svg")

# Fig 02 A-B: Layer Probing
def create_fig_02():
    for panel, model_type in [('A', 'Encoder'), ('B', 'Decoder')]:
        fig, ax = plt.subplots(figsize=(6, 4))

        np.random.seed(42 if panel == 'A' else 43)
        layers = np.arange(1, 13)

        if model_type == 'Encoder':
            # Encoder: middle layers often best
            performance = 0.6 + 0.3 * np.sin((layers - 6) * np.pi / 12) + np.random.randn(12) * 0.03
        else:
            # Decoder: later layers often better
            performance = 0.5 + 0.35 * (layers / 12) + np.random.randn(12) * 0.03

        ax.plot(layers, performance, 'o-', color='#1f77b4' if panel == 'A' else '#d62728',
                linewidth=2, markersize=8)

        best_layer = layers[np.argmax(performance)]
        ax.axvline(x=best_layer, color='#2ca02c', linestyle='--', linewidth=1.5, alpha=0.7)
        ax.text(best_layer + 0.3, max(performance) - 0.05, f'Best: L{best_layer}', fontsize=9, color='#2ca02c')

        ax.set_xlabel('Layer Number', fontweight='bold')
        ax.set_ylabel('Probing Performance', fontweight='bold')
        ax.set_title(f'{panel}. {model_type} Model Layer-wise Performance', fontweight='bold', loc='left')

        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / f'02-{panel}-fig-layer-probing-decoder.svg', format='svg')
        plt.close()
        print(f"Saved: 02-{panel}-fig-layer-probing-decoder.svg")

# Fig 03: Adaptation Decision Tree
def create_fig_03():
    dot = graphviz.Digraph('decision', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='8,10!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('start', 'How much\ndownstream data?', fillcolor='#fff8dc', shape='diamond')
    dot.node('little', '< 1000\nsamples', fillcolor='#aec7e8', shape='box')
    dot.node('medium', '1000-10000\nsamples', fillcolor='#98df8a', shape='box')
    dot.node('lots', '> 10000\nsamples', fillcolor='#ffbb78', shape='box')

    dot.node('probe', 'Linear\nProbing', fillcolor='#1f77b4', fontcolor='white', shape='box')
    dot.node('lora', 'LoRA /\nAdapter', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.node('finetune', 'Full\nFine-tuning', fillcolor='#d62728', fontcolor='white', shape='box')

    dot.edge('start', 'little')
    dot.edge('start', 'medium')
    dot.edge('start', 'lots')
    dot.edge('little', 'probe')
    dot.edge('medium', 'lora')
    dot.edge('lots', 'finetune')

    dot.render(OUTPUT_DIR / '03-fig-adaptation-decision-tree', cleanup=True)
    print("Saved: 03-fig-adaptation-decision-tree.svg")

# Fig 04 A-C: Domain Shift Detection
def create_fig_04():
    panels = [
        ('A', 'Embedding Space', 'scatter'),
        ('B', 'Calibration', 'line'),
        ('C', 'Performance Degradation', 'bar'),
    ]

    for panel_id, title, plot_type in panels:
        fig, ax = plt.subplots(figsize=(5, 4))
        np.random.seed(42)

        if plot_type == 'scatter':
            # Embedding clustering
            train_x = np.random.normal(0, 0.5, 50)
            train_y = np.random.normal(0, 0.5, 50)
            test_x = np.random.normal(1.5, 0.5, 50)
            test_y = np.random.normal(1, 0.5, 50)
            ax.scatter(train_x, train_y, c='#1f77b4', s=30, alpha=0.6, label='Training')
            ax.scatter(test_x, test_y, c='#d62728', s=30, alpha=0.6, label='Test (shifted)')
            ax.legend(fontsize=8)

        elif plot_type == 'line':
            # Calibration plot
            predicted = np.linspace(0, 1, 10)
            observed_good = predicted + np.random.randn(10) * 0.05
            observed_bad = 0.3 + 0.4 * predicted + np.random.randn(10) * 0.08
            ax.plot([0, 1], [0, 1], 'k--', label='Perfect calibration')
            ax.plot(predicted, np.clip(observed_good, 0, 1), 'o-', color='#2ca02c', label='In-domain')
            ax.plot(predicted, np.clip(observed_bad, 0, 1), 's-', color='#d62728', label='Out-of-domain')
            ax.legend(fontsize=8)
            ax.set_xlabel('Predicted Probability')
            ax.set_ylabel('Observed Frequency')

        else:  # bar
            datasets = ['Train', 'Val\n(ID)', 'Test\n(Near)', 'Test\n(Far)']
            performance = [0.92, 0.88, 0.75, 0.55]
            colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#d62728']
            ax.bar(datasets, performance, color=colors, edgecolor='white')
            ax.set_ylabel('Performance')
            ax.axhline(y=0.7, color='#555555', linestyle='--', alpha=0.5)

        ax.set_title(f'{panel_id}. {title}', fontweight='bold', loc='left')

        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / f'04-{panel_id}-fig-domain-shift-detection.svg', format='svg')
        plt.close()
        print(f"Saved: 04-{panel_id}-fig-domain-shift-detection.svg")

# Fig 05 A-D: Validation Pitfalls
def create_fig_05():
    panels = ['A', 'B', 'C', 'D']
    titles = ['Data Overlap', 'Temporal Leakage', 'Baseline Issues', 'Stratified Performance']

    for panel_id, title in zip(panels, titles):
        fig, ax = plt.subplots(figsize=(5, 3))

        ax.text(0.5, 0.5, f'Pitfall: {title}', ha='center', va='center', fontsize=12,
                transform=ax.transAxes, fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#fee0d2', edgecolor='#d62728'))

        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        ax.set_title(f'{panel_id}. {title}', fontweight='bold', loc='left')

        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / f'05-{panel_id}-fig-validation-pitfalls.svg', format='svg')
        plt.close()
        print(f"Saved: 05-{panel_id}-fig-validation-pitfalls.svg")

if __name__ == '__main__':
    create_fig_01()
    create_fig_02()
    create_fig_03()
    create_fig_04()
    create_fig_05()
    print("All Chapter 10 figures generated.")
