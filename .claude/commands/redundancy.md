# Redundancy Detector

Find repeated content and explanations across chapters.

## Invocation
```
/redundancy [topic]
```
- No argument: Scan for all redundancy
- With argument: Focus on specific topic (e.g., `ClinVar`, `attention`, `calibration`)

## Tasks

1. **Identify repeated concepts**: Find explanations that appear in multiple chapters
2. **Measure overlap**: Quantify how similar the explanations are
3. **Categorize redundancy**:
   - Necessary (background in each chapter)
   - Consolidatable (should be in one place with cross-refs)
   - Contradictory (different explanations that conflict)
4. **Generate recommendations**: Suggest which chapter should "own" each concept
5. **Cross-reference suggestions**: Where to add `@sec-` references instead of re-explaining

## Known Redundancy Areas (from TODO/notes.md)

- **ClinVar**: Appears in Ch4, Ch14, Ch20, Ch26
- **Phenotype quality issues**: Multiple chapters
- **Calibration concepts**: Ch14 and Ch23
- **Attention mechanism**: Ch7, Ch10, Ch11, Ch12
- **Transfer learning**: Ch9 and various Part 3 chapters
- **Benchmark limitations**: Ch20 and individual model chapters

## Output

Save report to `meta/reports/redundancy-YYYY-MM-DD.md` with:

```markdown
# Redundancy Analysis Report

Generated: [timestamp]

## Summary
- Concepts appearing in 3+ chapters: X
- High-overlap passages: X
- Consolidation opportunities: X
- Cross-reference suggestions: X

## Redundancy by Concept

### ClinVar
**Appears in**: Ch4 (line 234), Ch14 (line 567), Ch20 (line 123), Ch26 (line 89)
**Overlap level**: High (similar explanations)
**Recommendation**: Primary explanation in Ch4, cross-reference elsewhere
**Suggested changes**:
- Ch14: Replace lines 567-572 with "As described in @sec-ch04-clinvar, ClinVar provides..."
- Ch20: Add brief mention with cross-reference
- Ch26: Keep clinical context, add cross-reference for background

### Attention Mechanism
**Appears in**: Ch7 (primary), Ch10, Ch11, Ch12
**Overlap level**: Medium
**Recommendation**: Ch7 owns the concept; others reference
...

## High-Overlap Passages

### Passage 1
**Locations**:
- `part_1/p1-ch04.qmd:234-245`
- `part_3/p3-ch14.qmd:567-578`

**Similarity**: 85%
**Content**: [First 100 chars of the passage]
**Recommendation**: Consolidate in Ch4, reference from Ch14

## Cross-Reference Suggestions
| From Chapter | Line | Topic | Add Reference To |
|--------------|------|-------|------------------|
| Ch14 | 567 | ClinVar | @sec-ch04-clinvar |
| Ch23 | 234 | Calibration basics | @sec-ch14-calibration |

## Necessary Redundancy (keep as-is)
Some concepts legitimately need re-introduction:
| Concept | Chapters | Rationale |
|---------|----------|-----------|
| What is a foundation model | Ch10, Ch16 | Different contexts (DNA vs single-cell) |
```

## Implementation Notes

- Use fuzzy string matching to detect similar passages
- Check `meta/cross-reference-proposals.md` for planned consolidation
- Reference TODO/notes.md for known redundancy issues
- Consider chapter reading order - earlier chapters should "own" foundational concepts
- Part introductions may intentionally summarize content
