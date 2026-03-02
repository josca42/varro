<fact tables>
<table>
id: akv11
description: Akvakultur efter anlægstype, enhed, fiske- og skaldyrsarter og tid
columns: anlaeg, tal, fiskskal, tid (time), indhold (unit -)
tid range: 2021-01-01 to 2023-01-01
</table>
<table>
id: akregn1
description: Regnskabsstatistik for akvakultur efter enhed, anlægstype, regnskabsposter og tid
columns: enhed, anlaeg, regnskposter, tid (time), indhold (unit -)
tid range: 2017-01-01 to 2023-01-01
</table>
<table>
id: nak1
description: Nøgletal for akvakultur efter anlægstype, regnskabsposter og tid
columns: anlaeg, regnskposter, tid (time), indhold (unit -)
tid range: 2017-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- For production volumes (tons) or production value (1000 kr) by species and facility type: use akv11. Filter tal to select the unit (10=tons, 20=1000 kr). Only covers 2021–2023.
- For financial accounts (revenue, costs, assets, employment): use akregn1 (from 2017, 170 accounting line items). Always filter enhed (1=total, 5=per-facility average) and one specific regnskposter.
- For financial ratios (profit margin, return on assets, equity ratio, owner compensation): use nak1 (from 2017, 4 key figures). Simpler table — no enhed selector.
- All three tables share the same anlaeg dimension (facility types: 0=all, 6=traditional trout farms, 11–13=recirculation systems at low/medium/high levels, 25=sea farms, 36=mussel/oyster farms). anlaeg=0 is always the aggregate — do not mix with subtypes when summing.
- Common pitfall: akv11 tal and akregn1 enhed are measurement selectors that silently double counts if not filtered. Always specify one value for these columns.