table: fact.frld225
description: Nøgletal 2025: Fremskrivning af befolkningens bevægelser efter landsdel, bevægelsesart og tid
measure: indhold (unit Antal)
columns:
- landsdel: join dim.nuts on landsdel=kode; levels [2]
- bevaegelse: values [B01=Befolkningen primo, B02=Levendefødte, B03=Døde, B05=Tilflyttede, B06=Fraflyttede, B11=Befolkningstilvækst]
- tid: date range 2025-01-01 to 2050-01-01
dim docs: /dim/nuts.md

notes:
- Map: context/geo/landsdele.parquet — merge on landsdel=dim_kode. Exclude landsdel=0.