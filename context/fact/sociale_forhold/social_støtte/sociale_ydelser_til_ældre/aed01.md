table: fact.aed01
description: Hjemmehjælp, leveret tid efter område, ydelsestype, alder, køn og tid
measure: indhold (unit Timer pr. uge)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- ydelsestype: values [50=Leverede timer i alt, 100=Leverede timer til personlig pleje, i alt, 150=Leverede timer til praktisk hjælp, i alt, 200=Leverede timer til modtagere der udelukkende modtager personlig pleje, 250=Leverede timer til modtagere der udelukkende modtager praktisk hjælp, 300=Leverede timer til modtagere af både personlig pleje og praktisk hjælp i alt, 350=Leverede timer til personlig pleje til modtagere af både personlig pleje og praktisk hjælp, 400=Leverede timer til praktisk hjælp til modtagere af både personlig pleje og praktisk hjælp]
- alder: values [50=Alder i alt, 100=Under 65 år, 200=65-66 år, 300=67-69 år, 400=70-74 år, 500=75-79 år, 600=80-84 år, 700=85-89 år, 800=90 år og derover]
- koen: values [100=Mænd og kvinder i alt, 200=Mænd, 300=Kvinder]
- tid: date range 2011-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- Leveret (delivered) hours — compare with aed022 for visiteret (authorized) hours. Data from 2011 (aed022 goes back to 2008).
- omrade joins dim.nuts with both niveau 1 (5 regioner) and niveau 3 (98 kommuner). Filter WHERE d.niveau=3 for kommuner, d.niveau=1 for regioner. omrade=0 is national total (not in dim).
- ydelsestype nested hierarchy: 50=i alt; 100=personlig pleje i alt = 200+350; 150=praktisk hjælp i alt = 250+400; 300=both types i alt includes 350+400. Never sum across ydelsestype. For total delivered hours filter ydelsestype=50.
- alder=50 is total; age bands 100-800 are non-overlapping. koen=100 is total.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
