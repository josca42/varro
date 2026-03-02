table: fact.uheld4
description: Færdselsuheld med personskade efter uheldsart, transportmiddel, klokkeslet, ugedag, måned og tid
measure: indhold (unit Antal)
columns:
- uhelda: values [0=Alle uheld, 1000=Spiritusuheld, 2000=Øvrige uheld]
- transmid: values [0=I alt, 11=Almindelig personbil, 12=Taxi, 13=Køretøj 0-3.500 kg under udrykning, 22=Varebil 0-2.000 kg, 23=Varebil 2.001-3.500 kg, 31=Lastbil over 3.500 kg., 34=Rutebus, 35=Bus i øvrigt, 42=Traktor, 41=Motorcykel, 45=Knallert 45, 51=Knallert med konstruktive ændringer, 52=Knallert i øvrigt, 61=Cykel, 62=El-cykler, 71=Fodgænger, 99=Andre]
- klok: values [0001=00-01, 0102=01-02, 0203=02-03, 0304=03-04, 0405=04-05 ... 2021=20-21, 2122=21-22, 2223=22-23, 2324=23-24, UOPL=Uoplyst]
- uge: values [01=Mandag, 02=Tirsdag, 03=Onsdag, 04=Torsdag, 05=Fredag, 06=Lørdag, 07=Søndag, UOPL=Uoplyst]
- mnd: values [001=Januar, 002=Februar, 003=Marts, 004=April, 005=Maj, 006=Juni, 007=Juli, 008=August, 009=September, 010=Oktober, 011=November, 012=December, UOPL=Uoplyst]
- tid: date range 1997-01-01 to 2024-01-01
notes:
- uhelda=0 (Alle uheld) and transmid=0 (I alt) are both aggregates — filter each to one value or you silently multiply counts.
- klok, uge, and mnd have no total codes. Each row is a unique (klok×uge×mnd) time combination; the table is fully crossed but sparse (only non-zero combinations stored). Summing all rows with uhelda='0' and transmid='0' gives the correct yearly total.
- To analyse time-of-day: GROUP BY klok, SUM(indhold) WHERE uhelda='0' AND transmid='0'. Similarly for uge (day-of-week) or mnd (month). Do not cross two of these in the same GROUP BY without understanding the cross-product.
- klok codes are hour ranges like '0001'=midnight–1am, '1617'=4–5pm. ColumnValues("uheld4", "klok") returns the full list.
- This table counts accidents (not persons). Use uheld8–uheld11 for injured/killed persons.
