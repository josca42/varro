table: fact.aed07
description: Hjemmehjælp i plejebolig/plejehjem, visiterede personer efter område, alder, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- alder: values [50=Alder i alt, 100=Under 65 år, 200=65-66 år, 300=67-69 år, 850=67 år og derover, 400=70-74 år, 500=75-79 år, 600=80-84 år, 700=85-89 år, 800=90 år og derover]
- kon: values [100=Køn i alt, 200=Mænd, 300=Kvinder]
- tid: date range 2008-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- Covers persons in plejebolig/plejehjem (care homes), not in own home. For home-based care recipients use aed06.
- Gender column is kon (not koen as in most other tables in this subject). kon=100 is the total; 200=mænd, 300=kvinder.
- omrade joins dim.nuts with both niveau 1 (5 regioner) and niveau 3 (98 kommuner). Filter WHERE d.niveau=3 or d.niveau=1. omrade=0 is national total (not in dim).
- alder=50 is total; alder=850 is the 67+ sub-total. Do not mix sub-totals with individual age bands.
- No ydelsestype split — all home help in care homes combined. Compare laby20 (servyd=310) for the equivalent percentage of the population.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
