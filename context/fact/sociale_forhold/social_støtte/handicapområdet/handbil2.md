table: fact.handbil2
description: Afslag af støtte til handicapbil efter område, enhed og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- tal: values [5=Sager (antal), 6=Gennemsnitlig sagsbehandlingstid (uger)]
- tid: date range 2010-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- CRITICAL: tal is a measurement selector — always filter to one value at a time:
  - tal=5: antal afslag (number of rejected applications, count)
  - tal=6: gennemsnitlig sagsbehandlingstid i uger (average processing time in weeks, a rate)
  Never SUM across tal values.
- omrade joins dim.nuts at niveau=3. omrade=0 is a national total not in dim.nuts.
- Pair with handbil1 to compare approvals vs rejections: use tal=5 in both tables for case counts.
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.
