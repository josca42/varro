table: fact.smdbv002
description: Stofmisbrugsbehandling efter område, nøgletal og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- aktp: values [KTKFORL=Kontaktforløb, BEHFORL=Behandlingsforløb, PERSBEH=Personer i behandling]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts. Same structure as smdbv001: niveau 1 = 5 regioner (kode 81-85), niveau 3 = 98 kommuner. omrade = '0' is national total, not in dim — query directly with WHERE f.omrade = '0'. Filter to a single niveau to avoid double-counting.
- aktp has 3 distinct metrics: KTKFORL (kontaktforløb), BEHFORL (behandlingsforløb), PERSBEH (personer i behandling). These measure different aspects of treatment activity and are close in magnitude but not identical — do not sum them. Always filter to one aktp value.
- This table covers the same metrics as smdbv003 but WITH regional breakdown (no gender/age). Use smdbv002 when geography matters; use smdbv003 for gender/age breakdown.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.