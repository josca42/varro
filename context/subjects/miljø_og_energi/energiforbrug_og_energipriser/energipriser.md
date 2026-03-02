<fact tables>
<table>
id: energi1
description: Priser på elektricitet for husholdningskunder efter årsforbrug, prisdefinition, energienhed og tid
columns: aarsforbrug, prisdefinition, energienhed, tid (time), indhold (unit Kr. pr. enhed)
tid range: 2015-01-01 to 2025-01-01
</table>
<table>
id: energi2
description: Priser på elektricitet for erhvervskunder efter årsforbrug, prisdefinition, energienhed og tid
columns: aarsforbrug, prisdefinition, energienhed, tid (time), indhold (unit Kr. pr. enhed)
tid range: 2015-01-01 to 2025-01-01
</table>
<table>
id: energi3
description: Priser på naturgas for husholdningskunder efter årsforbrug, prisdefinition, energienhed og tid
columns: aarsforbrug, prisdefinition, energienhed, tid (time), indhold (unit Kr. pr. enhed)
tid range: 2015-01-01 to 2025-01-01
</table>
<table>
id: energi4
description: Priser på naturgas for erhvervskunder efter årsforbrug, prisdefinition, energienhed og tid
columns: aarsforbrug, prisdefinition, energienhed, tid (time), indhold (unit Kr. pr. enhed)
tid range: 2015-01-01 to 2025-01-01
</table>
<table>
id: oliepris
description: Gennemsnitlig pris på nordsøolie efter enhed og tid
columns: enhed, tid (time), indhold (unit USD)
tid range: 2022-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Electricity prices: energi1 (households) and energi2 (businesses). Natural gas prices: energi3 (households) and energi4 (businesses). Crude oil: oliepris (annual average, USD/barrel).
- All four energi* tables share the same column structure: aarsforbrug (consumption band), prisdefinition (price-component level), energienhed (unit). Semi-annual frequency (January and July), 2015–2025.
- Critical filter: every (aarsforbrug, tid) row is repeated 8× (4 prisdefinitioner × 2 energienheder). Always filter to exactly one prisdefinition and one energienhed before reading indhold, or you silently multiply the price.
- prisdefinition '22' = full consumer price incl. VAT — the most commonly asked-for figure. '20A' = base energy price only (before grid fees and taxes).
- energienhed for electricity: KWH or GJ. For gas: M3 or GJ. GJ enables cross-fuel price comparison; otherwise use the natural unit (KWH / M3).
- aarsforbrug consumption bands are not a hierarchy — there is no total code. Each band represents a different consumer segment; summing across bands is meaningless.
- To compare electricity vs gas prices on the same energy basis, filter energienhed = 'GJ' in both tables.
- oliepris has only 3 annual data points (2022–2024) and is mainly useful as context for energy price movements rather than detailed analysis.