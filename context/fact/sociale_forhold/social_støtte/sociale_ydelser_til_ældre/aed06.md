table: fact.aed06
description: Hjemmehjælp, visiterede personer efter område, ydelsestype, timer pr. uge, alder, køn og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- ydelsestype: values [100=Modtagere af hjemmehjælp i alt, 200=Modtagere der udelukkende modtager personlig pleje, 300=Modtagere der udelukkende modtager praktisk hjælp, 400=Modtagere af både personlig pleje og praktisk hjælp, 450=Modtagere der udelukkende modtager madservice (2023-)]
- timeuge: values [50=Omfang i alt, 100=Under 2 timer, 200=2 - 3,9 timer, 300=4 - 7,9 timer, 400=8 - 11,9 timer, 500=12 - 19,9 timer, 600=Mere end 20 timer]
- alder: values [50=Alder i alt, 100=Under 65 år, 200=65-66 år, 300=67-69 år, 850=67 år og derover, 400=70-74 år, 500=75-79 år, 600=80-84 år, 700=85-89 år, 800=90 år og derover]
- koen: values [100=Mænd og kvinder i alt, 200=Mænd, 300=Kvinder]
- tid: date range 2008-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts with both niveau 1 (5 regioner) and niveau 3 (98 kommuner). Filter WHERE d.niveau=3 for kommuner, d.niveau=1 for regioner. omrade=0 is national total (not in dim).
- ydelsestype: 100=i alt; 200/300/400 are mutually exclusive care-type categories, so 200+300+400=100. ydelsestype=450 (madservice only) from 2023 and separate from 100. Filter ydelsestype=100 for total person count.
- timeuge: 50=i alt; 100-600 are mutually exclusive hour bands that sum to 50. For a simple count of persons, filter timeuge=50 — forgetting this will multiply counts by 7.
- alder=50 is overall total; alder=850 is the 67+ sub-total. Do not mix with individual bands.
- koen=100 is total. Always filter all total codes to get a single non-duplicated count.
- For the number of persons receiving home help use this table (aed06); for hours use aed022.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
