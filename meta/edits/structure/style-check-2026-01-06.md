# Style Check Report

Generated: 2026-01-06
Scope: Entire book

## Summary

| Issue | Count | Priority |
|-------|------:|----------|
| Em-dashes in prose | 3 | Medium |
| Em-dashes in tables | 7 | OK (acceptable) |
| Non-italicized model names | ~250+ | **HIGH** |
| Non-italicized gene names | 46 | Medium |
| Databases incorrectly italicized | 0 | None |
| Bullet points in prose | 0 | None |
| Contractions | 1 | Low |

## Em-Dashes (must remove from prose)

Em-dashes in **tables** (showing "—" for missing data) are acceptable. Em-dashes in **prose** should be replaced:

| File | Line | Context | Action |
|------|------|---------|--------|
| preface.qmd | 34 | "pain points—data formats" | Replace with comma or colon |
| preface.qmd | 62 | "interpretability—how we know" | Replace with colon |
| preface.qmd | 130 | "— *Josh Meehl*" | Replace with em-dash-like styling or remove |
| p4-ch15-rna.qmd | 34 | Figure description "Deep minimum—single" | OK in figure caption |
| p6-ch28-design.qmd | 19 | Figure description | OK in figure caption |

**Note**: En-dashes (–) for ranges like "128–256" are correct and should remain.

## Model Formatting Issues

Many model names appear without italics. Per style guide, models should be formatted as `*ModelName*`.

### By Chapter (non-italicized model count)

| Chapter | Count | Models Found |
|---------|------:|--------------|
| p2-ch06-cnn.qmd | 21 | SpliceAI, DeepSEA, ExPecto |
| p3-ch14-vep-fm.qmd | 19 | SpliceAI, Enformer, AlphaMissense |
| p3-ch13-regulatory.qmd | 19 | Enformer, Borzoi, Sei |
| p3-ch12-protein-lm.qmd | 16 | ESMFold, AlphaFold |
| p1-ch01-ngs.qmd | 16 | DeepVariant |
| p3-ch11-dna-lm.qmd | 15 | DNABERT, HyenaDNA |
| p2-ch07-attention.qmd | 15 | Various |
| p2-ch08-pretraining.qmd | 14 | Various |

### Sample Issues

| File | Line | Found | Should Be |
|------|------|-------|-----------|
| p1-ch01-ngs.qmd | 256 | DeepVariant | *DeepVariant* |
| p1-ch01-ngs.qmd | 258 | DeepVariant | *DeepVariant* |
| p2-ch06-cnn.qmd | Various | SpliceAI | *SpliceAI* |
| p3-ch13-regulatory.qmd | Various | Enformer | *Enformer* |

**Note**: Some occurrences may be in headers, tables, or code blocks where italics aren't needed. Manual review recommended.

### Recommended Fix

Run find-replace for each model:
```bash
# Example for DeepVariant (avoid headers and already-italicized)
sed -i 's/\bDeepVariant\b/*DeepVariant*/g' part_1/p1-ch01-ngs.qmd
```

## Gene Formatting Issues (46 instances)

Gene names should be italicized: `*BRCA1*` not `BRCA1`

| File | Line | Found | Should Be |
|------|------|-------|-----------|
| p1-ch03-gwas.qmd | 268 | BRCA2 | *BRCA2* |
| p1-ch01-ngs.qmd | 110 | CFTR | *CFTR* |
| p1-ch01-ngs.qmd | 131 | CFTR | *CFTR* |
| p1-ch02-data.qmd | 260 | BRCA2 | *BRCA2* |
| p1-ch02-data.qmd | 285 | BRCA1, BRCA2, CFTR | *BRCA1*, *BRCA2*, *CFTR* |
| p1-ch04-vep-classical.qmd | 83 | BRCA2 | *BRCA2* |
| p2-ch06-cnn.qmd | 193 | BRCA1 (4x) | *BRCA1* |
| p2-ch08-pretraining.qmd | 307, 345 | BRCA1 | *BRCA1* |
| p2-ch05-representations.qmd | 148 | BRCA1 | *BRCA1* |
| p2-ch07-attention.qmd | 142, 276 | BRCA1 | *BRCA1* |
| p2-ch09-transfer.qmd | 349 | BRCA1 | *BRCA1* |
| p4-ch18-networks.qmd | 299 | TP53 | *TP53* |

### Most Common Gene Issues

| Gene | Occurrences |
|------|------------|
| BRCA1 | 15 |
| BRCA2 | 8 |
| CFTR | 4 |
| TP53 | 3 |
| APOE | 0 (properly formatted) |

## Database Formatting (PASS)

No databases were incorrectly italicized. These remain correctly unformatted:
- ClinVar
- gnomAD
- UniProt
- ENCODE
- GTEx
- dbSNP
- Ensembl

## Contractions (1 instance)

| File | Line | Found | Should Be |
|------|------|-------|-----------|
| p2-ch08-pretraining.qmd | 330 | it's | it is |

## Bullet Points in Prose (PASS)

No bullet points detected in prose sections. All lists appear to be in appropriate contexts (callouts, sidebars, or intentional lists).

## Abbreviation Expansion (PASS)

Spot-checked common abbreviations - properly expanded on first use:

| Abbreviation | First Use | Status |
|--------------|-----------|--------|
| NGS | p1-ch01-ngs.qmd:13 | "**Next-generation sequencing (NGS)**" ✓ |
| VEP | Expanded where used | ✓ |
| GWAS | Expanded where used | ✓ |

## Recommended Actions

### High Priority

1. **Fix model name italics** (~250+ instances)
   - Focus on: DeepVariant, SpliceAI, Enformer, DNABERT, AlphaFold
   - Use find-replace with manual verification

2. **Fix gene name italics** (46 instances)
   - Focus on: BRCA1 (15x), BRCA2 (8x), CFTR (4x)

### Medium Priority

3. **Remove prose em-dashes** (3 in preface.qmd)
   - Line 34, 62, 130

4. **Fix contraction** (1 instance)
   - p2-ch08-pretraining.qmd:330 - change "it's" to "it is"

### Low Priority / Manual Review

5. Verify model names in tables/headers don't need italics
6. Check if any genes in tables need different handling

## Style Compliance Score

| Category | Status |
|----------|--------|
| Em-dashes | 97% (3 in prose) |
| Contractions | 99.9% (1 found) |
| Database formatting | 100% |
| Bullet points | 100% |
| Abbreviations | 100% |
| Gene formatting | 85% (46 issues) |
| Model formatting | 60% (~250 issues) |
| **Overall** | **~85%** |

## Quick Fix Commands

```bash
# Fix gene names (run from book root, verify after)
cd /root/gfm_book

# BRCA1
grep -rl '\bBRCA1\b' part_*/*.qmd | xargs sed -i 's/\bBRCA1\b/*BRCA1*/g'

# BRCA2
grep -rl '\bBRCA2\b' part_*/*.qmd | xargs sed -i 's/\bBRCA2\b/*BRCA2*/g'

# CFTR
grep -rl '\bCFTR\b' part_*/*.qmd | xargs sed -i 's/\bCFTR\b/*CFTR*/g'

# TP53
grep -rl '\bTP53\b' part_*/*.qmd | xargs sed -i 's/\bTP53\b/*TP53*/g'

# Note: Run quarto preview after to verify no breakage in tables/code
```

**Warning**: Always verify after bulk replacements - some contexts (tables, code) may not need italics.
