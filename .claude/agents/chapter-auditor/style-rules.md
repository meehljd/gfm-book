# Style Rules Reference

Quick reference for typography and writing style requirements.

## Critical Non-Negotiables (Check First)

### 1. ZERO Em-Dashes
- No `—` (U+2014) or `–` (U+2013) or `--`
- Use: parentheses, commas, colons, semicolons, or separate sentences
- ❌ "reads—typically 100 to 300 bp—per sample"
- ✅ "reads (typically 100 to 300 bp) per sample"

### 2. ZERO Bullet Points in Prose
- Exceptions only: tables, boxed summaries, appendices, callouts

### 3. ZERO Meta-Commentary
- ❌ "Let's examine", "Here's what we'll cover", "It's worth noting"
- ❌ "This chapter examines...", "We will explore..."

### 4. Lead with Why
- Every major concept: motivation/problem before mechanism
- Why → What → How

## Typography Rules

### Bold: Glossary Terms (First Use Only)
- **transformer architecture** → transformer (after first use)
- **attention mechanisms** → attention mechanisms
- **fine-tuning** → fine-tuning

### Italics: Always

| Category | Examples |
|----------|----------|
| Gene names | *BRCA1*, *TP53*, *CFTR*, *CYP2D6* |
| Model names | *Enformer*, *ESM-2*, *DNABERT*, *AlphaFold*, *DeepVariant* |
| Math variables | *n*, *d_k*, *α* |
| Latin terms | *in silico*, *de novo*, *in cis*, *in trans* |

### Monospace: Computational Elements

| Category | Examples |
|----------|----------|
| File formats | `VCF`, `BAM`, `FASTQ`, `BED` |
| Code elements | `batch_size`, `forward()` |
| CLI tools | `bedtools`, `samtools`, `BWA` |
| Python packages | `torch`, `transformers` |

### Regular Text (No Formatting)

| Category | Examples |
|----------|----------|
| Databases | gnomAD, ClinVar, UniProt, ENCODE |
| Consortia | UK Biobank, GTEx, TCGA |
| Assays | ATAC-seq, ChIP-seq, RNA-seq |
| Diseases | cystic fibrosis, Alzheimer's disease |
| Drugs | codeine, tamoxifen, warfarin |

## Writing Rules

### Forbidden Patterns

**Transition clichés (use sparingly):**
- "However" / "Moreover" as sentence starters
- "Importantly", "Crucially", "Notably", "Interestingly"
- "It's worth noting that", "With this in mind"

**Formulaic section transitions:**
- ❌ "Having discussed X, we now turn to Y"
- ❌ "Building on the concepts above..."
- ❌ "The previous section established..."

**False enthusiasm:**
- ❌ "exciting developments", "powerful approach", "remarkable results"

**Anthropomorphization:**
- ❌ "The model learns to understand"
- ✅ "The model learns to predict"

**Bolded term lead-ins (disguised bullets):**
- ❌ "**Population structure** encompasses..."
- ✅ "Ancestry creates perhaps the most pervasive confounder..."

### Contractions
- No contractions in formal prose
- ❌ "don't", "won't", "can't", "it's"
- ✅ "do not", "will not", "cannot", "it is"

### Sentence Length
- Flag sentences over 40 words
- Vary sentence length for rhythm
- Front-load key information

### Colon/Semicolon Moderation
- Max 2-3 semicolons per page
- Avoid multiple colons in single paragraph

### Parenthetical Phrases
- Max 1-2 per paragraph
- Use for mechanistic precision without disrupting flow

## Metric Naming

| Preferred | Avoid |
|-----------|-------|
| auROC | ROC, AUC, AUROC |
| auPRC | PRC, AUPRC |
| F1 score | F1, F-score |

## Opening Requirements

### Chapter Openings
- [ ] Paradox/tension in paragraph 1 (not just topic)
- [ ] Unique hook (check other chapters)
- [ ] Concrete numbers/scales in first 100 words
- [ ] At least one memorable, quotable sentence
- [ ] No "This chapter examines..."

### Section Openings
- [ ] Stakes/motivation before mechanism
- [ ] No formulaic transitions
- [ ] Concrete example, limitation, or question

## No Orphaned Headers

Every header must have at least one paragraph before any subheader:

```markdown
## Variant Calling Approaches

[Introductory paragraph required here]

### Statistical Methods
```

## Quick Checklist

Before finalizing any section:
- [ ] Search for `—` (em-dash) - must be ZERO
- [ ] Search for bullet points in prose - must be ZERO
- [ ] Search for "Let's", "Here's", "It's worth noting" - remove all
- [ ] Check for **bolded term** paragraph openers - restructure
- [ ] Verify gene/model names are italicized
- [ ] Verify file formats are monospace
