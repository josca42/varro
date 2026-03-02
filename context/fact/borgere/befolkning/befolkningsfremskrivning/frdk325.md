table: fact.frdk325
description: Forudsætninger vedrørende fertilitet til befolkningsfremskrivningen 2025 efter alder, herkomst og tid
measure: indhold (unit Fertilitetskvotient)
columns:
- alder: values [TOT1=Samlet fertilitet, 15=15 år, 16=16 år, 17=17 år, 18=18 år ... 45=45 år, 46=46 år, 47=47 år, 48=48 år, 49=49 år]
- herkomst: join dim.herkomst on herkomst=kode::text [approx]
- tid: date range 2025-01-01 to 2069-01-01
dim docs: /dim/herkomst.md