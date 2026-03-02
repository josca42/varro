<fact tables>
<table>
id: kbs1
description: Udviklingsforløb i serviceerhverv efter branche (DB07), indikator, bedømmelse, forløb og tid
columns: branche07, indikator, bedommelse, forlob, tid (time), indhold (unit Pct.)
tid range: 2011-05-01 to 2025-10-01
</table>
<table>
id: kbs2
description: Produktionsbegrænsninger i serviceerhverv efter branche (DB07), type og tid
columns: branche07, type, tid (time), indhold (unit Pct.)
tid range: 2011-05-01 to 2025-10-01
</table>
<table>
id: kbs3
description: Kapacitetsudnyttelse i serviceerhverv (ultimo måneden før) efter branche (DB07) og tid
columns: branche07, tid (time), indhold (unit Pct.)
tid range: 2011-05-01 to 2025-10-01
</table>
</fact tables>

notes:
- Three complementary monthly survey tables covering the same service sectors and the same period (2011–2025). Use them together to build a full picture of sector conditions.
- kbs1 (sentiment/outlook): the richest table. Gives actual vs expected (forlob=FAK/FOR) assessments across 4 indicators (forretningssituation, omsætning, beskæftigelse, salgspriser). Use bedommelse=NET for the headline net balance (SFO-MFO). FOS only has FAK.
- kbs2 (production constraints): use when the question is about why firms are constrained — labour shortage, lack of demand, financial limits, etc. Values are non-exclusive percentages; never sum across type.
- kbs3 (capacity utilization): simplest table — one % per sector per month. Use for a direct capacity level reading without survey opinion noise.
- All three tables share the same branche07 coding: sector totals (uppercase names) and sub-sectors (lowercase names) coexist in the same column. Always pick one hierarchy level to avoid double-counting. branche07='0' is the aggregate for all services.