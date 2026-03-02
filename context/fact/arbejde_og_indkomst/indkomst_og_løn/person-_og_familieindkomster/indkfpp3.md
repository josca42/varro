table: fact.indkfpp3
description: Disponibel indkomst efter region, enhed, køn, indkomstinterval og tid
measure: indhold (unit -)
columns:
- region: join dim.nuts on region=kode; levels [1]
- enhed: values [103=Personer i gruppen (antal), 110=Indkomstbeløb (1.000 kr.), 118=Gennemsnit for personer i gruppen (kr.)]
- koen: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- indkintb: values [0=Alle, 100=Under 100.000 kr., 110=100.000 - 199.999 kr., 810=200.000 - 299.999 kr., 815=300.000 - 399.999 kr., 820=400.000 - 499.999 kr., 900=500.000 - 749.999 kr., 910=750.000 - 999.999 kr., 915=1.000.000 - 1.999.999 kr., 920=2.000.000 - 2.999.999 kr., 925=3.000.000 - 3.999.999 kr., 930=4.000.000 - 4.999.999 kr., 935=5.000.000 - 9.999.999 kr., 940=10.000.000 kr. og derover]
- tid: date range 1987-01-01 to 2023-01-01
dim docs: /dim/nuts.md
notes:
- region joins dim.nuts at niveau 1 only (5 regioner). region='0' is national aggregate, not in dim.
- indkintb='0' is "Alle" (total). Same coarse high-end bracket structure as indkp102.
- enhed selector (3 types). Always filter to one.
- Covers disponibel indkomst (after-tax). For indkomst i alt by region use indkp102.
- koen='MOK' is total.
- Map: context/geo/regioner.parquet — merge on region=dim_kode. Exclude region=0.
