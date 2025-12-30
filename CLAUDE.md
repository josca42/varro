# VARRO

AI-powered data analysis platform for Denmark Statistics (Danmarks Statistik).

## Structure

```
backend/     # Chainlit chat UI + Pydantic-AI agent (Python)
frontend/    # Next.js app with split-pane iframes (TypeScript)
```

## Running

```bash
# Backend (chat UI on port 8026)
cd backend && chainlit run ui_chat/app.py --port 8026

# Frontend (Next.js on port 3000)
cd frontend && npm run dev
```

## Code Style

- Simple and concise
- Let code fail naturally (minimal try/except)
- Essential comments only
