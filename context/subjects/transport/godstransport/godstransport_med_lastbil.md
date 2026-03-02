<fact tables>
<table>
id: nvg1
description: National vejgodstransport efter enhed, kørselsart, vogntype/totalvægt, bilens alder, turlængde og tid
columns: enhed, korart, typevaegt, bilalder, turkm, tid (time), indhold (unit -)
tid range: 1999-01-01 to 2024-01-01
</table>
<table>
id: nvg11
description: National vejgodstransport efter kørselsart, enhed og tid
columns: korart, enhed, tid (time), indhold (unit -)
tid range: 1999-01-01 to 2025-04-01
</table>
<table>
id: nvg5
description: Danske lastbiler kapacitetsudnyttelse ved national transport efter enhed, turlængde, vogntype/kørselsart, læs og tid
columns: enhed, turkm, vogn, laes, tid (time), indhold (unit Pct.)
tid range: 1999-01-01 to 2024-01-01
</table>
<table>
id: nvg121
description: National vejgodstransport efter kørselsart, godsart, enhed og tid
columns: korart, gods, enhed, tid (time), indhold (unit -)
tid range: 2008-01-01 to 2025-04-01
</table>
<table>
id: nvg23
description: National vejgodstransport mellem regioner efter enhed, pålæsningsregion, aflæsningsregion, godsart og tid
columns: enhed, paregion, afregion, gods, tid (time), indhold (unit -)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: nvg13
description: Danske lastbilers kapacitetsudnyttelse ved national vejgodstransport efter enhed, kørselsart, læs og tid
columns: enhed, korart, laes, tid (time), indhold (unit -)
tid range: 1999-01-01 to 2025-04-01
</table>
<table>
id: nvg33
description: National vejgodstransport med farligt gods efter enhed, pålæsningsregion, aflæsningsregion, godsart og tid
columns: enhed, paregion, afregion, gods, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: nvg41
description: National vejgodstransport efter enhed, lasttype, godsart og tid
columns: enhed, lasttype, gods, tid (time), indhold (unit -)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: uvg1
description: Vejgodstransport med udenlandsk lastbil efter enhed, registreringsland, kørselsart og tid
columns: enhed, reg, korart, tid (time), indhold (unit -)
tid range: 2000-01-01 to 2024-01-01
</table>
<table>
id: ivg11
description: International vejgodstransport med dansk lastbil efter kørselsart, enhed og tid
columns: korart, enhed, tid (time), indhold (unit -)
tid range: 1999-01-01 to 2025-04-01
</table>
<table>
id: ivg41
description: International vejgodstransport efter enhed, kørselsart, lasttype, godsart og tid
columns: maengde4, korart, lasttype, gods, tid (time), indhold (unit -)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: ivg121
description: International godstransport med dansk lastbil efter kørselsart, godsart, enhed og tid
columns: korart, gods, enhed, tid (time), indhold (unit -)
tid range: 2008-01-01 to 2025-04-01
</table>
<table>
id: ivg13
description: International vejgodstransport  med dansk lastbil efter kørselsart, land, enhed og tid
columns: korart, land, enhed, tid (time), indhold (unit -)
tid range: 1999-01-01 to 2025-04-01
</table>
<table>
id: ivg6
description: Danske lastbilers kapacitetsudnyttelse ved international transport efter enhed, turlængde, kørselsart/vogntype, læs og tid
columns: maengde4, turkm, vogn1, laes, tid (time), indhold (unit -)
tid range: 1999-01-01 to 2024-01-01
</table>
<table>
id: ivg14
description: Danske lastbilers kapacitetsudnyttelse ved international vejgodstransport efter kørselsart, læs, enhed og tid
columns: korart, laes, enhed, tid (time), indhold (unit -)
tid range: 1999-01-01 to 2025-04-01
</table>
<table>
id: ivg5
description: International vejgodstransport efter enhed, startland, slutland og tid
columns: maengde4, start1, slut1, tid (time), indhold (unit -)
tid range: 1999-01-01 to 2024-01-01
</table>
<table>
id: ivg23
description: International vejgodstransport mellem lande efter enhed, pålæsningsland, aflæsningsland, godsart og tid
columns: maengde4, paland, afland, gods, tid (time), indhold (unit -)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: ivg1
description: International vejgodstransport efter enhed, vogntype/totalvægt, bilens alder, turlængde og tid
columns: maengde4, typevaegt, bilalder, turkm, tid (time), indhold (unit -)
tid range: 1999-01-01 to 2024-01-01
</table>
<table>
id: ivg3
description: International vejgodstransport med farligt gods efter enhed, kørselsart, godsart og tid
columns: maengde4, korart, gods, tid (time), indhold (unit -)
tid range: 1999-01-01 to 2024-01-01
</table>
<table>
id: vg2
description: Vejgodstransport (faktiske tal) efter kørselsart, enhed og tid
columns: korart, maengde4, tid (time), indhold (unit -)
tid range: 1998-01-01 to 2025-04-01
</table>
<table>
id: vg3
description: Vejgodstransport (sæsonkorrigeret) efter kørselsart, enhed og tid
columns: korart, enhed, tid (time), indhold (unit -)
tid range: 2010-01-01 to 2025-04-01
</table>
</fact tables>
notes:
- Table prefix tells you the scope: nvg*=national vejgodstransport (domestic), ivg*=international vejgodstransport (Danish trucks abroad), uvg*=udenlandsk lastbil (foreign trucks in Denmark), vg*=combined summary.
- Suffix pattern: *11=simplest aggregate (korart×enhed×tid), *1=detailed truck breakdown (typevaegt/bilalder/turkm), *121=goods type breakdown, *13/*14=country/capacity by direction, *23=origin-destination matrix, *33=dangerous goods between regions, *41=load type + goods, *5=capacity utilization by trip distance, *6=international capacity utilization detailed.
- For national freight time series: nvg11 (from 1999, most dates, simplest). For international freight time series: ivg11 (from 1999).
- For combined national+international overview: vg2 (actual figures, from 1998) or vg3 (seasonally adjusted, from 2010).
- For goods type breakdown: nvg121/ivg121 (5 broad NST-R categories, from 2008) or nvg41/ivg41 (more detailed NST-2000 goods + lasttype split, from 2008).
- For regional origin-destination: nvg23 (all goods between 11 landsdele) or nvg33 (dangerous goods only between landsdele).
- For country-level international flows: ivg5 (8 enhed options, start/end country matrix, from 1999) or ivg23 (goods breakdown added but only tons/tonkm, from 2008). For a simple 9-country grouping use ivg13 (inline codes, no dim join needed).
- For foreign trucks: uvg1 (by registration country via dim.lande_psd, from 2000).
- For truck characteristics (vehicle type, age, trip distance): nvg1 (national) or ivg1 (international).
- For capacity utilization: nvg13/ivg14 (simple, by korart+læs) or nvg5/ivg6 (detailed, by trip distance and vehicle/direction type).
- For dangerous goods: nvg33 (national, by region) or ivg3 (international, by direction).
- Map: nvg23 and nvg33 support choropleth at landsdel level (context/geo/landsdele.parquet) via paregion/afregion. All other tables have no Danish geographic column.
- Universal pitfall: enhed (or maengde4) is a measurement selector present in every table — every row repeats per measurement unit. Always filter to one enhed/maengde4 value or results will be multiplied.
- Universal pitfall: korart always has an aggregate total (1000=KØRSEL I ALT) plus breakdown codes that sum to it. Never sum the total with its children.
- laes (present in nvg5, nvg13, ivg6, ivg14): 1010=inkl. tomkørsel contains 1030=med læs. Not mutually exclusive — always pick one.
- gods hierarchies: total codes (100 or 700) are always the sum of their children. The layered gods in nvg23/ivg23 (1xx/2xx/3xx groups) overlap — use only one group at a time.
