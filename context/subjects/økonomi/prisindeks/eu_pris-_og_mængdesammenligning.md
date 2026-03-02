<fact tables>
<table>
id: ppp
description: Købekraftpariteter og internationale mængde- og prissammenligninger efter varegruppe, land, enhed og tid
columns: varegr, land, enhed, tid (time), indhold (unit -)
tid range: 2000-01-01 to 2023-01-01
</table>
<table>
id: ppp11
description: Købekraftkorrigerede indeks og værdier per indbygger efter varegrupper, land, enhed og tid
columns: vargr, land, tal, tid (time), indhold (unit -)
tid range: 2000-01-01 to 2023-01-01
</table>
<table>
id: ppp1
description: Prisniveau indeks for fødevarer EU=100 efter varegruppe, land og tid
columns: varegr, land, tid (time), indhold (unit -)
tid range: 2006-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- For food price comparisons (EU=100): use ppp1 — simplest table, 2006–2024, no measurement selector, 10 varegr codes covering food/alcohol/tobacco. Best for "how does Denmark compare to EU on food prices".
- For broad cross-country spending comparisons (PPP, price levels, per capita): use ppp — most comprehensive (63 varegr codes, 2000–2023, multiple measurement types). Always filter `enhed` to exactly one value; prefer enhed=29 (prisniveauindeks, EU-27=100) or enhed=39 (per capita index, EU-27=100).
- For GDP/expenditure per capita in PPS or index form: use ppp11 — 9 top-level expenditure categories, same years as ppp. Filter `tal` to one value; prefer tal=39 (index) or tal=49 (PPS value), both using EU-27 baseline.
- All three tables: `land` column includes DK (Denmark) and Eurostat EU aggregate codes (U2=Euroområdet, D2=EU-28, D3=EU-27, V5=EU-27 pre-Brexit, V3=EU-15) that are not in dim.lande_uhv — reference these directly without a join. DK has the most rows in all three tables.
- ppp and ppp11 share the same `land` unmatched codes (DK, U2, D2, D3, V3, V5, RS). ppp1 only has DK unmatched.
- `varegr` codes are hierarchical — parent and child codes both appear in the data. Never sum across all varegr values without filtering to a consistent hierarchy level.