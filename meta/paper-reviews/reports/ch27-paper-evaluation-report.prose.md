# Chapter 27: Drug Discovery — Paper Evaluation Report (Prose)

Date: 2025-12-22


---

## avsec_alphagenome_2025

**Title:** AlphaGenome: AI for better understanding the genome


**First author / year / venue:** Avsec / 2025 / Google DeepMind


**Where it appears in the chapter:** Chapter 27: Drug Discovery — From Variant-Level Predictions to Gene-Level Evidence


**Publication status:** bioRxiv preprint; public docs and tooling available.


### 30-Second Triage (Gates)

- **Scope fit (DL + genomics sequences/variants/regulation, or (for this part) biomolecular design):** YES. 
This appears within the book’s scope for this chapter.

- **Recency relevance:** modern (based on year 2025).

- **Venue signal:** YES. 
Preprint status increases the durability bar.


### Tier 1: Red Flags (Immediate Disqualification)

I did not run a full PDF-level audit for leakage/overlap, and most chapters’ Quarto text does not include the methodological details needed to verify held-out evaluation rigor. 
So: **no hard red flags were confirmed from the chapter text alone**; any high-stakes claims should still be verified in the paper PDF (train/test splits, external validation, baselines, ablations, and confounder controls).


### Tier 2: Quality Scoring

- **Reproducibility (0–3):** 1. 
No clear code/weights link was confirmed in the quick check; treat as harder to reproduce.

- **Validation rigor (0–3):** 2. 
The work is commonly evaluated across multiple datasets/benchmarks or on strong external tasks; still confirm true independence of test sets.

- **Claim calibration:** OVER. 
Some headline claims appear broader than what a conservative textbook would assert without replication.


### Tier 3: Book Relevance

- **Gap filled / role in chapter:** This citation supports the section “From Variant-Level Predictions to Gene-Level Evidence” (per chapter structure) and can serve as an example or canonical reference for the concept discussed there.

- **Integration cost:** 
Low-to-medium: likely a drop-in citation plus (optionally) a short boxed example/figure callout, depending on how central the paper is to the section.

- **Pedagogical value:** L. 
Useful as a pointer, but limited as a teaching vehicle.


### Tier 4: Longevity (“Textbook Test”)

- **Longevity:** ?. 
May be superseded; keep if it uniquely illustrates a principle or is heavily adopted.


### Recommendation

- **Status:** MONITOR

- **Re-eval trigger:** check for peer-reviewed publication, stronger external validation, and stable code/weights.


---

## avsec_enformer_2021

**Title:** [Enformer] Effective gene expression prediction from sequence by integrating long-range interactions


**First author / year / venue:** Avsec / 2021 / Nature Methods


**Where it appears in the chapter:** Chapter 27: Drug Discovery — From Variant-Level Predictions to Gene-Level Evidence


**Publication status:** not checked beyond metadata (assume published if venue is a journal/conference; otherwise treat as preprint).


### 30-Second Triage (Gates)

- **Scope fit (DL + genomics sequences/variants/regulation, or (for this part) biomolecular design):** NO. 
This looks like a general ML/clinical-methods citation rather than genomics-specific; treat as background-only.

- **Recency relevance:** mid (based on year 2021).

- **Venue signal:** YES. 
Preprint status increases the durability bar.


### Tier 1: Red Flags (Immediate Disqualification)

I did not run a full PDF-level audit for leakage/overlap, and most chapters’ Quarto text does not include the methodological details needed to verify held-out evaluation rigor. 
So: **no hard red flags were confirmed from the chapter text alone**; any high-stakes claims should still be verified in the paper PDF (train/test splits, external validation, baselines, ablations, and confounder controls).


### Tier 2: Quality Scoring

- **Reproducibility (0–3):** 2. 
There is public code and/or packaging for reproduction (per web check for major items), but confirm exact data/weights access in the PDF or repo.

- **Validation rigor (0–3):** 2. 
The work is commonly evaluated across multiple datasets/benchmarks or on strong external tasks; still confirm true independence of test sets.

- **Claim calibration:** OK. 
Claims appear broadly commensurate with typical evidence for the venue/category.


### Tier 3: Book Relevance

- **Gap filled / role in chapter:** This citation supports the section “From Variant-Level Predictions to Gene-Level Evidence” (per chapter structure) and can serve as an example or canonical reference for the concept discussed there.

- **Integration cost:** 
Low-to-medium: likely a drop-in citation plus (optionally) a short boxed example/figure callout, depending on how central the paper is to the section.

- **Pedagogical value:** H. 
Strong candidate for a worked example or figure-based explanation.


### Tier 4: Longevity (“Textbook Test”)

- **Longevity:** +. 
Likely to remain a standard reference for the concept or method family.


### Recommendation

- **Status:** INCLUDE

- **Integration note:** consider adding a short “why it matters” paragraph + pointer to code/resources.


---

## benegas_gpn-msa_2024

**Title:** GPN-MSA: an alignment-based DNA language model for genome-wide variant effect prediction


**First author / year / venue:** Benegas / 2024 / bioRxiv


**Where it appears in the chapter:** Chapter 27: Drug Discovery — From Variant-Level Predictions to Gene-Level Evidence


**Publication status:** Nat Biotechnol (2025) (update from web check).


### 30-Second Triage (Gates)

- **Scope fit (DL + genomics sequences/variants/regulation, or (for this part) biomolecular design):** YES. 
This appears within the book’s scope for this chapter.

- **Recency relevance:** modern (based on year 2024).

- **Venue signal:** YES. 
Published venue suggests baseline credibility.


### Tier 1: Red Flags (Immediate Disqualification)

I did not run a full PDF-level audit for leakage/overlap, and most chapters’ Quarto text does not include the methodological details needed to verify held-out evaluation rigor. 
So: **no hard red flags were confirmed from the chapter text alone**; any high-stakes claims should still be verified in the paper PDF (train/test splits, external validation, baselines, ablations, and confounder controls).


### Tier 2: Quality Scoring

- **Reproducibility (0–3):** 2. 
There is public code and/or packaging for reproduction (per web check for major items), but confirm exact data/weights access in the PDF or repo.

- **Validation rigor (0–3):** 2. 
The work is commonly evaluated across multiple datasets/benchmarks or on strong external tasks; still confirm true independence of test sets.

- **Claim calibration:** OK. 
Claims appear broadly commensurate with typical evidence for the venue/category.


### Tier 3: Book Relevance

- **Gap filled / role in chapter:** This citation supports the section “From Variant-Level Predictions to Gene-Level Evidence” (per chapter structure) and can serve as an example or canonical reference for the concept discussed there.

- **Integration cost:** 
Low-to-medium: likely a drop-in citation plus (optionally) a short boxed example/figure callout, depending on how central the paper is to the section.

- **Pedagogical value:** M. 
Good supporting example; probably not worth a long deep-dive unless it’s central.


### Tier 4: Longevity (“Textbook Test”)

- **Longevity:** ?. 
May be superseded; keep if it uniquely illustrates a principle or is heavily adopted.


### Recommendation

- **Status:** INCLUDE

- **Integration note:** consider adding a short “why it matters” paragraph + pointer to code/resources.


---

## brandes_genome-wide_2023

**Title:** Genome-wide prediction of disease variant effects with a deep protein language model


**First author / year / venue:** Brandes / 2023 / Nature Genetics


**Where it appears in the chapter:** Chapter 27: Drug Discovery — From Variant-Level Predictions to Gene-Level Evidence


**Publication status:** not checked beyond metadata (assume published if venue is a journal/conference; otherwise treat as preprint).


### 30-Second Triage (Gates)

- **Scope fit (DL + genomics sequences/variants/regulation, or (for this part) biomolecular design):** YES. 
This appears within the book’s scope for this chapter.

- **Recency relevance:** modern (based on year 2023).

- **Venue signal:** YES. 
Preprint status increases the durability bar.


### Tier 1: Red Flags (Immediate Disqualification)

I did not run a full PDF-level audit for leakage/overlap, and most chapters’ Quarto text does not include the methodological details needed to verify held-out evaluation rigor. 
So: **no hard red flags were confirmed from the chapter text alone**; any high-stakes claims should still be verified in the paper PDF (train/test splits, external validation, baselines, ablations, and confounder controls).


### Tier 2: Quality Scoring

- **Reproducibility (0–3):** 1. 
No clear code/weights link was confirmed in the quick check; treat as harder to reproduce.

- **Validation rigor (0–3):** 2. 
The work is commonly evaluated across multiple datasets/benchmarks or on strong external tasks; still confirm true independence of test sets.

- **Claim calibration:** OK. 
Claims appear broadly commensurate with typical evidence for the venue/category.


### Tier 3: Book Relevance

- **Gap filled / role in chapter:** This citation supports the section “From Variant-Level Predictions to Gene-Level Evidence” (per chapter structure) and can serve as an example or canonical reference for the concept discussed there.

- **Integration cost:** 
Low-to-medium: likely a drop-in citation plus (optionally) a short boxed example/figure callout, depending on how central the paper is to the section.

- **Pedagogical value:** H. 
Strong candidate for a worked example or figure-based explanation.


### Tier 4: Longevity (“Textbook Test”)

- **Longevity:** +. 
Likely to remain a standard reference for the concept or method family.


### Recommendation

- **Status:** INCLUDE

- **Integration note:** consider adding a short “why it matters” paragraph + pointer to code/resources.


---

## cheng_alphamissense_2023

**Title:** [AlphaMissense] Accurate proteome-wide missense variant effect prediction with AlphaMissense


**First author / year / venue:** Cheng / 2023 / Science


**Where it appears in the chapter:** Chapter 27: Drug Discovery — From Variant-Level Predictions to Gene-Level Evidence


**Publication status:** not checked beyond metadata (assume published if venue is a journal/conference; otherwise treat as preprint).


### 30-Second Triage (Gates)

- **Scope fit (DL + genomics sequences/variants/regulation, or (for this part) biomolecular design):** YES. 
This appears within the book’s scope for this chapter.

- **Recency relevance:** modern (based on year 2023).

- **Venue signal:** YES. 
Preprint status increases the durability bar.


### Tier 1: Red Flags (Immediate Disqualification)

I did not run a full PDF-level audit for leakage/overlap, and most chapters’ Quarto text does not include the methodological details needed to verify held-out evaluation rigor. 
So: **no hard red flags were confirmed from the chapter text alone**; any high-stakes claims should still be verified in the paper PDF (train/test splits, external validation, baselines, ablations, and confounder controls).


### Tier 2: Quality Scoring

- **Reproducibility (0–3):** 2. 
There is public code and/or packaging for reproduction (per web check for major items), but confirm exact data/weights access in the PDF or repo.

- **Validation rigor (0–3):** 2. 
The work is commonly evaluated across multiple datasets/benchmarks or on strong external tasks; still confirm true independence of test sets.

- **Claim calibration:** OK. 
Claims appear broadly commensurate with typical evidence for the venue/category.


### Tier 3: Book Relevance

- **Gap filled / role in chapter:** This citation supports the section “From Variant-Level Predictions to Gene-Level Evidence” (per chapter structure) and can serve as an example or canonical reference for the concept discussed there.

- **Integration cost:** 
Low-to-medium: likely a drop-in citation plus (optionally) a short boxed example/figure callout, depending on how central the paper is to the section.

- **Pedagogical value:** H. 
Strong candidate for a worked example or figure-based explanation.


### Tier 4: Longevity (“Textbook Test”)

- **Longevity:** +. 
Likely to remain a standard reference for the concept or method family.


### Recommendation

- **Status:** INCLUDE

- **Integration note:** consider adding a short “why it matters” paragraph + pointer to code/resources.


---

## dalla-torre_nucleotide_2023

**Title:** Nucleotide Transformer: building and evaluating robust foundation models for human genomics


**First author / year / venue:** Dalla-Torre / 2023 / Nature Methods


**Where it appears in the chapter:** Chapter 27: Drug Discovery — From Variant-Level Predictions to Gene-Level Evidence


**Publication status:** not checked beyond metadata (assume published if venue is a journal/conference; otherwise treat as preprint).


### 30-Second Triage (Gates)

- **Scope fit (DL + genomics sequences/variants/regulation, or (for this part) biomolecular design):** YES. 
This appears within the book’s scope for this chapter.

- **Recency relevance:** modern (based on year 2023).

- **Venue signal:** YES. 
Preprint status increases the durability bar.


### Tier 1: Red Flags (Immediate Disqualification)

I did not run a full PDF-level audit for leakage/overlap, and most chapters’ Quarto text does not include the methodological details needed to verify held-out evaluation rigor. 
So: **no hard red flags were confirmed from the chapter text alone**; any high-stakes claims should still be verified in the paper PDF (train/test splits, external validation, baselines, ablations, and confounder controls).


### Tier 2: Quality Scoring

- **Reproducibility (0–3):** 3. 
There is public code and/or packaging for reproduction (per web check for major items), but confirm exact data/weights access in the PDF or repo.

- **Validation rigor (0–3):** 1. 
Evidence suggests standard held-out evaluation and/or multiple benchmarks, but truly independent external validation is unclear.

- **Claim calibration:** OK. 
Claims appear broadly commensurate with typical evidence for the venue/category.


### Tier 3: Book Relevance

- **Gap filled / role in chapter:** This citation supports the section “From Variant-Level Predictions to Gene-Level Evidence” (per chapter structure) and can serve as an example or canonical reference for the concept discussed there.

- **Integration cost:** 
Low-to-medium: likely a drop-in citation plus (optionally) a short boxed example/figure callout, depending on how central the paper is to the section.

- **Pedagogical value:** H. 
Strong candidate for a worked example or figure-based explanation.


### Tier 4: Longevity (“Textbook Test”)

- **Longevity:** +. 
Likely to remain a standard reference for the concept or method family.


### Recommendation

- **Status:** INCLUDE

- **Integration note:** consider adding a short “why it matters” paragraph + pointer to code/resources.


---

## fishman_gena-lm_2025

**Title:** GENA-LM: a family of open-source foundational DNA language models for long sequences


**First author / year / venue:** Fishman / 2025 / Nucleic Acids Research


**Where it appears in the chapter:** Chapter 27: Drug Discovery — Building Model Infrastructure


**Publication status:** not checked beyond metadata (assume published if venue is a journal/conference; otherwise treat as preprint).


### 30-Second Triage (Gates)

- **Scope fit (DL + genomics sequences/variants/regulation, or (for this part) biomolecular design):** YES. 
This appears within the book’s scope for this chapter.

- **Recency relevance:** modern (based on year 2025).

- **Venue signal:** YES. 
Preprint status increases the durability bar.


### Tier 1: Red Flags (Immediate Disqualification)

I did not run a full PDF-level audit for leakage/overlap, and most chapters’ Quarto text does not include the methodological details needed to verify held-out evaluation rigor. 
So: **no hard red flags were confirmed from the chapter text alone**; any high-stakes claims should still be verified in the paper PDF (train/test splits, external validation, baselines, ablations, and confounder controls).


### Tier 2: Quality Scoring

- **Reproducibility (0–3):** 1. 
No clear code/weights link was confirmed in the quick check; treat as harder to reproduce.

- **Validation rigor (0–3):** 1. 
Evidence suggests standard held-out evaluation and/or multiple benchmarks, but truly independent external validation is unclear.

- **Claim calibration:** OK. 
Claims appear broadly commensurate with typical evidence for the venue/category.


### Tier 3: Book Relevance

- **Gap filled / role in chapter:** This citation supports the section “Building Model Infrastructure” (per chapter structure) and can serve as an example or canonical reference for the concept discussed there.

- **Integration cost:** 
Low-to-medium: likely a drop-in citation plus (optionally) a short boxed example/figure callout, depending on how central the paper is to the section.

- **Pedagogical value:** L. 
Useful as a pointer, but limited as a teaching vehicle.


### Tier 4: Longevity (“Textbook Test”)

- **Longevity:** ?. 
May be superseded; keep if it uniquely illustrates a principle or is heavily adopted.


### Recommendation

- **Status:** CITED

- **Integration note:** keep as supporting citation; avoid leaning on it for the chapter’s main empirical claims.


---

## lin_evolutionary-scale_2023

**Title:** Evolutionary-scale prediction of atomic-level protein structure with a language model


**First author / year / venue:** Lin / 2023 / Science


**Where it appears in the chapter:** Chapter 27: Drug Discovery — Representing Targets for Binding Prediction


**Publication status:** not checked beyond metadata (assume published if venue is a journal/conference; otherwise treat as preprint).


### 30-Second Triage (Gates)

- **Scope fit (DL + genomics sequences/variants/regulation, or (for this part) biomolecular design):** YES. 
This appears within the book’s scope for this chapter.

- **Recency relevance:** modern (based on year 2023).

- **Venue signal:** YES. 
Preprint status increases the durability bar.


### Tier 1: Red Flags (Immediate Disqualification)

I did not run a full PDF-level audit for leakage/overlap, and most chapters’ Quarto text does not include the methodological details needed to verify held-out evaluation rigor. 
So: **no hard red flags were confirmed from the chapter text alone**; any high-stakes claims should still be verified in the paper PDF (train/test splits, external validation, baselines, ablations, and confounder controls).


### Tier 2: Quality Scoring

- **Reproducibility (0–3):** 1. 
No clear code/weights link was confirmed in the quick check; treat as harder to reproduce.

- **Validation rigor (0–3):** 1. 
Evidence suggests standard held-out evaluation and/or multiple benchmarks, but truly independent external validation is unclear.

- **Claim calibration:** OK. 
Claims appear broadly commensurate with typical evidence for the venue/category.


### Tier 3: Book Relevance

- **Gap filled / role in chapter:** This citation supports the section “Representing Targets for Binding Prediction” (per chapter structure) and can serve as an example or canonical reference for the concept discussed there.

- **Integration cost:** 
Low-to-medium: likely a drop-in citation plus (optionally) a short boxed example/figure callout, depending on how central the paper is to the section.

- **Pedagogical value:** L. 
Useful as a pointer, but limited as a teaching vehicle.


### Tier 4: Longevity (“Textbook Test”)

- **Longevity:** ?. 
May be superseded; keep if it uniquely illustrates a principle or is heavily adopted.


### Recommendation

- **Status:** CITED

- **Integration note:** keep as supporting citation; avoid leaning on it for the chapter’s main empirical claims.


---

## linder_borzoi_2025

**Title:** [Borzoi] Predicting RNA-seq coverage from DNA sequence as a unifying model of gene regulation


**First author / year / venue:** Linder / 2025 / Nature Genetics


**Where it appears in the chapter:** Chapter 27: Drug Discovery — From Variant-Level Predictions to Gene-Level Evidence


**Publication status:** not checked beyond metadata (assume published if venue is a journal/conference; otherwise treat as preprint).


### 30-Second Triage (Gates)

- **Scope fit (DL + genomics sequences/variants/regulation, or (for this part) biomolecular design):** YES. 
This appears within the book’s scope for this chapter.

- **Recency relevance:** modern (based on year 2025).

- **Venue signal:** YES. 
Preprint status increases the durability bar.


### Tier 1: Red Flags (Immediate Disqualification)

I did not run a full PDF-level audit for leakage/overlap, and most chapters’ Quarto text does not include the methodological details needed to verify held-out evaluation rigor. 
So: **no hard red flags were confirmed from the chapter text alone**; any high-stakes claims should still be verified in the paper PDF (train/test splits, external validation, baselines, ablations, and confounder controls).


### Tier 2: Quality Scoring

- **Reproducibility (0–3):** 3. 
There is public code and/or packaging for reproduction (per web check for major items), but confirm exact data/weights access in the PDF or repo.

- **Validation rigor (0–3):** 2. 
The work is commonly evaluated across multiple datasets/benchmarks or on strong external tasks; still confirm true independence of test sets.

- **Claim calibration:** OK. 
Claims appear broadly commensurate with typical evidence for the venue/category.


### Tier 3: Book Relevance

- **Gap filled / role in chapter:** This citation supports the section “From Variant-Level Predictions to Gene-Level Evidence” (per chapter structure) and can serve as an example or canonical reference for the concept discussed there.

- **Integration cost:** 
Low-to-medium: likely a drop-in citation plus (optionally) a short boxed example/figure callout, depending on how central the paper is to the section.

- **Pedagogical value:** H. 
Strong candidate for a worked example or figure-based explanation.


### Tier 4: Longevity (“Textbook Test”)

- **Longevity:** +. 
Likely to remain a standard reference for the concept or method family.


### Recommendation

- **Status:** INCLUDE

- **Integration note:** consider adding a short “why it matters” paragraph + pointer to code/resources.


---

## nguyen_hyenadna_2023

**Title:** HyenaDNA: Long-Range Genomic Sequence Modeling at Single Nucleotide Resolution


**First author / year / venue:** Nguyen / 2023 / —


**Where it appears in the chapter:** Chapter 27: Drug Discovery — From Variant-Level Predictions to Gene-Level Evidence


**Publication status:** NeurIPS (2023) (update from web check).


### 30-Second Triage (Gates)

- **Scope fit (DL + genomics sequences/variants/regulation, or (for this part) biomolecular design):** YES. 
This appears within the book’s scope for this chapter.

- **Recency relevance:** modern (based on year 2023).

- **Venue signal:** YES. 
Published venue suggests baseline credibility.


### Tier 1: Red Flags (Immediate Disqualification)

I did not run a full PDF-level audit for leakage/overlap, and most chapters’ Quarto text does not include the methodological details needed to verify held-out evaluation rigor. 
So: **no hard red flags were confirmed from the chapter text alone**; any high-stakes claims should still be verified in the paper PDF (train/test splits, external validation, baselines, ablations, and confounder controls).


### Tier 2: Quality Scoring

- **Reproducibility (0–3):** 3. 
There is public code and/or packaging for reproduction (per web check for major items), but confirm exact data/weights access in the PDF or repo.

- **Validation rigor (0–3):** 1. 
Evidence suggests standard held-out evaluation and/or multiple benchmarks, but truly independent external validation is unclear.

- **Claim calibration:** OK. 
Claims appear broadly commensurate with typical evidence for the venue/category.


### Tier 3: Book Relevance

- **Gap filled / role in chapter:** This citation supports the section “From Variant-Level Predictions to Gene-Level Evidence” (per chapter structure) and can serve as an example or canonical reference for the concept discussed there.

- **Integration cost:** 
Low-to-medium: likely a drop-in citation plus (optionally) a short boxed example/figure callout, depending on how central the paper is to the section.

- **Pedagogical value:** M. 
Good supporting example; probably not worth a long deep-dive unless it’s central.


### Tier 4: Longevity (“Textbook Test”)

- **Longevity:** ?. 
May be superseded; keep if it uniquely illustrates a principle or is heavily adopted.


### Recommendation

- **Status:** CITED

- **Integration note:** keep as supporting citation; avoid leaning on it for the chapter’s main empirical claims.


---

## rakowski_mifm_2025

**Title:** [MIFM] Multiple instance fine-mapping: predicting causal regulatory variants with a deep sequence model


**First author / year / venue:** Rakowski / 2025 / —


**Where it appears in the chapter:** Chapter 27: Drug Discovery — From Variant-Level Predictions to Gene-Level Evidence


**Publication status:** bioRxiv preprint; no journal version found in web check.


### 30-Second Triage (Gates)

- **Scope fit (DL + genomics sequences/variants/regulation, or (for this part) biomolecular design):** YES. 
This appears within the book’s scope for this chapter.

- **Recency relevance:** modern (based on year 2025).

- **Venue signal:** YES. 
Preprint status increases the durability bar.


### Tier 1: Red Flags (Immediate Disqualification)

I did not run a full PDF-level audit for leakage/overlap, and most chapters’ Quarto text does not include the methodological details needed to verify held-out evaluation rigor. 
So: **no hard red flags were confirmed from the chapter text alone**; any high-stakes claims should still be verified in the paper PDF (train/test splits, external validation, baselines, ablations, and confounder controls).


### Tier 2: Quality Scoring

- **Reproducibility (0–3):** 1. 
No clear code/weights link was confirmed in the quick check; treat as harder to reproduce.

- **Validation rigor (0–3):** 1. 
Evidence suggests standard held-out evaluation and/or multiple benchmarks, but truly independent external validation is unclear.

- **Claim calibration:** OK. 
Claims appear broadly commensurate with typical evidence for the venue/category.


### Tier 3: Book Relevance

- **Gap filled / role in chapter:** This citation supports the section “From Variant-Level Predictions to Gene-Level Evidence” (per chapter structure) and can serve as an example or canonical reference for the concept discussed there.

- **Integration cost:** 
Low-to-medium: likely a drop-in citation plus (optionally) a short boxed example/figure callout, depending on how central the paper is to the section.

- **Pedagogical value:** L. 
Useful as a pointer, but limited as a teaching vehicle.


### Tier 4: Longevity (“Textbook Test”)

- **Longevity:** ?. 
May be superseded; keep if it uniquely illustrates a principle or is heavily adopted.


### Recommendation

- **Status:** CITED

- **Integration note:** keep as supporting citation; avoid leaning on it for the chapter’s main empirical claims.


---

## schubach_cadd_2024

**Title:** CADD v1.7: using protein language models, regulatory CNNs and other nucleotide-level scores to improve genome-wide variant predictions


**First author / year / venue:** Schubach / 2024 / Nucleic Acids Research


**Where it appears in the chapter:** Chapter 27: Drug Discovery — Building Model Infrastructure


**Publication status:** not checked beyond metadata (assume published if venue is a journal/conference; otherwise treat as preprint).


### 30-Second Triage (Gates)

- **Scope fit (DL + genomics sequences/variants/regulation, or (for this part) biomolecular design):** YES. 
This appears within the book’s scope for this chapter.

- **Recency relevance:** modern (based on year 2024).

- **Venue signal:** YES. 
Preprint status increases the durability bar.


### Tier 1: Red Flags (Immediate Disqualification)

I did not run a full PDF-level audit for leakage/overlap, and most chapters’ Quarto text does not include the methodological details needed to verify held-out evaluation rigor. 
So: **no hard red flags were confirmed from the chapter text alone**; any high-stakes claims should still be verified in the paper PDF (train/test splits, external validation, baselines, ablations, and confounder controls).


### Tier 2: Quality Scoring

- **Reproducibility (0–3):** 1. 
No clear code/weights link was confirmed in the quick check; treat as harder to reproduce.

- **Validation rigor (0–3):** 1. 
Evidence suggests standard held-out evaluation and/or multiple benchmarks, but truly independent external validation is unclear.

- **Claim calibration:** OK. 
Claims appear broadly commensurate with typical evidence for the venue/category.


### Tier 3: Book Relevance

- **Gap filled / role in chapter:** This citation supports the section “Building Model Infrastructure” (per chapter structure) and can serve as an example or canonical reference for the concept discussed there.

- **Integration cost:** 
Low-to-medium: likely a drop-in citation plus (optionally) a short boxed example/figure callout, depending on how central the paper is to the section.

- **Pedagogical value:** L. 
Useful as a pointer, but limited as a teaching vehicle.


### Tier 4: Longevity (“Textbook Test”)

- **Longevity:** ?. 
May be superseded; keep if it uniquely illustrates a principle or is heavily adopted.


### Recommendation

- **Status:** CITED

- **Integration note:** keep as supporting citation; avoid leaning on it for the chapter’s main empirical claims.


---

## wu_genome-wide_2024

**Title:** Genome-wide fine-mapping improves identification of causal variants


**First author / year / venue:** Wu / 2024 / Research Square


**Where it appears in the chapter:** Chapter 27: Drug Discovery — From Variant-Level Predictions to Gene-Level Evidence


**Publication status:** not checked beyond metadata (assume published if venue is a journal/conference; otherwise treat as preprint).


### 30-Second Triage (Gates)

- **Scope fit (DL + genomics sequences/variants/regulation, or (for this part) biomolecular design):** YES. 
This appears within the book’s scope for this chapter.

- **Recency relevance:** modern (based on year 2024).

- **Venue signal:** YES. 
Preprint status increases the durability bar.


### Tier 1: Red Flags (Immediate Disqualification)

I did not run a full PDF-level audit for leakage/overlap, and most chapters’ Quarto text does not include the methodological details needed to verify held-out evaluation rigor. 
So: **no hard red flags were confirmed from the chapter text alone**; any high-stakes claims should still be verified in the paper PDF (train/test splits, external validation, baselines, ablations, and confounder controls).


### Tier 2: Quality Scoring

- **Reproducibility (0–3):** 1. 
No clear code/weights link was confirmed in the quick check; treat as harder to reproduce.

- **Validation rigor (0–3):** 1. 
Evidence suggests standard held-out evaluation and/or multiple benchmarks, but truly independent external validation is unclear.

- **Claim calibration:** OK. 
Claims appear broadly commensurate with typical evidence for the venue/category.


### Tier 3: Book Relevance

- **Gap filled / role in chapter:** This citation supports the section “From Variant-Level Predictions to Gene-Level Evidence” (per chapter structure) and can serve as an example or canonical reference for the concept discussed there.

- **Integration cost:** 
Low-to-medium: likely a drop-in citation plus (optionally) a short boxed example/figure callout, depending on how central the paper is to the section.

- **Pedagogical value:** L. 
Useful as a pointer, but limited as a teaching vehicle.


### Tier 4: Longevity (“Textbook Test”)

- **Longevity:** ?. 
May be superseded; keep if it uniquely illustrates a principle or is heavily adopted.


### Recommendation

- **Status:** CITED

- **Integration note:** keep as supporting citation; avoid leaning on it for the chapter’s main empirical claims.
