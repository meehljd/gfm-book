# Citation Mapping Suggestions

Quick reference for mapping missing citation keys to existing bib entries or identifying truly missing papers.

## Potential Duplicates / Same Paper Different Key

| Missing Key | Might Be Same As | Notes |
|-------------|------------------|-------|
| `verkuil_language_2022` | `lin_esm-2_2022` | ESMFold paper - Verkuil is co-author |
| `chen_sequence-based_2022` | `chen_deepsea_2022` | Sei paper - already fixed |

## By Chapter - Quick Actions

### p1-ch02-data.qmd
- `uniprot_2023` → **ADD** (UniProt Consortium 2023)
- `xu_improving_2025` → **ADD** (PGS improvement paper)

### p1-ch03-gwas.qmd
- `weissbrod_functionally_2020` → **ADD** (functionally-informed fine-mapping)
- `xu_improving_2025` → same as above

### p3-ch08-pretraining.qmd
- `gu_pubmedbert_2021` → **ADD** (Domain-specific pretraining)
- `lee_biobert_2020` → **ADD** (BioBERT)
- `nijkamp_progen2_2023` → **ADD** (ProGen2)

### p3-ch11-benchmarks.qmd
- `esposito_mavedb_2019` → **ADD** (MaveDB)
- `hoskins_cagi6_2023` → **ADD** (CAGI6)
- `kryshtafovych_critical_2021` → **ADD** (CASP14)

### p3-ch12-evaluation.qmd
- `delong_comparing_1988` → **ADD** (ROC comparison)
- `li_cd-hit_2006` → **ADD** (CD-HIT)
- `platt_probabilistic_1999` → **ADD** (Platt scaling)
- `rost_twilight_1999` → **ADD** (twilight zone)
- `steinegger_mmseqs2_2017` → **ADD** (MMseqs2)

### p4-ch16-protein-lm.qmd
- `sanderson_deepectransformer_2023` → **VERIFY** (may be different paper)
- `verkuil_language_2022` → **CHECK** if `lin_esm-2_2022` covers this

### p5-ch22-networks.qmd (25 missing)
Most are GNN foundational papers - all need adding:
- Graph foundations: hamilton, velickovic, xu_powerful, ying, dwivedi, morris, oono, li_deeper
- Bio KGs: szklarczyk (STRING), oughtred (BioGRID), orchard (IntAct), pinero (DisGeNET), himmelstein, chandak (PrimeKG)
- COVID examples: richardson, stebbing
- Recent/unclear: biomedkg, cgcom, decarlo, dreamgnn, lin_gobeacon, saadat, segceco

### p6-ch26-causal.qmd
- `candes_panning_2018` → **ADD** (Model-X knockoffs)
- `hartwig_robust_2017` → **ADD** (MR zero modal)

### p6-ch27-regulatory.qmd
- `common_rule_2018` → **ADD** (45 CFR 46)

### p7-ch28-clinical-risk.qmd
- `xu_improving_2025` → same as p1-ch02

### app-d-models.qmd
- `cao_multi-omics_2022` → **ADD** (GLUE)
- `pollard_detection_2010` → **ADD** (PhyloP/GERP related)
- `sundaram_primateai_2018` → **ADD** (PrimateAI)
- `yang_scbert_2022` → **ADD** (scBERT)
- `zeng_predicting_2022` → **ADD** (Pangolin)
- `nijkamp_progen2_2023` → same as p3-ch08

## Summary

| Action | Count |
|--------|-------|
| Definitely ADD | ~40 |
| Check for duplicates | 2 |
| Unclear/verify | ~7 |
