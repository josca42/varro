<fact tables>
<table>
id: uddakt40
description: Uddannelsesaktivitet på korte videregående uddannelser efter uddannelse, alder, herkomst, national oprindelse, køn, status og tid
columns: uddannelse, alder, herkomst, herkomst1, kon, fstatus, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: uddakt50
description: Uddannelsesaktivitet på mellemlange videregående  uddannelser efter uddannelse, alder, herkomst, national oprindelse, køn, status og tid
columns: uddannelse, alder, herkomst, herkomst1, kon, fstatus, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: uddakt60
description: Uddannelsesaktivitet på bacheloruddannelser efter uddannelse, alder, herkomst, national oprindelse, køn, status og tid
columns: uddannelse, alder, herkomst, herkomst1, kon, fstatus, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: uddakt70
description: Uddannelsesaktivitet på lange videregående uddannelser efter uddannelse, alder, herkomst, national oprindelse, køn, status og tid
columns: uddannelse, alder, herkomst, herkomst1, kon, fstatus, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: laby52
description: Gennemsnitlig afstand til videregående uddannelse efter kommunegruppe, uddannelse og tid
columns: komgrp, uddannelse, tid (time), indhold (unit Km)
tid range: 2008-01-01 to 2021-01-01
</table>
</fact tables>

notes:
- uddakt40/50/60/70 cover the 4 education levels: uddakt40=KVU (korte, 2 years), uddakt50=MVU (mellemlange, 3-4 years), uddakt60=BACH (bachelors, 3 years), uddakt70=LVU (lange, 5+ years). Pick the table matching the education level in the question.
- All four uddakt tables share identical column structure and the same critical pitfalls — fstatus inflates counts 3x if not filtered, and uddannelse hierarchy causes double-counting if levels are mixed.
- fstatus must always be filtered: B=enrolled Oct 1 (stock), F=completed (flow), T=new intake (flow). Omitting fstatus silently triples every count.
- uddannelse codes encode both the education level and hierarchy depth via code length. len=3 is the single top-level total (e.g. H40), len=5 is main subject area, len=7 is specific program. Use LENGTH(uddannelse) to filter to a single level.
- herkomst (origin type) and herkomst1 (national region) are cross-tabulated. When analyzing one, filter the other to TOT. Never GROUP BY both simultaneously without understanding the matrix structure.
- kon total is '10' (not 'TOT') across all uddakt tables.
- laby52 is the only table with a geographic dimension (5 kommunegrupper). Use it for questions about regional access/distance to higher education. indhold is km distance — do not sum it. Data only goes to 2021.