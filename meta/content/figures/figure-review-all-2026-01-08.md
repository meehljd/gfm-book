# Figure Quality Review - All Parts
**Date:** 2026-01-08

## Executive Summary

Reviewed 437 SVG figures across all 31 chapters. Found:
- **8 SEVERE issues**: Bar charts with invisible bars (data scaling errors)
- **Many MINOR issues**: Standard matplotlib off-canvas label positioning (not affecting readability)

## Critical Issues to Fix

### SEVERE: Invisible Bar Charts (Data Scaling Errors)

These matplotlib bar charts have Y-coordinates rendered far outside the viewBox, making bars completely invisible:

| Chapter | Figure | Issue |
|---------|--------|-------|
| Ch 14 | `02-B-fig-long-context-revolution.svg` | Y-coords at ~135,000 vs viewBox ~350 |
| Ch 14 | `04-B-fig-evo2-training.svg` | Y-coords at ~102,000 |
| Ch 15 | `02-B-fig-esm2-scaling.svg` | Y-coords at ~126,000 |
| Ch 16 | `01-B-fig-long-range-regulation.svg` | Y-coords at ~51,000 |
| Ch 18 | `03-A-fig-rna-plm-gap.svg` | Y-coords at ~121,000 |
| Ch 18 | `04-B-fig-codon-tokenization.svg` | Y-coords at ~85,000 |
| Ch 20 | `02-B-fig-chromatin-hierarchy.svg` | Y-coords at ~-52,000 |
| Ch 21 | `01-B-fig-biological-networks.svg` | Y-coords at ~83,000 |

**Root Cause:** Matplotlib bar chart Y-axis data was not properly scaled to plot coordinates.

**Fix Required:** Regenerate these figures with correct axis scaling.

## Part-by-Part Summary

### Part 1 (Ch 1-4): 31 figures
- **Status:** GOOD
- No critical issues
- Graphviz flowcharts properly formatted
- Matplotlib plots have correct scaling

### Part 2 (Ch 5-12): 91 figures
- **Status:** GOOD
- No critical issues
- Text placement correct on all figures

### Part 3 (Ch 13-17): 84 figures
- **Status:** 5 SEVERE issues found
- Ch 14: 2 broken bar charts
- Ch 15: 1 broken bar chart
- Ch 16: 1 broken bar chart
- Ch 17: OK

### Part 4 (Ch 18-22): 146 figures
- **Status:** 3 SEVERE issues found
- Ch 18: 2 broken bar charts
- Ch 20: 1 broken bar chart
- Ch 21: 1 broken bar chart

### Part 5 (Ch 23-26): 42 figures
- **Status:** GOOD
- No critical issues
- Minor text scaling variations acceptable

### Part 6 (Ch 27-31): 43 figures
- **Status:** GOOD
- No critical issues
- Graphviz diagrams well-formatted

## Recommended Actions

1. **Priority 1:** Fix the 8 SEVERE figures with invisible bars ✅ DONE
2. **Priority 2:** Review the regenerated figures visually
3. **Priority 3:** Minor label positioning issues can be addressed in future passes if needed

---

## Fixes Applied (2026-01-08)

All 8 SEVERE issues were fixed by adding explicit `ylim` or `xlim` constraints to log-scale bar charts:

| Chapter | Figure | Fix Applied |
|---------|--------|-------------|
| Ch 14 | `02-B-fig-long-context-revolution.svg` | Added `ax.set_ylim(1, 2000)` |
| Ch 14 | `04-B-fig-evo2-training.svg` | Added `ax.set_ylim(1, 3000)` |
| Ch 15 | `02-B-fig-esm2-scaling.svg` | Added `ax.set_ylim(10, 5000)` |
| Ch 16 | `01-B-fig-long-range-regulation.svg` | Added `ax.set_ylim(0.05, 3000)` |
| Ch 18 | `03-A-fig-rna-plm-gap.svg` | Added `ax.set_ylim(1, 500)` |
| Ch 18 | `04-B-fig-codon-tokenization.svg` | Added `ax.set_ylim(1, 3000)` |
| Ch 20 | `02-B-fig-chromatin-hierarchy.svg` | Added `ax.set_xlim(0.1, 200000)` |
| Ch 21 | `01-B-fig-biological-networks.svg` | Added `ax.set_ylim(0.1, 200)` |

All scripts regenerated successfully.

## Orphaned Files Check (2026-01-08)

Checked for orphaned files in `figs/` directory:
- **.dot files**: None found (all Graphviz source files cleaned up)
- **.png files**: None found (all figures are SVG)
- **Placeholder files**: None found
- **Total SVG files**: 437 properly generated figures

**Result:** No orphaned files to remove.
