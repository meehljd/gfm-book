# GFM Book Meta Directory

**Last organized:** 2026-01-21

Metadata, reports, and supporting materials for the "Genomic Foundation Models" textbook.

---

## Directory Structure

```
meta/
├── README.md                 # This file
├── qmd_headings.md           # Extracted chapter headings (auto-generated)
├── todos.md                  # Active TODO tracking
│
├── content/                  # Content domain materials
│   ├── glossary/             # Term definitions and audits
│   ├── figures/              # Figure inventory, style guide, critiques
│   ├── citations/            # Citation tracking and gap analysis
│   └── pedagogy/             # Learning science reviews
│
├── edits/                    # Editing workflow outputs
│   ├── line-edits/           # Per-chapter prose editing
│   ├── fact-checking/        # Verification and hallucination checks
│   ├── structure/            # Style, cross-refs, section titles
│   └── epistemic/            # Certainty calibration reviews
│
├── integration/              # External content integration
│   ├── editorial-workflow/   # Active paper additions (2025 papers)
│   ├── kb-integration/       # Knowledge base mapping
│   └── literature/           # Paper reviews and PDFs
│
├── publishing/               # Publication preparation
│
└── _archive/                 # Stale/superseded files
    └── old-instructions/     # Pre-Claude Code instructions (now in agents)
```

---

## What Moved Where

### Style Guides → Agents
Writing style rules are now in `/root/.claude/agents/book/`:
- `chapter-auditor/style-rules.md` - Typography, forbidden patterns
- `chapter-auditor/soft-landings.md` - Chapter endings
- `textbook-editor/AGENT.md` - Line editing standards

### Figure Style → Content Domain
- `content/figures/figure-style-guide.md` - Color palette, typography, sizing

### Section References → Edits/Structure
- `edits/structure/section_titles.md` - Canonical section titles
- `edits/structure/section-key-proposals.md` - Cross-reference IDs

---

## Key Files by Domain

| Domain | Key File | Purpose |
|--------|----------|---------|
| **Glossary** | `content/glossary/glossary-core-245.md` | Canonical 245 terms |
| **Figures** | `content/figures/figure-style-guide.md` | Color/typography spec |
| **Citations** | `content/citations/gap-analysis-*.md` | Missing citations |
| **Pedagogy** | `content/pedagogy/pedagogy-*.md` | Learning science audits |
| **Line Edits** | `edits/line-edits/line-edit-pX-chYY-*.md` | Per-chapter edits |
| **Structure** | `edits/structure/section_titles.md` | Section ID reference |
| **Integration** | `integration/editorial-workflow/*.md` | Current paper work |

---

## File Counts

| Folder | Files |
|--------|-------|
| content/glossary/ | 3 |
| content/figures/ | 10 |
| content/citations/ | 13 |
| content/pedagogy/ | 18 |
| edits/line-edits/ | 33 |
| edits/fact-checking/ | 11 |
| edits/structure/ | 15 |
| integration/editorial-workflow/ | 5 |
| integration/kb-integration/ | 8 |
| integration/literature/ | 2 |
| publishing/ | 5 |
| **Total** | **~123** |

---

## Slash Commands → Output Locations

| Command | Output |
|---------|--------|
| `/structure` | `edits/structure/` |
| `/glossary` | `content/glossary/` |
| `/figures` | `content/figures/` |
| `/bib-audit` | `content/citations/` |
| `/style-check` | `edits/structure/` |
