# GFM Book Project

A Quarto-based textbook on **Genomic Foundation Models** covering deep learning architectures for DNA, RNA, and protein sequence analysis.

## Book Structure

The book has **32 chapters** organized into **7 parts** plus appendices:

| Part | Title | Chapters | Focus |
|------|-------|----------|-------|
| 1 | Data Foundations | 1-4 | Sequencing, datasets, GWAS, classical VEP |
| 2 | Architectures | 5-7 | Representations, CNNs, attention mechanisms |
| 3 | Learning & Evaluation | 8-13 | Pretraining, transfer, adaptation, benchmarks, evaluation, confounding |
| 4 | Foundation Model Families | 14-18 | FM principles, DNA-LMs, protein-LMs, regulatory models, VEP |
| 5 | Cellular Context | 19-23 | RNA, single-cell, 3D genome, networks, multi-omics |
| 6 | Responsible Deployment | 24-27 | Uncertainty, interpretability, causality, regulation |
| 7 | Applications & Frontiers | 28-32 | Clinical risk, rare disease, drug discovery, design, frontiers |

## File Naming Conventions

```
part_N/pN-chXX-topic.qmd     # Chapter files (e.g., part_4/p4-ch15-dna-lm.qmd)
part_N/pN--partname.qmd      # Part intro files (double dash)
appendix/app-X-topic.qmd     # Appendix files
bib/pN/pN-chXX.bib           # Per-chapter bibliography files
```

**Cross-reference IDs** follow `sec-chXX-topic` pattern (see `_quarto.yml` comments).

## Directory Structure

```
/
├── part_1/ through part_7/  # Chapter content (.qmd files)
├── appendix/                # Appendices A-F
├── bib/                     # Bibliography files organized by part
│   ├── p1/ through p7/      # Per-chapter .bib files
│   ├── apx/                 # Appendix bibliographies
│   └── references.qmd       # References page
├── figs/                    # Figures organized by part/chapter
├── docs/                    # Rendered HTML output (git-tracked for GitHub Pages)
├── meta/                    # Project metadata and documentation
│   ├── qmd_headings.md      # Extracted headings from all chapters
│   ├── cross-reference-proposals.md
│   ├── papers-to-add.md     # Papers to potentially incorporate
│   ├── _instructions/       # Detailed writing instructions
│   ├── glossary/            # Glossary management files
│   ├── paper-reviews/       # Paper review notes
│   └── reports/             # Output from slash commands
├── scripts/                 # Utility scripts (see below)
├── TODO/                    # Planning documents
├── .claude/                 # Claude Code configuration
│   ├── commands/            # Slash command definitions
│   └── agents/              # Agent definitions
└── _quarto.yml              # Book configuration
```

## Scripts

### Extract Headers (`scripts/extract_headers.py`)
Regenerates `meta/qmd_headings.md` with all chapter headings:
```bash
python scripts/extract_headers.py
```

### Combine Book (`scripts/combine_quarto_book.py`)
Combines all chapters into a single file (useful for full-text analysis):
```bash
python scripts/combine_quarto_book.py combined.qmd
```

### Count Words (`scripts/count_book_words.sh`)
Counts words across all chapters with exclusion support:
```bash
./scripts/count_book_words.sh
```

### Watermark PNGs (`scripts/watermark_pngs.py`)
Adds watermarks to placeholder figures:
```bash
python scripts/watermark_pngs.py ./figs --inplace --text "PLACEHOLDER"
```

## Slash Commands

Run these for quality checks (output to `meta/reports/`):

| Command | Purpose | Example |
|---------|---------|---------|
| `/structure` | Analyze section structure and balance | `/structure` or `/structure p3-ch14` |
| `/glossary` | Check glossary term usage | `/glossary`, `/glossary coverage` |
| `/xref-check` | Validate cross-references | `/xref-check` or `/xref-check p3-ch14` |
| `/todos` | Organize TODOs and editing tasks | `/todos` or `/todos p3-ch14` |
| `/bib-audit` | Audit bibliography integrity | `/bib-audit` or `/bib-audit p3-ch14` |
| `/figures` | Inventory figures and placeholders | `/figures` or `/figures p3-ch14` |
| `/redundancy` | Find repeated content | `/redundancy` or `/redundancy ClinVar` |
| `/style-check` | Check style guide compliance | `/style-check` or `/style-check p3-ch14` |

## Agents

More complex review tools in `.claude/agents/`:

### Editorial Board (Orchestrator)

The `editorial-board` agent coordinates comprehensive reviews by dispatching specialized agents:

```bash
# Full review of a chapter using all agents
/editorial-board p3-ch14-dna-lm

# Review entire Part
/editorial-board part_3

# Book-wide assessment
/editorial-board

# Focus on content only (major members)
/editorial-board p3-ch14 --focus content

# Quick pass for status check
/editorial-board p3-ch14 --depth quick
```

**Major members:** `chapter-auditor`, `textbook-editor`, `pedagogy-review`, `course-designer`
**Minor members:** `fact-checker`, `figure-design`, `lean-out`

### Individual Agents

| Agent | Purpose |
|-------|---------|
| `chapter-auditor` | Structural audit: openings, soft landings, cross-chapter consistency, style rules (36 checks) |
| `textbook-editor` | Line editing, prose polish, publication readiness, market positioning |
| `pedagogy-review` | Learning science optimization (cognitive load, retrieval practice, spacing) |
| `course-designer` | Convert book into course materials: lectures, slides, exams, assignments, projects |
| `literature-critic` | Evaluate external papers/books for potential inclusion |
| `fact-checker` | Citation validation, claim verification, retraction/preprint audit |
| `figure-design` | Figure opportunities, specs, captions, critique |
| `lean-out` | Identify content with diminishing pedagogical returns for removal |
| `pre-commit` | Pre-commit content/style review |

### Chapter Auditor Agent

The `chapter-auditor` agent performs structural quality audits:

```bash
# Full audit of a chapter
/chapter-auditor p3-ch14-dna-lm

# Audit with cross-chapter context
/chapter-auditor p3-ch14-dna-lm --context p3-ch13,p3-ch15

# Audit in context of entire Part
/chapter-auditor p4-ch18-vep-fm --context part4
```

**36 checks** covering:
- **Openings**: Hook uniqueness, stakes, concrete specificity, no meta-commentary
- **Soft landings**: Three-beat structure, tension-based headings, forward connections
- **Style rules**: Em-dashes (zero tolerance), bullet points, gene/model formatting
- **Cross-chapter**: Terminology alignment, concept ordering, redundancy detection

**Note:** For prose polish (wordiness, passive voice, rhythm), use `textbook-editor` instead.

### Literature Critic Agent

The `literature-critic` agent evaluates papers for potential inclusion:

```bash
# Full evaluation of a paper
/literature-critic https://arxiv.org/abs/2306.15794

# Quick triage only
/literature-critic paper.pdf --mode triage

# Evaluate multiple papers
/literature-critic batch.txt --mode batch

# Check if citation supports claim
/literature-critic "DNABERT-2" --mode citation-check --chapter ch14
```

**Evaluation tiers:**
1. **Triage**: Scope fit, recency, venue quality
2. **Red flags**: Methodological issues, reporting problems
3. **Quality**: Reproducibility (0-3), validation rigor (0-3)
4. **Relevance**: Gap analysis, integration complexity
5. **Longevity**: Textbook test (will this matter in 2030?)

**Decisions:** INCLUDE / EXCLUDE / MONITOR

### Figure Design Agent

The `figure-design` agent specializes in visual communication:

```bash
# Full audit: opportunities + design + captions + AI prompts
/figure-design p3-ch14-dna-lm

# Just identify what needs figures
/figure-design p3-ch14-dna-lm --mode identify

# Generate AI prompts for placeholders
/figure-design p3-ch14-dna-lm --mode prompts

# Review/rewrite captions
/figure-design p3-ch14-dna-lm --mode captions
```

Generates prompts optimized for:
- **ChatGPT/DALL-E**: Scientific diagrams, conceptual illustrations
- **Fallback**: Manual creation descriptions

### Fact Checker Agent

The `fact-checker` agent validates citation integrity:

```bash
# Full audit: claims + citations + retractions + preprints
/fact-check p3-ch14-dna-lm

# Only find unsupported claims
/fact-check p3-ch14-dna-lm --mode claims

# Verify citations support their claims
/fact-check p3-ch14-dna-lm --mode verify

# Check for retracted papers
/fact-check p3-ch14-dna-lm --mode retractions

# Audit preprint status (find published versions)
/fact-check p3-ch14-dna-lm --mode preprints
```

Preprint policy:
- **ML preprints (arXiv cs/stat)**: Allowed (standard in the field)
- **Bio preprints (bioRxiv/medRxiv)**: Prefer peer-reviewed; flag if published version available

### Lean-Out Agent

The `lean-out` agent identifies content with diminishing pedagogical returns:

```bash
# Single chapter analysis
/lean-out p3-ch14-dna-lm

# Analyze entire Part
/lean-out part_3

# Book-wide analysis
/lean-out

# Focus on specific pattern
/lean-out p3-ch14 --mode lists-only
```

Key patterns detected:
- **Exhaustive lists**: Lists beyond 3-5 items with diminishing value
- **Redundant examples**: Multiple examples illustrating identical points
- **Historical tangents**: History that doesn't illuminate current practice
- **Appendix candidates**: Reference material better suited to appendices

**Realistic expectations:** Well-edited prose with cross-references yields 0.5-2% cuts, not 15-20%. The agent validates estimates by checking for existing cross-references and drafting replacement text before reporting savings.

### Course Designer Agent

The `course-designer` agent converts book content into comprehensive course materials:

```bash
# Full course materials for a chapter
/course-design p3-ch14-dna-lm

# Generate semester syllabus for the whole book
/course-design book --mode syllabus --format semester

# Create lecture notes for a chapter
/course-design p3-ch14-dna-lm --mode lecture

# Generate slide deck outline
/course-design p2-ch07-attention --mode slides

# Design exam/assessment
/course-design part_2 --mode exam

# Create homework assignments
/course-design p3-ch15-protein-lm --mode assignment --level graduate

# Design hands-on projects
/course-design part_3 --mode project

# Generate lab exercises
/course-design p2-ch10-adaptation --mode lab
```

**Modes available:**
- `full` - Complete course package (default)
- `syllabus` - Course schedule, objectives, policies
- `lecture` - Detailed teaching notes with timing
- `slides` - Slide deck structure with speaker notes
- `exam` - Quizzes, exams with rubrics and solutions
- `assignment` - Problem sets with scaffolded tasks
- `project` - Multi-week projects with milestones
- `discussion` - Seminar discussion questions
- `lab` - Guided coding tutorials

**Format options** (for syllabus): `semester`, `quarter`, `intensive`, `module`

**Level options**: `undergraduate`, `graduate`, `professional`, `mixed`

## Key Reference Files

| File | Purpose |
|------|---------|
| `meta/qmd_headings.md` | All chapter headings (regenerate with `extract_headers.py`) |
| `meta/_instructions/section_titles.md` | Canonical section titles |
| `meta/_instructions/ref-instructions.md` | Citation/reference guidelines |
| `meta/glossary/glossary-core-245.md` | Core glossary terms |
| `meta/papers-to-add.md` | Papers under consideration |
| `meta/cross-reference-proposals.md` | Cross-reference suggestions |
| `TODO/restructure-plan.md` | Restructuring documentation |

## Common Tasks

### After restructuring chapters
```bash
python scripts/extract_headers.py  # Update headings file
```

### Before editing a chapter
```bash
# Get chapter overview
/structure p3-ch14

# Check existing issues
/xref-check p3-ch14
/todos p3-ch14
```

### Quality review workflow
```bash
/style-check      # Style compliance
/glossary         # Term consistency
/bib-audit        # Citation integrity
/redundancy       # Content overlap
/figures          # Figure completeness
```

### Building the book
```bash
quarto preview    # Live preview
quarto render     # Full render to docs/
```

## Style Notes

- Use `@citation-key` for citations (keys defined in per-chapter .bib files)
- Cross-references: `@sec-chXX-topic` for sections, `@fig-name` for figures
- Math: Use `$...$` for inline, `$$...$$` for display
- Callouts: `:::{.callout-note}`, `:::{.callout-warning}`, etc.
- Figures: Place in `figs/part_N/chXX/` with descriptive names

## Important Notes

- The `docs/` directory is the rendered output for GitHub Pages - avoid editing directly
- Each chapter has its own `.bib` file in `bib/pN/`
- Reports from slash commands go to `meta/reports/` with date stamps
- When adding new chapters, update `_quarto.yml` and create corresponding `.bib` file
