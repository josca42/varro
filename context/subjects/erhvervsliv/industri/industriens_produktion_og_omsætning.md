<fact tables>
<table>
id: ipoo2021
description: Industriens omsætningssituation efter omsætning, sæsonkorrigering, branche (DB07) og tid
columns: omsaetning, saeson, branche07, tid (time), indhold (unit Indeks)
tid range: 2000-01-01 to 2025-08-01
</table>
<table>
id: ipop2021
description: Industriens produktionsindeks efter sæsonkorrigering, branche (DB07) og tid
columns: saeson, branche07, tid (time), indhold (unit Indeks)
tid range: 2000-01-01 to 2025-08-01
</table>
</fact tables>

notes:
- For industrial production index (produktionsindeks): use ipop2021. For turnover (omsætning i løbende priser — total, export, domestic): use ipoo2021. Both cover 2000–2025 monthly at the same branche07 granularity.
- Both tables carry the same branche07 coding scheme: standard DB07 letter codes (CA, CB, CC… at section level), custom numeric sub-codes (10001–10005 for food industry sub-sectors, etc.), cross-section aggregates (BC, CDE, BCD), and MIG sector groups (S1–S5 = Main Industrial Groups: investment goods, intermediate goods, durable/non-durable consumer goods, energy). Browse with ColumnValues("ipop2021", "branche07") for labels.
- Both require filtering saeson to one value (EJSÆSON = unadjusted, SÆSON = seasonally adjusted) — every row exists in both variants, so omitting this filter doubles all results.
- ipoo2021 additionally requires filtering omsaetning to one of: 410 (total), 411 (eksport), 415 (hjemmemarked). All three variants are present for every row.
- indhold is always an index value (base 100), not absolute kroner/units. Do not sum across branches.
- The dim.nr_branche join only covers ~40% of branche07 codes (the standard letter codes). Custom numeric and aggregate codes have no dim match — use ColumnValues for labels instead of the dim join.