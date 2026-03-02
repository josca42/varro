table: fact.sao02
description: Øvrige arbejdsomkostninger for virksomheder og organisationer  pr. præsteret time efter branche (DB07), lønkomponenter, lønmodtagergruppe og tid
measure: indhold (unit Kr.)
columns:
- branche07: join dim.db_10 on branche07=kode::text [approx]; levels [1]
- lonmal: values [LUA=Lønomkostning for hjemsendelse men uden mulighed for at arbejde, TOT=I alt, OKB=Bidrag til offentlige kasser, OKR=Refusion fra offentlige kasser, ALO=Andre lovpligtige omkostninger (netto), ABB=Aftalebestemte bidrag, ABR=Aftalebestemt refusion, UDD=Uddannelse, APO=Andre personale omkostninger]
- offgrp: values [TOT=I alt, VOK=I alt, ekskl. unge og elever, LED=Ledere, MED=Lønmodtagere uden ledelsesansvar, UNG=Unge (13-17 år), ELE=Elever]
- tid: date range 2014-01-01 to 2023-01-01
dim docs: /dim/db_10.md

notes:
- sao02 covers only "øvrige arbejdsomkostninger" (other/non-wage labor costs) — the lonmal values are cost sub-types of OVROMK (not earnings components). TOT here = total øvrige, not total labor cost. Don't mix with sao01 lonmal values.
- lonmal breakdown: OKB=public contributions, OKR=public reimbursements (negative), ALO=other statutory costs (net), ABB=collectively agreed contributions, ABR=collectively agreed reimbursements, UDD=training, APO=other personnel costs, LUA=lay-off cost, TOT=sum. Never sum across lonmal.
- indhold is Kr. per præsteret time (rate). Same rate-vs-count caveat as sao01 — don't sum across sectors.
- branche07 same as sao01: niveau 1 only, sectors 2–8, 10 + TOT + O3 (custom code, not in dim). Use WHERE branche07 NOT IN ('TOT', 'O3') with the dim join.
- offgrp: same structure as sao01 (TOT, VOK, LED, MED, UNG, ELE). Filter to offgrp='TOT' for overall.
- No kon column (unlike sao01/sao03).
- sao02 ends at 2023; sao01 extends to 2024. Use sao01 lonmal='OVROMK' if you only need the øvrige total up to 2024.