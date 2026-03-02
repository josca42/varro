<fact tables>
<table>
id: nrhp
description: 1-2.1.1 Produktion, BNP og indkomstdannelse efter område, transaktion, prisenhed og tid
columns: omrade, transakt, prisenhed, tid (time), indhold (unit -)
tid range: 1993-01-01 to 2024-01-01
</table>
<table>
id: vnrhp
description: Versionstabel NRHP - Produktion, BNP og indkomstdannelse efter version, område, transaktion, prisenhed og tid
columns: version, omrade, transakt, prisenhed, tid (time), indhold (unit -)
tid range: 1993-01-01 to 2024-01-01
</table>
<table>
id: nrhb
description: Befolkning efter område, socioøkonomisk status og tid
columns: omrade, socio, tid (time), indhold (unit Antal)
tid range: 1993-01-01 to 2024-01-01
</table>
<table>
id: vnrbb10
description: Versionstabel NRBB10 - Beskæftigelse og timer (10a3-gruppering) efter version, område, socioøkonomisk status, branche og tid
columns: version, omrade, socio, branche, tid (time), indhold (unit -)
tid range: 1993-01-01 to 2024-01-01
</table>
<table>
id: nrbb10
description: Beskæftigelse og timer (10a3-gruppering) efter område, socioøkonomisk status, branche og tid
columns: omrade, socio, branche, tid (time), indhold (unit -)
tid range: 1993-01-01 to 2024-01-01
</table>
<table>
id: vnrbp10
description: Versionstabel NRBP10 - Produktion, BVT og indkomstdannelse (10a3-gruppering) efter version, område, transaktion, branche, prisenhed og tid
columns: version, omrade, transakt, branche, prisenhed, tid (time), indhold (unit -)
tid range: 1993-01-01 to 2024-01-01
</table>
<table>
id: nrbp10
description: 1-2.1.1 Produktion, BVT og indkomstdannelse (10a3-gruppering) efter område, transaktion, branche, prisenhed og tid
columns: omrade, transakt, branche, prisenhed, tid (time), indhold (unit -)
tid range: 1993-01-01 to 2024-01-01
</table>
<table>
id: nrbi10
description: Investeringer (10a3-gruppering) efter område, branche, prisenhed og tid
columns: omrade, branche, prisenhed, tid (time), indhold (unit -)
tid range: 2000-01-01 to 2023-01-01
</table>
<table>
id: vnrs
description: Versionstabel NRS - Husholdningernes indkomst efter version, område, transaktion, prisenhed og tid
columns: version, omrade, transakt, prisenhed, tid (time), indhold (unit -)
tid range: 2000-01-01 to 2024-01-01
</table>
<table>
id: nrs
description: Husholdningernes indkomst efter område, transaktion, prisenhed og tid
columns: omrade, transakt, prisenhed, tid (time), indhold (unit -)
tid range: 2000-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- All tables use omrade → dim.nuts (niveau 1=5 regioner, niveau 2=11 landsdele). Codes 0 (hele landet) and 999 (ikke regionalfordelt) appear in every table but are NOT in the dim — exclude them for regional breakdowns. Exception: nrbi10 only has niveau 1 (regioner), no landsdele.
- Version tables (vnrhp, vnrbb10, vnrbp10, vnrs) each contain 14 release versions all covering the full time series from 1993 — querying without filtering version inflates every number by ~14x. Use these only when comparing estimates across revision vintages. For all standard analysis, use the non-version tables (nrhp, nrbb10, nrbp10, nrs).
- prisenhed is a measurement selector in every table except nrhb — the same data repeats once per price unit. Always filter to one prisenhed or totals are silently multiplied.
- For BNP (GDP) by region/landsdel: nrhp (transakt='B1GQD'), from 1993.
- For BVT broken down by branche and region: nrbp10 (transakt='B1GD'), from 1993. nrhp has BNP but no branche; nrbp10 has branche but no BNP.
- For employment/hours by region and sector: nrbb10. Filter socio to one measure: EMPM_DC (headcount) or EMPH_DC (1000 timer).
- For household disposable income by region: nrs (transakt='B6GD'). From 2000 only, no branche breakdown, current prices only.
- For regional investment by sector: nrbi10. Shortest series (2000–2023) and coarsest geography (regioner only).
- For population by region (useful for per-capita denominators): nrhb. No measurement selectors — the simplest table here.
- nrhp and nrs include per-capita prisenhed options (V_C, LRG_C), so you can get per-capita figures directly without dividing by nrhb.
- Map: all tables support choropleth via context/geo/regioner.parquet (niveau 1) or context/geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. nrbi10 is regioner only. Exclude omrade IN (0, 999) in all tables except nrhb (which only has omrade=0 as non-regional code).