<fact tables>
<table>
id: fisk1
description: Danske fiskefartøjer efter område, enhed, fartøjstype, længde, tonnage og tid
columns: omrade, tal, fiskfar, laeng, tonnage, tid (time), indhold (unit Antal)
tid range: 1996-01-01 to 2024-01-01
</table>
<table>
id: fisk2
description: Danske fartøjers landing af fisk efter fangstområde, landingsplads, enhed, fiskeart og tid
columns: fangst, landing1, tal, fisk, tid (time), indhold (unit -)
tid range: 1996-01-01 to 2024-01-01
</table>
<table>
id: fisk3
description: Landinger af fisk i Danmark efter fangstområde, landingsplads, enhed, fiskeart og tid
columns: fangst, landing1, tal, fisk, tid (time), indhold (unit -)
tid range: 1996-01-01 to 2024-01-01
</table>
<table>
id: firegn1
description: Regnskabsstatistik for fiskeri (total) efter fartøjslængde, regnskabsposter og tid
columns: farlaengd, regnskposter, tid (time), indhold (unit -)
tid range: 2009-01-01 to 2023-01-01
</table>
<table>
id: firegn2
description: Regnskabsstatistik for fiskeri (gennemsnit pr. enhed) efter fartøjslængde, regnskabsposter og tid
columns: farlaengd, regnskposter, tid (time), indhold (unit -)
tid range: 2009-01-01 to 2023-01-01
</table>
<table>
id: nfisk
description: Nøgletal for fiskeri efter fartøjslængde, regnskabsposter og tid
columns: farlaengd, regnskposter, tid (time), indhold (unit -)
tid range: 2009-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- For vessel fleet statistics (antal fartøjer, tonnage, maskineffekt by region/type/size): use fisk1. It has a dim.nuts join for regions but only at niveau=1 (5 regions). Always filter tal to one measurement unit.
- For fish landings by Danish vessels: use fisk2 (covers catches landed anywhere, including abroad). For fish landed in Denmark (any vessel's nationality): use fisk3. The distinction matters: fisk2 = what Danish fishers caught; fisk3 = what came into Danish ports.
- Both fisk2 and fisk3 have a fisk species column with two hierarchy levels (species groups vs individual species). Filter to one level to avoid double-counting.
- For financial/accounting data on fishing businesses: firegn1 (totals), firegn2 (per-vessel averages), nfisk (4 key ratios). All three share the same farlaengd codes and cover 2009-2023.
- farlaengd in firegn1/firegn2/nfisk has two tiers: size-class aggregates (codes 9/10/12/14/16/18/20, UPPERCASE labels) and gear-type subcategories within each size class (codes 40-86, mixed-case labels). Never sum across both tiers.
- firegn1 has 204 regnskposter accounting line items; nfisk has just 4 summary ratios. Start with nfisk for a quick sector health check, then drill into firegn1/firegn2 for detail.
- All three financial tables (firegn1, firegn2, nfisk) use the same farlaengd dimension — ColumnValues("firegn1", "farlaengd") shows the full code list with labels.
- Map: fisk1 supports choropleth maps at region level (niveau 1) via /geo/regioner.parquet — merge on omrade=dim_kode, exclude omrade=0. fisk2/fisk3 use hardcoded string region codes (R84, R82…) that do not join to geo files directly.