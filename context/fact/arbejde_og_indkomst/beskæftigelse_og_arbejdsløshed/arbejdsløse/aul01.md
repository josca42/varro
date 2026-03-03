table: fact.aul01
description: Fuldtidsledige efter område, ydelsestype, a-kasse, alder, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 2, 3]
- ydelsestype: values [TOT=Bruttoledige, LDP=Nettoledige dagpengemodtagere, LKT=Nettoledige kontanthjælpsmodtagere, ADP=Aktiverede dagpengeberettigede, AKT=Aktiverede kontanthjælpsmodtagere (arbejdsmarkedsparate)]
- akasse: values [TOT=I alt, 48=Akademikernes (fra 1. juli 2013 inkl. ingeniører), 46=Din Faglige A-kasse (fra 1. januar 2025 inkl. Fødevareforbundet (NNF), 05=Børne- og Ungdomspædagoger (BUPL-A), 06=Din Sundhedsfaglige A-kasse (DSA) ... 25=Maritim a-kasse (- dec. 2002), 09=Forsvarets a-kasse (- dec. 2001), 10=Frisører, Artister og Maritim (- dec. 2001), 14=Grafisk a-kasse (- dec. 1999), 45=Ikke forsikrede]
- alder: values [TOT=Alder i alt, 16-24=16-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 6099=60 år og derover]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- Superseded by aulk01 (same structure, updated to 2025). Use aulk01 for current data.
- omrade joins dim.nuts (levels 1/2/3). omrade='0'=Hele landet not in dim.
- ydelsestype: TOT=Bruttoledige is the aggregate of LDP+LKT+ADP+AKT. Filter to one ydelsestype.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.