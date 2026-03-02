table: fact.ligelb1
description: Lønniveau efter arbejdssted/bopæl, område, alder, køn, familietype og tid
measure: indhold (unit Kr.)
columns:
- arbbop: values [AK=Arbejdsstedskommune, BK=Bopælskommune]
- omrade: join dim.nuts on omrade=kode; levels [3]
- alder: values [TOT=Alder i alt, 1319=13-19 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6099=60 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- famtyp: values [TOT=I alt, EUHB=Enlige uden hjemmeboende børn, EMHB=Enlige med hjemmeboende børn, PUHB=Par uden hjemmeboende børn, PMHB=Par med hjemmeboende børn]
- tid: date range 2009-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at niveau 3 (98 municipalities). Code "0" is the national total — not in dim.nuts. Use ColumnValues("nuts", "titel", for_table="ligelb1") to see the 98 available municipalities. Join with WHERE d.niveau = 3.
- arbbop is a view selector: AK=arbejdsstedskommune (where you work), BK=bopælskommune (where you live). Each municipality appears twice in the data — once for each perspective. Always filter arbbop to one value: WHERE arbbop='AK' for economic geography, WHERE arbbop='BK' for residential geography. Forgetting this doubles the row count.
- alder is a flat 7-band column: TOT=all, then 1319/2029/3039/4049/5059/6099. Filter alder='TOT' for all ages.
- famtyp: TOT=all, EUHB=single no kids, EMHB=single with kids, PUHB=couple no kids, PMHB=couple with kids. Filter to TOT for overall.
- kon: TOT=all, M=men, K=women.
- To get average pay by municipality: WHERE arbbop='AK' AND alder='TOT' AND kon='TOT' AND famtyp='TOT', GROUP BY omrade + join dim.nuts.
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.
