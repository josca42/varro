table: fact.dnpnogl
description: Nøgletal for pengeinstitutter efter nøgletal, rapporterende institut, sektor for korrigeret udlån og tid
measure: indhold (unit -)
columns:
- aktp: values [INDLUNDPI=Indlånsoverskud (mio. kr.), INDLUNDREPOKORRPI=Indlånsoverskud korrigeret for repoforretninger (mio. kr.), CR5PIPI=Koncentrationsindeks CR5 (indeks), HERFINPIPI=Koncentrationsindeks Herfindahl-indeks (indeks)]
- rapinst: values [ALLE=Alle pengeinstitutter]
- sekkornat: values [1000A1=X000: Alle sektorer i ind- og udland, 1100DK=- heraf 1100: Indenlandske ikke-finansielle selskaber, 1400DK=- heraf 1400: Indenlandske husholdninger]
- tid: date range 2013-10-01 to 2025-09-01

notes:
- aktp contains 4 heterogeneous metrics with different units: INDLUNDPI and INDLUNDREPOKORRPI are mio. kr. (deposit surplus); CR5PIPI and HERFINPIPI are index values. Never sum or average across aktp.
- sekkornat uses compound sector+country codes (1000A1=all sectors worldwide, 1100DK/1400DK=specific domestic sector). These do not join to dim.esr_sekt; treat as inline values.
- rapinst only has ALLE — no individual bank breakdowns in this table.