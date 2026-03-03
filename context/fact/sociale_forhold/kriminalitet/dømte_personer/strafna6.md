table: fact.strafna6
description: Skyldige personer efter område, køn, alder, national oprindelse og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- kon: values [M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 15-29=15-29 år, 30-49=30-49 år, 50-79=50-79 år]
- herkomst1: values [1=Personer med dansk oprindelse, 6=Personer med udenlandsk oprindelse]
- tid: date range 2005-01-01 to 2023-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at niveau 1 (5 regioner) and niveau 3 (99 kommuner). Code 0 (I alt) is not in the dim — exclude or handle separately. Filter WHERE d.niveau=1 for regions or niveau=3 for kommuner.
- 4 non-tid dimensions: omrade, kon, alder, herkomst1. To get a simple total for a region: filter kon to sum M+K, alder=TOT, and sum herkomst1 values (no aggregate — only 1=dansk og 6=udenlandsk).
- herkomst1 has only 2 values (1=Personer med dansk oprindelse, 6=Personer med udenlandsk oprindelse) — no total row. Sum both for total. This is a coarser origin split than the herkomst column in strafna9/strfna10/strfna11.
- alder TOT is aggregate — filter to one level.
- kon has only M and K — no total row.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
- Map: kommune data (niveau 3) can be aggregated to politikredse via dim.politikredse (niveau 2 = kommuner, niveau 1 = 12 politikredse). Use /geo/politikredse.parquet for boundaries.
