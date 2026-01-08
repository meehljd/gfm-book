#!/usr/bin/env python3
"""
Figure 4.6: The Circularity Problem
Diagram showing feedback loop between predictors and clinical databases.
"""

import graphviz
from pathlib import Path

# Output path
OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_1" / "ch04"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

dot = graphviz.Digraph('circularity', format='svg')

# Graph attributes
dot.attr(
    rankdir='TB',
    splines='curved',
    nodesep='0.5',
    ranksep='0.6',
    size='8,8!',
    ratio='compress',
)

# Default styles
dot.attr('node',
    fontname='Arial',
    fontsize='10',
    style='filled,rounded',
    color='#333333',
    penwidth='1.5',
    margin='0.12,0.08',
)

dot.attr('edge',
    fontname='Arial',
    fontsize='9',
    color='#d62728',
    penwidth='1.5',
    arrowsize='0.8',
)

# Main cycle nodes
dot.node('predictor', 'Computational\nPredictor\n(CADD, REVEL)',
         fillcolor='#aec7e8', shape='box')
dot.node('clinician', 'Clinical\nLaboratory',
         fillcolor='#98df8a', shape='box')
dot.node('clinvar', 'ClinVar\nDatabase',
         fillcolor='#ffbb78', shape='box')
dot.node('benchmark', 'Benchmarking\nStudy',
         fillcolor='#c5b0d5', shape='box')

# Cycle edges with labels
dot.edge('predictor', 'clinician', label='1. High score\nsupports classification')
dot.edge('clinician', 'clinvar', label='2. Classification\nsubmitted')
dot.edge('clinvar', 'benchmark', label='3. Benchmark\nuses ClinVar')
dot.edge('benchmark', 'predictor', label='4. "High performance"\nencourages use')

# Add central warning
dot.node('warning', 'Circularity:\nPredictors evaluated on\nlabels they helped create',
         fillcolor='#fee0d2', shape='box', fontcolor='#d62728',
         style='filled,rounded,bold')

# Connect warning to center
dot.edge('predictor', 'warning', style='invis')
dot.edge('clinvar', 'warning', style='invis')

# Intervention strategies
with dot.subgraph(name='cluster_solutions') as c:
    c.attr(
        label='Intervention Strategies',
        style='rounded,dashed',
        fillcolor='#f7f7f7',
        color='#555555',
        fontname='Arial',
        fontsize='10',
        labeljust='l',
    )
    c.node('temporal', 'Temporal Holdouts\n(pre-adoption variants)',
           fillcolor='#e8f4f8', shape='box', fontsize='9')
    c.node('functional', 'Functional Assays\n(DMS ground truth)',
           fillcolor='#e8f4f8', shape='box', fontsize='9')
    c.node('prospective', 'Prospective Evaluation\n(new variants)',
           fillcolor='#e8f4f8', shape='box', fontsize='9')

# Render
output_path = OUTPUT_DIR / '06-fig-circularity-problem'
dot.render(output_path, cleanup=True)
print(f"Saved: {output_path}.svg")
