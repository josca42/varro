table: fact.bygv04
description: Den samlede byggeaktivitet (historisk oversigt) efter byggefase, anvendelse og tid
measure: indhold (unit M2)
columns:
- bygfase: values [30=Tilladt byggeri (1982 - ), 32=Påbegyndt byggeri (1949 - ), 34=Fuldførtbyggeri (1939 - ), 36=Byggeri under opførelse (1982 - )]
- anvend: join dim.byganv on anvend=kode [approx]; levels [1]
- tid: date range 1939-01-01 to 2024-01-01
dim docs: /dim/byganv.md
notes:
- Historical series from 1939 — the longest etageareal series in this subject. National totals only.
- bygfase codes are different from modern tables: 30=Tilladt, 32=Påbegyndt, 34=Fuldført, 36=Under opførelse (versus 1/2/3/4 in other tables). Always filter to one phase.
- anvend only has niveau 1 codes from dim.byganv (105=Beboelse, 205=Erhverv, 405=Øvrige) plus code '99' (total, not in dim). Filter `WHERE anvend != '99'` or treat '99' as the Denmark total row. Do NOT join to dim.byganv for niveau 2+ detail — it's not available here.
