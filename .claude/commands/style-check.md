# Style Enforcer

Check adherence to the book's documented style guide.

## Invocation
```
/style-check [chapter]
```
- No argument: Check entire book
- With argument: Check specific chapter (e.g., `p3-ch11-dna-lm`)

## Style Rules (from meta/_instructions/)

### Typography Rules (from ref-instructions.md)

1. **Gene names**: Must be italicized - `*TP53*`, `*BRCA1*`, `*APOE*`
2. **Model names**: Must be italicized - `*Enformer*`, `*ESM-2*`, `*DNABERT*`, `*AlphaFold*`
3. **Databases/Resources**: NOT italicized - `ClinVar`, `gnomAD`, `UniProt`, `ENCODE`
4. **Tools/Software**: NOT italicized - `bedtools`, `samtools`, `BLAST`
5. **File formats**: Monospace - `` `VCF` ``, `` `BAM` ``, `` `FASTQ` ``

### Writing Rules (from claude-project-instructions.md)

6. **No em-dashes**: Use commas, parentheses, or restructure instead of `—` or `--`
7. **No bullet points in prose**: Use flowing paragraphs, not lists (exceptions: summaries, sidebars)
8. **Abbreviations**: Must be expanded on first use per chapter
9. **Bold**: Reserved for glossary terms on first definition only
10. **Avoid contractions**: Use "do not" instead of "don't", etc.

### Additional Writing Rules

11. **No bolded term lead-ins**: Paragraphs must not open with bolded terminology followed by definitions (disguised bullets)
12. **Colon/semicolon moderation**: Max 2-3 semicolons per page; avoid multiple colons in single paragraph
13. **Parenthetical phrase limit**: Maximum 1-2 parenthetical phrases per paragraph
14. **Metric formatting**: Use `auROC` not `AUC`, `AUROC`, or `ROC` when referring to area under ROC curve
15. **No orphaned headers**: Every header must have at least one paragraph before any subheader

## Tasks

1. **Scan for em-dashes**: Find `—` (U+2014), `–` (U+2013), and `--` patterns
2. **Check gene formatting**: Find gene names not in italics (compile list from glossary)
3. **Check model formatting**: Find model names not in italics
4. **Check database formatting**: Find databases incorrectly italicized
5. **Find bullet points**: Detect `- ` or `* ` in prose sections (not in callouts/sidebars)
6. **Abbreviation tracking**: Check common abbreviations (NGS, VEP, GWAS, CNN, etc.) for first-use expansion
7. **Find contractions**: Detect don't, won't, can't, etc.
8. **Find bolded term lead-ins**: Detect paragraphs starting with `**Term**` followed by definition text
9. **Check semicolon density**: Flag pages with >3 semicolons
10. **Check parenthetical density**: Flag paragraphs with >2 parenthetical phrases
11. **Check metric naming**: Find `AUC`, `AUROC`, `ROC` that should be `auROC`
12. **Find orphaned headers**: Detect `##` immediately followed by `###` without intervening prose

## Output

Save report to `meta/reports/style-check-YYYY-MM-DD.md` with:

```markdown
# Style Check Report

Generated: [timestamp]
Scope: [entire book | specific chapter]

## Summary
- Em-dashes found: X
- Gene formatting issues: X
- Model formatting issues: X
- Database formatting issues: X
- Bullet point violations: X
- Abbreviation issues: X
- Contractions found: X

## Em-Dashes (must remove)
| File | Line | Context |
|------|------|---------|

## Gene Formatting Issues
| File | Line | Found | Should Be |
|------|------|-------|-----------|
| p3-ch11.qmd | 45 | TP53 | *TP53* |

## Model Formatting Issues
| File | Line | Found | Should Be |
|------|------|-------|-----------|

## Database Formatting Issues (incorrectly italicized)
| File | Line | Found | Should Be |
|------|------|-------|-----------|

## Bullet Points in Prose
| File | Line | Context |
|------|------|---------|

## Abbreviation Issues (not expanded on first use)
| File | Line | Abbreviation | First Use Line |
|------|------|--------------|----------------|

## Contractions Found
| File | Line | Found | Should Be |
|------|------|-------|-----------|

## Bolded Term Lead-ins (disguised bullets)
| File | Line | Pattern Found |
|------|------|---------------|

## Semicolon Density Issues
| File | Section | Count | Lines |
|------|---------|-------|-------|

## Parenthetical Overuse
| File | Line | Count | Context |
|------|------|-------|---------|

## Metric Naming Issues
| File | Line | Found | Should Be |
|------|------|-------|-----------|
| p3-ch11.qmd | 234 | AUROC | auROC |

## Orphaned Headers
| File | Line | Header | Missing Intro Before |
|------|------|--------|---------------------|
```

## Implementation Notes

- Reference `meta/_instructions/ref-instructions.md` for complete typography rules
- Reference `meta/_instructions/claude-project-instructions.md` for writing rules
- Reference `appendix/appendix-f-glossary.qmd` for term list
- Known model names: Enformer, Borzoi, ESM, ESM-1b, ESM-2, ESMFold, DNABERT, HyenaDNA, Caduceus, Evo, AlphaFold, AlphaMissense, AlphaGenome, Geneformer, scGPT, SpliceAI, Sei, Akita, Orca, GPN, Nucleotide Transformer
- Known databases: ClinVar, gnomAD, UniProt, ENCODE, GTEx, TCGA, UK Biobank, dbSNP, Ensembl, GENCODE
