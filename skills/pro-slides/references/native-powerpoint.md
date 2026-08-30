# Native PowerPoint Enhancement

This reference describes the optional second-stage enhancement workflow for native Microsoft PowerPoint features.

Use it only when Windows and desktop PowerPoint are available and the deck benefits from native Morph, native object animation, or embedded 3D.

## Why use a second stage

Cross-platform PPTX generation libraries are effective for editable layouts, text, shapes, charts, diagrams, and images. Native PowerPoint features such as Morph behavior, animation timelines, and 3D model objects are more reliably authored through PowerPoint itself.

The recommended architecture is:

```text
content + storyboard
      ↓
editable base deck
      ↓
motion manifest
      ↓
PowerPoint native enhancement
      ↓
render / slideshow QA
```

The base deck must remain usable even if the native enhancement stage cannot run.

## Requirements

- Windows
- desktop Microsoft PowerPoint
- Python 3
- `pywin32`

Install the Python dependency:

```bash
pip install pywin32
```

Run:

```bash
python scripts/enhance_pptx.py input.pptx motion.json --output output.pptx
```

Use `--validate-only` to check the manifest structure without opening PowerPoint.

## PowerPoint APIs used

The helper relies on native PowerPoint automation concepts including:

- `SlideShowTransition.EntryEffect`
- `SlideShowTransition.Duration`
- `TimeLine.MainSequence.AddEffect`
- `Effect.Timing.Duration`
- `Effect.Timing.TriggerType`
- `Effect.Timing.TriggerDelayTime`
- `Shapes.Add3DModel`
- `Shape.Model3D` rotation and camera properties

These are native Office object-model features, not simulated slide frames.

## Motion manifest

The manifest is JSON. Slide numbers are 1-based, matching PowerPoint.

Minimal example:

```json
{
  "version": 1,
  "slides": {
    "2": {
      "rename": {
        "Hero Product": "!!hero-product"
      },
      "transition": {
        "type": "morph",
        "mode": "object",
        "duration": 0.75
      }
    }
  }
}
```

A fuller example is in `examples/motion-manifest.example.json`.

## Shape naming

Manifest shape selectors use the current PowerPoint shape name.

When a generated deck is intended for native enhancement, give important objects deterministic names during base-deck generation whenever the library supports it.

Preferred examples:

```text
Hero Product
Architecture Controller
Metric Latency
Callout Sensor
```

Then the enhancement pass can rename Morph-persistent objects:

```json
"rename": {
  "Hero Product": "!!hero-product",
  "Architecture Controller": "!!controller"
}
```

PowerPoint's Morph matching convention requires the same `!!name` on corresponding objects in successive slides.

## Transitions

Native enhancement currently focuses on Morph because ordinary transitions can usually be authored in the base-generation stage.

Manifest form:

```json
"transition": {
  "type": "morph",
  "mode": "object",
  "duration": 0.8
}
```

Morph is applied to the **destination slide**. If slide 2 has a Morph transition, PowerPoint animates the change from slide 1 into slide 2. Therefore any forced `!!` object identity used by that transition must exist on both slide 1 and slide 2. The manifest may contain rename-only entries on source slides for this reason.

Supported Morph modes:

- `object`
- `word`
- `character`

Use `object` unless text transformation is explicitly part of the storytelling.

## Native animations

Animation entries target shapes by PowerPoint name.

Example:

```json
"animations": [
  {
    "shape": "Main Diagram",
    "effect": "fade",
    "trigger": "on-click",
    "duration": 0.4
  },
  {
    "shape": "Result Metric",
    "effect": "zoom",
    "trigger": "after-previous",
    "duration": 0.45,
    "delay": 0.12
  }
]
```

The helper intentionally supports a conservative effect set:

- `appear`
- `fade`
- `fly`
- `zoom`
- `wipe`

This is deliberate. A professional deck rarely benefits from exposing the full PowerPoint novelty-effect catalog.

Triggers:

- `on-click`
- `with-previous`
- `after-previous`

## Insert native 3D

Example:

```json
"insert3d": [
  {
    "file": "assets/robot.glb",
    "name": "!!robot",
    "left": 520,
    "top": 120,
    "width": 320,
    "height": 320,
    "rotation": {"x": 0, "y": 25, "z": 0}
  }
]
```

Coordinates and dimensions are PowerPoint points.

Relative asset paths are resolved from the manifest directory.

## Modify an existing 3D model

When a native 3D model already exists on the slide, use:

```json
"model3d": [
  {
    "shape": "!!robot",
    "rotation": {"x": 5, "y": 70, "z": 0},
    "field_of_view": 35
  }
]
```

This makes it practical to duplicate a slide and change the 3D view before applying Morph.

## Safe authoring sequence

For a Morph pair:

1. build slide A
2. duplicate or recreate slide B with the same intended persistent objects
3. preserve deterministic shape names
4. move/resize/rotate/crop objects on B
5. assign the same `!!` names on both slides
6. apply Morph to slide B
7. test in slideshow mode

Do not rely on visual similarity alone for important Morph pairings.

## Editing existing animation timelines

The helper appends requested effects. It does not assume it is safe to erase an existing complex animation timeline.

If a deck already contains carefully authored animations, inspect them before adding more.

## PowerPoint version behavior

Advanced features may vary by Office version.

The helper resolves COM enum names dynamically. If a required Morph or animation constant is not exposed by the installed PowerPoint version, it should fail clearly rather than silently substituting an unrelated effect.

## Platform fallback

If native enhancement is unavailable:

- keep the base deck editable
- preserve scene states as consecutive slides
- use standard transitions supported by the base-generation library
- do not claim Morph or native 3D exists
- optionally leave the motion manifest with the deck so it can be enhanced later on a Windows/PowerPoint machine

## Verification

After enhancement:

1. reopen the saved PPTX in desktop PowerPoint
2. inspect the Selection Pane names for critical Morph objects
3. run slideshow mode through every Morph pair
4. confirm animation order matches narration
5. confirm 3D models are embedded and not broken links
6. save, close, reopen, and retest at least one representative advanced sequence

A successful script exit is not sufficient proof that the motion looks correct.
