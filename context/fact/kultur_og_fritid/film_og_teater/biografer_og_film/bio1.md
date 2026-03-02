table: fact.bio1
description: Danske biografer, biografsale og faste siddepladser efter biografer/sale/sæder, biografstørrelse og tid
measure: indhold (unit Antal)
columns:
- sader: values [180=Biografer, 190=Biografsale, 200=Sæder (1.000), 210=Sæder pr. biografsal]
- biograf: values [TOT6=Alle biografer, 00220=Ensalsbiograf, 00230=Flersalsbiograf]
- tid: date range 1980-01-01 to 2024-01-01

notes:
- sader is a measurement selector — each row exists once per sader value. Filter to one: 180=Biografer (count of theaters), 190=Biografsale (count of screens), 200=Sæder 1.000 (total seat capacity), 210=Sæder pr. biografsal (avg seats per screen). Never sum across sader values.
- biograf has TOT6=Alle as total; the two sub-types (ensals/flersals) add up to TOT6. Simple filter.
- Longest time series for cinema infrastructure: 1980–2024. Use for trend analysis on how many cinemas/screens exist.