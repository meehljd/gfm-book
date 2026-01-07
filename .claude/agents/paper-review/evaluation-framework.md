# Paper Evaluation Framework Reference

Quick reference for paper evaluation criteria.

## Quick Triage Gates

1. **Scope**: Deep learning + genomic sequences/variants/regulation?
2. **Recency**: Foundational (pre-2020 still cited) OR recent (2022+)?
3. **Venue**: Reputable journal/conference OR credible preprint?

NO to any → Stop unless strong reason to continue.

## Red Flags (Immediate EXCLUDE)

### Methodological
- No held-out test set / test leakage
- Single dataset, no external validation
- Cherry-picked metrics
- Missing/weak baselines
- Hyperparameter tuning on test set
- No code/data for SOTA claims

### Reporting
- No confidence intervals
- "Outperforms all" without nuance
- Vague dataset descriptions
- Metric inflation (tiny gains as breakthroughs)
- No ablations for complex architectures

### Scientific
- Biological implausibility
- Confounding not addressed
- Circular validation
- Distribution shift ignored

## Scoring Scales

### Reproducibility (0-3)
| Score | Meaning |
|-------|---------|
| 0 | No code, no methods |
| 1 | Methods only |
| 2 | Code + models |
| 3 | Code + data + models + docs |

### Validation (0-3)
| Score | Meaning |
|-------|---------|
| 0 | Single dataset |
| 1 | Multiple same-source |
| 2 | External validation |
| 3 | Multiple external / prospective |

### Claims
| Rating | Meaning |
|--------|---------|
| OK | Proportional to evidence |
| OVER | Hype > results |
| UNDER | Modest claims, strong results |

### Pedagogy
| Rating | Meaning |
|--------|---------|
| H | Clear principle, memorable, good figures |
| M | Solid but no pedagogical clarity |
| L | Correct but wouldn't help students |

### Longevity
| Rating | Meaning |
|--------|---------|
| + | Passes textbook test |
| ? | Uncertain, monitor |
| - | Likely superseded |

## Book Gap Types by Part

| Part | Worth Including |
|------|-----------------|
| 1 Foundations | Better genomics for ML readers |
| 2 Principles | Novel lasting architectures |
| 3 Architectures | New FMs, significant analysis |
| 4 Multi-Scale | Cross-scale integration |
| 5 Evaluation | Rigorous methodology |
| 6 Translation | Clinical deployment |

## Integration Complexity

| Type | Meaning | When to Use |
|------|---------|-------------|
| Drop-in | Citation only | Most papers |
| Section | New subsection | Significant methods |
| Chapter | Reorganize chapter | Major advances |
| Major | Reorganize part/book | Paradigm shifts |

## Decision Matrix

| Repro | Valid | Claims | Pedagogy | Longevity | → Decision |
|-------|-------|--------|----------|-----------|------------|
| ≥2 | ≥2 | OK | H | + | INCLUDE |
| ≥2 | ≥2 | OK | M | + | INCLUDE (citation) |
| ≥2 | ≥2 | OK | L | + | MONITOR |
| ≥1 | ≥1 | OK | H | ? | MONITOR |
| Any | Any | OVER | Any | Any | EXCLUDE |
| <2 | <2 | Any | Any | Any | EXCLUDE |

## Status Definitions

| Status | Meaning | Action |
|--------|---------|--------|
| INCLUDE | Approved | Add to chapter |
| EXCLUDE | Doesn't meet criteria | Log rationale |
| MONITOR | Promising but uncertain | Re-evaluate later |
| CITED | Already in manuscript | Track for updates |
| SUPERSEDED | Replaced by newer | Note replacement |

## Longevity Signals

### Positive
- Genuinely novel approach
- Solves unsolved problem
- New standard benchmark
- Changes field thinking
- Track record lab
- Rapid citations

### Negative
- Incremental only
- Benchmark-chasing
- Narrow application
- Dataset-specific
- Already superseded
- "FM for X" (narrow X)

## Textbook Test

> Would a thoughtful expert include this in a textbook written in 2030?

When uncertain → Default to EXCLUDE.
