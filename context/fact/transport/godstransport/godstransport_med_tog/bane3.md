table: fact.bane3
description: International jernbanetransport af gods efter retning, enhed, land og tid
measure: indhold (unit -)
columns:
- ret: values [TIL=Til Danmark fra udlandet, FRA=Fra Danmark til udlandet]
- enhed: values [75=1000 ton, 76=Mio. tonkm]
- land: join dim.lande_uhv on land=kode; levels [4]
- tid: date range 2000-01-01 to 2024-01-01
dim docs: /dim/lande_uhv.md

notes:
- land joins dim.lande_uhv at niveau=4 (individual countries). Use ColumnValues("lande_uhv", "titel", for_table="bane3") to see the ~23 countries that appear.
- Three land codes are not in dim.lande_uhv: IA=I ALT (total across all countries), OV=øvrige (other/unspecified countries), CS=historical code for former Czechoslovakia (appears 2001–2022, now replaced by CZ and SK). An INNER JOIN silently drops all three — this is usually correct for country-level breakdowns.
- To get the aggregate total: filter WHERE land='IA' instead of joining and summing. IA ≠ sum of joinable countries because OV is excluded from the join.
- ret has two values: TIL=til Danmark fra udlandet, FRA=fra Danmark til udlandet. Filter to one direction or aggregate both explicitly.
- enhed is a measurement selector: 75=1000 ton, 76=Mio. tonkm. Always filter to one.
- Annual data from 2000. Use this table for international rail freight breakdown by partner country.