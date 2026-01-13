# Web Application

The main FastHTML web application that serves the Varro interface.

## Structure

```
app/
├── main.py          # FastHTML app setup, routing, session auth
└── routes/
    ├── auth.py      # Authentication routes and session management
    └── index.py     # Index/home page routes
```

## Key Patterns

### Authentication
- Session-based auth using `require_auth` beforeware
- Password hashing with Argon2
- `AUTH_SKIP` and `STATIC_SKIP` patterns for route exclusion
- `SESSION_SECRET` from environment variable

### Route Organization
Routes are organized as modular router objects that get mounted to the app:
```python
from app.routes import AuthRouter, IndexRouter
app = AuthRouter(app)  # etc.
```

## Usage

Always import UI components from the `ui` library - never define UI components directly in the app code. If a new component is needed, add it to `ui/components/` first.
