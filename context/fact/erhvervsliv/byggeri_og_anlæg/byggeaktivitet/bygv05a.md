table: fact.bygv05a
description: Det samlede boligbyggeri (historisk oversigt) efter byggefase, anvendelse og tid
measure: indhold (unit Antal)
columns:
- bygfase: values [20=Tilladt boliger (1981 -), 22=Påbegyndt boliger (1938 - ), 24=Fuldført boliger (1917 - ), 26=Boliger under opførelse (1981 - )]
- anvend: join dim.byganv on anvend=kode [approx]; levels [2, 3]
- tid: date range 1917-01-01 to 2024-01-01
dim docs: /dim/byganv.md
notes:
- Historical series from 1917 — the longest boligbyggeri (antal) series in this subject. National totals only.
- bygfase codes are different from modern tables: 20=Tilladt, 22=Påbegyndt, 24=Fuldført, 26=Under opførelse (versus 1/2/3/4 in other tables). Always filter to one phase.
- anvend has legacy codes not in dim.byganv: '9' (old total for all housing), '116' (old residential category, predecessor to codes 110-120), '10000' (recent total code). Only '130' and '140' match dim.byganv. Do not join to dim — use inline values. '9' and '10000' are totals; '116', '130', '140' are subcategories.
- The mix of old codes ('9', '116') in early years and newer codes ('10000') in recent years means time series analysis requires handling the coding change.
