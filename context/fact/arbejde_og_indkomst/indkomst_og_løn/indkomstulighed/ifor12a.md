table: fact.ifor12a
description: Personer i Lavindkomst familier efter kommune, indkomstniveau og tid
measure: indhold (unit Antal)
columns:
- kommunedk: join dim.nuts on kommunedk=kode [approx]; levels [3]
- indkn: values [50=50 procent af medianindkomsten, 60=60 procent af medianindkomsten]
- tid: date range 2000-01-01 to 2023-01-01
dim docs: /dim/nuts.md
notes:
- indkn is a threshold selector (50% or 60% of median income). Always filter to one: indkn = '60' is standard. Forgetting doubles all counts.
- kommunedk code 0 = Danmark i alt (not in dim.nuts). All other codes join dim.nuts at niveau=3 (kommuner).
- indhold is Antal (absolute count of low-income persons). See ifor12p for the same table as percentages (Pct.).
- Map: /geo/kommuner.parquet — merge on kommunedk=dim_kode. Exclude kommunedk=0.
