table: fact.ligehi13
description: Ligestillingsindikator hjemmehjælp, visiteret tid pr. person efter indikator, område, alder, familietype og tid
measure: indhold (unit Gns. antal timer pr. uge)
columns:
- indikator: values [LA1T=Mænd (timer), LA2T=Kvinder (timer), LA3T=Forskel mellem mænd og kvinder (timer)]
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- alder: values [TOT=Alder i alt, 6569=65-69 år, 7074=70-74 år, 7579=75-79 år, 8084=80-84 år, 8589=85-89 år, 9099=90 år og derover]
- famtyp: values [FAMIALT=Familier i alt, ENL=Enlige, PAF=Parfamilier]
- tid: date range 2010-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- indhold is average hours per week per person. Never sum across indikator: LA3T is a derived difference (LA1T-LA2T), not a raw average.
- omrade joins dim.nuts with both niveau 1 (5 regioner) and niveau 3 (98 kommuner). Filter WHERE d.niveau=3 for kommuner, d.niveau=1 for regioner. omrade=0 is national total (not in dim).
- alder=TOT is total; bands (6569-9099) are non-overlapping. famtyp=FAMIALT is the total.
- Pair with ligehi12 for the equivalent by person count (pct. receiving home help).
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
