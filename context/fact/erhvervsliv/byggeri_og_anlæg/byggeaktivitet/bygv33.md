table: fact.bygv33
description: Boliger i det samlede boligbyggeri (ikke korrigeret for forsinkelser) efter område, byggefase, anvendelse, bygherreforhold og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- bygfase: values [2=Påbegyndt byggeri, 3=Fuldført byggeri, 4=Byggeri under opførelse, 1=Tilladt byggeri]
- anvend: join dim.byganv on anvend=kode::text [approx]; levels [2, 3]
- bygherre: join dim.bygherre on bygherre=kode::text [approx]; levels [2]
- tid: date range 2006-01-01 to 2025-07-01
dim docs: /dim/byganv.md, /dim/bygherre.md, /dim/nuts.md
notes:
- omrade joins dim.nuts but code '0' (Denmark total) is not in the dim. All three nuts levels (1, 2, 3) are present — filter `WHERE d.niveau=3` for kommuner to avoid double-counting.
- anvend joins dim.byganv at niveauer 2 and 3. Code '009' (boligbyggeri i alt) and 'UOPL' are not in the dim — '009' is an aggregate row for all residential types; exclude it when summing subtypes.
- bygherre does NOT join cleanly to dim.bygherre. The codes used are: '10+30+40+90' (combined private builders), '20' (almene boligselskaber), '41' (private andelsboligforeninger), 'SK' (stat og kommuner), 'UOPL'. Only '20' and '41' match dim.bygherre. Query bygherre as inline codes, not via dim join.
- bygfase has 4 mutually exclusive phases — always filter to one when aggregating.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
