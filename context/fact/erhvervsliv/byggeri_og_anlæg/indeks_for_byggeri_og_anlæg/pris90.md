table: fact.pris90
description: Producentprisindeks for byggeri af boliger efter boligtype, enhed og tid
measure: indhold (unit Indeks)
columns:
- boltyp: join dim.ejendom on boltyp=kode; levels [1, 2]
- enhed: values [100=Indeks, 210=Ændring i forhold til kvartalet før (pct.)]
- tid: date range 2015-01-01 to 2025-04-01
dim docs: /dim/ejendom.md

notes:
- `enhed` is a measurement selector — every boltyp×tid combination appears twice (100=Indeks, 210=kvartal-over-kvartal pct). Always filter to the enhed you need.
- Quarterly frequency (months 1, 4, 7, 10). Shortest history in this subject: only from 2015.
- `boltyp` only contains code 111 (Enfamiliehuse). Despite the dim.ejendom join, this table effectively covers a single housing type. No need to filter on boltyp beyond confirming the only value.
- CRITICAL dim join gotcha: dim.ejendom has kode=111 at both niveau=1 and niveau=2 (identical title). Joining without `WHERE d.niveau = 1` will double every row. Always add `AND d.niveau = 1` to the join condition.