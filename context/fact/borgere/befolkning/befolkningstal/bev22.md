table: fact.bev22
description: Befolkningens udvikling (foreløbig opgørelse) efter område, bevægelsesart, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- bevaegelse: values [B01K=Befolkningen ultimo forrige kvartal, B02=Levendefødte, B03=Døde, B04=Fødselsoverskud, B05=Tilflyttede, B06=Fraflyttede, B07=Nettotilflyttede, B08AA=Indvandrede i alt, B08AK=Indvandret i indeværende kvartal, B08BK=Indvandret før indeværende kvartal, B09BA=Udvandrede i alt, B09AK=Udvandret i indeværende kvartal, B09BK=Udvandret før indeværende kvartal, B10=Nettoindvandrede, B12=Korrektioner, B11=Befolkningstilvækst, B20K=Befolkningen ultimo indeværende kvartal]
- kon: values [M=Mænd, K=Kvinder]
- tid: date range 2007-04-01 to 2025-04-01
dim docs: /dim/nuts.md

notes:
- Quarterly population movement (foreløbig/preliminary). omrade joins dim.nuts at niveau=3 only (99 kommuner — no national or regional aggregate rows).
- kon has only M/K (no total). Sum M+K to get both sexes.
- bevaegelse codes are NOT independent — several are derived sums: B04=Fødselsoverskud=B02-B03, B07=Nettotilflyttede=B05-B06, B10=Nettoindvandrede=B08AA-B09BA, B11=Befolkningstilvækst=B04+B07+B10+B12. B08AA=B08AK+B08BK, B09BA=B09AK+B09BK. Never sum all bevaegelse — pick the specific component(s) needed.
- B01K=start-of-quarter population, B20K=end-of-quarter population; their difference equals B11.
- Preliminary figures — for final annual data use bev107.
- ColumnValues("nuts", "titel", for_table="bev22") for municipality names.
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.