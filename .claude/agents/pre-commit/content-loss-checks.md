# Content Loss Detection Reference

Criteria for detecting detrimental content loss in diffs.

## Severity Classification

### BLOCK - Critical Loss (Must Revert or Justify)

| Pattern | Detection | Why Critical |
|---------|-----------|--------------|
| Entire section deleted | `^## ` or `^### ` removed with content | Structural damage |
| >500 words removed | Word count diff | Major content loss |
| Figure + caption deleted | `![` removal | Visual learning lost |
| Table deleted | `\|.*\|` block removal | Data presentation lost |
| Callout deleted | `::: {.callout` removal | Key concept highlighted |
| Multiple citations removed | `[@` count decrease >3 | Evidence removed |
| Cross-ref target deleted | `{#sec-` removed | Breaks other chapters |

### WARN - Significant Loss (Review Required)

| Pattern | Detection | Concern |
|---------|-----------|---------|
| 100-500 words removed | Word count diff | Substantial content |
| Paragraph removed | Blank line delimited block | Argument flow |
| Single figure removed | `![` removal | Visual aid lost |
| Sidebar removed | `::: {.sidebar` | Context lost |
| Key term removed | Glossary term in deletion | Concept coverage |
| Example removed | "Example:" or "Consider" context | Pedagogy weakened |

### INFO - Minor Loss (Note Only)

| Pattern | Detection | Usually OK |
|---------|-----------|------------|
| <100 words changed | Word count diff | Normal editing |
| Sentence reworded | Similar word count | Style improvement |
| Redundancy removed | Duplicate content | Intentional cleanup |
| Typo/error fixed | Small deletion | Correction |

## Content Type Detection

### Headers
```regex
^#{1,4}\s+.+$
```
- `#` = Chapter title (BLOCK if removed)
- `##` = Major section (BLOCK if removed)
- `###` = Subsection (WARN if removed)
- `####` = Minor heading (INFO)

### Figures
```regex
!\[.*\]\(.*\)
```
- Check if image file also deleted
- Check if caption contains key info
- WARN minimum, BLOCK if pedagogically critical

### Tables
```regex
\|.+\|
```
- Count rows removed
- WARN if >3 rows deleted
- BLOCK if entire table removed

### Callouts
```regex
::: \{\.callout-(note|tip|warning|important|caution)\}
```
- WARN for any callout deletion
- BLOCK if callout contains definition

### Citations
```regex
\[@[\w_-]+\]
```
- Count citations removed
- WARN if 1-3 removed
- BLOCK if >3 removed without replacement

### Cross-References
```regex
@sec-[\w-]+
```
- Any removal should trigger ref check
- BLOCK if target also removed

### Code Blocks
```regex
```[\w]*\n[\s\S]*?```
```
- WARN if code example removed
- INFO if just formatting change

## Glossary Term Detection

When content is deleted, check if it contains:

**Must preserve first occurrence of:**
- Foundation model, transformer, attention
- Embedding, tokenization, fine-tuning
- Variant, SNP, indel, pathogenic
- auROC, calibration, uncertainty
- Any term from `appendix/appendix-f-glossary.qmd`

## Pedagogical Value Markers

Content more likely to be pedagogically critical:

| Marker | Pattern | Value |
|--------|---------|-------|
| "For example" | Example introduction | High |
| "Consider" | Thought experiment | High |
| "This means" | Explanation | High |
| "In other words" | Clarification | Medium |
| "Specifically" | Detail | Medium |
| Numbers/stats | `\d+%` or specific values | High |
| Comparisons | "unlike", "compared to" | Medium |
| Clinical scenarios | Patient/disease mention | High |

## Replacement Detection

Deletion is less concerning if:

1. **Moved content**: Same text appears elsewhere in diff
2. **Rewritten**: Similar concepts with different words
3. **Consolidated**: Multiple mentions → single authoritative
4. **Updated**: Old info replaced with newer

Check for these before flagging:
```
# Pseudo-logic
if deleted_content appears in additions:
    severity = INFO  # Moved
elif similar_concepts in additions:
    severity = INFO  # Rewritten
else:
    severity = original_severity
```

## False Positive Reduction

Don't flag deletions in:
- Comments (`<!-- ... -->`)
- YAML frontmatter (`---` blocks)
- Empty lines
- Whitespace-only changes
- Import/include statements

## Reporting Template

For each significant deletion:

```markdown
### [SEVERITY]: [File] Lines [X-Y]

**Deleted content** ([N] words):
> [First 100 chars of deleted content]...

**Type**: [Section/Figure/Table/Paragraph/etc.]

**Contains**:
- [ ] Glossary terms: [list]
- [ ] Citations: [count]
- [ ] Cross-references: [list]
- [ ] Examples: [yes/no]

**Replacement found**: [Yes - moved to line X / No]

**Impact assessment**: [Why this matters or doesn't]

**Recommendation**: [Keep deletion / Revert / Review]
```
