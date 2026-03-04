# Test Plan: Rigsstatistikeren

## 1. Simple Factual Questions

| # | Question | Tests | First move |
|---|----------|-------|------------|
| 1 | "Hvor mange mennesker bor der i Danmark?" | Find `folk1a`, return a single number. Baseline data access. | Execute |
| 2 | "Hvad er den gennemsnitlige husleje i Danmark?" | Navigate `erhvervsliv/bygge_og_boligforhold`, find `livm12` or similar rental table. | Execute |
| 3 | "Hvor mange biler er der i Danmark?" | Find transport/køretøjer tables (`bil707`/`bil10`). Tests navigating a less obvious subject. | Execute |
| 4 | "Hvad er den mest dyrkede afgrøde i Danmark?" | Navigate `erhvervsliv/landbrug_gartneri_og_skovbrug`, find crop tables (`afg07`). Tests ColumnValues on agricultural categories. | Execute |

## 2. Exploratory / Vague Questions

| # | Question | Tests | First move |
|---|----------|-------|------------|
| 5 | "Hvordan går det med den danske økonomi?" | Agent should pick 2-3 headline indicators (BNP, ledighed, inflation) and show data — not ask "hvad mener du med økonomi?". | Explore |
| 6 | "Fortæl mig noget interessant om danske biblioteker" | Navigate `kultur_og_fritid/biblioteker`. Agent should surface data first, offer to dig deeper. Non-expert phrasing. | Explore |
| 7 | "Hvad sker der med energiforbruget i Danmark?" | Navigate `miljø_og_energi/energi`. Should show a trend and volunteer observations about the mix (renewables vs fossil). | Explore |
| 8 | "Jeg er nysgerrig på kriminalitet i Danmark — hvad viser tallene?" | Navigate `sociale_forhold/kriminalitet`. Should show headline trend, then offer drill-down directions. | Explore |

## 3. Multi-step Analysis

| # | Question | Tests | First move |
|---|----------|-------|------------|
| 9 | "Sammenlign befolkningsvæksten i de 5 regioner de sidste 10 år — hvilke vokser og hvilke skrumper?" | Join `folk1a` with `dim.nuts`, filter by niveau. Time series comparison across regions. | Execute |
| 10 | "Er der sammenhæng mellem uddannelsesniveau og indkomstniveau på tværs af kommuner?" | Cross-domain: `uddannelse_og_forskning` + `arbejde_og_indkomst`. Requires joining on geography. | Execute |
| 11 | "Hvordan har Danmarks import og eksport med Kina udviklet sig sammenlignet med Tyskland og USA?" | Navigate `økonomi/udenrigshandel`, filter trade tables by partner country. Multi-series comparison. | Execute |
| 12 | "Hvilke brancher har det højeste sygefravær, og er der kønsforskelle?" | Join sickness absence tables with industry dimensions and gender breakdown. Requires careful overcounting avoidance. | Execute |

## 4. Dashboard Requests

| # | Question | Tests | First move |
|---|----------|-------|------------|
| 13 | "Lav et dashboard om turisme i Danmark" | Vague request — agent should explore `erhvervsliv/hoteller_og_restauranter` + `erhvervsliv/ferie_og_turisme` first, then consolidate. Tests the full dashboard creation workflow. | Explore → build |
| 14 | "Lav et dashboard over boligmarkedet med prisudvikling, boligbestand og salgsaktivitet, filtreret på region og ejendomstype" | Specific request — agent should build directly from `erhvervsliv/bygge_og_boligforhold`. Tests multi-query dashboard with filters. | Execute |
| 15 | "Kan du tilføje en fane om pendling til dashboardet?" | Extension of #14. Tests iteration: editing existing `dashboard.md` and `outputs.py`, adding queries. Must read existing dashboard first. | Execute |
| 16 | "Lav et dashboard der viser hvordan det går med den grønne omstilling" | Semi-vague — agent should identify relevant tables across `miljø_og_energi` (renewable energy share, emissions, waste recycling) and build a coherent narrative. | Explore → build |

## 5. Collaboration Edge Cases

| # | Question | Tests | First move |
|---|----------|-------|------------|
| 17 | "Vis mig data om uddannelse" | Ambiguous — could be enrollment, completion, expenditure, or international students. One clarifying question is justified (but should be accompanied by a data teaser). | Clarify (lightly) |
| 18 | "Lav et dashboard om turisme" (when #13 already exists) | Tests `/dashboard/index.md` check. Agent should surface the existing dashboard and ask whether to extend or start fresh. | Clarify |
| 19 | Start analyzing crime trends (#8), then: "Vent — kan vi i stedet kigge på, om det hænger sammen med ungdomsarbejdsløshed?" | Mid-conversation pivot. Tests that the agent can shift direction without losing context, and joins crime data with youth unemployment. | Execute (new direction) |

## 6. Visualization Quality

| # | Question | Tests | First move |
|---|----------|-------|------------|
| 20 | "Lav en befolkningspyramide for Danmark" | Classic demographic chart. Tests age×gender breakdown from `folk1a`, horizontal bar chart, proper axis formatting. | Execute |
| 21 | "Vis et kort over indkomstniveauet i danske kommuner" | Tests GeoParquet map visualization. Agent must read `/geo/README.md`, join income data with `dim.nuts`, and render a choropleth. | Execute |
| 22 | "Sammenlign de nordiske landes BNP per capita som et bar chart" | Tests whether the agent recognizes it needs external data (DST covers Denmark only) or finds Nordic comparison tables. Should handle gracefully. | Execute or explain limitation |

## Suggested Test Order

### Session A — Core flow (questions in one continuous session)

| Phase | Questions | Focus |
|-------|-----------|-------|
| **Smoke test** | #1, #3 | Basic data lookup works |
| **Exploration** | #5 | Agent shows data without over-asking |
| **Analysis** | #9 | Multi-step join + comparison |
| **Visualization** | #20 | Chart quality |
| **Dashboard creation** | #13 | Full dashboard workflow (vague → explore → build) |
| **Dashboard iteration** | snapshot + navigate with filters | Validate, snapshot, filter interaction |

Session A tests conversation continuity: the agent should remember context from earlier turns and not repeat work.

### Session B — Targeted dashboard (fresh session)

| Phase | Questions | Focus |
|-------|-----------|-------|
| **Specific dashboard** | #14 | Direct build from detailed spec |
| **Extension** | #15 | Iterating on existing dashboard |

### Session C — Analysis depth (fresh session)

| Phase | Questions | Focus |
|-------|-----------|-------|
| **Cross-domain** | #10 | Education × income join |
| **Trade analysis** | #11 | Multi-country comparison |
| **Exploratory** | #7 | Energy data, open scope |

### Session D — Edge cases (fresh session)

| Phase | Questions | Focus |
|-------|-----------|-------|
| **Ambiguity** | #17 | Light clarification + data |
| **Overlap** | #18 | Existing dashboard detection |
| **Pivot** | #8 → #19 | Direction change mid-analysis |

### Session E — Remaining (fresh sessions, any order)

| Questions | Focus |
|-----------|-------|
| #2, #4 | Niche factual lookups |
| #6, #8 | Exploration of unfamiliar domains |
| #12 | Sickness absence analysis |
| #16 | Green transition dashboard |
| #21, #22 | Map visualization, data boundary handling |

### Session notes

- **Session A** is the critical path — if it fails, later sessions will too.
- **Session B** depends on Session A only for #15 (extending the tourism dashboard from #13 could be swapped to extending #14 instead).
- **Sessions C–E** are independent and can run in any order.
- Run #18 after #13 has been completed (needs the existing dashboard to detect).
