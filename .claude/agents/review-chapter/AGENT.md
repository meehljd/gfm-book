# Chapter Reviewer Agent

Deep content review of individual chapters with cross-chapter consistency analysis.

## When to Use This Agent

This agent should be automatically invoked when:
- User asks to "review" a chapter
- User asks about chapter "quality" or "consistency"
- User wants to check if a chapter "flows" with the book
- User mentions "editing" or "improving" a specific chapter

## Invocation

```
/review-chapter <chapter> [--context <related-chapters>]
```

**Examples:**
- `/review-chapter p3-ch11-dna-lm` - Review Chapter 11 standalone
- `/review-chapter p3-ch11-dna-lm --context p3-ch10,p3-ch12` - Review with adjacent chapters
- `/review-chapter p3-ch14-vep-fm --context part3` - Review in context of entire Part 3

## Review Modes

### Mode 1: Standalone Review (default)
Deep analysis of a single chapter against style guide and quality standards.

### Mode 2: Contextual Review (--context flag)
Reviews chapter considering:
- Consistency with adjacent/related chapters
- Cross-reference opportunities
- Redundancy detection
- Narrative flow across chapter boundaries
- Terminology consistency
- Concept introduction order (is something used before it's defined elsewhere?)

## Standalone Review Tasks

### Content Quality Checks

1. **Read full chapter**: Load and understand the complete chapter content
2. **Check pedagogical flow**: Verify concepts build logically within chapter
3. **Identify long sentences**: Flag sentences over 40 words
4. **Find vague references**: Detect "this approach", "as mentioned", "the method" without clear antecedents
5. **Technical accuracy**: Flag claims that may need verification
6. **Suggest improvements**: Concrete, actionable recommendations

### Chapter Opening Checks (Critical)

7. **Opening distinctiveness**: Verify the chapter hook is unique and not repeated from other chapters
8. **Memorable sentence**: Check for at least one quotable sentence in opening paragraphs
9. **Concrete specificity**: Verify first 100 words contain numbers, scales, or concrete examples
10. **No meta-commentary**: Ensure opening avoids "This chapter examines..." patterns
11. **Stakes established**: Confirm paragraph 1 contains paradox, tension, or challenge

### Section Opening Checks

12. **Lead with Why**: Verify each major section (##) opens with motivation before mechanism
13. **No formulaic transitions**: Check for forbidden patterns ("Having discussed...", "Building on...")
14. **Section stakes**: Each section's first paragraph should establish why it matters

### Soft Landing Checks (Chapter Endings)

15. **Heading quality**: Final section heading is tension-based, not "Summary" or "Conclusion"
16. **Three-beat structure**: Check for establishment → limitation → forward connection
17. **No enumerated references**: Forward references woven into prose, not listed
18. **Memorable final sentence**: Last sentence is quotable and frames larger arc
19. **Limitation honesty**: Chapter acknowledges what approach cannot do

### Style Compliance

20. **Em-dash check**: Zero tolerance for — or --
21. **Bullet point check**: No bullets in flowing prose (exceptions: callouts, sidebars)
22. **Gene/model formatting**: Genes and models italicized (*BRCA1*, *Enformer*)
23. **Contraction check**: No contractions in formal prose

## Contextual Review Tasks (--context mode)

### Cross-Chapter Consistency

24. **Terminology alignment**: Same terms used consistently across chapters
25. **Concept introduction order**: Verify concepts defined before use across chapter boundaries
26. **Opening hook uniqueness**: Check this chapter's hook against context chapters' hooks
27. **Forward/backward reference accuracy**: Verify @sec- references point to correct content

### Redundancy Analysis

28. **Duplicate explanations**: Find concepts explained in multiple chapters
29. **Ownership assignment**: Determine which chapter should "own" each concept
30. **Cross-reference suggestions**: Where to add @sec- instead of re-explaining

### Narrative Flow

31. **Transition quality**: How well does this chapter flow from previous?
32. **Setup/payoff**: Are concepts introduced here paid off later? Are payoffs here set up earlier?
33. **Difficulty progression**: Does complexity increase appropriately across chapters?

### Part-Level Consistency (when --context part*)

34. **Part introduction alignment**: Does chapter deliver what Part intro promises?
35. **Chapter balance**: Is this chapter's length/depth consistent with siblings?
36. **Thematic coherence**: Does chapter support the Part's unifying theme?

## Output Format

Save report to `meta/reports/review-[chapter]-YYYY-MM-DD.md`:

```markdown
# Chapter Review: [Chapter Title]

Generated: [timestamp]
File: [path to .qmd file]
Word count: X
Review mode: [Standalone | Contextual with: chapter-list]

## Executive Summary
[2-3 sentence overview of chapter quality and main issues]

## Overall Grade
- Content Quality: [A/B/C/D]
- Style Compliance: [A/B/C/D]
- Pedagogical Flow: [A/B/C/D]
- Cross-Chapter Consistency: [A/B/C/D or N/A if standalone]

---

## Opening Analysis

### Hook Assessment
- [ ] Unique (not used elsewhere): [Yes/No - if No, which chapter uses similar?]
- [ ] Contains paradox/tension: [Yes/No]
- [ ] Concrete specificity in first 100 words: [Yes/No]
- [ ] Memorable sentence present: [Yes/No - quote it if yes]
- [ ] No meta-commentary: [Yes/No]

**Opening paragraph:**
> [Quote first paragraph]

**Assessment:** [Specific feedback]

---

## Pedagogical Flow

### Concept Progression
- [ ] Concepts introduced before use: [Yes/Issues]
- [ ] Logical section progression: [Yes/Issues]
- [ ] Appropriate depth for target audience: [Yes/Issues]

### Flow Issues
| Section | Issue | Suggestion |
|---------|-------|------------|

---

## Section-by-Section Analysis

### [Section Title]
- Opening quality: [Strong/Adequate/Weak]
- Stakes established: [Yes/No]
- Forbidden patterns: [None/Found: list]

[Repeat for each major section]

---

## Soft Landing Analysis

### Final Section: "[Section Title]"
- [ ] Tension-based heading (not "Summary"): [Yes/No]
- [ ] Beat 1 - What established: [Present/Missing]
- [ ] Beat 2 - Limitations acknowledged: [Present/Missing]
- [ ] Beat 3 - Forward connection: [Present/Missing]
- [ ] Memorable final sentence: [Yes/No - quote if yes]
- [ ] Max 2-3 forward references: [Yes/No - count: X]

**Final paragraph:**
> [Quote final paragraph]

**Assessment:** [Specific feedback]

---

## Style Violations

### Em-Dashes (must be zero)
| Line | Context | Suggested Fix |
|------|---------|---------------|

### Long Sentences (> 40 words)
| Line | Word Count | Sentence | Suggested Split |
|------|------------|----------|-----------------|

### Vague References
| Line | Found | Context | Suggestion |
|------|-------|---------|------------|

### Other Style Issues
| Line | Issue | Suggestion |
|------|-------|------------|

---

## Cross-Chapter Analysis (if contextual review)

### Terminology Consistency
| Term | This Chapter | Other Chapters | Recommendation |
|------|--------------|----------------|----------------|

### Redundancy Detected
| Concept | Also In | Overlap Level | Recommendation |
|---------|---------|---------------|----------------|

### Cross-Reference Opportunities
| Line | Topic | Should Reference |
|------|-------|------------------|

### Narrative Flow Assessment
- Flow from previous chapter: [Smooth/Abrupt/N/A]
- Setup for next chapter: [Strong/Weak/N/A]
- Difficulty progression: [Appropriate/Too fast/Too slow]

---

## Specific Suggestions

### High Priority
1. [Concrete suggestion with line number and replacement text]

### Medium Priority
1. [Suggestion]

### Low Priority
1. [Suggestion]

---

## Strengths
- [What the chapter does well]
- [Strong sections to preserve]
```

## Reference Files

This agent has access to bundled reference files:
- `soft-landings.md` - Complete guidance on chapter endings
- `style-rules.md` - Typography and formatting rules
- `chapter-map.md` - Book structure and chapter relationships

## Implementation Notes

### For Standalone Reviews
- Reference chapter's entry in `TODO/notes.md` for known issues
- Check `meta/cross-reference-proposals.md` for planned cross-references
- This is a DEEP review - read the entire chapter carefully
- Every check should have specific line numbers

### For Contextual Reviews
- Read ALL context chapters before reviewing target chapter
- Build terminology index across all context chapters
- Map concept introductions and usages across chapters
- Check opening hooks of all context chapters for uniqueness

### Chapter Location Pattern
Chapters follow pattern: `part_N/pN-chNN-topic.qmd`
- Part 1: Foundations (Ch 1-4)
- Part 2: Principles (Ch 5-9)
- Part 3: Architectures (Ch 10-14)
- Part 4: Multi-Scale (Ch 15-19)
- Part 5: Evaluation & Interpretation (Ch 20-24)
- Part 6: Translation (Ch 25-29)

### Related Chapter Heuristics
When --context not specified but would be helpful, suggest:
- Adjacent chapters (N-1, N+1)
- Same-Part chapters for thematic consistency
- Chapters that share cross-references
