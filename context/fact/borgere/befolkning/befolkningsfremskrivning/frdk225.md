table: fact.frdk225
description: Nøgletal 2025: Fremskrivning af befolkningens bevægelser efter herkomst, bevægelsesart og tid
measure: indhold (unit Antal)
columns:
- herkomst: join dim.herkomst on herkomst=kode [approx]
- bevaegelse: values [B01=Befolkningen primo, B02=Levendefødte, B03=Døde, B08=Indvandrede, B09=Udvandrede, B11=Befolkningstilvækst]
- tid: date range 2025-01-01 to 2070-01-01
dim docs: /dim/herkomst.md