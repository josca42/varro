table: fact.skolm11
description: Musikskolers samarbejde med ungdomsuddannelser og ungdomsskoler efter kommune, kunstart, nøgletal og tid
measure: indhold (unit Antal)
columns:
- komk: join dim.kommunegrupper on komk=kode; levels [2]
- kunstart: values [TOTK=Kunstart i alt, 1001=Musik, 1002=Visuel kunst, 1003=Håndværk og design, 1004=Scenekunst, 1005=Dans, 1006=Film og animation, 1007=Skrivekunst, 1008=Medier, 1009=Øvrige]
- bnogle: values [3050=Forløb, 3070=Deltagende elever, 3075=Undervisningstimer]
- tid: date range 2022 to 2025
dim docs: /dim/kommunegrupper.md

notes:
- komk joins dim.kommunegrupper at niveau 2. komk='0' is national total, not in the dim.
- bnogle is a measurement selector — 3050=Forløb, 3070=Deltagende elever, 3075=Undervisningstimer. Always filter to one bnogle value.
- kunstart='TOTK' is total across art forms.
- Map: context/geo/kommuner.parquet — merge on komk=dim_kode. Exclude komk=0.