# Playground Q2: Husleje (Chat 71)

Date: 2026-03-06.

Findings at: `data/trajectory/1/71/findings.md`

## Key findings

1. **Subject navigation cost** — Agent needed 5 `ls` calls + 6 Read calls to navigate from "husleje" to the right tables (`økonomi/ejendomme/huslejeindeks` + `økonomi/forbrug/forbrugsundersøgelsen`). A subject search tool or keyword index would save 2-3 steps.

2. **Snapshot works** — Unlike Q1 (Chat 70), Snapshot now succeeds. Auth/cookie issue is fixed. Dashboard workflow is end-to-end functional.

3. **Collaboration quality excellent** — Agent found two complementary data sources, provided caveats about methodology (all-household average including owners), offered natural follow-up directions, and transitioned to dashboard after 3 substantive exploration turns.

4. **Dashboard iteration smooth** — Region filter + new data source (bol101 for renter/owner share) added cleanly. Double ValidateDashboard (unfiltered + filtered) was good practice.

## What worked well

- Two complementary data angles: actual rent (fu12/fu17) + rent index (hus1)
- Exploration turns were efficient: Turn 1 had only 3 tool calls, Turn 2 had 4
- Dashboard reused exploration queries structurally
- Agent proactively explained caveats about all-household averaging
- Charts were clean and informative (faceted line chart, stacked bar, trend)

## Improvement opportunity

- **Subject/table search tool** — highest-impact improvement across both Q1 and Q2. Would reduce navigation steps for any question with indirect subject mapping.
