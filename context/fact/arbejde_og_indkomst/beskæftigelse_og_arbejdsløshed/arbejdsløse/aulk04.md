table: fact.aulk04
description: Langtidsledige efter område, enhed, alder, køn og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2, 3]
- enhed: values [1=Langtidsledige (antal), 2=Langtidledige i procent af arbejdsstyrken]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 6099=60 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2009-01-01 to 2025-05-01
dim docs: /dim/nuts.md

notes:
- enhed is a measurement selector: 1=antal, 2=pct. af arbejdsstyrken. Every combination appears twice. Always filter to one enhed.
- omrade joins dim.nuts at levels 1/2/3. omrade='0'=Hele landet not in dim.
- Covers langtidsledige (long-term unemployed, ≥26 weeks), not all fuldtidsledige. For all fuldtidsledige use auf01/aulk01.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.