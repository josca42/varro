"""ui.components

Opinionated, shadcn-inspired components implemented on top of DaisyUI.

Import from here if you want building blocks:

    from ui.components import Button, Card, Input

Most projects will use the top-level re-exports:

    from ui import Button, Card, Input
"""

from .button import Button, LinkButton, IconButton, ButtonVariant, ButtonSize
from .card import (
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
from .input import Input, Select, InputVariant, InputSize, InputColor
from .textarea import Textarea, TextareaVariant, TextareaSize, TextareaColor
from .separator import Separator, SeparatorOrientation, SeparatorColor
from .field import (
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
from .prose import Prose, MarkdownProse
from .badge import Badge, BadgeVariant, BadgeSize, BadgeColor
from .alert import Alert, Callout, AlertVariant
from .checkbox import Checkbox, CheckboxSize, CheckboxColor
from .grid import Grid
from .stack import Stack, HStack, VStack, StackDirection
from .form import Form, FormLayout
from .stat import Stat, StatSkeleton
from .link import Link, LinkColor
from .metric import MetricValue, MetricFormat
from .table import DataTable, TableVariant, TableSize
from .figure import Figure, FigureSkeleton
from .filter import SelectFilter, DateRangeFilter, CheckboxFilter

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
