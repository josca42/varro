table: fact.rehab19
description: Rehabilitering, personer efter område, alder, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- alder1: values [50=Alder i alt, 100=Under 65 år, 375=65-69 år, 400=70-74 år, 500=75-79 år, 600=80-84 år, 700=85-89 år, 800=90 år og derover]
- koen: values [100=Mænd og kvinder i alt, 200=Mænd, 300=Kvinder]
- tid: date range 2019-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts niveau 3 only (98 kommuner, no regional breakdown). omrade=0 not in fact table — all rows are at kommune level.
- Age column is named alder1 (not alder). alder1=50 is total; bands 100/375/400-800 are non-overlapping. Note: 65-69 år uses code 375 (not 6569 as in other tables).
- koen=100 is total. For total rehabilitering persons per kommune: filter alder1=50 and koen=100.
- Data from 2019 only. Rehabilitering is distinct from genoptræning/vedligeholdelsestræning (see aed08).
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.
