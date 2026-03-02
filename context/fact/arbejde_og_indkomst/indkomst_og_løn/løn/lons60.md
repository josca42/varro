table: fact.lons60
description: Fortjeneste pr. præsteret time efter branche (DB07), alder, køn, lønkomponenter og tid
measure: indhold (unit Kr.)
columns:
- branche07: join dim.db on branche07=kode::text; levels [2]
- alder: values [TOT=Alder i alt, 1819=18-19 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6099=60 år og derover]
- kon: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- lonmal: values [FORINKL=FORTJENESTE PR. PRÆSTERET TIME, GENEOVERB=Gene- og Overtidstillæg pr. præsteret time, SYGDOM=Fraværsbetalinger pr. præsteret time, GODE=Personalegoder pr. præsteret time, UREGEL=Uregelmæssige betalinger pr. præsteret time, PENS=Pension inkl. ATP pr. præsteret time, BASIS=Basisfortjenesten pr. præsteret time, FERIE=..Feriebetalinger pr. præsteret time, NEDRE=Nedre kvartil, fortjeneste pr. præsteret time, MEDIAN=Median, fortjeneste pr. præsteret time, OVRE=Øvre kvartil, fortjeneste pr. præsteret time]
- tid: date range 2002-01-01 to 2024-01-01
dim docs: /dim/db.md
notes:
- WARNING: The documented dim.db join (branche07=kode::text) is WRONG — same issue as lons40. The numeric codes 1-10 and letter codes A-S in this table are DST-level aggregates that do not correspond to dim.db entries. Use ColumnValues("lons60", "branche07") for correct labels.
- lonmal here has 11 values (fewer than lons30/40/50): FORINKL=total, GENEOVERB=overtime+extras, SYGDOM=absence pay, GODE=perks, UREGEL=irregular, PENS=pension incl. ATP, BASIS=base pay, FERIE=holiday pay, NEDRE/MEDIAN/OVRE=quartiles/median. Always filter to one value.
- alder is coarser than lons50's alder1: TOT, 1819, 2029, 3039, 4049, 5059, 6099. Filter alder='TOT' for all ages.
- This table covers virksomheder og organisationer (private sector) only, from 2002 — no sektor column, no afloen, no longrp. Useful for long-run private-sector trends.
- 4 selector dimensions: branche07, alder, kon, lonmal. Filter all to a single value for a clean time series.
