table: fact.ligeai2
description: Ligestillingsindikator for erhvervs- og beskæftigelsesfrekvenser (16-64 år) efter frekvens, indikator, familietype, område, alder og tid
measure: indhold (unit -)
columns:
- frek: values [BFK=Beskæftigelsesfrekvens, EFK=Erhvervsfrekvens]
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- famtype: values [TOT=I alt, F2=Familier uden hjemmeboende børn, i alt, F1=Familier med hjemmeboende børn, i alt, E1=Enlige, i alt, EUHB=Enlige uden hjemmeboende børn, EMHB=Enlige med hjemmeboende børn, P1=Par, i alt, PUHB=Par uden hjemmeboende børn, PMHB=Par med hjemmeboende børn, U9=Uoplyst familietype]
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- alder: values [TOT=Alder i alt, 16-17=16-17 år, 18-19=18-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- indikator has 3 independent values: LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel (procentpoint). These are not summable. Always filter to one indikator per query.
- frek is a measurement selector (BFK/EFK) — doubles rows. Filter to one: WHERE frek = 'BFK'.
- omrade joins dim.nuts on omrade=kode. dim.nuts has 5 regioner (niveau 1), 11 landsdele (niveau 2), 99 kommuner (niveau 3). Filter WHERE d.niveau = N.
- omrade='0' is the national total — not in dim.nuts. Use directly.
- famtype includes sub-totals — see ligeab1/ligeai1 notes for the hierarchy structure.
- No herkomst column (unlike ligeai1). Use ligeai1 for herkomst × famtype, ligeai2 for region × famtype.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.