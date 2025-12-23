# Chapter 08 — Paper evaluation report (prose)

Processed in alphabetical order by citation key. Date: 2025-12-22.


### avsec_enformer_2021

[Enformer] Effective gene expression prediction from sequence by integrating long-range interactions — Avsec, Žiga and Agarwal, Vikram and Visentin, D. and Ledsam, J. and Grabska-Barwinska, A. and Taylor, Kyle R. and Assael, Yannis and Jumper, J. and Kohli, Pushmeet and Kelley, David R. — Nature Methods (2021) — DOI: 10.1038/s41592-021-01252-x — URL: https://consensus.app/papers/effective-gene-expression-prediction-from-sequence-by-avsec-agarwal/6afb944129f35bad916e6f4a889c07cb/

**Scope fit.** This work is in-scope for the book: it applies deep learning to biological sequences (genomics), with direct relevance to genomic/protein foundation models or downstream tasks.

**Recency relevance.** This is mid-era work (year 2021) that often serves as a bridge between early deep learning for sequences and modern foundation models.

**Venue signal.** The venue given in the BibTeX entry is Nature Methods. This is generally a credible signal, but final confidence depends on confirming the version-of-record (especially if the entry is a preprint).

**Tier 1 red flags.** No immediate red flags are visible from bibliographic metadata alone. However, the framework’s highest-risk failure modes (data leakage, weak baselines, missing held-out evaluation, circular validation) require checking the paper PDF and supplementary methods.

**Reproducibility (0–3): 2.** This line of work commonly provides sufficient methodological detail and/or some artifacts (code, models, or datasets), but this should be confirmed in the PDF and associated repositories.

**Validation rigor (0–3): 2.** Validation is likely reasonably rigorous (multiple benchmarks or tasks), though the independence of test sets should be verified.

**Claim calibration.** No obvious over-claiming is detectable from the citation metadata alone; confirm by reading the abstract/results to ensure claims match evidence.

**Book relevance (gap filled).** This paper likely supports a core concept, model family, benchmark, or deployment-relevant application that the textbook should teach explicitly.

**Integration cost.** Integration cost: moderate. Recommend adding a short boxed example/figure plus a citation, and referencing it in the relevant chapter narrative.

**Pedagogical value.** Moderate pedagogical value: useful concept, but may require careful framing or simplification.

**Longevity.** Likely to remain relevant (‘textbook test’ passes).

**PDF availability.** Publisher PDF via DOI (may be paywalled).

**Recommendation.** INCLUDE. Suggested book location: Ch08 (genomic sequence modeling).


---

### devlin_bert_2019

BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding — Devlin, Jacob and Chang, Ming-Wei and Lee, Kenton and Toutanova, Kristina — arXiv (2019) — DOI: 10.48550/arXiv.1810.04805 — URL: http://arxiv.org/abs/1810.04805

**Scope fit.** This paper is not genomics-specific, but it is relevant background: it introduces or analyzes a general deep learning method (e.g., Transformers, scaling laws, parameter-efficient fine-tuning, or calibration) that is widely reused in genomic foundation models.

**Recency relevance.** This is a foundational paper (year 2019) that remains influential and is still commonly cited in modern foundation-model practice.

**Venue signal.** The BibTeX entry does not specify a venue (journal/conference). This weakens venue signal until a version-of-record is confirmed. Preprint/published-status check: Published version: NAACL (2019).

**Tier 1 red flags.** No immediate red flags are visible from bibliographic metadata alone. However, the framework’s highest-risk failure modes (data leakage, weak baselines, missing held-out evaluation, circular validation) require checking the paper PDF and supplementary methods.

**Reproducibility (0–3): 2.** This line of work commonly provides sufficient methodological detail and/or some artifacts (code, models, or datasets), but this should be confirmed in the PDF and associated repositories.

**Validation rigor (0–3): 1.** Validation is likely limited (e.g., single benchmark or closely related datasets), pending PDF verification.

**Claim calibration.** No obvious over-claiming is detectable from the citation metadata alone; confirm by reading the abstract/results to ensure claims match evidence.

**Book relevance (gap filled).** This paper is useful as supporting/background material rather than a centerpiece.

**Integration cost.** Integration cost: low. A brief citation (and possibly a one-sentence pointer) is usually sufficient.

**Pedagogical value.** Lower pedagogical value: mostly background or incremental, best kept as a citation only.

**Longevity.** Likely to remain relevant (‘textbook test’ passes).

**PDF availability.** Likely public PDF via preprint server.

**Recommendation.** CITED. Suggested book location: Ch08 (methods background).


---

### encode_project_integrated_2012

Placeholder: encode project integrated 2012 — (2012)

**Scope fit.** Scope fit is unclear from the BibTeX metadata alone; the title/venue do not unambiguously signal deep learning over genomic or protein sequences.

**Recency relevance.** This is a foundational paper (year 2012) that remains influential and is still commonly cited in modern foundation-model practice.

**Venue signal.** The BibTeX entry does not specify a venue (journal/conference). This weakens venue signal until a version-of-record is confirmed.

**Tier 1 red flags.** No immediate red flags are visible from bibliographic metadata alone. However, the framework’s highest-risk failure modes (data leakage, weak baselines, missing held-out evaluation, circular validation) require checking the paper PDF and supplementary methods.

**Reproducibility (0–3): 1.** Reproducibility is unclear from the citation metadata; assume methods-only unless the PDF provides code/data/weights.

**Validation rigor (0–3): 1.** Validation is likely limited (e.g., single benchmark or closely related datasets), pending PDF verification.

**Claim calibration.** No obvious over-claiming is detectable from the citation metadata alone; confirm by reading the abstract/results to ensure claims match evidence.

**Book relevance (gap filled).** This paper is useful as supporting/background material rather than a centerpiece.

**Integration cost.** Integration cost: low. A brief citation (and possibly a one-sentence pointer) is usually sufficient.

**Pedagogical value.** Moderate pedagogical value: useful concept, but may require careful framing or simplification.

**Longevity.** Longevity uncertain; adoption and replication should be monitored.

**PDF availability.** PDF not identifiable from BibTeX metadata.

**Recommendation.** CITED. Suggested book location: Ch08.


---

### ferruz_protgpt2_2022

ProtGPT2 is a deep unsupervised language model for protein design — Ferruz, Noelia and Schmidt, Steffen and Höcker, Birte — Nature Communications (2022) — DOI: 10.1038/s41467-022-32007-7 — URL: https://www.nature.com/articles/s41467-022-32007-7

**Scope fit.** This work is in-scope for the book: it applies deep learning to biological sequences (protein), with direct relevance to genomic/protein foundation models or downstream tasks.

**Recency relevance.** This is recent/modern work (year 2022), aligned with current genomic foundation-model approaches.

**Venue signal.** The venue given in the BibTeX entry is Nature Communications. This is generally a credible signal, but final confidence depends on confirming the version-of-record (especially if the entry is a preprint).

**Tier 1 red flags.** No immediate red flags are visible from bibliographic metadata alone. However, the framework’s highest-risk failure modes (data leakage, weak baselines, missing held-out evaluation, circular validation) require checking the paper PDF and supplementary methods.

**Reproducibility (0–3): 2.** This line of work commonly provides sufficient methodological detail and/or some artifacts (code, models, or datasets), but this should be confirmed in the PDF and associated repositories.

**Validation rigor (0–3): 2.** Validation is likely reasonably rigorous (multiple benchmarks or tasks), though the independence of test sets should be verified.

**Claim calibration.** No obvious over-claiming is detectable from the citation metadata alone; confirm by reading the abstract/results to ensure claims match evidence.

**Book relevance (gap filled).** This paper likely supports a core concept, model family, benchmark, or deployment-relevant application that the textbook should teach explicitly.

**Integration cost.** Integration cost: moderate. Recommend adding a short boxed example/figure plus a citation, and referencing it in the relevant chapter narrative.

**Pedagogical value.** Moderate pedagogical value: useful concept, but may require careful framing or simplification.

**Longevity.** Likely to remain relevant (‘textbook test’ passes).

**PDF availability.** Publisher PDF via DOI (may be paywalled).

**Recommendation.** INCLUDE. Suggested book location: Ch08 (protein models/variant effects).


---

### hoffmann_training_2022

Placeholder: hoffmann training 2022 — (2022)

**Scope fit.** Scope fit is unclear from the BibTeX metadata alone; the title/venue do not unambiguously signal deep learning over genomic or protein sequences.

**Recency relevance.** This is recent/modern work (year 2022), aligned with current genomic foundation-model approaches.

**Venue signal.** The BibTeX entry does not specify a venue (journal/conference). This weakens venue signal until a version-of-record is confirmed.

**Tier 1 red flags.** No immediate red flags are visible from bibliographic metadata alone. However, the framework’s highest-risk failure modes (data leakage, weak baselines, missing held-out evaluation, circular validation) require checking the paper PDF and supplementary methods.

**Reproducibility (0–3): 1.** Reproducibility is unclear from the citation metadata; assume methods-only unless the PDF provides code/data/weights.

**Validation rigor (0–3): 1.** Validation is likely limited (e.g., single benchmark or closely related datasets), pending PDF verification.

**Claim calibration.** No obvious over-claiming is detectable from the citation metadata alone; confirm by reading the abstract/results to ensure claims match evidence.

**Book relevance (gap filled).** This paper is useful as supporting/background material rather than a centerpiece.

**Integration cost.** Integration cost: low. A brief citation (and possibly a one-sentence pointer) is usually sufficient.

**Pedagogical value.** Moderate pedagogical value: useful concept, but may require careful framing or simplification.

**Longevity.** Longevity uncertain; adoption and replication should be monitored.

**PDF availability.** PDF not identifiable from BibTeX metadata.

**Recommendation.** CITED. Suggested book location: Ch08.


---

### ji_dnabert_2021

DNABERT: pre-trained Bidirectional Encoder Representations from Transformers model for DNA-language in genome — Ji, Yanrong and Zhou, Zhihan and Liu, Han and Davuluri, Ramana V — Bioinformatics (2021) — DOI: 10.1093/bioinformatics/btab083 — URL: https://doi.org/10.1093/bioinformatics/btab083

**Scope fit.** This work is in-scope for the book: it applies deep learning to biological sequences (genomics), with direct relevance to genomic/protein foundation models or downstream tasks.

**Recency relevance.** This is mid-era work (year 2021) that often serves as a bridge between early deep learning for sequences and modern foundation models.

**Venue signal.** The venue given in the BibTeX entry is Bioinformatics. This is generally a credible signal, but final confidence depends on confirming the version-of-record (especially if the entry is a preprint).

**Tier 1 red flags.** No immediate red flags are visible from bibliographic metadata alone. However, the framework’s highest-risk failure modes (data leakage, weak baselines, missing held-out evaluation, circular validation) require checking the paper PDF and supplementary methods.

**Reproducibility (0–3): 2.** This line of work commonly provides sufficient methodological detail and/or some artifacts (code, models, or datasets), but this should be confirmed in the PDF and associated repositories.

**Validation rigor (0–3): 2.** Validation is likely reasonably rigorous (multiple benchmarks or tasks), though the independence of test sets should be verified.

**Claim calibration.** No obvious over-claiming is detectable from the citation metadata alone; confirm by reading the abstract/results to ensure claims match evidence.

**Book relevance (gap filled).** This paper likely supports a core concept, model family, benchmark, or deployment-relevant application that the textbook should teach explicitly.

**Integration cost.** Integration cost: moderate. Recommend adding a short boxed example/figure plus a citation, and referencing it in the relevant chapter narrative.

**Pedagogical value.** Moderate pedagogical value: useful concept, but may require careful framing or simplification.

**Longevity.** Likely to remain relevant (‘textbook test’ passes).

**PDF availability.** Publisher PDF via DOI (may be paywalled).

**Recommendation.** INCLUDE. Suggested book location: Ch08 (genomic sequence modeling).


---

### kaplan_scaling_2020

Placeholder: kaplan scaling 2020 — (2020)

**Scope fit.** This paper is not genomics-specific, but it is relevant background: it introduces or analyzes a general deep learning method (e.g., Transformers, scaling laws, parameter-efficient fine-tuning, or calibration) that is widely reused in genomic foundation models.

**Recency relevance.** This is mid-era work (year 2020) that often serves as a bridge between early deep learning for sequences and modern foundation models.

**Venue signal.** The BibTeX entry does not specify a venue (journal/conference). This weakens venue signal until a version-of-record is confirmed.

**Tier 1 red flags.** No immediate red flags are visible from bibliographic metadata alone. However, the framework’s highest-risk failure modes (data leakage, weak baselines, missing held-out evaluation, circular validation) require checking the paper PDF and supplementary methods.

**Reproducibility (0–3): 2.** This line of work commonly provides sufficient methodological detail and/or some artifacts (code, models, or datasets), but this should be confirmed in the PDF and associated repositories.

**Validation rigor (0–3): 1.** Validation is likely limited (e.g., single benchmark or closely related datasets), pending PDF verification.

**Claim calibration.** No obvious over-claiming is detectable from the citation metadata alone; confirm by reading the abstract/results to ensure claims match evidence.

**Book relevance (gap filled).** This paper is useful as supporting/background material rather than a centerpiece.

**Integration cost.** Integration cost: low. A brief citation (and possibly a one-sentence pointer) is usually sufficient.

**Pedagogical value.** Lower pedagogical value: mostly background or incremental, best kept as a citation only.

**Longevity.** Likely to remain relevant (‘textbook test’ passes).

**PDF availability.** PDF not identifiable from BibTeX metadata.

**Recommendation.** CITED. Suggested book location: Ch08 (methods background).


---

### karczewski_gnomad_2020

The mutational constraint spectrum quantified from variation in 141,456 humans — Karczewski, Konrad J. and Francioli, Laurent C. and Tiao, Grace and Cummings, Beryl B. and Alföldi, Jessica and Wang, Qingbo and Collins, Ryan L. and Laricchia, Kristen M. and Ganna, Andrea and Birnbaum, Daniel P. and Gauthier, Laura D. and Brand, Harrison and Solomonson, Matthew and Watts, Nicholas A. and Rhodes, Daniel and Singer-Berk, Moriel and England, Eleina M. and Seaby, Eleanor G. and Kosmicki, Jack A. and Walters, Raymond K. and Tashman, Katherine and Farjoun, Yossi and Banks, Eric and Poterba, Timothy and Wang, Arcturus and Seed, Cotton and Whiffin, Nicola and Chong, Jessica X. and Samocha, Kaitlin E. and Pierce-Hoffman, Emma and Zappala, Zachary and O’Donnell-Luria, Anne H. and Minikel, Eric Vallabh and Weisburd, Ben and Lek, Monkol and Ware, James S. and Vittal, Christopher and Armean, Irina M. and Bergelson, Louis and Cibulskis, Kristian and Connolly, Kristen M. and Covarrubias, Miguel and Donnelly, Stacey and Ferriera, Steven and Gabriel, Stacey and Gentry, Jeff and Gupta, Namrata and Jeandet, Thibault and Kaplan, Diane and Llanwarne, Christopher and Munshi, Ruchi and Novod, Sam and Petrillo, Nikelle and Roazen, David and Ruano-Rubio, Valentin and Saltzman, Andrea and Schleicher, Molly and Soto, Jose and Tibbetts, Kathleen and Tolonen, Charlotte and Wade, Gordon and Talkowski, Michael E. and Neale, Benjamin M. and Daly, Mark J. and MacArthur, Daniel G. — Nature (2020) — DOI: 10.1038/s41586-020-2308-7 — URL: https://www.nature.com/articles/s41586-020-2308-7

**Scope fit.** This work is in-scope for the book: it applies deep learning to biological sequences (protein), with direct relevance to genomic/protein foundation models or downstream tasks.

**Recency relevance.** This is mid-era work (year 2020) that often serves as a bridge between early deep learning for sequences and modern foundation models.

**Venue signal.** The venue given in the BibTeX entry is Nature. This is generally a credible signal, but final confidence depends on confirming the version-of-record (especially if the entry is a preprint).

**Tier 1 red flags.** No immediate red flags are visible from bibliographic metadata alone. However, the framework’s highest-risk failure modes (data leakage, weak baselines, missing held-out evaluation, circular validation) require checking the paper PDF and supplementary methods.

**Reproducibility (0–3): 2.** This line of work commonly provides sufficient methodological detail and/or some artifacts (code, models, or datasets), but this should be confirmed in the PDF and associated repositories.

**Validation rigor (0–3): 2.** Validation is likely reasonably rigorous (multiple benchmarks or tasks), though the independence of test sets should be verified.

**Claim calibration.** No obvious over-claiming is detectable from the citation metadata alone; confirm by reading the abstract/results to ensure claims match evidence.

**Book relevance (gap filled).** This paper likely supports a core concept, model family, benchmark, or deployment-relevant application that the textbook should teach explicitly.

**Integration cost.** Integration cost: moderate. Recommend adding a short boxed example/figure plus a citation, and referencing it in the relevant chapter narrative.

**Pedagogical value.** Moderate pedagogical value: useful concept, but may require careful framing or simplification.

**Longevity.** Likely to remain relevant (‘textbook test’ passes).

**PDF availability.** Publisher PDF via DOI (may be paywalled).

**Recommendation.** INCLUDE. Suggested book location: Ch08 (protein models/variant effects).


---

### landrum_clinvar_2018

ClinVar: improving access to variant interpretations and supporting evidence — Landrum, Melissa J and Lee, Jennifer M and Benson, Mark and Brown, Garth R and Chao, Chen and Chitipiralla, Shanmuga and Gu, Baoshan and Hart, Jennifer and Hoffman, Douglas and Jang, Wonhee and Karapetyan, Karen and Katz, Kenneth and Liu, Chunlei and Maddipatla, Zenith and Malheiro, Adriana and McDaniel, Kurt and Ovetsky, Michael and Riley, George and Zhou, George and Holmes, J Bradley and Kattman, Brandi L and Maglott, Donna R — Nucleic Acids Research (2018) — DOI: 10.1093/nar/gkx1153 — URL: https://doi.org/10.1093/nar/gkx1153

**Scope fit.** This work is in-scope for the book: it applies deep learning to biological sequences (genomics), with direct relevance to genomic/protein foundation models or downstream tasks.

**Recency relevance.** This is a foundational paper (year 2018) that remains influential and is still commonly cited in modern foundation-model practice.

**Venue signal.** The venue given in the BibTeX entry is Nucleic Acids Research. This is generally a credible signal, but final confidence depends on confirming the version-of-record (especially if the entry is a preprint).

**Tier 1 red flags.** No immediate red flags are visible from bibliographic metadata alone. However, the framework’s highest-risk failure modes (data leakage, weak baselines, missing held-out evaluation, circular validation) require checking the paper PDF and supplementary methods.

**Reproducibility (0–3): 2.** This line of work commonly provides sufficient methodological detail and/or some artifacts (code, models, or datasets), but this should be confirmed in the PDF and associated repositories.

**Validation rigor (0–3): 2.** Validation is likely reasonably rigorous (multiple benchmarks or tasks), though the independence of test sets should be verified.

**Claim calibration.** No obvious over-claiming is detectable from the citation metadata alone; confirm by reading the abstract/results to ensure claims match evidence.

**Book relevance (gap filled).** This paper likely supports a core concept, model family, benchmark, or deployment-relevant application that the textbook should teach explicitly.

**Integration cost.** Integration cost: moderate. Recommend adding a short boxed example/figure plus a citation, and referencing it in the relevant chapter narrative.

**Pedagogical value.** Moderate pedagogical value: useful concept, but may require careful framing or simplification.

**Longevity.** Likely to remain relevant (‘textbook test’ passes).

**PDF availability.** Publisher PDF via DOI (may be paywalled).

**Recommendation.** INCLUDE. Suggested book location: Ch08 (genomic sequence modeling).


---

### lin_evolutionary_2023

Placeholder: lin evolutionary 2023 — (2023)

**Scope fit.** Scope fit is unclear from the BibTeX metadata alone; the title/venue do not unambiguously signal deep learning over genomic or protein sequences.

**Recency relevance.** This is recent/modern work (year 2023), aligned with current genomic foundation-model approaches.

**Venue signal.** The BibTeX entry does not specify a venue (journal/conference). This weakens venue signal until a version-of-record is confirmed.

**Tier 1 red flags.** No immediate red flags are visible from bibliographic metadata alone. However, the framework’s highest-risk failure modes (data leakage, weak baselines, missing held-out evaluation, circular validation) require checking the paper PDF and supplementary methods.

**Reproducibility (0–3): 1.** Reproducibility is unclear from the citation metadata; assume methods-only unless the PDF provides code/data/weights.

**Validation rigor (0–3): 1.** Validation is likely limited (e.g., single benchmark or closely related datasets), pending PDF verification.

**Claim calibration.** No obvious over-claiming is detectable from the citation metadata alone; confirm by reading the abstract/results to ensure claims match evidence.

**Book relevance (gap filled).** This paper is useful as supporting/background material rather than a centerpiece.

**Integration cost.** Integration cost: low. A brief citation (and possibly a one-sentence pointer) is usually sufficient.

**Pedagogical value.** Moderate pedagogical value: useful concept, but may require careful framing or simplification.

**Longevity.** Longevity uncertain; adoption and replication should be monitored.

**PDF availability.** PDF not identifiable from BibTeX metadata.

**Recommendation.** CITED. Suggested book location: Ch08.


---

### linder_borzoi_2023

[Borzoi] Predicting RNA-seq coverage from DNA sequence as a unifying model of gene regulation — Linder, Johannes and Srivastava, Divyanshi and Yuan, Han and Agarwal, Vikram and Kelley, David R. — Nature Genetics (2025) — DOI: 10.1038/s41588-024-02053-6 — URL: https://www.nature.com/articles/s41588-024-02053-6

**Scope fit.** This work is in-scope for the book: it applies deep learning to biological sequences (genomics), with direct relevance to genomic/protein foundation models or downstream tasks.

**Recency relevance.** This is recent/modern work (year 2025), aligned with current genomic foundation-model approaches.

**Venue signal.** The venue given in the BibTeX entry is Nature Genetics. This is generally a credible signal, but final confidence depends on confirming the version-of-record (especially if the entry is a preprint).

**Tier 1 red flags.** No immediate red flags are visible from bibliographic metadata alone. However, the framework’s highest-risk failure modes (data leakage, weak baselines, missing held-out evaluation, circular validation) require checking the paper PDF and supplementary methods.

**Reproducibility (0–3): 2.** This line of work commonly provides sufficient methodological detail and/or some artifacts (code, models, or datasets), but this should be confirmed in the PDF and associated repositories.

**Validation rigor (0–3): 2.** Validation is likely reasonably rigorous (multiple benchmarks or tasks), though the independence of test sets should be verified.

**Claim calibration.** No obvious over-claiming is detectable from the citation metadata alone; confirm by reading the abstract/results to ensure claims match evidence.

**Book relevance (gap filled).** This paper likely supports a core concept, model family, benchmark, or deployment-relevant application that the textbook should teach explicitly.

**Integration cost.** Integration cost: moderate. Recommend adding a short boxed example/figure plus a citation, and referencing it in the relevant chapter narrative.

**Pedagogical value.** Moderate pedagogical value: useful concept, but may require careful framing or simplification.

**Longevity.** Longevity uncertain; adoption and replication should be monitored.

**PDF availability.** Publisher PDF via DOI (may be paywalled).

**Recommendation.** INCLUDE. Suggested book location: Ch08 (genomic sequence modeling).


---

### nguyen_hyenadna_2023

HyenaDNA: Long-Range Genomic Sequence Modeling at Single Nucleotide Resolution — Nguyen, Eric and Poli, Michael and Faizi, Marjan and Thomas, Armin and Birch-Sykes, Callum and Wornow, Michael and Patel, Aman and Rabideau, Clayton and Massaroli, Stefano and Bengio, Yoshua and Ermon, Stefano and Baccus, Stephen A. and Ré, Chris — arXiv (2023) — DOI: 10.48550/arXiv.2306.15794 — URL: http://arxiv.org/abs/2306.15794

**Scope fit.** This work is in-scope for the book: it applies deep learning to biological sequences (genomics), with direct relevance to genomic/protein foundation models or downstream tasks.

**Recency relevance.** This is recent/modern work (year 2023), aligned with current genomic foundation-model approaches.

**Venue signal.** The BibTeX entry does not specify a venue (journal/conference). This weakens venue signal until a version-of-record is confirmed. Preprint/published-status check: Published version: NeurIPS 2023 (same title).

**Tier 1 red flags.** No immediate red flags are visible from bibliographic metadata alone. However, the framework’s highest-risk failure modes (data leakage, weak baselines, missing held-out evaluation, circular validation) require checking the paper PDF and supplementary methods.

**Reproducibility (0–3): 2.** This line of work commonly provides sufficient methodological detail and/or some artifacts (code, models, or datasets), but this should be confirmed in the PDF and associated repositories.

**Validation rigor (0–3): 2.** Validation is likely reasonably rigorous (multiple benchmarks or tasks), though the independence of test sets should be verified.

**Claim calibration.** No obvious over-claiming is detectable from the citation metadata alone; confirm by reading the abstract/results to ensure claims match evidence.

**Book relevance (gap filled).** This paper likely supports a core concept, model family, benchmark, or deployment-relevant application that the textbook should teach explicitly.

**Integration cost.** Integration cost: moderate. Recommend adding a short boxed example/figure plus a citation, and referencing it in the relevant chapter narrative.

**Pedagogical value.** High pedagogical value: clean principle or widely-reused method with teachable examples/figures.

**Longevity.** Likely to remain relevant (‘textbook test’ passes).

**PDF availability.** Likely public PDF via preprint server.

**Recommendation.** INCLUDE. Suggested book location: Ch08 (genomic sequence modeling).


---

### nguyen_sequence_2024

Placeholder: nguyen sequence 2024 — (2024)

**Scope fit.** Scope fit is unclear from the BibTeX metadata alone; the title/venue do not unambiguously signal deep learning over genomic or protein sequences.

**Recency relevance.** This is recent/modern work (year 2024), aligned with current genomic foundation-model approaches.

**Venue signal.** The BibTeX entry does not specify a venue (journal/conference). This weakens venue signal until a version-of-record is confirmed.

**Tier 1 red flags.** No immediate red flags are visible from bibliographic metadata alone. However, the framework’s highest-risk failure modes (data leakage, weak baselines, missing held-out evaluation, circular validation) require checking the paper PDF and supplementary methods.

**Reproducibility (0–3): 1.** Reproducibility is unclear from the citation metadata; assume methods-only unless the PDF provides code/data/weights.

**Validation rigor (0–3): 1.** Validation is likely limited (e.g., single benchmark or closely related datasets), pending PDF verification.

**Claim calibration.** No obvious over-claiming is detectable from the citation metadata alone; confirm by reading the abstract/results to ensure claims match evidence.

**Book relevance (gap filled).** This paper is useful as supporting/background material rather than a centerpiece.

**Integration cost.** Integration cost: low. A brief citation (and possibly a one-sentence pointer) is usually sufficient.

**Pedagogical value.** Moderate pedagogical value: useful concept, but may require careful framing or simplification.

**Longevity.** Longevity uncertain; adoption and replication should be monitored.

**PDF availability.** PDF not identifiable from BibTeX metadata.

**Recommendation.** CITED. Suggested book location: Ch08.


---

### oord_representation_2018

Placeholder: oord representation 2018 — (2018)

**Scope fit.** Scope fit is unclear from the BibTeX metadata alone; the title/venue do not unambiguously signal deep learning over genomic or protein sequences.

**Recency relevance.** This is a foundational paper (year 2018) that remains influential and is still commonly cited in modern foundation-model practice.

**Venue signal.** The BibTeX entry does not specify a venue (journal/conference). This weakens venue signal until a version-of-record is confirmed.

**Tier 1 red flags.** No immediate red flags are visible from bibliographic metadata alone. However, the framework’s highest-risk failure modes (data leakage, weak baselines, missing held-out evaluation, circular validation) require checking the paper PDF and supplementary methods.

**Reproducibility (0–3): 1.** Reproducibility is unclear from the citation metadata; assume methods-only unless the PDF provides code/data/weights.

**Validation rigor (0–3): 1.** Validation is likely limited (e.g., single benchmark or closely related datasets), pending PDF verification.

**Claim calibration.** No obvious over-claiming is detectable from the citation metadata alone; confirm by reading the abstract/results to ensure claims match evidence.

**Book relevance (gap filled).** This paper is useful as supporting/background material rather than a centerpiece.

**Integration cost.** Integration cost: low. A brief citation (and possibly a one-sentence pointer) is usually sufficient.

**Pedagogical value.** Moderate pedagogical value: useful concept, but may require careful framing or simplification.

**Longevity.** Longevity uncertain; adoption and replication should be monitored.

**PDF availability.** PDF not identifiable from BibTeX metadata.

**Recommendation.** CITED. Suggested book location: Ch08.


---

### raffel_t5_2019

Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer — Raffel, Colin and Shazeer, Noam and Roberts, Adam and Lee, Katherine and Narang, Sharan and Matena, Michael and Zhou, Yanqi and Li, Wei and Liu, Peter J. — arXiv (2019) — DOI: 10.48550/arXiv.1910.10683 — URL: http://arxiv.org/abs/1910.10683

**Scope fit.** This paper is not genomics-specific, but it is relevant background: it introduces or analyzes a general deep learning method (e.g., Transformers, scaling laws, parameter-efficient fine-tuning, or calibration) that is widely reused in genomic foundation models.

**Recency relevance.** This is a foundational paper (year 2019) that remains influential and is still commonly cited in modern foundation-model practice.

**Venue signal.** The BibTeX entry does not specify a venue (journal/conference). This weakens venue signal until a version-of-record is confirmed. Preprint/published-status check: Published version: JMLR (2020).

**Tier 1 red flags.** No immediate red flags are visible from bibliographic metadata alone. However, the framework’s highest-risk failure modes (data leakage, weak baselines, missing held-out evaluation, circular validation) require checking the paper PDF and supplementary methods.

**Reproducibility (0–3): 2.** This line of work commonly provides sufficient methodological detail and/or some artifacts (code, models, or datasets), but this should be confirmed in the PDF and associated repositories.

**Validation rigor (0–3): 1.** Validation is likely limited (e.g., single benchmark or closely related datasets), pending PDF verification.

**Claim calibration.** No obvious over-claiming is detectable from the citation metadata alone; confirm by reading the abstract/results to ensure claims match evidence.

**Book relevance (gap filled).** This paper is useful as supporting/background material rather than a centerpiece.

**Integration cost.** Integration cost: low. A brief citation (and possibly a one-sentence pointer) is usually sufficient.

**Pedagogical value.** Lower pedagogical value: mostly background or incremental, best kept as a citation only.

**Longevity.** Likely to remain relevant (‘textbook test’ passes).

**PDF availability.** Likely public PDF via preprint server.

**Recommendation.** CITED. Suggested book location: Ch08 (methods background).


---

### suzek_uniref_2015

UniRef: comprehensive and non-redundant UniProt reference clusters — Suzek, Baris E. and Huang, Hongzhan and McGarvey, Peter and Mazumder, Raja and Wu, Cathy H. — Bioinformatics (2007) — DOI: 10.1093/bioinformatics/btm098 — URL: https://doi.org/10.1093/bioinformatics/btm098

**Scope fit.** Scope fit is unclear from the BibTeX metadata alone; the title/venue do not unambiguously signal deep learning over genomic or protein sequences.

**Recency relevance.** This is a foundational paper (year 2007) that remains influential and is still commonly cited in modern foundation-model practice.

**Venue signal.** The venue given in the BibTeX entry is Bioinformatics. This is generally a credible signal, but final confidence depends on confirming the version-of-record (especially if the entry is a preprint).

**Tier 1 red flags.** No immediate red flags are visible from bibliographic metadata alone. However, the framework’s highest-risk failure modes (data leakage, weak baselines, missing held-out evaluation, circular validation) require checking the paper PDF and supplementary methods.

**Reproducibility (0–3): 1.** Reproducibility is unclear from the citation metadata; assume methods-only unless the PDF provides code/data/weights.

**Validation rigor (0–3): 1.** Validation is likely limited (e.g., single benchmark or closely related datasets), pending PDF verification.

**Claim calibration.** No obvious over-claiming is detectable from the citation metadata alone; confirm by reading the abstract/results to ensure claims match evidence.

**Book relevance (gap filled).** This paper is useful as supporting/background material rather than a centerpiece.

**Integration cost.** Integration cost: low. A brief citation (and possibly a one-sentence pointer) is usually sufficient.

**Pedagogical value.** Moderate pedagogical value: useful concept, but may require careful framing or simplification.

**Longevity.** Longevity uncertain; adoption and replication should be monitored.

**PDF availability.** Publisher PDF via DOI (may be paywalled).

**Recommendation.** CITED. Suggested book location: Ch08.


---

### zhou_dnabert2_2023

DNABERT-2: Efficient Foundation Model and Benchmark For Multi-Species Genome — Zhou, Zhihan and Ji, Yanrong and Li, Weijian and Dutta, Pratik and Davuluri, Ramana and Liu, Han — arXiv (2024) — DOI: 10.48550/arXiv.2306.15006 — URL: http://arxiv.org/abs/2306.15006

**Scope fit.** This work is in-scope for the book: it applies deep learning to biological sequences (genomics), with direct relevance to genomic/protein foundation models or downstream tasks.

**Recency relevance.** This is recent/modern work (year 2024), aligned with current genomic foundation-model approaches.

**Venue signal.** The BibTeX entry does not specify a venue (journal/conference). This weakens venue signal until a version-of-record is confirmed. Preprint/published-status check: Earlier preprint; later published as ICLR 2024 (DNABERT-2).

**Tier 1 red flags.** No immediate red flags are visible from bibliographic metadata alone. However, the framework’s highest-risk failure modes (data leakage, weak baselines, missing held-out evaluation, circular validation) require checking the paper PDF and supplementary methods.

**Reproducibility (0–3): 2.** This line of work commonly provides sufficient methodological detail and/or some artifacts (code, models, or datasets), but this should be confirmed in the PDF and associated repositories.

**Validation rigor (0–3): 2.** Validation is likely reasonably rigorous (multiple benchmarks or tasks), though the independence of test sets should be verified.

**Claim calibration.** No obvious over-claiming is detectable from the citation metadata alone; confirm by reading the abstract/results to ensure claims match evidence.

**Book relevance (gap filled).** This paper likely supports a core concept, model family, benchmark, or deployment-relevant application that the textbook should teach explicitly.

**Integration cost.** Integration cost: moderate. Recommend adding a short boxed example/figure plus a citation, and referencing it in the relevant chapter narrative.

**Pedagogical value.** High pedagogical value: clean principle or widely-reused method with teachable examples/figures.

**Longevity.** Likely to remain relevant (‘textbook test’ passes).

**PDF availability.** Likely public PDF via preprint server.

**Recommendation.** INCLUDE. Suggested book location: Ch08 (genomic sequence modeling).


---
