table: fact.frkm225
description: Nøgletal 2025: Fremskrivning af befolkningens bevægelser efter kommune, bevægelsesart og tid
measure: indhold (unit Antal)
columns:
- kommunedk: join dim.nuts on kommunedk=kode; levels [3]
- bevaegelse: values [B01=Befolkningen primo, B02=Levendefødte, B03=Døde, B05=Tilflyttede, B06=Fraflyttede, B11=Befolkningstilvækst]
- tid: date range 2025-01-01 to 2050-01-01
dim docs: /dim/nuts.md

notes:
- Map: /geo/kommuner.parquet — merge on kommunedk=dim_kode. Exclude kommunedk=0.