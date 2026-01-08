#!/usr/bin/env python3
"""
Figure 4.1: Variant Interpretation Funnel
Shows progressive filtering from millions of variants to manageable review set.
"""

import graphviz
from pathlib import Path

# Output path
OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_1" / "ch04"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Colors from style guide
COLORS = {
    'dna_light': '#aec7e8',
    'rna_light': '#98df8a',
    'protein_light': '#ffbb78',
    'model_light': '#c5b0d5',
    'neutral': '#7f7f7f',
}

dot = graphviz.Digraph('variant_funnel', format='svg')

# Graph attributes
dot.attr(
    rankdir='TB',
    splines='polyline',
    nodesep='0.4',
    ranksep='0.5',
    size='8,10!',
    ratio='compress',
)

# Default node style
dot.attr('node',
    fontname='Arial',
    fontsize='10',
    style='filled,rounded',
    color='#333333',
    penwidth='1.5',
    margin='0.15,0.08',
)

# Default edge style
dot.attr('edge',
    fontname='Arial',
    fontsize='8',
    color='#555555',
    penwidth='1.2',
    arrowsize='0.8',
)

# Funnel stages (wider at top, narrower at bottom)
# Width encoded in node shape/label

# Stage 1: All variants
dot.node('all', '~4-5 Million Variants\n(Whole Genome Sequencing)',
         fillcolor=COLORS['dna_light'], shape='box', width='4')

# Stage 2: Rare variants
dot.node('rare', '~100,000 Rare Variants\n(MAF < 1% in gnomAD)',
         fillcolor='#c6dbef', shape='box', width='3.5')

# Stage 3: Coding/splice
dot.node('coding', '~25,000 Coding/Splice Variants\n(Protein-altering or splice-site)',
         fillcolor=COLORS['rna_light'], shape='box', width='3')

# Stage 4: Conserved
dot.node('conserved', '~5,000 Conserved Positions\n(phyloP > 2)',
         fillcolor=COLORS['protein_light'], shape='box', width='2.5')

# Stage 5: High-scoring
dot.node('highscore', '~500 High-Scoring Variants\n(CADD ≥ 20)',
         fillcolor=COLORS['model_light'], shape='box', width='2')

# Stage 6: Final review
dot.node('final', '50-100 Candidates\n(Expert Review)',
         fillcolor='#d62728', fontcolor='white', shape='box', width='1.5')

# Edges with filter descriptions
dot.edge('all', 'rare', label='Population\nFrequency Filter')
dot.edge('rare', 'coding', label='Consequence\nFilter')
dot.edge('coding', 'conserved', label='Conservation\nFilter')
dot.edge('conserved', 'highscore', label='Ensemble\nScoring')
dot.edge('highscore', 'final', label='Clinical\nPrioritization')

# Render
output_path = OUTPUT_DIR / '01-fig-variant-funnel'
dot.render(output_path, cleanup=True)
print(f"Saved: {output_path}.svg")
