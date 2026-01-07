# Section Structure Analyzer

Analyze chapter structure, section depth, and balance.

## Invocation
```
/structure [chapter]
```
- No argument: Analyze entire book structure
- With argument: Deep analysis of specific chapter

## Tasks

1. **Word count by section**: Calculate words per section at each heading level
2. **Identify brief sections**: Flag sections under 150 words (potential merging candidates)
3. **Identify long sections**: Flag sections over 2000 words (potential splitting candidates)
4. **Check heading hierarchy**: Ensure proper nesting (no ### without ##)
5. **Balance analysis**: Compare section lengths within chapters
6. **Depth consistency**: Check heading depth patterns across chapters
7. **Part balance**: Compare chapter lengths within each Part

### Additional Checks (from claude-project-instructions.md)

8. **Orphaned headers**: Detect headers immediately followed by subheaders without intervening prose (min 2-3 sentences required)
9. **Part Introduction length**: Verify Part intros are 300-500 words
10. **Part Introduction structure**: Check for backward references in opening (prohibited: "The preceding parts...", "Part I established...")

## Output

Save report to `meta/reports/structure-YYYY-MM-DD.md` with:

```markdown
# Structure Analysis Report

Generated: [timestamp]

## Book Overview
- Total word count: X
- Total chapters: X
- Average chapter length: X words
- Median chapter length: X words

## Part Balance
| Part | Chapters | Total Words | Avg Words/Chapter |
|------|----------|-------------|-------------------|
| Part I: Foundations | 4 | X | X |
| Part II: Principles | 5 | X | X |
| ... | | | |

## Chapter Word Counts
| Chapter | Words | Sections | Avg Words/Section |
|---------|-------|----------|-------------------|

## Brief Sections (< 150 words) - Review for merging
| File | Section | Words | Suggestion |
|------|---------|-------|------------|
| p3-ch11.qmd | ### Training Corpus Composition | 89 | Consider merging with previous section |

## Long Sections (> 2000 words) - Review for splitting
| File | Section | Words | Suggestion |
|------|---------|-------|------------|

## Heading Hierarchy Issues
| File | Line | Issue |
|------|------|-------|
| ch15.qmd | 234 | ### without parent ## |

## Section Depth Distribution
| Depth | Count | Example |
|-------|-------|---------|
| # (H1) | 29 | Chapter titles |
| ## (H2) | X | Major sections |
| ### (H3) | X | Subsections |

## Unbalanced Chapters (high variance in section lengths)
| Chapter | Shortest Section | Longest Section | Ratio |
|---------|------------------|-----------------|-------|

## Orphaned Headers (no intro before subheader)
| File | Line | Header | Subheader |
|------|------|--------|-----------|
| ch15.qmd | 45 | ## Methods | ### Statistical (no intro) |

## Part Introduction Issues
| Part | Words | Issue |
|------|-------|-------|
| Part II | 250 | Under 300 words |
| Part IV | 45 | Opens with "Building on Part III..." |
```

## Implementation Notes

- Use `scripts/count_book_words.sh` as reference for word counting approach
- Reference `meta/qmd_headings.md` for extracted heading structure
- Reference `meta/_instructions/claude-project-instructions.md` for orphaned header and Part Introduction rules
- TODO/notes.md contains specific notes about sections being "too brief"
- Consider callouts and sidebars separately from prose sections
- Part Introduction requirements: 300-500 words, no backward references, clear unifying theme
