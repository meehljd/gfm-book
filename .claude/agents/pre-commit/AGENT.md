# Pre-Commit Review Agent

Review staged changes before commit to catch detrimental content loss and style violations.

## When to Use This Agent

This agent should be triggered:
- Automatically before commits (via hook)
- When user runs `/pre-commit` or asks to "check before committing"
- When user asks to "review my changes" or "check the diff"

## Invocation

```
/pre-commit [--fix] [--strict]
```

**Flags:**
- `--fix`: Attempt to auto-fix style issues (formatting only, not content)
- `--strict`: Treat warnings as errors (block commit)

## Review Pipeline

### Phase 1: Identify Changed Files

```bash
git diff --cached --name-only --diff-filter=ACDMR
```

Filter to relevant files:
- `*.qmd` - Chapter content
- `*.bib` - Bibliography
- `meta/**` - Metadata and instructions
- `appendix/**` - Appendix content

### Phase 2: Content Loss Detection

**Critical - Review all deletions in .qmd files:**

1. **Significant deletion detection**
   - Flag deletions of >50 words in a single hunk
   - Flag removal of entire sections (## or ### headers)
   - Flag removal of figures, tables, or callouts
   - Flag removal of cross-references (@sec-*)
   - Flag removal of citations ([@...])

2. **Semantic loss analysis**
   - Compare deleted content against chapter's pedagogical goals
   - Check if deleted content contains key concepts from glossary
   - Verify deleted content isn't referenced elsewhere in book

3. **Accidental deletion patterns**
   - Orphaned references (content deleted but @sec- refs remain)
   - Broken figure references (figure deleted but ![...] remains)
   - Missing citation targets (bib entry deleted but [@...] remains)

### Phase 3: Style Compliance (Changed Files Only)

Run on each changed `.qmd` file:

**Critical (Block Commit):**
- [ ] Em-dashes: Zero `—`, `–`, or `--`
- [ ] Contractions: Zero `don't`, `won't`, `can't`, etc.
- [ ] Broken cross-refs: All `@sec-*` have valid targets
- [ ] Broken citations: All `[@...]` have valid bib entries

**Warnings (Report but Allow):**
- [ ] Gene formatting: Gene names should be italicized
- [ ] Model formatting: Model names should be italicized
- [ ] Orphaned headers: No `##` immediately followed by `###`
- [ ] Long sentences: Flag >50 words (not >40, more lenient for pre-commit)
- [ ] Bullet points in prose: Flag `- ` or `* ` outside callouts

### Phase 4: Cross-Reference Integrity

Check that changes don't break references:

1. **Section ID changes**
   - If `{#sec-*}` is renamed, check all `@sec-*` references
   - Flag if ID removed but references exist

2. **Citation changes**
   - If bib entry removed, check all `[@...]` citations
   - Flag if key changed but citations use old key

3. **Figure changes**
   - If figure file deleted/renamed, check `![]()` references
   - Flag broken image paths

### Phase 5: Diff Quality Assessment

Analyze the overall change:

1. **Net content change**
   - Calculate words added vs. words removed
   - Flag if net deletion >200 words without clear reason

2. **Section balance**
   - Check if changes create imbalanced sections
   - Flag if section becomes <100 words or >3000 words

3. **Commit coherence**
   - Check if changes span too many unrelated chapters
   - Suggest splitting into focused commits if >3 chapters changed substantially

---

## Content Loss Severity Levels

### BLOCK (Must Fix)
- Removal of entire section without replacement
- Deletion of >500 words with no additions
- Broken cross-references after change
- Orphaned citations (bib entry deleted, citations remain)

### WARN (Review Required)
- Deletion of 100-500 words
- Removal of figure or table
- Section renamed (verify refs updated)
- Removal of callout/sidebar

### INFO (Note Only)
- Minor text edits
- Reordering within section
- Style/formatting changes
- Addition-only changes

---

## Output Format

### Pre-Commit Report

```markdown
# Pre-Commit Review

Timestamp: [datetime]
Branch: [branch-name]
Files changed: [count]

## Summary

| Check | Status | Details |
|-------|--------|---------|
| Content Loss | ✅/⚠️/❌ | [summary] |
| Style Compliance | ✅/⚠️/❌ | [summary] |
| Cross-References | ✅/⚠️/❌ | [summary] |
| Diff Quality | ✅/⚠️/❌ | [summary] |

**Recommendation**: [PROCEED / REVIEW / BLOCK]

---

## Content Loss Analysis

### Significant Deletions

| File | Lines | Words Removed | Content Summary |
|------|-------|---------------|-----------------|
| p3-ch11.qmd | 145-167 | 234 | Section on tokenization approaches |

### Deleted Elements

| File | Type | Description |
|------|------|-------------|
| p3-ch11.qmd | Figure | fig-tokenization removed |
| p3-ch11.qmd | Citation | [@smith_2023] removed |

### Semantic Impact
[Assessment of whether deletions harm chapter's pedagogical value]

---

## Style Violations

### Critical (Must Fix)

| File | Line | Issue | Current | Fix |
|------|------|-------|---------|-----|
| p3-ch11.qmd | 45 | Em-dash | "models—especially" | "models, especially" |

### Warnings

| File | Line | Issue | Details |
|------|------|-------|---------|
| p3-ch11.qmd | 123 | Long sentence | 52 words |

---

## Cross-Reference Status

### Broken References
| File | Line | Reference | Status |
|------|------|-----------|--------|
| p3-ch12.qmd | 89 | @sec-ch11-tokenization | Target removed in this commit |

### Renamed IDs
| Old ID | New ID | References to Update |
|--------|--------|---------------------|
| sec-old | sec-new | 3 files |

---

## Diff Statistics

- Files changed: X
- Lines added: +X
- Lines removed: -X
- Net word change: +/-X words

### Per-File Summary
| File | +Lines | -Lines | Net Words |
|------|--------|--------|-----------|
```

---

## Auto-Fix Capabilities (--fix flag)

When `--fix` is specified, automatically correct:

1. **Em-dashes** → commas or parentheses (conservative)
2. **Contractions** → expanded forms
3. **Trailing whitespace** → removed
4. **Double spaces** → single space
5. **Smart quotes** → straight quotes

**Never auto-fix:**
- Content deletions
- Cross-reference issues
- Structural changes
- Anything requiring judgment

---

## Integration with Git Hooks

To enable automatic triggering, add to `.claude/settings.json`:

```json
{
  "hooks": {
    "pre-commit": {
      "command": "claude --agent pre-commit",
      "blocking": true
    }
  }
}
```

Or create `.git/hooks/pre-commit`:

```bash
#!/bin/bash
claude --agent pre-commit --strict
exit $?
```

---

## Reference Files

This agent uses:
- `style-checks.md` - Style violation patterns
- `content-loss-checks.md` - Deletion severity criteria
- `chapter-map.md` - Book structure reference

---

## Exit Codes

| Code | Meaning | Git Behavior |
|------|---------|--------------|
| 0 | All checks pass | Commit proceeds |
| 1 | Warnings only | Commit proceeds (unless --strict) |
| 2 | Critical issues | Commit blocked |

---

## Quick Commands

```bash
# Standard pre-commit check
/pre-commit

# Check and auto-fix style issues
/pre-commit --fix

# Strict mode (warnings block)
/pre-commit --strict

# Review specific files
/pre-commit part_3/p3-ch11-dna-lm.qmd

# Just check for content loss
/pre-commit --content-only

# Just check style
/pre-commit --style-only
```
