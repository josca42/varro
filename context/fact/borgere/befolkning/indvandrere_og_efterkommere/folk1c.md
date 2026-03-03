table: fact.folk1c
description: Befolkningen den 1. i kvartalet efter område, køn, alder, herkomst, oprindelsesland og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- alder: values [IALT=Alder i alt, 0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år ... 80-84=80-84 år, 85-89=85-89 år, 90-94=90-94 år, 95-99=95-99 år, 100OV=100 år og derover]
- herkomst: values [TOT=I alt, 5=Personer med dansk oprindelse, 4=Indvandrere, 3=Efterkommere]
- ieland: join dim.lande_psd on ieland=kode; levels [3]
- tid: date range 2008-01-01 to 2020-01-01
dim docs: /dim/lande_psd.md, /dim/nuts.md

notes:
- omrade=0 is the national total ("I alt") — not in dim.nuts. dim.nuts covers niveau=1 (5 regioner) and niveau=3 (99 kommuner).
- ieland=0 is the "I alt" total across all origin countries. All other ieland codes are niveau=3 individual countries.
- herkomst is inline: TOT=I alt, 5=dansk oprindelse, 4=Indvandrere, 3=Efterkommere. No dim join needed.
- This table ends 2020-01-01. For current data use folk1e (herkomst without country detail) or folk1b (statsb with country detail).
- 6 dimension columns (omrade, kon, alder, herkomst, ieland, tid). Filter non-target dims to totals: omrade=0, kon='TOT', alder='IALT', herkomst='TOT', ieland=0.
- Use ColumnValues("lande_psd", "titel", for_table="folk1c") to browse origin country codes.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.