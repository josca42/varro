<fact tables>
<table>
id: skat
description: Skatter og afgifter efter type og tid
columns: type, tid (time), indhold (unit 1.000 kr.)
tid range: 1947-01-01 to 2024-01-01
</table>
<table>
id: skres2
description: Skatter der ikke indbetales, periodiseret efter skattetype og tid
columns: skatter, tid (time), indhold (unit Mio. kr.)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: sktryk
description: Skattetryk efter nationalregnskabsgrupper og tid
columns: natgrup, tid (time), indhold (unit Pct.)
tid range: 1971-01-01 to 2024-01-01
</table>
<table>
id: pskat
description: Personbeskatningen efter område, beskatningsprocent og tid
columns: omrade, skatpct, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2025-01-01
</table>
<table>
id: pskat1
description: Skatteydernes indkomster og skatter efter type og tid
columns: type, tid (time), indhold (unit Mio. kr.)
tid range: 1987-01-01 to 2023-01-01
</table>
<table>
id: pskat2
description: Indkomster og fradrag ved slutligningen efter type og tid
columns: type, tid (time), indhold (unit Mio. kr.)
tid range: 1994-01-01 to 2023-01-01
</table>
<table>
id: pskat3
description: Skattepligtige personer efter skattetype og tid
columns: skatter, tid (time), indhold (unit 1.000 personer)
tid range: 1994-01-01 to 2023-01-01
</table>
<table>
id: pskat4
description: Slutskat efter område, indkomstskattetype og tid
columns: omrade, indkomst, tid (time), indhold (unit 1.000 kr.)
tid range: 2011-01-01 to 2023-01-01
</table>
<table>
id: eskat
description: Beskatningsværdier og ejendomsskatter efter område, beskatningsgrundlag og tid
columns: omrade, skatgrl, tid (time), indhold (unit -)
tid range: 2006-01-01 to 2024-01-01
</table>
<table>
id: ejdsk1
description: Ejendomsskatter efter område, skattetype og tid
columns: omrade, skatter, tid (time), indhold (unit 1.000 kr.)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: ejdsk2
description: Ejendomsskatter efter område, skattepromille og tid
columns: omrade, skatpro, tid (time), indhold (unit Skattepromille)
tid range: 2007-01-01 to 2025-01-01
</table>
<table>
id: ejdsk3
description: Grundskyld efter område, ejendomstype og tid
columns: omrade, ejentyp, tid (time), indhold (unit 1.000 kr.)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: selsk1
description: Selskaber mv. efter type, skattepligtig indkomst og tid
columns: type, skat, tid (time), indhold (unit Antal)
tid range: 1996-01-01 to 2023-01-01
</table>
<table>
id: selsk2
description: Skatteydende selskaber mv. efter type, indkomst og skat og tid
columns: type, indskat, tid (time), indhold (unit -)
tid range: 1996-01-01 to 2023-01-01
</table>
<table>
id: selsk3
description: Selskabsskat fordelt - DB07 efter branche, indkomst og skat og tid
columns: branche, indskat, tid (time), indhold (unit -)
tid range: 1996-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- For total Danish tax revenue by category (since 1947): skat. Has 214 type codes in a 3-level hierarchy (TOTAL, 1–6, X.Y, X.Y.ZZ) — always filter to one level to avoid double-counting.
- For tax burden as % of GDP (since 1971): sktryk. 8 independent rate measures — use natgrup=1 for standard total skattetryk.
- For unpaid taxes (skatterestancer, since 1995): skres2. Codes split into tax-type view (22–66) or sector view (77–88) — pick one view per query.

- For personal tax rates by kommune/region (since 2007): pskat. Has kommunal udskrivningspct, kirkeskattepct, and grundskyldspromille — always filter to one skatpct. Note: GRUND ends 2023; use ejdsk2 for 2024+ rates.
- For personal income and tax totals, national level: pskat1 (full settlement report, 1987–), pskat2 (income components and deductions, 1994–). Both use hierarchical type codes — never sum across levels. pskat1 mixes units (some types in 1.000 persons, others in Mio. kr.).
- For count of taxpayers by tax type (since 1994): pskat3. Tax types are NOT mutually exclusive (same person pays multiple taxes) — never sum across skatter values.
- For slutskat breakdown by kommune (since 2011): pskat4. Kommune-level only (niveau 3), indkomst column mixes units (persons vs 1.000 kr. vs averages).

- For property taxes (ejendomsskatter) by kommune: ejdsk1 has amounts (1.000 kr., 2007–), ejdsk2 has rates (skattepromille, 2007–, through 2025). eskat gives valuation bases (ejendomsværdi/grundværdi) alongside tax totals but mixes units. ejdsk3 breaks grundskyld by property type (en-familiehuse, landbrug, etc.).
- All property tables are kommune-level only (niveau 3), except pskat and ejdsk2 which also have niveau 1 (5 regioner). National totals have omrade='0' or '0.0' (not in dim.nuts — handle separately or exclude from joins).

- For corporate tax: selsk1 counts all selskaber by type and income bracket (incl. loss-making). selsk2 covers only tax-paying selskaber with count/income/tax in one indskat column (always filter to one indskat). selsk3 is the same as selsk2 but by DB07 industry instead of company type. Both selsk2 and selsk3 mixes units in indskat (Antal, Mio. kr., Mio. kr.) — never aggregate across indskat values.

- Map: pskat, ejdsk2 support kommune + region choropleths (niveau 3 + 1). pskat4, eskat, ejdsk1, ejdsk3 support kommune-only choropleths (niveau 3). All merge on omrade=dim_kode via /geo/kommuner.parquet or /geo/regioner.parquet.