table: fact.sao04
description: Øvrige arbejdsomkostninger for virksomheder og organisationer pr. præsteret time efter arbejdsfunktion, lønkomponenter, lønmodtagergruppe og tid
measure: indhold (unit Kr.)
columns:
- arbf: join dim.disco on arbf=kode::text [approx]; levels [1, 2]
- lonmal: values [LUA=Lønomkostning for hjemsendelse men uden mulighed for at arbejde, TOT=I alt, OKB=Bidrag til offentlige kasser, OKR=Refusion fra offentlige kasser, ALO=Andre lovpligtige omkostninger (netto), ABB=Aftalebestemte bidrag, ABR=Aftalebestemt refusion, UDD=Uddannelse, APO=Andre personale omkostninger]
- offgrp: values [TOT=I alt, VOK=I alt, ekskl. unge og elever, LED=Ledere, MED=Lønmodtagere uden ledelsesansvar, UNG=Unge (13-17 år), ELE=Elever]
- tid: date range 2014-01-01 to 2023-01-01
dim docs: /dim/disco.md

notes:
- CRITICAL: Same disco join issue as sao03 — arbf codes 1, 2, 3 match both niveau 1 and niveau 2 in dim.disco. Always add WHERE d.niveau = 1.
- sao04 covers only "øvrige arbejdsomkostninger" by job function. Same lonmal breakdown as sao02: TOT, OKB, OKR, ALO, ABB, ABR, UDD, APO, LUA. Never sum across lonmal.
- No kon column (unlike sao03).
- sao04 ends at 2023; sao03 extends to 2024. For øvrige total up to 2024, use sao03 with lonmal='OVROMK'.
- offgrp: TOT, VOK, LED, MED, UNG, ELE. Filter to offgrp='TOT' for overall.