table: fact.uheld5
description: Færdselsuheld med personskade efter uheldsart, uheldssituation, transportmiddel, modpart og tid
measure: indhold (unit Antal)
columns:
- uhelda: values [0=Alle uheld, 1000=Spiritusuheld, 2000=Øvrige uheld]
- uheldsit: values [0=Eneuheld, 100=Indhentningsuheld, 200=Mødeuheld, 300=Svingningsuheld mellem medkørende, 400=Svingningsuheld mellem modkørende, 500=Uheld mellem krydsende køretøjer, 600=Svingningsuheld mellem krydsende køretøjer, 700=Parkeringsuheld, 800=Fodgængeruheld, 900=Forhindringsuheld, 999=Uoplyst]
- transmid: values [0=I alt, 11=Almindelig personbil, 12=Taxi, 13=Køretøj 0-3.500 kg under udrykning, 22=Varebil 0-2.000 kg, 23=Varebil 2.001-3.500 kg, 31=Lastbil over 3.500 kg., 34=Rutebus, 35=Bus i øvrigt, 42=Traktor, 41=Motorcykel, 45=Knallert 45, 51=Knallert med konstruktive ændringer, 52=Knallert i øvrigt, 61=Cykel, 62=El-cykler, 71=Fodgænger, 99=Andre]
- modpart: values [0=I alt, 11=Almindelig personbil, 12=Taxi, 13=Køretøj 0-3.500 kg under udrykning, 22=Varebil 0-2.000 kg, 23=Varebil 2.001-3.500 kg, 31=Lastbil over 3.500 kg., 34=Rutebus, 35=Bus i øvrigt, 42=Traktor, 41=Motorcykel, 45=Knallert 45, 51=Knallert med konstruktive ændringer, 52=Knallert i øvrigt, 61=Cykel, 71=Fodgænger, 99=Andre, 80=forhindring, 90=Ingen modpart]
- tid: date range 2001-01-01 to 2024-01-01
notes:
- uhelda=0, transmid=0, and modpart=0 are all aggregate totals — filter all three to avoid overcounting.
- uheldsit=0 means Eneuheld (single-vehicle), NOT a total.
- For single-vehicle accidents, modpart='90' (Ingen modpart). For pedestrian collisions: transmid='71' or modpart='71'.
- modpart has two extra codes not in transmid: '80'=forhindring (obstacle hit) and '90'=Ingen modpart (no counterpart).
