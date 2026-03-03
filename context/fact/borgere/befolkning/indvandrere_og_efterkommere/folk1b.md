table: fact.folk1b
description: Befolkningen den 1. i kvartalet efter område, køn, alder, statsborgerskab og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- alder: values [IALT=Alder i alt, 0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år ... 80-84=80-84 år, 85-89=85-89 år, 90-94=90-94 år, 95-99=95-99 år, 100OV=100 år og derover]
- statsb: join dim.lande_psd on statsb=kode; levels [3]
- tid: date range 2008-01-01 to 2025-07-01
dim docs: /dim/lande_psd.md, /dim/nuts.md

notes:
- omrade=0 is the national total ("I alt") — not in dim.nuts. dim.nuts has niveau=1 (5 regioner) and niveau=3 (99 kommuner). Filter WHERE d.niveau=1 or d.niveau=3 to pick granularity; never join omrade=0.
- statsb=0 is the "I alt" total across all nationalities. In dim.lande_psd, kode=0 is labelled "Helt uoplyst" — ignore that label here; in fact.folk1b it is the aggregate. All other statsb codes are niveau=3 individual countries (~207 countries).
- To avoid overcounting: 5 dimension columns (omrade, kon, alder, statsb, tid). Filter all non-target dimensions to their totals: omrade=0 for national, kon='TOT', alder='IALT', statsb=0 for all nationalities.
- Use ColumnValues("lande_psd", "titel", for_table="folk1b") to browse the ~208 nationality codes in this table.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.