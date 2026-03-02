<fact tables>
<table>
id: bil800
description: Familiernes bilrådighed (faktiske tal) efter område, rådighedsmønster og tid
columns: omrade, raadmoens, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2025-01-01
</table>
<table>
id: bil811
description: Familiernes bilrådighed (andele og fordelinger) efter område, enhed, rådighedsmønster og tid
columns: omrade, maengde4, raadmoens, tid (time), indhold (unit Pct.)
tid range: 2007-01-01 to 2025-01-01
</table>
<table>
id: bil82
description: Familiernes bilrådighed (faktiske tal) efter bestand, familietype, rådighedsmønster og tid
columns: bestand, famtyp, raadmoens, tid (time), indhold (unit Antal)
tid range: 2000-01-01 to 2025-01-01
</table>
<table>
id: bil83
description: Familiernes bilrådighed (andele og fordelinger) efter enhed, familietype, rådighedsmønster og tid
columns: maengde4, famtyp, raadmoens, tid (time), indhold (unit Pct.)
tid range: 2000-01-01 to 2025-01-01
</table>
<table>
id: bil84
description: Familiernes bilrådighed (faktiske tal) efter bestand, uddannelse, rådighedsmønster og tid
columns: bestand, uddannelse, raadmoens, tid (time), indhold (unit Antal)
tid range: 2000-01-01 to 2024-01-01
</table>
<table>
id: bil85
description: Familiernes bilrådighed (andele og fordelinger) efter enhed, uddannelse, rådighedsmønster og tid
columns: maengde4, uddannelse, raadmoens, tid (time), indhold (unit Pct.)
tid range: 2000-01-01 to 2024-01-01
</table>
<table>
id: bil86
description: Familiernes bilrådighed (faktiske tal) efter bestand, indkomst, rådighedsmønster og tid
columns: bestand, indkom, raadmoens, tid (time), indhold (unit Antal)
tid range: 2000-01-01 to 2024-01-01
</table>
<table>
id: bil87
description: Familiernes bilrådighed (andele og fordelinger) efter enhed, indkomst, rådighedsmønster og tid
columns: maengde4, indkom, raadmoens, tid (time), indhold (unit Pct.)
tid range: 2000-01-01 to 2024-01-01
</table>
<table>
id: bil88
description: Familiernes bilrådighed (faktiske tal) efter bestand, boligforhold, rådighedsmønster og tid
columns: bestand, bol, raadmoens, tid (time), indhold (unit Antal)
tid range: 2000-01-01 to 2024-01-01
</table>
<table>
id: bil89
description: Familiernes bilrådighed (andele og fordelinger) efter enhed, boligforhold, rådighedsmønster og tid
columns: maengde4, bol, raadmoens, tid (time), indhold (unit Pct.)
tid range: 2000-01-01 to 2024-01-01
</table>
<table>
id: bil90
description: Familiernes bilrådighed (faktiske tal) efter bestand, socioøkonomisk status, rådighedsmønster og tid
columns: bestand, socio, raadmoens, tid (time), indhold (unit Antal)
tid range: 2000-01-01 to 2024-01-01
</table>
<table>
id: bil91
description: Familiernes bilrådighed (andele og fordelinger) efter enhed, socioøkonomisk status, rådighedsmønster og tid
columns: maengde4, socio, raadmoens, tid (time), indhold (unit Pct.)
tid range: 2000-01-01 to 2024-01-01
</table>
<table>
id: bil92
description: Familiernes bilrådighed (faktiske tal) efter bystørrelse, rådighedsmønster og tid
columns: byst, raadmoens, tid (time), indhold (unit Antal)
tid range: 2013-01-01 to 2025-01-01
</table>
<table>
id: bil93
description: Familiernes bilrådighed (andele og fordelinger) efter enhed, bystørrelse, rådighedsmønster og tid
columns: maengde4, byst, raadmoens, tid (time), indhold (unit Pct.)
tid range: 2013-01-01 to 2025-01-01
</table>
<table>
id: laby28
description: Familiernes bilrådighed (faktiske tal) efter kommunegruppe, rådighedsmønster og tid
columns: komgrp, raadmoens, tid (time), indhold (unit Antal)
tid range: 2013-01-01 to 2024-01-01
</table>
<table>
id: laby53
description: Familiernes sommerhus- og bilrådighed efter bopælskommunegruppe, socioøkonomisk status, rådighedsmønster, sommerhuskommunegruppe og tid
columns: bopkomgrp, socio, raadmoens, somkom, tid (time), indhold (unit Antal)
tid range: 2022-01-01 to 2022-01-01
</table>
<table>
id: laby54
description: Familiernes sommerhus- og bilrådighed efter bopælskommunegruppe, boligforhold, rådighedsmønster, sommerhuskommunegruppe og tid
columns: bopkomgrp, bol, raadmoens, somkom, tid (time), indhold (unit Antal)
tid range: 2022-01-01 to 2022-01-01
</table>
<table>
id: laby55
description: Familiernes sommerhus- og bilrådighed efter bopælskommunegruppe, indkomst, rådighedsmønster, sommerhuskommunegruppe og tid
columns: bopkomgrp, indkom, raadmoens, somkom, tid (time), indhold (unit Antal)
tid range: 2022-01-01 to 2022-01-01
</table>
<table>
id: laby56
description: Familiernes sommerhus- og bilrådighed efter bopælskommunegruppe, uddannelse, rådighedsmønster, sommerhuskommunegruppe og tid
columns: bopkomgrp, uddannelse, raadmoens, somkom, tid (time), indhold (unit Antal)
tid range: 2022-01-01 to 2022-01-01
</table>
<table>
id: laby57
description: Familiernes sommerhus- og bilrådighed efter bopælskommunegruppe, familietype, rådighedsmønster, sommerhuskommunegruppe og tid
columns: bopkomgrp, famtyp, raadmoens, somkom, tid (time), indhold (unit Antal)
tid range: 2022-01-01 to 2022-01-01
</table>
</fact tables>
notes:
- Tables come in pairs: "faktiske tal" (Antal, e.g. bil82) + "andele og fordelinger" (Pct., e.g. bil83). The Pct. tables always have a maengde4 column that must be filtered (50=procentfordeling, 70=andel af total bilrådighed). Use Antal tables for counts, Pct. tables for pre-computed shares.
- raadmoens is hierarchical across ALL tables: 10000=familier i alt, 10200=ingen bil, 10210=med bil (10200+10210=10000). 10210 splits further into 10220 (1 bil) + 10260 (2 biler) + 10330 (3 biler) + 10340 (4+ biler). Never SUM across all raadmoens values — pick one level.
- Geographic breakdown: bil800/bil811 give NUTS regions/landsdele/kommuner (from 2007), laby28 gives the 5 kommunegrupper (from 2013), bil92/bil93 give bystørrelse (from 2013). Use bil800 for longest regional series.
- Sociodemographic breakdowns (bil82-91): choose by characteristic — familietype (bil82/83), uddannelse (bil84/85), indkomst (bil86/87), boligforhold (bil88/89), socioøkonomisk status (bil90/91). All go back to 2000 but end at 2024.
- bestand column (bil82-91): methodology selector for the family register definition. 52/72 in bil82, 53/73 elsewhere. Filter to the value covering your time period — they don't overlap. Never aggregate across both bestand values.
- laby53-57: unique sommerhus+bil cross-tables with two geographic dimensions (bopkomgrp where family lives, somkom where summer house is). 2022 only. Use these for questions about whether summer house ownership correlates with car access by region/sociodemographic.
- indkom (bil86/87): three overlapping schemes — income bands, decils, quartiles. Pick one. laby55 simplifies to decils+quartiles only.
- bol (bil88/89): two overlapping classification schemes — boligtype (110-610) and ejerforhold (620-640). Pick one. bol=100/TOT1 is the total for both.
- socio (bil90/91, laby53): hierarchical sub-groups. 100=total; 110=alle selvstændige, 130=alle lønmodtagere, 515=alle pensionister are sub-totals. Pick one granularity level.
- Map: bil800 and bil811 support choropleth maps via context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
