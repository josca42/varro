table: fact.ivg23
description: International vejgodstransport mellem lande efter enhed, pålæsningsland, aflæsningsland, godsart og tid
measure: indhold (unit -)
columns:
- maengde4: values [70=Pålæsset godsmængde (1000 ton), 80=Transportarbejde (1000 tonkm)]
- paland: join dim.lande_uhv on paland=kode [approx]; levels [4]
- afland: join dim.lande_uhv on afland=kode [approx]; levels [4]
- gods: values [100=GODS I ALT, 112=I alt, Landbrugs, skovbrugs,- og fiskeriprodukter, 122=I alt, Fødevarer, drikkevarer, tobak og foderstoffer, 132=I alt, Kul, koks, olie og kemiske produkter (inkl. gødning), 142=I alt, Malm, sten, grus, sand, ler, salt, cement, kalk og andre mineralske byggematerialer, 152=I alt, Stykgods, bearbejdede varer i øvrigt, 202=I containere/veksellad i alt, 212=I containere/veksellad, Landbrugs, skovbrugs,- og fiskeriprodukter, 222=I containere/veksellad, Fødevarer, drikkevarer, tobak og foderstoffer, 232=I containere/veksellad, Kul, koks, olie og kemiske produkter (inkl. gødning), 242=I containere/veksellad, Malm, sten, grus, sand, ler, salt, cement, kalk og andre mineralske byggematerialer, 252=I containere/veksellad, Stykgods, bearbejdede varer i øvrigt, 302=I anden lasttype, i alt, 312=I anden lasttype, Landbrugs, skovbrugs,- og fiskeriprodukter, 322=I anden lasttype, Fødevarer, drikkevarer, tobak og foderstoffer, 332=I anden lasttype, Kul, koks, olie og kemiske produkter (inkl. gødning), 342=I anden lasttype, Malm, sten, grus, sand, ler, salt, cement, kalk og andre mineralske byggematerialer, 352=I anden lasttype, Stykgods, bearbejdede varer i øvrigt]
- tid: date range 2008-01-01 to 2024-01-01
dim docs: /dim/lande_uhv.md

notes:
- maengde4 is a measurement selector (70=tons, 80=tonkm only — fewer options than ivg5). Filter to one.
- paland and afland join dim.lande_uhv at niveau 4 (individual countries). Use ColumnValues("lande_uhv", "titel", for_table="ivg23") to see available countries.
- Unmatched codes: DK=Danmark (reporting country), IA=Ikke angivet (unspecified), OV=Øvrige (other). Exclude these or handle manually when joining.
- gods has the same layered hierarchy as nvg23: 100=GODS I ALT, 112-152 are the 5 goods categories (sum to 100), 202-252 are the same 5 in containers (subset of 100), 302-352 in other load type (subset of 100). For goods totals by category use 112-152 only.
- Country-level goods origin-destination matrix from 2008. For longer time series without goods breakdown use ivg5.