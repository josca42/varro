<fact tables>
<table>
id: fod
description: Levendefødte efter moders alder, barnets køn og tid
columns: modersalder, barnkon, tid (time), indhold (unit Antal)
tid range: 1973-01-01 to 2024-01-01
</table>
<table>
id: fodie
description: Levendefødte efter område, moders herkomst, moders oprindelsesland, moders statsborgerskab, moders alder, barnets køn og tid
columns: omrade, moherk, mooprind, mostat, modersalder, barnkon, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: foddag
description: Levendefødte efter fødselsdag, fødselsmåned og tid
columns: fdag, fmaaned, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: fodpm
description: Levendefødte efter moders alder, levendefødtnummer og tid
columns: modersalder, lfnr, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: fodpf
description: Levendefødte efter faders alder, levendefødtnummer og tid
columns: faald, lfnr, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: bev3a
description: Levendefødte og døde efter bevægelse og tid
columns: bevaegelsev, tid (time), indhold (unit Antal)
tid range: 1901-01-01 to 2025-06-01
</table>
<table>
id: km3
description: Levendefødte og døde efter sogn, bevægelse og tid
columns: sogn, bevaegelsev, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2025-04-01
</table>
<table>
id: fod8
description: Enkelt- og flerfødsler efter fødselstype og tid
columns: fodtype, tid (time), indhold (unit Antal)
tid range: 1850-01-01 to 2023-01-01
</table>
<table>
id: fod9
description: Tvillingefødsler fordelt efter fødselstype og tid
columns: fodtype, tid (time), indhold (unit Antal)
tid range: 1911-01-01 to 2023-01-01
</table>
<table>
id: fod11
description: Gennemsnitsalder for fødende kvinder og nybagte fædre efter alder og tid
columns: alder, tid (time), indhold (unit -)
tid range: 1901-01-01 to 2024-01-01
</table>
<table>
id: fod111
description: Gennemsnitsalder for fødende kvinder og nybagte fædre efter område, alder og tid
columns: omrade, alder, tid (time), indhold (unit Gns.)
tid range: 2006-01-01 to 2024-01-01
</table>
<table>
id: foraeld
description: Antal forældre 1. januar efter køn, alder, antal børn og tid
columns: kon, alder, antborn, tid (time), indhold (unit Antal)
tid range: 1986-01-01 to 2025-01-01
</table>
<table>
id: barnlos
description: Barnløse pr. 1.000 efter køn, alder og tid
columns: kon, alder, tid (time), indhold (unit Pr. 1.000 indb.)
tid range: 1986-01-01 to 2025-01-01
</table>
</fact tables>
notes:
- For a simple national births time series going back to 1901: use bev3a (filter bevaegelsev='B02'). For births from 1973 with mother's age breakdown: fod. For births from 1850 by delivery type (single/twin/triplet): fod8.
- For births with demographic detail (mother's origin, region): fodie (from 2007). For births by birth order: fodpm (mother's age) or fodpf (father's age), both from 2007.
- For births by calendar day/month pattern: foddag (from 2007). For births at parish (sogn) level: km3 (from 2007).
- For average parental age: fod11 (national, from 1901) or fod111 (by region, from 2006). indhold in both is an average — never sum across the alder dimension.
- For stock of parents by gender/age/number-of-children: foraeld (from 1986). For childlessness rates: barnlos (from 1986). barnlos is a rate table — never sum its values.
- For twin birth gender breakdown: fod9 (counts twin deliveries by gender combination, from 1911).
- Common pitfall: most tables have no aggregate total rows. fod/fodpm/fodpf/foraeld-antborn all use individual ages/birth-orders only — sum all rows explicitly rather than filtering to a "total" code.
- foraeld has kon='TOT' but no IALT for alder or antborn. barnlos has no TOT for either dimension.
- bev3a and km3 cover both births (B02) and deaths (B03) — always filter bevaegelsev.
- Map: fodie and fod111 support choropleth at kommune (niveau 3) or region (niveau 1) via context/geo/kommuner.parquet or context/geo/regioner.parquet. km3 supports parish-level maps via context/geo/sogne.parquet.
