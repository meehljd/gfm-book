#!/usr/bin/env python3
"""
Figure 8.5: Multi-Task Pretraining
Shows architecture for comprehensive regulatory prediction.
"""

import graphviz
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_2" / "ch08"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

dot = graphviz.Digraph('multitask', format='svg')

dot.attr(
    rankdir='TB',
    splines='polyline',
    nodesep='0.4',
    ranksep='0.5',
    size='8,8!',
    ratio='compress',
)

dot.attr('node',
    fontname='Arial',
    fontsize='10',
    style='filled,rounded',
    color='#333333',
    penwidth='1.5',
    margin='0.12,0.08',
)

# Input
dot.node('input', 'DNA Sequence\n(e.g., 100kb window)', fillcolor='#aec7e8', shape='box')

# Shared encoder
dot.node('encoder', 'Shared Transformer\nEncoder', fillcolor='#9467bd', fontcolor='white', shape='box')

# Task-specific heads
tasks = [
    ('head_tf', 'TF Binding\n(690 TFs)', '#1f77b4'),
    ('head_dnase', 'DNase\n(125 cell types)', '#2ca02c'),
    ('head_histone', 'Histone Marks\n(100+ features)', '#ff7f0e'),
    ('head_expr', 'Expression\n(GTEx tissues)', '#d62728'),
]

dot.edge('input', 'encoder')

for task_id, label, color in tasks:
    dot.node(task_id, label, fillcolor=color, fontcolor='white', shape='box')
    dot.edge('encoder', task_id)

# Add note about shared representations
dot.node('note', 'Shared encoder learns general\nregulatory grammar\n\nTask heads specialize', fillcolor='#fff8dc', shape='note', fontsize='9')

output_path = OUTPUT_DIR / '05-fig-multitask-pretraining'
dot.render(output_path, cleanup=True)
print(f"Saved: {output_path}.svg")
