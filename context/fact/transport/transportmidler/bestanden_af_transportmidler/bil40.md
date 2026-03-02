table: fact.bil40
description: Fremskrivning af personbilbestand efter bestanddele og tid
measure: indhold (unit -)
columns:
- bestanddel: values [605=Nyregistreringer (antal), 625=Bestand (antal), 655=Nettotilgang (procent), 660=Afgang (procent)]
- tid: date range 2025-01-01 to 2029-01-01

notes:
- This is a projection/forecast table (fremskrivning), not historical data. Values are model estimates for 2025–2029.
- bestanddel mixes absolute counts and percentages in the same column: 605=Nyregistreringer (antal), 625=Bestand (antal), 655=Nettotilgang (procent), 660=Afgang (procent). Always filter to one bestanddel — summing across them is meaningless.
- For projected stock size: WHERE bestanddel=625. For new registrations: WHERE bestanddel=605.