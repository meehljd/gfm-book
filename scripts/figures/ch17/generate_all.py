#!/usr/bin/env python3
"""
Chapter 17: VEP Foundation Models Figures
Generates all figures for this chapter.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from pathlib import Path
import graphviz

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_3" / "ch17"
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

# Fig 01 A-B: FM VEP Paradigm
def create_fig_01():
    # Panel A: Classical VEP
    dot = graphviz.Digraph('classical_vep', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='8,3!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('var', 'Variant', fillcolor='#aec7e8', shape='box')
    dot.node('feat', 'Hand-crafted\nFeatures', fillcolor='#ffbb78', shape='box')
    dot.node('model', 'ML\nClassifier', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('score', 'Pathogenicity\nScore', fillcolor='#98df8a', shape='box')

    dot.edge('var', 'feat', label='Conservation\nFrequency\nAnnotation')
    dot.edge('feat', 'model')
    dot.edge('model', 'score')

    dot.render(OUTPUT_DIR / '01-A-fig-fm-vep-paradigm', cleanup=True)
    print("Saved: 01-A-fig-fm-vep-paradigm.svg")

    # Panel B: Foundation model VEP
    dot = graphviz.Digraph('fm_vep', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='8,3!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('var', 'Variant +\nContext', fillcolor='#aec7e8', shape='box')
    dot.node('fm', 'Foundation\nModel', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('embed', 'Learned\nEmbeddings', fillcolor='#c5b0d5', shape='box')
    dot.node('score', 'Effect\nScore', fillcolor='#98df8a', shape='box')

    dot.edge('var', 'fm', label='Sequence')
    dot.edge('fm', 'embed', label='Self-supervised')
    dot.edge('embed', 'score', label='Zero-shot or\nfine-tuned')

    dot.render(OUTPUT_DIR / '01-B-fig-fm-vep-paradigm', cleanup=True)
    print("Saved: 01-B-fig-fm-vep-paradigm.svg")

# Fig 02 A-B: AlphaMissense
def create_fig_02():
    # Panel A: Architecture
    dot = graphviz.Digraph('alphamissense', format='svg')
    dot.attr(rankdir='TB', splines='polyline', size='8,6!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('seq', 'Protein\nSequence', fillcolor='#aec7e8', shape='box')
    dot.node('msa', 'Multiple Sequence\nAlignment', fillcolor='#aec7e8', shape='box')
    dot.node('struct', 'AlphaFold\nStructure Module', fillcolor='#9467bd', fontcolor='white', shape='box')
    dot.node('embed', 'Structure-Aware\nEmbeddings', fillcolor='#c5b0d5', shape='box')
    dot.node('head', 'Pathogenicity\nHead', fillcolor='#ff7f0e', shape='box')
    dot.node('score', 'Pathogenicity\nScore', fillcolor='#2ca02c', fontcolor='white', shape='box')

    dot.edge('seq', 'struct')
    dot.edge('msa', 'struct')
    dot.edge('struct', 'embed')
    dot.edge('embed', 'head')
    dot.edge('head', 'score')

    dot.render(OUTPUT_DIR / '02-A-fig-alphamissense', cleanup=True)
    print("Saved: 02-A-fig-alphamissense.svg")

    # Panel B: Performance comparison
    fig, ax = plt.subplots(figsize=(6, 4))
    np.random.seed(42)

    methods = ['SIFT', 'PolyPhen-2', 'CADD', 'REVEL', 'ESM-1v', 'AlphaMissense']
    auroc = [0.72, 0.75, 0.80, 0.84, 0.86, 0.91]
    colors = ['#aec7e8', '#aec7e8', '#ffbb78', '#ffbb78', '#1f77b4', '#2ca02c']

    bars = ax.bar(methods, auroc, color=colors, edgecolor='white')
    ax.axhline(y=0.5, color='#555555', linestyle='--', alpha=0.5)

    ax.set_ylabel('auROC (ClinVar)', fontweight='bold')
    ax.set_title('B. Pathogenicity Prediction Performance', fontweight='bold', loc='left')
    ax.set_ylim(0.5, 1)

    # Add era labels
    ax.axvline(x=1.5, color='#555555', linestyle=':', alpha=0.3)
    ax.axvline(x=3.5, color='#555555', linestyle=':', alpha=0.3)
    ax.text(0.5, 0.95, 'Classical', ha='center', fontsize=8, alpha=0.7)
    ax.text(2.5, 0.95, 'Ensemble', ha='center', fontsize=8, alpha=0.7)
    ax.text(4.5, 0.95, 'Foundation', ha='center', fontsize=8, alpha=0.7)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '02-B-fig-alphamissense.svg', format='svg')
    plt.close()
    print("Saved: 02-B-fig-alphamissense.svg")

# Fig 03 A-B: Multi-Model Integration
def create_fig_03():
    # Panel A: Model ensemble
    dot = graphviz.Digraph('ensemble', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='10,4!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('var', 'Variant', fillcolor='#aec7e8', shape='box')

    dot.node('dna', 'DNA-LM\n(Evo 2)', fillcolor='#1f77b4', fontcolor='white', shape='box')
    dot.node('prot', 'Protein-LM\n(ESM-2)', fillcolor='#2ca02c', fontcolor='white', shape='box')
    dot.node('reg', 'Regulatory\n(Enformer)', fillcolor='#ff7f0e', fontcolor='white', shape='box')
    dot.node('struct', 'Structure\n(AlphaMissense)', fillcolor='#9467bd', fontcolor='white', shape='box')

    dot.node('combine', 'Integration\nLayer', fillcolor='#d62728', fontcolor='white', shape='box')
    dot.node('final', 'Final\nScore', fillcolor='#98df8a', shape='box')

    dot.edge('var', 'dna')
    dot.edge('var', 'prot')
    dot.edge('var', 'reg')
    dot.edge('var', 'struct')
    dot.edge('dna', 'combine')
    dot.edge('prot', 'combine')
    dot.edge('reg', 'combine')
    dot.edge('struct', 'combine')
    dot.edge('combine', 'final')

    dot.render(OUTPUT_DIR / '03-A-fig-multimodel-integration', cleanup=True)
    print("Saved: 03-A-fig-multimodel-integration.svg")

    # Panel B: Complementary strengths
    fig, ax = plt.subplots(figsize=(6, 4))

    variant_types = ['Coding\nMissense', 'Coding\nSynonymous', 'Splice\nJunction', 'Regulatory\nNoncoding', 'Intronic']
    dna_lm = [0.75, 0.70, 0.85, 0.80, 0.72]
    protein_lm = [0.90, 0.60, 0.55, 0.50, 0.50]
    regulatory = [0.70, 0.75, 0.82, 0.88, 0.78]

    x = np.arange(len(variant_types))
    width = 0.25

    ax.bar(x - width, dna_lm, width, label='DNA-LM', color='#1f77b4')
    ax.bar(x, protein_lm, width, label='Protein-LM', color='#2ca02c')
    ax.bar(x + width, regulatory, width, label='Regulatory', color='#ff7f0e')

    ax.set_ylabel('Prediction Quality', fontweight='bold')
    ax.set_title('B. Model Strengths by Variant Type', fontweight='bold', loc='left')
    ax.set_xticks(x)
    ax.set_xticklabels(variant_types, fontsize=8)
    ax.legend(fontsize=8)
    ax.set_ylim(0, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '03-B-fig-multimodel-integration.svg', format='svg')
    plt.close()
    print("Saved: 03-B-fig-multimodel-integration.svg")

# Fig 04 A-B: Calibration for Clinical Use
def create_fig_04():
    np.random.seed(42)

    # Panel A: Calibration curves
    fig, ax = plt.subplots(figsize=(6, 5))

    predicted = np.linspace(0, 1, 10)
    perfect = predicted
    uncalibrated = 0.2 + 0.6 * predicted + np.random.randn(10) * 0.05
    calibrated = predicted + np.random.randn(10) * 0.03

    ax.plot([0, 1], [0, 1], 'k--', linewidth=2, label='Perfect calibration')
    ax.plot(predicted, np.clip(uncalibrated, 0, 1), 'o-', color='#d62728', linewidth=2, label='Uncalibrated')
    ax.plot(predicted, np.clip(calibrated, 0, 1), 's-', color='#2ca02c', linewidth=2, label='Calibrated')

    ax.set_xlabel('Predicted Probability', fontweight='bold')
    ax.set_ylabel('Observed Frequency', fontweight='bold')
    ax.set_title('A. Model Calibration', fontweight='bold', loc='left')
    ax.legend(fontsize=9)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-A-fig-calibration-clinical.svg', format='svg')
    plt.close()
    print("Saved: 04-A-fig-calibration-clinical.svg")

    # Panel B: Clinical decision thresholds
    fig, ax = plt.subplots(figsize=(6, 4))

    categories = ['Benign', 'Likely\nBenign', 'VUS', 'Likely\nPathogenic', 'Pathogenic']
    thresholds = [0.1, 0.3, 0.5, 0.7, 0.9]
    colors = ['#2ca02c', '#98df8a', '#ffff00', '#ffbb78', '#d62728']

    for i, (cat, thresh, color) in enumerate(zip(categories, thresholds, colors)):
        width = thresholds[min(i+1, len(thresholds)-1)] - thresholds[max(i-1, 0)] if i < len(thresholds)-1 else 0.2
        ax.barh(cat, width, left=thresholds[i] - width/2, color=color, edgecolor='white', height=0.6)

    ax.set_xlabel('Pathogenicity Score', fontweight='bold')
    ax.set_title('B. Clinical Classification Thresholds', fontweight='bold', loc='left')
    ax.set_xlim(0, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '04-B-fig-calibration-clinical.svg', format='svg')
    plt.close()
    print("Saved: 04-B-fig-calibration-clinical.svg")

# Fig 05 A-B: VEP Uncertainty
def create_fig_05():
    np.random.seed(42)

    # Panel A: Uncertainty by variant class
    fig, ax = plt.subplots(figsize=(6, 4))

    classes = ['Common\n(MAF>1%)', 'Rare\n(MAF<1%)', 'Novel\n(unseen)', 'VUS\n(uncertain)']
    uncertainty = [0.1, 0.25, 0.45, 0.6]
    colors = ['#2ca02c', '#ff7f0e', '#d62728', '#9467bd']

    bars = ax.bar(classes, uncertainty, color=colors, edgecolor='white')
    ax.axhline(y=0.3, color='#555555', linestyle='--', alpha=0.5)
    ax.text(3.5, 0.32, 'High uncertainty', fontsize=8, alpha=0.7)

    ax.set_ylabel('Prediction Uncertainty', fontweight='bold')
    ax.set_title('A. Uncertainty by Variant Class', fontweight='bold', loc='left')
    ax.set_ylim(0, 0.8)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '05-A-fig-vep-uncertainty.svg', format='svg')
    plt.close()
    print("Saved: 05-A-fig-vep-uncertainty.svg")

    # Panel B: Uncertainty-performance relationship
    fig, ax = plt.subplots(figsize=(6, 4))

    uncertainty = np.linspace(0, 0.6, 100)
    accuracy = 0.95 - 0.8 * uncertainty + np.random.randn(100) * 0.02
    accuracy = np.clip(accuracy, 0, 1)

    ax.scatter(uncertainty, accuracy, alpha=0.5, c='#1f77b4', s=20)
    z = np.polyfit(uncertainty, accuracy, 1)
    p = np.poly1d(z)
    ax.plot([0, 0.6], [p(0), p(0.6)], 'r--', linewidth=2)

    ax.set_xlabel('Model Uncertainty', fontweight='bold')
    ax.set_ylabel('Prediction Accuracy', fontweight='bold')
    ax.set_title('B. Uncertainty Tracks with Accuracy', fontweight='bold', loc='left')

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '05-B-fig-vep-uncertainty.svg', format='svg')
    plt.close()
    print("Saved: 05-B-fig-vep-uncertainty.svg")

# Fig 06 A-B: VEP Gains and Gaps
def create_fig_06():
    np.random.seed(42)

    # Panel A: Performance gains over time
    fig, ax = plt.subplots(figsize=(6, 4))

    years = [2015, 2017, 2019, 2021, 2023, 2025]
    performance = [0.72, 0.76, 0.82, 0.86, 0.90, 0.93]
    models = ['SIFT', 'M-CAP', 'CADD v1.4', 'REVEL', 'ESM-1v', 'AlphaMissense']

    ax.plot(years, performance, 'o-', color='#1f77b4', linewidth=2, markersize=8)
    for year, perf, model in zip(years, performance, models):
        ax.annotate(model, (year, perf), textcoords="offset points",
                    xytext=(0, 10), ha='center', fontsize=8)

    ax.set_xlabel('Year', fontweight='bold')
    ax.set_ylabel('auROC (ClinVar)', fontweight='bold')
    ax.set_title('A. VEP Performance Gains Over Time', fontweight='bold', loc='left')
    ax.set_ylim(0.6, 1)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '06-A-fig-vep-gains-gaps.svg', format='svg')
    plt.close()
    print("Saved: 06-A-fig-vep-gains-gaps.svg")

    # Panel B: Remaining gaps
    fig, ax = plt.subplots(figsize=(6, 4))

    gaps = ['Non-coding\nVariants', 'Structural\nVariants', 'Ancestry\nGeneralization', 'Rare Genes\n(few labels)', 'Epistatic\nEffects']
    gap_size = [0.4, 0.55, 0.35, 0.45, 0.6]
    colors = ['#d62728', '#d62728', '#ff7f0e', '#ff7f0e', '#d62728']

    bars = ax.barh(gaps, gap_size, color=colors, edgecolor='white')
    ax.axvline(x=0.3, color='#555555', linestyle='--', alpha=0.5)

    ax.set_xlabel('Performance Gap (vs. coding missense)', fontweight='bold')
    ax.set_title('B. Remaining Challenges', fontweight='bold', loc='left')
    ax.set_xlim(0, 0.7)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / '06-B-fig-vep-gains-gaps.svg', format='svg')
    plt.close()
    print("Saved: 06-B-fig-vep-gains-gaps.svg")

# Fig 07: Long-Read VEP
def create_fig_07():
    dot = graphviz.Digraph('longread', format='svg')
    dot.attr(rankdir='LR', splines='polyline', size='12,4!', ratio='compress')
    dot.attr('node', fontname='Arial', fontsize='9', style='filled,rounded', penwidth='1.5')

    dot.node('longread', 'Long-Read\nSequencing', fillcolor='#aec7e8', shape='box')
    dot.node('sv', 'Structural\nVariants', fillcolor='#ffbb78', shape='box')
    dot.node('phase', 'Phased\nHaplotypes', fillcolor='#ffbb78', shape='box')
    dot.node('repeat', 'Repeat\nExpansions', fillcolor='#ffbb78', shape='box')

    dot.node('fm', 'Long-Context\nFM (Evo 2)', fillcolor='#9467bd', fontcolor='white', shape='box')

    dot.node('sv_score', 'SV Effect\nScore', fillcolor='#98df8a', shape='box')
    dot.node('hap_score', 'Haplotype\nEffect', fillcolor='#98df8a', shape='box')
    dot.node('rep_score', 'Expansion\nPathogenicity', fillcolor='#98df8a', shape='box')

    dot.edge('longread', 'sv')
    dot.edge('longread', 'phase')
    dot.edge('longread', 'repeat')
    dot.edge('sv', 'fm')
    dot.edge('phase', 'fm')
    dot.edge('repeat', 'fm')
    dot.edge('fm', 'sv_score')
    dot.edge('fm', 'hap_score')
    dot.edge('fm', 'rep_score')

    dot.render(OUTPUT_DIR / '07-fig-long-read-vep', cleanup=True)
    print("Saved: 07-fig-long-read-vep.svg")

if __name__ == '__main__':
    create_fig_01()
    create_fig_02()
    create_fig_03()
    create_fig_04()
    create_fig_05()
    create_fig_06()
    create_fig_07()
    print("All Chapter 17 figures generated.")
