<fact tables>
<table>
id: skib41
description: Godstransport over danske havne efter enhed og tid
columns: enhed, tid (time), indhold (unit 1.000 ton)
tid range: 1990-01-01 to 2024-01-01
</table>
<table>
id: skib421
description: Godsomsætning på danske havne efter havn, enhed og tid
columns: havn, enhed, tid (time), indhold (unit 1.000 ton)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: skib431
description: International godsomsætning på danske havne efter havn, retning, godsart og tid
columns: havn, ret, gods, tid (time), indhold (unit 1.000 ton)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: skib44
description: International godsomsætning på større danske havne efter havn, retning, land og tid
columns: havn, ret, land, tid (time), indhold (unit 1.000 ton)
tid range: 2004-01-01 to 2024-01-01
</table>
<table>
id: skib451
description: National godsomsætning på danske havne efter havn, retning, godsart og tid
columns: havn, ret, gods, tid (time), indhold (unit 1.000 ton)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: skib461
description: National godsomsætning på danske havne efter havn, retning, landsdel og tid
columns: havn, ret, landdel, tid (time), indhold (unit 1.000 ton)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: skib47
description: Fragtskibes godsomsætning på større danske havne efter flagstat, retning, godsart og tid
columns: flag, ret, gods, tid (time), indhold (unit 1.000 ton)
tid range: 1997-01-01 to 2024-01-01
</table>
<table>
id: skib481
description: Godstransport med skib mellem danske landsdele efter pålæsningsregion, aflæsningsregion, enhed og tid
columns: paregion, afregion, enhed, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: skib49
description: Godsomsætning af container- og ro-ro-gods på større danske havne efter havn, retning, lasteenhed, enhed og tid
columns: havn, ret, last, enhed, tid (time), indhold (unit -)
tid range: 1997-01-01 to 2024-01-01
</table>
<table>
id: skib50
description: International godsomsætning på større danske havne efter retning, land, godsart og tid
columns: ret, land, gods, tid (time), indhold (unit 1.000 ton)
tid range: 2004-01-01 to 2024-01-01
</table>
<table>
id: skib72
description: Godsomsætning på større danske havne efter havn, retning, godsart og tid
columns: havn, ret, gods, tid (time), indhold (unit 1.000 ton)
tid range: 2000-01-01 to 2025-04-01
</table>
<table>
id: skib73
description: Omsætning af container- og ro-ro-enheder på større danske havne efter retning, lasteenhed, transport enhed og tid
columns: ret, last, transport1, tid (time), indhold (unit -)
tid range: 2000-01-01 to 2025-04-01
</table>
<table>
id: skib74
description: Godsomsætning på større havne efter landegrupper, godsart og tid
columns: landgrp, gods, tid (time), indhold (unit 1.000 ton)
tid range: 2000-01-01 to 2025-04-01
</table>
</fact tables>
notes:
- **Common overcounting traps**: Almost every table in this subject has hierarchical aggregate codes mixed in with leaf codes — in havn (0=I ALT, LANDSDEL codes), ret (total + sub-totals), gods/enhed (total + sub-categories), and land (IA=I alt). Always filter each dimension to a single level before summing.

- **Time coverage**: skib41 goes back to 1990 (longest). skib47/skib49 from 1997. skib44/skib50 from 2004. Most others from 2007. skib72/skib73/skib74 are the most current (through 2025).

- **Port scope**: "Alle havne" tables (skib421, skib431, skib451, skib461) include all Danish ports including smaller ones. "Større havne" tables (skib44, skib47, skib49, skib50, skib72, skib73, skib74) cover only the larger ports.

- **Choosing by question type**:
  - Overall goods volume over time (no breakdown): skib41 (from 1990, freight vs. ferry split via enhed)
  - Goods by port + unit type (freight/ferry/inbound/outbound): skib421 (all ports, from 2007)
  - Goods by port + cargo type, international: skib431 (all ports) or skib72 (larger ports, through 2025)
  - Goods by port + cargo type, domestic: skib451 (all ports)
  - Goods by port + cargo type, both combined: skib72 (larger ports, through 2025)
  - Goods by country of origin/destination + port: skib44 (larger ports only, from 2004)
  - Goods by country + cargo type (no port detail): skib50 (larger ports in aggregate, from 2004)
  - Goods by broad geographic region + cargo category: skib74 (simplest, through 2025)
  - Goods by flag state (Danish vs. foreign ships): skib47 (larger ports, from 1997)
  - Containers and ro-ro by port: skib49 (larger ports, size breakdown, from 1997)
  - Containers and ro-ro national summary: skib73 (aggregate only, through 2025)
  - Domestic inter-regional flows (origin-destination matrix): skib481 (only table with this)
  - Goods by port + landsdel (destination region, domestic): skib461

- **land column warning** (skib44, skib50): these tables do NOT use the standard lande_uhv GEONOM coding for all codes. Use ColumnValues("skib44"/"skib50", "land") to get labels — do not rely on a dim.lande_uhv JOIN alone (76% match rate, 10 codes unmatched).

- **enhed vs. gods vs. ret**: Several tables use `enhed` as a measurement-type selector (skib41, skib421, skib481, skib49) where every data cell is repeated for each measurement type. Always filter enhed to one value. Tables with `ret` (direction: inbound/outbound) also require filtering — ret always has a total code plus breakdowns.

- **Map**: skib461 and skib481 support landsdele-level choropleth maps via /geo/landsdele.parquet. See individual fact docs for merge details.
