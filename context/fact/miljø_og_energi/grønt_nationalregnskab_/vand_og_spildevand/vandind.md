table: fact.vandind
description: Indvinding af vand efter område, vandtype, indvindingskategori og tid
measure: indhold (unit Mio. m3)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- vandtyp: values [TOTVAND=Vand i alt, GVAND=Grundvand, OVAND=Overfladevand]
- indkat: values [100=Alment vandværk, 105=Virksomheder med egen indvinding, 110=Markvanding]
- tid: date range 1989-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts on omrade=kode. niveau 1 = 5 regioner (kode 81-85), niveau 3 = 99 kommuner. omrade='0' = Danmark i alt (not in dim — use WHERE f.omrade='0' for the national total).
- vandtyp is hierarchical: TOTVAND = GVAND + OVAND. Filter to one value to avoid double-counting.
- indkat (100/105/110) are independent source categories — safe to sum or filter individually.
- Longest water abstraction series in this subject (1989–2023) and the only one with regional breakdown. Use for geography questions; use vandrg1 for industry breakdown.
- Sample: groundwater abstraction by region in 2023:
  SELECT d.titel, sum(f.indhold) FROM fact.vandind f JOIN dim.nuts d ON f.omrade=d.kode WHERE f.vandtyp='GVAND' AND d.niveau=1 AND f.tid='2023-01-01' GROUP BY d.titel;
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
