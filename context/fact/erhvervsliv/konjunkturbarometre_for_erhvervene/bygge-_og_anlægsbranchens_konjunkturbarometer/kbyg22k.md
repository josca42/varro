table: fact.kbyg22k
description: Vurdering af ordrebeholdningen i bygge og anlæg, nettotal (sæson- og brudkorrigeret) efter branche (DB07), indikator, sæsonkorrigering og tid
measure: indhold (unit Pct.)
columns:
- branche07: join dim.db_10 on branche07=kode::text [approx]
- indikator: values [1008=Ordrebeholdning, 1009=Ordrebeholdning, brudkorrigeret]
- saeson: values [EJSÆSON=Ikke sæsonkorrigeret, SÆSON=Sæsonkorrigeret]
- tid: date range 2005-01-01 to 2025-10-01
dim docs: /dim/db_10.md

notes:
- branche07 does NOT join dim.db_10 — same 4 coarser survey groupings as kbyg11k. Use ColumnValues("kbyg22k", "branche07").
- indikator is a measurement selector: 1008 = Ordrebeholdning, 1009 = Ordrebeholdning brudkorrigeret (break-corrected). These are two different series — do not sum. Note: 1009 only exists with EJSÆSON (not seasonally adjusted).
- saeson is a view selector (EJSÆSON vs SÆSON). Always filter to one. SÆSON is only available for indikator=1008.
- This table contains only NET totals. For the full MN1/NOR1/SNO1/NET breakdown use kbyg22.