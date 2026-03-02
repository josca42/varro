<fact tables>
<table>
id: tec01
description: Udenrigshandel med varer (virksomhedskarakteristika efter økonomiske enheder) efter im- og eksport, branche, virksomhedsstørrelse og tid
columns: indud, branche, virkstrrda, tid (time), indhold (unit Mio. kr.)
tid range: 2023-01-01 to 2024-01-01
</table>
<table>
id: tec02
description: Udenrigshandel med varer (virksomhedskarakteristika efter økonomiske enheder) efter im- og eksport, branche, poster og tid
columns: indud, branche, post, tid (time), indhold (unit Mio. kr.)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: tec06
description: Udenrigshandel med varer (virksomhedskarakteristika efter økonomiske enheder) efter im- og eksport, branche, ejerskab og tid
columns: indud, branche, ejerskab, tid (time), indhold (unit Mio. kr.)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: stec01
description: Udenrigshandel med tjenester (virksomhedskarakteristika efter økonomiske enheder) efter im- og eksport, branche, virksomhedsstørrelse og tid
columns: indud, branche, virkstrrda, tid (time), indhold (unit Mio. kr.)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: stec02
description: Udenrigshandel med tjenester (virksomhedskarakteristika efter økonomiske enheder) efter im- og eksport, branche, ejerskab og tid
columns: indud, branche, ejerskab, tid (time), indhold (unit Mio. kr.)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: dkstec06
description: Udenrigshandel med tjenester (virksomhedskarakteristika efter økonomiske enheder) efter im- og eksport, branche, poster og tid
columns: indud, branche, post, tid (time), indhold (unit Mio. kr.)
tid range: 2019-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- All 6 tables cover only 2023 (single year snapshot), except tec01 (goods by firm size, 2023–2024) and dkstec06 (services by type, 2019–2023). For time series, use tec01 or dkstec06.
- Goods vs. services split: tec01/tec02/tec06 cover trade in goods (varer); stec01/stec02/dkstec06 cover trade in services (tjenester). Pick the right group before querying.
- Breakdown dimension per table: firm size (tec01, stec01), goods/services type (tec02, dkstec06), ownership (tec06, stec02). No single table combines more than one breakdown — these are separate cuts of the same underlying data.
- All tables require filtering indud to 'IMP' or 'EXP'. Forgetting this silently doubles all aggregates.
- branche coding differs between goods and services tables. In goods tables (tec01/02/06), branche mixes NACE letter codes (AB, C, DE…) with numeric DB07 Afsnit codes (10–47). In services tables (stec01/02, dkstec06), branche has only letter codes and cannot be joined to dim.db at all.
- For goods tables with a dim.db join on branche, always filter WHERE d.niveau = 2. The same numeric code (e.g. 11) appears at multiple niveaux in dim.db and will produce duplicate rows without this filter.
- post and virkstrrda aggregation: in tec02 filter to '1.A.A' for goods total; in dkstec06 filter to '0' for services total. In tec01 filter virkstrrda = 'TOT'; in stec01 filter virkstrrda = '_T'. The naming convention differs between goods and services tables (TOT vs _T).
- ejerskab in tec06/stec02: 'D' is the sum of 'DI' + 'DM'. Do not sum D + DI + DM — that triple-counts Danish-owned firms.