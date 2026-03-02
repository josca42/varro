table: fact.nvg23
description: National vejgodstransport mellem regioner efter enhed, pålæsningsregion, aflæsningsregion, godsart og tid
measure: indhold (unit -)
columns:
- enhed: values [10=Ture i alt, 1000, 20=Ture med læs, 1000, 30=Ture uden læs, 1000, 40=Kørte km i alt, 1000 km, 50=Kørte km med læs, 1000 km, 60=Kørte km uden læs, 1000 km, 70=Pålæsset godsmængde (1000 ton), 80=Transportarbejde (1000 tonkm)]
- paregion: join dim.nuts on paregion=kode; levels [2]
- afregion: join dim.nuts on afregion=kode; levels [2]
- gods: values [100=GODS I ALT, 112=I alt, Landbrugs, skovbrugs,- og fiskeriprodukter, 122=I alt, Fødevarer, drikkevarer, tobak og foderstoffer, 132=I alt, Kul, koks, olie og kemiske produkter (inkl. gødning), 142=I alt, Malm, sten, grus, sand, ler, salt, cement, kalk og andre mineralske byggematerialer, 152=I alt, Stykgods, bearbejdede varer i øvrigt, 202=I containere/veksellad i alt, 212=I containere/veksellad, Landbrugs, skovbrugs,- og fiskeriprodukter, 222=I containere/veksellad, Fødevarer, drikkevarer, tobak og foderstoffer, 232=I containere/veksellad, Kul, koks, olie og kemiske produkter (inkl. gødning), 242=I containere/veksellad, Malm, sten, grus, sand, ler, salt, cement, kalk og andre mineralske byggematerialer, 252=I containere/veksellad, Stykgods, bearbejdede varer i øvrigt, 302=I anden lasttype, i alt, 312=I anden lasttype, Landbrugs, skovbrugs,- og fiskeriprodukter, 322=I anden lasttype, Fødevarer, drikkevarer, tobak og foderstoffer, 332=I anden lasttype, Kul, koks, olie og kemiske produkter (inkl. gødning), 342=I anden lasttype, Malm, sten, grus, sand, ler, salt, cement, kalk og andre mineralske byggematerialer, 352=I anden lasttype, Stykgods, bearbejdede varer i øvrigt]
- tid: date range 2008-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- paregion and afregion join dim.nuts at niveau 2 only (11 landsdele). Use ColumnValues("nuts", "titel", for_table="nvg23") to see the 11 available regions. Code 0 = "alle regioner" (total across all regions) — not in dim.nuts; handle as aggregate.
- enhed is a measurement selector — every origin/destination/gods combination repeats per enhed. Filter to one value before summing.
- gods has a layered hierarchy: 100=GODS I ALT (total), 112-152 are the 5 goods categories (these 5 sum to 100), 202-252 are the same 5 goods in containers (subset of 100), 302-352 are the same 5 in other load type (subset of 100). The 100/1xx/2xx/3xx groups are overlapping. For total goods by category use 112-152; for container breakdown use 202-252.
- For a clean origin-destination matrix: WHERE gods='100' AND enhed='70' AND paregion != '0' AND afregion != '0' gives 11×11 landsdel-level cells.
- Join example: JOIN dim.nuts pa ON f.paregion=pa.kode AND pa.niveau=2 JOIN dim.nuts af ON f.afregion=af.kode AND af.niveau=2
- Map: context/geo/landsdele.parquet (niveau 2) — merge on paregion=dim_kode or afregion=dim_kode. Exclude code 0. OD table; aggregate by one dimension for choropleth.