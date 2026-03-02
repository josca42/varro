table: fact.aed14
description: Hjemmehjælp, visiterede personer der skifter mellem privat og kommunal leverandør efter område, ydelsestype, alder, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- ydelsestype: values [100=Modtagere af hjemmehjælp i alt, 200=Modtagere der udelukkende modtager personlig pleje, 300=Modtagere der udelukkende modtager praktisk hjælp, 400=Modtagere af både personlig pleje og praktisk hjælp, 450=Modtagere der udelukkende modtager madservice (2023-)]
- alder: values [50=Alder i alt, 100=Under 65 år, 200=65-66 år, 300=67-69 år, 400=70-74 år, 500=75-79 år, 600=80-84 år, 700=85-89 år, 800=90 år og derover]
- koen: values [100=Mænd og kvinder i alt, 200=Mænd, 300=Kvinder]
- tid: date range 2009-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- This table counts persons who switch between private and municipal provider (not all recipients). Use aed06 for total visiterede persons and aed12 for the percentage using private providers.
- omrade joins dim.nuts with both niveau 1 (5 regioner) and niveau 3 (98 kommuner). Filter WHERE d.niveau=3 for kommuner, d.niveau=1 for regioner. omrade=0 is national total (not in dim).
- ydelsestype: 100=i alt; 200/300/400 are mutually exclusive care types. Filter ydelsestype=100 for total switchers. 450 (madservice) only from 2023.
- alder=50 is total; alder bands 100-800 are non-overlapping. koen=100 is total.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
