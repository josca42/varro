table: fact.idrfin01
description: Kommunale udgifter (1000 kr.) til idræt efter område, funktion, dranst og tid
measure: indhold (unit 1.000 kr.)
columns:
- omrade: join dim.nuts on omrade=kode; levels [2, 3]
- funktion: values [TOT=I alt, 03231=0.32.31 Stadion og idrætsanlæg, 03235=0.32.35 Andre fritidsfaciliteter, 32218=3.22.18 Idrætsfaciliteter for børn og unge]
- dranst: values [TOT=I alt, 12=12 Driftskonti inkl. statsrefusion, 3=3 Anlægskonti]
- tid: date range 2011-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts. The table has niveau 2 (11 landsdele) and niveau 3 (98 kommuner). omrade='0' is the national aggregate — not in dim.nuts. Use ColumnValues("nuts", "titel", for_table="idrfin01") to browse available areas.
- To get a total for Denmark, filter omrade='0'. To get kommuner, JOIN dim.nuts and filter WHERE d.niveau=3. Mixing niveaus in the same query risks double-counting.
- funktion and dranst both have totals (TOT). Filter to TOT in both unless you specifically want breakdown by function or account type. Forgetting either multiplies rows.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.
