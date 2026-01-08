#!/usr/bin/env python3
"""
Chapter 11: Benchmarks and Evaluation Figures
Generates all 15 figures for this chapter.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import graphviz

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_2" / "ch11"
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

# Fig 01: Benchmark Landscape
def create_fig_01():
    fig, ax = plt.subplots(figsize=(10, 6))

    # Categories and benchmarks
    categories = ['Protein Function', 'Protein Structure', 'DNA Regulatory',
                  'Variant Effect', 'Trait/PGS']
    benchmarks = [
        ['TAPE', 'FLIP', 'ProteinGym'],
        ['CASP', 'AlphaFold', 'ESMFold'],
        ['ENCODE', 'BEND', 'Genomic Benchmarks'],
        ['ClinVar', 'CAGI', 'DMS/MaveDB'],
        ['TraitGym', 'EmbedGEM', 'UK Biobank']
    ]

    colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#d62728', '#9467bd']

    for i, (cat, bmarks) in enumerate(zip(categories, benchmarks)):
        y = len(categories) - i - 1
        ax.text(0, y, cat, ha='left', va='center', fontsize=10, fontweight='bold')
        for j, bmark in enumerate(bmarks):
            ax.add_patch(mpatches.FancyBboxPatch((1.5 + j*1.8, y - 0.3), 1.6, 0.6,
                                                  boxstyle='round,pad=0.02',
                                                  facecolor=colors[i], alpha=0.6,
                                                  edgecolor='white', linewidth=1))
            ax.text(2.3 + j*1.8, y, bmark, ha='center', va='center',
                    fontsize=9, color='white', fontweight='bold')

    ax.set_xlim(-0.5, 7.5)
    ax.set_ylim(-0.5, len(categories))
    ax.axis('off')
    ax.set_title('Genomic AI Benchmark Landscape', fontweight='bold')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '01-fig-benchmark-landscape.svg', format='svg')
    plt.close()
    print("Saved: 01-fig-benchmark-landscape.svg")

# Fig 02: Leakage Pathways
def create_fig_02():
    dot = graphviz.Digraph('leakage', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='8,8!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='10', style='filled,rounded', penwidth='1.5')

    # Main pipeline nodes
    dot.node('pretrain', 'Pretraining\nData', fillcolor='#aec7e8', shape='box')
    dot.node('finetune', 'Fine-tuning\nData', fillcolor='#98df8a', shape='box')
    dot.node('benchmark', 'Benchmark\nEvaluation', fillcolor='#ffbb78', shape='box')

    # Leakage types
    dot.node('direct', 'Direct\nOverlap', fillcolor='#ff9896', shape='box')
    dot.node('homology', 'Homology\nLeakage', fillcolor='#ff9896', shape='box')
    dot.node('label', 'Label\nCircularity', fillcolor='#ff9896', shape='box')
    dot.node('resource', 'Resource\nSharing', fillcolor='#ff9896', shape='box')

    # Legitimate path (blue)
    dot.edge('pretrain', 'finetune', color='#1f77b4', penwidth='2')
    dot.edge('finetune', 'benchmark', color='#1f77b4', penwidth='2')

    # Leakage paths (red dashed)
    dot.edge('pretrain', 'benchmark', style='dashed', color='#d62728', label='direct')
    dot.edge('pretrain', 'homology', style='dashed', color='#d62728')
    dot.edge('homology', 'benchmark', style='dashed', color='#d62728')
    dot.edge('label', 'benchmark', style='dashed', color='#d62728')
    dot.edge('resource', 'finetune', style='dashed', color='#d62728')
    dot.edge('resource', 'benchmark', style='dashed', color='#d62728')

    dot.render(OUTPUT_DIR / '02-fig-leakage-pathways', cleanup=True)
    print("Saved: 02-fig-leakage-pathways.svg")

# Fig 03 A-B: Benchmark Saturation and Staleness
def create_fig_03():
    # Panel A: Saturation over time
    fig, ax = plt.subplots(figsize=(6, 4))
    np.random.seed(42)

    years = np.arange(2015, 2026)
    performance = 0.65 + 0.3 * (1 - np.exp(-(years - 2015) / 4)) + np.random.randn(len(years)) * 0.02
    performance = np.clip(performance, 0, 0.98)

    ax.plot(years, performance, 'o-', color='#1f77b4', linewidth=2, markersize=8)
    ax.axhline(y=0.95, color='#d62728', linestyle='--', linewidth=1.5, alpha=0.7)
    ax.fill_between(years, 0.93, 1.0, alpha=0.2, color='#d62728')
    ax.text(2024, 0.96, 'Saturation\nZone', fontsize=9, color='#d62728', ha='right')

    ax.set_xlabel('Year', fontweight='bold')
    ax.set_ylabel('Benchmark Performance', fontweight='bold')
    ax.set_title('A. Performance Saturation Over Time', fontweight='bold', loc='left')
    ax.set_ylim(0.5, 1.0)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '03-A-fig-benchmark-saturation.svg', format='svg')
    plt.close()
    print("Saved: 03-A-fig-benchmark-saturation.svg")

    # Panel B: Staleness
    fig, ax = plt.subplots(figsize=(6, 4))

    benchmarks = ['TAPE\n(2019)', 'Genomic\nBenchmarks\n(2023)', 'BEND\n(2024)']
    ages = [2026 - 2019, 2026 - 2023, 2026 - 2024]
    colors = ['#d62728', '#ff7f0e', '#2ca02c']

    bars = ax.bar(benchmarks, ages, color=colors, edgecolor='white')
    ax.axhline(y=3, color='#555555', linestyle='--', linewidth=1, alpha=0.5)
    ax.text(2.5, 3.2, 'Staleness threshold', fontsize=9, alpha=0.7)

    ax.set_ylabel('Benchmark Age (years)', fontweight='bold')
    ax.set_title('B. Benchmark Staleness', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '03-B-fig-benchmark-saturation.svg', format='svg')
    plt.close()
    print("Saved: 03-B-fig-benchmark-saturation.svg")

# Fig 04: Proxy-Target Gap
def create_fig_04():
    fig, ax = plt.subplots(figsize=(8, 5))

    # Proxy boxes (left)
    proxies = ['ClinVar\nLabels', 'Held-out\nauROC', 'DMS\nCorrelation', 'Expression\nPrediction']
    targets = ['Clinical\nImpact', 'Deployment\nDiscrimination', 'Protein\nFunction', 'Regulatory\nUnderstanding']

    for i, (proxy, target) in enumerate(zip(proxies, targets)):
        y = len(proxies) - i - 1
        # Proxy box
        ax.add_patch(mpatches.FancyBboxPatch((0.5, y - 0.3), 1.5, 0.6,
                                              boxstyle='round,pad=0.02',
                                              facecolor='#aec7e8', alpha=0.8,
                                              edgecolor='#1f77b4', linewidth=2))
        ax.text(1.25, y, proxy, ha='center', va='center', fontsize=9, fontweight='bold')

        # Target box
        ax.add_patch(mpatches.FancyBboxPatch((4.5, y - 0.3), 1.5, 0.6,
                                              boxstyle='round,pad=0.02',
                                              facecolor='#98df8a', alpha=0.8,
                                              edgecolor='#2ca02c', linewidth=2))
        ax.text(5.25, y, target, ha='center', va='center', fontsize=9, fontweight='bold')

        # Gap arrow
        ax.annotate('', xy=(4.4, y), xytext=(2.1, y),
                    arrowprops=dict(arrowstyle='->', color='#d62728', lw=2))

    ax.text(3.25, 4.2, 'PROXY-TARGET GAP', ha='center', fontsize=12, fontweight='bold', color='#d62728')
    ax.text(1.25, -0.8, 'What benchmarks\nmeasure', ha='center', fontsize=10, style='italic')
    ax.text(5.25, -0.8, 'What we want\nto know', ha='center', fontsize=10, style='italic')

    ax.set_xlim(0, 7)
    ax.set_ylim(-1.5, 5)
    ax.axis('off')
    ax.set_title('The Proxy-Target Gap in Genomic AI Evaluation', fontweight='bold')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-fig-proxy-target-gap.svg', format='svg')
    plt.close()
    print("Saved: 04-fig-proxy-target-gap.svg")

# Fig 05: Cross-Population Performance
def create_fig_05():
    fig, ax = plt.subplots(figsize=(8, 5))

    populations = ['European\n(reference)', 'East Asian', 'South Asian', 'Hispanic', 'African']
    performance = [1.0, 0.85, 0.78, 0.72, 0.55]
    colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#9467bd', '#d62728']

    bars = ax.bar(populations, performance, color=colors, edgecolor='white', width=0.6)

    # Add performance labels
    for bar, perf in zip(bars, performance):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                f'{perf:.0%}', ha='center', fontsize=9, fontweight='bold')

    ax.axhline(y=1.0, color='#1f77b4', linestyle='--', linewidth=1, alpha=0.5)
    ax.set_ylabel('Relative Performance', fontweight='bold')
    ax.set_title('Cross-Population Performance Degradation', fontweight='bold')
    ax.set_ylim(0, 1.15)

    # Inset for training data composition
    ax_inset = ax.inset_axes([0.65, 0.55, 0.3, 0.35])
    sizes = [78, 10, 5, 5, 2]
    ax_inset.pie(sizes, colors=colors, autopct='%1.0f%%', textprops={'fontsize': 7})
    ax_inset.set_title('Training Data', fontsize=8, fontweight='bold')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '05-fig-cross-population-performance.svg', format='svg')
    plt.close()
    print("Saved: 05-fig-cross-population-performance.svg")

# Fig 06 A-C: Random Splits Fail
def create_fig_06():
    panels = [
        ('A', 'Images: Independent Samples', 'Each sample independent', '#2ca02c'),
        ('B', 'Proteins: Related by Evolution', 'Homologs in train/test', '#ff7f0e'),
        ('C', 'Variants: Multiple Dependencies', 'Gene, family, ancestry', '#d62728'),
    ]

    for panel_id, title, note, color in panels:
        fig, ax = plt.subplots(figsize=(5, 4))
        np.random.seed(42 + ord(panel_id))

        if panel_id == 'A':
            # Random scattered points (independent)
            x = np.random.randn(50)
            y = np.random.randn(50)
            ax.scatter(x, y, c=color, s=40, alpha=0.6)
        elif panel_id == 'B':
            # Clustered points (related)
            for i in range(5):
                center_x, center_y = np.random.randn(2)
                cluster_x = center_x + np.random.randn(10) * 0.3
                cluster_y = center_y + np.random.randn(10) * 0.3
                ax.scatter(cluster_x, cluster_y, c=color, s=40, alpha=0.6)
                # Draw cluster boundary
                circle = plt.Circle((center_x, center_y), 0.6, fill=False,
                                    linestyle='--', color='#555555', alpha=0.5)
                ax.add_patch(circle)
        else:
            # Hierarchical clusters (multiple dependencies)
            for i in range(3):
                center_x = i * 2 - 2
                for j in range(3):
                    sub_x = center_x + np.random.randn(5) * 0.2
                    sub_y = j - 1 + np.random.randn(5) * 0.2
                    ax.scatter(sub_x, sub_y, c=color, s=40, alpha=0.6)

        ax.text(0.5, 0.05, note, ha='center', transform=ax.transAxes,
                fontsize=10, style='italic',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

        ax.set_xlabel('Feature 1')
        ax.set_ylabel('Feature 2')
        ax.set_title(f'{panel_id}. {title}', fontweight='bold', loc='left')

        plt.tight_layout()
        plt.savefig(OUTPUT_DIR / f'06-{panel_id}-fig-random-splits-fail.svg', format='svg')
        plt.close()
        print(f"Saved: 06-{panel_id}-fig-random-splits-fail.svg")

# Fig 07: Homology-Aware Splitting
def create_fig_07():
    dot = graphviz.Digraph('homology_split', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='10,4!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='10', style='filled,rounded', penwidth='1.5')

    dot.node('seqs', 'All\nSequences', fillcolor='#aec7e8', shape='box')
    dot.node('cluster', 'Cluster by\nSimilarity\n(CD-HIT)', fillcolor='#c5b0d5', shape='box')
    dot.node('viz', 'Visualize\nClusters', fillcolor='#98df8a', shape='box')
    dot.node('assign', 'Assign Clusters\nto Splits', fillcolor='#ffbb78', shape='box')
    dot.node('validate', 'Validate No\nCross-Leakage', fillcolor='#2ca02c', fontcolor='white', shape='box')

    dot.edge('seqs', 'cluster', label='Step 1')
    dot.edge('cluster', 'viz', label='Step 2')
    dot.edge('viz', 'assign', label='Step 3')
    dot.edge('assign', 'validate', label='Step 4')

    dot.render(OUTPUT_DIR / '07-fig-homology-splitting', cleanup=True)
    print("Saved: 07-fig-homology-splitting.svg")

# Fig 08: Splitting Strategies
def create_fig_08():
    fig, ax = plt.subplots(figsize=(10, 6))

    strategies = ['Random', 'Individual', 'Family', 'Chromosome',
                  'Gene Family', 'Cohort/Site', 'Temporal', 'Ancestry']
    dependencies = ['Sample\nOverlap', 'Relatedness', 'Homology',
                    'Batch\nEffects', 'Ancestry']

    # Create a matrix showing which strategy addresses which dependency
    matrix = np.array([
        [0, 0, 0, 0, 0],  # Random
        [1, 0, 0, 0, 0],  # Individual
        [1, 1, 0, 0, 0],  # Family
        [1, 0, 1, 0, 0],  # Chromosome
        [1, 0, 1, 0, 0],  # Gene Family
        [1, 0, 0, 1, 0],  # Cohort/Site
        [1, 0, 0, 1, 0],  # Temporal
        [1, 1, 0, 0, 1],  # Ancestry
    ])

    im = ax.imshow(matrix, cmap='Greens', aspect='auto', alpha=0.8)

    ax.set_xticks(np.arange(len(dependencies)))
    ax.set_yticks(np.arange(len(strategies)))
    ax.set_xticklabels(dependencies, fontsize=9)
    ax.set_yticklabels(strategies, fontsize=9)

    # Add checkmarks
    for i in range(len(strategies)):
        for j in range(len(dependencies)):
            if matrix[i, j]:
                ax.text(j, i, 'Yes', ha='center', va='center', fontsize=9, fontweight='bold')

    ax.set_xlabel('Dependencies Addressed', fontweight='bold')
    ax.set_ylabel('Splitting Strategy', fontweight='bold')
    ax.set_title('Splitting Strategies and Dependencies', fontweight='bold')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '08-fig-splitting-strategies.svg', format='svg')
    plt.close()
    print("Saved: 08-fig-splitting-strategies.svg")

# Fig 09 A-C: Foundation Model Evaluation Paradigms
def create_fig_09():
    paradigms = [
        ('A', 'Zero-Shot', 'Frozen model, no task training'),
        ('B', 'Linear Probing', 'Frozen embeddings, trained classifier'),
        ('C', 'Fine-Tuning', 'Full gradient updates'),
    ]

    for panel_id, title, desc in paradigms:
        dot = graphviz.Digraph(f'paradigm_{panel_id}', format='svg')
        dot.attr(rankdir='LR', splines='polyline', size='6,3!', ratio='compress')
        dot.attr('node', fontname='Arial', fontsize='10', style='filled,rounded', penwidth='1.5')

        if panel_id == 'A':
            dot.node('input', 'Input', fillcolor='#aec7e8', shape='box')
            dot.node('model', 'Pretrained\nModel\n(frozen)', fillcolor='#9467bd', fontcolor='white', shape='box')
            dot.node('output', 'Prediction', fillcolor='#2ca02c', fontcolor='white', shape='box')
            dot.edge('input', 'model')
            dot.edge('model', 'output', label='Log-likelihood\nscoring')
        elif panel_id == 'B':
            dot.node('input', 'Input', fillcolor='#aec7e8', shape='box')
            dot.node('model', 'Pretrained\nEncoder\n(frozen)', fillcolor='#9467bd', fontcolor='white', shape='box')
            dot.node('embed', 'Embeddings', fillcolor='#c5b0d5', shape='box')
            dot.node('probe', 'Linear\nClassifier\n(trained)', fillcolor='#ff7f0e', shape='box')
            dot.node('output', 'Prediction', fillcolor='#2ca02c', fontcolor='white', shape='box')
            dot.edge('input', 'model')
            dot.edge('model', 'embed')
            dot.edge('embed', 'probe')
            dot.edge('probe', 'output')
        else:
            dot.node('input', 'Input', fillcolor='#aec7e8', shape='box')
            dot.node('model', 'Pretrained\nModel\n(trainable)', fillcolor='#ff7f0e', shape='box')
            dot.node('output', 'Prediction', fillcolor='#2ca02c', fontcolor='white', shape='box')
            dot.edge('input', 'model', label='Gradients')
            dot.edge('model', 'output', label='Gradients')

        dot.render(OUTPUT_DIR / f'09-{panel_id}-fig-fm-evaluation-paradigms', cleanup=True)
        print(f"Saved: 09-{panel_id}-fig-fm-evaluation-paradigms.svg")

# Fig 10: Metric Selection Flowchart
def create_fig_10():
    dot = graphviz.Digraph('metrics', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='8,10!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('start', 'Task Type?', fillcolor='#fff8dc', shape='diamond')
    dot.node('binary', 'Binary\nClassification', fillcolor='#aec7e8', shape='box')
    dot.node('regression', 'Continuous\nPrediction', fillcolor='#aec7e8', shape='box')
    dot.node('ranking', 'Ranking/\nPrioritization', fillcolor='#aec7e8', shape='box')

    dot.node('balanced', 'Class\nBalance?', fillcolor='#fff8dc', shape='diamond')
    dot.node('auroc', 'auROC\n(balanced)', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.node('auprc', 'auPRC\n(imbalanced)', fillcolor='#2ca02c', fontcolor='white', shape='box')

    dot.node('corr', 'Pearson/\nSpearman\nCorrelation', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.node('topk', 'Top-k Recall\nNDCG', fillcolor='#2ca02c', fontcolor='white', shape='box')

    dot.node('calibration', 'Need\nCalibration?', fillcolor='#fff8dc', shape='diamond')
    dot.node('ece', 'ECE +\nReliability\nDiagram', fillcolor='#ff7f0e', shape='box')

    dot.edge('start', 'binary')
    dot.edge('start', 'regression')
    dot.edge('start', 'ranking')
    dot.edge('binary', 'balanced')
    dot.edge('balanced', 'auroc', label='Yes')
    dot.edge('balanced', 'auprc', label='No')
    dot.edge('regression', 'corr')
    dot.edge('ranking', 'topk')
    dot.edge('auroc', 'calibration')
    dot.edge('auprc', 'calibration')
    dot.edge('calibration', 'ece', label='Yes')

    dot.render(OUTPUT_DIR / '10-fig-metric-selection', cleanup=True)
    print("Saved: 10-fig-metric-selection.svg")

if __name__ == '__main__':
    create_fig_01()
    create_fig_02()
    create_fig_03()
    create_fig_04()
    create_fig_05()
    create_fig_06()
    create_fig_07()
    create_fig_08()
    create_fig_09()
    create_fig_10()
    print("All Chapter 11 figures generated.")
