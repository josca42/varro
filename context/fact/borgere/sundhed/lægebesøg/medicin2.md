table: fact.medicin2
description: Salg af receptpligtig medicin (eksperimentel statistik) efter herkomst, medicintype, nøgletal, køn, aldersgruppe og tid
measure: indhold (unit Antal)
columns:
- herkomst: values [TOT=I alt, 1=Personer med dansk oprindelse, 24=Indvandrere fra vestlige lande, 25=Indvandrere fra ikke-vestlige lande, 34=Efterkommere fra vestlige lande, 35=Efterkommere fra ikke-vestlige lande]
- medicintype: values [TOT=MEDICINTYPE I ALT, A=A FORDØJELSESORGANER OG STOFSKIFTE, A01=A01 Midler mod sygdomme i mundhulen, A02=A02 Midler mod syrerelaterede forstyrrelser, A03=A03 Midler mod funktionelle gastrointestinale forstyrrelser ... V07=V07 Alle andre non-terapeutiske produkter, V08=V08 Kontrastmidler, V09=V09 Radiofarmaka til diagnostisk brug, V10=V10 Radiofarmaka til terapeutisk brug, V20=V20 Surgical dressings]
- bnogle: values [2000=Personer, 2005=Indløste recepter]
- kon: values [0=Køn i alt, 1=Mænd, 2=Kvinder]
- agebygroup: values [TOT=Alder i alt, 0009=0-9 år, 1019=10-19 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7079=70-79 år, 8089=80-89 år, 9000=90 år og derover]
- tid: date range 2016-01-01 to 2021-01-01
notes:
- Experimental statistics. herkomst is inline (no dim join): TOT=total, 1=Dansk oprinding, 24=Indvandrere vestlige, 25=Indvandrere ikke-vestlige, 34=Efterkommere vestlige, 35=Efterkommere ikke-vestlige. Note finer split than sygher (which uses 10/20/30).
- bnogle is a measurement selector (2000=persons, 2005=prescriptions filled). Never aggregate across bnogle values.
- medicintype two-level hierarchy (TOT, letter codes, letter+digit codes). Do not sum across levels.
- kon uses 0=køn i alt, 1=mænd, 2=kvinder. Data only through 2021.
