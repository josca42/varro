table: fact.ejen77
description: Ejendomssalg efter område, ejendomskategori, nøgletal, overdragelsesformer og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- ejendomskate: join dim.ejendom on ejendomskate=kode [approx]; levels [1, 2]
- bnogle: values [2=Salg ved prisberegning (antal), 3=Gennemsnitlig pris pr. ejendom (1000 kr), 4=Købesum pr. ha/m2 (landbrug/grunde), 5=Købesum i 0/00 af ejendomsværdi, 1=Beregnet antal salg]
- overdrag: values [1=Almindelig fri handel, 2=Familieoverdragelse, 3=Andre salg]
- tid: date range 1992-01-01 to 2025-04-01
dim docs: /dim/ejendom.md, /dim/nuts.md

notes:
- `bnogle` selects the key figure — always filter to one value: 1=Beregnet antal salg, 2=Salg ved prisberegning (antal), 3=Gennemsnitlig pris pr. ejendom (1000 kr), 4=Købesum pr. ha/m2 (landbrug/grunde kun), 5=Købesum i promille af ejendomsværdi.
- `overdrag` has three mutually exclusive transfer types: 1=Almindelig fri handel, 2=Familieoverdragelse, 3=Andre salg. For market price analysis, filter to `overdrag='1'` (ordinary free-market). To get total sales count, SUM across all three (or use the national totals where omrade=0).
- `omrade` joins dim.nuts at niveau 1 (5 regioner, kode 81-85) and niveau 2 (11 landsdele, kode 1-11). Code 0 = "Hele landet" (national total, not in dim). Filter `d.niveau` to avoid mixing levels. Use ColumnValues("nuts", "titel", for_table="ejen77") to see available regions.
- `ejendomskate` joins dim.ejendom at both niveau 1 and 2 (full coverage). Code 9999 = "Samlet salg" (grand total across all property types, not in dim) — exclude when doing per-category breakdowns. Use `WHERE f.ejendomskate != '9999'` or filter dim join.
- Most comprehensive sales table: covers all property types, all transfer types, regions and landsdele, quarterly from 1992 (current to 2025). For annual, use ejen88. For definitive/final revision, use ej131.
- Map: /geo/regioner.parquet (niveau 1) or /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.