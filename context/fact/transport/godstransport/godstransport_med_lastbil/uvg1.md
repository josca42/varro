table: fact.uvg1
description: Vejgodstransport med udenlandsk lastbil efter enhed, registreringsland, kørselsart og tid
measure: indhold (unit -)
columns:
- enhed: values [70=Pålæsset godsmængde (1000 ton), 88=Transportarbejde (mio. tonkm)]
- reg: join dim.lande_psd on reg=kode [approx]; levels [3]
- korart: values [1100=I alt kørsel mellem Danmark og udlandet, 1150=Fra Danmark med lastbil til registreringsland, 1250=Til Danmark med lastbil fra registreringsland, 1255=Heraf tredjelandskørsel mellem Danmark og udland, 7001=Cabotagekørsel i Danmark]
- tid: date range 2000-01-01 to 2024-01-01
dim docs: /dim/lande_psd.md

notes:
- reg joins dim.lande_psd at niveau 3 (individual countries). Use ColumnValues("lande_psd", "titel", for_table="uvg1") to see the ~22 countries present. Join: JOIN dim.lande_psd d ON f.reg=d.kode AND d.niveau=3.
- Code 9999 = uoplyst (unknown registration country) — not in dim.lande_psd. Exclude or label manually.
- enhed has only 2 options: 70=godsmængde (1000 ton), 88=transportarbejde (mio. tonkm). Always filter to one.
- korart: 1100=I alt (total), 1150=Fra Danmark (outbound), 1250=Til Danmark (inbound), 1255=heraf tredjelandskørsel (subset of 1100), 7001=Cabotagekørsel (Denmark only). 1100 includes 1150+1250+1255. Don't sum 1100 with its children.
- This table only covers foreign-registered trucks. For Danish trucks doing international transport use the ivg* tables.