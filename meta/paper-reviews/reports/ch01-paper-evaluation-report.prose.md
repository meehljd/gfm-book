# Chapter 01 Paper Evaluation Report

This report evaluates every paper cited in Chapter 1 (from `p1-ch01.bib`) under the project evaluation framework.

## Summary

Chapter 1 cites 34 papers. Status breakdown: INCLUDE: 34.

## Preprints and publication status

The following citations are preprints or cite preprint versions based on venue metadata: @li_aligning_2013 (Aligning sequence reads, clone sequences and assembly contigs with BWA-MEM). Where a peer-reviewed version is known, it is noted in the per-paper section.

## Per-paper evaluations

### @browning_fast_2021

**Bibliographic anchor.** *Fast two-stage phasing of large-scale sequence data* (2021; Am J Hum Genet).

**Scope fit.** Scope fit is supportive: this is a core genomics pipeline or sequencing method that underpins the data used by genomic foundation models.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-HaplotypePhasing/Imputation**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

**Notes.** Two-stage phasing; cohort-scale speed/accuracy evidence

### @bycroft_uk_2018

**Bibliographic anchor.** *UK Biobank resource w/ deep phenotyping & genomic data* (2018; Nature).

**Scope fit.** Scope fit is strong: it directly uses deep learning on genomic sequence, variants, or gene regulation.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 2).** Moderate reproducibility signal: methods are usually clear and there is often code or an established implementation, but full end-to-end re-running may require additional effort or data access.

**Validation rigor (score 2).** Moderate validation signal: evaluation is usually present and reasonably broad, but independence across cohorts or prospective validation may be limited.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-CohortCalling/GLnexus**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

**Notes.** Canonical biobank-scale cohort + QC/imputation context

### @dabernig-heinz_multicenter_2024

**Bibliographic anchor.** *Multicenter ONT genotyping accuracy & reproducibility* (2024; J Clin Microbiol).

**Scope fit.** Scope fit is partial: it is cited for context but is not central to deep learning on genomic sequence.

**Recency relevance.** Recency relevance is strong because it reflects current practice and datasets (2022 or later).

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 2).** Moderate reproducibility signal: methods are usually clear and there is often code or an established implementation, but full end-to-end re-running may require additional effort or data access.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-LongReadTech**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

**Notes.** Multi-lab ONT study; strain-specific errors; mitigations via models/polish

### @depristo_framework_2011

**Bibliographic anchor.** *Framework for variation discovery & genotyping (NGS)* (2011; Nat Genet).

**Scope fit.** Scope fit is partial: it is cited for context but is not central to deep learning on genomic sequence.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 2).** Moderate reproducibility signal: methods are usually clear and there is often code or an established implementation, but full end-to-end re-running may require additional effort or data access.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-ClassicalPipelines/CohortFiltering**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

**Notes.** Foundational pipeline stages + validation across technologies/designs

### @garrison_variation_2018

**Bibliographic anchor.** *Variation graph toolkit improves read mapping (vg)* (2018; Nat Biotechnol).

**Scope fit.** Scope fit is supportive: this is a core genomics pipeline or sequencing method that underpins the data used by genomic foundation models.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-HLA/ComplexRegions**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

**Notes.** Graph references reduce mapping bias; practical human-scale toolkit

### @goodwin_coming_2016

**Bibliographic anchor.** *Coming of age: ten years of next-generation sequencing technologies* (2016; Nat Rev Genet).

**Scope fit.** Scope fit is supportive: this is a core genomics pipeline or sequencing method that underpins the data used by genomic foundation models.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 1).** Limited reproducibility signal: the citation is mainly a review, high-level resource description, or guidance; re-running is not the core contribution.

**Validation rigor (score 1-2).** Validation rigor could not be scored confidently from the available metadata.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-NGSChallenge**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

**Notes.** High-level tech evolution + limitations; good framing citation

### @jiang_long-read-based_2020

**Bibliographic anchor.** *Long-read-based human genomic structural variation detection with cuteSV* (2020; Genome Biology).

**Scope fit.** Scope fit is partial: it is cited for context but is not central to deep learning on genomic sequence.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 2-3).** Validation rigor could not be scored confidently from the available metadata.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-LongReadSV**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

**Notes.** cuteSV signatures + clustering/refinement; benchmarked on sim+real data

### @karczewski_mutational_2020

**Bibliographic anchor.** *Mutational constraint spectrum from variation in 141,456 humans (gnomAD)* (2020; Nature).

**Scope fit.** Scope fit is indirect: this is primarily a genomic resource or reference database. It fails the strict deep-learning gate but is still valuable for grounding model training and evaluation.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 2).** Moderate reproducibility signal: methods are usually clear and there is often code or an established implementation, but full end-to-end re-running may require additional effort or data access.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-PopResources/Interpretation**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

**Notes.** Constraint metrics; addendum highlights pLoF artefact risk and need for curation

### @krusche_best_2019

**Bibliographic anchor.** *Best practices for benchmarking germline small-variant calls in human genomes* (2019; Nat Biotechnol).

**Scope fit.** Scope fit is supportive: this work defines evaluation practice, calibration, or benchmarking. It is essential scaffolding even when the contribution is not a new deep model.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-Evaluation/Benchmarks**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

**Notes.** GA4GH benchmarking framework; standard metrics/stratification; hap.py ecosystem

### @li_aligning_2013

**Bibliographic anchor.** *Aligning sequence reads, clone sequences and assembly contigs with BWA-MEM* (2013; arXiv).

**Scope fit.** Scope fit is supportive: this is a core genomics pipeline or sequencing method that underpins the data used by genomic foundation models.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is provisional because this is a preprint. Treat performance claims as unconfirmed until peer-reviewed or independently replicated.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 2).** Moderate validation signal: evaluation is usually present and reasonably broad, but independence across cohorts or prospective validation may be limited.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-Alignment**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

**Notes.** SMEM seeding + re-seeding; banded affine-gap DP; chimeric/PE rescue; sim benchmarking + runtimes

### @li_towards_2014

**Bibliographic anchor.** *Towards {Better} {Understanding} of {Artifacts} in {Variant} {Calling} from {High}-{Coverage} {Samples}* (2014; Bioinformatics).

**Scope fit.** Scope fit is partial: it is cited for context but is not central to deep learning on genomic sequence.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 2).** Moderate validation signal: evaluation is usually present and reasonably broad, but independence across cohorts or prospective validation may be limited.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-Foundations**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

**Notes.** Published in Bioinformatics (2014); arXiv version also exists.

### @li_minimap2_2018

**Bibliographic anchor.** *Minimap2: pairwise alignment for nucleotide sequences* (2018; Bioinformatics).

**Scope fit.** Scope fit is supportive: this is a core genomics pipeline or sequencing method that underpins the data used by genomic foundation models.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 2).** Moderate validation signal: evaluation is usually present and reasonably broad, but independence across cohorts or prospective validation may be limited.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-Alignment**. Integration cost is low because it is already positioned as a reference point in that section.

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

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-Foundations**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @loh_reference-based_2016

**Bibliographic anchor.** *Reference-based phasing using the {Haplotype} {Reference} {Consortium} panel* (2016; Nature Genetics).

**Scope fit.** Scope fit is indirect: this is primarily a genomic resource or reference database. It fails the strict deep-learning gate but is still valuable for grounding model training and evaluation.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-Phasing**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @mallal_hla-b5701_2008

**Bibliographic anchor.** *{HLA}-{B}*5701 {Screening} for {Hypersensitivity} to {Abacavir}* (2008; New England Journal of Medicine).

**Scope fit.** Scope fit is partial: it is cited for context but is not central to deep learning on genomic sequence.

**Recency relevance.** Recency relevance is strong in the ‘foundational’ sense: although older, it remains influential and is still commonly cited or used.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 1).** Limited reproducibility signal: the citation is mainly a review, high-level resource description, or guidance; re-running is not the core contribution.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-Foundations**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @nielsen_genotype_2011

**Bibliographic anchor.** *Genotype and {SNP} calling from next-generation sequencing data* (2011; Nature Reviews. Genetics).

**Scope fit.** Scope fit is supportive: this is a core genomics pipeline or sequencing method that underpins the data used by genomic foundation models.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 2).** Moderate reproducibility signal: methods are usually clear and there is often code or an established implementation, but full end-to-end re-running may require additional effort or data access.

**Validation rigor (score 2).** Moderate validation signal: evaluation is usually present and reasonably broad, but independence across cohorts or prospective validation may be limited.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-Foundations**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @noauthor_pacificbiosciencespbsv_2025

**Bibliographic anchor.** *{PacificBiosciences}/pbsv* (2025; PacBio).

**Scope fit.** Scope fit is partial: it is cited for context but is not central to deep learning on genomic sequence.

**Recency relevance.** Recency relevance is strong because it reflects current practice and datasets (2022 or later).

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 2).** Moderate validation signal: evaluation is usually present and reasonably broad, but independence across cohorts or prospective validation may be limited.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-StructuralVariants**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @noauthor_realtimegenomicsrtg-core_2025

**Bibliographic anchor.** *{RealTimeGenomics}/rtg-core* (2025; Real Time Genomics).

**Scope fit.** Scope fit is partial: it is cited for context but is not central to deep learning on genomic sequence.

**Recency relevance.** Recency relevance is strong because it reflects current practice and datasets (2022 or later).

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 2).** Moderate validation signal: evaluation is usually present and reasonably broad, but independence across cohorts or prospective validation may be limited.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-Foundations**. Integration cost is low because it is already positioned as a reference point in that section.

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

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-Foundations**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @oconnell_general_2014

**Bibliographic anchor.** *A {General} {Approach} for {Haplotype} {Phasing} across the {Full} {Spectrum} of {Relatedness}* (2014; PLOS Genetics).

**Scope fit.** Scope fit is supportive: this is a core genomics pipeline or sequencing method that underpins the data used by genomic foundation models.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-Phasing**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @poplin_deepvariant_2018

**Bibliographic anchor.** *[{DeepVariant}] {A} universal {SNP} and small-indel variant caller using deep neural networks* (2018; Nature Biotechnology).

**Scope fit.** Scope fit is strong: it directly uses deep learning on genomic sequence, variants, or gene regulation.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 2).** Moderate reproducibility signal: methods are usually clear and there is often code or an established implementation, but full end-to-end re-running may require additional effort or data access.

**Validation rigor (score 2).** Moderate validation signal: evaluation is usually present and reasonably broad, but independence across cohorts or prospective validation may be limited.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-VariantCallingDL**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @robinson_ipd-imgthla_2020

**Bibliographic anchor.** *{IPD}-{IMGT}/{HLA} {Database}* (2020; Nucleic Acids Research).

**Scope fit.** Scope fit is indirect: this is primarily a genomic resource or reference database. It fails the strict deep-learning gate but is still valuable for grounding model training and evaluation.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-Foundations**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @sakaue_tutorial_2023

**Bibliographic anchor.** *Tutorial: a statistical genetics guide to identifying {HLA} alleles driving complex disease* (2023; Nature Protocols).

**Scope fit.** Scope fit is supportive: this work defines evaluation practice, calibration, or benchmarking. It is essential scaffolding even when the contribution is not a new deep model.

**Recency relevance.** Recency relevance is strong because it reflects current practice and datasets (2022 or later).

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-Foundations**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @shafin_haplotype-aware_2021

**Bibliographic anchor.** *Haplotype-aware variant calling with {PEPPER}-{Margin}-{DeepVariant} enables high accuracy in nanopore long-reads* (2021; Nature Methods).

**Scope fit.** Scope fit is strong: it directly uses deep learning on genomic sequence, variants, or gene regulation.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 2).** Moderate validation signal: evaluation is usually present and reasonably broad, but independence across cohorts or prospective validation may be limited.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-VariantCallingDL**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @smolka_detection_2024

**Bibliographic anchor.** *Detection of mosaic and population-level structural variants with {Sniffles2}* (2024; Nature Biotechnology).

**Scope fit.** Scope fit is supportive: this is a core genomics pipeline or sequencing method that underpins the data used by genomic foundation models.

**Recency relevance.** Recency relevance is strong because it reflects current practice and datasets (2022 or later).

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-StructuralVariants**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @song_t1k_2022

**Bibliographic anchor.** *{T1K}: efficient and accurate {KIR} and {HLA} genotyping with next-generation sequencing data* (2023; Genome Res).

**Scope fit.** Scope fit is supportive: this is a core genomics pipeline or sequencing method that underpins the data used by genomic foundation models.

**Recency relevance.** Recency relevance is strong because it reflects current practice and datasets (2022 or later).

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 1).** Limited reproducibility signal: the citation is mainly a review, high-level resource description, or guidance; re-running is not the core contribution.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-Foundations**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

**Notes.** Published version: Genome Research 2023 (doi:10.1101/gr.277585.122).

### @van_der_auwera_fastq_2018

**Bibliographic anchor.** *From {FastQ} {Data} to {High}-{Confidence} {Variant} {Calls}: {The} {Genome} {Analysis} {Toolkit} {Best} {Practices} {Pipeline}* (2018; Current Protocols in Bioinformatics).

**Scope fit.** Scope fit is partial: it is cited for context but is not central to deep learning on genomic sequence.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 2).** Moderate validation signal: evaluation is usually present and reasonably broad, but independence across cohorts or prospective validation may be limited.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-Foundations**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @wenger_accurate_2019

**Bibliographic anchor.** *Accurate circular consensus long-read sequencing improves variant detection and assembly of a human genome* (2019; Nature Biotechnology).

**Scope fit.** Scope fit is supportive: this is a core genomics pipeline or sequencing method that underpins the data used by genomic foundation models.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 2).** Moderate reproducibility signal: methods are usually clear and there is often code or an established implementation, but full end-to-end re-running may require additional effort or data access.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-Foundations**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

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

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-Foundations**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @zheng_symphonizing_2022

**Bibliographic anchor.** *Symphonizing pileup and full-alignment for deep learning-based long-read variant calling* (2022; Nature Computational Science).

**Scope fit.** Scope fit is strong: it directly uses deep learning on genomic sequence, variants, or gene regulation.

**Recency relevance.** Recency relevance is strong because it reflects current practice and datasets (2022 or later).

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 2).** Moderate validation signal: evaluation is usually present and reasonably broad, but independence across cohorts or prospective validation may be limited.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-VariantCallingDL**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (?).** Longevity outlook is uncertain: likely useful now, but may be superseded or depends on current benchmarks and tooling.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @zook_open_2019

**Bibliographic anchor.** *An open resource for accurately benchmarking small variant and reference calls* (2019; Nature biotechnology).

**Scope fit.** Scope fit is indirect: this is primarily a genomic resource or reference database. It fails the strict deep-learning gate but is still valuable for grounding model training and evaluation.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper’s role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-Resources**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

### @rubinacci_efficient_2021

**Bibliographic anchor.** *Efficient phasing and imputation of low-coverage sequencing data using large reference panels* (2021; Nat Genet).

**Scope fit.** Scope fit is supportive: this is a core genomics pipeline or sequencing method that underpins the data used by genomic foundation models.

**Recency relevance.** Recency relevance is acceptable: it represents established practice that is still directly used or cited in modern pipelines.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper's role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 3).** High reproducibility signal: the work is typically accompanied by usable implementations and sufficient methodological detail to re-run, and in many cases has become part of standard toolchains.

**Validation rigor (score 3).** Strong validation signal: results are typically supported across multiple independent datasets, cohorts, or orthogonal truth sets, often with careful stratification or error analysis.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-Imputation/LowCoverage**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

**Notes.** GLIMPSE method for low-coverage WGS imputation; demonstrates 90% reduction in false call rates; key enabler of low-pass sequencing strategies.

### @zanger_cytochrome_2013

**Bibliographic anchor.** *Cytochrome P450 enzymes in drug metabolism: regulation of gene expression, enzyme activities, and impact of genetic variation* (2013; Pharmacol Ther).

**Scope fit.** Scope fit is partial: it is cited for context but is not central to deep learning on genomic sequence.

**Recency relevance.** Recency relevance is strong in the 'foundational' sense: although older, it remains influential and is still commonly cited or used.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper's role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 1).** Limited reproducibility signal: the citation is mainly a review, high-level resource description, or guidance; re-running is not the core contribution.

**Validation rigor (score 2).** Moderate validation signal: comprehensive review synthesizing evidence from many primary studies.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-SegmentalDuplications/CYP2D6**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (H).** High pedagogical value: it teaches a durable concept, provides a canonical reference, or includes figures and experimental framing that readers can reuse.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

**Notes.** Comprehensive CYP450 review; source for "~25% of drugs metabolized by CYP2D6" statistic; highly cited pharmacogenomics reference.

### @ingelman-sundberg_genetic_2005

**Bibliographic anchor.** *Genetic polymorphisms of cytochrome P450 2D6 (CYP2D6): clinical consequences, evolutionary aspects and functional diversity* (2005; Pharmacogenomics J).

**Scope fit.** Scope fit is partial: it is cited for context but is not central to deep learning on genomic sequence.

**Recency relevance.** Recency relevance is strong in the 'foundational' sense: although older, it remains influential and is still commonly cited or used.

**Venue signal.** Venue signal is strong: it is published in a reputable journal or conference and has clear provenance.

**Tier 1 red-flags check.** Based on the citation context and the paper's role (method, resource, or benchmark), there are no obvious immediate red flags like missing evaluation, but a full read should still confirm held-out testing, leakage control, and appropriate baselines when the paper is used for performance claims.

**Reproducibility (score 1).** Limited reproducibility signal: the citation is mainly a review, high-level resource description, or guidance; re-running is not the core contribution.

**Validation rigor (score 2).** Moderate validation signal: comprehensive review synthesizing evidence from many primary studies.

**Claim calibration.** Claims appear calibrated to the evidence as cited in the chapter.

**Book relevance and integration.** In the manuscript, this citation supports **Ch01-SegmentalDuplications/CYP2D6**. Integration cost is low because it is already positioned as a reference point in that section.

**Pedagogical value (M).** Moderate pedagogical value: it is useful for context and as a reference, but it may not be the clearest teaching vehicle on its own.

**Longevity (+).** Longevity outlook is positive: likely to remain a standard reference or durable exemplar through 2030.

**Framework decision.** Decision: INCLUDE as a durable anchor for the chapter section noted below.

**Notes.** Classic CYP2D6-specific reference; covers clinical phenotypes (poor/intermediate/extensive/ultra-rapid metabolizers) and substrate specificity.
