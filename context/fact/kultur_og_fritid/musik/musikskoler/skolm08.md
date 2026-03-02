table: fact.skolm08
description: Korte projekter på musikskoler efter kommune, kunstart, nøgletal og tid
measure: indhold (unit Antal)
columns:
- komk: join dim.nuts on komk=kode; levels [3]
- kunstart: values [TOTK=Kunstart i alt, 1001=Musik, 1002=Visuel kunst, 1003=Håndværk og design, 1004=Scenekunst, 1005=Dans, 1006=Film og animation, 1007=Skrivekunst, 1008=Medier, 1009=Øvrige]
- bnogle: values [3035=Korte projekter, 3040=Dage, 3045=Deltagere, 3075=Undervisningstimer]
- tid: date range 2022 to 2025
dim docs: /dim/nuts.md

notes:
- komk joins dim.nuts at niveau 3. komk='0' is national total, not in the dim.
- bnogle is a measurement selector — 3035=Korte projekter (count), 3040=Dage (days), 3045=Deltagere (participants), 3075=Undervisningstimer (teaching hours). These are four distinct metrics. Always filter to one bnogle value.
- kunstart='TOTK' is the total across art forms.
- Map: context/geo/kommuner.parquet — merge on komk=dim_kode. Exclude komk=0.