<fact tables>
<table>
id: pend101
description: Beskæftigede (ultimo november) efter område, branche (DB07), pendling, køn og tid
columns: omrade, branche07, pendling, kon, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2023-01-01
</table>
<table>
id: pend100
description: Beskæftigede (ultimo november) efter bopælskommune, arbejdsstedsområde, køn og tid
columns: bopkom, arbejdssted, kon, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2023-01-01
</table>
<table>
id: afsta3
description: Beskæftigede (ultimo november) efter arbejdsstedsområde, socioøkonomisk status, køn, pendlingsafstand og tid
columns: arbejdssted, socio, koen, pendafst, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2023-01-01
</table>
<table>
id: afsta4
description: Gennemsnitlig pendlingsafstand (ultimo november) efter arbejdsstedsområde, socioøkonomisk status, køn og tid
columns: arbejdssted, socio, koen, tid (time), indhold (unit Km)
tid range: 2008-01-01 to 2023-01-01
</table>
<table>
id: afstb4
description: Gennemsnitlig pendlingsafstand (ultimo november) efter bopælsområde, socioøkonomisk status, køn og tid
columns: bopomr, socio, kon, tid (time), indhold (unit Km)
tid range: 2008-01-01 to 2023-01-01
</table>
<table>
id: afstb3
description: Beskæftigede (ultimo november) efter bopælsområde, socioøkonomisk status, køn, pendlingsafstand og tid
columns: bopomr, socio, koen, pendafst, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2023-01-01
</table>
<table>
id: laby44
description: Beskæftigede (ultimo november) efter bopælskommunegruppe, køn, pendlingsafstand og tid
columns: bopkomgrp, kon, pendafst, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2023-01-01
</table>
<table>
id: ligefb6
description: Beskæftigede efter familietype, pendlingsafstand, køn, alder og tid
columns: famtyp, pendafst, kon, alder, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2023-01-01
</table>
<table>
id: ligefi6
description: Ligestillingsindikator for pendlingsafstand (gennemsnitlig) for beskæftigede personer efter indikator, familietype, alder og tid
columns: indikator, famtyp, alder, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- For commuting flows between areas (OD matrix): use pend100. It contains counts of workers by (bopælskommune × arbejdsstedsområde). Both sides have all 3 nuts levels — always filter to a consistent niveau pair to avoid double-counting.
- For commuting counts by municipality broken down by industry and pendling type: use pend101. Pendling types: NAT=natbefolkning, DAG=dagbefolkning, IND=indpendlere, UD=udpendlere. Only kommune level (niveau 3) — no regional totals.
- For commuting DISTANCE counts by distance band: use afsta3 (by workplace area) or afstb3 (by residence area). These show how many workers fall into each pendlingsafstand bracket.
- For AVERAGE commuting distance in km: use afsta4 (by workplace area) or afstb4 (by residence area).
- For commuting by kommunegruppe type (Hovedstad/Storby/Provinsby/Opland/Land): use laby44.
- For commuting by family type and gender equality angle: use ligefb6 (counts by pendlingsafstand) or ligefi6 (average km by gender, a ligestillingsindikator).
- Critical pitfall — socio column: afsta3/afstb3/afsta4/afstb4 all have a socio column that looks like it joins dim.socio but does NOT. It uses a custom encoding (5=Selvstændige, 10=Medarbejdende ægtefæller, 15–40=Lønmodtager subcategories, and 2=Beskæftigede i alt in the afst*4 tables). Never join dim.socio on these tables.
- Critical pitfall — nuts hierarchy: area columns (arbejdssted, bopomr, bopkom) span all 3 nuts levels in the same column. Always join dim.nuts and filter to one niveau, or use the aggregate code 0=Hele landet (not in dim.nuts) directly for national figures.
- All tables cover 2008–2023 at annual frequency (ultimo november snapshot). No total-gender (TOT) in pend100/pend101 — must sum M+K explicitly.
- Map: pend101 (kommune only), pend100, afsta3, afsta4, afstb3, afstb4 all support choropleth maps via dim.nuts — see individual table notes for geo file and column details. laby44, ligefb6, ligefi6 have no geographic column.