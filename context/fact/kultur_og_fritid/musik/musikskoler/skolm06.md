table: fact.skolm06
description: Talentelever på musikskoler efter kommune, kunstart og tid
measure: indhold (unit Antal)
columns:
- komk: join dim.nuts on komk=kode [approx]; levels [3]
- kunstart: values [TOTK=Kunstart i alt, 1001=Musik, 1002=Visuel kunst, 1003=Håndværk og design, 1004=Scenekunst, 1005=Dans, 1006=Film og animation, 1007=Skrivekunst, 1008=Medier, 1009=Øvrige]
- tid: date range 2022 to 2025
dim docs: /dim/nuts.md

notes:
- komk joins dim.nuts at niveau 3 (99 kommuner, approx match). komk='0' is national total, komk='99' is an unspecified/residual code (only 4 rows in data) — both are not in the dim.
- kunstart='TOTK' is the total across all art forms. Use kunstart='1001' for music specifically.
- Only from 2022 — use for talent student counts broken down by art form and municipality.
- Map: context/geo/kommuner.parquet — merge on komk=dim_kode. Exclude komk=0 and komk=99.