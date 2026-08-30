---
name: pro-slides
description: Create or upgrade high-end editable PowerPoint presentations with strong storytelling, polished visual design, scene-based motion, Morph choreography, object animation, and optional native 3D models. Use for competition decks, pitches, demos, technical presentations, product storytelling, keynote-style slides, or whenever the user asks for professional slides, cinematic transitions, Morph, smooth animation, 3D, or a visually impressive PPTX.
---

# Pro Slides

Create presentations that behave like designed visual stories rather than decorated documents.

The goal is not to maximize effects. The goal is to make the audience understand, remember, and feel the intended idea with as little visual friction as possible.

This skill is optimized for editable Microsoft PowerPoint (`.pptx`) output. It supports a cross-platform base-deck workflow and an optional Windows + desktop PowerPoint enhancement pass for native Morph, animation timelines, and embedded 3D models.

## Rule priority

Apply requirements in this order:

1. Explicit user instructions.
2. Supplied competition rules, brand guidelines, templates, slide masters, or example decks.
3. Existing deck language and visual system when editing a presentation.
4. This skill's defaults.

Never override a supplied requirement merely to match this skill.

## Core principle

Treat a presentation as a sequence of **scenes and states**, not a stack of independent pages.

A scene may span several physical PowerPoint slides:

```text
Scene: Product architecture

State A: product overview
   ↓ Morph
State B: zoom into controller
   ↓ reveal
State C: controller expands into architecture
   ↓ Morph
State D: data flow becomes visible
```

To the audience, these should feel like one continuous thought.

## Required workflow

### 1. Understand the presentation job

Before layout work, determine from the supplied context:

- audience
- decision or impression the deck must create
- presentation length or slide limit
- live presentation vs self-reading deck
- room/screen context when known
- available source material
- whether an existing template or brand system must be preserved
- whether native PowerPoint features such as Morph or 3D are requested

Do not ask for information that can be inferred safely from the user's materials. When something is unknown, use a reasonable default and keep moving unless the missing fact would fundamentally change the deck.

### 2. Build the story before styling

Write a compact story spine before constructing slides.

For competition and pitch decks, prefer a progression such as:

```text
Hook → Problem → Why current approaches fail → Insight → Solution →
How it works → Evidence → Differentiation → Impact → Ask / conclusion
```

Technical decks may instead use:

```text
Context → Requirement → Architecture → Critical mechanism →
Implementation → Results → Trade-offs → Next step
```

Do not force either sequence when the content calls for something else.

Every slide or state must have one primary job. If a slide has two unrelated conclusions, split it.

Read `references/storytelling-visual-design.md` before designing a substantial deck.

### 3. Plan scene rhythm and motion before building

For each slide/state, assign:

- narrative role
- visual focal point
- density: `anchor`, `breathing`, or `dense`
- motion level: `0` to `4`
- transition intent
- reveal order
- Morph relationships, if any
- 3D asset requirement, if any

Use the following motion hierarchy:

| Level | Meaning | Typical use |
| --- | --- | --- |
| 0 | Static | dense reference or supporting slide |
| 1 | Subtle | fade, appear, small emphasis |
| 2 | Narrative | controlled reveals or normal Morph |
| 3 | Hero | large spatial transformation or camera-like move |
| 4 | Showpiece | 3D, complex staged sequence, signature moment |

Level 3 and 4 motion should be rare. A deck where every slide is dramatic has no dramatic slides.

Read `references/motion-morph.md` before authoring animated sequences.

### 4. Build the editable base deck

Prefer native editable PowerPoint elements for:

- text
- simple shapes
- charts
- tables
- arrows/connectors
- diagrams that benefit from editing

SVG is appropriate for complex vectors and illustrations, but avoid turning every slide into one flattened SVG or raster image when the user wants editable PowerPoint and native Morph.

Use raster images only when raster content is inherently appropriate, such as photography, screenshots, rendered artwork, or generated imagery.

When using generated or external visuals, crop and compose them intentionally. Never use an image merely to fill empty space.

### 5. Establish object identity for scene continuity

Objects intended to persist across Morph states must have stable semantic identities.

Use PowerPoint's explicit Morph naming convention when native Morph will be applied:

```text
!!hero-product
!!controller
!!architecture-node-api
!!metric-revenue
```

The same `!!name` should appear at most once on a slide and should map 1:1 to the corresponding object on the next slide.

Do not use generic names such as `!!Shape1` unless the object truly has no semantic identity.

### 6. Author motion as choreography, not decoration

Use animation to answer one of these questions:

- What should the audience look at now?
- What changed?
- What caused what?
- Where did this object come from?
- How are these two states related?
- What should be remembered?

If an animation answers none of them, remove it.

Prefer:

- appear/fade for routine reveals
- wipe for directional flow
- Morph for spatial continuity and transformation
- zoom only when scale is semantically meaningful
- 3D rotation only when understanding the object benefits from another view

Avoid random motion, bouncing, spinning text, long decorative entrances, and multiple competing effects on the same beat.

### 7. Use native PowerPoint enhancement when available

Base deck generation should remain usable without Windows.

When the environment is Windows with desktop Microsoft PowerPoint installed, use the native enhancement path for requested advanced features:

```text
editable base PPTX
      ↓
motion manifest
      ↓
scripts/enhance_pptx.py
      ↓
PowerPoint COM automation
      ↓
Morph + native animations + 3D
```

Requirements for the helper script:

- Windows
- desktop Microsoft PowerPoint
- Python 3
- `pywin32`

Example:

```bash
pip install pywin32
python scripts/enhance_pptx.py deck.pptx motion.json --output deck-final.pptx
```

Read `references/native-powerpoint.md` before using the native enhancement path.

### 8. Treat 3D as a storytelling tool

Use a 3D model when the audience benefits from seeing:

- physical form
- orientation
- assembly
- component location
- spatial relationship
- product transformation

Do not add a 3D model merely because 3D looks expensive.

Prefer `.glb` assets for the PowerPoint-native workflow. Keep polygon count and texture size reasonable for presentation performance.

Read `references/3d-assets.md` when the deck uses 3D.

### 9. Render, inspect, and revise

A generated deck is not complete when code runs successfully.

Inspect every slide visually and inspect motion sequences as sequences.

Check at minimum:

- clipped or overflowing text
- text too small for projected viewing
- accidental misalignment
- poor contrast
- inconsistent margins
- weak hierarchy
- visual repetition that makes every slide feel identical
- excessive card-grid layouts
- incorrect Morph pairings
- objects that jump because identities changed
- animations that reveal in the wrong narration order
- transitions that are too slow
- missing 3D assets
- unsupported effects on the target PowerPoint version

Read `references/qa-delivery.md` before final delivery.

## Visual system defaults

Unless the user or template specifies otherwise:

- 16:9 widescreen
- strong whitespace
- few large elements rather than many small elements
- clear grid and alignment
- restrained palette
- one dominant accent color plus neutrals
- large display typography for key statements
- body text sized for live projection, not laptop reading
- no ornamental gradients, shadows, glass cards, or neon effects unless they support the selected visual direction

Avoid the common AI-slide pattern of placing all content into rounded cards. Use full-bleed composition, scale, diagrams, photography, whitespace, and asymmetric layouts where appropriate.

## Competition-deck rules

For short judged presentations:

- optimize for what judges can understand in a few seconds
- put the conclusion in the visual hierarchy, not only in speaker notes
- make the first 20 seconds visually intentional
- reserve at least one memorable hero sequence for the central insight or product
- make evidence legible at presentation distance
- use motion to clarify the mechanism or change in state
- keep backup/detail slides visually consistent but less theatrical

A showpiece transition cannot compensate for weak evidence, unclear claims, or unreadable content.

## Motion timing defaults

Use these as starting points, not rigid rules:

| Context | Transition | Object entrance | Stagger/delay |
| --- | ---: | ---: | ---: |
| Dense technical | 0.20–0.35 s | 0.25–0.40 s | 0.08–0.18 s |
| Normal narrative | 0.30–0.50 s | 0.35–0.55 s | 0.12–0.25 s |
| Hero concept | 0.45–0.80 s | 0.45–0.70 s | 0.18–0.35 s |
| Signature Morph | 0.60–1.20 s | as needed | minimal extra delay |

Avoid routine transitions above about 1 second. Long transitions consume presentation time and often feel slower than expected on stage.

## Deliverables

For a substantial deck, the final work should normally include:

- editable `.pptx`
- source code or generation files when applicable
- motion manifest when native enhancement was used
- required local assets
- brief note identifying any features that require desktop PowerPoint to play correctly

Do not claim Morph, object animation, or 3D was applied unless it actually exists in the delivered PPTX.

## Reference map

- `references/storytelling-visual-design.md` — narrative structure, layout, typography, competition design
- `references/motion-morph.md` — scene planning, Morph identity, choreography, pacing
- `references/native-powerpoint.md` — COM workflow and motion manifest
- `references/3d-assets.md` — model selection, insertion, camera and rotation
- `references/qa-delivery.md` — visual and motion QA
- `examples/motion-manifest.example.json` — example native enhancement manifest
- `scripts/enhance_pptx.py` — optional Windows + PowerPoint native enhancement helper
