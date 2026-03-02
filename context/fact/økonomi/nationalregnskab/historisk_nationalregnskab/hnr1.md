table: fact.hnr1
description: Syntetisk forhistorie for det aktuelle nationalregnskabs tal efter version, transaktion, prisenhed og tid
measure: indhold (unit Mio. kr.)
columns:
- version: values [1=1. Version, 2=2. Version, 3=3. Version, 4=4. Version, 5=5. Version, 6=6. Version, 7=7. Version, 8=8. Version, 9=9. Version, 10=10. Version]
- transakt: values [101=Bruttonationalprodukt (BNP), 102=Bruttonationalindkomst (BNI), 103=Bruttofaktorindkomst (BFI), 104=Nettonationalprodukt (NNP), 105=Nettonationalindkomst (NNI), 106=Nettofaktorindkomst (NFI), 107=Forbrug af fast realkapital (afskrivninger)]
- prisenhed: values [401=Løbende priser, 410=Kædede værdier, 2010-priser]
- tid: date range 1930-01-01 to 2024-01-01

notes:
- Despite the doc listing 10 versions and 2 prisenhed values, the table in practice only contains version=1 and prisenhed=401 (Løbende priser). Do not filter on these columns — they have no variation.
- Only transakt=101 (BNP) covers the full 1930–2024 range. All other transakt values (102–107) only go back to 1966.
- This table is a synthetic unified backcast ("syntetisk forhistorie") using the current national accounts methodology. Values will differ from vhnr, which preserves the original figures from each historical accounting regime.
- To get a clean annual BNP series: SELECT tid, indhold FROM fact.hnr1 WHERE transakt=101 ORDER BY tid.