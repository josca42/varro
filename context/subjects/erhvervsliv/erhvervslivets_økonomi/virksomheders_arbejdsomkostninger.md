<fact tables>
<table>
id: sao01
description: Samlede arbejdsomkostninger for virksomheder og organisationer pr. præsteret time efter branche (DB07), lønkomponenter, lønmodtagergruppe, køn og tid
columns: branche07, lonmal, offgrp, kon, tid (time), indhold (unit Kr.)
tid range: 2014-01-01 to 2024-01-01
</table>
<table>
id: sao02
description: Øvrige arbejdsomkostninger for virksomheder og organisationer  pr. præsteret time efter branche (DB07), lønkomponenter, lønmodtagergruppe og tid
columns: branche07, lonmal, offgrp, tid (time), indhold (unit Kr.)
tid range: 2014-01-01 to 2023-01-01
</table>
<table>
id: sao03
description: Samlede arbejdsomkostninger for virksomheder og organisationer pr. præsteret time efter arbejdsfunktion, lønkomponenter, lønmodtagergruppe, køn og tid
columns: arbf, lonmal, offgrp, kon, tid (time), indhold (unit Kr.)
tid range: 2014-01-01 to 2024-01-01
</table>
<table>
id: sao04
description: Øvrige arbejdsomkostninger for virksomheder og organisationer pr. præsteret time efter arbejdsfunktion, lønkomponenter, lønmodtagergruppe og tid
columns: arbf, lonmal, offgrp, tid (time), indhold (unit Kr.)
tid range: 2014-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- All four tables measure Kr. per præsteret time (labor cost rates, not headcounts). Do not sum indhold across rows — compare rates or use a single filtered row per category.
- All tables share the same critical filter pattern: pick exactly one value for each of lonmal, offgrp, (and kon in sao01/sao03) to get a single non-overlapping figure. Forgetting any one of these silently multiplies the result.
- sao01 and sao02 break down by branche (DB07 10-groupering, niveau 1 only). sao03 and sao04 break down by arbejdsfunktion (DISCO-08 niveau 1, 9 main groups).
- sao01/sao03 = total labor costs (all components). sao02/sao04 = øvrige (non-wage) costs only, with a finer sub-breakdown of those costs.
- sao01 and sao03 extend to 2024; sao02 and sao04 only to 2023. Prefer sao01/sao03 for current data; use sao02/sao04 when you need the detailed øvrige sub-breakdown.
- branche07 join gotcha (sao01/sao02): O3 is a custom sector code not in dim.db_10 — exclude it from dim joins. Sectors 1 (Landbrug), 9 (Offentlig administration), 11 (Uoplyst) are not present individually.
- arbf join gotcha (sao03/sao04): disco codes 1, 2, 3 match both niveau 1 and niveau 2 in dim.disco. Always add WHERE d.niveau = 1 — without it, rows for arbf 1/2/3 are duplicated.