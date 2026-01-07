# Glossary Checker

Ensure glossary terms are properly used throughout the book.

## Invocation
```
/glossary [mode]
```
- No argument: Full glossary analysis
- `coverage`: Check which terms are used where
- `missing`: Find terms used but not in glossary
- `unused`: Find glossary terms never used

## Tasks

1. **Extract glossary terms**: Parse `appendix/appendix-f-glossary.qmd` for defined terms
2. **Scan for term usage**: Find occurrences of each term across all chapters
3. **Check first-use**: Verify terms are introduced before heavy usage
4. **Find missing terms**: Identify concepts used frequently but not in glossary
5. **Find unused terms**: Glossary entries never referenced in main text
6. **Consistency check**: Ensure terms are used consistently (not variant spellings)

## Output

Save report to `meta/reports/glossary-YYYY-MM-DD.md` with:

```markdown
# Glossary Analysis Report

Generated: [timestamp]

## Summary
- Glossary terms defined: X
- Terms used in main text: X
- Unused glossary terms: X
- Missing from glossary: X (frequent terms not defined)

## Term Coverage Matrix
| Term | Ch1 | Ch2 | Ch3 | ... | Total Uses |
|------|-----|-----|-----|-----|------------|
| Variant Effect Prediction | - | 2 | 5 | ... | 45 |
| Foundation Model | 3 | 1 | 8 | ... | 89 |

## First Use Analysis
| Term | First Use | Chapter | Definition in Glossary |
|------|-----------|---------|------------------------|
| VEP | Line 45 | Ch1 | Yes |
| PLM | Line 234 | Ch5 | No - needs adding |

## Unused Glossary Terms
| Term | Definition (truncated) |
|------|------------------------|
| [term] | [first 50 chars of definition] |

## Missing from Glossary (frequent terms)
| Term | Usage Count | Chapters Used |
|------|-------------|---------------|
| attention mechanism | 67 | Ch7, Ch8, Ch10, Ch11, Ch12 |

## Inconsistent Usage
| Variant 1 | Variant 2 | Recommended |
|-----------|-----------|-------------|
| foundation model | Foundation Model | foundation model |
| pre-training | pretraining | pretraining |

## Acronym Consistency
| Acronym | Expansions Found | Recommended |
|---------|------------------|-------------|
| VEP | variant effect prediction, Variant Effect Prediction | variant effect prediction |
```

## Implementation Notes

- Glossary file: `appendix/appendix-f-glossary.qmd`
- Terms may appear in bold on first definition: `**term**`
- Check for both full terms and acronyms
- Reference `meta/_instructions/claude-project-instructions.md` for term formatting rules
- Common genomics terms to check: SNP, SNV, indel, GWAS, VEP, PLM, DNA-LM, etc.
