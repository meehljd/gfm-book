#!/usr/bin/env python3
"""
Figure 1.1: Variant Calling Pipeline (v2)
Uses Graphviz with TB layout and horizontal phase clusters.
"""

from graphviz import Digraph
from pathlib import Path

OUTPUT_DIR = Path('/root/gfm_book/figs/part_1/ch01')
OUTPUT_FILE = OUTPUT_DIR / '01-fig-variant-pipeline'

def create_pipeline():
    """Create the variant calling pipeline diagram."""

    dot = Digraph('variant_pipeline', format='svg')

    # Graph attributes - TB with compact settings
    dot.attr(
        rankdir='TB',
        splines='polyline',
        nodesep='0.25',
        ranksep='0.3',
        fontname='Arial',
        fontsize='10',
        bgcolor='white',
        pad='0.2',
        size='10,8!',
        ratio='compress',
    )

    # Default node style - compact
    dot.attr('node',
        fontname='Arial',
        fontsize='9',
        style='filled,rounded',
        fillcolor='#f7f7f7',
        color='#333333',
        penwidth='1.2',
        margin='0.08,0.04',
        height='0.35',
    )

    # Default edge style
    dot.attr('edge',
        fontname='Arial',
        fontsize='8',
        color='#555555',
        penwidth='1.0',
        arrowsize='0.6',
    )

    # === PHASE 1: Sample Prep ===
    with dot.subgraph(name='cluster_prep') as prep:
        prep.attr(label='Sample Preparation', labelloc='t', fontsize='10',
                  style='rounded', color='#1f77b4', bgcolor='#f8f9fa')
        prep.node('dna', 'DNA Sample',
                  shape='parallelogram', fillcolor='#aec7e8', color='#1f77b4')
        prep.node('libprep', 'Library Prep', shape='box', fillcolor='#f0f0f0')

    # === PHASE 2: Sequencing ===
    with dot.subgraph(name='cluster_seq') as seq:
        seq.attr(label='Sequencing', labelloc='t', fontsize='10',
                 style='rounded', color='#2ca02c', bgcolor='#f8f9fa')
        seq.node('shortread', 'Short-Read (Illumina)',
                 shape='box', fillcolor='#aec7e8', color='#1f77b4')
        seq.node('longread', 'Long-Read (PacBio/ONT)',
                 shape='box', fillcolor='#98df8a', color='#2ca02c')
        seq.node('fastq', 'FASTQ', shape='note', fillcolor='#e8e8e8')

    # === PHASE 3: Alignment ===
    with dot.subgraph(name='cluster_align') as align:
        align.attr(label='Alignment', labelloc='t', fontsize='10',
                   style='rounded', color='#9467bd', bgcolor='#f8f9fa')
        align.node('ref', 'Reference (GRCh38)',
                   shape='cylinder', fillcolor='#e0e0e0', color='#7f7f7f')
        align.node('aligner', 'BWA-MEM / minimap2',
                   shape='box', fillcolor='#c5b0d5', color='#9467bd')
        align.node('bam', 'BAM/CRAM', shape='note', fillcolor='#e8e8e8')

    # === PHASE 4: Post-processing ===
    with dot.subgraph(name='cluster_post') as post:
        post.attr(label='Post-Processing', labelloc='t', fontsize='10',
                  style='rounded', color='#ff7f0e', bgcolor='#f8f9fa')
        post.node('dedup', 'Mark Duplicates', shape='box', fillcolor='#f0f0f0')
        post.node('bqsr', 'BQSR', shape='box', fillcolor='#f0f0f0')

    # === PHASE 5: Variant Calling ===
    with dot.subgraph(name='cluster_call') as call:
        call.attr(label='Variant Calling', labelloc='t', fontsize='10',
                  style='rounded', color='#d62728', bgcolor='#f8f9fa')
        call.node('caller', 'DeepVariant / GATK',
                  shape='box', fillcolor='#c5b0d5', color='#9467bd')
        call.node('gvcf', 'gVCF', shape='note', fillcolor='#ffbb78', color='#ff7f0e')

    # === PHASE 6: Joint Calling ===
    with dot.subgraph(name='cluster_joint') as joint:
        joint.attr(label='Cohort Analysis', labelloc='t', fontsize='10',
                   style='rounded', color='#2ca02c', bgcolor='#f8f9fa')
        joint.node('jointcall', 'Joint Genotyping',
                   shape='box', fillcolor='#c5b0d5', color='#9467bd')
        joint.node('filter', 'VQSR Filtering', shape='box', fillcolor='#f0f0f0')
        joint.node('vcf', 'VCF', shape='note', fillcolor='#98df8a',
                   color='#2ca02c', penwidth='2')

    # === EDGES ===
    dot.edge('dna', 'libprep')
    dot.edge('libprep', 'shortread')
    dot.edge('libprep', 'longread')
    dot.edge('shortread', 'fastq')
    dot.edge('longread', 'fastq')
    dot.edge('fastq', 'aligner')
    dot.edge('ref', 'aligner')
    dot.edge('aligner', 'bam')
    dot.edge('bam', 'dedup')
    dot.edge('dedup', 'bqsr')
    dot.edge('bqsr', 'caller')
    dot.edge('caller', 'gvcf')
    dot.edge('gvcf', 'jointcall')
    dot.edge('jointcall', 'filter')
    dot.edge('filter', 'vcf')

    return dot


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    dot = create_pipeline()
    dot.render(OUTPUT_FILE, cleanup=True)
    print(f"Saved: {OUTPUT_FILE}.svg")


if __name__ == '__main__':
    main()
