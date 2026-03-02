<fact tables>
<table>
id: kbyg11
description: Udviklingsforløb for bygge og anlæg efter branche (DB07), indikator, bedømmelse, forløb og tid
columns: branche07, indikator, bedommelse, forlob, tid (time), indhold (unit Pct.)
tid range: 2005-01-01 to 2025-10-01
</table>
<table>
id: kbyg22
description: Vurdering af ordrebeholdningen i bygge og anlæg efter branche (DB07), bedømmelse og tid
columns: branche07, bedommelse, tid (time), indhold (unit Pct.)
tid range: 2005-01-01 to 2025-10-01
</table>
<table>
id: kbyg33
description: Produktionsbegrænsninger i bygge og anlæg efter branche (DB07), type og tid
columns: branche07, type, tid (time), indhold (unit Pct.)
tid range: 2005-01-01 to 2025-10-01
</table>
<table>
id: kbyg11k
description: Udviklingsforløb i bygge og anlæg, nettotal (sæsonkorrigeret) efter branche (DB07), indikator, sæsonkorrigering, forløb og tid
columns: branche07, indikator, saeson, forlob, tid (time), indhold (unit Pct.)
tid range: 2005-01-01 to 2025-10-01
</table>
<table>
id: kbyg22k
description: Vurdering af ordrebeholdningen i bygge og anlæg, nettotal (sæson- og brudkorrigeret) efter branche (DB07), indikator, sæsonkorrigering og tid
columns: branche07, indikator, saeson, tid (time), indhold (unit Pct.)
tid range: 2005-01-01 to 2025-10-01
</table>
</fact tables>

notes:
- The "k" suffix marks seasonally-adjusted versions: kbyg11k is the sæsonkorrigeret counterpart of kbyg11, and kbyg22k of kbyg22. The k-tables contain only NET totals and fewer branche07 values (4 vs 9). Prefer k-tables for trend analysis, base tables for full response distributions.
- branche07 in ALL tables uses DST's own survey groupings, NOT standard DB07 codes — the dim.db_10 join does not work. Always get labels via ColumnValues("{table_id}", "branche07"). F = total bygge og anlæg sector.
- For the full response breakdown (STØR/UÆNDR/MINDRE/NET or MN1/NOR1/SNO1/NET): use kbyg11 or kbyg22. The bedommelse/NET column is derived (NET = %positive − %negative) — never sum across all bedommelse values.
- For production constraints by type: use kbyg33. The type values are NOT mutually exclusive (firms report multiple constraints simultaneously) — never sum across type.
- kbyg11/11k cover three indicators (omsætning, beskæftigelse, tilbudspriser) for both faktisk (past 3 months) and forventet (next 3 months). kbyg22/22k cover only ordrebeholdning.
- kbyg22k has two indikator values: 1008 (ordrebeholdning) and 1009 (brudkorrigeret). The break-corrected series (1009) is only available without seasonal adjustment.