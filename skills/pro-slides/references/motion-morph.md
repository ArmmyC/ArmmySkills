# Motion and Morph

Use this reference when a deck includes slide transitions, staged reveals, Morph, camera-like motion, or any scene spanning multiple physical slides.

## Motion has a job

Use motion to encode:

- continuity
- hierarchy
- sequence
- causality
- transformation
- change in scale
- change in focus

Do not use motion as proof of effort.

## Think in scenes and states

A `scene` is one audience thought. A `state` is one visual condition inside that scene.

Example:

```text
Scene: Why the architecture is simpler

State 1: legacy architecture, all modules visible
State 2: redundant modules dim
State 3: redundant modules collapse away
State 4: new architecture occupies the same space
State 5: key latency number appears
```

These may be five physical slides if Morph is used, but they should feel like one scene.

## Scene planning table

Before implementation, make a compact plan like:

| State | Narrative beat | Focal object | Motion | Level |
| --- | --- | --- | --- | ---: |
| A | establish system | full architecture | none | 0 |
| B | isolate bottleneck | queue | Morph zoom | 2 |
| C | show replacement | controller | Morph transform | 3 |
| D | prove result | latency metric | fade | 1 |

Do not choose effects before knowing the narrative beat.

## Morph object identity

PowerPoint can match objects automatically, but advanced sequences should establish explicit identity.

For objects that must map across consecutive slides, use the same unique name beginning with `!!`:

```text
!!hero-product
!!cpu-module
!!flow-packet
!!metric-42ms
```

PowerPoint's documented convention uses the `!!` prefix to force a 1:1 match between objects of the same type on successive slides.

### Naming rules

- Use semantic names.
- Keep a name unique within a slide.
- Reuse it only for the intended corresponding object on the next state.
- Do not assign one `!!name` to multiple objects on the same slide.
- Do not change identity halfway through a Morph sequence unless the visual concept actually changes identity.

### What should persist

Good persistent objects:

- hero product image or model
- highlighted architecture component
- diagram node followed across states
- one key metric or label
- recurring timeline marker

Bad persistent objects:

- every decorative line
- background texture
- unrelated text that happens to be in a similar location

## Morph strategies

### Spatial continuity

Move the same object to a new location while preserving identity.

Use for:

- diagram reorganization
- timeline progression
- moving a product from context into focus

### Camera-like zoom

Duplicate the scene, enlarge and reposition its major elements, then apply Morph.

Use this to simulate a camera moving into a detail.

Do not zoom so aggressively that viewers lose orientation. Keep at least one visual landmark when possible.

### Transformation

Match two same-type objects with the same `!!name` and change size, position, crop, or compatible geometry.

Use for:

- turning overview into detail
- simplifying a diagram
- changing a product or component state

### Recomposition

Morph a group of persistent objects into a cleaner arrangement while other elements fade out or appear.

This is effective for turning a complex problem diagram into the proposed solution without a hard scene cut.

## Morph by object, word, or character

Native PowerPoint exposes Morph modes for object, word, and character behavior.

Use object Morph by default.

Use word or character Morph only when typography itself is the story, for example:

- changing a key phrase
- revealing a naming transformation
- showing a before/after statement

Do not use character Morph for ordinary body copy.

## Transition timing

Starting points:

- routine transition: `0.25–0.45 s`
- normal Morph: `0.45–0.80 s`
- hero Morph: `0.70–1.20 s`

The right duration depends on travel distance, scene complexity, and presentation tempo.

Long-distance movement needs slightly more time than a small reposition. Complex transformations need enough time for the audience to perceive the relationship.

Do not make routine slide movement cinematic.

## In-slide reveals

A reveal should follow the speaker's explanation order.

Good sequence:

```text
title already visible
↓ click / auto
main mechanism appears
↓
input label appears
↓
output label appears
↓
result metric appears last
```

Bad sequence:

```text
five unrelated boxes fly in from different directions
```

### Preferred effects

Use these first:

- `appear` — fastest and least distracting
- `fade` — neutral reveal
- `wipe` — directional process or chart reveal
- `fly` — only when directional entry is meaningful
- `zoom` — when scale/focus is meaningful

Do not mix effect families without a reason.

## Trigger modes

Use:

- `on-click` when presenter control is important
- `with-previous` for simultaneous supporting elements
- `after-previous` for controlled automatic cascades

For a live competition deck, avoid long chains of automatic timing that make recovery difficult if the speaker pauses or judges interrupt.

## Stagger

Stagger helps the audience parse repeated elements, but large stagger values make a deck feel slow.

Practical defaults:

- dense repeated elements: `0.08–0.16 s`
- normal sequence: `0.12–0.25 s`
- hero sequence: `0.18–0.35 s`

If more than about five elements reveal one by one, reconsider whether they should be grouped conceptually.

## Motion hierarchy

Use level 0 through 4 intentionally.

### Level 0: Static

No motion except perhaps a neutral page transition.

### Level 1: Subtle

Fade/appear, minor emphasis, or one simple reveal.

### Level 2: Narrative

A controlled sequence or standard Morph supporting explanation.

### Level 3: Hero

A major scale change, recomposition, or camera-like Morph.

### Level 4: Showpiece

Native 3D, several coordinated states, or a signature transition central to the presentation.

A typical short competition deck should have few Level 3/4 moments.

## 3D + Morph choreography

A useful pattern for physical products:

```text
State A: model front view, small in context
   ↓ Morph
State B: model center, larger, slight rotation
   ↓ Morph
State C: model rotated to expose component
   ↓ reveal
State D: callout labels appear
```

The 3D rotation should expose information, not simply show that the model can spin.

## Diagram choreography

For process and architecture slides:

1. establish stable structure
2. highlight only the current path
3. reveal movement or causality
4. show result

Avoid animating every connector at once.

If a diagram is too complicated to animate clearly, simplify the diagram before adding motion.

## Data choreography

For charts:

- reveal axes/context first if needed
- reveal the relevant data series
- highlight the comparison
- show the conclusion annotation last

Do not animate every bar independently unless the sequence itself carries meaning.

## Text choreography

Text should normally be present when needed rather than theatrically animated.

Use motion for text when:

- a single key phrase changes meaning
- a result number is the payoff
- the audience must not read ahead

Do not animate paragraphs line by line in a short judged presentation unless disclosure order is essential.

## Failure modes

- no stable object identity, causing jumps instead of Morph
- using Morph between unrelated compositions
- objects moving just because they can
- transitions slower than the speaker's pace
- automatic sequences that cannot be interrupted naturally
- too many click steps
- animating decoration while the actual explanation remains static
- changing scale so much the audience loses spatial context
- using 3D rotation as a screensaver

## Motion test

Watch the sequence with audio muted.

You should still be able to infer:

- what changed
- what is important
- where to look next

Then present the sequence aloud. If motion forces the narration to wait for the slide, shorten the motion.
