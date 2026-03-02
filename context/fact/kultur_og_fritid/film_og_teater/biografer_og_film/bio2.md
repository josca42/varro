table: fact.bio2
description: Aktivitet i danske biografer efter biograffilm/billetter, nationalitet og tid
measure: indhold (unit -)
columns:
- bio: values [240=Foreviste film (antal), 250=Årets premierefilm (antal), 260=Solgte billetter (1.000), 270=Billetindtægt ekskl. moms (1.000 kr.)]
- nation2: values [TOT7=Alle lande, 00280=Danske, 00290=Europa udenfor Danmark, 00300=USA, 00310=Verden udenfor Europa og USA]
- tid: date range 1980-01-01 to 2024-01-01

notes:
- bio is a measurement selector — determines what indhold means. Filter to one: 240=Foreviste film (antal), 250=Årets premierefilm (antal), 260=Solgte billetter (1.000), 270=Billetindtægt ekskl. moms (1.000 kr.). Never sum across bio values.
- nation2 has TOT7=Alle lande as total. Sub-groups (Danske, Europa udenfor DK, USA, Øvrige) add up to TOT7.
- Longest time series for cinema activity: 1980–2024. Best table for historical ticket sales and revenue trends.