table: fact.km6
description: Befolkningen 1. januar efter kommune, køn, alder, folkekirkemedlemsskab og tid
measure: indhold (unit Antal)
columns:
- komk: join dim.nuts on komk=kode; levels [3]
- kon: values [1=Mænd, 2=Kvinder]
- alder: values [0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år, 20-24=20-24 år ... 80-84=80-84 år, 85-89=85-89 år, 90-94=90-94 år, 95-99=95-99 år, 100OV=100 år og derover]
- fkmed: values [F=Medlem af Folkekirken, U=Ikke medlem af Folkekirken]
- tid: date range 2011-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- komk joins dim.nuts at niveau 3 (kommuner) only — 99 kommuner, 100% match. Use: JOIN dim.nuts d ON f.komk=d.kode WHERE d.niveau=3. Use ColumnValues("nuts", "titel", for_table="km6") to see available kommuner.
- alder uses 5-year interval bands: '[0,5)', '[5,10)', ..., '[95,100)', '[100,)' — 21 bands, no IALT total. Sum across all alder rows for a total by kommune.
- kon: 1=Mænd, 2=Kvinder. No TOT — sum both for combined total.
- fkmed: F=Medlem, U=Ikke-Medlem. Filter or sum both explicitly.
- Starts from 2011 (later than km5/km55 which go back to 2007). The only folkekirke table with a dim-linked geographic column (vs. sogns/provsti inline codes).
- Map: context/geo/kommuner.parquet — merge on komk=dim_kode.
