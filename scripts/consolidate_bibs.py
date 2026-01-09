#!/usr/bin/env python3
"""Consolidate all .bib files into a single sorted file."""

import re
from pathlib import Path

def parse_bib_entries(content: str) -> dict[str, str]:
    """Parse BibTeX content and return dict of key -> full entry."""
    entries = {}
    # Match @type{key, ... } entries (handling nested braces)
    pattern = r'(@\w+\s*\{[^,]+,)'

    # Split by entry starts
    parts = re.split(r'(?=@\w+\s*\{)', content)

    for part in parts:
        part = part.strip()
        if not part or not part.startswith('@'):
            continue

        # Extract the key
        key_match = re.match(r'@\w+\s*\{\s*([^,\s]+)', part)
        if key_match:
            key = key_match.group(1)
            entries[key] = part

    return entries

def main():
    bib_dir = Path(__file__).parent.parent / 'bib'

    # Collect all entries
    all_entries = {}

    # Find all .bib files
    bib_files = sorted(bib_dir.rglob('*.bib'))

    for bib_file in bib_files:
        content = bib_file.read_text(encoding='utf-8')
        entries = parse_bib_entries(content)

        for key, entry in entries.items():
            if key in all_entries:
                # Keep the entry but note duplicate
                print(f"Duplicate key '{key}' found in {bib_file.name}")
            else:
                all_entries[key] = entry

    # Sort by key (case-insensitive)
    sorted_keys = sorted(all_entries.keys(), key=str.lower)

    # Write consolidated file
    output_file = bib_dir / 'references.bib'
    with open(output_file, 'w', encoding='utf-8') as f:
        for i, key in enumerate(sorted_keys):
            if i > 0:
                f.write('\n\n')
            f.write(all_entries[key])

    print(f"\nConsolidated {len(all_entries)} entries from {len(bib_files)} files")
    print(f"Output: {output_file}")

if __name__ == '__main__':
    main()
