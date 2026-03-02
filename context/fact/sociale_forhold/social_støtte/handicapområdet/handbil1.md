table: fact.handbil1
description: Bevilget støtte til handicapbil efter område, enhed og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- tal: values [5=Sager (antal), 6=Gennemsnitlig sagsbehandlingstid (uger), 7=Samlet bevilget beløb (kr.)]
- tid: date range 2011-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- CRITICAL: tal is a measurement selector with three completely different measures stored in indhold. Always filter to exactly one tal value:
  - tal=5: antal sager (number of granted applications, count)
  - tal=6: gennemsnitlig sagsbehandlingstid i uger (average processing time in weeks, a rate — max ~117 weeks)
  - tal=7: samlet bevilget beløb i kr. (total granted amount in DKK, money — max ~416M kr.)
  Never SUM across tal values — the unit of indhold differs completely between rows.
- omrade joins dim.nuts at niveau=3 (98 kommuner). omrade=0 is a national total not in dim.nuts — use it for Denmark-wide figures.
- The "unit Antal" label in the measure column is misleading for tal=6 (weeks) and tal=7 (kr.). Treat indhold unit as determined by the tal filter.
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.
