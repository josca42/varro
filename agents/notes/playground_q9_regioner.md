# Playground Q9: Befolkningsvækst i regioner (Chat 74)

Date: 2026-03-06.

Findings at: `data/trajectory/1/74/findings.md`

## Key findings

1. **Strongest multi-step analysis session** — 5 turns, 48 tool calls. Clean arc: specific analysis → deep dive → all-region comparison → dashboard → iteration. No crashes, two self-repairs.

2. **Excellent collaboration quality** — Agent executed immediately on the specific question (correct for a concrete analysis request). Each turn built on the prior narrative thread. Dashboard offered at the right moment (after turn 2).

3. **Multi-table analysis** — Agent used `folk1a` for population totals, then found `bev107` for movement components (birth surplus, internal migration, immigration). Three-level nuts join (kommune → province → region) was executed correctly.

4. **Dashboard self-repair** — Two bugs caught and fixed mid-turn: (a) facet title showing "Region Hovedstaden" instead of faceting when "All" selected (filter value returns empty string, not None), (b) parquet export rejecting mixed int/str column types.

5. **Analytical quality high** — Agent correctly identified that immigration (not internal migration) drives Sjælland's post-2021 growth. Correctly noted that 3 of 5 regions have negative birth surplus.

## Improvement opportunities

- **Filter value contract** — Dashboard SKILL should document what `filters.get()` returns for "all" default. Would save 4+ steps per faceted dashboard.
- **Parquet type constraints** — Dashboard SKILL should note that table columns must be homogeneous types.

## What worked well

- Direct execution on specific question (no unnecessary clarification)
- Natural follow-up offers at each turn
- Checked for existing dashboards before creating
- Parallel tool calls throughout (3 queries in turn 3 step 3, parallel snapshots in turn 3 step 18)
- Visual inspection of snapshots with self-correction
- Dashboard validated both unfiltered and filtered states
