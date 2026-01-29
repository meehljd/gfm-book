"""
Pronunciation Guide for GFM Book TTS

This module provides text replacements to help TTS engines
correctly pronounce genomics, ML, and technical terms.

Usage:
    from pronunciation_guide import apply_pronunciations
    text = apply_pronunciations(text)
"""

import re

# =============================================================================
# ACRONYMS - Spell out or expand
# =============================================================================

ACRONYMS = {
    # Genomics Core
    "GWAS": "G-W-A-S",
    "SNP": "snip",
    "SNPs": "snips",
    "SNV": "S-N-V",
    "SNVs": "S-N-Vs",
    "eQTL": "E-Q-T-L",
    "eQTLs": "E-Q-T-Ls",
    "pQTL": "P-Q-T-L",
    "mQTL": "M-Q-T-L",
    "sQTL": "S-Q-T-L",
    "QTL": "Q-T-L",
    "VEP": "V-E-P",
    "VUS": "V-U-S",
    "MAF": "M-A-F",
    "LD": "L-D",
    "PRS": "P-R-S",
    "PGS": "P-G-S",
    "FDR": "F-D-R",
    "PIP": "P-I-P",
    "HWE": "H-W-E",

    # Evaluation Metrics
    "AUROC": "A-U-R-O-C",
    "auROC": "A-U-R-O-C",
    "AUC": "A-U-C",
    "AUPRC": "A-U-P-R-C",
    "ROC": "R-O-C",
    "ECE": "E-C-E",
    "MLM": "M-L-M",
    "NLL": "N-L-L",

    # Sequencing Methods
    "RNA-seq": "R-N-A-seek",
    "scRNA-seq": "single-cell R-N-A-seek",
    "ChIP-seq": "chip-seek",
    "ATAC-seq": "attack-seek",
    "DNase-seq": "D-N-ase-seek",
    "CLIP-seq": "clip-seek",
    "Hi-C": "high-C",
    "HiC": "high-C",
    "CAGE": "cage",
    "MPRA": "M-P-R-A",
    "DMS": "D-M-S",
    "ISM": "I-S-M",
    "MSA": "M-S-A",

    # File Formats
    "VCF": "V-C-F",
    "BAM": "B-A-M",
    "FASTA": "fast-A",
    "FASTQ": "fast-Q",
    "BED": "bed",
    "GTF": "G-T-F",
    "GFF": "G-F-F",
    "HDF5": "H-D-F-5",
    "TSV": "T-S-V",
    "CSV": "C-S-V",

    # Databases
    "gnomAD": "genome-A-D",
    "ClinVar": "clin-var",
    "ENCODE": "encode",
    "GTEx": "G-tex",
    "UniProt": "uni-prot",
    "UniRef": "uni-ref",
    "Rfam": "R-fam",
    "JASPAR": "jaspar",
    "OMIM": "O-M-I-M",
    "dbSNP": "D-B-snip",
    "MaveDB": "mave-D-B",

    # Standards & Organizations
    "ACMG": "A-C-M-G",
    "AMP": "A-M-P",
    "CASP": "C-A-S-P",
    "FDA": "F-D-A",
    "CLIA": "C-L-I-A",
    "HIPAA": "hippa",
    "IRB": "I-R-B",

    # ML/Stats
    "CNN": "C-N-N",
    "RNN": "R-N-N",
    "LSTM": "L-S-T-M",
    "GRU": "G-R-U",
    "GNN": "G-N-N",
    "GCN": "G-C-N",
    "VAE": "V-A-E",
    "LLM": "L-L-M",
    "LLMs": "L-L-Ms",
    "GPT": "G-P-T",
    "NLP": "N-L-P",
    "API": "A-P-I",
    "GPU": "G-P-U",
    "TPU": "T-P-U",
    "CPU": "C-P-U",

    # Biological
    "DNA": "D-N-A",
    "RNA": "R-N-A",
    "mRNA": "messenger R-N-A",
    "tRNA": "transfer R-N-A",
    "rRNA": "ribosomal R-N-A",
    "miRNA": "micro R-N-A",
    "lncRNA": "long non-coding R-N-A",
    "ncRNA": "non-coding R-N-A",
    "UTR": "U-T-R",
    "ORF": "O-R-F",
    "CDS": "C-D-S",
    "TSS": "T-S-S",
    "TTS": "T-T-S",
    "TF": "T-F",
    "TFs": "T-Fs",
    "TAD": "T-A-D",
    "TADs": "T-A-Ds",
    "CTCF": "C-T-C-F",
    "MHC": "M-H-C",
    "HLA": "H-L-A",
    "TCR": "T-C-R",
    "BCR": "B-C-R",
}

# =============================================================================
# MODEL NAMES - Careful pronunciation
# =============================================================================

MODEL_NAMES = {
    # DNA Models
    "DNABERT": "D-N-A-bert",
    "DNABERT-2": "D-N-A-bert 2",
    "DNABERT2": "D-N-A-bert 2",
    "HyenaDNA": "hyena D-N-A",
    "Caduceus": "ca-doo-see-us",
    "GPN-MSA": "G-P-N M-S-A",
    "Nucleotide Transformer": "nucleotide transformer",

    # Protein Models
    "ESM": "E-S-M",
    "ESM-1b": "E-S-M 1-B",
    "ESM-1v": "E-S-M 1-V",
    "ESM-2": "E-S-M 2",
    "ESM-3": "E-S-M 3",
    "ESM2": "E-S-M 2",
    "ESM3": "E-S-M 3",
    "ESMFold": "E-S-M fold",
    "ProtBERT": "prot-bert",
    "ProtTrans": "prot-trans",
    "ProtXLNet": "prot X-L-net",
    "AlphaFold": "alpha-fold",
    "AlphaFold2": "alpha-fold 2",
    "AlphaFold3": "alpha-fold 3",
    "AlphaMissense": "alpha-missense",
    "AlphaGenome": "alpha-genome",
    "OpenFold": "open-fold",
    "OmegaFold": "omega-fold",
    "RoseTTAFold": "rose-T-T-A-fold",
    "EVE": "E-V-E",
    "popEVE": "pop E-V-E",

    # Regulatory Models
    "DeepSEA": "deep-sea",
    "Basset": "bass-et",
    "Beluga": "beluga",
    "Enformer": "en-former",
    "Borzoi": "bor-zoy",
    "Sei": "say",
    "DanQ": "dan-Q",
    "SpliceAI": "splice A-I",
    "Basenji": "ba-sen-jee",
    "Basenji2": "ba-sen-jee 2",

    # RNA Models
    "RNA-FM": "R-N-A F-M",
    "SPOT-RNA": "spot R-N-A",
    "CodonBERT": "codon-bert",
    "cdsFM": "C-D-S F-M",

    # Variant Effect Predictors
    "SIFT": "sift",
    "PolyPhen": "poly-fen",
    "PolyPhen-2": "poly-fen 2",
    "REVEL": "revel",
    "CADD": "cad",
    "M-CAP": "M-cap",
    "PROVEAN": "pro-veen",
    "FATHMM": "fath-um",
    "MutationAssessor": "mutation assessor",
    "PrimateAI": "primate A-I",

    # PRS Methods
    "LDpred": "L-D-pred",
    "LDpred2": "L-D-pred 2",
    "PRS-CS": "P-R-S C-S",
    "SBayesR": "S-bayes-R",
    "PRSice": "precise",
    "PRSice-2": "precise 2",

    # Interpretation
    "TF-MoDISco": "T-F mo-disco",
    "BPNet": "B-P-net",
    "SHAP": "shap",
    "LIME": "lime",
    "GradCAM": "grad-cam",

    # General ML
    "BERT": "bert",
    "XLNet": "X-L-net",
    "RoBERTa": "ro-berta",
    "T5": "T-5",
    "GPT-2": "G-P-T 2",
    "GPT-3": "G-P-T 3",
    "GPT-4": "G-P-T 4",
    "Mamba": "mamba",
    "Hyena": "hyena",
    "FlashAttention": "flash attention",
    "LoRA": "low-rah",
    "QLoRA": "Q-low-rah",

    # Architecture Components
    "RoPE": "rope",
    "Evoformer": "evo-former",
    "BPE": "B-P-E",
    "SentencePiece": "sentence-piece",
}

# =============================================================================
# GENE NAMES - Common genes mentioned in the book
# =============================================================================

GENE_NAMES = {
    "TP53": "T-P-53",
    "BRCA1": "braca-1",
    "BRCA2": "braca-2",
    "CFTR": "C-F-T-R",
    "HTT": "H-T-T",
    "APP": "A-P-P",
    "SOD1": "S-O-D-1",
    "LRRK2": "L-R-R-K-2",
    "APOE": "A-P-O-E",
    "MYC": "mick",
    "EGFR": "E-G-F-R",
    "KRAS": "K-ras",
    "BRAF": "B-raf",
    "BCL2": "B-C-L-2",
    "CASP3": "caspase-3",
    "STK11": "S-T-K-11",
    "LKB1": "L-K-B-1",
    "PIK3CA": "P-I-K-3-C-A",
    "PTEN": "P-ten",
    "RB1": "R-B-1",
    "NF1": "N-F-1",
    "DMD": "D-M-D",
    "FMR1": "F-M-R-1",
    "MECP2": "M-E-C-P-2",
    "SCN1A": "S-C-N-1-A",
    "KCNQ1": "K-C-N-Q-1",
    "GBA": "G-B-A",
    "HEXA": "hex-A",
    "PAH": "P-A-H",
    "CYP2D6": "sip-2-D-6",
    "CYP2C19": "sip-2-C-19",
    "TPMT": "T-P-M-T",
    "DPYD": "D-P-Y-D",
    "UGT1A1": "U-G-T-1-A-1",
}

# =============================================================================
# GREEK LETTERS - Expand to spoken form
# =============================================================================

GREEK_LETTERS = {
    "α": " alpha ",
    "β": " beta ",
    "γ": " gamma ",
    "δ": " delta ",
    "ε": " epsilon ",
    "ζ": " zeta ",
    "η": " eta ",
    "θ": " theta ",
    "λ": " lambda ",
    "μ": " mu ",
    "ν": " nu ",
    "π": " pi ",
    "ρ": " rho ",
    "σ": " sigma ",
    "τ": " tau ",
    "φ": " phi ",
    "χ": " chi ",
    "ψ": " psi ",
    "ω": " omega ",
    "Δ": " delta ",
    "Σ": " sigma ",
    "Ω": " omega ",
}

# =============================================================================
# TECHNICAL TERMS - Genomics jargon
# =============================================================================

TECHNICAL_TERMS = {
    # Directional
    "5'": "5-prime",
    "3'": "3-prime",
    "5′": "5-prime",
    "3′": "3-prime",

    # Scores and metrics
    "r²": "r-squared",
    "R²": "R-squared",
    "r2": "r-squared",
    "R2": "R-squared",
    "p-value": "p-value",
    "P-value": "p-value",
    "log2": "log-2",
    "log10": "log-10",
    "-log10": "negative log-10",
    "log-fold": "log-fold",
    "PHRED": "fred",
    "phred": "fred",

    # Constraint scores
    "pLI": "P-L-I",
    "pLoF": "P-lof",
    "LOEUF": "luff",
    "shet": "S-het",
    "phyloP": "phylo-P",
    "phastCons": "fast-cons",
    "GERP": "gerp",
    "GERP++": "gerp plus plus",

    # Variant types
    "indel": "in-del",
    "indels": "in-dels",
    "InDel": "in-del",
    "InDels": "in-dels",
    "SNP/indel": "snip or in-del",
    "LOF": "loss of function",
    "LoF": "loss of function",
    "GOF": "gain of function",
    "GoF": "gain of function",

    # Clinical
    "APOE ε4": "A-P-O-E epsilon-4",
    "APOEε4": "A-P-O-E epsilon-4",
    "APOE-ε4": "A-P-O-E epsilon-4",

    # Stats methods
    "C+T": "C plus T",
    "P+T": "P plus T",

    # K-mers
    "k-mer": "k-mer",
    "k-mers": "k-mers",
    "6-mer": "6-mer",
    "6-mers": "6-mers",
}

# =============================================================================
# SYMBOLS AND SPECIAL CHARACTERS
# =============================================================================

SYMBOLS = {
    "×": " times ",
    "±": " plus or minus ",
    "≈": " approximately ",
    "≥": " greater than or equal to ",
    "≤": " less than or equal to ",
    "→": " to ",
    "←": " from ",
    "↔": " bidirectional ",
    "∈": " in ",
    "∞": " infinity ",
    "√": " square root of ",
    "Σ": " sum of ",
    "∏": " product of ",
    "∂": " partial ",
    "∇": " gradient ",
    "⊗": " tensor product ",
}


def apply_pronunciations(text: str, verbose: bool = False) -> str:
    """Apply all pronunciation replacements to text.

    Args:
        text: Input text to process
        verbose: If True, print replacement counts

    Returns:
        Text with pronunciation-friendly replacements
    """
    counts = {}

    # Apply replacements in order of specificity (longer patterns first)
    all_replacements = {}
    all_replacements.update(GREEK_LETTERS)
    all_replacements.update(SYMBOLS)
    all_replacements.update(TECHNICAL_TERMS)
    all_replacements.update(GENE_NAMES)
    all_replacements.update(MODEL_NAMES)
    all_replacements.update(ACRONYMS)

    # Sort by length (longest first) to avoid partial replacements
    sorted_items = sorted(all_replacements.items(), key=lambda x: -len(x[0]))

    for original, replacement in sorted_items:
        # Use word boundaries for most replacements
        if len(original) > 1 and original[0].isalnum():
            pattern = r'\b' + re.escape(original) + r'\b'
        else:
            pattern = re.escape(original)

        matches = len(re.findall(pattern, text))
        if matches > 0:
            text = re.sub(pattern, replacement, text)
            counts[original] = matches

    if verbose and counts:
        print(f"Pronunciation replacements made: {len(counts)}")
        for term, count in sorted(counts.items(), key=lambda x: -x[1])[:20]:
            print(f"  {term}: {count}")

    return text


# =============================================================================
# INTEGRATION WITH TTS PIPELINE
# =============================================================================

def preprocess_with_pronunciations(text: str) -> str:
    """Wrapper for use in TTS pipeline.

    Call this AFTER the main preprocessing but BEFORE sending to TTS.
    """
    return apply_pronunciations(text)


if __name__ == "__main__":
    # Test with sample text
    test_text = """
    GWAS studies have identified SNPs associated with BRCA1 and TP53.
    The ESM-2 model achieved an AUROC of 0.95 on the ClinVar dataset.
    The 5' UTR region shows strong CTCF binding at TAD boundaries.
    AlphaFold2 predicts the structure with high confidence.
    The eQTL analysis used RNA-seq data from GTEx.
    """

    result = apply_pronunciations(test_text, verbose=True)
    print("\nOriginal:")
    print(test_text)
    print("\nWith pronunciations:")
    print(result)
