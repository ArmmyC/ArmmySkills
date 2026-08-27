# ArmmySkills

A small collection of reusable Agent Skills I use with Codex and other compatible coding agents.

## Skills

### `thai-academic-docx`

Formats and generates Microsoft Word (`.docx`) documents using practical conventions for Thai university coursework.

Designed for:

- homework and assignments
- class reports
- lab reports
- engineering reports
- project reports
- short academic write-ups
- Thai documents containing English technical terms, equations, tables, figures, and references

The skill provides an opinionated default for casual academic work, including:

- A4 page layout
- TH Sarabun New typography
- Thai paragraph alignment and indentation
- heading hierarchy
- paragraph spacing and tab stops
- bold, italic, and emphasis rules
- native Word lists and numbering
- tables and repeating table headers
- figures and captions
- native Word equations and equation numbering
- page breaks, pagination, and TOC behavior
- Thai/English mixed-text handling
- DOCX/OpenXML construction rules

Explicit instructor, course, faculty, university, or supplied template requirements always take priority over the defaults in this skill.

## Install

### Codex

Install the Thai academic DOCX skill globally:

```bash
npx skills add ArmmyC/ArmmySkills \
  --skill thai-academic-docx \
  --agent codex \
  --global
```

For a non-interactive install:

```bash
npx skills add ArmmyC/ArmmySkills \
  --skill thai-academic-docx \
  --agent codex \
  --global \
  --yes
```

### Discover available skills

```bash
npx skills add ArmmyC/ArmmySkills --list
```

## Repository structure

```text
ArmmySkills/
├── README.md
└── skills/
    └── thai-academic-docx/
        └── SKILL.md
```

Each skill lives in its own directory under `skills/` and uses `SKILL.md` as its entry point.

## Usage

Once installed, ask Codex to create or format a Thai academic Word document normally. For example:

```text
Create a DOCX report from these notes and use the Thai academic DOCX formatting skill.
```

or:

```text
Format this report.docx as a normal Thai university coursework report.
```

If you provide a course template or explicit formatting requirements, those should override the skill defaults.

## Skill source

See [`skills/thai-academic-docx/SKILL.md`](skills/thai-academic-docx/SKILL.md) for the complete formatting and document-construction rules.

## License

No license has been specified yet.
