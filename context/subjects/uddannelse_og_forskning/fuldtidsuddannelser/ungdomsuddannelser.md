<fact tables>
<table>
id: uddakt30
description: Uddannelsesaktivitet på gymnasiale uddannelser efter uddannelse, bopælsregion, herkomst, national oprindelse, køn, status og tid
columns: uddannelse, bopreg, herkomst, herkomst1, kon, fstatus, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: uddakt34
description: Uddannelsesaktivitet på erhvervsfaglige uddannelser efter uddannelse, alder, herkomst, national oprindelse, køn, status, uddannelsesdel og tid
columns: uddannelse, alder, herkomst, herkomst1, kon, fstatus, udddl, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: eud34
description: Uddannelsesaktivitet på erhvervsfaglige uddannelser efter uddannelse, alder, herkomst, national oprindelse, køn, status, uddannelsesdel og tid
columns: uddannelse, alder, herkomst, herkomst1, kon, fstatus, udddl, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: uddakt35
description: Uddannelsesaktivitet på erhvervsfaglige uddannelser efter uddannelse, alder, herkomst, national oprindelse, køn, status, uddannelsesform og tid
columns: uddannelse, alder, herkomst, herkomst1, kon, fstatus, uddform, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: laby48
description: Gennemsnitlig afstand til ungdomsuddannelse efter kommunegruppe, uddannelse og tid
columns: komgrp, uddannelse, tid (time), indhold (unit Km)
tid range: 2008-01-01 to 2021-01-01
</table>
</fact tables>

notes:
- For gymnasiale uddannelser (STX, HF, HTX, HHX, GS, …): use uddakt30. It has regional breakdown (bopreg = 5 regioner), herkomst, and køn. Only niveau=1 regions available — no kommune-level.
- For erhvervsfaglige uddannelser (EUD/EUX): use uddakt34, uddakt35, or eud34. None has regional breakdown.
  - uddakt34: breaks by uddannelsesdel (grundforløb 1/2, hovedforløb, EUX-forløb). Use when you need the course-part split.
  - uddakt35: breaks by uddannelsesform (training pathway: Mesterlære, EUD praktikvej/skolevej, EUX variants). Use when comparing practical vs. school pathways.
  - eud34: same dimensions as uddakt34 but uses a different numeric uddannelse classification (1–4 digit) vs H-prefix codes. Fewer rows (~1.7M vs ~5M). Use when the numeric classification is needed; otherwise prefer uddakt34.
- For geographic accessibility (how far do students travel?): use laby48. It gives average distance in km by kommunegruppe (5 groups) and education type. Covers 2008–2021 only.
- All four enrollment tables share the same fstatus column: B=enrolled 1. okt., F=fuldført, T=tilgang. Always filter to exactly one fstatus — the values represent different phenomena, not additive categories.
- All uddannelse columns are hierarchical (code length encodes level). Always pick one level to avoid double-counting parent and child rows.
- Map: uddakt30 supports regional choropleth via context/geo/regioner.parquet — merge on bopreg=dim_kode, exclude bopreg IN (0, 999). No other table in this subject has a geographic column.