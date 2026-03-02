table: fact.bygv01
description: Landstal for den samlede byggeaktivitet (ikke korrigeret for forsinkelser) efter byggefase, anvendelse, bygherreforhold og tid
measure: indhold (unit M2)
columns:
- bygfase: values [2=Påbegyndt byggeri, 3=Fuldført byggeri, 4=Byggeri under opførelse, 1=Tilladt byggeri]
- anvend: join dim.byganv on anvend=kode::text [approx]; levels [2, 3]
- bygherre: join dim.bygherre on bygherre=kode::text [approx]; levels [2]
- tid: date range 1982-01-01 to 2024-01-01
dim docs: /dim/byganv.md, /dim/bygherre.md
notes:
- National totals only — no regional breakdown. For regional data use bygv11 (from 2006). bygv01 goes back to 1982.
- anvend joins dim.byganv at niveauer 2 and 3. Code 'UOPL' is not in the dim.
- bygherre joins dim.bygherre at niveau 2 only. Code 'UOPL' is not in the dim. Niveau 1 codes (1, 2, 3) are absent.
- bygfase has 4 mutually exclusive phases — always filter to one when aggregating.
