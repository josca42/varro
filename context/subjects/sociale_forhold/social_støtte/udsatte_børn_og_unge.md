<fact tables>
<table>
id: bu43
description: Børn og unge der modtager støtte pr. 31. december (andel af 0-22-årige) efter område, Foranstaltning, alder og tid
columns: omrade, foranstalt, alder, tid (time), indhold (unit Pct.)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: bu04a
description: Støtte til børn og unge pr. 31. december (nettoopgørelse) efter område, foranstaltning, alder, køn og tid
columns: omrade, foran, alder, kon, tid (time), indhold (unit Antal)
tid range: 2011-01-01 to 2024-01-01
</table>
<table>
id: bu28
description: Samlede offentlige netto-driftsudgifter til udsatte børn og unge efter foranstaltning og tid
columns: foran, tid (time), indhold (unit Mio. kr.)
tid range: 2002-01-01 to 2024-01-01
</table>
<table>
id: anbaar2
description: Anbragte børn og unge pr. 31. december efter foranstaltning, alder, køn og tid
columns: foran, alder1, kon, tid (time), indhold (unit Antal)
tid range: 2011-01-01 to 2024-01-01
</table>
<table>
id: anbaar15
description: Anbragte børn og unge pr. 31. december efter anbringelsessted, alder, køn og tid
columns: anbringelse, alder1, kon, tid (time), indhold (unit Antal)
tid range: 2011-01-01 to 2024-01-01
</table>
<table>
id: anbaar16
description: Anbragte børn og unge pr. 31. december efter landsdel, anbringelsessted, foranstaltning, alder, køn og tid
columns: landdel, anbringelse, foran, alder1, kon, tid (time), indhold (unit Antal)
tid range: 2011-01-01 to 2024-01-01
</table>
<table>
id: anbaar12
description: Anbragte børn og unge pr. 31. december efter administrationskommune, anbringelsessted og tid
columns: admkom, anbringelse, tid (time), indhold (unit Antal)
tid range: 2011-01-01 to 2024-01-01
</table>
<table>
id: anbaar13
description: Anbragte børn og unge pr. 31. december efter administrationskommune, foranstaltning og tid
columns: admkom, foran, tid (time), indhold (unit Antal)
tid range: 2011-01-01 to 2024-01-01
</table>
<table>
id: anbaar9
description: Anbragte børn og unge pr. 31. december efter administrationskommune, alder og tid
columns: admkom, alerams, tid (time), indhold (unit Antal)
tid range: 2011-01-01 to 2024-01-01
</table>
<table>
id: anbaar8
description: Iværksatte anbringelser af børn og unge efter landsdel, foranstaltning, alder, køn og tid
columns: landdel, foran, alder1, kon, tid (time), indhold (unit Antal)
tid range: 2011-01-01 to 2024-01-01
</table>
<table>
id: anbaar17
description: Iværksatte anbringelser af børn og unge efter landsdel, anbringelsessted, alder, køn og tid
columns: landdel, anbringelse, alder1, kon, tid (time), indhold (unit Antal)
tid range: 2011-01-01 to 2024-01-01
</table>
<table>
id: anbaar14
description: Iværksatte anbringelser efter administrationskommune, alder og tid
columns: admkom, alerams, tid (time), indhold (unit Antal)
tid range: 2011-01-01 to 2024-01-01
</table>
<table>
id: anbaar10
description: Udslagsgivende årsager til iværksatte anbringelser efter landsdel, årsag til anbringelse, alder, køn og tid
columns: landdel, anbringaarsag, alder1, kon, tid (time), indhold (unit Antal)
tid range: 2018-01-01 to 2024-01-01
</table>
<table>
id: isbu01
description: Aktive indsatser og støtte til børn og unge i året efter kommune, indsats og tid
columns: kommunedk, indsatser, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: isbu02
description: Børn og unge der modtager indsatser og støtte efter kommune, indsats og tid
columns: kommunedk, indsatser, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: isbu03
description: Iværksatte indsatser og støtte til børn og unge i året efter landsdel, indsats og tid
columns: landsdel, indsatser, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: isbu04
description: Aktive indsatser og støtte til børn og unge pr. 31. december efter landsdel, indsats, alder, køn og tid
columns: landsdel, indsatser, alder, kon, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: und1
description: Underretninger vedr. børn efter administrationskommune, underrettere, alder, køn og tid
columns: admkom, underretere, alder1, kon, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: und2
description: Børn der er modtaget underretninger om efter administrationskommune, underretninger, alder, køn og tid
columns: admkom, underret, alder1, kon, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: laby16
description: Andel af børn mellem 0-18 år med underretninger efter kommunegruppe og tid
columns: komgrp, tid (time), indhold (unit Pct.)
tid range: 2015-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Three topic clusters: (1) broad support (bu*), (2) out-of-home placements/anbringelser (anbaar*), (3) early interventions/indsatser (isbu*), and (4) notifications/underretninger (und*, laby16).

**Broad support — bu tables:**
- bu43: shares (Pct.) of 0-22 yr olds with support by kommune. For "how prevalent is support in municipality X". From 2015.
- bu04a: counts (Antal) of children/interventions by landsdel. Broadest overview of all support types (65 foran codes, hierarchical). From 2011.
- bu28: public expenditure (Mio. kr.) by intervention type, national only. Longest history (2002–). No geography.

**Anbringelser (out-of-home placements) — anbaar tables:**
- Stock (pr. 31. december): anbaar2 (national, legal basis, single-year ages), anbaar15 (national, placement type, single-year ages), anbaar16 (landsdel, both placement type and legal basis, age groups), anbaar9/12/13 (kommune level, limited dimensions).
- Flow (iværksatte = newly initiated): anbaar8 (landsdel, legal basis), anbaar17 (landsdel, placement type), anbaar14 (kommune, age only).
- Causes: anbaar10 (triggering causes, from 2018 only, causes are non-mutually-exclusive — see fact doc).
- For regional breakdown of placed children stock: anbaar16 (landsdel) or anbaar12/13/9 (kommune but limited dimensions).
- For national detail (single-year ages, full legal basis): anbaar2 or anbaar15.

**Indsatser (early interventions) — isbu tables:**
- isbu01: intervention counts by kommune (55 detailed codes, hierarchical). Use when question is "how many interventions".
- isbu02: child counts by kommune (same 55 codes). Use when question is "how many children receive support".
- isbu03: new interventions by landsdel, 4 high-level codes only. Flow table.
- isbu04: active interventions by landsdel, 4 high-level codes, with age and gender. Stock table.
- Key distinction: isbu01 vs isbu02 — same structure, different unit (interventions vs children).

**Underretninger (notifications) — und tables:**
- und1: notification counts by kommune, who sent them, single-year ages. "How many notifications" and "who reported".
- und2: child counts by kommune, grouped by how many notifications they received (1, 2, 3, 4, 5, 6+). "How many repeat-notification children".
- laby16: notification share (Pct.) of 0-18 yr olds by kommunegruppe type (uses dim.kommunegrupper, not dim.nuts).

**Common pitfalls across all tables:**
- Total codes differ by table: many anbaar tables use 0 for totals (foran=0, kon=0, alder=0/IALT), while bu04a uses TOT/IALT/TOT. Check each table's encoding.
- Gender encoding differs: bu04a uses M/K/TOT; all anbaar/isbu/und tables use D (drenge) / P (piger) / 0 (I alt).
- All tables with multiple dimension columns require filtering on ALL non-target dimensions to avoid overcounting.
- anbaar10 causes are non-mutually exclusive — never sum across anbringaarsag codes.
- Map: kommune-level tables (bu43, anbaar9/12/13/14, isbu01/02, und1/2) support choropleth via context/geo/kommuner.parquet; landsdel-level tables (bu04a, anbaar8/10/16/17, isbu03/04) via context/geo/landsdele.parquet.