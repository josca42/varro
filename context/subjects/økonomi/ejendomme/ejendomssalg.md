<fact tables>
<table>
id: ej5
description: Prisindeks for ejendomssalg efter ejendomskategori, enhed og tid
columns: ejendomskate, tal, tid (time), indhold (unit Indeks)
tid range: 1992-01-01 to 2025-04-01
</table>
<table>
id: ej56
description: Prisindeks for ejendomssalg efter område, ejendomskategori, enhed og tid
columns: omrade, ejendomskate, tal, tid (time), indhold (unit Indeks)
tid range: 1992-01-01 to 2025-04-01
</table>
<table>
id: ej121
description: Sæsonkorrigerede ejendomssalg, almindelig fri handel efter region, ejendomskategori, enhed og tid
columns: region, ejkat20, tal, tid (time), indhold (unit -)
tid range: 2005-01-01 to 2025-04-01
</table>
<table>
id: ej6
description: Prisindeks for ejendomssalg efter ejendomskategori, enhed og tid
columns: ejendomskate, tal, tid (time), indhold (unit Indeks)
tid range: 1992-01-01 to 2024-01-01
</table>
<table>
id: ej67
description: Prisindeks for ejendomssalg efter område, ejendomskategori, enhed og tid
columns: omrade, ejendomskate, tal, tid (time), indhold (unit Indeks)
tid range: 1992-01-01 to 2024-01-01
</table>
<table>
id: ej99
description: Prisindeks for andelsboliger og ejerboliger efter område, boligtype, enhed og tid
columns: omrade, boltyp, enhed, tid (time), indhold (unit -)
tid range: 2015-01-01 to 2025-04-01
</table>
<table>
id: ej131
description: Ejendomssalg (endelig) efter region, ejendomskategori, nøgletal og tid
columns: region, ejendomskate, bnogle, tid (time), indhold (unit -)
tid range: 2006-01-01 to 2024-08-01
</table>
<table>
id: ejen77
description: Ejendomssalg efter område, ejendomskategori, nøgletal, overdragelsesformer og tid
columns: omrade, ejendomskate, bnogle, overdrag, tid (time), indhold (unit -)
tid range: 1992-01-01 to 2025-04-01
</table>
<table>
id: ejen88
description: Ejendomssalg efter område, ejendomskategori, nøgletal, overdragelsesformer og tid
columns: omrade, ejendomskate, bnogle, overdrag, tid (time), indhold (unit -)
tid range: 1992-01-01 to 2024-01-01
</table>
<table>
id: ejen99
description: Nøgletal for andelsboligsalg efter område, vurderingsprincip og tid
columns: omrade, vurdering, tid (time), indhold (unit Pct.)
tid range: 2015-01-01 to 2025-04-01
</table>
<table>
id: laby22
description: Ejendomssalg efter kommunegruppe, ejendomskategori, nøgletal og tid
columns: komgrp, ejendomskate, bnogle, tid (time), indhold (unit -)
tid range: 2012-01-01 to 2024-01-01
</table>
<table>
id: ejeneu
description: EU-harmoniseret boligprisindeks (HPI) efter urbaniseringsgrad, udgiftstype og tid
columns: urbangrad, udgtyp, tid (time), indhold (unit Indeks)
tid range: 2002-10-01 to 2025-04-01
</table>
</fact tables>

notes:
**Table naming pattern:** The suffix encodes time granularity — "5"/"56"/"57" = quarterly, "6"/"67" = annual. ejen77 = quarterly, ejen88 = annual. All "5x" tables end 2025 (current); all "6x" and "88" tables end 2024.

**Price index vs. sales data:** Two fundamentally different data types in this subject:
- Price index tables (ej5, ej6, ej56, ej67, ej121, ej99, ejeneu): `indhold` is an index number or % change. Never sum across rows.
- Sales data tables (ejen77, ejen88, ej131, laby22): `indhold` is antal salg or price in 1000 kr. Summable within a single bnogle type.

**Choosing a price index table:**
- National only, quarterly: ej5 (current to 2025), ej6 (annual, ends 2024)
- By region/landsdel, quarterly: ej56 (current), ej67 (annual, ends 2024)
- Seasonally adjusted + sales count by region: ej121 (from 2005, covers both price index and antal salg in one table via `tal`)
- Andelsboliger + ejerboliger by landsdel: ej99 (from 2015 only)
- EU-comparable HPI: ejeneu (from 2002, by urbanisation degree)

**Choosing a sales data table:**
- Most comprehensive (all property types, all transfer types, regions + landsdele, quarterly): ejen77 (current), ejen88 (annual, ends 2024)
- Definitive/final revision by region, fewer property types: ej131 (ends 2024-08)
- First-time buyer statistics by kommunegruppe: laby22 (annual, ends 2024, only table with this)
- Andelsbolig key ratios (price as % of valuation) down to municipality level: ejen99 (quarterly from 2015)

**Universal gotcha — measurement selector columns:** Every price index table has a `tal` or `enhed` column that selects between price level, QoQ%, and YoY%. Every sales table has a `bnogle` column selecting between antal salg, gennemsnitspris, m2-pris, etc. ALWAYS filter to exactly one value — omitting it silently multiplies results by the number of selector values (2-6x).

**Universal gotcha — area code 0:** In all tables with an area column (omrade, region), code 0 = "Hele landet" (national total). It is NOT in dim.nuts. When joining to dim.nuts, rows with code 0 drop out — use a LEFT JOIN or filter to `omrade != '0'` explicitly.

**ejendomskate code 9999 in ejen77/ejen88:** = "Samlet salg" (grand total across all property types). Not in dim.ejendom. Exclude it when you want per-category breakdowns.

**Map support:** All tables with an area column support choropleth maps via dim.nuts. Geographic depth varies: ej56, ej67, ejen77, ejen88 cover regioner (niveau 1) and landsdele (niveau 2); ej121 and ej131 cover regioner only; ej99 covers landsdele only; ejen99 goes deepest — down to kommuner (niveau 3). Use /geo/regioner.parquet, landsdele.parquet, or kommuner.parquet accordingly. Exclude omrade=0 (and omrade=95 for ejen99) before merging.