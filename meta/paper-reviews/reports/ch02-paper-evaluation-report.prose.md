# Chapter 02 Paper Evaluation Report

This report evaluates every paper cited in Chapter 2 (from `p1-ch02.bib`) under the project evaluation framework.

## Summary

Chapter 2 cites 42 papers. Status breakdown: INCLUDE: 41, MONITOR: 1.

## Preprints and publication status

The following citations are preprints or cite preprint versions based on venue metadata: @benegas_traitgym_2025 ([{TraitGym}] {Benchmarking} {DNA} {Sequence} {Models} for {Causal} {Regulatory} {Variant} {Prediction} in {Human} {Genetics}). Where a peer-reviewed version is known, it is noted in the per-paper section.

## Per-paper evaluations

### @amberger_omim_2015

**Bibliographic anchor.** *{OMIM}.org: {Online} {Mendelian} {Inheritance} in {Man} ({OMIM}®), an online catalog of human genes and genetic disorders* (2015; Nucleic Acids Research).

**Scope fit.** Scope fit is indirect: this is primarily a genomic resource or reference database. It fails the strict deep-learning gate but is still valuable for grounding model training and evaluation.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @auton_1kgp_2015

**Bibliographic anchor.** *A global reference for human genetic variation* (2015; Nature).

**Scope fit.** Scope fit is partial: it is cited for context but is not central to deep learning on genomic sequence.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-PopulationResources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @benegas_traitgym_2025

**Bibliographic anchor.** *[{TraitGym}] {Benchmarking} {DNA} {Sequence} {Models} for {Causal} {Regulatory} {Variant} {Prediction} in {Human} {Genetics}* (2025; bioRxiv).

**Scope fit.** Scope fit is supportive: this work defines evaluation practice, calibration, or benchmarking. It is essential scaffolding even when the contribution is not a new deep model.

**Recency relevance.** Recency relevance is strong because it reflects current practice and datasets (2022 or later).

**Venue signal.** Venue signal is provisional because this is a preprint. Treat performance claims as unconfirmed until peer-reviewed or independently replicated.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-SequenceToFunctionModels**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: MONITOR. Promising, but re-check after peer review or broader replication.

**Notes.** Preprint; benchmark study. Re-check for journal publication.

### @bycroft_uk_2018

**Bibliographic anchor.** *The {UK} {Biobank} resource with deep phenotyping and genomic data* (2018; Nature).

**Scope fit.** Scope fit is strong: it directly uses deep learning on genomic sequence, variants, or gene regulation.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-PopulationResources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @edgar_geo_2002

**Bibliographic anchor.** *Gene {Expression} {Omnibus}: {NCBI} gene expression and hybridization array data repository* (2002; Nucleic Acids Research).

**Scope fit.** Scope fit is indirect: this is primarily a genomic resource or reference database. It fails the strict deep-learning gate but is still valuable for grounding model training and evaluation.

**Recency relevance.** Recency relevance is strong in the ‘foundational’ sense: although older, it remains influential and is still commonly cited or used.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 1).** Limited reproducibility signal: the citation is mainly a review, high-level resource description, or guidance; re-running is not the core contribution.

**Validation rigor (score 2).** Moderate validation signal: evaluation is usually present and reasonably broad, but independence across cohorts or prospective validation may be limited.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-FunctionalGenomicsResources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @fokkema_lovd_2011

**Bibliographic anchor.** *LOVD v.2.0: the next generation in gene variant databases* (2011; Human Mutation).

**Scope fit.** Scope fit is indirect: this is primarily a genomic resource or reference database. It fails the strict deep-learning gate but is still valuable for grounding model training and evaluation.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @frankish_gencode_2019

**Bibliographic anchor.** *{GENCODE} reference annotation for the human and mouse genomes* (2019; Nucleic Acids Research).

**Scope fit.** Scope fit is indirect: this is primarily a genomic resource or reference database. It fails the strict deep-learning gate but is still valuable for grounding model training and evaluation.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-FunctionalGenomicsResources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @gamazon_predixcan_2015

**Bibliographic anchor.** *A gene-based association method for mapping traits using reference transcriptome data* (2015; Nature Genetics).

**Scope fit.** Scope fit is supportive: this is statistical genetics methodology and is relevant for interpreting model outputs and downstream genetic inference.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-GeneExpressionImputation**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @gtex_2020

**Bibliographic anchor.** *The {GTEx} {Consortium} atlas of genetic regulatory effects across human tissues* (2020; Science).

**Scope fit.** Scope fit is indirect: this is primarily a genomic resource or reference database. It fails the strict deep-learning gate but is still valuable for grounding model training and evaluation.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-FunctionalGenomicsResources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @gudbjartsson_decode_2015

**Bibliographic anchor.** *Sequence variants from whole genome sequencing a large group of Icelanders* (2015; Scientific Data).

**Scope fit.** Scope fit is supportive: this is a core genomics pipeline or sequencing method that underpins the data used by genomic foundation models.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 1).** Limited reproducibility signal: the citation is mainly a review, high-level resource description, or guidance; re-running is not the core contribution.

**Validation rigor (score 2).** Moderate validation signal: evaluation is usually present and reasonably broad, but independence across cohorts or prospective validation may be limited.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-PopulationResources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @gusev_twas_2016

**Bibliographic anchor.** *Integrative approaches for large-scale transcriptome-wide association studies* (2016; Nature Genetics).

**Scope fit.** Scope fit is supportive: this is statistical genetics methodology and is relevant for interpreting model outputs and downstream genetic inference.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 2).** Moderate reproducibility signal: methods are usually clear and there is often code or an established implementation, but full end-to-end re-running may require additional effort or data access.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-GeneExpressionImputation**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @kagda_encode_2025

**Bibliographic anchor.** *Data navigation on the {ENCODE} portal* (2025; Nature Communications).

**Scope fit.** Scope fit is indirect: this is primarily a genomic resource or reference database. It fails the strict deep-learning gate but is still valuable for grounding model training and evaluation.

**Recency relevance.** Recency relevance is strong because it reflects current practice and datasets (2022 or later).

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-FunctionalGenomicsResources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @karczewski_mutational_2020

**Bibliographic anchor.** *The mutational constraint spectrum quantified from variation in 141,456 humans* (2020; Nature).

**Scope fit.** Scope fit is partial: it is cited for context but is not central to deep learning on genomic sequence.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 2).** Moderate reproducibility signal: methods are usually clear and there is often code or an established implementation, but full end-to-end re-running may require additional effort or data access.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-PopulationResources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @kundaje_roadmap_2015

**Bibliographic anchor.** *Integrative analysis of 111 reference human epigenomes* (2015; Nature).

**Scope fit.** Scope fit is partial: it is cited for context but is not central to deep learning on genomic sequence.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-FunctionalGenomicsResources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @kurki_finngen_2023

**Bibliographic anchor.** *{FinnGen} provides genetic insights from a well-phenotyped isolated population* (2023; Nature).

**Scope fit.** Scope fit is partial: it is cited for context but is not central to deep learning on genomic sequence.

**Recency relevance.** Recency relevance is strong because it reflects current practice and datasets (2022 or later).

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-PopulationResources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @lambert_pgs-catalog_2021

**Bibliographic anchor.** *The {Polygenic} {Score} {Catalog} as an open database for reproducibility and systematic evaluation* (2021; Nature Genetics).

**Scope fit.** Scope fit is indirect: this is primarily a genomic resource or reference database. It fails the strict deep-learning gate but is still valuable for grounding model training and evaluation.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @landrum_clinvar_2018

**Bibliographic anchor.** *{ClinVar}: improving access to variant interpretations and supporting evidence* (2018; Nucleic Acids Research).

**Scope fit.** Scope fit is indirect: this is primarily a genomic resource or reference database. It fails the strict deep-learning gate but is still valuable for grounding model training and evaluation.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 1).** Limited reproducibility signal: the citation is mainly a review, high-level resource description, or guidance; re-running is not the core contribution.

**Validation rigor (score 2).** Moderate validation signal: evaluation is usually present and reasonably broad, but independence across cohorts or prospective validation may be limited.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @liao_draft_2023

**Bibliographic anchor.** *A draft human pangenome reference* (2023; Nature).

**Scope fit.** Scope fit is indirect: this is primarily a genomic resource or reference database. It fails the strict deep-learning gate but is still valuable for grounding model training and evaluation.

**Recency relevance.** Recency relevance is strong because it reflects current practice and datasets (2022 or later).

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @marees_gwas_2018

**Bibliographic anchor.** *[{GWAS}] {A} tutorial on conducting genome-wide association studies: {Quality} control and statistical analysis* (2018; International Journal of Methods in Psychiatric Research).

**Scope fit.** Scope fit is supportive: this work defines evaluation practice, calibration, or benchmarking. It is essential scaffolding even when the contribution is not a new deep model.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @morales_mane_2022

**Bibliographic anchor.** *A joint {NCBI} and {EMBL}-{EBI} transcript set for clinical genomics and research* (2022; Nature).

**Scope fit.** Scope fit is partial: it is cited for context but is not central to deep learning on genomic sequence.

**Recency relevance.** Recency relevance is strong because it reflects current practice and datasets (2022 or later).

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 2).** Moderate reproducibility signal: methods are usually clear and there is often code or an established implementation, but full end-to-end re-running may require additional effort or data access.

**Validation rigor (score 2).** Moderate validation signal: evaluation is usually present and reasonably broad, but independence across cohorts or prospective validation may be limited.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @mountjoy_open_2021

**Bibliographic anchor.** *An open approach to systematically prioritize causal variants and genes at all published human {GWAS} trait-associated loci* (2021; Nature Genetics).

**Scope fit.** Scope fit is supportive: this is statistical genetics methodology and is relevant for interpreting model outputs and downstream genetic inference.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 2).** Moderate reproducibility signal: methods are usually clear and there is often code or an established implementation, but full end-to-end re-running may require additional effort or data access.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @notin_proteingym_2023

**Bibliographic anchor.** *{ProteinGym}: {Large}-{Scale} {Benchmarks} for {Protein} {Fitness} {Prediction} and {Design}* (2023; Advances in Neural Information Processing Systems).

**Scope fit.** Scope fit is supportive: this work defines evaluation practice, calibration, or benchmarking. It is essential scaffolding even when the contribution is not a new deep model.

**Recency relevance.** Recency relevance is strong because it reflects current practice and datasets (2022 or later).

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @null_all-of-us_2019

**Bibliographic anchor.** *The “{All} of {Us}” {Research} {Program}* (2019; New England Journal of Medicine).

**Scope fit.** Scope fit is partial: it is cited for context but is not central to deep learning on genomic sequence.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 1).** Limited reproducibility signal: the citation is mainly a review, high-level resource description, or guidance; re-running is not the core contribution.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @nurk_complete_2022

**Bibliographic anchor.** *The complete sequence of a human genome* (2022; Science).

**Scope fit.** Scope fit is partial: it is cited for context but is not central to deep learning on genomic sequence.

**Recency relevance.** Recency relevance is strong because it reflects current practice and datasets (2022 or later).

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 2).** Moderate reproducibility signal: methods are usually clear and there is often code or an established implementation, but full end-to-end re-running may require additional effort or data access.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @oleary_refseq_2016

**Bibliographic anchor.** *Reference sequence ({RefSeq}) database at {NCBI}: current status, taxonomic expansion, and functional annotation* (2016; Nucleic Acids Research).

**Scope fit.** Scope fit is indirect: this is primarily a genomic resource or reference database. It fails the strict deep-learning gate but is still valuable for grounding model training and evaluation.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @pejaver_calibration_2022

**Bibliographic anchor.** *Calibration of computational tools for missense variant pathogenicity classification and {ClinGen} recommendations for {PP3}/{BP4} criteria* (2022; American Journal of Human Genetics).

**Scope fit.** Scope fit is supportive: this work defines evaluation practice, calibration, or benchmarking. It is essential scaffolding even when the contribution is not a new deep model.

**Recency relevance.** Recency relevance is strong because it reflects current practice and datasets (2022 or later).

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @regev_cell-atlas_2017

**Bibliographic anchor.** *The {Human} {Cell} {Atlas}* (2017; eLife).

**Scope fit.** Scope fit is indirect: this is primarily a genomic resource or reference database. It fails the strict deep-learning gate but is still valuable for grounding model training and evaluation.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @rehm_clingen_2015

**Bibliographic anchor.** *{ClinGen} — {The} {Clinical} {Genome} {Resource}* (2015; New England Journal of Medicine).

**Scope fit.** Scope fit is indirect: this is primarily a genomic resource or reference database. It fails the strict deep-learning gate but is still valuable for grounding model training and evaluation.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @rentzsch_cadd_2019

**Bibliographic anchor.** *{CADD}: predicting the deleteriousness of variants throughout the human genome* (2019; Nucleic Acids Research).

**Scope fit.** Scope fit is partial: it is cited for context but is not central to deep learning on genomic sequence.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 1).** Limited reproducibility signal: the citation is mainly a review, high-level resource description, or guidance; re-running is not the core contribution.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @schubach_cadd_2024

**Bibliographic anchor.** *{CADD} v1.7: using protein language models, regulatory {CNNs} and other nucleotide-level scores to improve genome-wide variant predictions* (2024; Nucleic Acids Research).

**Scope fit.** Scope fit is strong: it directly uses deep learning on genomic sequence, variants, or gene regulation.

**Recency relevance.** Recency relevance is strong because it reflects current practice and datasets (2022 or later).

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 1).** Limited reproducibility signal: the citation is mainly a review, high-level resource description, or guidance; re-running is not the core contribution.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-SequenceToFunctionModels**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @sherry_dbsnp_2001

**Bibliographic anchor.** *{dbSNP}: the {NCBI} database of genetic variation* (2001; Nucleic Acids Research).

**Scope fit.** Scope fit is indirect: this is primarily a genomic resource or reference database. It fails the strict deep-learning gate but is still valuable for grounding model training and evaluation.

**Recency relevance.** Recency relevance is strong in the ‘foundational’ sense: although older, it remains influential and is still commonly cited or used.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @sirugo_diversity_2019

**Bibliographic anchor.** *The {Missing} {Diversity} in {Human} {Genetic} {Studies}* (2019; Cell).

**Scope fit.** Scope fit is partial: it is cited for context but is not central to deep learning on genomic sequence.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 2).** Moderate reproducibility signal: methods are usually clear and there is often code or an established implementation, but full end-to-end re-running may require additional effort or data access.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @sollis_gwas-catalog_2023

**Bibliographic anchor.** *The {NHGRI}-{EBI} {GWAS} {Catalog}: knowledgebase and deposition resource* (2023; Nucleic Acids Research).

**Scope fit.** Scope fit is indirect: this is primarily a genomic resource or reference database. It fails the strict deep-learning gate but is still valuable for grounding model training and evaluation.

**Recency relevance.** Recency relevance is strong because it reflects current practice and datasets (2022 or later).

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @stenson_hgmd_2017

**Bibliographic anchor.** *The Human Gene Mutation Database: towards a comprehensive repository of inherited mutation data for medical research, genetic diagnosis and next-generation sequencing studies* (2017; Human Genetics).

**Scope fit.** Scope fit is indirect: this is primarily a genomic resource or reference database. It fails the strict deep-learning gate but is still valuable for grounding model training and evaluation.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @sullivan_leveraging_2023

**Bibliographic anchor.** *Leveraging base-pair mammalian constraint to understand genetic variation and human disease* (2023; Science).

**Scope fit.** Scope fit is partial: it is cited for context but is not central to deep learning on genomic sequence.

**Recency relevance.** Recency relevance is strong because it reflects current practice and datasets (2022 or later).

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 2).** Moderate reproducibility signal: methods are usually clear and there is often code or an established implementation, but full end-to-end re-running may require additional effort or data access.

**Validation rigor (score 2).** Moderate validation signal: evaluation is usually present and reasonably broad, but independence across cohorts or prospective validation may be limited.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @tabula_sapiens_2022

**Bibliographic anchor.** *The {Tabula} {Sapiens}: {A} multiple-organ, single-cell transcriptomic atlas of humans* (2022; Science).

**Scope fit.** Scope fit is indirect: this is primarily a genomic resource or reference database. It fails the strict deep-learning gate but is still valuable for grounding model training and evaluation.

**Recency relevance.** Recency relevance is strong because it reflects current practice and datasets (2022 or later).

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @vosa_eqtl-gen_2021

**Bibliographic anchor.** *Large-scale cis- and trans-{eQTL} analyses identify thousands of genetic loci and polygenic scores that regulate blood gene expression* (2021; Nature Genetics).

**Scope fit.** Scope fit is supportive: this is statistical genetics methodology and is relevant for interpreting model outputs and downstream genetic inference.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 2).** Moderate reproducibility signal: methods are usually clear and there is often code or an established implementation, but full end-to-end re-running may require additional effort or data access.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @whirl-PharmGKB_2012

**Bibliographic anchor.** *Pharmacogenomics {Knowledge} for {Personalized} {Medicine}* (2012; Clinical Pharmacology \& Therapeutics).

**Scope fit.** Scope fit is partial: it is cited for context but is not central to deep learning on genomic sequence.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 1).** Limited reproducibility signal: the citation is mainly a review, high-level resource description, or guidance; re-running is not the core contribution.

**Validation rigor (score 2).** Moderate validation signal: evaluation is usually present and reasonably broad, but independence across cohorts or prospective validation may be limited.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @yun_accurate_2021

**Bibliographic anchor.** *Accurate, scalable cohort variant calls using {DeepVariant} and {GLnexus}* (2021; Bioinformatics).

**Scope fit.** Scope fit is strong: it directly uses deep learning on genomic sequence, variants, or gene regulation.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-SequenceToFunctionModels**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @zheng_cistrome_2019

**Bibliographic anchor.** *Cistrome {Data} {Browser}: expanded datasets and new tools for gene regulatory analysis* (2019; Nucleic Acids Research).

**Scope fit.** Scope fit is indirect: this is primarily a genomic resource or reference database. It fails the strict deep-learning gate but is still valuable for grounding model training and evaluation.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-FunctionalGenomicsResources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @zhou_deepsea_2015

**Bibliographic anchor.** *[{DeepSEA}] {Predicting} effects of noncoding variants with deep learning–based sequence model* (2015; Nature Methods).

**Scope fit.** Scope fit is strong: it directly uses deep learning on genomic sequence, variants, or gene regulation.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 2).** Moderate reproducibility signal: methods are usually clear and there is often code or an established implementation, but full end-to-end re-running may require additional effort or data access.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-SequenceToFunctionModels**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @zhou_expecto_2018

**Bibliographic anchor.** *[{Expecto}] {Deep} learning sequence-based ab initio prediction of variant effects on expression and disease risk* (2018; Nature Genetics).

**Scope fit.** Scope fit is strong: it directly uses deep learning on genomic sequence, variants, or gene regulation.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch02-SequenceToFunctionModels**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.
