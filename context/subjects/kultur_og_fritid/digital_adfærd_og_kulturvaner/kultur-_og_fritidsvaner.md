<fact tables>
<table>
id: medlem2
description: Medlemstal for ungdoms- og friluftsorganisationer efter organisation og tid
columns: organisation, tid (time), indhold (unit 1.000 personer)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: kv2hoved
description: Forbrug af kulturaktiviteter efter kulturaktivitet, køn, alder og tid
columns: kultur, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2025-04-01
</table>
<table>
id: kv2ahov
description: Forbrug af kulturaktiviteter (år) efter kulturaktivitet, køn, alder og tid
columns: kultur, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2udd
description: Forbrug af kulturaktiviteter efter kulturaktivitet, køn, højest fuldførte uddannelse og tid
columns: kultur, kon, hfudd2, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2025-04-01
</table>
<table>
id: kv2audd
description: Forbrug af kulturaktiviteter (år) efter kulturaktivitet, køn, højest fuldførte uddannelse og tid
columns: kultur, kon, hfudd2, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2urb
description: Forbrug af kulturaktiviteter efter kulturaktivitet, køn og alder, urbaniseringsgrad og tid
columns: kultur, koal, urbangrad, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2025-04-01
</table>
<table>
id: kv2aurb
description: Forbrug af kulturaktiviteter (år) efter kulturaktivitet, køn og alder, urbaniseringsgrad og tid
columns: kultur, koal, urbangrad, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2hyp1
description: Forbrug af medier, sociale medier, musik, litteratur, digitale spil, og sport og motion efter kulturaktivitet, køn, alder, hyppighed og tid
columns: kultur, kon, alder, hyp, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2025-04-01
</table>
<table>
id: kv2ahyp1
description: Forbrug af medier, sociale medier, musik, litteratur, digitale spil, og sport og motion (år) efter kulturaktivitet, køn, alder, hyppighed og tid
columns: kultur, kon, alder, hyp, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2hyp2
description: Forbrug af biograf, udøvende kunstarter, udstilling, bibliotek, sportsbegivenheder og kulturarv efter kulturaktivitet, køn, alder, hyppighed og tid
columns: kultur, kon, alder, hyp, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2025-04-01
</table>
<table>
id: kv2ahyp2
description: Forbrug af biograf, udøvende kunstarter, udstilling, bibliotek, sportsbegivenheder og kulturarv (år) efter kulturaktivitet, køn, alder, hyppighed og tid
columns: kultur, kon, alder, hyp, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2geo
description: Forbrug af kulturaktiviteter efter kulturaktivitet, kommune og tid
columns: kultur, kommunedk, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2fr1
description: Frivilligt arbejde efter hyppighed, køn, alder og tid
columns: hyp, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2fr2
description: Frivilligt arbejde efter arbejdsområde, køn, alder og tid
columns: arbom, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2fr3
description: Foreningsmedlemskab efter foreningstype, køn, alder og tid
columns: forentyp, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2fr4
description: Forbrug af fritidsbegivenheder efter begivenhed, køn, alder og tid
columns: begivenhed, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2fr5
description: Besøg på religiøse samlingssteder efter hyppighed, køn, alder og tid
columns: hyp, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2fr6
description: Forbrug af fritidsaktiviteter efter aktivitet, hyppighed, køn, alder og tid
columns: aktivitet, hyp, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2brn1
description: Kulturvaner i barndomshjemmet efter kulturvane, omfang, køn, alder og tid
columns: kultvane2, bogtype, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2brn2
description: Forbrug af kulturaktiviteter efter dine aktiviteter, kulturvaner i barndomshjemmet, omfang, køn, alder og tid
columns: dinakt, kultvane, bogtype, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: laby58
description: Frivilligt arbejde efter kommunegruppe og tid
columns: komgrp, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
</fact tables>
notes:
- Table naming convention: kv2 prefix = Kulturvaner 2-survey data (2024). Suffix 'a' = annual (single 2024 obs); no suffix = quarterly updates. E.g. kv2hoved (quarterly) vs kv2ahov (annual).
- For culture consumption rates (% who did activity X) broken down by age/gender: kv2hoved/kv2ahov. By education: kv2udd/kv2audd. By urbanisation: kv2urb/kv2aurb. By geography (kommune/landsdel/region): kv2geo (annual only). Use the quarterly tables for latest data; annual 'a' tables for consistent 2024 snapshot.
- For frequency of activities (how often, not just whether): kv2hyp1/kv2ahyp1 (digital/home 101xx activities) and kv2hyp2/kv2ahyp2 (physical/venue 201xx activities).
- For voluntary work: kv2fr1 (how often), kv2fr2 (which area — NOT mutually exclusive), laby58 (% by kommunegruppe — 5 groups, annual only).
- For association membership: kv2fr3 (by type — NOT mutually exclusive).
- For leisure events attended: kv2fr4 (event type — NOT mutually exclusive).
- For religious venue visits: kv2fr5 (frequency, same hyp scale as kv2fr1).
- For hobby/leisure activities by frequency: kv2fr6 (5 hobby types × frequency grid).
- For childhood cultural habits and their relationship to current behaviour: kv2brn1 (habits alone), kv2brn2 (habits × current activities cross-tab — complex, 5 dimensions).
- For long time-series membership counts (2007–2024): medlem2 (1.000 persons, not %).
- Critical gotcha shared by all kv2* tables: indhold is a percentage, not a count. Each kultur/arbom/forentyp/begivenhed row is an independent activity — never sum across these category columns. They represent separate yes/no survey questions, not mutually exclusive choices.
- For tables with kon and alder: always filter both to their totals (kon='10', alder='TOT') unless you specifically want a breakdown. kv2urb/kv2aurb use a merged koal column instead (koal='0' for total).
- Map: kv2geo supports choropleth maps via /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on kommunedk=dim_kode. All other tables lack a geographic column.
