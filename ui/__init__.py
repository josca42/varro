"""ui

FastHTML + DaisyUI UI kit (project-specific).

This package is intentionally opinionated and modeled after shadcn-ui's
conventions (variant + size APIs, compound components, slot attributes).

Suggested usage for this repo:

    from ui import *

Recommended structure:
- `ui.core`: helpers and headers
- `ui.components`: building blocks (Button, Card, Input, ...)
- `ui.app`: demo-app compositions (Navbar, ChatInput, DashboardPanel)
- `ui.daisy`: low-level DaisyUI primitives (escape hatch)
"""

from .core import (
    DEFAULT_DARK_THEME,
    DEFAULT_THEME,
    daisy_app,
    daisy_hdrs,
    theme_css,
    ui_hdrs,
    cn,
    cls_join,
)

# Opinionated components
from .components import (
    Button,
    LinkButton,
    IconButton,
    ButtonVariant,
    ButtonSize,
    Card,
    CardBody,
    CardHeader,
    CardTitle,
    CardDescription,
    CardContent,
    CardFooter,
    CardActions,
    Input,
    Select,
    Textarea,
    Separator,
    Field,
    FieldSet,
    FieldLegend,
    FieldLabel,
    FieldContent,
    FieldDescription,
    FieldError,
    Prose,
    MarkdownProse,
    Badge,
    Alert,
    Callout,
    Checkbox,
    Grid,
    Stack,
    HStack,
    VStack,
    Form,
    Stat,
    StatSkeleton,
    FormField,
    Link,
    LinkColor,
)

# App-specific compositions
from .app import (
    Navbar,
    UserMessage,
    AssistantMessage,
    ThinkingSteps,
    EditsIndicator,
    ChatInput,
    MetricCard,
    ChartShell,
    DashboardPanel,
    AuthPage,
    AuthFormCard,
    AuthSimpleCard,
    AuthNotices,
    AuthLinks,
    AuthGoogleCta,
    AuthLoginForm,
    AuthSignupForm,
    AuthVerificationResendForm,
    AuthPasswordResetForm,
    AuthPasswordResetConfirmForm,
)

# Escape hatch: low-level primitives (not star-exported by default)
from . import daisy

__version__ = "0.2.0"

__all__ = [
    # Core
    "DEFAULT_THEME",
    "DEFAULT_DARK_THEME",
    "daisy_app",
    "daisy_hdrs",
    "ui_hdrs",
    "theme_css",
    "cn",
    "cls_join",

    # Components
    "Button",
    "LinkButton",
    "IconButton",
    "ButtonVariant",
    "ButtonSize",
    "Card",
    "CardBody",
    "CardHeader",
    "CardTitle",
    "CardDescription",
    "CardContent",
    "CardFooter",
    "CardActions",
    "Input",
    "Select",
    "Textarea",
    "Separator",
    "Field",
    "FieldSet",
    "FieldLegend",
    "FieldLabel",
    "FieldContent",
    "FieldDescription",
    "FieldError",
    "Prose",
    "MarkdownProse",
    "Badge",
    "Alert",
    "Callout",
    "Checkbox",
    "Grid",
    "Stack",
    "HStack",
    "VStack",
    "Form",
    "Stat",
    "StatSkeleton",
    "FormField",
    "Link",
    "LinkColor",

    # App
    "Navbar",
    "UserMessage",
    "AssistantMessage",
    "ThinkingSteps",
    "EditsIndicator",
    "ChatInput",
    "MetricCard",
    "ChartShell",
    "DashboardPanel",
    "AuthPage",
    "AuthFormCard",
    "AuthSimpleCard",
    "AuthNotices",
    "AuthLinks",
    "AuthGoogleCta",
    "AuthLoginForm",
    "AuthSignupForm",
    "AuthVerificationResendForm",
    "AuthPasswordResetForm",
    "AuthPasswordResetConfirmForm",

    # Escape hatch module
    "daisy",
]
