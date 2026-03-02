<fact tables>
<table>
id: kn8mest
description: Im- og eksport KN (EU Kombineret nomenklatur) efter im- og eksport, varer, land, enhed, datakilde og tid
columns: indud, vare, land, enhed, datakilde, tid (time), indhold (unit -)
tid range: 2016-01-01 to 2016-06-01
</table>
<table>
id: kn8y
description: Im- og eksport KN (EU Kombineret nomenklatur) efter im- og eksport, varer, land, enhed og tid
columns: indud, vare, land, enhed, tid (time), indhold (unit -)
tid range: 1988-01-01 to 2024-01-01
</table>
<table>
id: sitc2r4
description: Værdi af import og eksport (1000 kr.) efter SITC-hovedgrupper, land, im- og eksport, varebegreb og tid
columns: sitc, land, indud, uhbegreb, tid (time), indhold (unit 1.000 kr.)
tid range: 2022-01-01 to 2025-09-01
</table>
<table>
id: sitc2r4m
description: Værdi af import og eksport (1000 kr.) efter SITC-hovedgrupper, land, im- og eksport og tid
columns: sitc, land, indud, tid (time), indhold (unit 1.000 kr.)
tid range: 2007-01-01 to 2021-12-01
</table>
<table>
id: sitc2r4y
description: Værdi af import og eksport (1000 kr.) efter SITC-hovedgrupper, land, im- og eksport og tid
columns: sitc, land, indud, tid (time), indhold (unit 1.000 kr.)
tid range: 2007-01-01 to 2021-01-01
</table>
<table>
id: sitc5r4
description: Im- og eksport (1.000 kr.) efter SITC-hovedgrupper, land, im- og eksport, enhed, varebegreb og tid
columns: sitc, land, indud, enhed, uhbegreb, tid (time), indhold (unit -)
tid range: 2022-01-01 to 2025-08-01
</table>
<table>
id: sitc5r4m
description: Im- og eksport (Rev. 4 SITC) efter im- og eksport, SITC-hovedgrupper, land, enhed og tid
columns: indud, sitc, land, enhed, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2013-12-01
</table>
<table>
id: sitc5r4y
description: Im- og eksport (Rev. 4 SITC) efter im- og eksport, SITC-hovedgrupper, land, enhed og tid
columns: indud, sitc, land, enhed, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2021-01-01
</table>
<table>
id: sitcixm
description: Indeks for udenrigshandel med varer efter im- og eksport, indekstype, sæsonkorrigering, SITC-hovedgrupper og tid
columns: indud, indekstype, saeson2, sitc, tid (time), indhold (unit Indeks)
tid range: 2007-01-01 to 2025-09-01
</table>
<table>
id: sitcixy
description: Indeks for importen og eksporten efter im- og eksport, indekstype, SITC-hovedgrupper og tid
columns: indud, indekstype, sitc, tid (time), indhold (unit Indeks)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: uhixm
description: Indeks for udenrigshandel med varer efter im- og eksport, indekstype, sæsonkorrigering og tid
columns: indud, indekstype, saeson2, tid (time), indhold (unit Indeks)
tid range: 2007-01-01 to 2025-08-01
</table>
<table>
id: uhixy
description: Indeks for udenrigshandel med varer efter im- og eksport, indekstype og tid
columns: indud, indekstype, tid (time), indhold (unit Indeks)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: uhtx
description: Tjenestebalance, kvartal efter im- og eksport, poster, land og tid
columns: indud, post, land, tid (time), indhold (unit Mio. kr.)
tid range: 2005-01-01 to 2025-04-01
</table>
<table>
id: oeko4
description: Udenrigshandel med økologiske varer efter im- og eksport, varer og tid
columns: indud, vare, tid (time), indhold (unit 1.000 kr.)
tid range: 2003-01-01 to 2023-01-01
</table>
<table>
id: oeko55
description: Udenrigshandel med økologiske varer efter im- og eksport, land og tid
columns: indud, land, tid (time), indhold (unit 1.000 kr.)
tid range: 2003-01-01 to 2023-01-01
</table>
<table>
id: oeko66
description: Udenrigshandel med økologiske varer efter im- og eksport, land, SITC-hovedgrupper og tid
columns: indud, nation, sitc, tid (time), indhold (unit 1.000 kr.)
tid range: 2003-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- Table naming follows a pattern: suffix 'm' = monthly, 'y' = annual, no suffix = current (latest release). E.g. sitc2r4m (monthly 2007–2021), sitc2r4y (annual 2007–2021), sitc2r4 (monthly 2022–present).
- Goods trade at SITC level: sitc2r4/m/y give SITC group (niveau 2, 66 groups) by country. sitc5r4/m/y give SITC subgroup (niveau 3, ~2925 codes) by country — much more granular. For broad commodity types use sitc2-series; for specific products use sitc5-series.
- Goods trade at KN level: kn8y (annual 1988–2024) and kn8mest (monthly 2016 only) offer 8-digit Combined Nomenclature codes — the most granular product classification. Use for EU legal trade codes or when SITC is too coarse. Note: kn8mest covers only 2016.
- Services trade: uhtx is the only services table (quarterly 2005–2025, EBOPS classification by country). All other tables cover goods only. uhtx has a non-obvious join: REPLACE(f.post, '.', '') = d.kode::text.
- Price/volume indices: uhixm/uhixy give aggregate import/export price and volume indices. sitcixm/sitcixy give the same broken down by SITC afdeling (niveau 1). Use for inflation analysis, not for trade value totals.
- Organic trade: oeko4 (by product), oeko55 (by country), oeko66 (by country+SITC) cover organic goods 2003–2023. Very narrow subset — use SITC tables for total trade comparisons.
- SELECTOR columns that silently inflate counts appear across many tables: enhed (Kilo vs Kroner), uhbegreb (GP vs ES trade valuation), indekstype (Kvantum vs Enhedsværdi), saeson2 (seasonal adjustment). Always filter these before aggregating.
- All goods tables with a land column use dim.lande_uhv (GEONOM, 5 levels). uhtx uses dim.lande_uht_bb (4 levels, different codes). Not interchangeable.
- Aggregate land codes (W1=World, TOT, 9A, QX, RS, etc.) appear in fact tables but are absent from dim tables. Exclude when joining or handle explicitly.