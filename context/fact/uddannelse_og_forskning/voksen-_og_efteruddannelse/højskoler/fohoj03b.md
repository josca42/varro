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
- `enhed` and `tidspunkter` are measurement selectors — filter both to avoid doubling. Both are smallint.
- `alder` total code is `'TOT'`. Same broad age groups as fohoj03a: `-17`, `1829`, `3049`, `5069`, `7079`, `8099`.
- `pers_indk` is personal income (not family income — for family income see fohoj02b). Income codes are non-sequential (100, 110, 810, 815, 820, 900, 910, 950, 9999=Uoplyst). TOT is the total.
- Only covers korte kurser. For mellemlange og lange kurser with income breakdown, use fohoj02b.