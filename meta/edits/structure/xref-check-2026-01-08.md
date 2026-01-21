# Cross-Reference Report

Generated: 2026-01-08
Scope: Entire book (post-restructuring verification)

## Summary

| Metric | Count |
|--------|-------|
| Total cross-references | 1398 |
| Unique referenced sections | 280 |
| Defined sections | 1013 |
| Valid references | 185 (66%) |
| Broken references | 95 (34%) |

**Note**: This report follows the 6→7 part restructuring. Many broken references are forward references to sections not yet written, or legacy references from incomplete refactoring.

---

## Critical Fixes Applied This Session

The following critical issues from restructuring were fixed:

### Part Introduction Headers
- **Part 4**: Changed "Part III" → "Part IV: Foundation Model Families"
- **Part 5**: Changed "Part IV" → "Part V: Cellular Context"
- **Part 6**: Changed "Part V" → "Part VI: Evaluation and Trust"
- **Part 7**: Changed "Part VI" → "Part VII: Clinical Translation"

### Chapter 14 Section IDs
- Fixed 37 occurrences of `{#sec-ch13-*}` → `{#sec-ch14-*}` in FM Principles chapter

### Cross-Reference Updates
- `@sec-ch13-defining` → `@sec-ch14-defining`
- `@sec-ch13-taxonomy` → `@sec-ch14-taxonomy`
- `@sec-ch13-scaling` → `@sec-ch14-scaling`
- `@sec-ch13-task-specific` → `@sec-ch14-task-specific`
- `@sec-ch13-alphagenome` → `@sec-ch17-alphagenome`

### Evaluation Chapter Split (ch11→ch12)
- `@sec-ch11-eval` → `@sec-ch12-eval` (15 files)
- `@sec-ch11-homology-aware-splitting` → `@sec-ch12-homology-aware-splitting` (4 files)
- `@sec-ch11-calibration` → `@sec-ch12-calibration`
- `@sec-ch11-benchmark-leakage` → `@sec-ch12-benchmark-leakage`
- `@sec-ch11-label-leakage` → `@sec-ch12-label-leakage`
- `@sec-ch11-leakage-detection` → `@sec-ch12-leakage-detection`
- `@sec-ch11-metrics-genomic-tasks` → `@sec-ch12-metrics-genomic-tasks`
- `@sec-ch11-discrimination-metrics` → `@sec-ch12-discrimination-metrics`

---

## Broken References (95 total)

### Category 1: DNA-LM Model Sections (5)
These reference specific model subsections that may not exist yet:
- `sec-ch11-caduceus`
- `sec-ch11-evo2`
- `sec-ch11-gpn`
- `sec-ch11-hyenadna`
- `sec-ch11-nucleotide-transformer`

**Suggestion**: These should likely be `@sec-ch15-*` (DNA Language Models chapter)

### Category 2: Old Chapter 12 References (7)
References using old ch12 numbering (now ch13 confounding or moved):
- `sec-ch12-alternative-architectures`
- `sec-ch12-distribution-shift`
- `sec-ch12-emergent-knowledge`
- `sec-ch12-fairness`
- `sec-ch12-population-structure`
- `sec-ch12-structure-vep`
- `sec-ch12-variant-effects`

**Suggestion**: Review each - may need to be ch13 or removed

### Category 3: Old Chapter 13 References (3)
- `sec-ch13-sei`
- `sec-ch14-confounding` (should be `sec-ch13-confounding`)
- `sec-ch14-sei`

### Category 4: Old Chapter 14-15 References (14)
References to FM chapter sections that moved to ch15-16:
- `sec-ch14-borzoi` → should be `@sec-ch17-borzoi`
- `sec-ch15-acmg-mapping`
- `sec-ch15-alignment-models`
- `sec-ch15-calibration`
- `sec-ch15-combining-evidence`
- `sec-ch15-dna-vep`
- `sec-ch15-enformer-vep`
- `sec-ch15-fm-gains`
- `sec-ch15-fm-paradigm`
- `sec-ch15-integration-strategies`
- `sec-ch15-protein-vep`
- `sec-ch15-spliceai`
- `sec-ch15-workflow-design`
- `sec-ch15-zeroshot-plm`
- `sec-ch15-zeroshot-supervised`

### Category 5: Chapter 9 Transfer Learning (8)
Forward references to sections not yet defined:
- `sec-ch09-choosing-strategy`
- `sec-ch09-domain-shift`
- `sec-ch09-domain-shift-types`
- `sec-ch09-emerging-approaches`
- `sec-ch09-evaluation`
- `sec-ch09-full-finetuning`
- `sec-ch09-layer-selection`
- `sec-ch09-zero-shot`

### Category 6: Part 5-7 Forward References (45+)
Many forward references to sections in later chapters that may not be defined yet:
- `sec-ch19-*` (RNA chapter)
- `sec-ch20-*` (Single-cell chapter)
- `sec-ch22-*` (Networks chapter)
- `sec-ch23-*` (Multi-omics chapter)
- `sec-ch24-*` (Uncertainty chapter)
- `sec-ch26-*` (Causal chapter)
- `sec-ch27-*` (Regulatory chapter)
- `sec-ch28-*` (Clinical risk chapter)
- `sec-ch29-*` (Rare disease chapter)
- `sec-ch30-*` (Drug discovery chapter)
- `sec-ch32-*` (Frontiers chapter)

---

## Most Referenced Sections

| Section | Count | Chapter |
|---------|-------|---------|
| `@sec-ch13-confounding` | 63 | Confounding & Leakage |
| `@sec-ch18-vep-fm` | 58 | Variant Effect Prediction (FM) |
| `@sec-ch16-protein-lm` | 49 | Protein Language Models |
| `@sec-ch17-regulatory` | 46 | Regulatory Models |
| `@sec-ch25-interpretability` | 41 | Interpretability |
| `@sec-ch15-dna-lm` | 41 | DNA Language Models |
| `@sec-ch29-rare-disease` | 38 | Rare Disease & Cancer |
| `@sec-ch07-attention` | 38 | Transformers and Attention |
| `@sec-ch08-pretraining` | 33 | Pretraining Objectives |
| `@sec-ch09-transfer` | 32 | Transfer Learning |

---

## Recommendations

### Immediate (High Priority)
1. **Fix `@sec-ch14-confounding` → `@sec-ch13-confounding`** - Direct swap needed
2. **Fix `@sec-ch14-borzoi` → `@sec-ch17-borzoi`** - Wrong chapter
3. **Review ch11 DNA-LM model refs** - May need `@sec-ch15-*` prefix

### Medium Priority
1. Audit all `sec-ch12-*` broken refs - determine if ch13 or removed
2. Add missing section IDs to Chapter 9 (Transfer Learning)
3. Verify Part 5-7 chapter sections exist for forward references

### Low Priority (Content Development)
1. Many broken refs are forward references to content not yet written
2. As chapters are completed, these will resolve naturally
3. Consider marking forward references with TODO comments

---

## Post-Restructuring Verification

The 6→7 part restructuring is structurally complete:

| Component | Status |
|-----------|--------|
| `_quarto.yml` | Correct - 7 parts, 32 chapters |
| Part intro files | Fixed - all show correct part numbers |
| Chapter filenames | Correct - `pN-chXX-topic.qmd` pattern |
| Section IDs (ch14) | Fixed - uses `sec-ch14-*` |
| Bibliography files | Correct - aligned with new structure |
| Figure directories | Correct - aligned with new structure |

The remaining broken references are primarily forward references to undefined sections, not structural issues from the restructuring.

---

*Report generated by xref-check following 6→7 part restructuring*
