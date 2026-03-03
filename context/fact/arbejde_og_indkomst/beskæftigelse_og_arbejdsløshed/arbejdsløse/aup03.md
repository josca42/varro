table: fact.aup03
description: Fuldtidsledige i pct. af samtlige forsikrede (foreløbig opgørelse) efter område, alder, køn, a-kasse og tid
measure: indhold (unit Pct.)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2, 3]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 6099=60 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- akasse: values [TOT=I alt, 48=Akademikernes (fra 1. juli 2013 inkl. ingeniører), 46=Din Faglige A-kasse (fra 1. januar 2025 inkl. Fødevareforbundet (NNF), 05=Børne- og Ungdomspædagoger (BUPL-A), 06=Din Sundhedsfaglige A-kasse (DSA) ... 25=Maritim a-kasse (- dec. 2002), 09=Forsvarets a-kasse (- dec. 2001), 10=Frisører, Artister og Maritim (- dec. 2001), 14=Grafisk a-kasse (- dec. 1999), 45=Ikke forsikrede]
- tid: date range 2017-07-01 to 2025-09-01
dim docs: /dim/nuts.md

notes:
- indhold is pct. of samtlige forsikrede (all insured), not pct. of workforce. Different denominator from aup01/aup02. Do not sum rates.
- The only rate table with akasse breakdown. Useful for comparing unemployment rates across a-kasser.
- omrade joins dim.nuts at levels 1/2/3. omrade='0'=Hele landet not in dim.
- Preliminary (foreløbig), from Jul 2017 only.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.