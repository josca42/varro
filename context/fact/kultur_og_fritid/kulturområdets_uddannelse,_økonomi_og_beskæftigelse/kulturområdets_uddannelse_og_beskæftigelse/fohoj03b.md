table: fact.fohoj03b
description: Antallet af højskolekursister på korte kurser efter køn, alder, personlig indkomst, enhed, tidsangivelse og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, -17=Under 18 år, 1829=18-29 år, 3049=30-49 år, 5069=50-69 år, 7079=70-79 år, 8099=80 år og derover]
- pers_indk: values [TOT=I alt, 100=Under 100.000 kr., 110=100.000 - 199.999 kr., 810=200.000 - 299.999 kr., 815=300.000 - 399.999 kr., 820=400.000 - 499.999 kr., 900=500.000 - 749.999 kr., 910=750.000 - 999.999 kr., 950=1.000.000 kr. og derover, 9999=Uoplyst mv.]
- enhed: values [11=Kursister, 13=Årselever]
- tidspunkter: values [22=Skoleår, 11=Kalenderår]
- tid: date range 2016-01-01 to 2024-01-01
notes:
- CRITICAL: enhed and tidspunkter are both measurement selectors. Always filter both to a single value.
- Covers only short courses.
- pers_indk=TOT is the total. Personal income of the individual (not family equivalised, unlike fohoj02b).
- kon=TOT and alder=TOT are totals.
