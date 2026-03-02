table: fact.frdk525
description: Forudsætninger vedrørende vandringer til befolkningsfremskrivningen 2025 efter køn, alder, herkomst, bevægelse og tid
measure: indhold (unit Antal)
columns:
- kon: values [1=Mænd, 2=Kvinder]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 106=106 år, 107=107 år, 108=108 år, 109=109 år, 110=110 år]
- herkomst: join dim.herkomst on herkomst=kode::text [approx]
- bevaegelsev: values [B08=Indvandrede, B09=Udvandrede]
- tid: date range 2025-01-01 to 2069-01-01
dim docs: /dim/herkomst.md