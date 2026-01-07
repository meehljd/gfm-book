# Bibliography Auditor

Audit citation integrity across the book's 36 BibTeX files.

## Invocation
```
/bib-audit [chapter]
```
- No argument: Audit entire bibliography
- With argument: Audit specific chapter's bib file (e.g., `p3-ch11`)

## Tasks

1. **Extract cited keys**: Scan all `.qmd` files for `[@key]` and `@key` citation patterns
2. **Extract defined keys**: Parse all `.bib` files in `bib/` directory for entry keys
3. **Find missing citations**: Keys cited in `.qmd` but not defined in any `.bib` file
4. **Find orphaned entries**: Keys defined in `.bib` but never cited anywhere
5. **Detect duplicates**: Same key or same content appearing in multiple `.bib` files
6. **Find citation-needed markers**: Look for `[Citation Needed]`, `*[Citation Needed]*`, `TODO`, or similar placeholders
7. **Generate statistics**: Citation counts by chapter, most-cited papers

### Citation Style Checks (from claude-project-instructions.md)

8. **Check citation integration**: Flag mid-sentence brackets that break flow (prefer end-of-sentence)
9. **Check dangling citations**: Flag "Studies have shown [@key]" patterns (should name author)
10. **Verify seminal citations**: Major model/method introductions should use in-prose format ("Vaswani et al. @key introduced...")

## Output

Save report to `meta/reports/bib-audit-YYYY-MM-DD.md` with:

```markdown
# Bibliography Audit Report

Generated: [timestamp]

## Summary
- Total citations in text: X
- Unique citation keys: X
- Defined bibliography entries: X
- Missing citations: X
- Orphaned entries: X
- Duplicate entries: X
- Citation-needed markers: X

## Missing Citations (cited but not in .bib)
| File | Line | Citation Key |
|------|------|--------------|

## Orphaned Entries (in .bib but never cited)
| Bib File | Key | Title (truncated) |
|----------|-----|-------------------|

## Duplicate Entries
| Key | Found In |
|-----|----------|
| smith2023 | bib/p1/p1-ch02.bib, bib/p3/p3-ch11.bib |

## Citation-Needed Markers
| File | Line | Context |
|------|------|---------|

## Most Cited References (Top 20)
| Rank | Key | Count | Title |
|------|-----|-------|-------|

## Citations by Chapter
| Chapter | Citation Count |
|---------|----------------|
```

## Implementation Notes

- Master bibliography is `bib/references.bib` (full collection)
- Split files follow pattern `bib/p{N}/p{N}-ch{NN}.bib` and `bib/apx/app-{a-f}.bib`
- Citation patterns: `[@key]`, `[@key1; @key2]`, `@key` (narrative)
- Check `_quarto.yml` for the bibliography file list
