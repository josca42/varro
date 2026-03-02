<fact tables>
<table>
id: hdyr07
description: Landbrug med dyr efter område, enhed, art og tid
columns: omrade, enhed, dyr, tid (time), indhold (unit -)
tid range: 2006-01-01 to 2024-01-01
</table>
<table>
id: hdyr1
description: Landbrug med dyr efter areal, enhed, art og tid
columns: areal1, enhed, art, tid (time), indhold (unit -)
tid range: 1982-01-01 to 2024-01-01
</table>
<table>
id: hdyr2
description: Landbrug med dyr efter enhed, besætningsstørrelse og tid
columns: tal, besaet, tid (time), indhold (unit Antal)
tid range: 2012-01-01 to 2024-01-01
</table>
<table>
id: hdyroeko
description: Økologiske landbrug med udvalgte dyr efter enhed, art og tid
columns: enhed, dyr, tid (time), indhold (unit -)
tid range: 2010-01-01 to 2024-01-01
</table>
<table>
id: hdyr1920
description: Dyrebestanden (historisk) efter husdyrtype og tid
columns: husdyrtype, tid (time), indhold (unit 1.000 stk.)
tid range: 1920-01-01 to 1981-01-01
</table>
<table>
id: komb07
description: Besætningskombinationer med kvæg og svin efter område, type, enhed og tid
columns: omrade, type, enhed, tid (time), indhold (unit Antal)
tid range: 2006-01-01 to 2024-01-01
</table>
<table>
id: kvaeg5
description: Kvægbestanden efter område, art og tid
columns: omrade, dyr, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2025-07-01
</table>
<table>
id: svin
description: Svinebestanden den 1. i  kvartalet efter type og tid
columns: type, tid (time), indhold (unit 1.000 stk.)
tid range: 1998-01-01 to 2025-07-01
</table>
</fact tables>

notes:
- For current livestock by region: use hdyr07 (2006–2024, regional+landsdel breakdown, both farm count and animal count). For kvæg specifically with more up-to-date data: kvaeg5 (2008–2025, simpler — animal count only, no enhed selector).
- For farm-size breakdown instead of regional: hdyr1 (1982–2024, farm area groups). For herd-size distribution (how many farms have N animals): hdyr2 (2012–2024).
- For swine national quarterly series: svin (1998–2025, 1.000 stk.). For regional swine/cattle combination breakdown: komb07 (2006–2024).
- For organic livestock only: hdyroeko (2010–2024, national, 9 simple animal codes).
- For long historical animal counts (before 1982): hdyr1920 (1920–1981, in 1.000 stk.). Combine with hdyr1 or hdyr07 for a 100-year series — note unit difference (hdyr1920 is thousands; hdyr07/hdyr1 are actual counts).
- Common enhed gotcha: hdyr07, hdyr1, hdyr2, hdyroeko, and komb07 all have an enhed/tal column that multiplies every row (ANTAL=farms, DYR=animals, or in komb07 also AK/AS). Forgetting to filter enhed silently doubles all counts.
- omrade coding in hdyr07, komb07, kvaeg5: 12 values total, but codes 0 (Hele landet) and 15 (merged Copenhagen-area landsdel covering dim.nuts codes 1+2+3) are not in dim.nuts. The remaining 10 codes are 5 regioner (81-85, niveau 1) and 5 landsdele (4,7,8,9,10, niveau 2). Join with AND d.niveau=1 for region-level analysis.
- dyr/art column in hdyr07 and hdyr1 has 144–146 codes mixing animal categories (D-prefix) and herd-size groups (letter prefixes: MK, AK, KK, K, SO, SS, S, F, MF). Never sum across prefix families.
- Map: hdyr07, komb07, kvaeg5 support choropleth at region (context/geo/regioner.parquet) or landsdel (context/geo/landsdele.parquet) level — merge on omrade=dim_kode, exclude omrade IN (0, 15). No kommune-level breakdown available.