table: fact.uheld6
description: Færdselsuheld med personskade efter uheldsart, uheldssituation, transportmiddel, antal transportmidler involveret og tid
measure: indhold (unit Antal)
columns:
- uhelda: values [0=Alle uheld, 1000=Spiritusuheld, 2000=Øvrige uheld]
- uheldsit: values [0=Eneuheld, 100=Indhentningsuheld, 200=Mødeuheld, 300=Svingningsuheld mellem medkørende, 400=Svingningsuheld mellem modkørende, 500=Uheld mellem krydsende køretøjer, 600=Svingningsuheld mellem krydsende køretøjer, 700=Parkeringsuheld, 800=Fodgængeruheld, 900=Forhindringsuheld, 999=Uoplyst]
- transmid: values [0=I alt, 11=Almindelig personbil, 12=Taxi, 13=Køretøj 0-3.500 kg under udrykning, 22=Varebil 0-2.000 kg, 23=Varebil 2.001-3.500 kg, 31=Lastbil over 3.500 kg., 34=Rutebus, 35=Bus i øvrigt, 42=Traktor, 41=Motorcykel, 45=Knallert 45, 51=Knallert med konstruktive ændringer, 52=Knallert i øvrigt, 61=Cykel, 62=El-cykler, 71=Fodgænger, 99=Andre]
- transinv: values [106=Et, 206=To, 306=Tre eller flere]
- tid: date range 2001-01-01 to 2024-01-01
notes:
- uhelda=0 and transmid=0 are aggregates — always filter both.
- uheldsit=0 means Eneuheld (single-vehicle), NOT a total.
- transinv has exactly 3 mutually exclusive values with no total code — sum all three to get the full count.
- Stored codes are 106/206/306 (not 1/2/3). Single-vehicle accidents: transinv='106'.
