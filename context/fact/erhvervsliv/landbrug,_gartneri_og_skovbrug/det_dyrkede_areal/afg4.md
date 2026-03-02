table: fact.afg4
description: Bedrifter med korn efter område(2), bedriftstype, areal og tid
measure: indhold (unit -)
columns:
- omr2: join dim.landbrugslandsdele on omr2=kode [approx]
- bedrift: values [1000=Bedrifter i alt, 1002=Bedrifter hvor hvede dominerer, 1004=Bedrifter hvor rug dominerer, 1007=Bedrifter hvor byg dominerer, 1008=Bedrifter hvor havre dominerer, 1011=Andre bedrifter med korn, 1012=Bedrifter uden korn]
- areal1: values [400=Antal bedrifter, 402=Areal med hvede (ha), 404=Areal med rug (ha), 406=Areal med byg (ha), 408=Areal med havre (ha), 410=Areal med triticale og andet korn til modenhed (ha), 412=Areal med korn i alt (ha), 414=Areal i alt (ha)]
- tid: date range 1982-01-01 to 2024-01-01
dim docs: /dim/landbrugslandsdele.md
notes:
- omr2 does NOT join to dim.landbrugslandsdele. Only 4 values: 000=Hele landet, L3=Jylland, 1580=Fyn, 002=Øst for Storebælt (Sjælland + Bornholm). Very coarse 3-way regional split. Use ColumnValues("afg4","omr2") directly — no dim join needed.
- bedrift is the farm type classified by which grain dominates: 1000=Bedrifter i alt, 1002=Hvede dominerer, 1004=Rug dominerer, 1007=Byg dominerer, 1008=Havre dominerer, 1011=Andre bedrifter med korn, 1012=Bedrifter uden korn. Filter to 1000 for all farms.
- areal1 is a measurement selector (not a size class): 400=Antal bedrifter, 402=Areal med hvede (ha), 404=Areal med rug (ha), 406=Areal med byg (ha), 408=Areal med havre (ha), 410=Areal med triticale og andet korn (ha), 412=Areal med korn i alt (ha), 414=Areal i alt (ha). Always filter to one areal1 value — summing across them mixes counts and hectares.
- Both bedrift and areal1 must be filtered to avoid double-counting. Example — total grain area nationally in 2024: SELECT indhold FROM fact.afg4 WHERE tid='2024-01-01' AND omr2='000' AND bedrift=1000 AND areal1=412.
