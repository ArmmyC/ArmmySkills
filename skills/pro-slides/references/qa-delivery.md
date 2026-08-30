# QA and Delivery

A professional presentation is not complete when the file opens. It is complete when the visual hierarchy, editability, motion, assets, and stage behavior have all been checked.

## QA passes

Use separate passes rather than trying to inspect everything at once.

### Pass 1: content

Check:

- every claim is supported by the supplied material or clearly framed as a proposal
- numbers and units are correct
- slide order forms a coherent argument
- repeated content has been removed
- conclusion headlines match the evidence on the slide
- judging criteria or user requirements are all addressed

### Pass 2: layout

Inspect every slide rendered as an image.

Check:

- no clipping
- no text overflow
- no accidental overlap
- consistent outer margins
- clean alignment
- no tiny isolated labels
- no excessive empty space caused by unfinished layout
- no slide overloaded because content should have been split

### Pass 3: hierarchy and readability

View slides at thumbnail size.

The intended focal point should still be obvious.

Check:

- primary message can be found quickly
- body copy is readable at projected size
- key numbers are large enough
- secondary text does not compete with the headline
- contrast is sufficient
- dark slides remain readable on imperfect projectors

### Pass 4: visual system

Check the deck as a sequence.

Look for:

- accidental changes in typography
- inconsistent corner radius, stroke width, or icon style
- random accent colors
- repeated card-grid layouts
- every slide having the same density
- section transitions that do not feel distinct
- one-off decorative choices that create style drift

Consistency does not mean every slide should use the same layout.

### Pass 5: motion

Run the deck in slideshow mode, not only edit mode.

For every advanced sequence, check:

- Morph pairs match the intended objects
- persistent objects do not jump
- motion direction makes semantic sense
- duration matches narration pace
- automatic sequences do not run ahead of the speaker
- click count is manageable
- important content is not hidden until too late
- routine animations do not compete with hero moments

Test the sequence while speaking the intended narration aloud.

### Pass 6: 3D

If native 3D is used:

- reopen the deck after saving
- verify the model still loads
- verify it is embedded when required
- run all model transitions
- inspect performance
- verify callouts stay aligned enough to understand the target feature

### Pass 7: editability

Confirm that elements expected to be editable are truly editable.

Do not describe a full-slide raster image as an editable presentation merely because it is inside a PPTX container.

Check:

- text remains text
- charts remain charts when editability matters
- simple diagrams remain native shapes when practical
- flattened artwork is used only intentionally

## Collision and overflow checks

When generating programmatically, use library-level bounds checks when available, but still render the slide afterward.

Programmatic geometry checks cannot reliably detect every visual problem, especially:

- bad line wrapping
- optical misalignment
- low contrast
- awkward crops
- visually dense groups

## Motion-specific naming audit

For Morph decks, inspect important Selection Pane names.

Requirements:

- intended Morph objects use the same `!!name` on successive slides
- each `!!name` is unique per slide
- unrelated objects do not accidentally share a Morph name
- deleted/recreated objects did not lose intended identity

## Stage test

For a competition or live pitch, run the presentation from beginning to end in actual slideshow mode.

Check:

- opening slide loads cleanly
- first click behaves as expected
- videos, 3D, and fonts are available
- slide advancement never surprises the presenter
- presenter can recover if interrupted
- final slide lands on the intended conclusion
- total presentation timing fits the limit

## Performance

Advanced decks can become heavy.

Watch for:

- long file-open time
- slow slide switching
- lag before animation starts
- stuttering Morph
- video or 3D frame drops
- huge file size caused by oversized images/textures

Optimize the asset causing the problem rather than lowering the quality of the entire deck.

## Compatibility

When the presentation may run on another machine:

- use fonts likely to be available or embed where licensing and PowerPoint allow
- embed critical media when practical
- avoid unsupported features when the target PowerPoint version is known to be old
- test on the destination environment when possible

If native PowerPoint advanced features are essential, say so in the delivery note.

## Delivery package

For a substantial generated deck, keep together:

```text
presentation.pptx
source files / generation script
motion.json                # when native enhancement is used
assets/
    images
    icons
    3d models              # if licensing permits redistribution
```

Do not leave the final PPTX dependent on temporary absolute paths.

## Final acceptance checklist

A deck is ready only when all applicable items are true:

- [ ] narrative has a clear through-line
- [ ] each slide/state has one primary job
- [ ] hierarchy is obvious at thumbnail size
- [ ] no clipping or overflow
- [ ] visual system is consistent without being monotonous
- [ ] source numbers and claims are correct
- [ ] Morph identities are correct
- [ ] animation order matches narration
- [ ] advanced sequences have been tested in slideshow mode
- [ ] 3D assets reopen correctly
- [ ] expected elements remain editable
- [ ] deck performs reliably on the intended machine
- [ ] final slide reinforces the actual conclusion

If any showpiece feature remains unreliable, simplify it before delivery. Reliability on stage is part of presentation quality.
