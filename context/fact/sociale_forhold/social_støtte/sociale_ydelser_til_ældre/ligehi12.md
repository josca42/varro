table: fact.ligehi12
description: Ligestillingsindikator hjemmehjælp, visiterede personer efter indikator, område, alder, familietype og tid
measure: indhold (unit -)
columns:
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- alder: values [TOT=Alder i alt, 6569=65-69 år, 7074=70-74 år, 7579=75-79 år, 8084=80-84 år, 8589=85-89 år, 9099=90 år og derover]
- famtyp: values [FAMIALT=Familier i alt, ENL=Enlige, PAF=Parfamilier]
- tid: date range 2010-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- indhold unit is "-" meaning values are percentages (LA1, LA2) or procentpoints (LA3). Never sum across indikator: LA3 is a derived difference (LA1-LA2), not a count.
- omrade joins dim.nuts with both niveau 1 (5 regioner) and niveau 3 (98 kommuner). Filter WHERE d.niveau=3 for kommuner, d.niveau=1 for regioner. omrade=0 is national total (not in dim).
- alder=TOT is the all-age total; individual bands (6569-9099) are non-overlapping. famtyp=FAMIALT is the total; ENL and PAF are mutually exclusive sub-groups.
- To compare gender equality in home help by region: filter indikator='LA3' (gender gap in pct. points) and join dim.nuts at niveau 1.
- Pair with ligehi13 for the equivalent by hours per person.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
