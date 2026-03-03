table: fact.aua01
description: Forsikringsaktive efter område, a-kasse, alder, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2, 3]
- akasse: values [TOT=I alt, 48=Akademikernes (fra 1. juli 2013 inkl. ingeniører), 46=Din Faglige A-kasse (fra 1. januar 2025 inkl. Fødevareforbundet (NNF), 05=Børne- og Ungdomspædagoger (BUPL-A), 06=Din Sundhedsfaglige A-kasse (DSA) ... 25=Maritim a-kasse (- dec. 2002), 09=Forsvarets a-kasse (- dec. 2001), 10=Frisører, Artister og Maritim (- dec. 2001), 14=Grafisk a-kasse (- dec. 1999), 45=Ikke forsikrede]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 6099=60 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2000-04-01 to 2025-09-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts at levels 1/2/3. Extra codes not in dim: 0=Hele landet, 997=Udlandet, 998=Uoplyst. Hele landet (0) = sum of 5 regioner + 997 (Udlandet). Use WHERE f.omrade = '0' for national total.
- Denominator table for unemployment rate calculations. Pairs with auf01/aup03 for pct. af forsikrede.
- Longest series in subject from 2000-04. Includes '45=Ikke forsikrede' in akasse — filter this out when computing rates for insured members only.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.