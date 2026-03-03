table: fact.aus08
description: Fuldtidsledige (sæsonkorrigeret) efter område, sæsonkorrigering og faktiske tal og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2, 3]
- saesonfak: values [9=Sæsonkorrigeret i pct. af arbejdsstyrken, 10=Sæsonkorrigeret, 22=Opregnede faktiske i pct. af arbejdsstyrken, 24=Opregnede faktiske]
- tid: date range 2007-01-01 to 2025-09-01
dim docs: /dim/nuts.md

notes:
- saesonfak is a measurement selector — always filter to exactly one value (10=count seasonally adjusted, 24=actual count, 9/22=percentage forms). Failing to filter inflates sums 4x.
- omrade joins dim.nuts at levels 1/2/3. Extra code 0=Hele landet not in dim — use WHERE f.omrade = '0' for national total.
- No ydelsestype or gender/age breakdown — regional seasonal adjustment only. Pair with auf01/aulk01 for full breakdowns.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.