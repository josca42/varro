<fact tables>
<table>
id: oeko3
description: Detailomsætningen af økologiske fødevarer efter varer, enhed og tid
columns: vare, maengde4, tid (time), indhold (unit -)
tid range: 2003-01-01 to 2024-01-01
</table>
<table>
id: oeko77
description: Salg til foodservice efter varetype, varegruppe, enhed og tid
columns: vartyp, varegr, maengde6, tid (time), indhold (unit -)
tid range: 2021-01-01 to 2024-01-01
</table>
<table>
id: oeko88
description: Salg til foodservice efter varetype, kundegrupper, enhed og tid
columns: vartyp, kundegrp, maengde6, tid (time), indhold (unit -)
tid range: 2017-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- For retail sales of organic food (detailhandel): use oeko3. Longest series (2003–2024), 76 product categories with two hierarchy levels. Filter maengde4 to one unit (10=tons, 20=1000 kr.).
- For foodservice sales by product category: use oeko77 (2021–2024). Has vartyp (all/organic/conventional) and varegr hierarchy (5 main categories, 40 sub-categories). Filter maengde6 to one unit.
- For foodservice sales by customer segment: use oeko88 (2017–2024). Has same vartyp plus kundegrp (5 customer types: public institutions, public/private canteens, hotels/restaurants, other). Also has maengde6=40 (percent share) — never sum these, just read them.
- All three tables share the same overcounting trap: a unit/measure selector column (maengde4 or maengde6) repeats every row for each unit. Always filter to one unit.
- vartyp in oeko77/oeko88: 10=total, 20=organic, 30=conventional. 10 = 20 + 30 exactly. Never sum all three vartyp values.
- oeko3 and oeko77/oeko88 cover different sales channels: oeko3 = retail (supermarkets etc.), oeko77/oeko88 = foodservice (restaurants, canteens, institutions). They are not additive.