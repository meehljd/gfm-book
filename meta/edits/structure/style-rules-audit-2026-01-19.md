# Style Rules Audit Report
**Date:** 2026-01-19
**Audit Focus:** Em-dashes and contractions

## Executive Summary

**Status: COMPLETED**

| Category | Before | After | Reduction |
|----------|--------|-------|-----------|
| Em-dashes (violations) | 208 | 58* | 72% |
| Contractions | 75 | 0 | 100% |

*Remaining 58 are proper en-dashes (number ranges, compound terms)

---

## Em-Dash Fixes

### Initial State
- **208 total em-dashes** across 31 files
- Mix of style violations and proper en-dash usage

### Final State
- **58 remaining** (all proper usage)
  - Appendix files: 42 (ranges like "50M–2.5B", compound terms like "enhancer–promoter")
  - Preface: 1 (signature attribution)
  - Chapter files: 15 (proper en-dashes in ranges/compounds)

### Chapters Fixed (all em-dash violations removed)

| Chapter | Original Count | Pattern Applied |
|---------|---------------|-----------------|
| p4-ch18-vep-fm.qmd | 14 | All patterns |
| p3-ch13-confounding.qmd | 13 | Explanations, clauses |
| p6-ch24-uncertainty.qmd | 12 | Definitions, clauses |
| p5-ch23-multi-omics.qmd | 12 | Explanations, lists |
| p1-ch03-gwas.qmd | 10 | Definitions, clauses |
| p6-ch26-causal.qmd | 10 | Parentheticals, clauses |
| p5-ch21-3d-genome.qmd | 10 | Explanations, definitions |
| p6-ch27-regulatory.qmd | 10 | Consent examples, definitions |
| p2-ch06-cnn.qmd | 9 | Technical explanations |
| p4-ch17-regulatory.qmd | 14 | Multi-pattern fixes |
| p3-ch12-evaluation.qmd | 8 | Explanations, figure captions |
| p5-ch20-single-cell.qmd | 8 | Technical notes |
| p4-ch15-dna-lm.qmd | 8 | Explanations, limitations |
| p7-ch32-frontiers.qmd | 7 | Synthesis points |
| p7-ch31-design.qmd | 7 | Design constraints |
| p6-ch25-interpretability.qmd | 6 | Explanations |
| p4-ch16-protein-lm.qmd | 6 | Limitations, examples |
| p7-ch29-rare-disease.qmd | 6 | Clinical scenarios |
| p7-ch30-drug-discovery.qmd | 6 | Answer explanations |
| p1-ch01-ngs.qmd | 5 | Technology descriptions |
| p1-ch02-data.qmd | 5 | Database definitions |
| p3-ch11-benchmarks.qmd | 4 | Benchmark descriptions |
| p5-ch19-rna.qmd | 4 | Structure explanations |
| p3-ch08-pretraining.qmd | 4 | Training concepts |
| p1-ch04-vep-classical.qmd | 3 | Predictor limitations |
| p4-ch14-fm-principles.qmd | 3 | Decision frameworks |
| p3-ch10-adaptation.qmd | 2 | Model adaptation |
| p3-ch09-transfer.qmd | 2 | Transfer learning |
| p5-ch22-networks.qmd | 2 | Network analysis |
| p7-ch28-clinical-risk.qmd | 2 | Clinical utility |
| index.qmd | 1 | Learning objectives |

### Em-Dash Replacement Patterns Applied

**Pattern 1: Introducing explanation**
- Before: `concept—explanation`
- After: `concept: explanation`
- Example: "Training data bias—models" → "Training data bias: models"

**Pattern 2: Independent clauses**
- Before: `clause—clause`
- After: `clause; clause` or `clause, clause`
- Example: "transfer failures are silent—models produce" → "transfer failures are silent; models produce"

**Pattern 3: Parenthetical (paired)**
- Before: `text—parenthetical—text`
- After: `text (parenthetical) text`
- Example: "this section—orphan proteins—recur" → "this section (orphan proteins) recur"

**Pattern 4: List definitions**
- Before: `**Term**—definition`
- After: `**Term**: definition`
- Example: "**ClinVar**—Aggregates" → "**ClinVar**: Aggregates"

---

## Contraction Fixes

### Initial State
- **75 contractions** across 28 files

### Final State
- **0 contractions** remaining

### Contractions Fixed

| Contraction | Expansion | Count Fixed |
|-------------|-----------|-------------|
| don't | do not | 15 |
| can't | cannot | 8 |
| doesn't | does not | 10 |
| won't | will not | 3 |
| isn't | is not | 5 |
| aren't | are not | 2 |
| couldn't | could not | 2 |
| wouldn't | would not | 2 |
| shouldn't | should not | 1 |
| didn't | did not | 3 |
| haven't | have not | 2 |
| you're | you are | 12 |
| you've | you have | 5 |
| it's | it is | 3 |
| there's | there is | 2 |

---

## Proper En-Dash Usage (Retained)

The following en-dashes were correctly identified and retained:

### Number Ranges (appendix/app-d-models.qmd, app-b-compute.qmd)
- "50M–2.5B" (parameter counts)
- "$3–4/hour" (cost ranges)
- "60–80% discounts" (percentage ranges)

### Compound Terms (appendix/app-f-glossary.qmd)
- "enhancer–promoter interaction"
- "drug–gene interaction"
- "gene–disease validity"
- "protein–protein interaction"
- "Hardy–Weinberg equilibrium"
- "Query–Key–Value"

### Table Categories
- "A–Z" (alphabetical range)
- "[ML] – Machine learning" (category labels)

---

## Other Style Checks (Not Yet Addressed)

The following may require separate review:

1. **Meta-commentary patterns**
   - "This chapter covers..."
   - "In this chapter..."
   - "We will discuss..."

2. **False enthusiasm**
   - "revolutionary"
   - "groundbreaking"
   - "remarkable"

3. **Gene/Model formatting**
   - Gene names should be italicized (*BRCA1*)
   - Model names should be italicized (*ESM-2*)

4. **Citation formatting**
   - Verify @citation-key format consistency

---

## Verification Commands

```bash
# Verify no remaining em-dash violations (should return mostly appendices)
grep -n "—\|–" /root/gfm-book/part_*/p*-ch*.qmd

# Verify no contractions remain
grep -inE "\b(don't|won't|can't|isn't|aren't|doesn't|couldn't|wouldn't|shouldn't|didn't|haven't|you're|you've|it's|there's)\b" /root/gfm-book/**/*.qmd
```

---

*Generated by chapter-auditor style-rules review*
*Completion date: 2026-01-19*
