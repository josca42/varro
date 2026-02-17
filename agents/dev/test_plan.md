# Test Plan: Rigsstatistikeren

## Category 1: Simple Analytical Questions (warm-up)
Basic workflow: read docs → find table → SQL → present answer.

1. **"Hvor mange mennesker bor der i Danmark?"** — Simplest possible query. Tests that the agent can find `folk1a` and return a number.

2. **"Hvad er arbejdsløshedsprocenten lige nu?"** — Tests finding the right unemployment table (`aup01`), understanding seasonally adjusted data.

3. **"Hvad er Danmarks BNP?"** — Tests navigation to `økonomi/nationalregnskab` and querying `nan1` or `nkn1`.

## Category 2: Multi-step Analysis (analytical depth)
Joining tables, filtering, and interpreting results.

4. **"Hvordan har befolkningsudviklingen været i de 5 regioner de sidste 10 år? Hvilke regioner vokser og hvilke skrumper?"** — Tests joining with `dim.nuts`, filtering by `niveau`, creating a time series comparison.

5. **"Er der en sammenhæng mellem forældres uddannelsesniveau og unges gennemførelse af ungdomsuddannelser?"** — Tests `statusu4`/`statusu5` (youth education by parental education/income). Requires thoughtful analysis.

6. **"Sammenlign sygefravær på tværs af brancher og køn. Hvilke brancher har størst kønsforskelle?"** — Tests `fra020`+ tables, requires joins with industry dimension, comparison logic.

7. **"Hvordan har kriminaliteten udviklet sig de sidste 20 år, opdelt på overtrædelsestyper?"** — Tests `strafna3`-`strafna9`, hierarchical offense classification, long time series.

## Category 3: Visualization Quality (Jupyter + Plotly)
Should produce good figures and test the `show` parameter.

8. **"Lav en befolkningspyramide for Danmark"** — Classic demographic visualization. Tests age/gender breakdown from `folk1a`, proper horizontal bar chart.

9. **"Vis udviklingen i detailhandlen de sidste 5 år som et line chart, opdelt på produktgrupper"** — Tests `deta212`, time series plotly line chart with multiple traces.

10. **"Plot Danmarks jernbaneinvesteringer over tid sammenlignet med togkilometer"** — Tests `bane42` + `bane31`, dual-axis or normalized comparison chart.

## Category 4: Dashboard Creation (core feature)

11. **"Lav et dashboard over befolkningsudviklingen i Danmark med filtre for region og tidsperiode"** — The canonical test. Should create `queries/*.sql`, `outputs.py`, `dashboard.md` with filters, metrics, and figures. Agent should read `/skills/dashboard/SKILL.md` first.

12. **"Lav et dashboard der sammenligner uddannelsesniveauet på tværs af regioner med fokus på kønsforskelle"** — Complex dashboard with multiple queries, cross-dimensional analysis. Good test of filter implementation.

13. **"Kan du lave et dashboard over affald og genanvendelse i Danmark?"** — Tests material/waste data (`affald`, `laby24`). Less obvious subject, tests navigation of unfamiliar tables.

## Category 5: Dashboard Navigation & Iteration
Tests `UpdateUrl`, `Snapshot`, and iterating on existing dashboards.

14. After dashboard #11: **"Naviger til dashboardet og vis mig Region Hovedstaden"** — Tests `UpdateUrl` with filter params.

15. **"Tag et snapshot af dashboardet med de nuværende filtre"** — Tests `Snapshot()` tool, verify folder structure matches design doc pattern.

16. **"Figuren for befolkningstrend ser lidt rodet ud — kan du ændre den til kun at vise de sidste 5 år?"** — Tests editing an existing dashboard (`Edit` on `outputs.py` or `queries/*.sql`), not creating a new one.

## Category 6: Cross-domain / Exploratory
Working across subject areas, open-ended questions.

17. **"Hvad kan du fortælle mig om den danske økonomi over de sidste 150 år?"** — Tests historical national accounts (`hnr1`, 1870-2024). Open-ended, tests how the agent structures a long analysis.

18. **"Er der en sammenhæng mellem urbanisering og kriminalitet i Danmark?"** — Requires combining population data (`by1`/`by2`) with crime data (`strafna6`/`strafna7`). True cross-domain analysis.

19. **"Sammenlign energiforbrug med BNP-udvikling — har Danmark afkoblet vækst fra energiforbrug?"** — Tests `miljø_og_energi` + `økonomi`, requires normalization and interpretation.

## Category 7: Edge Cases & Robustness

20. **"Hvor mange spiller cello i danske musikskoler?"** — Tests `ColumnValues` fuzzy matching, niche data.

21. **"Vis mig data om turisme"** — Vague query, tests whether the agent navigates to `overnatninger_og_rejser` and handles ambiguity.

22. **"Hvad er den mest populære uddannelse i Danmark?"** — Ambiguous (popular how?), tests agent reasoning.

## Suggested Test Order

| Phase | Tests | Focus |
|-------|-------|-------|
| **1. Smoke test** | #1, #2, #3 | Basic query → answer flow works |
| **2. Analysis depth** | #4, #8, #9 | Multi-step analysis + visualization |
| **3. Dashboard creation** | #11 | Core dashboard creation flow |
| **4. Dashboard interaction** | #14, #15, #16 | Navigation, snapshots, iteration |
| **5. Complex analysis** | #5, #6, #7 | Cross-dimensional, interpretation |
| **6. Second dashboard** | #12 or #13 | Another domain, verify consistency |
| **7. Cross-domain** | #17, #18, #19 | Open-ended, multi-subject |
| **8. Edge cases** | #20, #21, #22 | Robustness, ambiguity handling |

Phase 1-4 in one chat session (tests conversation continuity and dashboard iteration). Phases 5-8 as separate conversations to test fresh starts across different subject areas.
