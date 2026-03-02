table: fact.byg1
description: Beskæftigede ved bygge og anlæg efter branche (DB07), art, sæsonkorrigering og tid
measure: indhold (unit Antal)
columns:
- branche07: join dim.db on branche07=kode::text [approx]; levels [5]
- art: values [TOT=I alt, 001=Nybyggeri og tilbygning i alt, 002=Reparation og vedligeholdelse i alt, 003=Anlægsvirksomhed i alt, 004=Anden virksomhed i alt, 008=Kontorarbejde, 007=Ikke på arbejde pga. dårligt vejr, ferie, sygdom, undervisning o.l.]
- saeson: values [10=Sæsonkorrigeret, 20=Faktiske tal]
- tid: date range 2000-01-01 to 2025-01-01
dim docs: /dim/db.md

notes:
- saeson is a measurement selector that doubles every row: saeson=10 (Sæsonkorrigeret) and saeson=20 (Faktiske tal) exist for every branche07+art+tid combination. Always filter to one value — use saeson='20' for actual figures or saeson='10' for seasonally adjusted. Forgetting this silently doubles all counts.
- art='TOT' is the sum of all activity types (001 Nybyggeri og tilbygning + 002 Reparation og vedligeholdelse + 003 Anlægsvirksomhed + 004 Anden virksomhed + 007 Fraværende + 008 Kontorarbejde). Filter art='TOT' for a simple headcount, or filter to a specific art code for breakdowns. Never include TOT when summing across art values.
- branche07 does NOT reliably join dim.db — only 2 of 9 codes (432200, 439910) match the standard DB07 hierarchy. The table uses custom survey codes: 41000=Byggeentreprenører, 42000=Anlægsentreprenører, 43003=Anden specialiseret bygge- og anlægsvirksomhed mv., 43201=El-installation mv., 432200=VVS- og blikkenslagerforretninger, 43301=Tømrer- og bygningsvirksomhed mv., 43302=Maler- og glarmestervirksomhed mv., 439910=Murere, F=I alt (total for all construction). Use ColumnValues("byg1", "branche07") to get all 9 codes with labels — do not attempt a dim.db join.
- branche07='F' is the total across all construction branches. The individual 8 codes sum to F (e.g. 2024 Q1 faktiske tal: 193,186 vs F=193,189). Filter branche07='F' for a sector-wide total.