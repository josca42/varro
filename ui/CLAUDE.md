# UI Library

An opinionated FastHTML + DaisyUI component library inspired by shadcn-ui. This is not a general-purpose library—it serves this specific app with a specific visual style.

## Philosophy

- **shadcn-style API**: Components use `variant` + `size` props, with `cls` for Tailwind overrides
- **No build step**: Uses Tailwind Browser runtime + CDN DaisyUI v5
- **Flat, compact aesthetic**: Minimal shadows, tight spacing, warm neutral palette
- **Composition over configuration**: Build complex UIs by composing simple components

## Structure

```
ui/
├── core.py          # Helpers: cn(), daisy_app(), ui_hdrs
├── daisy.py         # Low-level DaisyUI primitives (escape hatch)
├── theme.css        # Warmink theme (light/dark)
├── components/      # Opinionated, reusable components
│   ├── button.py    # Button, IconButton
│   ├── card.py      # Card, CardHeader, CardTitle, CardContent, CardFooter, CardSimple
│   ├── input.py     # Input, Select
│   ├── textarea.py  # Textarea
│   ├── field.py     # Field, FieldLabel, FieldError, FormField
│   ├── separator.py # Separator
│   └── prose.py     # Prose, MarkdownProse
└── app/             # App-specific compositions (demo/reference)
    ├── navbar.py    # Navbar
    ├── chat.py      # UserMessage, AssistantMessage, ChatInput
    └── dashboard.py # MetricCard, ChartShell, DashboardPanel
```

## Component Patterns

### Standard signature
```python
def Component(*c, variant="default", size="default", cls: str = "", **kw):
    return BaseComponent(*c, cls=cn("-variant-mod", cls), data_slot="component", **kw)
```

### Variants and sizes
Components expose semantic variants (e.g., `default`, `destructive`, `ghost`) and sizes (`sm`, `md`, `lg`). The mapping to DaisyUI classes is internal.

### Class joining
Use `cn()` to join classes—it filters falsy values:
```python
cn("btn", loading and "loading", cls)
```

### Data attributes
Components set `data_slot`, `data_variant`, `data_size` for styling hooks and debugging.

## Usage

### Creating a FastHTML app
```python
from ui import daisy_app

app, rt = daisy_app()
```

### Using components
```python
from ui import Button, Card, CardHeader, CardTitle, CardContent, Input

Card(
    CardHeader(CardTitle("Login")),
    CardContent(
        Input(name="email", placeholder="Email"),
        Button("Submit", variant="default")
    ),
    variant="border"
)
```

### Custom styling
Pass Tailwind classes via `cls`:
```python
Button("Wide", cls="w-full mt-4")
```

## Key Conventions

1. **Imports**: Import from `ui`, not submodules
2. **Inputs are full-width** by default (`w-full`)
3. **Cards have compact padding** via theme tokens
4. **Use FormField** for labeled inputs with error states
5. **Prefer components/** over direct `daisy` primitives

## Adding New Components

1. Create file in `components/` (or `app/` if app-specific)
2. Follow the variant/size pattern with `cn()` for class building
3. Use `data_slot` for the component name
4. Export from `components/__init__.py` and `ui/__init__.py`
5. Use primitives from `daisy.py` as building blocks. Docs on daisy-ui can be found at agent/docs/daisy-ui.txt
6. For client side interactivity use alpine.js . Docs and examples on alpine.js can be found at agent/docs/alpine_js/*

## Theme

The `warmink` theme in `theme.css` defines:
- Warm neutral palette (paper-like base colors)
- Compact density (`--card-p: 1rem`, smaller font sizes)
- Flat surfaces (`--depth: 0`)
- Smaller border radius (`--radius-box: 0.75rem`)

To customize, edit `theme.css` or create a new theme following the DaisyUI v5 theme format.
