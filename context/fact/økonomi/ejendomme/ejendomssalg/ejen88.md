table: fact.ejen88
description: Ejendomssalg efter område, ejendomskategori, nøgletal, overdragelsesformer og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2]
- ejendomskate: join dim.ejendom on ejendomskate=kode [approx]; levels [1, 2]
- bnogle: values [2=Salg ved prisberegning (antal), 3=Gennemsnitlig pris pr. ejendom (1000 kr), 4=Købesum pr. ha/m2 (landbrug/grunde), 5=Købesum i 0/00 af ejendomsværdi, 1=Beregnet antal salg]
- overdrag: values [1=Almindelig fri handel, 2=Familieoverdragelse, 3=Andre salg]
- tid: date range 1992-01-01 to 2024-01-01
dim docs: /dim/ejendom.md, /dim/nuts.md

notes:
- Same structure as ejen77 but annual granularity. Ends 2024. For quarterly or current data, use ejen77.
- `bnogle` selects the key figure — always filter to one value: 1=Beregnet antal salg, 2=Salg ved prisberegning, 3=Gennemsnitlig pris (1000 kr), 4=Købesum pr. ha/m2 (landbrug/grunde), 5=Købesum i promille af ejendomsværdi.
- `overdrag`: 1=Almindelig fri handel, 2=Familieoverdragelse, 3=Andre salg. Filter to `overdrag='1'` for market-price analysis.
- `omrade` joins dim.nuts niveau 1 (regioner) and niveau 2 (landsdele). Code 0 = "Hele landet" (not in dim). Filter `d.niveau` to avoid mixing levels.
- `ejendomskate` joins dim.ejendom at both niveaus. Code 9999 = "Samlet salg" (aggregate total, not in dim) — exclude for per-category analysis.
- Map: /geo/regioner.parquet (niveau 1) or /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.