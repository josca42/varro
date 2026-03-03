table: fact.idrfin02
description: Kommunale udgifter (Kr.) pr. indbygger til idræt efter område, funktion, dranst og tid
measure: indhold (unit Kr. pr. indb.)
columns:
- amt: join dim.nuts on amt=kode; levels [2, 3]
- funktion: values [TOT=I alt, 03231=0.32.31 Stadion og idrætsanlæg, 03235=0.32.35 Andre fritidsfaciliteter, 32218=3.22.18 Idrætsfaciliteter for børn og unge]
- dranst: values [TOT=I alt, 12=12 Driftskonti inkl. statsrefusion, 3=3 Anlægskonti]
- tid: date range 2011-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- amt joins dim.nuts. Same structure as idrfin01 (omrade): niveau 2 (11 landsdele) and niveau 3 (98 kommuner). amt='0' is the national average — not in dim.nuts.
- Measure is Kr. pr. indb. (per capita), not total. Do not sum across kommuner — use the per-capita value per row directly for comparisons.
- funktion and dranst both have totals (TOT). Filter to TOT in both unless breaking down by function or account type.
- For comparing municipalities: JOIN dim.nuts WHERE d.niveau=3, filter funktion='TOT' AND dranst='TOT'. This gives one per-capita figure per kommune per year.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/landsdele.parquet (niveau 2) — merge on amt=dim_kode. Exclude amt=0.
