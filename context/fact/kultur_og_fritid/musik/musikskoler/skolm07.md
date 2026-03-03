table: fact.skolm07
description: Arrangementer på musikskoler efter kommune, arrangementstype, nøgletal og tid
measure: indhold (unit Antal)
columns:
- komk: join dim.nuts on komk=kode; levels [3]
- arrangementtype: values [3000=Arrangementstyper, i alt, 3005=Koncert, 3010=Forestilling, 3015=Fernisering/udstilling, 3020=Øvrige arrangementer]
- bnogle: values [3025=Arrangementer, 3030=Publikum]
- tid: date range 2022 to 2025
dim docs: /dim/nuts.md

notes:
- komk joins dim.nuts at niveau 3. komk='0' is national total, not in the dim.
- bnogle is a measurement selector — 3025=Arrangementer (count of events), 3030=Publikum (audience count). These are different metrics with different magnitudes. Always filter to one bnogle value; summing both silently doubles rows.
- arrangementtype='3000' is the total across all arrangement types. Use to get total events/audience, then filter to e.g. 3005=Koncert for breakdown.
- Map: /geo/kommuner.parquet — merge on komk=dim_kode. Exclude komk=0.