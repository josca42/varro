table: fact.ligeab2
description: Befolkningen (16-64 år) efter område, socioøkonomisk status, familietype, køn, alder og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- socio: values [TOT=I alt, 00=Beskæftigede, 50=Arbejdsløse, 55=Uden for arbejdsstyrken]
- famtype: values [TOT=I alt, F2=Familier uden hjemmeboende børn, i alt, F1=Familier med hjemmeboende børn, i alt, E1=Enlige, i alt, EUHB=Enlige uden hjemmeboende børn, EMHB=Enlige med hjemmeboende børn, P1=Par, i alt, PUHB=Par uden hjemmeboende børn, PMHB=Par med hjemmeboende børn, U9=Uoplyst familietype]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 16-17=16-17 år, 18-19=18-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts on omrade=kode. dim.nuts has 5 regioner (niveau 1), 11 landsdele (niveau 2), 99 kommuner (niveau 3). Filter WHERE d.niveau = N to avoid double-counting.
- omrade='0' is the national total — not in dim.nuts. Use directly: WHERE f.omrade = '0'.
- famtype includes sub-totals (F1/F2/E1/P1) alongside sub-types (EUHB/EMHB/PUHB/PMHB) — see ligeab1 notes. Do not mix levels in the same SUM.
- No herkomst column (unlike ligeab1). Use ligeab1 for herkomst × famtype, ligeab2 for region × famtype.
- Population scope is 16-64 år only.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.