table: fact.ivg5
description: International vejgodstransport efter enhed, startland, slutland og tid
measure: indhold (unit -)
columns:
- maengde4: values [10=Ture i alt, 1000, 20=Ture med læs, 1000, 30=Ture uden læs, 1000, 40=Kørte km i alt, 1000 km, 50=Kørte km med læs, 1000 km, 60=Kørte km uden læs, 1000 km, 70=Pålæsset godsmængde (1000 ton), 80=Transportarbejde (1000 tonkm)]
- start1: join dim.lande_uhv on start1=kode [approx]; levels [4]
- slut1: join dim.lande_uhv on slut1=kode [approx]; levels [4]
- tid: date range 1999-01-01 to 2024-01-01
dim docs: /dim/lande_uhv.md

notes:
- maengde4 is a measurement selector (8 options, trips to tonkm). Filter to one.
- start1 and slut1 join dim.lande_uhv at niveau 4 (individual countries). Use ColumnValues("lande_uhv", "titel", for_table="ivg5") to see which countries are present.
- Unmatched codes: CS=Tjekkoslovakiet (historical code, pre-1993 data), DK=Danmark (reporting country, not in dim), IA=Ikke angivet (unspecified origin/destination), OV=Øvrige (residual "other" category). Filter these out or handle manually when joining dim.
- This is an origin-destination matrix at country level. For the full matrix: WHERE maengde4='70' and exclude aggregates (DK/IA/OV) or handle them as special cases.
- For country-level goods breakdown use ivg23 instead (has gods column but fewer enhed options).