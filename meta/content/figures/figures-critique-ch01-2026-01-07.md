# Figure Design Critique Report: Chapter 1

**Generated**: 2026-01-07
**File**: part_1/p1-ch01-ngs.qmd
**Mode**: `--mode critique`
**Existing figures**: 7
**Figures critiqued**: 7

---

## Executive Summary

All seven figures replace previous placeholders and successfully communicate their intended messages. However, several issues were identified:

1. **Grayscale readability is problematic** across most figures - important for print
2. **Some figures are visually busy** with too many elements competing for attention
3. **Label legibility** is marginal in several figures at typical reading sizes
4. **The phasing figure (02)** relies on pink/blue gender-coded colors that may be confusing without context

**Overall chapter grade: B**

---

## Figure Inventory

| Fig # | Title | Status | Grade | Primary Issue |
|-------|-------|--------|-------|---------------|
| 1.1 | Variant Pipeline | Complete | B+ | Dense; grayscale fails |
| 1.2A | Unphased Genotypes | Complete | C+ | Unclear message in isolation |
| 1.2B | Cis Configuration | Complete | B | Color relies on pink/blue convention |
| 1.2C | Trans Configuration | Complete | B | Same as B |
| 1.3 | Error Sources | Complete | B+ | Bullet points compete with tree |
| 1.4 | Difficult Regions | Complete | B- | Very dense; small labels |
| 1.5 | DeepVariant Pileup | Complete | B | CNN diagram oversimplified |

---

## Detailed Critiques

### Figure 1.1: Variant Calling Pipeline

**File**: `figs/part_1/ch01/01-fig-variant-pipeline.svg` (684×461pt, 106 KB)

#### Scores

| Criterion | Score | Weight | Notes |
|-----------|-------|--------|-------|
| Clarity | B | 25% | Main flow clear, but dense with many boxes |
| Accuracy | A | 25% | All pipeline stages correctly represented |
| Consistency | A | 20% | Follows genomics color palette |
| Accessibility | C | 15% | Blues/purples indistinguishable in grayscale |
| Integration | A | 15% | Well-referenced in text (line 166-170) |

**Weighted Grade: B+ (83%)**

#### Critique Questions

1. **<10 seconds to understand?** Partially. The flow is top-to-bottom, but there are many boxes requiring careful reading.
2. **All elements necessary?** The section grouping boxes (dotted lines) add visual noise without aiding comprehension significantly.
3. **Genomics color conventions?** Yes - DNA blues, long-read greens, model purples.
4. **Works in grayscale?** No - "Short-Read" (#aec7e8) and "Long-Read" (#98df8a) become nearly identical grays.
5. **Labels legible?** Marginal - 8-9pt text in some boxes; would benefit from larger fonts.
6. **Caption explains what to notice?** Yes - comprehensive caption describes each stage.
7. **Referenced in text?** Yes - line 166.

#### Specific Issues

1. **Visual hierarchy unclear**: All boxes have similar visual weight; critical nodes (FASTQ, VCF) should be more prominent
2. **Grayscale failure**: Short-read vs long-read paths indistinguishable when printed B&W
3. **Box labels too small**: "Post-Processing" section labels cramped
4. **Missing file format icons**: Would aid recognition (e.g., distinctive shapes for file types)

#### Recommendations

1. **Add distinctive shapes** for file formats (ovals for data files, rectangles for processes)
2. **Increase contrast** between short-read and long-read paths (use texture or shape, not just color)
3. **Increase font size** to minimum 10pt
4. **Simplify** by removing dotted section boxes or making them less prominent

---

### Figure 1.2A: Unphased Genotypes

**File**: `figs/part_1/ch01/02-A-fig-phasing-compound-het.svg` (293×236pt, 43 KB)

#### Scores

| Criterion | Score | Weight | Notes |
|-----------|-------|--------|-------|
| Clarity | C | 25% | Purpose unclear without reading B/C |
| Accuracy | B | 25% | Correct representation but generic |
| Consistency | B | 20% | Matches palette but grey chromosomes bland |
| Accessibility | B | 15% | Red variants clear; grey neutral |
| Integration | B | 15% | Works as part of multi-panel figure |

**Weighted Grade: C+ (74%)**

#### Specific Issues

1. **Lacks standalone message**: Panel A only makes sense after seeing B/C - violates "self-contained" principle
2. **Both chromosomes grey**: Doesn't foreshadow the maternal/paternal distinction
3. **Question mark** as only visual difference is weak
4. **Variant markers** (triangles) placed arbitrarily; positions don't clearly indicate "same site"

#### Recommendations

1. **Add visual hint** that these chromosomes will be assigned to parents (subtle gradient?)
2. **Align variant markers** more clearly to show they're at the same genomic position
3. **Consider combining** all three panels into a single figure with clear A/B/C labels

---

### Figure 1.2B: Cis Configuration

**File**: `figs/part_1/ch01/02-B-fig-phasing-compound-het.svg` (293×236pt, 44 KB)

#### Scores

| Criterion | Score | Weight | Notes |
|-----------|-------|--------|-------|
| Clarity | B | 25% | Clear once you know pink=maternal |
| Accuracy | A | 25% | Correctly shows both variants on maternal |
| Consistency | B | 20% | Pink/blue gender coding may confuse |
| Accessibility | C | 15% | Pink (#e377c2) and blue (#1f77b4) similar in deuteranopia |
| Integration | A | 15% | Critical for understanding text discussion |

**Weighted Grade: B (82%)**

#### Specific Issues

1. **Pink/blue color convention** assumes reader knows pink=female=maternal, which is a cultural assumption not explained
2. **Green dots** for normal alleles are very small and easy to miss
3. **Colorblind concern**: Pink and blue can be confused in some color vision deficiencies

#### Recommendations

1. **Add pattern fills** or labels (M/P) to distinguish chromosomes without relying solely on color
2. **Make normal allele markers** larger or use a different shape (checkmarks?)
3. **Add "Maternal"/"Paternal" directly on chromosomes** rather than just in left labels

---

### Figure 1.2C: Trans Configuration

**File**: `figs/part_1/ch01/02-C-fig-phasing-compound-het.svg` (293×236pt, 42 KB)

#### Scores

| Criterion | Score | Weight | Notes |
|-----------|-------|--------|-------|
| Clarity | B | 25% | Clear contrast with panel B |
| Accuracy | A | 25% | Correctly shows split variants |
| Consistency | B | 20% | Matches panel B style |
| Accessibility | C | 15% | Same pink/blue colorblind issue |
| Integration | A | 15% | Essential for clinical message |

**Weighted Grade: B (82%)**

#### Specific Issues

Same as Panel B, plus:
1. **Red "AFFECTED" box** creates high visual weight - appropriate given clinical importance
2. **The contrast between green (carrier) and red (affected) boxes** is the strongest teaching element

#### Recommendations

Same as Panel B - add pattern/texture for colorblind accessibility.

---

### Figure 1.3: Error Sources Taxonomy

**File**: `figs/part_1/ch01/03-fig-error-sources.svg` (684×402pt, 99 KB)

#### Scores

| Criterion | Score | Weight | Notes |
|-----------|-------|--------|-------|
| Clarity | B | 25% | Hierarchy clear; bullet points compete |
| Accuracy | A | 25% | Categories correctly organized |
| Consistency | A | 20% | Good use of categorical colors |
| Accessibility | B | 15% | FP (red) and FN (grey) distinguishable |
| Integration | A | 15% | Referenced at line 359-363 |

**Weighted Grade: B+ (85%)**

#### Specific Issues

1. **Bullet point lists compete with tree structure**: Two organizational systems fighting for attention
2. **Sub-nodes** (Instrument Noise, Mapping Ambiguity, etc.) are smaller than they should be
3. **FP/FN badges** are effective but small

#### Recommendations

1. **Remove bullet points** or integrate them as leaves in the tree (expand the hierarchy)
2. **Increase sub-node size** for better hierarchy
3. **Consider a cleaner Mermaid-style tree** without the manual bullet lists

---

### Figure 1.4: Difficult Genomic Regions

**File**: `figs/part_1/ch01/04-fig-difficult-regions.svg` (845×533pt, 123 KB)

#### Scores

| Criterion | Score | Weight | Notes |
|-----------|-------|--------|-------|
| Clarity | C | 25% | Too much information; hard to parse |
| Accuracy | A | 25% | Regions correctly placed |
| Consistency | B | 20% | Colors match palette |
| Accessibility | C | 15% | Many similar colors; small labels |
| Integration | A | 15% | Referenced at line 412-416 |

**Weighted Grade: B- (78%)**

#### Specific Issues

1. **Information overload**: 24 chromosomes + pie chart + long read comparison = too much
2. **Chromosome labels** (1-22, X, Y) are very small
3. **Highlighted regions** are tiny relative to chromosome size - hard to see
4. **Annotations** (HTT, HLA, CYP2D6, FMR1) overlap with chromosomes
5. **Pie chart inset** legend overflows its space

#### Recommendations

1. **Split into two figures**: (a) ideogram with regions, (b) pie chart + long read comparison
2. **Zoom in on key examples** rather than showing all 24 chromosomes at once
3. **Increase chromosome spacing** to allow larger annotation text
4. **Consider a simplified schematic** showing 3-4 key examples in detail

---

### Figure 1.5: DeepVariant Pileup Tensor

**File**: `figs/part_1/ch01/05-fig-deepvariant-pileup.svg` (952×389pt, 114 KB)

#### Scores

| Criterion | Score | Weight | Notes |
|-----------|-------|--------|-------|
| Clarity | B | 25% | Pileup clear; CNN portion oversimplified |
| Accuracy | B | 25% | CNN lacks depth representation |
| Consistency | A | 20% | Good color use |
| Accessibility | B | 15% | Variant (orange/green) distinguishable |
| Integration | A | 15% | Central to section 1.6 |

**Weighted Grade: B (82%)**

#### Specific Issues

1. **CNN architecture oversimplified**: "Conv Layers → Pooling → FC Layers" doesn't show the actual Inception architecture mentioned in text
2. **Pileup tensor lacks channel visualization**: Text mentions "multi-channel tensor" but figure shows single-channel view
3. **Read quality gradient** (alpha transparency) is subtle and easy to miss
4. **Missing strand indicators visualization**: The +/- column is present but not explained in the visual

#### Recommendations

1. **Add channel exploder view**: Show 2-3 of the actual channels (base identity, quality, strand) as separate matrices
2. **Simplify CNN portion** or add "..." to indicate abstraction
3. **Add quality scale** legend to explain the gradient
4. **Label the strand column** more prominently

---

## Grayscale Accessibility Summary

| Figure | Grayscale Safe? | Issue |
|--------|-----------------|-------|
| 1.1 | No | Short/long read paths merge |
| 1.2A | Yes | Grey chromosomes fine |
| 1.2B | No | Pink/blue become similar greys |
| 1.2C | No | Same as B |
| 1.3 | Partial | Blue/orange/green distinguishable |
| 1.4 | No | Many overlapping greys |
| 1.5 | Partial | Variant colors distinguishable |

---

## Recommendations Summary

### Immediate Actions (Before Publication)

1. **Add texture/pattern fills** to 1.2B/C for colorblind accessibility
2. **Increase font sizes** across all figures to minimum 10pt
3. **Split Figure 1.4** into two simpler figures

### High Priority

4. **Revise Figure 1.5** to show actual multi-channel tensor structure
5. **Add shapes** to Figure 1.1 to distinguish file types from processes
6. **Convert bullet lists to tree leaves** in Figure 1.3

### Nice to Have

7. Add grayscale-safe versions for print
8. Create high-contrast versions for accessibility
9. Consider interactive versions for digital edition

---

## Replacement Specs Needed

The following figures warrant revision:

### Figure 1.4: Recommend split

```yaml
figure_id: fig-ch01-difficult-regions-v2
action: split
new_figures:
  - type: ideogram
    focus: "3-4 key examples with zoom insets"
  - type: comparison
    focus: "short vs long read capabilities"
```

### Figure 1.5: Recommend multi-channel view

```yaml
figure_id: fig-ch01-deepvariant-pileup-v2
changes:
  - "Add channel exploder showing 3 tensor channels"
  - "Simplify CNN diagram with '...' for abstracted layers"
  - "Add quality gradient legend"
```

---

## Caption Quality Scores

| Figure | Caption Score (0-6) | Issues |
|--------|---------------------|--------|
| 1.1 | 6/6 | Excellent - comprehensive, interpretive |
| 1.2 | 5/6 | Good - could add genotype notation examples |
| 1.3 | 5/6 | Good - could emphasize the FP/FN distinction more |
| 1.4 | 5/6 | Good - mentions insets appropriately |
| 1.5 | 6/6 | Excellent - explains tensor structure and output |

---

**End of Critique Report**
