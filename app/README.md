# FastHTML app

## Auth setup

Required for Google login:

- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`

Optional:

- `GOOGLE_PROJECT_ID` (used by the FastHTML Google client)
- `OAUTH_SCHEME` (override scheme for Google redirect URIs, e.g. `https`)
- `SESSION_SECRET` (signing key for session cookies; FastHTML will auto-generate if unset)

Required for email verification and password reset:

- `RESEND_API_KEY`
- `RESEND_FROM`
- `AUTH_TOKEN_SECRET` (signing key for verification/reset tokens; `SESSION_SECRET` is used if unset)

Optional:

- `APP_BASE_URL` (public base URL for email links, e.g. `https://app.example.com`)

## Running

```bash
python app/main.py
```
