table: fact.uheld9
description: Tilskadekomne og dræbte i færdselsuheld efter uheldsart, personskade, transportmiddel, personart, by/landområde, gade- eller vejtype og tid
measure: indhold (unit Antal)
columns:
- uhelda: values [0=Alle uheld, 1000=Spiritusuheld, 2000=Øvrige uheld]
- uheld: values [0=Personskade i alt, 1=Dræbte, 2=Alvorligt tilskadekomne, 3=Lettere tilskadekomne]
- transmid: values [0=I alt, 11=Almindelig personbil, 12=Taxi, 13=Køretøj 0-3.500 kg under udrykning, 22=Varebil 0-2.000 kg, 23=Varebil 2.001-3.500 kg, 31=Lastbil over 3.500 kg., 34=Rutebus, 35=Bus i øvrigt, 42=Traktor, 41=Motorcykel, 45=Knallert 45, 51=Knallert med konstruktive ændringer, 52=Knallert i øvrigt, 61=Cykel, 62=El-cykler, 71=Fodgænger, 99=Andre]
- persart: values [10=Motorfører, 40=knallertfører, 60=Fører af køretøj, hvor kørekort/knallertbevis ikke kræves, 70=Passager, 80=Fodgænger, 990=Uoplyst]
- byland: values [1=I byzone, 2=I landzone]
- gadevej: values [1=Motorvej, 2=Motortrafikvej, 3=Rampe ved motorvej o.lign, 4=4 spor, 5=3 spor, 9=2 spor, 55=1 spor, 56=Fartdæmpet vej, 7=Ensrettet vej, 15=Selvstændig sti, 16=Plads, 17=Fra/til ejendom, P-plads, 98=Andet]
- tid: date range 2001-01-01 to 2024-01-01
notes:
- uhelda=0, uheld=0, and transmid=0 are aggregates — filter all three.
- persart, byland, and gadevej have no total codes; all values are specific categories.
- persart: 10=Motorfører (car driver), 70=Passager, 80=Fodgænger. 990=Uoplyst (not a total).
- gadevej: codes are non-sequential (1, 2, 3, 4, 5, 9, 55, 56, 7, 15, 16, 17, 98). Use ColumnValues("uheld9", "gadevej") for the full labeled list.
- This table counts persons (not accidents). To count injuries on motorways: filter gadevej='1' (Motorvej) AND uhelda='0' AND uheld='0' AND transmid='0', then SUM(indhold).
