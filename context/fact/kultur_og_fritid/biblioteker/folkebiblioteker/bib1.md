table: fact.bib1
description: Folkebibliotekernes nøgletal efter område, nøgletal og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- bnogle: values [15110=Udlån i alt, 15120=Udlån. Bøger, 15130=Udlån. Lydbøger, 15140=Udlån. Musikoptagelser, 15150=Udlån. Levende billeder, 15160=Udlån. Multimediematerialer, 15170=Udlån. Andre materialer, 15175=Udlån. Seriepublikationer, 15180=Bestand i alt, 15190=Bestand. Bøger, 15200=Bestand. Lydbøger, 15210=Bestand. Musikoptagelser, 15220=Bestand. Levende billeder, 15230=Bestand. Multimediematerialer, 15240=Bestand. Andre materialer, 15245=Bestand. Seriepublikationer (abonnementer), 15250=Brug af elektroniske ressourcer (downloads), 15260=Materialeudgifter (1.000 kr.)]
- tid: date range 2009-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts. Use ColumnValues("nuts", "titel", for_table="bib1") to see available areas. niveau 1 = 5 regioner, niveau 3 = 97 kommuner. omrade=0 means "Hele landet" (not in dim.nuts — use WHERE omrade='0' directly).
- bnogle is a metric selector, not a category to sum across. Each bnogle code is a separate KPI (loans, holdings, expenses). Always filter to a single bnogle value.
- Code 15260 (Materialeudgifter) is in 1.000 kr., not Antal — the unit header is misleading for this one code.
- Typical query: SELECT tid, d.titel, f.indhold FROM fact.bib1 f JOIN dim.nuts d ON f.omrade=d.kode WHERE f.bnogle='15110' AND d.niveau=1 ORDER BY tid.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
