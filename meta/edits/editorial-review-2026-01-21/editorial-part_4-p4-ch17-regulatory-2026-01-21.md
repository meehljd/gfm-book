# Editorial Review: part_4/p4-ch17-regulatory.qmd

Extracted from agent: acaf8c8

---

I need to use a different method to save the file. Let me check for available tools.

I apologize - I do not have the Write tool available in this environment. I can only use Read, Grep, and Glob tools. Let me provide the complete editorial report that should be saved to `/root/gfm-book/meta/reports/editorial-p4-ch17-2026-01-21.md`:

---

# Editorial Board Review: Chapter 17 - Regulatory Models

**Generated:** 2026-01-21  
**Scope:** /root/gfm-book/part_4/p4-ch17-regulatory.qmd  
**Focus:** Full editorial review  
**Depth:** Comprehensive

---

## Executive Summary

**Overall Assessment:** Ready (Minor Revisions)

**Key Findings:**
1. Strong pedagogical structure with excellent use of callouts for active learning
2. Minor style violations: two em-dash instances (line 43, 260) and one "Notably" usage (line 191)
3. Well-balanced coverage of four major models with appropriate forward/backward references
4. Missing citation for ChromHMM claim (line 260)

**Readiness by Dimension:**

| Dimension | Grade | Status |
|-----------|-------|--------|
| Structural Quality | A | Excellent section organization with tension-based closing |
| Prose Polish | A- | Minor em-dash issues; otherwise clean |
| Pedagogical Effectiveness | A | Outstanding retrieval practice and active learning elements |
| Visual Communication | A- | 7 figures, 2 tables; appropriate figure placement |
| Citation Integrity | A- | One unsupported claim; otherwise well-cited |
| Content Efficiency | A | ~7,500 words; appropriate for scope |

---

## Chapter Auditor Report

**Grade: A**

### Opening Analysis

The chapter opens with a compelling hook (line 3 epigraph: "Gene regulation happens at distances that most models cannot see") that establishes the central tension immediately. The opening paragraph (line 21) uses concrete numbers (80 kilobases, 50 kilobases, 200 kilobases) within the first 100 words.

**Strengths:**
- Paradox established in first paragraph: models that work well locally fail systematically for long-range tasks
- Unique hook compared to other chapters (marionette analogy in line 30)
- Learning objectives are specific and measurable (lines 12-16)

### Section Structure

| Section | Lines | Content Assessment |
|---------|-------|-------------------|
| Long-Range Regulation Problem | 28-73 | Excellent problem framing with marionette analogy |
| Enformer | 75-198 | Comprehensive architecture + training + VEP coverage |
| Borzoi | 200-251 | Clear differentiation from Enformer (RNA-seq vs CAGE) |
| Sei | 254-301 | Good contrast with track-prediction models |
| AlphaGenome | 303-355 | Balanced treatment of capabilities and access limitations |
| What Hybrid Architectures Accomplish | 357-380 | Effective synthesis |
| Limitations and Open Challenges | 382-430 | Five limitations clearly articulated |
| Relationship to Foundation Models | 433-443 | Good positioning within Part 4 arc |
| Prediction Without Explanation | 446-529 | Tension-based soft landing (excellent) |

### Soft Landing Assessment

**Heading:** "Prediction Without Explanation" (line 446)
- Tension-based: Yes
- Quotable: Yes
- Avoids forbidden headings: Yes

### Style Rule Compliance

| Rule | Status | Details |
|------|--------|---------|
| Zero em-dashes | VIOLATION | Line 43: `--`; Line 260: `---` |
| Zero bullets in prose | PASS | Bullets only in callouts and tables |
| Zero meta-commentary | PASS | No "Let's examine" or similar |
| Lead with Why | PASS | Each section opens with motivation |
| Italics for model names | PASS | Correctly italicized |
| No contractions | PASS | None found |

---

## Textbook Editor Report

**Grade: A-**

### Line Editing Issues

| Line | Issue | Severity | Suggested Fix |
|------|-------|----------|---------------|
| 43 | Em-dash (double hyphen) | Critical | Change `--` to semicolon or period |
| 191 | "Notably" sentence starter | Medium | Remove "Notably" |
| 260 | Em-dash (triple hyphen) | Critical | Change `---` to period or semicolon |

### Word Choice Assessment

| Word | Lines | Assessment |
|------|-------|------------|
| "comprehensive" | 281, 305, 307, 348, 354 | 5 occurrences - Claude tell-word, but justified in context |
| "paradigm" | 202, 238, 305 | 3 occurrences - acceptable for technical discussion |
| "interesting" | 435 | Consider rewording |

---

## Pedagogy Review Report

**Grade: A**

### Learning Science Principle Application

| Principle | Implementation | Assessment |
|-----------|----------------|------------|
| Cognitive Load | Chunked into 7 major sections | Excellent |
| Retrieval Practice | 7 knowledge check callouts | Outstanding |
| Interleaving | Explicit model comparisons (Table 2) | Good |
| Spacing | Backward refs to Ch6, Ch7; forward to Ch18, Ch21, Ch25 | Excellent |
| Dual Coding | 7 figures + 2 tables | Excellent |
| Desirable Difficulties | Prediction prompts before reveals | Excellent |

### Retrieval Practice Inventory

| Type | Count | Lines |
|------|-------|-------|
| Stop and Think | 3 | 32, 206, 309 |
| Knowledge Check | 5 | 93, 162, 220, 285, 386 |
| Predict Before You Look | 1 | 48 |
| Apply Your Knowledge | 1 | 454 |
| Test Yourself | 1 | 460 |

**Total active learning elements: 11** - Outstanding for chapter length

---

## Fact Checker Report

**Grade: A-**

### Citation Analysis

All major model claims properly cited:
- @gasperini_genome-wide_2019 for enhancer-promoter distances
- @maurano_systematic_2012 for GWAS regulatory enrichment
- @avsec_enformer_2021 for Enformer
- @linder_borzoi_2025 for Borzoi
- @chen_deepsea_2022 for Sei
- @avsec_alphagenome_2025 for AlphaGenome

### Unsupported Claims

| Line | Claim | Recommendation |
|------|-------|----------------|
| 260 | "Previous methods like ChromHMM" | Add @ernst_chromhmm_2012 |

---

## Prose Doctor Report

**Grade: A-**

### Critical Issues

| Symptom | Count | Lines |
|---------|-------|-------|
| Em-dashes | 2 | 43, 260 |
| Meta-commentary | 0 | - |
| False enthusiasm | 0 | - |

### Em-Dash Fixes Required

1. **Line 43:** `not a minor inconvenience--it is` 
   - Fix: `not a minor inconvenience; it is`

2. **Line 260:** `"partially open"---it is`
   - Fix: `"partially open." It is`

### AI Probability Assessment: **Low**

The prose reads naturally with consistent voice and minimal AI writing tells.

---

## Prioritized Action Items

### Critical (Before Any Release)

1. [ ] **Line 43:** Replace `--` with semicolon or period
2. [ ] **Line 260:** Replace `---` with period or semicolon

### High (Before Publication)

3. [ ] **Line 260:** Add citation for ChromHMM
4. [ ] **Line 191:** Remove "Notably"

### Medium (Should Address)

5. [ ] **Line 435:** Consider rewording "interesting position"

### Low (Nice to Have)

6. [ ] Add "Common Misconception" callout distinguishing context window from receptive field

---

## Review Coverage

| Agent | Status | Grade |
|-------|--------|-------|
| Chapter Auditor | Complete | A |
| Textbook Editor | Complete | A- |
| Pedagogy Review | Complete | A |
| Fact Checker | Complete | A- |
| Prose Doctor | Complete | A- |

---

**Report generated by Editorial Board Agent**  
**Chapter file:** `/root/gfm-book/part_4/p4-ch17-regulatory.qmd`

---

## Summary

The chapter is in excellent shape overall. The two **critical fixes** are the em-dash replacements on lines 43 and 260. The **high priority** items are adding the ChromHMM citation and removing the "Notably" transition. After these four fixes, the chapter would achieve an overall **A grade** and be ready for publication.

The pedagogical structure is outstanding with 11 active learning elements including Stop and Think prompts, Knowledge Checks with collapsed answers, and a comprehensive Test Yourself section. The chapter's treatment of model limitations (5 clearly articulated constraints) demonstrates intellectual honesty that will serve readers well.
