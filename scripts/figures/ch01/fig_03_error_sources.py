#!/usr/bin/env python3
"""
Figure 1.3: Error Sources Taxonomy (v2)
Uses Graphviz for clean hierarchical tree layout.
"""

from graphviz import Digraph
from pathlib import Path

OUTPUT_DIR = Path('/root/gfm_book/figs/part_1/ch01')
OUTPUT_FILE = OUTPUT_DIR / '03-fig-error-sources'

def create_error_taxonomy():
    """Create the error sources taxonomy diagram."""

    dot = Digraph('error_sources', format='svg')

    # Graph attributes - constrained size
    dot.attr(
        rankdir='LR',  # Horizontal orientation
        splines='polyline',
        nodesep='0.5',
        ranksep='0.4',
        fontname='Arial',
        fontsize='10',
        bgcolor='white',
        pad='0.2',
        size='8,8!',  # Constrain to 8x8 inches
        ratio='auto',
    )

    # Default node style
    dot.attr('node',
        fontname='Arial',
        fontsize='10',
        style='filled,rounded',
        fillcolor='#f7f7f7',
        color='#333333',
        penwidth='1.2',
        margin='0.15,0.08',
        height='0.35',
    )

    # Default edge style
    dot.attr('edge',
        fontname='Arial',
        fontsize='8',
        color='#555555',
        penwidth='1.2',
        arrowsize='0.7',
    )

    # === ROOT NODE ===
    dot.node('root', 'Variant Calling Errors',
             shape='box', fillcolor='#9467bd', fontcolor='white',
             fontsize='11', penwidth='2')

    # === LEVEL 1: Three main categories ===
    dot.node('seq', 'Sequencing Artifacts',
             shape='box', fillcolor='#aec7e8', color='#1f77b4', fontsize='10')
    dot.node('align', 'Alignment Artifacts',
             shape='box', fillcolor='#ffbb78', color='#ff7f0e', fontsize='10')
    dot.node('bio', 'Biological Complexity',
             shape='box', fillcolor='#98df8a', color='#2ca02c', fontsize='10')

    # === CONSEQUENCE LABELS (as edge labels instead of nodes) ===

    # === LEVEL 2: Sub-categories ===
    dot.node('instrument', 'Instrument Noise',
             shape='box', fillcolor='#e8e8e8', fontsize='9')
    dot.node('mapping', 'Mapping Ambiguity',
             shape='box', fillcolor='#e8e8e8', fontsize='9')
    dot.node('refbias', 'Reference Bias',
             shape='box', fillcolor='#e8e8e8', fontsize='9')
    dot.node('lowsig', 'Low Allele Fraction',
             shape='box', fillcolor='#e8e8e8', fontsize='9')

    # === LEVEL 3: Examples ===
    # Sequencing
    dot.node('ex_homo', 'Homopolymer slippage', shape='box', fillcolor='white', fontsize='8')
    dot.node('ex_pcr', 'PCR duplicates', shape='box', fillcolor='white', fontsize='8')
    dot.node('ex_strand', 'Strand bias', shape='box', fillcolor='white', fontsize='8')

    # Alignment
    dot.node('ex_segdup', 'Segmental duplications', shape='box', fillcolor='white', fontsize='8')
    dot.node('ex_paralog', 'Paralogous genes', shape='box', fillcolor='white', fontsize='8')
    dot.node('ex_nonref', 'Non-ref allele penalty', shape='box', fillcolor='white', fontsize='8')

    # Biological
    dot.node('ex_mosaic', 'Mosaicism', shape='box', fillcolor='white', fontsize='8')
    dot.node('ex_coverage', 'Coverage gaps', shape='box', fillcolor='white', fontsize='8')
    dot.node('ex_complex', 'Complex variants', shape='box', fillcolor='white', fontsize='8')

    # === CONSEQUENCE NODES ===
    dot.node('fp_seq', 'FP', shape='ellipse', fillcolor='#d62728',
             fontcolor='white', fontsize='9', width='0.4', height='0.25', fixedsize='true')
    dot.node('fp_align', 'FP', shape='ellipse', fillcolor='#d62728',
             fontcolor='white', fontsize='9', width='0.4', height='0.25', fixedsize='true')
    dot.node('fn_align', 'FN', shape='ellipse', fillcolor='#7f7f7f',
             fontcolor='white', fontsize='9', width='0.4', height='0.25', fixedsize='true')
    dot.node('fn_bio', 'FN', shape='ellipse', fillcolor='#7f7f7f',
             fontcolor='white', fontsize='9', width='0.4', height='0.25', fixedsize='true')

    # === EDGES ===
    # Root to categories
    dot.edge('root', 'seq')
    dot.edge('root', 'align')
    dot.edge('root', 'bio')

    # Categories to sub-categories
    dot.edge('seq', 'instrument')
    dot.edge('align', 'mapping')
    dot.edge('align', 'refbias')
    dot.edge('bio', 'lowsig')

    # Sub-categories to examples
    dot.edge('instrument', 'ex_homo')
    dot.edge('instrument', 'ex_pcr')
    dot.edge('instrument', 'ex_strand')

    dot.edge('mapping', 'ex_segdup')
    dot.edge('mapping', 'ex_paralog')
    dot.edge('refbias', 'ex_nonref')

    dot.edge('lowsig', 'ex_mosaic')
    dot.edge('lowsig', 'ex_coverage')
    dot.edge('lowsig', 'ex_complex')

    # Consequence edges (dashed, to the side)
    dot.edge('seq', 'fp_seq', style='dashed', color='#d62728', constraint='false')
    dot.edge('align', 'fp_align', style='dashed', color='#d62728', constraint='false')
    dot.edge('align', 'fn_align', style='dashed', color='#7f7f7f', constraint='false')
    dot.edge('bio', 'fn_bio', style='dashed', color='#7f7f7f', constraint='false')

    # === LEGEND ===
    with dot.subgraph(name='cluster_legend') as legend:
        legend.attr(label='Consequence', labelloc='t', fontsize='9',
                    style='rounded', color='#cccccc', bgcolor='#fafafa')
        legend.node('leg_fp', 'FP = False Positive',
                    shape='box', fillcolor='#d62728', fontcolor='white', fontsize='8')
        legend.node('leg_fn', 'FN = False Negative',
                    shape='box', fillcolor='#7f7f7f', fontcolor='white', fontsize='8')
        legend.edge('leg_fp', 'leg_fn', style='invis')

    return dot


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    dot = create_error_taxonomy()

    # Render to SVG
    dot.render(OUTPUT_FILE, cleanup=True)
    print(f"Saved: {OUTPUT_FILE}.svg")


if __name__ == '__main__':
    main()
