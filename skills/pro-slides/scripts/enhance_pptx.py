#!/usr/bin/env python3
"""Apply native PowerPoint motion and 3D enhancements from a JSON manifest.

Requirements:
- Windows
- Microsoft PowerPoint desktop
- Python 3
- pywin32

This script intentionally supports a small, conservative animation vocabulary.
The base PPTX should already contain the final layout and editable objects.
"""

from __future__ import annotations

import argparse
import json
import os
import platform
import sys
from pathlib import Path
from typing import Any


ANIMATION_EFFECTS = {
    # Microsoft Office MsoAnimEffect values
    "appear": 1,
    "fly": 2,
    "fade": 10,
    "wipe": 22,
    "zoom": 23,
}

ANIMATION_TRIGGERS = {
    # Microsoft Office MsoAnimTriggerType values
    "on-click": 1,
    "with-previous": 2,
    "after-previous": 3,
}

MORPH_ENUM_NAMES = {
    "object": "ppEffectMorphByObject",
    "word": "ppEffectMorphByWord",
    "character": "ppEffectMorphByChar",
    "char": "ppEffectMorphByChar",
}

# Stable PpEntryEffect values used as a fallback when the generated COM
# type library does not expose the symbolic Morph constants to pywin32.
MORPH_FALLBACK_VALUES = {
    "object": 3954,
    "word": 3955,
    "character": 3956,
    "char": 3956,
}


def fail(message: str) -> None:
    raise ValueError(message)


def load_manifest(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail(f"Manifest not found: {path}")
    except json.JSONDecodeError as exc:
        fail(f"Invalid JSON in {path}: {exc}")

    if not isinstance(data, dict):
        fail("Manifest root must be a JSON object")
    if data.get("version") != 1:
        fail("Manifest must contain version: 1")
    slides = data.get("slides")
    if not isinstance(slides, dict) or not slides:
        fail("Manifest must contain a non-empty slides object")

    for slide_key, spec in slides.items():
        try:
            slide_number = int(slide_key)
        except (TypeError, ValueError):
            fail(f"Slide key must be a 1-based integer string, got {slide_key!r}")
        if slide_number < 1:
            fail(f"Slide number must be >= 1, got {slide_number}")
        if not isinstance(spec, dict):
            fail(f"Slide {slide_number} specification must be an object")

        rename = spec.get("rename", {})
        if not isinstance(rename, dict):
            fail(f"Slide {slide_number}: rename must be an object")
        for old_name, new_name in rename.items():
            if not isinstance(old_name, str) or not isinstance(new_name, str):
                fail(f"Slide {slide_number}: rename keys and values must be strings")

        transition = spec.get("transition")
        if transition is not None:
            if not isinstance(transition, dict):
                fail(f"Slide {slide_number}: transition must be an object")
            if transition.get("type") != "morph":
                fail(
                    f"Slide {slide_number}: native helper currently supports only "
                    "transition.type = 'morph'"
                )
            mode = transition.get("mode", "object")
            if mode not in MORPH_ENUM_NAMES:
                fail(
                    f"Slide {slide_number}: unsupported Morph mode {mode!r}; "
                    "use object, word, or character"
                )
            duration = transition.get("duration", 0.7)
            if not isinstance(duration, (int, float)) or duration <= 0:
                fail(f"Slide {slide_number}: transition duration must be > 0")

        animations = spec.get("animations", [])
        if not isinstance(animations, list):
            fail(f"Slide {slide_number}: animations must be an array")
        for index, animation in enumerate(animations, start=1):
            if not isinstance(animation, dict):
                fail(f"Slide {slide_number}: animation #{index} must be an object")
            if not isinstance(animation.get("shape"), str):
                fail(f"Slide {slide_number}: animation #{index} needs a shape name")
            effect = animation.get("effect", "fade")
            if effect not in ANIMATION_EFFECTS:
                fail(
                    f"Slide {slide_number}: unsupported animation effect {effect!r}; "
                    f"use one of {', '.join(ANIMATION_EFFECTS)}"
                )
            trigger = animation.get("trigger", "on-click")
            if trigger not in ANIMATION_TRIGGERS:
                fail(
                    f"Slide {slide_number}: unsupported trigger {trigger!r}; "
                    f"use one of {', '.join(ANIMATION_TRIGGERS)}"
                )
            for field in ("duration", "delay"):
                value = animation.get(field)
                if value is not None and (
                    not isinstance(value, (int, float)) or value < 0
                ):
                    fail(
                        f"Slide {slide_number}: animation #{index} {field} "
                        "must be a non-negative number"
                    )

        for key in ("insert3d", "model3d"):
            value = spec.get(key, [])
            if not isinstance(value, list):
                fail(f"Slide {slide_number}: {key} must be an array")

        for index, item in enumerate(spec.get("insert3d", []), start=1):
            if not isinstance(item, dict):
                fail(f"Slide {slide_number}: insert3d #{index} must be an object")
            if not isinstance(item.get("file"), str):
                fail(f"Slide {slide_number}: insert3d #{index} needs file")
            for field in ("left", "top"):
                if not isinstance(item.get(field), (int, float)):
                    fail(
                        f"Slide {slide_number}: insert3d #{index} needs numeric {field}"
                    )

        for index, item in enumerate(spec.get("model3d", []), start=1):
            if not isinstance(item, dict) or not isinstance(item.get("shape"), str):
                fail(f"Slide {slide_number}: model3d #{index} needs a shape name")

    return data


def shape_names(slide: Any) -> list[str]:
    return [slide.Shapes.Item(i).Name for i in range(1, slide.Shapes.Count + 1)]


def find_shape(slide: Any, name: str) -> Any:
    for i in range(1, slide.Shapes.Count + 1):
        shape = slide.Shapes.Item(i)
        if shape.Name == name:
            return shape
    available = ", ".join(shape_names(slide))
    raise RuntimeError(
        f"Slide {slide.SlideIndex}: shape {name!r} not found. "
        f"Available shapes: {available or '(none)'}"
    )


def resolve_asset(manifest_path: Path, raw_path: str) -> Path:
    candidate = Path(os.path.expandvars(os.path.expanduser(raw_path)))
    if not candidate.is_absolute():
        candidate = manifest_path.parent / candidate
    candidate = candidate.resolve()
    if not candidate.exists():
        raise FileNotFoundError(f"3D asset not found: {candidate}")
    return candidate


def apply_model3d_properties(model: Any, spec: dict[str, Any]) -> None:
    rotation = spec.get("rotation", {})
    if rotation:
        if "x" in rotation:
            model.RotationX = float(rotation["x"])
        if "y" in rotation:
            model.RotationY = float(rotation["y"])
        if "z" in rotation:
            model.RotationZ = float(rotation["z"])

    camera = spec.get("camera", {})
    if camera:
        if "x" in camera:
            model.CameraPositionX = float(camera["x"])
        if "y" in camera:
            model.CameraPositionY = float(camera["y"])
        if "z" in camera:
            model.CameraPositionZ = float(camera["z"])

    look_at = spec.get("look_at", {})
    if look_at:
        if "x" in look_at:
            model.LookAtPointX = float(look_at["x"])
        if "y" in look_at:
            model.LookAtPointY = float(look_at["y"])
        if "z" in look_at:
            model.LookAtPointZ = float(look_at["z"])

    if "field_of_view" in spec:
        model.FieldOfView = float(spec["field_of_view"])


def get_morph_value(win32: Any, mode: str) -> int:
    enum_name = MORPH_ENUM_NAMES[mode]
    try:
        return int(getattr(win32.constants, enum_name))
    except AttributeError:
        return MORPH_FALLBACK_VALUES[mode]


def enhance(input_path: Path, manifest_path: Path, output_path: Path, data: dict[str, Any]) -> None:
    if platform.system() != "Windows":
        raise RuntimeError(
            "Native enhancement requires Windows with desktop Microsoft PowerPoint installed"
        )

    try:
        import win32com.client as win32
    except ImportError as exc:
        raise RuntimeError(
            "pywin32 is required. Install it with: pip install pywin32"
        ) from exc

    if not input_path.exists():
        raise FileNotFoundError(f"Input presentation not found: {input_path}")

    input_path = input_path.resolve()
    output_path = output_path.resolve()

    if output_path != input_path and output_path.exists():
        output_path.unlink()

    app = None
    presentation = None
    try:
        # EnsureDispatch generates a typed wrapper when possible, which makes
        # newer PowerPoint enum constants available through win32.constants.
        app = win32.gencache.EnsureDispatch("PowerPoint.Application")
        app.Visible = True
        presentation = app.Presentations.Open(str(input_path), False, False, False)

        for slide_key in sorted(data["slides"], key=lambda value: int(value)):
            slide_number = int(slide_key)
            if slide_number > presentation.Slides.Count:
                raise RuntimeError(
                    f"Manifest references slide {slide_number}, but presentation has "
                    f"only {presentation.Slides.Count} slides"
                )

            spec = data["slides"][slide_key]
            slide = presentation.Slides.Item(slide_number)

            # Insert native 3D shapes first so they can immediately participate
            # in the same slide's rename/model configuration.
            for item in spec.get("insert3d", []):
                asset = resolve_asset(manifest_path, item["file"])
                width = float(item.get("width", -1))
                height = float(item.get("height", -1))
                shape = slide.Shapes.Add3DModel(
                    str(asset),
                    0,      # msoFalse: do not link
                    -1,     # msoTrue: embed/save with presentation
                    float(item["left"]),
                    float(item["top"]),
                    width,
                    height,
                )
                if item.get("name"):
                    shape.Name = item["name"]
                apply_model3d_properties(shape.Model3D, item)

            for old_name, new_name in spec.get("rename", {}).items():
                find_shape(slide, old_name).Name = new_name

            for item in spec.get("model3d", []):
                shape = find_shape(slide, item["shape"])
                apply_model3d_properties(shape.Model3D, item)

            transition = spec.get("transition")
            if transition:
                mode = transition.get("mode", "object")
                slide.SlideShowTransition.EntryEffect = get_morph_value(win32, mode)
                slide.SlideShowTransition.Duration = float(
                    transition.get("duration", 0.7)
                )

            for animation in spec.get("animations", []):
                shape = find_shape(slide, animation["shape"])
                effect_id = ANIMATION_EFFECTS[animation.get("effect", "fade")]
                trigger_id = ANIMATION_TRIGGERS[
                    animation.get("trigger", "on-click")
                ]
                # Level 0 is msoAnimateLevelNone.
                effect = slide.TimeLine.MainSequence.AddEffect(
                    shape, effect_id, 0, trigger_id
                )
                effect.Timing.Duration = float(animation.get("duration", 0.4))
                effect.Timing.TriggerDelayTime = float(animation.get("delay", 0.0))
                if "accelerate" in animation:
                    effect.Timing.Accelerate = float(animation["accelerate"])
                if "decelerate" in animation:
                    effect.Timing.Decelerate = float(animation["decelerate"])

        if output_path == input_path:
            presentation.Save()
        else:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            presentation.SaveAs(str(output_path))

    finally:
        if presentation is not None:
            try:
                presentation.Close()
            except Exception:
                pass
        if app is not None:
            try:
                app.Quit()
            except Exception:
                pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Apply native PowerPoint Morph, animations, and 3D from JSON"
    )
    parser.add_argument("input", type=Path, help="Input .pptx")
    parser.add_argument("manifest", type=Path, help="Motion manifest JSON")
    parser.add_argument(
        "--output",
        type=Path,
        help="Output .pptx. Omit to modify the input presentation in place.",
    )
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate JSON structure without opening PowerPoint",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest_path = args.manifest.resolve()
    try:
        data = load_manifest(manifest_path)
        if args.validate_only:
            print(f"Manifest OK: {manifest_path}")
            return 0

        output = args.output if args.output else args.input
        enhance(args.input, manifest_path, output, data)
        print(f"Enhanced presentation saved to: {output.resolve()}")
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
