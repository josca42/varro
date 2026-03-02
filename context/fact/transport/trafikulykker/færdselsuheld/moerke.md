table: fact.moerke
description: Personskader i færdselsuheld indberettet af politi, sygehusenes akutmodtagelse og sygehuse efter indberetter, uheldssituation, transportmiddel, køn, alder, skadens type og tid
measure: indhold (unit Antal)
columns:
- indberet: values [0=Indberetter i alt, 1=Politi, 2=Kun skadestue, 3=Kun sygehusenes akutmodtagelse]
- uheldsit: values [0=Uheldssituation i alt, 100=Uheld med kun et transportmiddel, 200=Uheld med mere end et transportmiddel]
- transmid: values [0=Transportmiddel i alt, 11=Personbil, 22=Varebil, 31=Lastbil mv., 41=Motorcykel mv., 51=Knallert-30, 61=Cykel, 62=El-cykler, 71=Fodgænger, 99=Andet eller uoplyst]
- koen: values [0=I alt, 1=Mænd, 2=Kvinder]
- alder: values [0000=Alder i alt, 0006=0-6 år, 0714=7-14 år, 1517=15-17 år, 1819=18-19 år, 2024=20-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år, 7599=75- år, 9999=Uoplyst alder]
- skade: values [0=Uheldssituation i alt, 102=Hoved- og halslæsioner, 202=Thorax, adbomen-, lænd- og bækkenlæsioner, 402=Læsion i skulder, arm, hånd, 502=Læsion i hofte, ben, fod, 902=Øvrige]
- tid: date range 2001-01-01 to 2023-01-01
notes:
- This is the "mørketals" (dark number) table combining police reports and hospital data to estimate total injury counts including accidents not reported to police.
- CRITICAL: ALL 6 dimension columns have aggregate codes that must be filtered to avoid massive overcounting:
  - indberet=0 (Indberetter i alt), uheldsit=0 (Uheldssituation i alt), transmid=0 (Transportmiddel i alt), koen=0 (I alt), alder=0 (Alder i alt), skade=0 (Uheldssituation i alt — yes the label says uheldsit but it's the skade aggregate).
- uheldsit coding here is DIFFERENT from all other uheld* tables: 100=Uheld med kun et transportmiddel, 200=Uheld med mere end et transportmiddel (just 2 categories vs the 10-category scheme elsewhere).
- alder total is stored as '0' (not '0000') — WHERE alder='0' for all ages. Similarly alder='6' for 0–6 år (not '0006').
- indberet='1' for police-only reports, '2' for skadestue-only, '3' for sygehusenes akutmodtagelse-only. Use indberet='0' for the combined estimate.
- Data ends at 2023 (not updated to 2024 unlike the police-based uheld* tables).
- Sample total query: WHERE indberet='0' AND uheldsit='0' AND transmid='0' AND koen='0' AND alder='0' AND skade='0'.
