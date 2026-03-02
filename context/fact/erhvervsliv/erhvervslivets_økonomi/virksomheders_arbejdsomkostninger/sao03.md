table: fact.sao03
description: Samlede arbejdsomkostninger for virksomheder og organisationer pr. præsteret time efter arbejdsfunktion, lønkomponenter, lønmodtagergruppe, køn og tid
measure: indhold (unit Kr.)
columns:
- arbf: join dim.disco on arbf=kode::text [approx]; levels [1, 2]
- lonmal: values [TOT=Samlede arbejdsomkostninger, OVROMK=Øvrige arbejdsomkostninger, LUA=Lønomkostning for hjemsendelse men uden mulighed for at arbejde, FORINKL=FORTJENESTE PR. PRÆSTERET TIME, OVERB=Overtidstillæg pr. præsteret time, SYGDOM=Fraværsbetalinger pr. præsteret time, GENE=Genetillæg pr. præsteret time, GODE=Personalegoder pr. præsteret time, UREGEL=Uregelmæssige betalinger pr. præsteret time, PENS=Pension inkl. ATP pr. præsteret time, BASIS=Basisfortjenesten pr. præsteret time]
- offgrp: values [TOT=I alt, VOK=I alt, ekskl. unge og elever, LED=Ledere, MED=Lønmodtagere uden ledelsesansvar, UNG=Unge (13-17 år), ELE=Elever]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2014-01-01 to 2024-01-01
dim docs: /dim/disco.md

notes:
- CRITICAL: arbf codes 1, 2, 3 match BOTH niveau 1 AND niveau 2 in dim.disco (single-digit codes collide between levels). A join without WHERE d.niveau = 1 returns 2 rows for each of arbf 1, 2, 3, doubling their indhold. Always add WHERE d.niveau = 1.
- arbf codes in this table are 1–9 (niveau 1 of DISCO-08: main occupational groups) plus TOT. Use ColumnValues("disco", "titel", for_table="sao03") to see labels. disco has 5 hierarchy levels but only niveau 1 is used here.
- indhold is Kr. per præsteret time (rate). Same caveat as sao01 — don't sum across job functions.
- lonmal is a decomposition selector: same breakdown as sao01 (TOT, FORINKL, OVROMK, BASIS, etc). Pick one; FORINKL + OVROMK = TOT.
- offgrp: TOT, VOK, LED, MED, UNG, ELE. Filter to offgrp='TOT' for overall.
- kon: TOT, M, K. Filter to kon='TOT' for total.
- Minimal correct query: SELECT d.titel, f.indhold FROM fact.sao03 f JOIN dim.disco d ON f.arbf = d.kode::text WHERE d.niveau = 1 AND f.lonmal='TOT' AND f.offgrp='TOT' AND f.kon='TOT' AND f.tid='2024-01-01'.