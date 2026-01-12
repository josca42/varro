"""ui.components.field

Form field layout helpers (shadcn-inspired).

DaisyUI provides form primitives (input, select, textarea) but does not enforce
shadcn-like field composition (label/description/error). This module provides a
small set of helpers that match the patterns used in this repo.

Key ideas:
- `data-slot` attributes for styling/debugging.
- compact spacing by default.
- orientation support (vertical/horizontal/responsive).
"""

from __future__ import annotations

from typing import Literal, Optional

from fasthtml.common import *

from ..core import cn


FieldOrientation = Literal["vertical", "horizontal", "responsive"]


def FieldSet(*c, cls: str = "", **kw):
    return Fieldset(
        *c,
        cls=cn("space-y-4", cls),
        data_slot="field-set",
        **kw,
    )


def FieldLegend(*c, cls: str = "", **kw):
    return Legend(
        *c,
        cls=cn("text-sm font-medium", cls),
        data_slot="field-legend",
        **kw,
    )


def Field(
    *c,
    orientation: FieldOrientation = "vertical",
    invalid: bool = False,
    disabled: bool = False,
    cls: str = "",
    **kw,
):
    """Layout wrapper.

    Usage:
        Field(
            FieldLabel('Email', for_='email'),
            FieldContent(Input(id='email', name='email')),
            FieldDescription('We\'ll never share it.'),
        )
    """

    orient_cls = {
        "vertical": "flex flex-col gap-2",
        "horizontal": "flex flex-col gap-2 sm:flex-row sm:items-start sm:gap-4",
        "responsive": "flex flex-col gap-2 sm:flex-row sm:items-start sm:gap-4",
    }.get(orientation, "flex flex-col gap-2")

    return Div(
        *c,
        cls=cn(
            orient_cls,
            "[&_[data-slot=field-label]]:shrink-0",
            "[&_[data-slot=field-content]]:flex-1",
            "data-[invalid=true]:[&_[data-slot=field-label]]:text-error",
            "data-[invalid=true]:[&_[data-slot=field-error]]:text-error",
            "data-[disabled=true]:opacity-60",
            cls,
        ),
        data_slot="field",
        data_orientation=orientation,
        data_invalid=str(invalid).lower(),
        data_disabled=str(disabled).lower(),
        **kw,
    )


def FieldLabel(*c, for_: str | None = None, cls: str = "", **kw):
    return Label(
        *c,
        for_=for_,
        cls=cn("text-sm font-medium leading-snug", cls),
        data_slot="field-label",
        **kw,
    )


def FieldContent(*c, cls: str = "", **kw):
    return Div(
        *c,
        cls=cn("flex flex-col gap-1", cls),
        data_slot="field-content",
        **kw,
    )


def FieldDescription(*c, cls: str = "", **kw):
    return P(
        *c,
        cls=cn("text-sm text-base-content/60 leading-normal", cls),
        data_slot="field-description",
        **kw,
    )


def FieldError(*c, cls: str = "", **kw):
    return Div(
        *c,
        role="alert",
        cls=cn("text-sm text-error leading-normal", cls),
        data_slot="field-error",
        **kw,
    )


def FormField(
    label: str,
    control,
    *,
    id: str | None = None,
    description: Optional[str] = None,
    error: Optional[str] = None,
    required: bool = False,
    orientation: FieldOrientation = "vertical",
    cls: str = "",
    **kw,
):
    """Convenience wrapper used frequently in this repo."""

    # Prefer explicit ids so labels work. If the control already has an id,
    # pass it explicitly.
    label_bits = [label + (" *" if required else "")]

    bits = [
        FieldLabel(*label_bits, for_=id),
        FieldContent(control),
    ]

    if error:
        bits.append(FieldError(error))
    elif description:
        bits.append(FieldDescription(description))

    return Field(
        *bits,
        orientation=orientation,
        invalid=bool(error),
        cls=cls,
        **kw,
    )


__all__ = [
    "Field",
    "FieldContent",
    "FieldDescription",
    "FieldError",
    "FieldLabel",
    "FieldLegend",
    "FieldOrientation",
    "FieldSet",
    "FormField",
]
