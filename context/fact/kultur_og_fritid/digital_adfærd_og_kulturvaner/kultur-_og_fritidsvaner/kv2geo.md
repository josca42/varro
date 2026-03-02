table: fact.kv2geo
description: Forbrug af kulturaktiviteter efter kulturaktivitet, kommune og tid
measure: indhold (unit Pct.)
columns:
- kultur: values [10100=Har set film, 10200=Har set serier, 10300=Har lyttet til musik, 10400=Har læst eller lyttet til bøger, 10500=Har læst, lyttet til eller set nyheder, 10600=Har brugt sociale medier, 10700=Har spillet digitale spil, 10800=Har dyrket sport eller motion, 20100=Har været i biografen, 20200=Har været til koncert eller musikfestival, 20300=Har set scenekunst eller sceneforestillinger live, på internettet eller i TV, 20400=Har opsøgt billedkunst fysisk eller digitalt, 20500=Har været fysisk på biblioteket, 20600=Har benyttet bibliotekernes digitale tjenester, 20700=Har overværet sportsbegivenhed som tilskuer, 20800=Har været på museum, 20900=Har besøgt dansk kulturarv]
- kommunedk: join dim.nuts on kommunedk=kode; levels [1, 2, 3]
- tid: date range 2024-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- kommunedk joins dim.nuts but contains codes at all three NUTS hierarchy levels simultaneously: niveau 1 (5 regioner), niveau 2 (11 landsdele), niveau 3 (99 kommuner), plus kommunedk=0 (national total, not in dim). Always filter by d.niveau when joining to avoid mixing levels.
- kommunedk=0 is the national aggregate — it is not in dim.nuts and will be dropped by an inner join. Use a LEFT JOIN and handle NULL d.titel if you need the national row, or filter WHERE f.kommunedk != 0 before joining.
- Example for kommune level: JOIN dim.nuts d ON f.kommunedk=d.kode WHERE d.niveau=3
- Only 2024 annual data; no breakdown by kon/alder — each (kultur, kommunedk) cell represents the population-wide rate.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on kommunedk=dim_kode. Exclude kommunedk=0.
