# Pre-Commit Style Checks Reference

Quick style checks to run on changed files before commit.

## Critical Checks (Block Commit)

### 1. Em-Dashes (Zero Tolerance)

**Pattern**: `—` (U+2014), `–` (U+2013), `--`

```regex
—|–|--
```

**Auto-fix**: Replace with comma or parentheses (conservative)
- `"X—Y"` → `"X, Y"` or `"X (Y)"`

### 2. Contractions (Zero Tolerance)

**Pattern**: Common contractions

```regex
\b(don't|won't|can't|couldn't|wouldn't|shouldn't|isn't|aren't|wasn't|weren't|hasn't|haven't|hadn't|doesn't|didn't|it's|that's|there's|here's|what's|who's|let's|I'm|I've|I'll|I'd|we're|we've|we'll|we'd|you're|you've|you'll|you'd|they're|they've|they'll|they'd|he's|she's)\b
```

**Auto-fix**:
| Found | Replace |
|-------|---------|
| don't | do not |
| won't | will not |
| can't | cannot |
| it's | it is |
| that's | that is |
| let's | let us |
| I'm | I am |
| we're | we are |
| they're | they are |

### 3. Broken Cross-References

**Pattern**: `@sec-*` without matching `{#sec-*}`

```bash
# Find all references
grep -oE '@sec-[a-z0-9-]+' *.qmd | sort -u

# Find all definitions
grep -oE '\{#sec-[a-z0-9-]+\}' *.qmd | sort -u

# Diff to find broken
```

**No auto-fix** - requires manual resolution

### 4. Broken Citations

**Pattern**: `[@key]` without matching bib entry

```bash
# Find all citations
grep -oE '@[a-z_-]+_[0-9]{4}' *.qmd | sort -u

# Check against bib files
```

**No auto-fix** - requires manual resolution

---

## Warning Checks (Report Only)

### 5. Gene Names Not Italicized

**Known genes** (partial list):
```
BRCA1, BRCA2, TP53, CFTR, APOE, CYP2D6, HLA-A, NF1,
EGFR, KRAS, BRAF, MYC, RB1, APC, MLH1, MSH2, PTEN,
dystrophin, huntingtin
```

**Pattern**: Gene name not wrapped in `*...*`

```regex
\b(BRCA1|BRCA2|TP53|CFTR|...)\b(?!\*)
```

**Check**: Ensure `*GENE*` format

### 6. Model Names Not Italicized

**Known models**:
```
Enformer, Borzoi, ESM, ESM-1b, ESM-2, ESMFold, DNABERT,
DNABERT-2, HyenaDNA, Caduceus, Evo, AlphaFold, AlphaMissense,
AlphaGenome, Geneformer, scGPT, SpliceAI, Sei, Akita, Orca,
GPN, Nucleotide Transformer, DeepVariant, DeepSEA, Basset
```

**Pattern**: Model name not wrapped in `*...*`

```regex
\b(Enformer|ESM-2|DNABERT|...)\b(?!\*)
```

### 7. Orphaned Headers

**Pattern**: `##` immediately followed by `###` without prose

```regex
^##[^#].*\n+###
```

**Should have**: At least one paragraph between header levels

### 8. Long Sentences

**Threshold**: >50 words (lenient for pre-commit; full review uses 40)

**Detection**: Split on `.!?` and count words

### 9. Bullet Points in Prose

**Pattern**: `- ` or `* ` at line start outside callouts

```regex
^[\s]*[-*]\s+(?!.*:::|.*callout)
```

**Exceptions**: Inside `::: {.callout-*}` blocks

### 10. Databases Incorrectly Italicized

**Should NOT be italicized**:
```
ClinVar, gnomAD, UniProt, ENCODE, GTEx, TCGA,
UK Biobank, dbSNP, Ensembl, GENCODE
```

**Pattern**: Database wrapped in `*...*`

```regex
\*(ClinVar|gnomAD|UniProt|...)\*
```

---

## Info Checks (Log Only)

### 11. Semicolon Density

**Threshold**: >3 semicolons per 500 words

### 12. Parenthetical Density

**Threshold**: >2 parenthetical phrases per paragraph

**Pattern**: `(...)`

### 13. Metric Naming

**Preferred**: `auROC`, `auPRC`
**Avoid**: `AUC`, `AUROC`, `ROC` (when meaning area under curve)

```regex
\b(AUC|AUROC)\b(?!-)
```

---

## Auto-Fix Rules (--fix flag)

### Safe to Auto-Fix

| Issue | Detection | Fix |
|-------|-----------|-----|
| Em-dash | `—` | `, ` or ` (` `)` |
| Contraction | `don't` | `do not` |
| Trailing whitespace | `\s+$` | trim |
| Double space | `  +` | single space |
| Smart quotes | `""''` | `""''` |
| Tab in prose | `\t` | spaces |

### Never Auto-Fix

| Issue | Why |
|-------|-----|
| Cross-refs | Requires understanding context |
| Citations | May need bib update |
| Content | Requires judgment |
| Gene/model formatting | May be intentional |
| Headers | Structural change |

---

## File Type Handling

| Extension | Checks to Run |
|-----------|---------------|
| `.qmd` | All checks |
| `.bib` | Citation integrity only |
| `.md` | Style checks (not xrefs) |
| `.yml` | Syntax only |
| Other | Skip |

---

## Quick Reference

### Must Pass (Critical)
```
✗ Em-dashes: —, –, --
✗ Contractions: don't, can't, etc.
✗ Broken @sec- references
✗ Broken [@...] citations
```

### Should Review (Warning)
```
⚠ Gene names: BRCA1 → *BRCA1*
⚠ Model names: Enformer → *Enformer*
⚠ Orphaned headers: ## then ###
⚠ Long sentences: >50 words
⚠ Bullets in prose
```

### Note Only (Info)
```
ℹ Semicolon density
ℹ Parenthetical density
ℹ Metric naming
```
