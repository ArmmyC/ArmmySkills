# Storytelling and Visual Design

Use this reference for substantial decks, especially competition, pitch, demo, and technical storytelling.

## Start from the audience's decision

A presentation is not a document split into slides. It is a timed sequence that changes what the audience knows or believes.

Before designing, identify:

- what the audience already knows
- what they misunderstand or do not know
- what they need to believe by the end
- what evidence makes that belief credible
- what the presenter needs them to remember one hour later

The deck should spend the most visual energy on the steps that move the audience between those states.

## One primary message per state

Each slide or Morph state should have one dominant sentence that could complete:

> After this state, the audience should understand that ...

If that sentence contains `and` joining unrelated claims, the slide probably needs to split.

A slide may contain multiple supporting elements, but they should all serve the same conclusion.

## Recommended story patterns

### Competition / pitch

```text
1. Hook
2. Problem in concrete terms
3. Why the problem matters
4. Why existing approaches are insufficient
5. Key insight
6. Solution
7. How it works
8. Proof / result
9. Differentiation
10. Impact
11. Closing claim / ask
```

### Product demo

```text
1. User situation
2. Friction
3. Product promise
4. Product in context
5. Critical workflow
6. Mechanism or architecture
7. Result
8. Why it is defensible
9. Next step
```

### Technical presentation

```text
1. Requirement
2. Constraints
3. Architecture
4. Critical mechanism
5. Implementation
6. Measurement
7. Result
8. Failure modes / trade-offs
9. Recommendation
```

Use these as scaffolds only. Do not preserve steps that add no value.

## Slide roles

Assign each slide one of these roles during planning:

- `hook` — create curiosity or frame stakes
- `claim` — state an important conclusion
- `evidence` — prove a claim
- `mechanism` — explain how something works
- `comparison` — establish difference
- `transition` — move between sections or mental models
- `demo` — show product behavior
- `summary` — compress previous information
- `ask` — state next action or final judgment

The role should influence the layout. A claim slide should not look identical to an evidence slide.

## Density rhythm

Use three density classes:

### Anchor

A high-importance slide with low information density and large visual hierarchy.

Typical examples:

- opening hook
- key insight
- major result
- final takeaway

### Breathing

A normal explanatory slide with enough whitespace to guide attention.

Typical examples:

- product flow
- architecture overview
- comparison
- mechanism

### Dense

A slide containing necessary detail, usually data or technical structure.

Typical examples:

- benchmark table
- implementation details
- test matrix
- backup slide

Do not let the deck become uniformly dense or uniformly sparse. Rhythm creates perceived quality.

## Visual hierarchy

A viewer should know where to look within roughly one second.

Prefer hierarchy through:

1. scale
2. position
3. contrast
4. whitespace
5. weight
6. color

Use decoration only after these are working.

A strong hierarchy might be:

```text
large conclusion
      ↓
hero visual / number
      ↓
small supporting explanation
```

Avoid giving title, chart, callout, icon, and body copy equal weight.

## Typography

For live presentation:

- use large type aggressively
- prefer short declarative headlines
- avoid paragraphs when a diagram, comparison, or speaker narration can carry the detail
- use sentence case unless the visual system clearly calls for another convention
- keep line lengths short
- use no more font families than necessary

Body text that works on a laptop may fail on a projector. Inspect the slide at thumbnail size and at realistic viewing distance.

### Headline behavior

Weak:

```text
Our Solution
```

Stronger:

```text
One controller replaces three manual handoffs
```

Prefer a conclusion headline when the slide contains evidence for that conclusion.

## Layout

Build with a grid, even when the result is asymmetric.

Keep:

- consistent outer margins
- deliberate alignment anchors
- predictable spacing increments
- stable title zones when repeated

Break the grid intentionally for hero moments, not accidentally.

### Avoid card-grid defaulting

Do not automatically put every idea in a rounded rectangle.

Cards are useful when the content represents independent peer items. They are poor defaults for:

- process
- hierarchy
- causality
- spatial systems
- product views
- narrative claims

Prefer diagrams, scale changes, arrows, direct labels, whitespace, and composition when those better represent the content.

## Color

Use color to encode meaning or focus.

A practical default:

- neutral background
- neutral text
- one primary accent
- optional semantic colors for success/warning/error/data categories

Do not use five accent colors simply to make the deck feel energetic.

For dark decks, check that thin lines, secondary text, and data labels survive projectors with poor black levels.

## Images and renders

Images should do one of four jobs:

- establish context
- show the product
- explain a physical/spatial idea
- create emotional or visual emphasis

Crop images to support composition. Do not preserve an image's original aspect ratio if the composition needs a crop, unless important content would be lost.

Do not use decorative stock imagery behind dense text.

## Charts

A chart should answer a question.

Before drawing one, define the intended takeaway. Then remove everything that does not support it.

Prefer:

- direct labels over legends when practical
- highlighting the relevant series
- annotations for the actual conclusion
- consistent scales across comparisons
- honest axes and baselines

Avoid turning raw spreadsheet output into a slide without redesign.

## Diagrams

A diagram should expose structure, sequence, or relationship.

Use labels close to their objects. Keep connector paths clean. Avoid crossing lines. Use motion only when it helps explain sequence or causality.

For architecture diagrams, reveal by conceptual layer rather than animating every box individually.

## Competition decks

Judged presentations create specific constraints:

- attention is scarce
- judges may be reading while the presenter speaks
- timing is strict
- memorable visual moments matter
- evidence still matters more than spectacle

### Recommended visual pacing

In a 5 to 10 minute deck, aim for a small number of memorable moments rather than continuous effects.

Typical pattern:

```text
Opening anchor
Normal explanation
Normal explanation
Hero insight
Technical support
Showpiece mechanism / product
Evidence
Closing anchor
```

### Make judging easier

If judging criteria are known, make it easy for a judge to map the deck to them. Do not force them to infer where feasibility, novelty, impact, validation, or business value was addressed.

## Common failure modes

- every slide uses the same template
- the title repeats what the body already says
- all important information is small
- gradients and glow are used instead of hierarchy
- motion is added after the deck without narrative purpose
- diagrams are too detailed to understand live
- screenshots are pasted without cropping or annotation
- the deck contains more visual styles than ideas
- the best visual appears on an unimportant slide
- closing slide is a generic `Thank you` instead of the final argument

## Final design test

For every slide, ask:

1. What is the single most important thing here?
2. Can I see it immediately?
3. Is every element supporting it?
4. Would this still work from the back of a room?
5. Does this slide look different because its role is different, or merely because styling drifted?
