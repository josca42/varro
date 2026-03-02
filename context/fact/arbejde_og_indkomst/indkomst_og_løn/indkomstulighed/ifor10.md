table: fact.ifor10
description: Lavindkomst grænse.  Månedlige disponible indkomst efter voksne 15 år og derover, børn under 15 år, indkomstniveau og tid
measure: indhold (unit Kr. pr. familie)
columns:
- voksne: values [V1=1 Voksen, V2=2 Voksne, V3=3 Voksne, V4=4 Voksne, V5=5 Voksne, V6=6 Voksne]
- boern: values [0=0 børn, 1=1 barn, 2=2 børn, 3=3 børn, 4=4 børn, 5=5 børn, 6=6 børn]
- indkn: values [50=50 procent af medianindkomsten, 60=60 procent af medianindkomsten]
- tid: date range 1987-01-01 to 2023-01-01
notes:
- This table gives the low-income threshold (Kr. pr. familie per month) — not a count of people, but the income cutoff level itself. Use it to find "where is the poverty line for a family of 2 adults + 2 children?"
- voksne and boern fully specify the family composition. Every combination of voksne x boern x indkn is a separate threshold. There is no "total" row — each row is a distinct family type.
- indkn selects the threshold definition: '50' = 50% of median, '60' = 60% of median (EU standard). Filter to one.
- To look up the threshold for a specific family type: WHERE voksne = 'V2' AND boern = '2' AND indkn = '60' AND tid = '2023-01-01'.
