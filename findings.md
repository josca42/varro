# Findings: Chat 19

## Exploration Goal
Test the agent on a multi-dimensional analytical question: comparing sickness absence across industries and gender (test plan question #6). The goal is to evaluate how well the agent navigates dimension tables, particularly the DB07 industry classification, and whether the tooling and documentation support efficient queries.

## Findings

### 1. dim.db missing DB07 section-level codes (A-S) causes 8 wasted steps

**Hypothesis**: The agent should be able to join `fact.fra022.erhverv` to `dim.db` and get industry names at an appropriate aggregation level in 1-2 SQL queries.

**Probe**: "Sammenlign sygefravær på tværs af brancher og køn. Hvilke brancher har størst kønsforskelle?"

**Observed Trajectory Evidence**:
- Steps 5-13 (9 SQL queries) were spent debugging the dimension mapping
- Step 5: Agent tries `JOIN dim.db ON erhverv=kode::text WHERE niveau=2` — gets 10 granular sub-industries, not the 19 sections it needs
- Step 6-8: Explores dim.db structure, discovers only numeric codes at niveauer 2-5
- Step 8: Discovers fact table contains letter codes (A-S) alongside numeric codes
- Steps 9-11: Tries to join letter codes to dim.db — fails (kode is INTEGER, no level 1 exists)
- Step 12: Falls back to regex `WHERE erhverv ~ '^[A-Z]$'` to extract letter-coded rows
- Step 13: Hardcodes all 19 DB07 section names in a CTE to get readable labels

**Interpretation**: The fra022 README says `erhverv: join dim.db on erhverv=kode::text; levels [2, 3]` but doesn't mention that `erhverv` **also** contains letter codes A-S representing DB07 sections (Afsnit) — a higher aggregation level that has no representation in dim.db. The agent naturally follows the documented join, gets overly granular results, and then spends 8 steps discovering and working around the gap. The `dim.db.kode` column is INTEGER, so letter codes structurally cannot exist there.

This is **systemic**: `hfudd16` has 8.4M rows with letter codes, `ligehb11` has 480, `aku420a` has 51. Any table referencing DB07 sections hits this wall.

**Proposed Change**: Two complementary fixes:

1. **Documentation fix (quick)**: In the README for tables where `erhverv`/`branche` contains letter codes, add the mapping explicitly:
   ```
   - erhverv: join dim.db on erhverv=kode::text; levels [2, 3].
     Also contains DB07 section codes not in dim.db:
     A=Landbrug, skovbrug og fiskeri, B=Råstofindvinding, C=Industri,
     D=Energiforsyning, E=Vandforsyning og renovation, F=Bygge og anlæg, ...
   ```
   This can be automated in `varro/context/fact_table.py` by detecting unjoined letter values.

2. **Structural fix (better)**: Add section-level rows to dim.db as niveau=1 with text kode. Requires changing `dim.db.kode` from INTEGER to VARCHAR (or creating a `dim.db_section` lookup). Then joins work naturally.

**Expected Trajectory Delta**: Steps 5-13 (9 queries) collapse to 1-2 queries. The agent reads the README, sees the section codes with labels, and writes one query joining or filtering by letter codes. Saves ~8 steps and ~45 seconds.

**Validation Probe**: Re-run the same question after implementing the documentation fix. The agent should go from README → single SQL query with letter codes → visualization in under 8 steps total.

---

### 2. ColumnValues on dim.db returns granular codes, not the aggregation level the agent needs

**Hypothesis**: `ColumnValues(table='db', column='titel')` should help the agent understand available industry groupings.

**Probe**: (same as above — observed at step 4)

**Observed Trajectory Evidence**:
- Step 4: Agent calls `ColumnValues(table='db', column='titel')` and gets niveau 2 entries (88 granular sub-industries like "Plante- og husdyravl" and "Skovbrug og skovning")
- This doesn't reveal that the fact table also uses letter-coded section-level aggregates
- Agent proceeds to query with niveau=2 codes, gets too many granular categories, and has to backtrack

**Interpretation**: ColumnValues shows what's in the dimension table, but the dimension table is incomplete. The agent has no tool-assisted way to discover that fact.fra022 contains values (A-S) that don't exist in dim.db. The only way to discover this is by querying the fact table directly and noticing unjoined rows — which is what the agent eventually did, but it took several tries.

**Proposed Change**: When a dimension column has values that don't join to the referenced dim table, the ColumnValues tool (or the README) should surface this. Options:
- ColumnValues could show "X unmatched values in fact table" when queried on a dimension
- The README generation (`get_niveau_levels` in `fact_table.py`) already joins to find matching levels — extend it to also report unmatched values

**Expected Trajectory Delta**: Agent immediately knows about unmatched letter codes after first ColumnValues call, avoiding the 5-step debugging detour (steps 6-11).

**Validation Probe**: Call `ColumnValues(table='fra022', column='erhverv')` — does it show the letter codes alongside the dim-joined values?

---

### 3. Final output quality is excellent despite trajectory inefficiency

**Hypothesis**: The agent should produce a good analytical answer with appropriate visualizations.

**Probe**: (same question)

**Observed Trajectory Evidence**:
- Steps 14-16: Clean pivot table, grouped bar chart, and diverging bar chart for gender gap
- Final response includes well-structured table, substantive interpretation (public sector correlation, selection effects in construction)
- Two complementary Plotly figures: absolute comparison and gender gap ranking
- Correct data source citation

**Interpretation**: Once the agent has the data, its analytical and visualization capabilities are strong. The hardcoded CTE (step 13) produced correct labels. The response quality validates that the bottleneck is data discovery, not analysis.

**Proposed Change**: None needed for analysis quality. The environment improvement (fixing the dimension gap) would let the agent spend its budget on deeper analysis rather than debugging joins.

**Expected Trajectory Delta**: N/A — this finding confirms the output is good; the improvement target is getting there faster.

**Validation Probe**: N/A

## Trajectory Summary

| Phase | Steps | Description |
|-------|-------|-------------|
| Navigation | 1-3 (3 steps) | Find and read fra022 docs — efficient |
| Dimension discovery | 4-13 (10 steps) | Debug dim.db join gap — **wasteful** |
| Analysis & viz | 14-16 (3 steps) | Pivot, chart, chart — efficient |
| Response | 17 (1 step) | Summary with interpretation — good quality |

**Total**: 17 steps, ~110 seconds. **Optimal**: ~8 steps, ~50 seconds.

## Prioritized Actions

1. **Document DB07 section codes in table READMEs** — Detect unjoined letter values in `fact_table.py` context generation and include them with labels. Highest impact (~8 steps saved), lowest effort (few lines in context code). Affects fra022, hfudd16, ligehb11, aku420a, and potentially more tables.

2. **Add DB07 sections to dim.db** — Change kode to VARCHAR or add niveau=1 text rows. Structural fix that makes joins work naturally. Medium effort (schema migration + data backfill). Eliminates the need for hardcoded CTEs.

3. **Surface unmatched fact values in ColumnValues or docs** — When dimension joins are partial, make this visible. Lower priority since fix #1 addresses the immediate symptom, but would catch future similar gaps.
