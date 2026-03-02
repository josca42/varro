table: fact.aed02
description: Hjemmehjælp, leveret tid pr. person efter område, ydelsestype, alder, køn og tid
measure: indhold (unit Gns. antal timer pr. uge)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- ydelsestype: values [50=Leverede timer i alt, 100=Leverede timer til personlig pleje, i alt, 150=Leverede timer til praktisk hjælp, i alt, 200=Leverede timer til modtagere der udelukkende modtager personlig pleje, 250=Leverede timer til modtagere der udelukkende modtager praktisk hjælp, 300=Leverede timer til modtagere af både personlig pleje og praktisk hjælp i alt, 350=Leverede timer til personlig pleje til modtagere af både personlig pleje og praktisk hjælp, 400=Leverede timer til praktisk hjælp til modtagere af både personlig pleje og praktisk hjælp]
- alder: values [50=Alder i alt, 100=Under 65 år, 200=65-66 år, 300=67-69 år, 850=67 år og derover, 400=70-74 år, 500=75-79 år, 600=80-84 år, 700=85-89 år, 800=90 år og derover]
- koen: values [100=Mænd og kvinder i alt, 200=Mænd, 300=Kvinder]
- tid: date range 2011-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- indhold is average (Gns. antal timer pr. uge per person) — do not sum across rows.
- Leveret (delivered) per person — compare with aed021 for visiteret (authorized) per person. Data from 2011.
- omrade joins dim.nuts with both niveau 1 (5 regioner) and niveau 3 (98 kommuner). Filter WHERE d.niveau=3 or d.niveau=1. omrade=0 is national total (not in dim).
- ydelsestype nested hierarchy same as aed01: 50=i alt; never sum across values. Filter ydelsestype=50 for the overall per-person average.
- alder=50 is overall total; alder=850 is the 67+ sub-total — do not mix with individual bands. koen=100 is total.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
