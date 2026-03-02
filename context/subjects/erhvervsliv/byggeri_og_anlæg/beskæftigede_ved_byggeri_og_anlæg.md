<fact tables>
<table>
id: byg1
description: Beskæftigede ved bygge og anlæg efter branche (DB07), art, sæsonkorrigering og tid
columns: branche07, art, saeson, tid (time), indhold (unit Antal)
tid range: 2000-01-01 to 2025-01-01
</table>
</fact tables>

notes:
- byg1 is the only table in this subject. It covers employed persons in construction (Antal) broken down by branch, activity type, and seasonal adjustment, quarterly from 2000.
- Always filter saeson: every row exists twice — saeson='20' for actual figures, saeson='10' for seasonally adjusted. This is the most common gotcha.
- branche07 uses 9 custom survey codes (not standard DB07 hierarchy). Use ColumnValues("byg1", "branche07") to see them. branche07='F' is the sector total; the 8 remaining codes are sub-segments (Byggeentreprenører, Anlægsentreprenører, El-installation, VVS, Tømrer, Maler, Murere, Anden specialiseret).
- art='TOT' gives the total headcount across all activity types. Use specific art codes (001–004, 007, 008) only for breakdowns of what workers are actually doing.