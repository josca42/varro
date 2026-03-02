table: fact.uheld11
description: Tilskadekomne og dræbte i færdselsuheld efter uheldsart, personskade, transportmiddel, i/udenfor transportmidlet, personart, spirituspåvirkning og tid
measure: indhold (unit Antal)
columns:
- uhelda: values [0=Alle uheld, 1000=Spiritusuheld, 2000=Øvrige uheld]
- uheld: values [0=Personskade i alt, 1=Dræbte, 2=Alvorligt tilskadekomne, 3=Lettere tilskadekomne]
- transmid: values [0=I alt, 11=Almindelig personbil, 12=Taxi, 13=Køretøj 0-3.500 kg under udrykning, 22=Varebil 0-2.000 kg, 23=Varebil 2.001-3.500 kg, 31=Lastbil over 3.500 kg., 34=Rutebus, 35=Bus i øvrigt, 42=Traktor, 41=Motorcykel, 45=Knallert 45, 51=Knallert med konstruktive ændringer, 52=Knallert i øvrigt, 61=Cykel, 62=El-cykler, 71=Fodgænger, 99=Andre]
- iudenfor: values [101=I transportmidlet, 201=Udenfor transportmidlet]
- persart: values [10=Motorfører, 40=knallertfører, 60=Fører af køretøj, hvor kørekort/knallertbevis ikke kræves, 70=Passager, 80=Fodgænger, 990=Uoplyst]
- spirit: values [104=Spirituspåvirket, 204=Ikke spirituspåvirket]
- tid: date range 2001-01-01 to 2024-01-01
notes:
- uhelda=0, uheld=0, and transmid=0 are aggregates — filter all three.
- iudenfor, persart, and spirit have no total codes; all values are specific and exhaustive.
- spirit: only 2 values (104=Spirituspåvirket / 204=Ikke spirituspåvirket) — mutually exclusive, no total. Sum both to get all injured.
- iudenfor: only 2 values (101=I transportmidlet / 201=Udenfor transportmidlet). Useful for e.g. pedestrian (udenfor) vs passenger (i) analysis.
- persart=990=Uoplyst is not a total.
