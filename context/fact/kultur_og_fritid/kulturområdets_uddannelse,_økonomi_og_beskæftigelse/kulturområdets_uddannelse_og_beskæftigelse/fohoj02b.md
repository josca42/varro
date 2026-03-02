table: fact.fohoj02b
description: Antallet af højskolekursister på mellemlange og lange kurser efter køn, alder, ækvivaleret disponibel indkomst i familien, enhed, tidsangivelse og tid
measure: indhold (unit Antal)
columns:
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, -17=Under 18 år, 1821=18-21 år, 2225=22-25 år, 2629=26-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6099=60 år og derover]
- aekvi_fam_indkomst: values [TOT=I alt, 800=Under 200.000 kr., 810=200.000 - 299.999 kr., 815=300.000 - 399.999 kr., 820=400.000 - 499.999 kr., 600=500.000 - 599.999 kr., 825=600.000 kr. og derover, 9999=Uoplyst mv.]
- enhed: values [11=Kursister, 13=Årselever]
- tidspunkter: values [22=Skoleår, 11=Kalenderår]
- tid: date range 2016-01-01 to 2024-01-01
notes:
- CRITICAL: enhed and tidspunkter are both measurement selectors. Always filter both to a single value.
- Covers only medium and long courses — no short courses.
- aekvi_fam_indkomst=TOT is the total. Note the income brackets are family equivalised income (ækvivaleret disponibel indkomst), not personal income — use fohoj03b for personal income.
- kon=TOT and alder=TOT are totals. Filter unused dimensions.
