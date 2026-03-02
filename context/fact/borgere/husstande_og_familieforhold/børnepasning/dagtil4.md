table: fact.dagtil4
description: Modtagere af tilskud vedr. privat pasning og pasning af egne børn efter område, tilskudsart, berørte og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [3]
- tilskudsart: values [30=Forældre, der vælger privat pasning, 31=Pasning af egne børn]
- berort: values [32=Børn, 33=Familier]
- tid: date range 2008-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- omrade contains kode 0 (national total, not in dim.nuts) and niveau 3 (98 kommuner) only — no regional breakdown.
- tilskudsart (30=privat pasning, 31=egne børn) and berort (32=børn, 33=familier) are fully orthogonal — there are NO total rows. Each of the 4 combinations is a distinct count. Do not sum across tilskudsart or berort to get a total (families receiving both subsidies would be double-counted).
- To get total children receiving any childcare subsidy, query berort=32 for each tilskudsart separately and note they may overlap.
- Longest time series in this subject: 2008-2024. Useful for long-run trend analysis of alternative childcare subsidies.
- Map: context/geo/kommuner.parquet — merge on omrade=dim_kode. Exclude omrade=0.
