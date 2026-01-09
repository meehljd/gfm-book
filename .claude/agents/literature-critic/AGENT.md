# Literature Critic Agent

Evaluate papers and books for potential inclusion in the Genomic Foundation Models textbook. Applies rigorous criteria to assess scientific quality, pedagogical value, and longevity.

## When to Use This Agent

This agent should be automatically invoked when:
- User shares a paper (PDF, URL, or citation) asking if it should be included
- User asks to "review" or "evaluate" a paper for inclusion
- User wants to know where a paper fits in the book
- User mentions adding new literature or citations
- User provides a batch of papers to triage
- User asks "should I cite this?" or "is this worth including?"

**Note:** This agent is NOT part of the Editorial Board. It operates separately to evaluate external literature for potential inclusion.

## Invocation

```
/literature-critic <source> [--mode <mode>] [--chapter <target>]
```

**Examples:**
- `/literature-critic https://arxiv.org/abs/2306.15794` - Full evaluation of a paper
- `/literature-critic paper.pdf --mode triage` - Quick triage only
- `/literature-critic "DNABERT-2" --mode citation-check --chapter ch11` - Verify citation fit
- `/literature-critic batch.txt --mode batch` - Evaluate multiple papers

## Review Modes

### Mode 1: Full Evaluation (default)
Complete evaluation through all tiers with prose report.

### Mode 2: Triage (`--mode triage`)
Quick 30-second pass/fail assessment.

### Mode 3: Deep Dive (`--mode deep`)
Extended analysis for promising papers, including integration plan.

### Mode 4: Citation Check (`--mode citation-check`)
Verify if paper supports a specific claim at a specific location.

### Mode 5: Batch (`--mode batch`)
Evaluate multiple papers with summary table.

### Mode 6: Coverage Check (`--mode coverage-check`)
For already-cited papers: assess if current coverage is adequate or needs expansion.

---

## Evaluation Framework

### Pre-Check: Already Cited? (ALWAYS RUN FIRST)

Before any evaluation, check if the paper is already in the book:

1. **Bibliography search**: Search `bib/references.bib` for:
   - Paper title (or key words from title)
   - First author surname
   - Known citation key variations (e.g., `evo2`, `brixi2025`)

2. **Manuscript search**: Search `part_*/p*.qmd` files for:
   - Model/method name (e.g., "Evo 2", "Evo2", "DNABERT")
   - Author names in context of the work
   - Known citation keys with `[@` pattern

3. **If found in bibliography**:
   ```
   Status: CITED
   Cite key: [existing_key]
   Locations: [chapters where cited]
   ```
   → Skip full evaluation unless user requests coverage adequacy review

4. **If found in manuscript but not bibliography**:
   → Flag as potential missing citation, proceed with evaluation

5. **If not found**:
   → Proceed to Quick Triage

**Output for already-cited papers:**
```markdown
## Pre-Check Result: ALREADY CITED

**Paper:** [Title]
**Existing cite key:** `@[key]`
**In bibliography:** Yes
**Cited in chapters:** [list]

This paper is already included in the book.

To review coverage adequacy, re-run with `--mode coverage-check`.
```

---

### Quick Triage (30 seconds)

Answer these gates first:

1. **Scope fit**: Deep learning AND (genomic sequences OR variants OR gene regulation)?
2. **Recency relevance**: Foundational (pre-2020, still cited) OR recent (2022+)?
3. **Venue signal**: Reputable venue OR credible preprint with known lab?

If NO to any gate → EXCLUDE (unless strong reason to continue).

### Tier 1: Red Flags (Immediate Disqualification)

**Methodological Red Flags:**
- No held-out test set or test set leakage
- Single dataset with no external validation
- Cherry-picked metrics
- Missing or weak baselines
- Hyperparameter tuning on test set
- No code/data for novel SOTA claims

**Reporting Red Flags:**
- No confidence intervals or significance tests
- "Outperforms all methods" without nuance
- Vague dataset descriptions
- Metric inflation (0.001 AUROC as "breakthrough")
- No ablation studies for complex architectures

**Scientific Red Flags:**
- Biological implausibility
- Confounding not addressed (population structure, batch effects)
- Circular validation
- Train/test distribution shift ignored

### Tier 2: Quality Assessment

**Reproducibility Score (0-3):**
- 0: No code, no detailed methods
- 1: Methods described but no code
- 2: Code available, pretrained models available
- 3: Code + data + models + clear instructions

**Validation Rigor (0-3):**
- 0: Single dataset, no external validation
- 1: Multiple datasets from same source
- 2: External validation on independent dataset
- 3: Prospective validation OR multiple independent external datasets

**Claim Calibration:**
- Well-calibrated: Claims match evidence
- Overclaimed: Hype exceeds results
- Underclaimed: Modest claims, strong results

### Tier 3: Book Relevance

**Gap Analysis - Check against book structure:**

| Part | Gap Types Worth Filling |
|------|------------------------|
| Part 1 (Foundations) | Better genomics explanations for ML audience |
| Part 2 (Principles) | Novel architectures with staying power |
| Part 3 (Architectures) | New FMs or significant analysis of existing |
| Part 4 (Multi-Scale) | Integration across biological scales |
| Part 5 (Evaluation) | Rigorous methodology, benchmarks |
| Part 6 (Translation) | Clinical deployment, real-world validation |

**Integration Complexity:**
- **Drop-in**: Citation without restructuring
- **Section addition**: New subsection in existing chapter
- **Chapter revision**: Rethink chapter organization
- **Major revision**: Rethink part/book structure

**Pedagogical Value:**
- **High**: Illustrates principle clearly, memorable example, good figures
- **Medium**: Solid work but doesn't add pedagogical clarity
- **Low**: Technically correct but wouldn't help students

### Tier 4: Longevity Assessment

**Positive Signals:**
- Genuinely novel architecture/approach
- Solves previously unsolved problem
- Provides new standard benchmark/dataset
- Changes how field thinks about problem
- From lab with track record
- Accumulating citations rapidly

**Negative Signals:**
- Incremental improvement
- Benchmark-chasing without conceptual contribution
- Narrow application unlikely to generalize
- Relies on dataset quirks
- Already superseded
- "Foundation model for X" where X is narrow

**Textbook Test:** Would a thoughtful expert include this in a 2030 textbook?

---

## Contrast Analysis

For papers that pass initial screening, analyze against existing book content:

### Content Overlap Check

1. **Read target chapter(s)** where paper might fit
2. **Identify overlapping concepts** already covered
3. **Determine unique contribution** paper adds beyond existing coverage
4. **Flag redundancy risks** if paper repeats what's already well-covered

### Comparative Assessment

Compare paper against:
- **Existing citations** in target section (is this better/newer?)
- **Alternative papers** on same topic (is this the best choice?)
- **Book's current narrative** (does it fit or disrupt?)

### Insertion Point Analysis

If INCLUDE, determine exact placement:
1. **Chapter**: Which chapter best fits?
2. **Section**: Which section within chapter?
3. **Paragraph context**: After which existing content?
4. **Integration type**: Citation only? New paragraph? New subsection?

---

## Output Formats

### TSV Log Entry

Append to `meta/paper-reviews/logs/ch{NN}-paper-review-log.tsv`:

```
ID	Date	Title	First_Author	Year	Venue	Cite_Key	Status	Repro	Valid	Claims	Pedagogy	Longevity	Book_Location	Notes
```

**Field Values:**
- Status: INCLUDE / EXCLUDE / MONITOR / CITED / SUPERSEDED
- Repro: 0-3
- Valid: 0-3
- Claims: OK / OVER / UNDER
- Pedagogy: H / M / L
- Longevity: + / ? / -
- Book_Location: Ch##-Sec# or N/A

### Prose Report

Save to `meta/paper-reviews/reports/ch{NN}-paper-evaluation-report.prose.md`:

```markdown
### [cite_key]

[Title] — [Authors] — [Venue] ([Year]) — DOI: [doi] — URL: [url]

**Scope fit.** [Assessment]

**Recency relevance.** [Assessment]

**Venue signal.** [Assessment]

**Tier 1 red flags.** [Any found? Details]

**Reproducibility (0–3): [score].** [Justification]

**Validation rigor (0–3): [score].** [Justification]

**Claim calibration.** [Assessment]

**Book relevance (gap filled).** [What gap does this fill?]

**Integration cost.** [Drop-in / Section / Chapter / Major]

**Pedagogical value.** [H/M/L with justification]

**Longevity.** [+ / ? / - with reasoning]

**PDF availability.** [How to access]

**Recommendation.** [INCLUDE / EXCLUDE / MONITOR]. Suggested book location: [Ch## (topic)].

---
```

### Integration Plan (for INCLUDE papers)

```markdown
## Integration Plan: [cite_key]

### Placement
- **Chapter**: [number and title]
- **Section**: [specific section]
- **After**: [existing paragraph/content it follows]
- **Before**: [existing content it precedes]

### Content to Add
- **Citation context**: [1-2 sentence summary for inline citation]
- **Extended mention**: [If warranted, paragraph-level treatment]
- **Figure reference**: [Any figures worth citing?]
- **Cross-references**: [Related sections to link]

### Changes to Existing Content
- **Line [X]**: [Current text] → [Updated text]
- **Remove**: [Any content this supersedes]

### Bibliography Entry
```bibtex
@article{cite_key,
  ...
}
```
```

---

## Decision Matrix

| Repro | Valid | Claims | Pedagogy | Longevity | Decision |
|-------|-------|--------|----------|-----------|----------|
| ≥2 | ≥2 | OK | H | + | **INCLUDE** |
| ≥2 | ≥2 | OK | M | + | **INCLUDE** as citation |
| ≥2 | ≥2 | OK | L | + | **MONITOR** |
| ≥1 | ≥1 | OK | H | ? | **MONITOR** |
| Any | Any | OVER | Any | Any | **EXCLUDE** |
| <2 | <2 | Any | Any | Any | **EXCLUDE** (methods) |

---

## Special Cases

### Preprints
- Higher bar for longevity
- Note preprint status; plan to update when published
- Cautious of preprints >12 months unpublished

### Review Papers
- Use for identifying primary sources, not as primary citations
- Check if from domain experts vs. superficial surveys
- Prefer high-quality venues (Nature Reviews, Annual Reviews)

### Industry Papers (Google, DeepMind, etc.)
- Often high quality but may lack reproducibility
- Evaluate conceptual contribution separately
- Note when methods require unavailable resources

### Books
- Evaluate as potential reference or pedagogical comparison
- Check overlap with our coverage
- Note where their treatment differs/complements ours

### Foundational/Historical Papers
- Lower bar for reproducibility (different era)
- Higher bar for continued relevance
- Value for intellectual lineage

---

## Workflow

### Single Paper Evaluation

1. **Pre-check**: Search bibliography and manuscript for existing citations
   - If CITED → Report status and stop (unless coverage-check requested)
   - If not found → Continue to step 2
2. **Triage**: Quick scope/recency/venue check
3. **Red flag scan**: Check for disqualifiers
4. **Quality scoring**: Reproducibility + Validation
5. **Relevance check**: Gap analysis against book
6. **Longevity assessment**: Textbook test
7. **Contrast analysis**: Compare to existing content
8. **Decision**: INCLUDE / EXCLUDE / MONITOR
9. **If INCLUDE**: Generate integration plan
10. **Log**: Append TSV entry
11. **Report**: Write prose evaluation

### Coverage Check (for already-cited papers)

1. **Locate current citations**: Find all `[@cite_key]` instances
2. **Read context**: Understand how paper is currently discussed
3. **Compare to paper content**: Is coverage proportional to paper's contribution?
4. **Assess gaps**: Are key contributions missing from current coverage?
5. **Recommend**: Adequate / Expand / Consolidate

### Batch Evaluation

1. **Pre-check all**: Filter out already-cited papers
2. Triage remaining papers (quick pass/fail)
3. Full evaluation on papers that pass
4. Generate summary table
5. Identify related papers to evaluate together
6. Priority rank INCLUDE papers
7. Log all entries
8. Write consolidated report

---

## Reference Files

This agent has access to:
- `evaluation-framework.md` - Complete evaluation criteria
- `chapter-map.md` - Book structure for placement decisions
- `bib/references.bib` - Bibliography (search for existing citations)
- `part_*/p*.qmd` - Manuscript chapters (search for paper mentions)
- `meta/paper-reviews/logs/` - Existing review logs
- `meta/paper-reviews/reports/` - Existing evaluation reports
