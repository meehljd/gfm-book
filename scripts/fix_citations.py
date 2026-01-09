#!/usr/bin/env python3
"""Fix citation key mismatches in .qmd files."""

import re
from pathlib import Path

# Mapping of wrong keys to correct keys in references.bib
FIXES = {
    # Part 1
    "ingelman-sundberg_genetic_2005": "ingelman-sundberg_genetic_2004",
    "ahlqvist_t2d-clusters_2018": "ahlqvist_novel_2018",
    "auton_1kgp_2015": "auton_global_2015",
    "berman_pdb_2000": "berman_protein_2000",
    "birman-deych_icd_2005": "birman-deych_accuracy_2005",
    "edgar_geo_2002": "edgar_gene_2002",
    "gamazon_predixcan_2015": "gamazon_gene-based_2015",
    "gtex_2020": "gtex_consortium_the_gtex_2020",
    "gudbjartsson_decode_2015": "gudbjartsson_sequence_2015",
    "gusev_twas_2016": "gusev_integrative_2016",
    "kagda_encode_2025": "kagda_data_2025",
    "kundaje_roadmap_2015": "kundaje_integrative_2015",
    "lambert_pgs-catalog_2021": "lambert_polygenic_2021",
    "morales_mane_2022": "morales_joint_2022",
    "null_all-of-us_2019": "all_of_us_research_program_investigators_the_all_2019",
    "oleary_refseq_2016": "oleary_reference_2016",
    "regev_cell-atlas_2017": "regev_human_2017",
    "sirugo_diversity_2019": "sirugo_missing_2019",
    "sollis_gwas-catalog_2023": "sollis_nhgri-ebi_2023",
    "steinegger_bfd_2019": "steinegger_protein-level_2019",
    "stenson_hgmd_2017": "stenson_human_2017",
    "suzek_uniref_2015": "suzek_uniref_2007",
    "tabula_sapiens_2022": "tabula_sapiens_consortium_the_tabula_2022",
    "vosa_eqtl-gen_2021": "vosa_large-scale_2021",
    "whirl-PharmGKB_2012": "whirl-carrillo_pharmacogenomics_2012",

    # Part 1 ch03
    "khera_genome-wide_2017": "khera_genetics_2017",
    "lambert_polygenic_2019": "lambert_towards_2019",
    "price_pca_2006": "price_principal_2006",
    "yengo_meta-analysis_2022": "yengo_saturated_2022",

    # Part 1 ch04
    "adzhubei_polyphen_2010": "adzhubei_method_2010",
    "davydov_gerp_2010": "davydov_identifying_2010",
    "rentzsch_cadd-splice_2021": "rentzsch_cadd-spliceimproving_2021",

    # Part 2
    "cho_learning_2014": "cho_properties_2014",
    "yeo_maxentscan_2004": "yeo_maximum_2004",
    "dallatorre_nucleotide_2024": "dalla-torre_nucleotide_2023",
    "linder_borzoi_2023": "linder_borzoi_2025",
    "vaswani_attention_2017": "vaswani_attention_2023",
    "zhou_dnabert2_2024": "zhou_dnabert-2_2024",
    "raffel_t5_2019": "raffel_exploring_2023",

    # Part 3
    "gene42_2024": "vishniakov_gene42_2025",
    "oord_representation_2018": "oord_representation_2019",
    "yang_xlnet_2019": "yang_xlnet_2020",
    "zhang_understanding_2017": "zhang_understanding_2021",
    "zhou_dnabert-s_2024": "zhou_dnabert-s_2025",
    "kelley_cross-species_2020": "kelley_basenji2_2020",
    "rives_biological_2021": "rives_esm-1b_2021",
    "wang_characterizing_2019": "wang_characterizing_2018",
    "gaedigk_pharmacogene_2018": "gaedigk_pharmacogene_2017",
    "lin_focal_2017": "lin_focal_2020",
    "varoquaux_preventing_2021": "dockes_preventing_2021",
    "notin_proteingym_2024": "notin_proteingym_2023",
    "yan_traitgym_2024": "benegas_traitgym_2025",

    # Part 4
    "hoffmann_chinchilla_2022": "hoffmann_training_2022",
    "li_omnidna_2025": "li_omni-dna_2025",
    "gresova_genomic-benchmarks_2023": "gresova_genomic_2023",
    "dauparas_proteinmpnn_2022": "dauparas_robust_2022",
    "kulmanov_deepgo-se_2024": "kulmanov_protein_2024",
    "morcos_dca_2011": "morcos_direct-coupling_2011",
    "rives_esm_2021": "rives_esm-1b_2021",
    "watson_rfdiffusion_2023": "watson_novo_2023",
    "chen_sei_2022": "chen_sequence-based_2022",

    # Part 5
    "fudenberg_predicting_2020": "fudenberg_akita_2020",
    "lupiañez_disruptions_2015": "lupianez_disruptions_2015",
    "tan_corigami_2023": "tan_cell-type-specific_2023",
    "zhou_orca_2022": "zhou_sequence-based_2022",
    "cui_scgpt_2023": "cui_scgpt_2024",
    "theodoris_transfer_2023": "theodoris_geneformer_2023",

    # Part 6
    "acce_framework_2004": "center_for_disease_control_acce_2022",
    "eu_ai_act_2024": "european_parliament_regulation_2024",
    "eu_mdr_2017": "european_parliament_regulation_2017",
    "gdpr_2016": "european_parliament_regulation_2016",
    "gina_2008": "us_congress_genetic_2008",
    "fda_aiml_framework_2021": "us_food_and_drug_administration_artificial_2021",
    "fda_aiml_devices_2025": "food_and_drug_administration_artificial_2025",
    "fda_ldt_final_rule_2024": "food_and_drug_administration_laboratory_2024",
    "imdrf_samd_2014": "international_medical_device_regulators_forum_software_2014",
    "imdrf_samd_clinical_2017": "international_medical_device_regulators_forum_software_2017",
    "kaye_dynamic_2015": "kaye_dynamic_2014",
    "thaler_dabus_2021": "arnold_thaler_2021",
    "myriad_2013": "supreme_court_of_the_united_states_assoc_2013",

    # Part 7
    "nguengang_wakap_estimating_2020": "nguengang_wakap_estimating_2019",
    "deboer_deciphering_2020": "de_boer_deciphering_2019",
    "madani_progen_2023": "madani_large_2023",

    # Appendix D
    "abramson_accurate_2024": "abramson_alphafold3_2024",
    "baek_accurate_2021": "jumper_alphafold2_2021",  # or different paper
    "cheng_accurate_2023": "cheng_alphamissense_2023",
    "elnaggar_prottrans_2022": "elnaggar_prottrans_2021",
    "frazer_disease_2021": "frazer_eve_2021",
    "jumper_highly_2021": "jumper_alphafold2_2021",
    "lin_language_2023": "lin_esm-2_2022",
    "zhou_deep_2015": "zhou_deepsea_2015",

    # lin_evolutionary_2023 -> Could be lin_esm-2_2022
    "lin_evolutionary_2023": "lin_esm-2_2022",
}

def fix_citations_in_file(filepath: Path, fixes: dict) -> list:
    """Fix citations in a single file. Returns list of fixes made."""
    content = filepath.read_text(encoding='utf-8')
    original = content
    changes = []

    for wrong, correct in fixes.items():
        # Match @wrong_key patterns (citation references)
        pattern = rf'@{re.escape(wrong)}\b'
        if re.search(pattern, content):
            content = re.sub(pattern, f'@{correct}', content)
            changes.append((wrong, correct))

    if content != original:
        filepath.write_text(content, encoding='utf-8')

    return changes

def main():
    root = Path(__file__).parent.parent

    # Find all .qmd files
    qmd_files = list(root.glob('**/*.qmd'))
    qmd_files = [f for f in qmd_files if 'docs' not in str(f)]  # Exclude rendered output

    total_changes = 0
    for qmd_file in sorted(qmd_files):
        changes = fix_citations_in_file(qmd_file, FIXES)
        if changes:
            print(f"\n{qmd_file.relative_to(root)}:")
            for wrong, correct in changes:
                print(f"  {wrong} -> {correct}")
            total_changes += len(changes)

    print(f"\n\nTotal fixes: {total_changes}")

if __name__ == '__main__':
    main()
