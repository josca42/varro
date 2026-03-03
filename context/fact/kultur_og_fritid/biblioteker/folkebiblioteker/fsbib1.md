table: fact.fsbib1
description: Folkeskolebibliotekernes nøgletal efter kommune, nøgletal og tid
measure: indhold (unit Antal)
columns:
- kommunedk: join dim.nuts on kommunedk=kode; levels [3]
- bnogle: values [15110=Udlån i alt, 15120=Udlån. Bøger, 15130=Udlån. Lydbøger, 15140=Udlån. Musikoptagelser, 15150=Udlån. Levende billeder, 15160=Udlån. Multimediematerialer, 15170=Udlån. Andre materialer, 15175=Udlån. Seriepublikationer, 15180=Bestand i alt, 15190=Bestand. Bøger, 15200=Bestand. Lydbøger, 15210=Bestand. Musikoptagelser, 15220=Bestand. Levende billeder, 15230=Bestand. Multimediematerialer, 15240=Bestand. Andre materialer, 15245=Bestand. Seriepublikationer (abonnementer), 10170=Aktive personlige lånere (i 1.000), 10175=Aktive betjeningssteder (2024-)]
- tid: date range 2022-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- School library (folkeskolebibliotek) stats — different from public libraries (folkebiblioteker). Only 3 years of data (2022-2024).
- kommunedk joins dim.nuts at niveau 3 only (97 kommuner). kommunedk=0 = Hele landet. No regional (niveau 1) grouping in this table.
- bnogle: 19 metric codes same as bib1 plus 10170=Aktive personlige lånere and 10175=Aktive betjeningssteder (2024-). Always filter to one bnogle.
- For national folkebibliotek stats use bib1; use fsbib1 only when specifically asked about school libraries.
- Map: /geo/kommuner.parquet — merge on kommunedk=dim_kode. Exclude kommunedk=0.
