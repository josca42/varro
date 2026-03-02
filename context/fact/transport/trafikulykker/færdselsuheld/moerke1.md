table: fact.moerke1
description: Personskader i færdselsuheld indberettet af sygehusenes akutmodtagelse og sygehuse efter indberetter, uheldssituation, transportmiddel, køn, alder, personskade (klassificeret efter diagnose) og tid
measure: indhold (unit Antal)
columns:
- indberet: values [0=Indberetter i alt, 2=Kun skadestue, 3=Kun sygehusenes akutmodtagelse]
- uheldsit: values [0=Uheldssituation i alt, 100=Uheld med kun et transportmiddel, 200=Uheld med mere end et transportmiddel]
- transmid: values [0=Transportmiddel i alt, 11=Personbil, 22=Varebil, 31=Lastbil mv., 41=Motorcykel mv., 51=Knallert-30, 61=Cykel, 62=El-cykler, 71=Fodgænger, 99=Andet eller uoplyst]
- koen: values [0=I alt, 1=Mænd, 2=Kvinder]
- alder: values [0000=Alder i alt, 0006=0-6 år, 0714=7-14 år, 1517=15-17 år, 1819=18-19 år, 2024=20-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 7599=75- år, 9999=Uoplyst alder]
- skadediag: values [0=Tilskadekomne i alt, 20000=Alvorligt tilskadekomne (diagnose klass.), 30000=Lettere tilskadekomne (diagnose klass.)]
- tid: date range 2009-01-01 to 2023-01-01
notes:
- Like moerke but hospital-only data (no police reports) from 2009 onward, with injury severity classified by diagnosis rather than police assessment.
- CRITICAL: ALL 6 dimension columns have aggregate codes: indberet=0, uheldsit=0, transmid=0, koen=0, alder=0 (Alder i alt), skadediag=0 (Tilskadekomne i alt).
- uheldsit coding same as moerke: 100=et transportmiddel, 200=mere end et (not the 10-category uheld* scheme).
- skadediag has only 3 values: 0=I alt, 20000=Alvorligt tilskadekomne, 30000=Lettere tilskadekomne. No Dræbte (killed) category — diagnosis-based classification only covers non-fatal injuries.
- alder aggregate stored as '0' (not '0000'); '6' for 0–6 år (not '0006').
- indberet: '2'=Kun skadestue, '3'=Kun sygehusenes akutmodtagelse (no '1'=Politi, unlike moerke).
- Data ends at 2023. Shorter series than moerke (starts 2009 vs 2001).
