# Missing Citations Report

**Generated:** 2026-01-22
**Source:** Editorial board reviews from 2026-01-21

This report lists quantitative claims and statements that require citations but currently lack them.

---

## Critical (Claims with specific numbers or facts)

### Chapter 27: Regulatory and Governance

| Line | Claim | Action Required |
|------|-------|-----------------|
| 217 | Reference to `@manson_rethinking_2007` | Citation key not found in `references.bib`. Either add the paper or replace with alternative source. |

### Chapter 28: Clinical Risk Prediction

| Line | Claim | Action Required |
|------|-------|-----------------|
| 58 | "roughly threefold higher lifetime risk than one in the bottom percentile" | Add citation (likely Khera et al. CAD PRS validation study or similar) |
| 208 | "ischemic stroke improved by 66%, heart failure by 32%, and peripheral artery disease by 25%" | Add `[@ruan_improving_2022]` |
| 233 | "adjusted p < 10^-20" | Add `[@ruan_improving_2022]` |

**Note:** Lines 58, 208, 233 have trailing ` .` (space before period), indicating missing citation brackets.

### Chapter 31: Sequence Design

| Line | Claim | Action Required |
|------|-------|-----------------|
| 139 (Table) | "30-50% express" and "30-70% express; 5-30% functional" success rates | Add citation (possibly @huang_coming_2016 or other de novo design review) |
| 241 | "Traditional codon optimization relied on codon adaptation indices..." | Add citation for CAI methodology history |
| 259 | "Chemical modifications of mRNA (pseudouridine, N1-methylpseudouridine)..." | Add citation (Kariko et al. foundational work on modified nucleosides) |
| 300 | "Structure-guided stabilization of the prefusion spike conformation" | Add citation for SARS-CoV-2 vaccine prefusion stabilization work |

---

## Medium Priority (Historical or methodological claims)

### Chapter 21: 3D Genome

| Line | Claim | Action Required |
|------|-------|-----------------|
| ~333 | Spatial transcriptomics models | Verify citations for spatial transcriptomics methods |
| ~335 | Additional spatial models | Check if spatial model citations are complete |
| ~349 | Spatial integration methods | Review for missing citations |

---

## Low Priority (General statements that could benefit from citations)

These are statements that make general claims but don't have specific numbers. Adding citations would strengthen the text but is not critical.

- Check claims about "first" or "original" methods throughout the book
- Historical timeline claims (e.g., "since 2018", "beginning in 2020")
- Performance comparison statements without specific numbers

---

## Papers to Add to references.bib

Based on the missing citations above, the following papers likely need to be added:

1. **Manson 2007** - For Ch27 line 217 (or identify correct paper)
2. **Khera et al.** - CAD PRS validation study for Ch28 threefold risk claim
3. **Kariko et al.** - mRNA modification foundational work for Ch31
4. **Prefusion spike paper** - SARS-CoV-2 vaccine design for Ch31

---

## Verification Notes

All other citations in these chapters were verified present in `references.bib`:
- Ch27: 26/27 citations verified
- Ch28: 23/23 citations verified (but 3 claims missing citation brackets)
- Ch31: 7/7 citations verified (but several uncited claims)

---

## Action Items

1. [ ] Add `@manson_rethinking_2007` to bib or replace reference in Ch27
2. [ ] Find and add Khera CAD PRS paper for Ch28 line 58
3. [ ] Add `[@ruan_improving_2022]` at Ch28 lines 208, 233
4. [ ] Add citations to Ch31 table success rates
5. [ ] Add Kariko mRNA modification citation to Ch31
6. [ ] Add prefusion spike citation to Ch31
