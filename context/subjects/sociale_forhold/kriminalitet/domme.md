<fact tables>
<table>
id: straf40
description: Strafferetlige afgørelser efter overtrædelsens art, afgørelsestype, alder, køn og tid
columns: overtraed, afgorelse, alder, kon, tid (time), indhold (unit Antal)
tid range: 1980-01-01 to 2024-01-01
</table>
<table>
id: straf42
description: Strafferetlige afgørelser efter national oprindelse, overtrædelsens art, afgørelsestype, alder, køn og tid
columns: herkomst1, overtraed, afgorelse, alder, kon, tid (time), indhold (unit Antal)
tid range: 1995-01-01 to 2024-01-01
</table>
<table>
id: straf43
description: Strafferetlige afgørelser pr. 100.000 indbyggere efter afgørelsestype, køn, alder og tid
columns: afgorelse, kon, alder, tid (time), indhold (unit Antal)
tid range: 2018-01-01 to 2024-01-01
</table>
<table>
id: straf44
description: Strafferetlige afgørelser efter område, overtrædelsens art, afgørelsestype, alder, køn og tid
columns: omrade, overtraed, afgorelse, alder, kon, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: straf46
description: Betingede frihedsstraffe efter område, køn, alder, overtrædelsens art, afgørelsestype, straflængde og tid
columns: omrade, koen, alder, overtraed, afgorelse, straflang, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: straf47
description: Ubetingede frihedsstraffe efter område, køn, alder, overtrædelsens art, afgørelsestype, straflængde og tid
columns: omrade, koen, alder, overtraed, afgorelse, straflang, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: straf49
description: Gennemsnitlig straflængde (mdr.) for ubetingede frihedsstraffe efter køn, alder, overtrædelsens art, afgørelsestype og tid
columns: koen, alder, overtraed, afgorelse, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: straf48
description: Gennemsnitlig straflængde(mdr.) for betingede frihedsstraffe efter køn, alder, overtrædelsens art, afgørelsestype og tid
columns: koen, alder, overtraed, afgorelse, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: straf61
description: Afgjorte biforhold efter overtrædelsens art, afgørelsestype, alder, køn og tid
columns: overtraed, afgorelse, alder, kon, tid (time), indhold (unit Antal)
tid range: 1980-01-01 to 2024-01-01
</table>
<table>
id: ligepb4
description: Domme for personfarlig kriminalitet efter overtrædelsens art, alder, køn og tid
columns: overtraed, alder, koen, tid (time), indhold (unit Antal)
tid range: 1991-01-01 to 2024-01-01
</table>
<table>
id: ligepi4
description: Ligestillingsindikator for domme for personfarlig kriminalitet efter overtrædelsens art, alder, indikator og tid
columns: overtraed, alder, indikator, tid (time), indhold (unit -)
tid range: 1991-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- For general sentenced convictions (all verdict types, crime types, gender, age): straf40 (1980-2024, no region) or straf44 (2007-2024, with regional breakdown by region/kommune). straf42 adds national origin (herkomst1) from 1995.
- For population-normalised conviction rates (per 100,000): straf43 (2018-2024 only, no crime type breakdown — indhold is a rate, never sum).
- For sentence length analysis: straf46 (betingede/conditional) and straf47 (ubetingede/unconditional) give count distributions by sentence length bands. straf48/straf49 give average sentence length in months (indhold = average, never sum these either).
- For secondary charges (biforhold): straf61 — counts adjudicated secondary matters with a simple guilty/not-guilty afgorelse. Goes back to 1980.
- For violent crime (personfarlig kriminalitet) specifically: ligepb4 (raw counts, 1991-2024) or ligepi4 (gender equality indicator — rates per 100,000 and male/female point difference). These use LS-prefix overtraed codes that are NOT compatible with the straf tables.
- Naming inconsistency: straf40/42/44/61 call the gender column kon; straf46/47/48/49/ligepb4/ligepi4 call it koen. straf40/42/44/61 also include VIRKSOMHEDER (companies) in kon; the koen tables are persons only.
- afgorelse is hierarchical across all straf tables: 000/0 = I alt, 1/2/3/4/5 = main types, 11/12 = sub-types, 111-118/121-124 = specific. straf46 restricted to codes 0/121-124 (betingede); straf47/48/49 restricted to 0/111-118 (ubetingede).
- overtraed uses the same hierarchical scheme in straf40/42/44/61/47/48/49 (TOT → 1/2/3 → 11/12... → 4-digit). straf47/48/49/61 join dim.overtraedtype (niveaux 1-3); straf40/42/44 treat it as inline. ligepb4/ligepi4 use a separate LS-prefix scheme — incompatible.
- Always filter all aggregate/total codes when counting. Forgetting overtraed='TOT', afgorelse='000', alder='TOT', and kon/koen='TOT' silently multiplies results.
- Map: straf44, straf46, straf47 support choropleth maps via context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Kommune data can also be aggregated to 12 politikredse via dim.politikredse and mapped with context/geo/politikredse.parquet.