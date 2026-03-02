table: fact.pboern2
description: Fuldtidsomregnet indskrevne børn i private dagtilbudsinstitutioner efter område, pasningstilbud og tid
measure: indhold (unit Antal)
columns:
- blstkom: join dim.nuts on blstkom=kode; levels [1, 3]
- paskat: values [TOT=I alt, 2=Daginstitution 0-2 år, 3=Daginstitution 3-5 år]
- tid: date range 2021-01-01 to 2023-01-01
dim docs: /dim/nuts.md
notes:
- blstkom contains kode 0 (national total, not in dim.nuts), niveau 1 (5 regioner), and niveau 3 (98 kommuner).
- paskat includes TOT=I alt alongside 2 specific types (no dagpleje — private institutions don't provide dagpleje). Filter to one paskat to avoid 3x inflation.
- Short time range only: 2021-2023. For kommunale og selvejende institutions use boern2 (2015-2024).
- To get total enrolled children (kommunal + private), join boern2 and pboern2 on blstkom, paskat='TOT', same tid.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on blstkom=dim_kode. Exclude blstkom=0.
