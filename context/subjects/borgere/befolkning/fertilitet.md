<fact tables>
<table>
id: fert1
description: Samlet fertilitet (15-49 år) efter herkomst og tid
columns: herkomst, tid (time), indhold (unit Pr. 1.000 kvinder)
tid range: 1986-01-01 to 2024-01-01
</table>
<table>
id: fod33
description: Fertilitetskvotienter efter alder og tid
columns: alder, tid (time), indhold (unit Pr. 1.000 kvinder)
tid range: 1973-01-01 to 2024-01-01
</table>
<table>
id: fod407
description: Fertilitetskvotienter efter område, alder og tid
columns: omrade, alder, tid (time), indhold (unit Pr. 1.000 kvinder)
tid range: 2006-01-01 to 2024-01-01
</table>
<table>
id: kohort01
description: Kumulerede fertilitetskvotienter for kvinders fødselsårgange efter fødselsår, alder og tid
columns: fodaar, alder, tid (time), indhold (unit Pr. 1.000 kvinder)
tid range: 2023-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- For national fertility trends over time (total fertility rate): fod33 goes back to 1973 and also includes BRUTTO/NETTO reproduction rates. fert1 goes back to 1986 and breaks down by herkomst (dansk oprindelse vs. indvandrere/efterkommere).
- For regional fertility breakdown: fod407 is the only table with geographic detail (from 2006). It joins dim.nuts at niveau 1 (5 regioner), 2 (11 landsdele), or 3 (94 kommuner). Filter to one niveau level when grouping by region.
- For cohort analysis (how many children has a generation had?): kohort01 has cumulative fertility by birth cohort and age. Only 2023–2024 snapshot data; always filter to a single tid value. Use alder='1549' for completed cohort fertility (reliable for cohorts born ≤ ~1974).
- fod33 and fod407 both express fertility as period rates (pr. 1.000 kvinder). Their TOT1/alder='TOT1' values are the total fertility rate for a given year — comparable across tables.
- All tables measure fertility in the same unit (pr. 1.000 kvinder). No table has a unit selector column — values are always rates, never counts.
- Map: fod407 supports choropleth maps at all three NUTS levels — context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.