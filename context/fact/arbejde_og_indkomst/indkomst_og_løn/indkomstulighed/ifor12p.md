table: fact.ifor12p
description: Personer i Lavindkomst familier efter kommune, indkomstniveau og tid
measure: indhold (unit Pct.)
columns:
- kommunedk: join dim.nuts on kommunedk=kode [approx]; levels [3]
- indkn: values [50=50 procent af medianindkomsten, 60=60 procent af medianindkomsten]
- tid: date range 2000-01-01 to 2023-01-01
dim docs: /dim/nuts.md
notes:
- indkn is a threshold selector: the table has two separate poverty-line definitions (50% or 60% of median income). Always filter to one: indkn = '60' is the EU standard (most common). Forgetting this doubles all counts.
- kommunedk code 0 = Danmark i alt (not in dim.nuts). All other codes join dim.nuts at niveau=3 (kommuner).
- indhold is Pct. — the share of people in low-income families in that kommune. See ifor12a for the same table in absolute counts (Antal).
- Sample query (share of low-income by kommune, 60% threshold, 2023): SELECT d.titel, f.indhold FROM fact.ifor12p f JOIN dim.nuts d ON f.kommunedk = d.kode::int WHERE f.indkn = '60' AND f.tid = '2023-01-01' AND f.kommunedk != 0 ORDER BY f.indhold DESC;
- Map: context/geo/kommuner.parquet — merge on kommunedk=dim_kode. Exclude kommunedk=0.
