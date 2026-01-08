#!/usr/bin/env python3
"""
Figure 6.3: ExPecto Pipeline
Shows the chromatin-to-expression prediction pipeline.
"""

import graphviz
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_2" / "ch06"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

dot = graphviz.Digraph('expecto', format='svg')

dot.attr(
    rankdir='LR',
    splines='polyline',
    nodesep='0.4',
    ranksep='0.6',
    size='10,5!',
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

dot.attr('edge',
    fontname='Arial',
    fontsize='9',
    color='#555555',
    penwidth='1.2',
    arrowsize='0.8',
)

# Pipeline stages
dot.node('seq', 'Genomic\nSequence\n(40kb window)', fillcolor='#aec7e8', shape='box')
dot.node('deepsea', 'DeepSEA\nModel', fillcolor='#1f77b4', fontcolor='white', shape='box')
dot.node('chromatin', 'Predicted\nChromatin\n(2,002 features)', fillcolor='#98df8a', shape='box')
dot.node('linear', 'Regularized\nLinear Model', fillcolor='#9467bd', fontcolor='white', shape='box')
dot.node('expr', 'Expression\nLevel', fillcolor='#d62728', fontcolor='white', shape='box')

dot.edge('seq', 'deepsea')
dot.edge('deepsea', 'chromatin', label='Predict\naccessibility')
dot.edge('chromatin', 'linear')
dot.edge('linear', 'expr', label='Predict\nexpression')

# Add annotation
dot.node('note', 'Key insight: Integrate chromatin\npredictions across 40kb to\ncapture distal regulatory effects',
         fillcolor='#fff8dc', shape='note', fontsize='9')

output_path = OUTPUT_DIR / '03-fig-expecto-pipeline'
dot.render(output_path, cleanup=True)
print(f"Saved: {output_path}.svg")
