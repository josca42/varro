<fact tables>
<table>
id: fu11
description: Forbrugsundersøgelsen efter baggrundsoplysninger, husstandsgrupper og tid
columns: bagopl, husgrp, tid (time), indhold (unit -)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: fu12
description: Husstandenes gennemsnitlige forbrug efter forbrugsgruppe, prisenhed og tid
columns: konsumgrp, prisenhed, tid (time), indhold (unit Kr. pr. husstand)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: fu13
description: Forbrug efter forbrugsgruppe, husstand, prisenhed og tid
columns: konsumgrp, husstand, prisenhed, tid (time), indhold (unit Kr. pr. husstand)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: fu14
description: Forbrug efter forbrugsgruppe, socioøkonomisk status, prisenhed og tid
columns: konsumgrp, socio, prisenhed, tid (time), indhold (unit Kr. pr. husstand)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: fu15
description: Forbrug efter forbrugsgruppe, samlet indkomst, prisenhed og tid
columns: konsumgrp, samind, prisenhed, tid (time), indhold (unit Kr. pr. husstand)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: fu16
description: Forbrug efter forbrugsgruppe, boligform, prisenhed og tid
columns: konsumgrp, bolform, prisenhed, tid (time), indhold (unit Kr. pr. husstand)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: fu17
description: Forbrug efter forbrugsgruppe, region, prisenhed og tid
columns: konsumgrp, region, prisenhed, tid (time), indhold (unit Kr. pr. husstand)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: fu18
description: Forbrug efter forbrugsgruppe, alder, prisenhed og tid
columns: konsumgrp, alder, prisenhed, tid (time), indhold (unit Kr. pr. husstand)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: fu19
description: Husstandenes gennemsnitlige indkomst og forbrug efter indkomsttype og tid
columns: indkomsttype, tid (time), indhold (unit Kr. pr. husstand)
tid range: 2015-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- All tables cover 2015-2023 (annual).
- fu11 is about survey demographics and household composition, not consumption amounts. Use it to look up how many households are in the survey, average household size, share of homeowners, etc. — cross-tabbed by 37 household groups.
- fu12 is the most detailed consumption table: 281 konsumgrp codes at niveau 1 (14 top-level categories) and niveau 4 (267 subcategories). Use it when you need granular spending breakdowns but no demographic cross-tab.
- fu13-fu18 each cross-tab consumption (niveau 1 and 2 konsumgrp, 62 codes) against one demographic variable: fu13=husstandstype, fu14=socioøkonomisk status, fu15=indkomstniveau, fu16=boligform, fu17=region (5 regioner), fu18=alder (5 aldersgrupper).
- fu19 is an income and expenditure accounting table (25 line items). Use it to put consumption in context of household income, taxes, and savings. Code 600 (Forbrug) links to the total in fu12-fu18.
- prisenhed doubles all rows in fu12-fu18 (AARPRIS=løbende priser, 08PRIS=faste 2008-priser). Always filter to one value — this is the most common overcounting trap in this subject.
- konsumgrp in fu12-fu18 uses ECOICOP dotted decimal notation ("01", "01.1", "01.1.1.1"), NOT the integer kode in dim.ecoicop. The dim join requires: `REPLACE(konsumgrp, '.', '')::integer = d.kode AND d.niveau = (LENGTH(konsumgrp) - LENGTH(REPLACE(konsumgrp, '.', ''))) + 1`. Category "00" = total; category "13.x" = DST-specific (forsikring/finansielle tjenester), not in standard ECOICOP.
- Map: fu17 supports regional choropleth via /geo/regioner.parquet. Region codes 6010–6050 map to NUTS dim_kode 84, 85, 83, 82, 81 respectively. Exclude region=2001 (national average).