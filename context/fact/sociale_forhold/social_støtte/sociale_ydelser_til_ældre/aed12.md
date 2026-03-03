table: fact.aed12
description: Hjemmehjælp, visiterede personer der benytter privat leverandør efter område, ydelsestype, alder, køn og tid
measure: indhold (unit Pct.)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- ydelsestype: values [100=Modtagere af hjemmehjælp i alt, 200=Modtagere der udelukkende modtager personlig pleje, 300=Modtagere der udelukkende modtager praktisk hjælp, 400=Modtagere af både personlig pleje og praktisk hjælp, 450=Modtagere der udelukkende modtager madservice (2023-)]
- alder: values [50=Alder i alt, 100=Under 65 år, 200=65-66 år, 300=67-69 år, 850=67 år og derover, 400=70-74 år, 500=75-79 år, 600=80-84 år, 700=85-89 år, 800=90 år og derover]
- koen: values [100=Mænd og kvinder i alt, 200=Mænd, 300=Kvinder]
- tid: date range 2008-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- indhold is a percentage (pct. of visiterede persons using private provider). Do not sum across rows.
- omrade joins dim.nuts with both niveau 1 (5 regioner) and niveau 3 (98 kommuner). Filter WHERE d.niveau=3 or d.niveau=1. omrade=0 is national total (not in dim).
- ydelsestype: 100=i alt; 200/300/400 are mutually exclusive care types. Each gives the private-provider share within that care type. Never sum percentages across ydelsestype.
- alder=50 is total; alder=850 is 67+ sub-total. Do not mix with individual bands. koen=100 is total.
- Compare with aed012 for the equivalent percentage for leveret (delivered) rather than visiteret (authorized) help.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
