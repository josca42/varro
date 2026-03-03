<fact tables>
<table>
id: bdf11
description: Bedrifter efter område, enhed, bedriftstype, areal og tid
columns: omrade, tal, bedrift, areal1, tid (time), indhold (unit -)
tid range: 2010-01-01 to 2024-01-01
</table>
<table>
id: bdf107
description: Bedrifter efter område, type, alder og tid
columns: omrade, type, alder, tid (time), indhold (unit -)
tid range: 2006-01-01 to 2024-01-01
</table>
<table>
id: bdf207
description: Bedrifter med forpagtning efter område, type, areal og tid
columns: omrade, type, areal1, tid (time), indhold (unit -)
tid range: 2006-01-01 to 2024-01-01
</table>
<table>
id: bdf51
description: Bedrifter efter område, udvalgte bedrifter afgrøder og husdyr og tid
columns: omrade, udbedrift, tid (time), indhold (unit -)
tid range: 2010-01-01 to 2020-01-01
</table>
<table>
id: bdf52
description: Bedrifter efter enhed, areal, landmandens alder og tid
columns: enhed, areal1, bdfalder, tid (time), indhold (unit -)
tid range: 1984-01-01 to 2024-01-01
</table>
<table>
id: bdf1974
description: Bedrifter (historisk) efter område, areal og tid
columns: amt, areal1, tid (time), indhold (unit Antal)
tid range: 1970-01-01 to 1981-01-01
</table>
<table>
id: bdf14
description: Bedrifter efter virksomhedsform, bedriftstype og tid
columns: virkf1, bedrift, tid (time), indhold (unit Antal)
tid range: 2006-01-01 to 2024-01-01
</table>
<table>
id: bdf15
description: Bedrifter efter virksomhedsform, bedriftsstørrelser og tid
columns: virkf1, bedriftstr, tid (time), indhold (unit Antal)
tid range: 2006-01-01 to 2024-01-01
</table>
<table>
id: forp1
description: Bedrifter med forpagtning efter enhed, areal, forpagtning og tid
columns: enhed, areal1, forp, tid (time), indhold (unit -)
tid range: 1982-01-01 to 2024-01-01
</table>
<table>
id: forp2
description: Bedrifter med forpagtning efter enhed, landmandens alder, forpagtning og tid
columns: enhed, bdfalder, forp, tid (time), indhold (unit -)
tid range: 1982-01-01 to 2024-01-01
</table>
<table>
id: bdf307
description: Beskæftigede i landbrug og gartneri efter område, enhed, type, arbejdstid og tid
columns: omrade, enhed, type, arbejdstid, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2023-01-01
</table>
<table>
id: bdf6
description: Medhjælpere i landbrug og gartneri efter område, antal ansatte, bedriftstype og tid
columns: omrade, ansatte, bedrift, tid (time), indhold (unit Antal)
tid range: 1982-01-01 to 2023-01-01
</table>
<table>
id: bdf7
description: Medhjælpere i landbrug og gartneri efter areal, antal ansatte, bedriftstype og tid
columns: areal1, ansatte, bedrift, tid (time), indhold (unit -)
tid range: 1982-01-01 to 2023-01-01
</table>
<table>
id: bdf807
description: Bedrifter efter område, beskæftigede uden for bedriften og tid
columns: omrade, beskland, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2023-01-01
</table>
<table>
id: bdf907
description: Bedrifter med andre aktiviteter end landbrug efter område, aktivitet og tid
columns: omrade, aktivi, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2023-01-01
</table>
<table>
id: pl1
description: Bedrifter efter enhed, præcisionsteknologi og tid
columns: enhed, praetek, tid (time), indhold (unit -)
tid range: 2018-01-01 to 2025-01-01
</table>
<table>
id: pl2
description: Bedrifter efter enhed, præcisionsteknologi, uddannelse og alder og tid
columns: enhed, praetek, udalder, tid (time), indhold (unit -)
tid range: 2018-01-01 to 2025-01-01
</table>
</fact tables>

notes:
- SHARED OMRADE PATTERN: bdf11, bdf107, bdf207, bdf307, bdf807, bdf907 all have omrade joining dim.nuts using plain integer codes: niveau 1 (81-85 = 5 regioner), niveau 2 (4,7,8,9,10 = 5 landsdele, NOT all 11 standard landsdele). Two aggregate codes not in dim.nuts: 0=Hele landet, 15=unidentified agricultural region (likely Sjælland og øerne). bdf51 joins dim.nuts at niveau 3 (kommuner). Use JOIN dim.nuts d ON f.omrade = d.kode.
- DIMENSION ERROR: bdf807 and bdf907 fact docs incorrectly list dim.landbrugslandsdele as the join target. Use dim.nuts instead.
- MEASURE-TYPE SELECTORS: Almost every table has an enhed/tal/type column that switches the measure (bedrifter count vs. areal in ha vs. forpagtet areal). Every dimension combination repeats for each selector value. Always filter to exactly one — omitting this silently multiplies counts.

Table selection guide:
- Farm counts + area by region/landsdel + farm type: bdf11 (2010-2024). For farm counts by virksomhedsform: bdf14 (national, 2006-2024). For farm sizes by virksomhedsform: bdf15 (national, 2006-2024; note bedriftstr mixes two size schemes — ha brackets and pig-count brackets).
- Farm counts by farmer age + region: bdf107 (2006-2024). By farmer age + farm size (national, longest series back to 1984): bdf52.
- Leased land (forpagtning) by region: bdf207 (2006-2024). National by farm size: forp1 (1982-2024). National by farmer age: forp2 (1982-2024). forp1/forp2 have the longest forpagtning series.
- Employment in agriculture by region + worker type + hours: bdf307 (2007-2023) — the main employment table with both farm counts (ANTAL) and person counts (PERS). Historical hired-worker data back to 1982 with very coarse geography (4 regions): bdf6 (by region) and bdf7 (by farm size).
- Municipality-level farm data by crop/livestock type: bdf51 (2010-2020 only — no more recent equivalent at kommune level).
- Off-farm work by farm household: bdf807 (2007-2023; beskland values are independent, not mutually exclusive).
- Non-agricultural activities on farm: bdf907 (2007-2023; aktivi values are independent; 5095=all farms with any secondary activity is the only valid total).
- Precision farming technology: pl1 (national, by technology type, 2018-2025; specific praetek codes are non-mutually-exclusive). pl2 (by education OR age, 2018-2025; udalder mixes two separate dimension groups — filter to one group at a time).
- Historical data 1970-1981: bdf1974 uses old amt codes (14 pre-reform counties) — no join to modern geography.
- Map: bdf11, bdf107, bdf207, bdf307, bdf807, bdf907 support choropleth at region level (/geo/regioner.parquet) or 5-landsdel level (/geo/landsdele.parquet) — merge on omrade=dim_kode, exclude omrade IN (0, 15). bdf51 supports kommune-level maps (/geo/kommuner.parquet) — merge on omrade=dim_kode, exclude omrade=0.