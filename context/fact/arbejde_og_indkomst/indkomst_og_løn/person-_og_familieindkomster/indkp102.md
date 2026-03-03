table: fact.indkp102
description: Indkomst i alt efter region, enhed, køn, indkomstinterval og tid
measure: indhold (unit -)
columns:
- region: join dim.nuts on region=kode; levels [1]
- enhed: values [103=Personer i gruppen (antal), 110=Indkomstbeløb (1.000 kr.), 118=Gennemsnit for personer i gruppen (kr.)]
- koen: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- indkintb: values [0=Alle, 100=Under 100.000 kr., 110=100.000 - 199.999 kr., 810=200.000 - 299.999 kr., 815=300.000 - 399.999 kr., 820=400.000 - 499.999 kr., 900=500.000 - 749.999 kr., 910=750.000 - 999.999 kr., 915=1.000.000 - 1.999.999 kr., 920=2.000.000 - 2.999.999 kr., 925=3.000.000 - 3.999.999 kr., 930=4.000.000 - 4.999.999 kr., 935=5.000.000 - 9.999.999 kr., 940=10.000.000 kr. og derover]
- tid: date range 1987-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- region joins dim.nuts at niveau 1 only (5 regioner). No landsdel or kommune detail.
- region='0' is the national aggregate — not in dim.nuts.
- indkintb='0' means "Alle" (all income brackets combined). Use for totals; pick specific brackets for distribution analysis.
- Income brackets here are coarser at the bottom (lowest is "under 100.000 kr.") but very detailed at the top (up to 10M+). Use indkp105/indkp106 for finer 25k-step brackets.
- enhed selector (3 types): always filter to one.
- Covers indkomst i alt (total income before tax). For disponibel by region use indkfpp3.
- Map: /geo/regioner.parquet — merge on region=dim_kode. Exclude region=0.
