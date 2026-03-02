table: fact.bygv06
description: Gennemsnitligt samlet areal i nyopførte boliger (historisk oversigt) efter anvendelse og tid
measure: indhold (unit M2)
columns:
- anvend: join dim.byganv on anvend=kode [approx]; levels [2, 3]
- tid: date range 1916-01-01 to 2024-01-01
dim docs: /dim/byganv.md
notes:
- indhold is average square meters (m2) per new dwelling — not a total or count. Do not sum across anvend categories.
- anvend has legacy codes not in dim.byganv: '101' (private single-family homes, ~124 m2) and '104' (rækkehuse, ~230 m2). Only '120', '130', '140' match dim.byganv. Do not join to dim — use inline values.
- National totals only. Historical series from 1916 — useful for long-term trends in dwelling size.
