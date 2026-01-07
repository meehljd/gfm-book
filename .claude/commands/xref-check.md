# Cross-Reference Validator

Validate and analyze internal cross-references in the Quarto book.

## Invocation
```
/xref-check [chapter]
```
- No argument: Check entire book
- With argument: Check specific chapter (e.g., `p3-ch11-dna-lm`)

## Tasks

1. **Extract all cross-references**: Scan all `.qmd` files for `@sec-*` patterns
2. **Extract all section IDs**: Find all `{#sec-*}` definitions in headers
3. **Validate references**: Identify any `@sec-*` that doesn't have a corresponding `{#sec-*}` definition
4. **Find orphaned sections**: Identify defined sections that are never referenced (may be intentional for top-level chapters)
5. **Detect redundancy opportunities**: Find chapters that discuss similar topics without cross-referencing each other
6. **Generate suggestions**: Based on content similarity, suggest where cross-references could be added

## Output

Save report to `meta/reports/xref-check-YYYY-MM-DD.md` with:

```markdown
# Cross-Reference Report

Generated: [timestamp]
Scope: [entire book | specific chapter]

## Summary
- Total cross-references: X
- Valid references: X
- Broken references: X
- Orphaned sections: X

## Broken References
| File | Line | Reference | Suggestion |
|------|------|-----------|------------|
| ... | ... | @sec-missing | Did you mean @sec-similar? |

## Orphaned Sections (never referenced)
| File | Section ID | Title |
|------|------------|-------|

## Cross-Reference Opportunities
Based on content analysis, these sections discuss related topics but don't cross-reference:
- `@sec-ch11-probing` and `@sec-ch12-emergent-knowledge` both discuss what models learn
- ...

## Statistics by Chapter
| Chapter | Outgoing Refs | Incoming Refs | Ratio |
|---------|---------------|---------------|-------|
```

## Implementation Notes

- Use `grep` to find `@sec-` patterns and `{#sec-` definitions
- Parse `meta/qmd_headings.md` for structured heading data
- Cross-reference proposals exist in `meta/cross-reference-proposals.md` - compare against actual usage
- Refer to `meta/_instructions/section-key-proposals.md` for naming conventions
