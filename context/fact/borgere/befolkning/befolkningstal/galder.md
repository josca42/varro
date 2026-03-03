table: fact.galder
description: Gennemsnitsalder efter kommune, køn og tid
measure: indhold (unit Gns.)
columns:
- komk: join dim.nuts on komk=kode; levels [1, 3]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2005-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- indhold is average age — a mean, not a count. Do NOT SUM across komk. To compare geographies, SELECT individual rows; to aggregate up, use population-weighted average (requires joining folk1a counts).
- komk has both niveau=1 (5 regioner) and niveau=3 (99 kommuner) plus komk=0 (Hele landet, not in dim.nuts). Always filter to one level to avoid mixing granularities.
- kon='TOT' for overall average age; filter komk to one geographic code.
- Longest average age series: back to 2005. For parish-level average age use kmgalder (back to 2007).
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on komk=dim_kode. Exclude komk=0.