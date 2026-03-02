table: fact.aed21
description: Serviceindikatorer, andel af befolkning på 67 år og derover efter område, serviceydelser og tid
measure: indhold (unit Pct.)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- servyd: values [130=Modtagere 67 år og derover af leveret hjemmehjælp i eget hjem (procent af befolkningen), 140=Modtagere 67 år og derover af visiteret hjemmehjælp i eget hjem (procent af befolkningen), 150=Plejehjemsbeboere 67 år og derover (procent af befolkningen), 160=Modtagere af træning 67 år og derover (procent af befolkningen), 170=Modtagere af forebyggende hjemmebesøg 75 år og derover (procent af befolkningen)]
- tid: date range 2008-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts niveau 3 only (98 kommuner). omrade=0 is the national total — use it directly without a JOIN. ColumnValues("nuts", "titel", for_table="aed21") lists the 98 kommuner.
- servyd contains 5 independent service indicators, each a separate percentage of the 67+ population. Never sum across servyd — each is its own metric. Pick the one relevant to the question and filter to it.
- Simple 2-column table (omrade × servyd): for a single indicator over all kommuner, just filter servyd and tid. No alder/koen/ydelsestype to manage.
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.
