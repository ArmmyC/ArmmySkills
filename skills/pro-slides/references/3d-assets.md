# 3D Models and Assets

Use this reference when a presentation includes native PowerPoint 3D models or 3D-rendered imagery.

## Decide whether native 3D is justified

Use native 3D when changing viewpoint helps the audience understand:

- shape
- component placement
- assembly
- orientation
- physical interaction
- product transformation

Prefer a static render or image when the model only needs to look attractive from one view.

Native 3D carries cost:

- larger file size
- potential slideshow performance issues
- dependence on PowerPoint feature support
- more QA requirements

## Preferred asset format

Prefer `.glb` for embedded PowerPoint-native 3D assets.

Keep assets presentation-friendly:

- reasonable polygon count
- compressed textures
- no unnecessary hidden geometry
- no oversized textures that will never be visible on screen
- clean material setup
- model origin and orientation that make rotation predictable

Test the actual asset in PowerPoint before building an important sequence around it.

## Native insertion

PowerPoint exposes `Shapes.Add3DModel` for inserting a model as a real PowerPoint shape.

For a self-contained deck, embed rather than link the asset whenever practical.

The helper script uses the equivalent of:

```text
Shapes.Add3DModel(file, link=false, saveWithDocument=true, left, top, width, height)
```

## Coordinate planning

PowerPoint native automation uses points.

For a standard 16:9 slide, think compositionally first, then translate to coordinates.

Keep a model away from slide edges when it will rotate or scale across Morph states. Leave room for visual travel.

## Camera and orientation

PowerPoint's 3D model format exposes:

- RotationX
- RotationY
- RotationZ
- CameraPositionX/Y/Z
- LookAtPointX/Y/Z
- FieldOfView

Use the simplest controls that produce the intended view.

### Rotation

Prefer absolute rotation values for repeatable scenes.

Example concept:

```text
State A: y = 0°
State B: y = 35°
State C: y = 80°
```

This makes the audience perceive a deliberate inspection path.

### Field of view

Field of view changes perspective. Use it carefully.

A dramatic wide-angle perspective may look dynamic but can distort product proportions. For technical or product explanation, a more neutral view is often clearer.

## Morph with 3D

A strong sequence preserves the same model identity while changing:

- position
- size
- rotation
- camera view

Example:

```text
Slide A
!!robot small, front view, placed in system context

Slide B
!!robot larger, centered, y-rotation 25°
Morph to B

Slide C
!!robot y-rotation 75°
callout region becomes visible
Morph to C

Slide D
component labels fade in
```

Use the rotation to reveal a feature. Do not rotate through arbitrary angles just to create motion.

## 3D model plus 2D labels

A reliable presentation pattern is:

- 3D model for form
- 2D PowerPoint callouts for explanation

Keep labels as native text/shapes so they remain sharp and editable.

Avoid attaching large amounts of text directly over the model.

Use leader lines with enough contrast and avoid line crossings.

## Exploded-view illusion

PowerPoint does not automatically create engineering exploded views from a single 3D asset.

For an exploded presentation, use one of these approaches:

1. prepare separate 3D assets/components and position them independently
2. use a pre-rendered exploded view
3. transition from a full 3D model to a 2D exploded diagram

Do not claim a physically correct exploded animation when the source asset does not support it.

## Performance

For competition decks, performance matters more than theoretical fidelity.

Test on the machine that will present when possible.

Watch for:

- stuttering rotation
- delayed texture loading
- blank model frames
- increased PPTX opening time
- animation lag when several heavy assets share a slide

If performance is poor, simplify the model or replace the showpiece with a rendered sequence.

## Asset licensing

Keep track of where external 3D assets came from and whether they can be redistributed with the deck.

Do not embed third-party assets into a deliverable if their license does not permit redistribution.

## Fallback strategy

If native 3D cannot be delivered reliably, prefer:

- high-quality rendered PNG/WebP with transparent background
- short pre-rendered video where appropriate
- multiple rendered angles connected with Morph-like composition

A stable static render is better than a native 3D model that breaks during judging.

## 3D QA checklist

- model loads after reopening the file
- model is embedded when required
- intended rotation values are correct
- Morph identity is stable across slides
- labels remain legible over all model states
- model does not cover critical text during transition
- presentation remains responsive
- fallback exists when the presenting environment is uncertain
