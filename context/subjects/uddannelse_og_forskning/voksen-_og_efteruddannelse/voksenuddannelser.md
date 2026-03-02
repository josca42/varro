<fact tables>
<table>
id: veu20
description: Kursusdeltagelse ved voksen og efteruddannelse efter uddannelsesområde, bopælsområde, alder, køn, tidsangivelse, enhed og tid
columns: fuddomr, bopomr, alder, kon, tidspunkter, overnat1, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: veuhel10
description: Personer der har fuldført en hel voksenuddannelse efter uddannelse, alder, køn, herkomst, tidsangivelse og tid
columns: uddannelse, alder, kon, herkams, tidspunkter, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: veuhel20
description: Personer der har fuldført en hel voksenuddannelse efter uddannelse, køn, højest fuldførte uddannelse, tidsangivelse og tid
columns: uddannelse, kon, hfudd, tidspunkter, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: ligeui2
description: Ligestillingsindikator for kursusdeltagelse ved voksen og efteruddannelse efter uddannelsesområde, indikator, alder, bopælsområde, enhed, tidsangivelse og tid
columns: fuddomr, indikator1, alder, bopomr, overnat1, tidspunkter, tid (time), indhold (unit -)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: cvts1
description: Efteruddannelse i virksomhederne (CVTS) efter type af efteruddannelse på virksomhed, antal ansatte og tid
columns: eftervir, ansatte, tid (time), indhold (unit Pct.)
tid range: 2005-01-01 to 2020-01-01
</table>
</fact tables>

notes:
- For course participation (kursusdeltagelse) by region, age, gender, or education area: use veu20. It has regional breakdown via dim.nuts (kommune/landsdel/region), a deep 4-level fuddomr hierarchy, and goes back to 2005. veu20 always needs two measurement-selector filters: overnat1 (Kursister=11 or Årselever=13) AND tidspunkter (Kalenderår=11 or Skoleår=22).
- For gender equality indicators on course participation: use ligeui2. It reports male %, female %, and gap (procentpoint) across regions and education areas. indhold is a rate — never sum across indikator1 values.
- For people who completed a whole adult education (fuldført hel voksenuddannelse): use veuhel10 (with age and herkomst breakdown) or veuhel20 (with prior education level breakdown). Both need a tidspunkter filter; skoleår and kalenderår differ for multi-year programs (KVU/MVU/BACH/LVU).
- For employer-provided training in companies (CVTS survey): use cvts1. Covers 2005, 2010, 2015, 2020 only (every 5 years). indhold is % of companies — not headcounts, not annual data.
- Common pitfall across veu20 and ligeui2: bopomr='0' is the national total and is not in dim.nuts. Join dim.nuts only when filtering by named region. Filter d.niveau to avoid mixing geographic levels.
- Common pitfall across veu20, veuhel10, veuhel20, ligeui2: tidspunkter doubles (or for veu20 quadruples with overnat1) the row count. Always filter to a single tidspunkter value.
- Map: veu20 and ligeui2 support choropleth maps via bopomr — use context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1). Merge on bopomr=dim_kode; exclude bopomr=0 (and bopomr=996 for veu20).