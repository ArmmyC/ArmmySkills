# ArmmySkills

A small collection of reusable Agent Skills I use with Codex and other compatible coding agents.

## Skills

### `thai-academic-docx`

Formats and generates Microsoft Word (`.docx`) documents using practical conventions for Thai university coursework.

Designed for homework, assignments, lab reports, engineering reports, project reports, short academic write-ups, and Thai documents containing English technical terms, equations, tables, figures, and references.

The skill covers A4 layout, TH Sarabun New typography, Thai paragraph alignment and indentation, heading hierarchy, native lists and numbering, tables, figures, equations, pagination, mixed Thai/English text, and DOCX/OpenXML construction rules.

Explicit instructor, course, faculty, university, or supplied template requirements always take priority over the skill defaults.

### `pro-slides`

Creates and upgrades professional editable PowerPoint presentations with a stronger focus on presentation storytelling and motion design.

Designed for:

- competition decks
- startup and product pitches
- technical presentations
- demos
- project showcases
- keynote-style presentations
- decks that need cinematic scene continuity rather than static page-by-page design

The skill covers:

- story architecture and slide roles
- visual hierarchy, typography, grid, density, diagrams, charts, and imagery
- scene-based presentation planning
- motion hierarchy and timing
- native PowerPoint Morph choreography using stable `!!` object identities
- staged object animation
- optional native 3D model insertion, rotation, and camera control
- competition-specific pacing
- slideshow, editability, and stage-readiness QA

The base deck can be generated cross-platform. Advanced native PowerPoint enhancement uses `skills/pro-slides/scripts/enhance_pptx.py` and requires Windows, desktop Microsoft PowerPoint, and `pywin32`.

## Install

### Discover available skills

```bash
npx skills add ArmmyC/ArmmySkills --list
```

### Install `thai-academic-docx`

```bash
npx skills add ArmmyC/ArmmySkills \
  --skill thai-academic-docx \
  --agent codex \
  --global
```

### Install `pro-slides`

```bash
npx skills add ArmmyC/ArmmySkills \
  --skill pro-slides \
  --agent codex \
  --global
```

For a non-interactive install, add `--yes`.

## Repository structure

```text
ArmmySkills/
├── README.md
└── skills/
    ├── thai-academic-docx/
    │   └── SKILL.md
    └── pro-slides/
        ├── SKILL.md
        ├── examples/
        │   └── motion-manifest.example.json
        ├── references/
        │   ├── 3d-assets.md
        │   ├── motion-morph.md
        │   ├── native-powerpoint.md
        │   ├── qa-delivery.md
        │   └── storytelling-visual-design.md
        └── scripts/
            └── enhance_pptx.py
```

Each skill lives in its own directory under `skills/` and uses `SKILL.md` as its entry point.

## Usage

### Thai academic DOCX

```text
Create a DOCX report from these notes and use the Thai academic DOCX formatting skill.
```

or:

```text
Format this report.docx as a normal Thai university coursework report.
```

### Professional slides

```text
Turn this project into a 7-minute competition deck using the pro-slides skill. Make it editable, visually strong, and use Morph only where it improves the story.
```

or:

```text
Upgrade this PPTX into a professional technical presentation. Keep the content accurate, redesign weak slides, and create one memorable Morph sequence for the architecture explanation.
```

For native PowerPoint motion and 3D enhancement on Windows:

```bash
pip install pywin32
python skills/pro-slides/scripts/enhance_pptx.py \
  presentation.pptx \
  motion.json \
  --output presentation-final.pptx
```

See `skills/pro-slides/examples/motion-manifest.example.json` for the manifest format.

## Skill sources

- [`skills/thai-academic-docx/SKILL.md`](skills/thai-academic-docx/SKILL.md)
- [`skills/pro-slides/SKILL.md`](skills/pro-slides/SKILL.md)

## License

No license has been specified yet.
