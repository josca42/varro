table: fact.kbi1
description: Udviklingsforløb i industrien efter branche (DB07), indikator, bedømmelse, forløb og tid
measure: indhold (unit Pct.)
columns:
- branche07: join dim.db on branche07=kode::text [approx]
- indikator: values [PRO=Produktion, BES=Beskæftigelse, SORD=Samlet ordreindgang, SALG=Salgspriser]
- bedommelse: values [STØ1=Stigende, UÆN=Omtrent uændret, MIN1=Faldende, NET=Nettotal]
- forlob: values [FAK=Faktisk (foregående 3 måneder), FOR=Forventet (kommende 3 måneder)]
- tid: date range 2005-01-01 to 2025-10-01
dim docs: /dim/db.md

notes:
- branche07 does NOT join dim.db — dim.db uses numeric codes (1, 2, 3…) while branche07 uses DB07 section letter codes (B, C, CA–CM). Use ColumnValues("kbi1", "branche07") for the full list with labels.
- branche07 hierarchy: BC = aggregate of B+C (mining + manufacturing). C = total manufacturing. CA–CM = 13 sub-industries of manufacturing. S1–S4 = MIG cross-cutting groupings (span multiple sub-industries). Never mix hierarchy levels in a sum — BC, C, and CA–CM all overlap.
- bedommelse=NET is a derived nettotal: NET = STØ1 − MIN1 (percentage points). It is the most useful single indicator for trend direction. Do NOT sum across all bedommelse values — NET is already derived from the others.
- forlob splits every dimension combination into FAK (actual, past 3 months) and FOR (expected, next 3 months). Always filter forlob unless explicitly comparing actual vs expected.
- All four dimension columns (branche07, indikator, bedommelse, forlob) must be filtered. A query for "production trend in total manufacturing" should be: branche07='C', indikator='PRO', bedommelse='NET', forlob='FAK'.
- Sample: SELECT tid, indhold FROM fact.kbi1 WHERE branche07='C' AND indikator='PRO' AND bedommelse='NET' AND forlob='FAK' ORDER BY tid;