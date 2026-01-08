#!/usr/bin/env python3
"""
Figure 4.3: ACMG-AMP Classification Framework
Five-tier classification with evidence types.
"""

import graphviz
from pathlib import Path

# Output path
OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_1" / "ch04"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

dot = graphviz.Digraph('acmg_classification', format='svg')

# Graph attributes
dot.attr(
    rankdir='LR',
    splines='polyline',
    nodesep='0.3',
    ranksep='0.5',
    size='10,6!',
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
    fontsize='8',
    color='#555555',
    penwidth='1.0',
    arrowsize='0.7',
)

# Classification tiers (left to right, benign to pathogenic)
dot.node('benign', 'Benign\n(B)', fillcolor='#2ca02c', fontcolor='white', shape='box')
dot.node('likely_benign', 'Likely\nBenign\n(LB)', fillcolor='#98df8a', shape='box')
dot.node('vus', 'VUS\n(Uncertain)', fillcolor='#7f7f7f', fontcolor='white', shape='box')
dot.node('likely_path', 'Likely\nPathogenic\n(LP)', fillcolor='#ffbb78', shape='box')
dot.node('pathogenic', 'Pathogenic\n(P)', fillcolor='#d62728', fontcolor='white', shape='box')

# Connect tiers
dot.edge('benign', 'likely_benign', style='invis')
dot.edge('likely_benign', 'vus', style='invis')
dot.edge('vus', 'likely_path', style='invis')
dot.edge('likely_path', 'pathogenic', style='invis')

# Evidence types cluster
with dot.subgraph(name='cluster_evidence') as c:
    c.attr(
        label='Evidence Types',
        style='rounded,filled',
        fillcolor='#f7f7f7',
        color='#555555',
        fontname='Arial',
        fontsize='10',
        labeljust='l',
    )

    c.node('pvs', 'PVS: Very Strong\n(e.g., null variant in LOF gene)',
           fillcolor='#fee0d2', shape='box')
    c.node('ps', 'PS: Strong\n(e.g., functional study, de novo)',
           fillcolor='#fcbba1', shape='box')
    c.node('pm', 'PM: Moderate\n(e.g., absent from controls)',
           fillcolor='#fc9272', shape='box')
    c.node('pp', 'PP: Supporting\n(e.g., computational, cosegregation)',
           fillcolor='#fb6a4a', shape='box')

# Computational evidence highlight
with dot.subgraph(name='cluster_computational') as c:
    c.attr(
        label='Computational (PP3/BP4)',
        style='rounded,dashed',
        fillcolor='#e8f4f8',
        color='#1f77b4',
        fontname='Arial',
        fontsize='9',
        labeljust='l',
    )
    c.node('comp', 'CADD, REVEL, SIFT,\nPolyPhen, conservation',
           fillcolor='#aec7e8', shape='box')

# Connect evidence to PP
dot.edge('pp', 'comp', label='includes', style='dashed', dir='none')

# Render
output_path = OUTPUT_DIR / '03-fig-acmg-classification'
dot.render(output_path, cleanup=True)
print(f"Saved: {output_path}.svg")
