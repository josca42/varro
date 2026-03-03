table: fact.ligeai6
description: Ligestillingsindikator for NEET efter indikator, bopælsområde, alder og tid
measure: indhold (unit -)
columns:
- indikator: values [LA1=Mænd (pct.), LA2=Kvinder (pct.), LA3=Forskel mellem mænd og kvinder (procentpoint)]
- bopomr: join dim.nuts on bopomr=kode; levels [1, 2, 3]
- alder: values [IALT=Alder i alt, 16=16 år, 17=17 år, 18=18 år, 19=19 år, 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- indikator has 3 values: LA1=mænd (pct.), LA2=kvinder (pct.), LA3=forskel mellem mænd og kvinder (procentpoint). These are three independent indicators — always filter to one at a time. Summing or averaging across them is meaningless.
- indhold unit is listed as '-' but values are percentages (LA1, LA2) or percentage-point differences (LA3). For 2023 nationally: mænd=10%, kvinder=9.2%, forskel=0.8pp.
- bopomr joins dim.nuts. bopomr='0' is the national total, not in dim.nuts. Three hierarchy levels via d.niveau: 1=5 regioner, 2=11 landsdele, 3=99 kommuner.
- alder: IALT=total, plus 9 individual ages (16-24). Filter to alder='IALT' for overall gender gap.
- Use this table specifically for gender-gap analysis on NEET. For raw NEET counts by gender use neet1 or neet2.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on bopomr=dim_kode. Exclude bopomr=0.