table: fact.boern2
description: Fuldtidsomregnet indskrevne børn i kommunale og selvejende daginstitutioner, puljeordninger og dagpleje efter område, pasningstilbud og tid
measure: indhold (unit Antal)
columns:
- blstkom: join dim.nuts on blstkom=kode; levels [1, 3]
- paskat: values [TOT=I alt, 1=Dagpleje, 2=Daginstitution 0-2 år, 3=Daginstitution 3-5 år]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- blstkom contains kode 0 (national total, not in dim.nuts), niveau 1 (5 regioner), and niveau 3 (98 kommuner). Use ColumnValues("nuts", "titel", for_table="boern2") to see available geographic codes; filter WHERE d.niveau = 1 or d.niveau = 3.
- paskat includes TOT=I alt alongside 3 specific types. Always filter to one paskat value — summing across all rows inflates by 4x.
- For total FTE enrolled children by municipality: WHERE paskat = 'TOT' AND blstkom != '0'.
- Covers kommunale og selvejende institutions only. For private institutions add pboern2 (2021-2023 only). For fritidsordninger (SFO, fritidshjem) use boern5.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on blstkom=dim_kode. Exclude blstkom=0.
