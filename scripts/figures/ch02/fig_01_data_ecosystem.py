#!/usr/bin/env python3
"""
Figure 2.1: The Genomic Data Ecosystem
Four-layer architecture showing data dependencies in genomic ML.

Uses Graphviz for clean layered architecture diagram.
"""

import graphviz
from pathlib import Path

# Output path
OUTPUT_DIR = Path(__file__).parent.parent.parent.parent / "figs" / "part_1" / "ch02"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Colors from style guide
COLORS = {
    'dna': '#1f77b4',
    'dna_light': '#aec7e8',
    'rna': '#2ca02c',
    'rna_light': '#98df8a',
    'protein': '#ff7f0e',
    'protein_light': '#ffbb78',
    'model': '#9467bd',
    'model_light': '#c5b0d5',
    'neutral': '#7f7f7f',
    'background': '#f7f7f7',
}

dot = graphviz.Digraph('data_ecosystem', format='svg')

# Graph attributes - vertical layout with horizontal clusters
dot.attr(
    rankdir='TB',
    splines='polyline',
    nodesep='0.4',
    ranksep='0.5',
    size='10,8!',
    ratio='compress',
)

# Default node style
dot.attr('node',
    fontname='Arial',
    fontsize='10',
    style='filled,rounded',
    fillcolor=COLORS['background'],
    color='#333333',
    penwidth='1.5',
    margin='0.12,0.08',
)

# Default edge style
dot.attr('edge',
    fontname='Arial',
    fontsize='8',
    color='#555555',
    penwidth='1.0',
    arrowsize='0.7',
)

# Layer 1: Reference Foundation (bottom)
with dot.subgraph(name='cluster_reference') as c:
    c.attr(
        label='Layer 1: Reference Foundation',
        style='rounded,filled',
        fillcolor='#e8f4f8',
        color='#1f77b4',
        fontname='Arial',
        fontsize='11',
        fontcolor='#1f77b4',
        labeljust='l',
    )
    c.attr('node', fillcolor=COLORS['dna_light'])
    c.node('grch38', 'GRCh38\nReference')
    c.node('t2t', 'T2T-CHM13\nTelomere-to-Telomere')
    c.node('gencode', 'GENCODE\nGene Models')
    c.node('mane', 'MANE Select\nCanonical Transcripts')

# Layer 2: Population Catalogs
with dot.subgraph(name='cluster_population') as c:
    c.attr(
        label='Layer 2: Population & Biobanks',
        style='rounded,filled',
        fillcolor='#f0f8e8',
        color='#2ca02c',
        fontname='Arial',
        fontsize='11',
        fontcolor='#2ca02c',
        labeljust='l',
    )
    c.attr('node', fillcolor=COLORS['rna_light'])
    c.node('gnomad', 'gnomAD\nAllele Frequencies')
    c.node('1kg', '1000 Genomes\nHaplotype Panels')
    c.node('ukbb', 'UK Biobank\nGWAS Cohort')
    c.node('allofus', 'All of Us\nDiversity Focus')

# Layer 3: Functional Genomics
with dot.subgraph(name='cluster_functional') as c:
    c.attr(
        label='Layer 3: Functional Genomics',
        style='rounded,filled',
        fillcolor='#fff8e8',
        color='#ff7f0e',
        fontname='Arial',
        fontsize='11',
        fontcolor='#ff7f0e',
        labeljust='l',
    )
    c.attr('node', fillcolor=COLORS['protein_light'])
    c.node('encode', 'ENCODE\nChromatin & TF Binding')
    c.node('roadmap', 'Roadmap\nEpigenomics')
    c.node('gtex', 'GTEx\neQTLs')
    c.node('dms', 'DMS\nVariant Effects')

# Layer 4: Clinical Interpretation (top)
with dot.subgraph(name='cluster_clinical') as c:
    c.attr(
        label='Layer 4: Clinical Interpretation',
        style='rounded,filled',
        fillcolor='#f8f0f8',
        color='#9467bd',
        fontname='Arial',
        fontsize='11',
        fontcolor='#9467bd',
        labeljust='l',
    )
    c.attr('node', fillcolor=COLORS['model_light'])
    c.node('clinvar', 'ClinVar\nPathogenicity')
    c.node('clingen', 'ClinGen\nExpert Curation')
    c.node('pharmgkb', 'PharmGKB\nPharmacogenomics')
    c.node('omim', 'OMIM\nGene-Disease')

# Inter-layer dependencies (vertical flow)
# Reference -> Population
dot.edge('grch38', 'gnomad', style='dashed', color='#888888')
dot.edge('gencode', '1kg', style='dashed', color='#888888')
dot.edge('mane', 'ukbb', style='dashed', color='#888888')

# Population -> Functional
dot.edge('gnomad', 'encode', style='dashed', color='#888888')
dot.edge('1kg', 'gtex', style='dashed', color='#888888')
dot.edge('ukbb', 'dms', style='dashed', color='#888888')

# Functional -> Clinical
dot.edge('encode', 'clinvar', style='dashed', color='#888888')
dot.edge('gtex', 'clingen', style='dashed', color='#888888')
dot.edge('dms', 'pharmgkb', style='dashed', color='#888888')

# Render
output_path = OUTPUT_DIR / '01-fig-data-ecosystem'
dot.render(output_path, cleanup=True)
print(f"Saved: {output_path}.svg")
