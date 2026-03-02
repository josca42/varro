<fact tables>
<table>
id: bane31
description: Trafikarbejde med tog efter transporttype og tid
columns: transport, tid (time), indhold (unit 1.000 togkm)
tid range: 1990-01-01 to 2024-01-01
</table>
<table>
id: bane41
description: Jernbanenettet pr. 1. januar efter banenet, enhed og tid
columns: bane, enhed, tid (time), indhold (unit -)
tid range: 1990-01-01 to 2025-01-01
</table>
<table>
id: bane42
description: Investeringer i jernbanenettet efter investeringstype, enhed og tid
columns: invest, enhed, tid (time), indhold (unit Mio. kr.)
tid range: 1990-01-01 to 2024-01-01
</table>
<table>
id: bane53
description: Investeringer i rullende materiel efter investeringstype, enhed og tid
columns: invest, enhed, tid (time), indhold (unit Mio. kr.)
tid range: 1990-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- bane31: traffic work (togkm) by transport type, annual 1990–2024. Use for "how many train-km did DSB/Metro/Letbane operate?" — no enhed column, just pick the right hierarchical transport code.
- bane41: network characteristics as of 1 January each year, 1990–2025. Use for "how many km of electrified track / how many level crossings?" — MUST filter enhed (7 incompatible measurement types: km variants, antal crossings, antal stops).
- bane42: infrastructure investment (Mio. kr.) by investor/project, 1990–2024. MUST filter enhed to a single price base (current or constant year). Use for capex on track/stations/fixed assets.
- bane53: rolling stock investment (Mio. kr.) by operator, 1990–2024. Same enhed selector as bane42. Use for capex on trains/wagons. Complement to bane42 — do not add the two tables together (different asset types).
- All tables with an enhed column (bane41, bane42, bane53) require filtering to exactly one enhed — failing to do so silently inflates sums by 4–7×.
- All category columns (transport, bane, invest) are hierarchical with aggregate totals mixed in. Always pick one level; never GROUP BY and SUM across all codes.