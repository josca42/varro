"""ui.components

Opinionated, shadcn-inspired components implemented on top of DaisyUI.

Import from here if you want building blocks:

    from ui.components import Button, Card, Input

Most projects should import directly:

    from ui.components import Button, Card, Input
"""

from ui.components.button import Button, LinkButton, IconButton, ButtonVariant, ButtonSize
from ui.components.card import (
    Card,
    CardBody,
    CardHeader,
    CardTitle,
    CardDescription,
    CardContent,
    CardFooter,
    CardActions,
    CardSimple,
    CardVariant,
)
from ui.components.input import Input, Select, InputVariant, InputSize, InputColor
from ui.components.textarea import Textarea, TextareaVariant, TextareaSize, TextareaColor
from ui.components.separator import Separator, SeparatorOrientation, SeparatorColor
from ui.components.field import (
    Field,
    FieldContent,
    FieldDescription,
    FieldError,
    FieldLabel,
    FieldLegend,
    FieldOrientation,
    FieldSet,
    FormField,
)
from ui.components.prose import Prose, MarkdownProse
from ui.components.badge import Badge, BadgeVariant, BadgeSize, BadgeColor
from ui.components.alert import Alert, Callout, AlertVariant
from ui.components.checkbox import Checkbox, CheckboxSize, CheckboxColor
from ui.components.grid import Grid
from ui.components.stack import Stack, HStack, VStack, StackDirection
from ui.components.form import Form, FormLayout
from ui.components.stat import Stat, StatSkeleton
from ui.components.link import Link, LinkColor
from ui.components.metric import MetricValue, MetricFormat
from ui.components.table import DataTable, TableVariant, TableSize
from ui.components.figure import Figure, FigureSkeleton
from ui.components.filter import SelectFilter, DateRangeFilter, CheckboxFilter

__all__ = [
    # Buttons
    "Button",
    "LinkButton",
    "IconButton",
    "ButtonVariant",
    "ButtonSize",
    # Cards
    "Card",
    "CardBody",
    "CardHeader",
    "CardTitle",
    "CardDescription",
    "CardContent",
    "CardFooter",
    "CardActions",
    "CardSimple",
    "CardVariant",
    # Inputs
    "Input",
    "Select",
    "InputVariant",
    "InputSize",
    "InputColor",
    # Textarea
    "Textarea",
    "TextareaVariant",
    "TextareaSize",
    "TextareaColor",
    # Separator
    "Separator",
    "SeparatorOrientation",
    "SeparatorColor",
    # Field
    "Field",
    "FieldContent",
    "FieldDescription",
    "FieldError",
    "FieldLabel",
    "FieldLegend",
    "FieldOrientation",
    "FieldSet",
    "FormField",
    # Prose
    "Prose",
    "MarkdownProse",
    # Badge
    "Badge",
    "BadgeVariant",
    "BadgeSize",
    "BadgeColor",
    # Alert
    "Alert",
    "Callout",
    "AlertVariant",
    # Checkbox
    "Checkbox",
    "CheckboxSize",
    "CheckboxColor",
    # Grid
    "Grid",
    # Stack
    "Stack",
    "HStack",
    "VStack",
    "StackDirection",
    # Form
    "Form",
    "FormLayout",
    # Stat
    "Stat",
    "StatSkeleton",
    # Link
    "Link",
    "LinkColor",
    # Metric
    "MetricValue",
    "MetricFormat",
    # Table
    "DataTable",
    "TableVariant",
    "TableSize",
    # Figure
    "Figure",
    "FigureSkeleton",
    # Filter
    "SelectFilter",
    "DateRangeFilter",
    "CheckboxFilter",
]
