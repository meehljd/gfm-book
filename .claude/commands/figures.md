# Figure Inventory

Track figures, placeholders, and specifications.

## Invocation
```
/figures [chapter]
```
- No argument: Inventory entire book
- With argument: Focus on specific chapter

## Tasks

1. **Extract figure references**: Find all `![caption](path)` patterns in `.qmd` files
2. **Inventory actual files**: List all files in `figs/` directory
3. **Match references to files**: Identify which references have corresponding files
4. **Find missing figures**: References without files
5. **Find orphaned files**: Files not referenced in any `.qmd`
6. **Check watermark status**: Identify placeholder vs. final figures
7. **Generate specifications**: For missing figures, create description templates

### Figure Category Analysis (from claude-project-instructions.md)

8. **Categorize by type**: Classify figures as architectural diagrams, performance plots, conceptual figures, or clinical workflows
9. **Check specification quality**: Verify figure descriptions are high-level, not pixel-level specifications

## Output

Save report to `meta/reports/figures-YYYY-MM-DD.md` with:

```markdown
# Figure Inventory Report

Generated: [timestamp]

## Summary
- Total figure references: X
- Actual figure files: X
- Missing figures: X
- Orphaned files: X
- Placeholder figures: X
- Final figures: X

## Figure References by Chapter
| Chapter | Figure Count | Status |
|---------|--------------|--------|
| p1-ch01 | 5 | 3 final, 2 placeholder |
| ... | | |

## Missing Figures (referenced but no file)
| File | Line | Reference Path | Caption |
|------|------|----------------|---------|

## Orphaned Files (exist but not referenced)
| Path | Size | Modified |
|------|------|----------|

## Placeholder Figures (need replacement)
| Path | Referenced In | Caption |
|------|---------------|---------|

## Figure Specifications Needed
For each missing or placeholder figure, generate:

### [Figure ID]
- **Chapter**: [chapter name]
- **Location**: [section where it appears]
- **Caption**: [from source]
- **Suggested content**: [based on surrounding text]
- **Type**: [diagram/chart/schematic/photo]
- **Dependencies**: [other figures it relates to]
```

## Implementation Notes

- Figures are in `figs/` organized by part (e.g., `figs/part_3/ch11/`)
- Recent commits used `scripts/watermark_pngs.py` to add "PLACEHOLDER" watermarks
- Figure captions are in the `.qmd` files, not separate files
- Check for both `![](path)` and `![[caption]](path)` patterns
- Reference `meta/_instructions/claude-project-instructions.md` for visual recommendation guidelines

### Figure Types (from instructions)

- **Architectural diagrams**: Model structure, layer connections, data flow, attention patterns
- **Performance plots**: Benchmark comparisons, scaling curves, ablation studies, error analysis
- **Conceptual figures**: Abstract concepts made concrete, biological processes, failure modes
- **Clinical workflows**: Application pipelines, integration with clinical tools, validation approaches
