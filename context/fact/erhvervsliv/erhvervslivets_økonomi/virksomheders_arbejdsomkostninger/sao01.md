table: fact.sao01
description: Samlede arbejdsomkostninger for virksomheder og organisationer pr. præsteret time efter branche (DB07), lønkomponenter, lønmodtagergruppe, køn og tid
measure: indhold (unit Kr.)
columns:
- branche07: join dim.db_10 on branche07=kode::text [approx]; levels [1]
- lonmal: values [TOT=Samlede arbejdsomkostninger, OVROMK=Øvrige arbejdsomkostninger, LUA=Lønomkostning for hjemsendelse men uden mulighed for at arbejde, FORINKL=FORTJENESTE PR. PRÆSTERET TIME, OVERB=Overtidstillæg pr. præsteret time, SYGDOM=Fraværsbetalinger pr. præsteret time, GENE=Genetillæg pr. præsteret time, GODE=Personalegoder pr. præsteret time, UREGEL=Uregelmæssige betalinger pr. præsteret time, PENS=Pension inkl. ATP pr. præsteret time, BASIS=Basisfortjenesten pr. præsteret time]
- offgrp: values [TOT=I alt, VOK=I alt, ekskl. unge og elever, LED=Ledere, MED=Lønmodtagere uden ledelsesansvar, UNG=Unge (13-17 år), ELE=Elever]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2014-01-01 to 2024-01-01
dim docs: /dim/db_10.md

notes:
- indhold is Kr. per præsteret time (labor cost rate, not a count). Summing across branches produces a sum of rates — meaningless unless weighted by hours. Compare rates, don't aggregate them.
- lonmal is a decomposition selector — never sum across its values. TOT = total labor cost. FORINKL (earnings) + OVROMK (other costs) = TOT. BASIS, OVERB, SYGDOM, GENE, GODE, UREGEL, PENS, LUA are sub-components of FORINKL. Pick one lonmal value per query; omitting a filter silently inflates by 10x.
- offgrp is also a selector: TOT = all workers, VOK = excl. unge/elever, LED = managers, MED = employees without management responsibility, UNG = young (13-17), ELE = apprentices. VOK is NOT a sub-group of TOT in an additive sense — rates can differ (VOK > TOT because young workers have lower cost rates). Filter to offgrp='TOT' for the overall figure.
- kon: TOT, M, K. Filter to kon='TOT' for total.
- branche07 joins dim.db_10 at niveau 1 only (all fact codes are single-digit). Use ColumnValues("db_10", "titel", for_table="sao01") to see available sectors. The fact table covers sectors 2–8, 10, plus TOT and O3 — sectors 1 (Landbrug), 9 (Offentlig administration), and 11 (Uoplyst) are absent.
- O3 is a custom code not in dim.db_10. It appears to group public/other sectors not covered individually. Exclude O3 from joins or handle it as a labeled special case: WHERE branche07 NOT IN ('TOT', 'O3').
- Minimal correct query: SELECT d.titel, f.indhold FROM fact.sao01 f JOIN dim.db_10 d ON f.branche07 = d.kode::text WHERE d.niveau = 1 AND f.lonmal='TOT' AND f.offgrp='TOT' AND f.kon='TOT' AND f.tid='2024-01-01'.