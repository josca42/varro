table: fact.skolm09
description: Musikskolers samarbejde med dagtilbud efter kommune, kunstart, aldersgruppe, nøgletal og tid
measure: indhold (unit Antal)
columns:
- komk: join dim.nuts on komk=kode; levels [3]
- kunstart: values [TOTK=Kunstart i alt, 1001=Musik, 1002=Visuel kunst, 1003=Håndværk og design, 1004=Scenekunst, 1005=Dans, 1006=Film og animation, 1007=Skrivekunst, 1008=Medier, 1009=Øvrige]
- agebygroup: values [TOT=Alder i alt, V02=0-2 år (vuggestue), B36=3-6 år (børnehave)]
- bnogle: values [3050=Forløb, 3055=Deltagende børn, 3075=Undervisningstimer]
- tid: date range 2022 to 2025
dim docs: /dim/nuts.md

notes:
- komk joins dim.nuts at niveau 3. komk='0' is national total, not in the dim.
- bnogle is a measurement selector — 3050=Forløb (sessions/courses), 3055=Deltagende børn (participating children), 3075=Undervisningstimer (teaching hours). Always filter to one bnogle value.
- agebygroup='TOT' is total across age groups. V02=vuggestue (0-2 yr), B36=børnehave (3-6 yr). These are non-overlapping; summing V02+B36 = TOT.
- Map: /geo/kommuner.parquet — merge on komk=dim_kode. Exclude komk=0.