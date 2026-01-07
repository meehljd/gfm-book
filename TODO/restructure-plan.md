# Book Restructuring Plan v2.0

**Date:** 2026-01-06
**Status:** Final Draft
**Scope:** Major pedagogical restructuring based on comprehensive review

---

## Executive Summary

This plan restructures the book from 29 chapters in 6 parts to **31 chapters in 6 parts**, implementing the following key changes:

1. **Move evaluation chapters earlier** — Ch20-22 move into Part II (merged into 2 chapters)
2. **Split Ch09** — Transfer Learning becomes two chapters (Foundations + Adaptation)
3. **Add Causal Inference chapter** — New Ch25 bridging trust and clinical application
4. **Split Ch29** — Regulatory/Governance separates from Frontiers
5. **Rename Part IV** — "Systems and Scale" → "Multi-Modal Models"
6. **Rename Part V** — Becomes "Responsible Deployment"
7. **Add bridge content** — Between classical and DL approaches
8. **Add missing concepts** — Cross-species, generative evaluation, efficiency

---

## Structure Comparison

### Current Structure (29 chapters, 6 parts)

```
Part I:   Data Foundations (Ch01-04)                    4 chapters
Part II:  Sequence Architectures (Ch05-09)              5 chapters
Part III: Foundation Model Families (Ch10-14)           5 chapters
Part IV:  Systems and Scale (Ch15-19)                   5 chapters
Part V:   Evaluation and Trust (Ch20-24)                5 chapters
Part VI:  Clinical Translation (Ch25-29)                5 chapters
```

### Target Structure (31 chapters, 6 parts)

```
Part I:   Data Foundations (Ch01-04)                    4 chapters
Part II:  Learning & Evaluation (Ch05-12)               8 chapters  ← expanded
Part III: Foundation Model Families (Ch13-17)           5 chapters  ← renumbered
Part IV:  Multi-Modal Models (Ch18-22)                  5 chapters  ← renamed
Part V:   Responsible Deployment (Ch23-26)              4 chapters  ← new content
Part VI:  Applications & Frontiers (Ch27-31)            5 chapters  ← restructured
```

---

## Complete Chapter Map

### Part I: Data Foundations (unchanged)

| New # | Old # | Title | Changes |
|-------|-------|-------|---------|
| Ch01 | Ch01 | Next-Generation Sequencing | None |
| Ch02 | Ch02 | Genomic Data Resources | None |
| Ch03 | Ch03 | GWAS and Polygenic Scores | None |
| Ch04 | Ch04 | Classical Variant Effect Prediction | + Bridge section at end |

### Part II: Learning & Evaluation (expanded from 5 to 8 chapters)

| New # | Old # | Title | Changes |
|-------|-------|-------|---------|
| Ch05 | Ch05 | Sequence Representations | None |
| Ch06 | Ch06 | Convolutional Architectures | None |
| Ch07 | Ch07 | Attention Mechanisms | None |
| Ch08 | Ch08 | Pretraining Strategies | None |
| Ch09 | Ch09 (part) | Transfer Learning Foundations | **SPLIT** - conceptual foundations |
| Ch10 | Ch09 (part) | Adaptation Strategies | **SPLIT** - practical methods |
| Ch11 | Ch20+Ch21 | Benchmarks & Evaluation | **MERGED + MOVED** from Part V |
| Ch12 | Ch22 | Confounding & Data Leakage | **MOVED** from Part V |

### Part III: Foundation Model Families (renumbered)

| New # | Old # | Title | Changes |
|-------|-------|-------|---------|
| Ch13 | Ch10 | Foundation Model Principles | Renumbered |
| Ch14 | Ch11 | DNA Language Models | + Cross-species section |
| Ch15 | Ch12 | Protein Language Models | Renumbered |
| Ch16 | Ch13 | Regulatory Sequence Models | Renumbered |
| Ch17 | Ch14 | Variant Effect Prediction with FMs | + Long-read section |

### Part IV: Multi-Modal Models (renamed from "Systems and Scale")

| New # | Old # | Title | Changes |
|-------|-------|-------|---------|
| Ch18 | Ch15 | RNA Structure and Function | Renumbered |
| Ch19 | Ch16 | Single-Cell Foundation Models | Renumbered |
| Ch20 | Ch17 | 3D Genome Organization | Renumbered |
| Ch21 | Ch18 | Networks and Graph Models | Renumbered |
| Ch22 | Ch19 | Multi-Omics Integration | Renumbered |

### Part V: Responsible Deployment (new title, restructured)

| New # | Old # | Title | Changes |
|-------|-------|-------|---------|
| Ch23 | Ch23 | Uncertainty & Calibration | Renumbered only |
| Ch24 | Ch24 | Interpretability | Renumbered only |
| Ch25 | NEW | Causal Inference with FMs | **NEW CHAPTER** |
| Ch26 | Ch29 (part) | Regulatory & Governance | **SPLIT** from old Ch29 |

### Part VI: Applications & Frontiers (restructured)

| New # | Old # | Title | Changes |
|-------|-------|-------|---------|
| Ch27 | Ch25 | Clinical Risk Prediction | Renumbered |
| Ch28 | Ch26 | Rare Disease Diagnosis | Renumbered |
| Ch29 | Ch27 | Drug Discovery | + Causal target section |
| Ch30 | Ch28 | Sequence Design | + Generative evaluation, active learning |
| Ch31 | Ch29 (part) | Frontiers & Synthesis | **SPLIT** from old Ch29 |

---

## Detailed Change Specifications

### Change 1: Split Ch09 (Transfer Learning)

**Current:** Single chapter, 13,173 words, 45 subsections (largest in book)

**Split into:**

**Ch09: Transfer Learning Foundations (~6,000 words)**
- Source and target domain concepts
- Task relatedness and transferability
- Distribution shift in genomics
- When transfer helps vs. hurts
- Theoretical foundations

**Ch10: Adaptation Strategies (~7,000 words)**
- Fine-tuning approaches
- Low-Rank Adaptation (LoRA)
- Adapter modules
- Prompt tuning
- Few-shot and zero-shot learning
- Practical deployment considerations

**Rationale:** Conceptual foundations (researchers) vs. practical methods (practitioners)

---

### Change 2: Merge Ch20+Ch21, Move to Part II

**Current:**
- Ch20: Benchmarks (6,664 words) — surveys existing benchmarks
- Ch21: Evaluation Principles (7,465 words) — how to use benchmarks properly

**Merged into:**

**Ch11: Benchmarks & Evaluation (~10,000 words)**
- Benchmark landscape (from Ch20)
- Benchmark design principles (from Ch20)
- Evaluation methodology (from Ch21)
- Metrics and their limitations (from Ch21)
- Homology-aware splitting (from Ch21)
- Proper train/val/test splits (from Ch21)

**Rationale:** These are "Part A and Part B" of the same topic. Merging creates a comprehensive evaluation reference. Moving to Part II enables critical reading of Parts III-IV.

---

### Change 3: Move Ch22 (Confounding) to Part II

**Becomes:** Ch12: Confounding & Data Leakage

**Content:** Unchanged, but now positioned before model chapters

**Rationale:** Confounding concepts (ancestry stratification, batch effects, label bias) are needed to critically evaluate model performance claims in Parts III-IV.

---

### Change 4: New Chapter — Causal Inference with FMs

**New Ch25: Causal Inference with Foundation Models (~7,000 words)**

**Outline:**

1. **Prediction vs. Causation**
   - The ladder of causation
   - Why predictive accuracy ≠ causal understanding
   - The clinical stakes: intervention requires causation

2. **Causal Methods in Genomics**
   - Mendelian randomization (expanded from Ch03)
   - Fine-mapping for causal variants
   - GWAS → causal genes pipeline

3. **Foundation Models and Causality**
   - Can FMs learn causal structure?
   - In-silico perturbation prediction
   - Counterfactual reasoning limitations
   - The correlation-causation gap in embeddings

4. **Intervention Prediction**
   - CRISPR screen analysis with FMs
   - Drug response prediction
   - Closed-loop experimental validation

5. **Causal Discovery**
   - Learning regulatory networks
   - Temporal causality
   - Multi-omics causal structure

6. **Clinical Implications**
   - Drug target validation evidence
   - Regulatory requirements for causal claims
   - From association to mechanism

**Placement rationale:** Bridges "can we trust predictions?" (Ch23-24) and "should we act on them?" (Ch27-31)

---

### Change 5: Split Ch29 (Future/Ethics)

**Current Ch29 covers:**
- Regulatory frameworks (FDA, CE, SaMD)
- Data governance (consent, privacy, IP)
- Equity and fairness
- Open problems and future directions
- Closing remarks

**Split into:**

**Ch26: Regulatory & Governance (~5,000 words)**
- FDA pathways for AI/ML medical devices
- EU MDR and CE marking
- Software as Medical Device (SaMD) classification
- Data consent frameworks (GDPR, HIPAA)
- Privacy-preserving approaches
- Intellectual property considerations
- Equity and fairness requirements

**Ch31: Frontiers & Synthesis (~4,000 words)**
- Open technical problems
- Emerging research directions
- Responsible development principles
- Synthesis of book themes
- The road ahead

**Rationale:** Regulatory knowledge is a deployment prerequisite (Part V); future directions are a capstone (Part VI)

---

### Change 6: Bridge Section — From Features to Representations

**Location:** End of Ch04 or beginning of Ch05

**Title:** "From Features to Representations: Why Deep Learning?"

**Content (~2,500 words):**

1. **Limitations of Hand-Crafted Features**
   - Conservation scores require evolutionary assumptions
   - Domain annotations need curated databases
   - Feature interactions are hard to specify
   - Long-range dependencies are missed

2. **The Representation Learning Paradigm**
   - Let the model learn what matters
   - End-to-end training from sequence to prediction
   - From Grantham distance to learned embeddings

3. **What Changes with Deep Learning**
   - Data requirements increase
   - Interpretability challenges emerge
   - Scalability becomes possible
   - Transfer learning enables generalization

4. **Preview of Part II**
   - Tokenization and embedding
   - Architectural choices (CNN, attention)
   - Learning from unlabeled data

---

### Change 7: Content Additions to Existing Chapters

#### Ch14 (DNA Language Models): Cross-Species Modeling Section

**Add section (~1,500 words):**
- Multi-species pretraining strategies
- Conservation vs. species-specific patterns
- Cross-species transfer methodology
- Applications beyond human genomics
- Trade-offs: diversity vs. human performance

#### Ch17 (VEP with FMs): Long-Read Implications Section

**Add section (~1,000 words):**
- Long-read variant calling with DL
- Structural variant interpretation
- Phasing and haplotype-aware analysis
- Training FMs on long-read data

#### Ch29 (Drug Discovery): Causal Target Section

**Expand existing content (~500 words):**
- Strengthen connection to Ch25 (Causal Inference)
- Causal evidence for target validation
- Beyond association: intervention prediction

#### Ch30 (Sequence Design): Generative Evaluation + Active Learning

**Add sections (~1,500 words total):**

*Generative Evaluation (~800 words):*
- How do we know generated sequences are good?
- Metrics: perplexity, novelty, validity, diversity
- Experimental validation strategies

*Active Learning (~700 words):*
- Model-guided experimental design
- Uncertainty-based prioritization
- The design-test-learn cycle

---

### Change 8: Appendix B Development

**Current:** Placeholder (6 words)

**Develop into:** "Model Efficiency & Practical Deployment" (~5,000 words)

**Outline:**

1. **Model Compression**
   - Knowledge distillation
   - Quantization (INT8, INT4)
   - Pruning strategies
   - Compact architectures

2. **Inference Optimization**
   - Batching strategies
   - KV-cache optimization
   - Flash attention
   - Speculative decoding

3. **Deployment Environments**
   - Cloud deployment (AWS, GCP, Azure)
   - On-premise considerations
   - Edge deployment for point-of-care
   - Container orchestration

4. **Practical Recipes**
   - ESM-2 inference optimization
   - Enformer memory management
   - Batch processing pipelines
   - Cost estimation

---

## File Operations

### Phase 2A: Create New Files

```bash
# New chapters (create from templates)
touch part_2/p2-ch10-adaptation.qmd      # Split from Ch09
touch part_2/p2-ch11-benchmarks.qmd      # Merged Ch20+Ch21
touch part_2/p2-ch12-confounding.qmd     # Moved Ch22
touch part_5/p5-ch25-causal.qmd          # New chapter
touch part_5/p5-ch26-regulatory.qmd      # Split from Ch29
touch part_6/p6-ch31-frontiers.qmd       # Split from Ch29

# New bib files
touch bib/p2/p2-ch10.bib
touch bib/p2/p2-ch11.bib
touch bib/p2/p2-ch12.bib
touch bib/p5/p5-ch25.bib
touch bib/p5/p5-ch26.bib
touch bib/p6/p6-ch31.bib
```

### Phase 2B: Move and Rename Existing Files

```bash
# Part 3: Ch10-14 → Ch13-17 (reverse order to avoid conflicts)
git mv part_3/p3-ch14-vep-fm.qmd part_3/p3-ch17-vep-fm.qmd
git mv part_3/p3-ch13-regulatory.qmd part_3/p3-ch16-regulatory.qmd
git mv part_3/p3-ch12-protein-lm.qmd part_3/p3-ch15-protein-lm.qmd
git mv part_3/p3-ch11-dna-lm.qmd part_3/p3-ch14-dna-lm.qmd
git mv part_3/p3-ch10-fm-principles.qmd part_3/p3-ch13-fm-principles.qmd

# Part 3 bib files
git mv bib/p3/p3-ch14.bib bib/p3/p3-ch17.bib
git mv bib/p3/p3-ch13.bib bib/p3/p3-ch16.bib
git mv bib/p3/p3-ch12.bib bib/p3/p3-ch15.bib
git mv bib/p3/p3-ch11.bib bib/p3/p3-ch14.bib
git mv bib/p3/p3-ch10.bib bib/p3/p3-ch13.bib

# Part 4: Ch15-19 → Ch18-22 (reverse order)
git mv part_4/p4-ch19-multi-omics.qmd part_4/p4-ch22-multi-omics.qmd
git mv part_4/p4-ch18-networks.qmd part_4/p4-ch21-networks.qmd
git mv part_4/p4-ch17-3d-genome.qmd part_4/p4-ch20-3d-genome.qmd
git mv part_4/p4-ch16-single-cell.qmd part_4/p4-ch19-single-cell.qmd
git mv part_4/p4-ch15-rna.qmd part_4/p4-ch18-rna.qmd

# Part 4 bib files
git mv bib/p4/p4-ch19.bib bib/p4/p4-ch22.bib
git mv bib/p4/p4-ch18.bib bib/p4/p4-ch21.bib
git mv bib/p4/p4-ch17.bib bib/p4/p4-ch20.bib
git mv bib/p4/p4-ch16.bib bib/p4/p4-ch19.bib
git mv bib/p4/p4-ch15.bib bib/p4/p4-ch18.bib

# Part 6: Ch25-28 → Ch27-30
git mv part_6/p6-ch28-design.qmd part_6/p6-ch30-design.qmd
git mv part_6/p6-ch27-drug-discovery.qmd part_6/p6-ch29-drug-discovery.qmd
git mv part_6/p6-ch26-rare-disease.qmd part_6/p6-ch28-rare-disease.qmd
git mv part_6/p6-ch25-clinical-risk.qmd part_6/p6-ch27-clinical-risk.qmd

# Part 6 bib files
git mv bib/p6/p6-ch28.bib bib/p6/p6-ch30.bib
git mv bib/p6/p6-ch27.bib bib/p6/p6-ch29.bib
git mv bib/p6/p6-ch26.bib bib/p6/p6-ch28.bib
git mv bib/p6/p6-ch25.bib bib/p6/p6-ch27.bib

# Rename part intro files
git mv part_4/p4--multi-scale.qmd part_4/p4--multi-modal.qmd
git mv part_5/p5--eval-interp.qmd part_5/p5--responsible-deployment.qmd
git mv part_6/p6--translation.qmd part_6/p6--applications.qmd
```

### Phase 2C: Delete Obsolete Files (after content merged)

```bash
# These files' content will be merged into new files, then deleted
# part_5/p5-ch20-benchmarks.qmd → merged into p2-ch11-benchmarks.qmd
# part_5/p5-ch21-eval.qmd → merged into p2-ch11-benchmarks.qmd
# part_5/p5-ch22-confounding.qmd → moved to p2-ch12-confounding.qmd
# part_6/p6-ch29-future.qmd → split into p5-ch26-regulatory.qmd and p6-ch31-frontiers.qmd

git rm part_5/p5-ch20-benchmarks.qmd  # after merge
git rm part_5/p5-ch21-eval.qmd        # after merge
git rm part_5/p5-ch22-confounding.qmd # after move
git rm part_6/p6-ch29-future.qmd      # after split

git rm bib/p5/p5-ch20.bib  # after merge
git rm bib/p5/p5-ch21.bib  # after merge
git rm bib/p5/p5-ch22.bib  # after move
git rm bib/p6/p6-ch29.bib  # after split
```

---

## Updated _quarto.yml

```yaml
book:
  title: "Genomic Foundation Models"
  author: "Josh Meehl"
  date: "1/6/2026"
  page-footer: "Copyright 2025-2026, Josh Meehl"
  chapters:
    - index.qmd
    - preface.qmd

    # Part I: Data Foundations
    - part: "part_1/p1--foundations.qmd"
      chapters:
        - part_1/p1-ch01-ngs.qmd
        - part_1/p1-ch02-data.qmd
        - part_1/p1-ch03-gwas.qmd
        - part_1/p1-ch04-vep-classical.qmd

    # Part II: Learning & Evaluation
    - part: "part_2/p2--principles.qmd"
      chapters:
        - part_2/p2-ch05-representations.qmd
        - part_2/p2-ch06-cnn.qmd
        - part_2/p2-ch07-attention.qmd
        - part_2/p2-ch08-pretraining.qmd
        - part_2/p2-ch09-transfer.qmd           # Foundations (split)
        - part_2/p2-ch10-adaptation.qmd         # Strategies (split)
        - part_2/p2-ch11-benchmarks.qmd         # Merged Ch20+21
        - part_2/p2-ch12-confounding.qmd        # Moved Ch22

    # Part III: Foundation Model Families
    - part: "part_3/p3--architectures.qmd"
      chapters:
        - part_3/p3-ch13-fm-principles.qmd
        - part_3/p3-ch14-dna-lm.qmd
        - part_3/p3-ch15-protein-lm.qmd
        - part_3/p3-ch16-regulatory.qmd
        - part_3/p3-ch17-vep-fm.qmd

    # Part IV: Multi-Modal Models
    - part: "part_4/p4--multi-modal.qmd"
      chapters:
        - part_4/p4-ch18-rna.qmd
        - part_4/p4-ch19-single-cell.qmd
        - part_4/p4-ch20-3d-genome.qmd
        - part_4/p4-ch21-networks.qmd
        - part_4/p4-ch22-multi-omics.qmd

    # Part V: Responsible Deployment
    - part: "part_5/p5--responsible-deployment.qmd"
      chapters:
        - part_5/p5-ch23-uncertainty.qmd
        - part_5/p5-ch24-interpretability.qmd
        - part_5/p5-ch25-causal.qmd             # NEW
        - part_5/p5-ch26-regulatory.qmd         # Split from Ch29

    # Part VI: Applications & Frontiers
    - part: "part_6/p6--applications.qmd"
      chapters:
        - part_6/p6-ch27-clinical-risk.qmd
        - part_6/p6-ch28-rare-disease.qmd
        - part_6/p6-ch29-drug-discovery.qmd
        - part_6/p6-ch30-design.qmd
        - part_6/p6-ch31-frontiers.qmd          # Split from Ch29

  appendices:
    - appendix/app-a-dl.qmd
    - appendix/app-b-compute.qmd                # DEVELOP
    - appendix/app-c-data-curation.qmd
    - appendix/app-d-models.qmd
    - appendix/app-e-resources.qmd
    - appendix/app-f-glossary.qmd
  references: bib/references.qmd

bibliography:
  # Part 1
  - bib/p1/p1-ch01.bib
  - bib/p1/p1-ch02.bib
  - bib/p1/p1-ch03.bib
  - bib/p1/p1-ch04.bib
  # Part 2
  - bib/p2/p2-ch05.bib
  - bib/p2/p2-ch06.bib
  - bib/p2/p2-ch07.bib
  - bib/p2/p2-ch08.bib
  - bib/p2/p2-ch09.bib
  - bib/p2/p2-ch10.bib
  - bib/p2/p2-ch11.bib
  - bib/p2/p2-ch12.bib
  # Part 3
  - bib/p3/p3-ch13.bib
  - bib/p3/p3-ch14.bib
  - bib/p3/p3-ch15.bib
  - bib/p3/p3-ch16.bib
  - bib/p3/p3-ch17.bib
  # Part 4
  - bib/p4/p4-ch18.bib
  - bib/p4/p4-ch19.bib
  - bib/p4/p4-ch20.bib
  - bib/p4/p4-ch21.bib
  - bib/p4/p4-ch22.bib
  # Part 5
  - bib/p5/p5-ch23.bib
  - bib/p5/p5-ch24.bib
  - bib/p5/p5-ch25.bib
  - bib/p5/p5-ch26.bib
  # Part 6
  - bib/p6/p6-ch27.bib
  - bib/p6/p6-ch28.bib
  - bib/p6/p6-ch29.bib
  - bib/p6/p6-ch30.bib
  - bib/p6/p6-ch31.bib
  # Appendices
  - bib/apx/app-a.bib
  - bib/apx/app-b.bib
  - bib/apx/app-c.bib
  - bib/apx/app-d.bib
  - bib/apx/app-e.bib
  - bib/apx/app-f.bib
```

---

## Cross-Reference Update Strategy

### Section Label Changes

| Old Label | New Label |
|-----------|-----------|
| `sec-ch09-transfer` | `sec-ch09-transfer` (keep for foundations) |
| — | `sec-ch10-adaptation` (new for split) |
| `sec-ch20-benchmarks` | `sec-ch11-benchmarks` |
| `sec-ch21-eval` | `sec-ch11-benchmarks` (merged) |
| `sec-ch22-confounding` | `sec-ch12-confounding` |
| `sec-ch10-fm-principles` | `sec-ch13-fm-principles` |
| `sec-ch11-dna-lm` | `sec-ch14-dna-lm` |
| `sec-ch12-protein-lm` | `sec-ch15-protein-lm` |
| `sec-ch13-regulatory` | `sec-ch16-regulatory` |
| `sec-ch14-vep-fm` | `sec-ch17-vep-fm` |
| `sec-ch15-rna` | `sec-ch18-rna` |
| `sec-ch16-single-cell` | `sec-ch19-single-cell` |
| `sec-ch17-3d-genome` | `sec-ch20-3d-genome` |
| `sec-ch18-networks` | `sec-ch21-networks` |
| `sec-ch19-multi-omics` | `sec-ch22-multi-omics` |
| `sec-ch23-uncertainty` | `sec-ch23-uncertainty` (unchanged) |
| `sec-ch24-interpretability` | `sec-ch24-interpretability` (unchanged) |
| — | `sec-ch25-causal` (new) |
| `sec-ch29-future` (part) | `sec-ch26-regulatory` (split) |
| `sec-ch25-clinical-risk` | `sec-ch27-clinical-risk` |
| `sec-ch26-rare-disease` | `sec-ch28-rare-disease` |
| `sec-ch27-drug-discovery` | `sec-ch29-drug-discovery` |
| `sec-ch28-design` | `sec-ch30-design` |
| `sec-ch29-future` (part) | `sec-ch31-frontiers` (split) |

### Find-Replace Order (Critical!)

Execute in this exact order to avoid conflicts:

```bash
# Phase 1: Moved/merged chapters (do FIRST)
sed -i 's/@sec-ch20-/@sec-ch11-/g' **/*.qmd
sed -i 's/@sec-ch21-/@sec-ch11-/g' **/*.qmd  # Merge into ch11
sed -i 's/@sec-ch22-/@sec-ch12-/g' **/*.qmd

# Phase 2: Renumber Parts 3-4 (use temp markers to avoid collision)
sed -i 's/@sec-ch10-fm/@sec-ch13-fm/g' **/*.qmd
sed -i 's/@sec-ch11-dna/@sec-ch14-dna/g' **/*.qmd
sed -i 's/@sec-ch12-protein/@sec-ch15-protein/g' **/*.qmd
sed -i 's/@sec-ch13-regulatory/@sec-ch16-regulatory/g' **/*.qmd
sed -i 's/@sec-ch14-vep/@sec-ch17-vep/g' **/*.qmd

sed -i 's/@sec-ch15-rna/@sec-ch18-rna/g' **/*.qmd
sed -i 's/@sec-ch16-single/@sec-ch19-single/g' **/*.qmd
sed -i 's/@sec-ch17-3d/@sec-ch20-3d/g' **/*.qmd
sed -i 's/@sec-ch18-networks/@sec-ch21-networks/g' **/*.qmd
sed -i 's/@sec-ch19-multi/@sec-ch22-multi/g' **/*.qmd

# Phase 3: Renumber Part 6
sed -i 's/@sec-ch25-clinical/@sec-ch27-clinical/g' **/*.qmd
sed -i 's/@sec-ch26-rare/@sec-ch28-rare/g' **/*.qmd
sed -i 's/@sec-ch27-drug/@sec-ch29-drug/g' **/*.qmd
sed -i 's/@sec-ch28-design/@sec-ch30-design/g' **/*.qmd

# Phase 4: Handle split Ch29 (manual review needed)
# @sec-ch29-future references need to be routed to either:
# - @sec-ch26-regulatory (if about governance)
# - @sec-ch31-frontiers (if about future)
```

---

## Content Writing Requirements

### New Content to Write

| Content | Location | Est. Words | Priority |
|---------|----------|------------|----------|
| Bridge: From Features to Representations | End of Ch04 | 2,500 | High |
| Ch10: Adaptation Strategies | New file | 7,000 | High |
| Ch11: Benchmarks & Evaluation | Merge + edit | 10,000 | High |
| Ch25: Causal Inference | New file | 7,000 | High |
| Ch26: Regulatory & Governance | Split from Ch29 | 5,000 | High |
| Ch31: Frontiers & Synthesis | Split from Ch29 | 4,000 | High |
| Cross-species section | Add to Ch14 | 1,500 | Medium |
| Long-read section | Add to Ch17 | 1,000 | Medium |
| Generative evaluation | Add to Ch30 | 800 | Medium |
| Active learning | Add to Ch30 | 700 | Medium |
| Appendix B | Develop from stub | 5,000 | Medium |

**Total new writing:** ~45,000 words

### Content to Edit/Split

| Content | Action | Est. Effort |
|---------|--------|-------------|
| Ch09: Transfer Learning | Split into Ch09 + Ch10 | Medium |
| Ch20 + Ch21 | Merge, relocate | Medium |
| Ch22 | Relocate, update refs | Low |
| Ch29 | Split into Ch26 + Ch31 | Medium |
| Part intro files | Update titles, content | Low |

---

## Execution Phases

### Phase 1: Preparation
- [ ] Create backup branch
- [ ] Run `/xref-check` baseline
- [ ] Commit all pending changes

### Phase 2: File Operations
- [ ] Create new empty files
- [ ] Execute git mv commands (Parts 3, 4, 6)
- [ ] Rename part intro files
- [ ] Create new bib files

### Phase 3: Update _quarto.yml
- [ ] Update chapter list
- [ ] Update bibliography list
- [ ] Verify quarto can parse

### Phase 4: Cross-Reference Updates
- [ ] Execute sed replacements in order
- [ ] Manual review of Ch29 splits
- [ ] Run `/xref-check` to verify

### Phase 5: Content Work
- [ ] Write bridge section (Ch04)
- [ ] Split Ch09 content
- [ ] Merge Ch20+Ch21 content
- [ ] Move Ch22 content
- [ ] Write Ch25 (Causal Inference)
- [ ] Split Ch29 into Ch26 + Ch31
- [ ] Add cross-species section (Ch14)
- [ ] Add long-read section (Ch17)
- [ ] Add generative/active learning (Ch30)
- [ ] Develop Appendix B

### Phase 6: Validation
- [ ] Run `/xref-check`
- [ ] Run `quarto render`
- [ ] Visual inspection of TOC
- [ ] Review navigation flow

---

## Success Criteria

- [ ] 31 chapters render correctly
- [ ] All cross-references resolve
- [ ] Part titles display correctly
- [ ] Navigation works in rendered book
- [ ] No broken internal links
- [ ] Bibliography compiles

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Broken cross-references | Systematic sed order; validate after each phase |
| Git history loss | Use `git mv`; commit frequently |
| Build failures | Test after each phase |
| Content loss in merges | Work on copies; diff against originals |
| Scope creep in new chapters | Strict word count targets |

### Rollback

```bash
git checkout main
git branch -D restructure/v2
```

---

## Appendix: Visual Structure

```
GENOMIC FOUNDATION MODELS
│
├── PART I: DATA FOUNDATIONS (4)
│   ├── Ch01: Next-Generation Sequencing
│   ├── Ch02: Genomic Data Resources
│   ├── Ch03: GWAS and Polygenic Scores
│   └── Ch04: Classical VEP [+bridge]
│
├── PART II: LEARNING & EVALUATION (8)
│   ├── Ch05: Sequence Representations
│   ├── Ch06: Convolutional Architectures
│   ├── Ch07: Attention Mechanisms
│   ├── Ch08: Pretraining Strategies
│   ├── Ch09: Transfer Learning Foundations [split]
│   ├── Ch10: Adaptation Strategies [split]
│   ├── Ch11: Benchmarks & Evaluation [merged+moved]
│   └── Ch12: Confounding & Leakage [moved]
│
├── PART III: FOUNDATION MODEL FAMILIES (5)
│   ├── Ch13: Foundation Model Principles
│   ├── Ch14: DNA Language Models [+cross-species]
│   ├── Ch15: Protein Language Models
│   ├── Ch16: Regulatory Sequence Models
│   └── Ch17: VEP with Foundation Models [+long-read]
│
├── PART IV: MULTI-MODAL MODELS (5)
│   ├── Ch18: RNA Structure and Function
│   ├── Ch19: Single-Cell Foundation Models
│   ├── Ch20: 3D Genome Organization
│   ├── Ch21: Networks and Graph Models
│   └── Ch22: Multi-Omics Integration
│
├── PART V: RESPONSIBLE DEPLOYMENT (4)
│   ├── Ch23: Uncertainty & Calibration
│   ├── Ch24: Interpretability
│   ├── Ch25: Causal Inference [NEW]
│   └── Ch26: Regulatory & Governance [split]
│
├── PART VI: APPLICATIONS & FRONTIERS (5)
│   ├── Ch27: Clinical Risk Prediction
│   ├── Ch28: Rare Disease Diagnosis
│   ├── Ch29: Drug Discovery
│   ├── Ch30: Sequence Design [+gen eval, active learning]
│   └── Ch31: Frontiers & Synthesis [split]
│
└── APPENDICES
    ├── App A: Deep Learning Primer
    ├── App B: Model Efficiency & Deployment [DEVELOP]
    ├── App C: Data Curation
    ├── App D: Model Reference
    ├── App E: Resources
    └── App F: Glossary
```
