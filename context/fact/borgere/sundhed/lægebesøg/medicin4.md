table: fact.medicin4
description: Salg af receptpligtig medicin (eksperimentel statistik) efter medicintype, nøgletal, køn, aldersgruppe og tid
measure: indhold (unit Pr. 100.000 personer)
columns:
- medicintype: values [TOT=MEDICINTYPE I ALT, A=A FORDØJELSESORGANER OG STOFSKIFTE, A01=A01 Midler mod sygdomme i mundhulen, A02=A02 Midler mod syrerelaterede forstyrrelser, A03=A03 Midler mod funktionelle gastrointestinale forstyrrelser ... V07=V07 Alle andre non-terapeutiske produkter, V08=V08 Kontrastmidler, V09=V09 Radiofarmaka til diagnostisk brug, V10=V10 Radiofarmaka til terapeutisk brug, V20=V20 Surgical dressings]
- bnogle: values [2000=Personer, 2005=Indløste recepter]
- kon: values [0=Køn i alt, 1=Mænd, 2=Kvinder]
- agebygroup: values [TOT=Alder i alt, 0009=0-9 år, 1019=10-19 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7079=70-79 år, 8089=80-89 år, 9000=90 år og derover]
- tid: date range 2016-01-01 to 2021-01-01
notes:
- indhold is a RATE — per 100.000 persons. Do NOT sum across rows. This table is for comparing rates between groups, not for calculating totals.
- bnogle is a measurement selector (2000=persons rate, 2005=prescriptions rate). Each bnogle gives an independent rate — never sum.
- medicintype two-level hierarchy (TOT, letter codes, letter+digit codes). Pick one level.
- No geographic or socioeconomic breakdown — national rates only by medicine type, gender, age. Data only through 2021.
- kon uses 0=køn i alt, 1=mænd, 2=kvinder.
