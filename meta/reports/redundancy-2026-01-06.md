# Redundancy Analysis Report

Generated: 2026-01-06
Scope: Entire book

## Summary

| Metric | Count |
|--------|------:|
| Concepts appearing in 3+ chapters | 14 |
| High-overlap passages | 6 |
| Consolidation opportunities | 8 |
| Cross-reference suggestions | 12 |
| Well-handled cross-refs | 15+ |

**Overall Assessment**: The book generally handles cross-references well. Most multi-chapter concepts properly designate a "primary" chapter and reference it elsewhere. However, several areas from TODO/notes.md require attention.

## Redundancy by Concept

### 1. ClinVar Database

**Appears in**: 20 files (~95 mentions)
- Ch2 (lines 262-297): Primary explanation of database, biases, ACMG
- Ch4 (lines 236-247): Usage in classical VEP
- Ch14 (various): VEP evaluation context
- Ch20 (lines 119-125): Benchmark usage
- Ch22 (various): Confounding/leakage context
- Ch23 (lines 103, 367-383): Uncertainty context

**Overlap level**: Low (appropriate distribution)
**Recommendation**: Ch2 owns the concept; others reference appropriately
**Status**: GOOD - Cross-references present

### 2. Masked Language Modeling (MLM)

**Appears in**: 14 files (~37 mentions)
- Ch8 (lines 18-110): **PRIMARY** - Detailed explanation
- Ch10 (lines 144, 290): Summary context
- Ch11 (lines 22-61): DNA-specific application
- Ch12 (lines 24, 176): Protein-specific application
- Ch15 (line 126): RNA application
- Ch16 (line 19): Single-cell context

**Overlap level**: Medium
**Recommendation**: Ch8 should be primary source; Ch11/12/15/16 should briefly introduce domain-specific aspects with cross-refs

**Suggested changes**:
- Ch11: Add explicit `(@sec-ch08-mlm)` reference when introducing MLM for DNA
- Ch12: Add explicit `(@sec-ch08-mlm)` reference for protein MLM
- Ch15: Already has appropriate brief mention with context

### 3. Calibration Methods (Temperature/Platt Scaling)

**Appears in**: 7 files (~175 mentions of "calibration")
- Ch23 (lines 125-232): **PRIMARY** - Detailed calibration methods
- Ch14 (line 189): Brief mention with cross-ref to Ch23
- Ch21 (lines 18-19, 362-370): Evaluation context
- Ch25 (lines 150, 186): Clinical application

**Overlap level**: Low (well cross-referenced)
**Recommendation**: Already well-handled
**Status**: GOOD - Ch14 explicitly references `@sec-ch23-post-hoc-calibration`

### 4. Attention Mechanism / Transformers

**Appears in**: 15+ files (~38 "attention mechanism" mentions, ~195 "transformer" mentions)
- Ch7 (lines 7-349): **PRIMARY** - Detailed transformer explanation
- Ch10 (various): FM context with cross-refs
- Ch11-13 (various): Model-specific applications
- Ch6 (line 235): CNN vs attention comparison

**Overlap level**: Low (appropriate)
**Recommendation**: Ch7 owns the concept; model chapters appropriately apply it
**Status**: GOOD - Most chapters reference `@sec-ch07-attention`

### 5. Population Stratification / Ancestry Confounding

**Appears in**: 13 files (~40+ mentions)
- Ch22 (lines 35-68): **PRIMARY** - `@sec-ch22-ancestry-confounding`
- Ch2 (lines 76-97): Data biases introduction
- Ch3 (lines 65-69, 290): GWAS context
- Ch25 (lines 196-198): Clinical deployment
- Ch11 (line 246): Training data bias
- Ch14 (line 291): VEP context

**Overlap level**: Low (well cross-referenced)
**Recommendation**: Already well-handled
**Status**: GOOD - Ch22 is consistently referenced via `@sec-ch22-ancestry-confounding`

### 6. Zero-Shot Prediction

**Appears in**: 13 files (~35 mentions)
- Ch9 (lines 21-241): **PRIMARY** - Transfer learning context
- Ch14 (lines 158-163): VEP application
- Ch11 (lines 66-70): DNA LM context
- Ch12 (lines 176-204): Protein LM context
- Ch21 (line 325): Evaluation context

**Overlap level**: HIGH
**Recommendation**: Per TODO/notes.md, Ch14 should not repeat Ch9/Ch12 content
**Action Required**:
- Ch14: Replace detailed zero-shot explanation with cross-refs to `@sec-ch09-transfer` and `@sec-ch12-variant-effects`
- TODO note (line 162): "Be sure not to repeat ch12 and ch09 on zero-shot prediction"

### 7. Batch Effects

**Appears in**: 13 files (~36 mentions)
- Ch22 (lines 33, various): **PRIMARY** - General confounding
- Ch16 (line 227+): Single-cell specific
- Ch19 (line 11+): Multi-omics specific
- Ch2 (line 1): Data introduction

**Overlap level**: Medium
**Recommendation**: Per xref-check report, Ch16 and Ch19 should reference Ch22 as primary
**Suggested changes**:
- Ch16: Add `(@sec-ch22-batch-effects)` for general batch effect discussion
- Ch19: Add `(@sec-ch22-batch-effects)` for general batch effect discussion

### 8. Deep Mutational Scanning (DMS)

**Appears in**: 12 files
- Ch2 (lines 156-160): **PRIMARY** - `@sec-ch02-dms`
- Ch20 (lines 137-141): Benchmark context
- Ch14 (various): VEP evaluation
- Ch23 (lines 29, 103): Uncertainty context
- Ch12 (line 195): Protein context

**Overlap level**: Low (appropriate)
**Recommendation**: Ch2 introduces, Ch20 details benchmarks; others reference appropriately
**Status**: GOOD

### 9. ACMG-AMP Guidelines

**Appears in**: 8 files
- Ch14 (lines 209-213): **PRIMARY** for model mapping - `@sec-ch14-acmg-mapping`
- Ch4 (line 66): Classical VEP intro
- Ch26 (lines 43-75): Clinical application
- Ch2 (lines 262, 297): Data context

**Overlap level**: Low
**Recommendation**: Ch14 owns model-to-ACMG mapping; Ch26 owns clinical application
**Note**: TODO/notes.md (line 184) requests ACMG sidebar - verify not already done
**Status**: GOOD but could add cross-refs

### 10. Enformer Model

**Appears in**: 22 files (~79 mentions)
- Ch13 (lines 35-80): **PRIMARY** - `@sec-ch13-enformer`
- Ch14 (lines 110-114): VEP application
- Ch7 (lines 269-340): Attention context
- Various other mentions

**Overlap level**: Low (well cross-referenced)
**Status**: GOOD - Ch13 is consistently referenced

### 11. SpliceAI Model

**Appears in**: 15 files
- Ch6 (lines 130-193): **PRIMARY** - `@sec-ch06-spliceai`
- Ch14 (lines 100-106): VEP application
- Ch15 (lines 262-270): RNA/splicing context
- Ch26 (line 163): Clinical validation

**Overlap level**: Low (appropriate)
**Status**: GOOD - Ch6 is consistently referenced

### 12. Benchmark Suites

**Appears in**: Multiple chapters
- Ch20: **PRIMARY** - All benchmark details
- Ch11 (lines 60-62): Brief mentions

**Overlap level**: HIGH per TODO/notes.md
**Recommendation**: Per TODO (line 60-62), Ch11 should move benchmark details to Ch20
**Action Required**:
- Ch11: Keep brief summary, add cross-refs to Ch20 sections
- TODO note: "X-ref with CH20 where possible" and "All these benchmarks need to be in CH20"

### 13. Practical Model Usage (Fine-tuning, Embeddings)

**Appears in**: Ch5-9 (PRIMARY) and Ch11
- Ch5-9: **PRIMARY** - Part 2 covers ML principles
- Ch11 (lines 65-70): DNA LM practical usage

**Overlap level**: HIGH per TODO/notes.md
**Recommendation**: Per TODO (line 66), Ch11 should reference Ch5-9 as primary
**Action Required**:
- Ch11: Add cross-refs to Part 2 chapters as primary source

### 14. Terminology: "Regulatory Model" vs "Sequence-to-Function Model"

**Appears in**: Ch10, Ch13
**Overlap level**: N/A (inconsistency issue)
**Recommendation**: Per TODO (line 117), clarify relationship and be consistent
**Action Required**:
- Standardize terminology or clarify hierarchy in Ch13

## High-Overlap Passages Requiring Attention

### Passage 1: Zero-Shot Prediction Methods
**Locations**:
- `part_2/p2-ch09-transfer.qmd` (primary)
- `part_3/p3-ch14-vep-fm.qmd:162` (per TODO note)

**Issue**: Ch14 may repeat Ch9 content on zero-shot scoring
**Recommendation**: Ch14 should cross-reference Ch9 and Ch12 for methodology; focus on VEP-specific applications

### Passage 2: Benchmark Suite Details
**Locations**:
- `part_3/p3-ch11-dna-lm.qmd:60-62`
- `part_5/p5-ch20-benchmarks.qmd` (should be primary)

**Issue**: Per TODO, benchmark details in Ch11 should be in Ch20
**Recommendation**: Ch11 summarizes; Ch20 has full details

### Passage 3: Practical Usage Patterns
**Locations**:
- `part_2/p2-ch05-representations.qmd` through `p2-ch09-transfer.qmd`
- `part_3/p3-ch11-dna-lm.qmd:66-70`

**Issue**: Per TODO, Ch11 "Using DNA Language Models in Practice" overlaps Part 2
**Recommendation**: Cross-ref to Ch5-9 as primary source

### Passage 4: Uncertainty Quantification
**Locations**:
- `part_5/p5-ch23-uncertainty.qmd` (primary)
- `part_3/p3-ch14-vep-fm.qmd:187`

**Issue**: Per TODO (line 187), Ch14 uncertainty section may repeat Ch23
**Recommendation**: Ch14 should focus on VEP-specific aspects; cross-ref Ch23 for methods
**Status**: Partially addressed - Ch14 line 189 has cross-ref to Ch23

### Passage 5: ACMG Guidelines
**Locations**:
- `part_3/p3-ch14-vep-fm.qmd:209-213`
- `part_6/p6-ch26-rare-disease.qmd:43-75`
- `part_1/p1-ch04-vep-classical.qmd:66`

**Issue**: ACMG explained in multiple places
**Recommendation**: Add cross-references between Ch14 and Ch26; consider sidebar per TODO

### Passage 6: Attention Scaling (Quadratic Complexity)
**Locations**:
- `part_2/p2-ch07-attention.qmd` (primary)
- `part_3/p3-ch13-regulatory.qmd:123`

**Issue**: Per TODO (line 123), attention scaling is repeated
**Status**: TODO notes "probably bears repeating in this context" - acceptable redundancy

## Cross-Reference Suggestions

| From Chapter | Section | Topic | Add Reference To |
|--------------|---------|-------|------------------|
| Ch11 | sec-ch11-benchmark-suites | Benchmark details | @sec-ch20-* benchmark sections |
| Ch11 | sec-ch11-practical-use | Embeddings, fine-tuning | @sec-ch05 through @sec-ch09 |
| Ch14 | sec-ch14-zeroshot-plm | Zero-shot methods | @sec-ch09-zero-shot, @sec-ch12-variant-effects |
| Ch14 | sec-ch14-uncertainty | UQ methods | @sec-ch23-* (partially done) |
| Ch14 | sec-ch14-spliceai | ACMG mapping | @sec-ch14-acmg-mapping (internal) |
| Ch14 | sec-ch14-double-counting | ACMG | @sec-ch14-acmg-mapping |
| Ch16 | sec-ch16-batch-effects | Batch effects | @sec-ch22-batch-effects |
| Ch19 | sec-ch19-batch-effects | Batch effects | @sec-ch22-batch-effects |
| Ch25 | sec-ch25-calibration | Calibration methods | @sec-ch23-calibration |

## Necessary Redundancy (Keep As-Is)

Some concepts legitimately need re-introduction in different contexts:

| Concept | Chapters | Rationale |
|---------|----------|-----------|
| Foundation model definition | Ch10, Ch16 | Different domains (DNA vs single-cell) |
| Attention mechanism basics | Ch7, Ch13 | Ch7 theory, Ch13 regulatory application |
| ClinVar description | Ch2, Ch20 | Ch2 data source, Ch20 benchmark usage |
| Calibration importance | Ch14, Ch23, Ch25 | Different contexts (VEP, UQ, clinical) |
| Ancestry/population structure | Ch2, Ch3, Ch22 | Data, GWAS, confounding perspectives |

## Action Items from TODO/notes.md

### High Priority (affects cross-referencing)

1. **Ch11 → Ch20**: Move benchmark suite details to Ch20, keep summaries in Ch11
   - TODO line 60-62

2. **Ch11 → Ch5-9**: Add cross-refs to Part 2 for practical usage
   - TODO line 66

3. **Ch14 → Ch23**: Ensure uncertainty section doesn't repeat Ch23
   - TODO line 187

4. **Ch14 → Ch9, Ch12**: Don't repeat zero-shot content
   - TODO line 162

### Medium Priority

5. **Ch13**: Clarify "regulatory model" vs "sequence-to-function model"
   - TODO line 117

6. **Ch14 internal**: Reference ACMG mapping section (14.5.3) consistently
   - TODO lines 169, 176

### Low Priority (acceptable context-specific repetition)

7. **Ch13**: Attention scaling (OK to repeat per TODO line 123)

## Redundancy Health Score

| Category | Status |
|----------|--------|
| Database descriptions | 95% - Well handled |
| ML concepts (MLM, attention) | 90% - Good cross-refs |
| Calibration/UQ | 85% - Minor cleanup |
| Model descriptions | 95% - Primary chapters clear |
| Benchmark details | 70% - Needs Ch11→Ch20 consolidation |
| Practical usage | 75% - Needs Ch11→Part2 cross-refs |
| Terminology consistency | 80% - Minor inconsistencies |
| **Overall** | **~85%** |

## Recommendations Summary

### Immediate Actions

1. **Ch11**: Add cross-references to Ch20 for benchmark details
2. **Ch11**: Add cross-references to Ch5-9 for practical usage patterns
3. **Ch14**: Verify uncertainty section appropriately references Ch23

### Soon

4. **Ch16/Ch19**: Add cross-references to Ch22 for batch effects
5. **Ch13**: Standardize "regulatory model" / "sequence-to-function model" terminology

### Nice to Have

6. Create ACMG guidelines sidebar (per TODO) for consistent referencing
7. Add Ch14 internal cross-refs to ACMG mapping section
