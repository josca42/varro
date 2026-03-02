table: fact.flow2
description: Befolkningens skift af socioøkonomisk status efter bopælskommune, tidligere socioøkonomisk status, ny socioøkonomisk status, bevægelse, køn, alder og tid
measure: indhold (unit Antal)
columns:
- bopkom: join dim.nuts on bopkom=kode; levels [1, 2, 3]
- tidsocio: values [0=Beskæftigede, 50=Arbejdsløse, 55=Uden for arbejdsstyrken]
- nysocio: values [0=Beskæftigede, 50=Arbejdsløse, 55=Uden for arbejdsstyrken, 60=Ikke i befolkningen]
- bevaegelsev: values [1-2KVT=1. kvartal til 2. kvartal, 2-3KVT=2. kvartal til 3. kvartal, 3-4KVT=3. kvartal til 4. kvartal]
- kon: values [M=Mænd, K=Kvinder]
- alder: values [-16=Under 16 år, 16-19=16-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, OV69=Over 69]
- tid: date range 2020-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- bopkom joins dim.nuts on bopkom=kode — 100% match (no aggregate '0' code). Use ColumnValues("nuts", "titel", for_table="flow2") to see available municipalities.
- dim.nuts has 5 regioner (niveau 1), 11 landsdele (niveau 2), 99 kommuner (niveau 3). Filter WHERE d.niveau = 3 to get municipality level.
- bevaegelsev represents different quarter-transitions (1-2KVT, 2-3KVT, 3-4KVT) — not duplicates. See flow1 notes for semantics.
- tidsocio/nysocio are simplified to 3 values (0=Beskæftigede, 50=Arbejdsløse, 55=Uden for arbejdsstyrken) unlike flow1's 9 categories. nysocio adds 60=Ikke i befolkningen.
- kon has NO total row (only M and K).
- Short time series: only 2020–2023.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on bopkom=dim_kode.