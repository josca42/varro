table: fact.uheld12
description: Førere og fodgængere efter transportmiddel, køn, alder, kørekortets alder, alkoholpromille og tid
measure: indhold (unit Antal)
columns:
- transmid: values [0=I alt, 11=Almindelig personbil, 12=Taxi, 13=Køretøj 0-3.500 kg under udrykning, 22=Varebil 0-2.000 kg, 23=Varebil 2.001-3.500 kg, 31=Lastbil over 3.500 kg., 34=Rutebus, 35=Bus i øvrigt, 42=Traktor, 41=Motorcykel, 45=Knallert 45, 51=Knallert med konstruktive ændringer, 52=Knallert i øvrigt, 61=Cykel, 62=El-cykler, 71=Fodgænger, 99=Andre]
- koen: values [1=Mænd, 2=Kvinder, 9=Uoplyst køn]
- alder: values [0006=0-6 år, 0714=7-14 år, 1515=15 år, 1616=16 år, 1717=17 år, 1818=18 år, 1919=19 år, 2024=20-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 7599=75- år, 9999=Uoplyst alder]
- kalder: values [105=Under 1 år, 205=1-2 år, 305=3-4 år, 405=5-9 år, 505=10 - år, 605=Uoplyst år, 705=Kørekort mangler til det benyttede køretøj, 805=Kørekort/knalllertbevis kræves ikke]
- alco: values [103=0,51-0,8 promille, 203=0,81-1,2 promille, 303=1,21-1,6 promille, 403=1,61-2,0 promille, 503=Over 2,0 promille, 603=Spirituspåvirket, men ikke prøvet, 703=Ikke skønnet spirituspåvirket]
- tid: date range 2001-01-01 to 2024-01-01
notes:
- This table counts drivers and pedestrians (people involved, not just injured). It covers everyone in an accident with alcohol information — not limited to injured persons.
- transmid=0 (I alt) is the only aggregate — filter it. koen and alder have no total codes.
- alco: 7 mutually exclusive values. 703=Ikke skønnet spirituspåvirket is the largest group (not impaired). 103–503 are progressively higher alcohol levels. 603=Spirituspåvirket men ikke prøvet. Sum all 7 to get total involved persons.
- kalder: driving licence age has no total code. 705=Kørekort mangler (no licence for the vehicle used). 805=Kørekort/bevis kræves ikke.
- alder codes: ColumnValues shows '0006' and '0714' with leading zeros but DB stores as '6' and '714'. Use WHERE alder='6' for 0–6 år and WHERE alder='714' for 7–14 år.
