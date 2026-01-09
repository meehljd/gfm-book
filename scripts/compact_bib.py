#!/usr/bin/env python3
"""Compact .bib file by removing unnecessary fields."""

import re
from pathlib import Path

# Fields to keep (essential for citations)
KEEP_FIELDS = {
    'title', 'author', 'year', 'journal', 'volume', 'number', 'pages',
    'publisher', 'booktitle', 'editor', 'edition', 'series',
    'doi', 'isbn', 'issn', 'month', 'howpublished', 'institution',
    'school', 'organization', 'address', 'chapter', 'type',
    'shorttitle',  # useful for long titles
}

# Fields to remove (verbose/unnecessary)
REMOVE_FIELDS = {
    'abstract', 'url', 'urldate', 'file', 'note', 'copyright',
    'language', 'keywords', 'annote', 'mendeley-tags', 'pmid',
    'pmcid', 'eprint', 'archiveprefix', 'primaryclass',
}

def parse_and_compact_bib(content: str) -> str:
    """Parse bib content and remove unnecessary fields."""
    result = []

    # Split into entries
    entries = re.split(r'(?=@\w+\s*\{)', content)

    for entry in entries:
        entry = entry.strip()
        if not entry or not entry.startswith('@'):
            continue

        # Extract entry type and key
        match = re.match(r'(@\w+\s*\{[^,]+,)', entry)
        if not match:
            result.append(entry)
            continue

        header = match.group(1)
        rest = entry[len(header):]

        # Parse fields - handle nested braces properly
        compacted_fields = []
        current_field = ""
        brace_depth = 0

        for char in rest:
            current_field += char
            if char == '{':
                brace_depth += 1
            elif char == '}':
                brace_depth -= 1
                if brace_depth < 0:
                    # End of entry
                    break
            elif char == ',' and brace_depth == 0:
                # End of field
                field_text = current_field.strip().rstrip(',')
                if field_text:
                    field_match = re.match(r'(\w+)\s*=', field_text)
                    if field_match:
                        field_name = field_match.group(1).lower()
                        if field_name in KEEP_FIELDS or field_name not in REMOVE_FIELDS:
                            compacted_fields.append(field_text)
                current_field = ""

        # Handle last field before closing brace
        if current_field.strip():
            field_text = current_field.strip().rstrip(',').rstrip('}').strip()
            if field_text:
                field_match = re.match(r'(\w+)\s*=', field_text)
                if field_match:
                    field_name = field_match.group(1).lower()
                    if field_name in KEEP_FIELDS or field_name not in REMOVE_FIELDS:
                        compacted_fields.append(field_text)

        # Rebuild entry
        if compacted_fields:
            compacted = header + "\n\t" + ",\n\t".join(compacted_fields) + ",\n}"
        else:
            compacted = header + "\n}"

        result.append(compacted)

    return "\n\n".join(result)


def main():
    bib_file = Path(__file__).parent.parent / 'bib' / 'references.bib'

    content = bib_file.read_text(encoding='utf-8')
    original_size = len(content)

    compacted = parse_and_compact_bib(content)
    new_size = len(compacted)

    bib_file.write_text(compacted, encoding='utf-8')

    reduction = (1 - new_size / original_size) * 100
    print(f"Original: {original_size:,} bytes")
    print(f"Compacted: {new_size:,} bytes")
    print(f"Reduction: {reduction:.1f}%")

if __name__ == '__main__':
    main()
