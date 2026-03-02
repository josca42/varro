table: fact.ligeai1
description: Ligestillingsindikator for erhvervs- og beskæftigelsesfrekvenser (16-64 år) efter frekvens, indikator, familietype, herkomst, alder og tid
measure: indhold (unit -)
columns:
- frek: values [BFK=Beskæftigelsesfrekvens, EFK=Erhvervsfrekvens]
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- famtype: values [TOT=I alt, F2=Familier uden hjemmeboende børn, i alt, F1=Familier med hjemmeboende børn, i alt, E1=Enlige, i alt, EUHB=Enlige uden hjemmeboende børn, EMHB=Enlige med hjemmeboende børn, P1=Par, i alt, PUHB=Par uden hjemmeboende børn, PMHB=Par med hjemmeboende børn, U9=Uoplyst familietype]
- herkomst: values [0=I alt, 10=Personer med dansk oprindelse, 21=Indvandrere i alt, 24=Indvandrere fra vestlige lande, 25=Indvandrere fra ikke-vestlige lande, 31=Efterkommere i alt, 34=Efterkommere fra vestlige lande, 35=Efterkommere fra ikke-vestlige lande]
- alder: values [TOT=Alder i alt, 16-17=16-17 år, 18-19=18-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år]
- tid: date range 2008-01-01 to 2023-01-01

notes:
- indikator has 3 independent values: LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel (procentpoint). These are not summable — LA3 is a derived gender gap measure, not a count. Always filter to one indikator value per query.
- frek is also a measurement selector (BFK vs EFK). Every combination is repeated once per frek. Filter to one: WHERE frek = 'BFK'.
- herkomst includes intermediate totals (21=Indvandrere i alt, 31=Efterkommere i alt) — same pattern as ligeab1. Do not mix totals and sub-groups in the same analysis.
- famtype includes sub-totals (F1/F2/E1/P1) alongside detailed sub-types — see ligeab1 notes.
- National level only. Use ligeai2 for regional breakdown.