table: fact.uheld8
description: Tilskadekomne og dræbte i færdselsuheld efter uheldsart, personskade, transportmiddel, køn, alder, skadens type og tid
measure: indhold (unit Antal)
columns:
- uhelda: values [0=Alle uheld, 1000=Spiritusuheld, 2000=Øvrige uheld]
- uheld: values [0=Personskade i alt, 1=Dræbte, 2=Alvorligt tilskadekomne, 3=Lettere tilskadekomne]
- transmid: values [0=I alt, 11=Almindelig personbil, 12=Taxi, 13=Køretøj 0-3.500 kg under udrykning, 22=Varebil 0-2.000 kg, 23=Varebil 2.001-3.500 kg, 31=Lastbil over 3.500 kg., 34=Rutebus, 35=Bus i øvrigt, 42=Traktor, 41=Motorcykel, 45=Knallert 45, 51=Knallert med konstruktive ændringer, 52=Knallert i øvrigt, 61=Cykel, 62=El-cykler, 71=Fodgænger, 99=Andre]
- koen: values [0=I alt, 1=Mænd, 2=Kvinder, 9=Uoplyst køn]
- alder: values [0006=0-6 år, 0714=7-14 år, 1515=15 år, 1616=16 år, 1717=17 år, 1818=18 år, 1919=19 år, 2024=20-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 7599=75- år, 9999=Uoplyst alder]
- skade: values [102=Kraniebrud, piskesmæld, hjernerystelse, 202=Læsion af brystkasse, underliv, 302=Læsion af rygsøjle, bækken, 402=Læsion i skulder, arm, hånd, 502=Læsion i hofte, ben, fod, 602=Læsion i flere kropsområder, 702=Forbrænding, 802=Alene lettere skade]
- tid: date range 2001-01-01 to 2024-01-01
notes:
- uhelda=0, uheld=0 (Personskade i alt), transmid=0, and koen=0 (I alt) are all aggregates — filter all four to avoid overcounting.
- alder and skade have NO total codes; all values are specific categories. 9999=Uoplyst alder (not a total).
- alder codes: ColumnValues shows '0006' and '0714' with leading zeros, but the database stores them as '6' and '714'. Use WHERE alder='6' for 0–6 år and WHERE alder='714' for 7–14 år. All other alder codes (1515, 2024, etc.) match between ColumnValues and DB.
- skade has 8 body-region types; no total. Sum across all skade to get total injuries.
- This table counts persons (not accidents). A single accident with 3 injured = 3 rows.
