table: fact.auf01
description: Fuldtidsledige (foreløbig opgørelse) efter område, ydelsestype, a-kasse, alder, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2, 3]
- ydelsestype: values [TOT=Bruttoledige, LDP=Nettoledige dagpengemodtagere, LKT=Nettoledige kontanthjælpsmodtagere, ADP=Aktiverede dagpengeberettigede, AKT=Aktiverede kontanthjælpsmodtagere (arbejdsmarkedsparate)]
- akasse: values [TOT=I alt, 48=Akademikernes (fra 1. juli 2013 inkl. ingeniører), 46=Din Faglige A-kasse (fra 1. januar 2025 inkl. Fødevareforbundet (NNF), 05=Børne- og Ungdomspædagoger (BUPL-A), 06=Din Sundhedsfaglige A-kasse (DSA) ... 25=Maritim a-kasse (- dec. 2002), 09=Forsvarets a-kasse (- dec. 2001), 10=Frisører, Artister og Maritim (- dec. 2001), 14=Grafisk a-kasse (- dec. 1999), 45=Ikke forsikrede]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 6099=60 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2017-07-01 to 2025-09-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts. Levels 1 (5 regioner), 2 (11 landsdele), 3 (98 kommuner). For national total use WHERE f.omrade = '0' directly — code 0 (Hele landet) is not in dim.nuts. Extra unmatched codes: 997=Udlandet, 998=Uoplyst kommune. Note: Hele landet (0) = sum of 5 regioner + 997 (Udlandet).
- ydelsestype: TOT=Bruttoledige is the sum of all components (LDP+LKT+ADP+AKT ≈ TOT). Don't sum all ydelsestype values — filter to TOT for a single total or pick one component.
- This is the most current preliminary table (foreløbig opgørelse) from Jul 2017. For longer history from 2007, use auf02 (also current) or aulk01 (also current, same structure, finer alder bands).
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.