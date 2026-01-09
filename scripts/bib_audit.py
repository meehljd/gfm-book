#!/usr/bin/env python3
"""
Bibliography Audit Script
Finds and removes orphaned citations from chapter .bib files.
"""

import re
from pathlib import Path
from collections import defaultdict

def extract_citations_from_qmd(qmd_path):
    """Extract all citation keys from a .qmd file."""
    with open(qmd_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match @citation-key
    # Exclude @sec-, @fig-, @tbl-, @eq- (cross-references)
    # Exclude email patterns (word@word)
    citations = set()

    # Find all @ patterns
    pattern = r'@([a-zA-Z][a-zA-Z0-9_:-]*)'

    for match in re.finditer(pattern, content):
        key = match.group(1)
        # Skip cross-references and common prefixes
        if key.startswith(('sec-', 'fig-', 'tbl-', 'eq-', 'lst-', 'thm-', 'lem-', 'cor-', 'prp-', 'cnj-', 'def-', 'exm-', 'exr-')):
            continue
        # Skip if it looks like an email (preceded by a word character)
        start = match.start()
        if start > 0 and content[start-1].isalnum():
            continue
        citations.add(key)

    return citations

def parse_bib_entries(bib_path):
    """Parse a .bib file and return a dict of {key: full_entry_text}."""
    if not bib_path.exists():
        return {}

    with open(bib_path, 'r', encoding='utf-8') as f:
        content = f.read()

    entries = {}
    # Match BibTeX entries: @type{key, ... }
    # Need to handle nested braces properly

    entry_pattern = r'@(\w+)\s*\{\s*([^,\s]+)\s*,'

    for match in re.finditer(entry_pattern, content):
        entry_type = match.group(1).lower()
        key = match.group(2)

        # Skip comments
        if entry_type == 'comment':
            continue

        # Find the full entry by counting braces
        start = match.start()
        brace_count = 0
        end = start
        in_entry = False

        for i, char in enumerate(content[start:], start):
            if char == '{':
                brace_count += 1
                in_entry = True
            elif char == '}':
                brace_count -= 1
                if in_entry and brace_count == 0:
                    end = i + 1
                    break

        entry_text = content[start:end]
        entries[key] = entry_text

    return entries

def get_chapter_bib_mapping():
    """Build mapping of chapter files to their corresponding bib files."""
    mapping = []
    base = Path('/root/gfm_book')

    # Process parts 1-7
    for part_num in range(1, 8):
        part_dir = base / f'part_{part_num}'
        bib_dir = base / 'bib' / f'p{part_num}'

        if part_dir.exists():
            for qmd_file in sorted(part_dir.glob(f'p{part_num}-ch*.qmd')):
                # Extract chapter number from filename like p1-ch04-topic.qmd
                match = re.match(r'p\d+-ch(\d+)', qmd_file.stem)
                if match:
                    ch_num = match.group(1)
                    bib_file = bib_dir / f'p{part_num}-ch{ch_num}.bib'
                    mapping.append((qmd_file, bib_file))

    # Process appendices
    appendix_dir = base / 'appendix'
    apx_bib_dir = base / 'bib' / 'apx'

    if appendix_dir.exists():
        for qmd_file in sorted(appendix_dir.glob('app-*.qmd')):
            # Extract appendix letter from filename like app-a-topic.qmd
            match = re.match(r'app-([a-z])', qmd_file.stem)
            if match:
                apx_letter = match.group(1)
                bib_file = apx_bib_dir / f'app-{apx_letter}.bib'
                mapping.append((qmd_file, bib_file))

    return mapping

def clean_bib_file(bib_path, entries_to_keep):
    """Rewrite a .bib file keeping only specified entries."""
    if not bib_path.exists():
        return

    entries = parse_bib_entries(bib_path)

    # Build new content with only kept entries
    kept_entries = []
    for key in sorted(entries_to_keep):
        if key in entries:
            kept_entries.append(entries[key])

    # Write back
    with open(bib_path, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(kept_entries))
        if kept_entries:
            f.write('\n')

def main():
    """Main audit function."""
    mapping = get_chapter_bib_mapping()

    report = []
    report.append("# Bibliography Audit Report")
    report.append("")

    total_bib_files = 0
    total_citations_removed = 0
    total_citations_kept = 0
    issues = []
    chapter_details = []

    for qmd_path, bib_path in mapping:
        chapter_name = qmd_path.stem

        # Extract citations from chapter
        try:
            used_citations = extract_citations_from_qmd(qmd_path)
        except Exception as e:
            issues.append(f"Error reading {qmd_path}: {e}")
            continue

        # Parse bib entries
        if not bib_path.exists():
            issues.append(f"Missing bib file: {bib_path}")
            continue

        total_bib_files += 1

        try:
            bib_entries = parse_bib_entries(bib_path)
        except Exception as e:
            issues.append(f"Error parsing {bib_path}: {e}")
            continue

        defined_keys = set(bib_entries.keys())

        # Find orphaned entries (defined but not used)
        orphaned = defined_keys - used_citations
        kept = defined_keys & used_citations

        # Also find missing (used but not defined) - just for reporting
        missing = used_citations - defined_keys

        if orphaned:
            total_citations_removed += len(orphaned)
            total_citations_kept += len(kept)

            # Clean the bib file
            clean_bib_file(bib_path, kept)

            chapter_details.append({
                'chapter': chapter_name,
                'bib_file': str(bib_path.relative_to('/root/gfm_book')),
                'removed': sorted(orphaned),
                'kept': len(kept),
                'removed_count': len(orphaned)
            })
        else:
            total_citations_kept += len(kept)

        if missing:
            issues.append(f"{chapter_name}: {len(missing)} citations used but not defined: {', '.join(sorted(missing)[:5])}{'...' if len(missing) > 5 else ''}")

    # Build report
    report.append("## Summary")
    report.append("")
    report.append(f"- **Total bib files checked:** {total_bib_files}")
    report.append(f"- **Total citations removed:** {total_citations_removed}")
    report.append(f"- **Total citations kept:** {total_citations_kept}")
    report.append(f"- **Chapters with removals:** {len(chapter_details)}")
    report.append("")

    if chapter_details:
        report.append("## Per-Chapter Breakdown")
        report.append("")

        for detail in chapter_details:
            report.append(f"### {detail['chapter']}")
            report.append(f"**File:** `{detail['bib_file']}`")
            report.append(f"**Kept:** {detail['kept']} | **Removed:** {detail['removed_count']}")
            report.append("")
            report.append("Removed citations:")
            for key in detail['removed']:
                report.append(f"- `{key}`")
            report.append("")

    if issues:
        report.append("## Issues Encountered")
        report.append("")
        for issue in issues:
            report.append(f"- {issue}")
        report.append("")

    report_text = '\n'.join(report)
    print(report_text)

    # Save report
    report_path = Path('/root/gfm_book/meta/reports/bib-audit-cleanup.md')
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, 'w') as f:
        f.write(report_text)

    print(f"\nReport saved to: {report_path}")

if __name__ == '__main__':
    main()
