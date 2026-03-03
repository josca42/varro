table: fact.boern8
description: Normeringer i kommunale og selvejende daginstitutioner, institutionslignende puljeordninger og dagpleje efter kommune, pasningstilbud og tid
measure: indhold (unit Antal)
columns:
- kommunedk: join dim.nuts on kommunedk=kode; levels [1, 3]
- paskat: values [1=Dagpleje, 2=Daginstitution 0-2 år, 3=Daginstitution 3-5 år]
- tid: date range 2023-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- kommunedk contains kode 0 (national total, not in dim.nuts), niveau 1 (5 regioner, kode 81-85), and niveau 3 (98 kommuner). Filter WHERE d.niveau = 1 or d.niveau = 3; exclude kode '0' or LEFT JOIN and check d.niveau IS NOT NULL.
- paskat has NO total — the 3 values (Dagpleje, 0-2 år, 3-5 år) are independent staffing norms. indhold is a ratio (e.g., 3.2 children per normeret staff at national level for Dagpleje), not a headcount. Do NOT sum across paskat.
- 2-year snapshot only (2023 and 2024). For trend data use boern2 (enrolled children, back to 2015).
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on kommunedk=dim_kode. Exclude kommunedk=0.