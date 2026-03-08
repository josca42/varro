# Playground Q4: Afgrøder (Chat 72)

Date: 2026-03-06.

Findings at: `data/trajectory/1/72/findings.md`

## Key findings

1. **SQL `::` cast conflicts with `:param` syntax** — Agent wrote `:aar::VARCHAR` which SQLAlchemy misparses. Self-corrected to `CAST()` in 2 extra steps. Should be documented in dashboard SKILL.md.

2. **Cleanest session yet** — 5 turns total. Exploration turns averaged 2.3 tool calls each. Dashboard creation + iteration worked end-to-end with validation and snapshot.

3. **Collaboration exemplary** — Agent answered directly with data (no over-asking), offered natural follow-ups, checked for existing dashboards, and transitioned to dashboard after 3 substantive exploration turns.

4. **Subject navigation fast** — Only 1 ls + 2 reads to reach `afg6`. Direct subject mapping ("afgrøde" → "landbrug" → "det dyrkede areal") worked well. Contrasts with Q2's indirect mapping cost.

5. **Stateless shell mode works for analysis** — 5 separate CLI invocations, no NameErrors. Agent re-queried as needed.

## What worked well

- Three complementary exploration angles before dashboard: current top, historical rivalry, newer crops
- Jupyter code smartly filtered group totals to show only leaf-level crops
- Dashboard reused all three exploration query patterns
- Double ValidateDashboard (unfiltered + filtered `?aar=1990`) was good practice
- YoY change shown in metrics, chart labels, and table column — coherent design

## Improvement opportunity

- **`CAST()` over `::` documentation** in dashboard SKILL.md — one-line addition preventing a common parameterization trap.
