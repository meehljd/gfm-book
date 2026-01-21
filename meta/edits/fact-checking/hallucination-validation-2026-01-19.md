# Hallucination Validation Report

**Date:** 2026-01-19
**Purpose:** Verify flagged potential hallucinations against primary sources

---

## Summary

| Claim | Location | Verdict | Action |
|-------|----------|---------|--------|
| HyenaDNA "1,500x fewer parameters" | Ch07:388 | **VALIDATED** | None needed |
| DNALongBench benchmark | Ch11 | **VALIDATED** | None needed |
| LRB (Long Range Benchmark) | Ch11 | **VALIDATED** | None needed |
| GenBench benchmark | Ch11 | **VALIDATED** | None needed |
| Evo 2 "7B/40B parameters" | Ch15 | **VALIDATED** | None needed |
| Evo 2 "9.3 trillion tokens" | Ch15 | **PARTIALLY VALIDATED** | Clarify: nucleotides vs tokens |
| Metformin "1.8 hops" | Ch30:144 | **NOT VERIFIED** | Add citation or mark illustrative |
| Geisinger "847 VUS" | Ch32:361 | **NOT VERIFIED** | Add citation or mark illustrative |

---

## Detailed Verification

### 1. HyenaDNA "1,500 times fewer parameters" (Ch07:388)

**Book claim:**
> "HyenaDNA achieves state-of-the-art results on 12 of 18 benchmarks from the Nucleotide Transformer suite while using 1,500 times fewer parameters"

**Verification:**
From the [HyenaDNA paper (Nguyen et al. 2023)](https://arxiv.org/abs/2306.15794) and [Hazy Research blog](https://hazyresearch.stanford.edu/blog/2023-06-29-hyena-dna):

> "On benchmarks from the Nucleotide Transformer, HyenaDNA uses a model with **1500x fewer parameters (2.5B vs 1.6M)** and 3200x less pretraining data"

**Verdict: VALIDATED**

The claim comes directly from the original paper. The comparison is:
- Nucleotide Transformer: 2.5B parameters
- HyenaDNA: 1.6M parameters
- Ratio: 2,500,000,000 / 1,600,000 = 1,562.5x (approximately 1,500x)

**Initial fact-check assessment was INCORRECT** - the 1,500x figure is accurate and comes from the paper itself.

---

### 2. Benchmark Names (Ch11)

#### DNALongBench

**Verification:**
- Published in [Nature Communications (2025)](https://www.nature.com/articles/s41467-025-65077-4)
- [GitHub repository](https://github.com/ma-compbio/DNALONGBENCH) available
- Covers 5 genomics tasks with long-range dependencies up to 1M base pairs

**Verdict: VALIDATED** - Real benchmark, published in peer-reviewed journal.

#### LRB (Long Range Benchmark / Human Genomics Long-Range Benchmark)

**Verification:**
- Available on [HuggingFace](https://huggingface.co/datasets/InstaDeepAI/genomics-long-range-benchmark)
- Published at OpenReview
- Contains 9 tasks for evaluating DNA language models on long-range dependencies

**Verdict: VALIDATED** - Real benchmark from InstaDeep.

#### GenBench

**Verification:**
- Published at [NeurIPS 2024](https://arxiv.org/abs/2406.01627)
- [GitHub repository](https://github.com/jimmylihui/GenBench) available
- Comprehensive benchmark with 43 datasets spanning coding regions, non-coding regions, and genomic architecture

**Verdict: VALIDATED** - Real benchmark, published at top venue.

---

### 3. Evo 2 Model Specifications (Ch15)

**Book claims:**
- "7 billion and 40 billion parameter variants"
- "9.3 trillion DNA tokens"

**Verification from [Arc Institute](https://arcinstitute.org/news/evo2) and [bioRxiv preprint](https://www.biorxiv.org/content/10.1101/2025.02.18.638918v1):**

> "Evo 2 features both **7B and 40B parameter** architectures"

> "Evo 2 is a biological foundation model trained on **9.3 trillion DNA base pairs**"

However, another source states:
> "Evo 2 was trained autoregressively on OpenGenome2, a dataset containing **8.8 trillion tokens**"

**Verdict: PARTIALLY VALIDATED**

- **Parameters:** 7B and 40B are **CORRECT**
- **Training data:** 9.3 trillion refers to **nucleotides/base pairs**, not tokens. Some sources report 8.8 trillion tokens (due to tokenization).

**Recommended action:** Clarify in book that "9.3 trillion" refers to nucleotides (base pairs), or use "8.8 trillion tokens" if referring to tokenized data.

---

### 4. Metformin "1.8 hops" Network Distance (Ch30:144)

**Book claim:**
> "The network proximity score (mean shortest path from metformin targets to cancer genes: 1.8 hops) was in the top 5% of all approved drugs."

**Verification:**
Searched for:
- "metformin network proximity cancer"
- "metformin protein network distance hops"
- "drug target disease genes average distance"

**Findings:**
- Found general literature on network medicine approaches (e.g., [Nature Communications 2018](https://www.nature.com/articles/s41467-018-05116-5))
- Found that metformin IS studied in network-based cancer repurposing contexts
- Found general concepts about network proximity scoring
- **Could NOT find any source for the specific "1.8 hops" value**

**Verdict: NOT VERIFIED**

The specific "1.8 hops" value could not be traced to any publication. This appears to be either:
1. A fabricated illustrative number
2. From an unpublished analysis
3. A misremembered or approximated value

**Recommended action:**
- Add citation if source exists
- OR remove the specific number and say "low network proximity"
- OR explicitly mark as illustrative: "e.g., ~1.8 hops"

---

### 5. Geisinger "847 VUS reclassified" (Ch32:361)

**Book claim:**
> "VUS reclassified through outcomes: 847 variants"
> "The 847 VUS reclassifications represent knowledge generated by the health system itself"

**Verification:**
Searched for:
- "Geisinger VUS reclassified MyCode"
- "Geisinger 847 variants"
- Geisinger MyCode publications

**Findings:**
- Geisinger MyCode is real and has enrolled 350,000+ patients
- VUS reclassification IS part of their program
- One study showed reclassification of "2% of VUS" in a specific kidney disease context (only ~10-20 variants)
- Another mentions "5,000+ participants at increased risk have received results"
- **Could NOT find the specific "847" number anywhere**

**Verdict: NOT VERIFIED**

The specific "847 VUS" number could not be traced to any publication. This appears to be either:
1. A fabricated number for the illustrative case study
2. From internal/unpublished Geisinger data
3. An aggregated estimate not from a single source

**Recommended action:**
- Verify with Geisinger contacts if you have them
- OR cite the source if it exists
- OR explicitly mark the entire case study as illustrative/hypothetical
- OR replace with documented numbers from published Geisinger papers

---

## Corrections to Previous Assessment

The initial fact-check report incorrectly flagged the following as potential hallucinations:

| Claim | Initial Assessment | Corrected Assessment |
|-------|-------------------|---------------------|
| HyenaDNA 1,500x parameters | "Likely error - should be ~357x" | **CORRECT** - 1,500x is from original paper |
| DNALongBench | "May not exist" | **EXISTS** - Nature Communications 2025 |
| LRB | "May not exist" | **EXISTS** - InstaDeep/HuggingFace |
| GenBench | "May not exist" | **EXISTS** - NeurIPS 2024 |

---

## Final Recommendations

### No Action Required
1. Ch07:388 - HyenaDNA parameter claim is **accurate**
2. Ch11 - All three benchmarks (DNALongBench, LRB, GenBench) **exist and are documented**
3. Ch15 - Evo 2 7B/40B parameters are **accurate**

### Minor Clarification Needed
4. **Ch15 - Evo 2 training data:** Clarify that "9.3 trillion" refers to nucleotides/base pairs. If using "tokens," the number is ~8.8 trillion.

### Citation or Revision Required
5. **Ch30:144 - Metformin "1.8 hops":** Add citation or revise to qualitative description
6. **Ch32:361 - Geisinger "847 VUS":** Add citation or mark case study as illustrative

---

## Sources Consulted

### HyenaDNA
- [arXiv:2306.15794](https://arxiv.org/abs/2306.15794)
- [Hazy Research Blog](https://hazyresearch.stanford.edu/blog/2023-06-29-hyena-dna)
- [NeurIPS 2023 Proceedings](https://papers.neurips.cc/paper_files/paper/2023/file/86ab6927ee4ae9bde4247793c46797c7-Paper-Conference.pdf)

### Nucleotide Transformer
- [Nature Methods 2024](https://www.nature.com/articles/s41592-024-02523-z)
- [HuggingFace Model Card](https://huggingface.co/InstaDeepAI/nucleotide-transformer-2.5b-multi-species)

### DNALongBench
- [Nature Communications 2025](https://www.nature.com/articles/s41467-025-65077-4)
- [GitHub](https://github.com/ma-compbio/DNALONGBENCH)

### LRB (Long Range Benchmark)
- [HuggingFace Dataset](https://huggingface.co/datasets/InstaDeepAI/genomics-long-range-benchmark)
- [OpenReview](https://openreview.net/forum?id=8O9HLDrmtq)

### GenBench
- [arXiv:2406.01627](https://arxiv.org/abs/2406.01627)
- [GitHub](https://github.com/jimmylihui/GenBench)

### Evo 2
- [Arc Institute](https://arcinstitute.org/news/evo2)
- [bioRxiv 2025](https://www.biorxiv.org/content/10.1101/2025.02.18.638918v1)

### Metformin Network Medicine
- [Nature Communications 2018](https://www.nature.com/articles/s41467-018-05116-5)
- [Cell Reports Medicine 2022](https://www.cell.com/cell-reports-medicine/fulltext/S2666-3791(22)00298-1)

### Geisinger MyCode
- [PMID 33576083](https://pubmed.ncbi.nlm.nih.gov/33576083/)
- [Genetics in Medicine 2020](https://www.nature.com/articles/s41436-020-0876-4)

---

*Report generated by validation against primary sources.*
