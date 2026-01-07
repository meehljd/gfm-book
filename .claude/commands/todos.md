# TODO Organizer

Parse and organize editing tasks from TODO/notes.md.

## Invocation
```
/todos [chapter]
```
- No argument: Organize all TODOs
- With argument: Focus on specific chapter's TODOs

## Tasks

1. **Parse TODO/notes.md**: Extract structured items from the 405-line notes file
2. **Categorize by type**: Structure, clarity, citation, content, figure, cross-reference
3. **Prioritize items**: Based on impact and effort indicators
4. **Group by chapter**: Organize tasks by chapter for focused work sessions
5. **Track status**: Identify which items may have been addressed in recent commits
6. **Generate work sessions**: Create focused task lists for editing sessions

## Output

Save report to `meta/reports/todos-YYYY-MM-DD.md` with:

```markdown
# TODO Organization Report

Generated: [timestamp]

## Summary
- Total items: X
- By priority: High (X), Medium (X), Low (X)
- By type: Structure (X), Clarity (X), Citation (X), Content (X), Figure (X), Cross-ref (X)
- Potentially completed: X (based on recent git activity)

## High Priority Items
| Chapter | Type | Description | Effort |
|---------|------|-------------|--------|

## Items by Chapter

### Chapter 10: Foundation Model Principles
| Type | Description | Line in notes.md |
|------|-------------|------------------|
| Structure | Subsections too brief | 45 |
| Clarity | Section titles ambiguous | 47 |

### Chapter 11: DNA Language Models
...

## Items by Type

### Structure Issues
| Chapter | Description |
|---------|-------------|

### Clarity Issues
| Chapter | Description |
|---------|-------------|

### Citation Needs
| Chapter | Description |
|---------|-------------|

## Suggested Work Sessions

### Session 1: Part 3 Structure (Est. 2 hours)
- [ ] Ch10: Expand brief subsections
- [ ] Ch11: Add benchmark cross-references
- [ ] Ch12: Improve table clarity

### Session 2: Part 4 Content (Est. 3 hours)
...

## Recurring Patterns
Issues that appear across multiple chapters:
- **Redundancy**: ClinVar mentioned in Ch4, Ch14, Ch20, Ch26
- **Missing sidebars**: ACMG (Ch14), Experimental assays (Ch13)
```

## Implementation Notes

- Main source: `TODO/notes.md` (405 lines of chapter-by-chapter notes)
- Cross-reference with `meta/cross-reference-proposals.md` for related work
- Reference `meta/_instructions/claude-project-instructions.md` for priority categorization criteria
- Check git log for recent commits that may have addressed items
- Pattern indicators in notes: "too brief", "needs", "missing", "unclear", "redundant"

### Priority Criteria (from instructions)

- **High**: Em-dashes, bullet points in prose, meta-commentary, weak "Lead with Why" openings
- **Medium**: Typography issues (gene/model formatting), abbreviation expansion, cross-reference gaps
- **Low**: Minor style refinements, optional enhancements
