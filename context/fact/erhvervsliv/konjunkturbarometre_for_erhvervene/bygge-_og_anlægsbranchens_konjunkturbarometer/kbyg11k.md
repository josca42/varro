table: fact.kbyg11k
description: Udviklingsforløb i bygge og anlæg, nettotal (sæsonkorrigeret) efter branche (DB07), indikator, sæsonkorrigering, forløb og tid
measure: indhold (unit Pct.)
columns:
- branche07: join dim.db_10 on branche07=kode::text [approx]
- indikator: values [VIAK=Omsætning, BES=Beskæftigelse, PRIS=Tilbudspriser ved licitation]
- saeson: values [EJSÆSON=Ikke sæsonkorrigeret, SÆSON=Sæsonkorrigeret]
- forlob: values [FAK=Faktisk (foregående 3 måneder), FOR=Forventet (kommende 3 måneder)]
- tid: date range 2005-01-01 to 2025-10-01
dim docs: /dim/db_10.md

notes:
- branche07 does NOT join dim.db_10 — uses 4 coarser survey groupings vs kbyg11's 9: F = total sector, 41000 = Byggeentreprenører, 42000 = Anlægsentreprenører, 43000 = Bygge- og anlægsvirksomhed specialisering (aggregate, not further broken down here). Use ColumnValues("kbyg11k", "branche07").
- saeson is a view selector that doubles the data (EJSÆSON vs SÆSON). Always filter to one. Use SÆSON for seasonally adjusted series, EJSÆSON for unadjusted.
- indikator is a measurement selector (VIAK/BES/PRIS are independent). Always filter to one.
- forlob is a measurement selector (FAK vs FOR). Always filter to one.
- This table contains only NET totals (nettotal = %stigende − %faldende). For the full STØR/UÆNDR/MINDRE/NET breakdown use kbyg11.
- kbyg11k has coarser branch granularity than kbyg11 (4 vs 9 branche07 values).