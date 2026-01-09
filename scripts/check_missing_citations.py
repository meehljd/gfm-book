#!/usr/bin/env python3
"""Check for citations in .qmd files that are missing from references.bib."""

import re
from pathlib import Path
from collections import defaultdict

def get_bib_keys(bib_file: Path) -> set:
    """Extract all citation keys from a .bib file."""
    content = bib_file.read_text(encoding='utf-8')
    keys = set()
    for match in re.finditer(r'^@\w+\s*\{\s*([^,\s]+)', content, re.MULTILINE):
        keys.add(match.group(1))
    return keys

def get_citations_in_file(qmd_file: Path) -> set:
    """Extract all @citation references from a .qmd file."""
    content = qmd_file.read_text(encoding='utf-8')
    # Match @citation_key patterns (excluding @fig-, @sec-, @tbl-, @eq-, @lst-)
    citations = set()
    for match in re.finditer(r'@([a-zA-Z][a-zA-Z0-9_-]+)', content):
        key = match.group(1)
        # Skip cross-references
        if not key.startswith(('fig-', 'sec-', 'tbl-', 'eq-', 'lst-', 'thm-', 'lem-', 'cor-', 'prp-', 'cnj-', 'def-', 'exm-', 'exr-')):
            citations.add(key)
    return citations

def main():
    root = Path(__file__).parent.parent
    bib_file = root / 'bib' / 'references.bib'

    # Get all known citation keys
    bib_keys = get_bib_keys(bib_file)
    print(f"Found {len(bib_keys)} keys in references.bib\n")

    # Find all .qmd files (excluding docs/)
    qmd_files = [f for f in root.glob('**/*.qmd') if 'docs' not in str(f)]

    # Track missing citations by file
    missing_by_file = defaultdict(set)
    all_missing = set()

    for qmd_file in sorted(qmd_files):
        citations = get_citations_in_file(qmd_file)
        missing = citations - bib_keys
        if missing:
            rel_path = qmd_file.relative_to(root)
            missing_by_file[str(rel_path)] = missing
            all_missing.update(missing)

    # Print results
    if missing_by_file:
        print("Missing citations by file:\n")
        for filepath, missing in sorted(missing_by_file.items()):
            print(f"{filepath}:")
            for key in sorted(missing):
                print(f"  - {key}")
            print()

        print(f"\n{'='*60}")
        print(f"SUMMARY: {len(all_missing)} unique missing citations\n")
        for key in sorted(all_missing):
            print(f"  {key}")
    else:
        print("No missing citations found!")

if __name__ == '__main__':
    main()
