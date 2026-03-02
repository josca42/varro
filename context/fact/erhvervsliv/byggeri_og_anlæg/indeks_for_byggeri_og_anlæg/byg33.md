table: fact.byg33
description: Byggeomkostningsindeks for boliger efter hovedindeks, art, enhed og tid
measure: indhold (unit -)
columns:
- hindeks: values [2=Byggeomkostningsindeks for enfamiliehuse, 3=Byggeomkostningsindeks for etageboliger]
- art: values [1002=I alt, 1004=Materialer, 1006=Arbejdsomkostninger]
- enhed: values [100=Indeks, 315=Ændring i forhold til året før (pct.)]
- tid: date range 2003-01-01 to 2024-01-01

notes:
- `enhed` is a measurement selector — every hindeks×art×tid combination appears twice (100=Indeks, 315=år-over-år pct). Always filter `enhed = 100` (index level) or `enhed = 315` (annual change).
- Annual frequency (month 1 only). Simpler than byg43/byg53 — no `dindeks` sub-component breakdown.
- `hindeks` has only 2 values: 2=Enfamiliehuse, 3=Etageboliger. There is no overall housing total in this table (unlike byg43/byg53 which have hindeks=1).
- `art` (1002=I alt, 1004=Materialer, 1006=Arbejdsomkostninger): 1002 is the combined total. Do not sum across art values.
- Data ends 2024. Use byg43 for current quarterly data or if the dindeks breakdown is needed.