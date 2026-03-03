<fact tables>
<table>
id: km1
description: Befolkningen den 1. i kvartalet efter sogn, folkekirkemedlemsskab og tid
columns: sogn, fkmed, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2025-07-01
</table>
<table>
id: km11
description: Befolkningen den 1. i kvartalet efter provsti, folkekirkemedlemsskab og tid
columns: provsti, fkmed, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2025-07-01
</table>
<table>
id: km5
description: Befolkningen 1. januar efter sogn, køn, alder, folkekirkemedlemsskab og tid
columns: sogn, kon, alder, fkmed, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2025-01-01
</table>
<table>
id: km55
description: Befolkningen 1. januar efter provsti, køn, alder, folkekirkemedlemsskab og tid
columns: provsti, kon, alder, fkmed, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2025-01-01
</table>
<table>
id: km6
description: Befolkningen 1. januar efter kommune, køn, alder, folkekirkemedlemsskab og tid
columns: komk, kon, alder, fkmed, tid (time), indhold (unit Antal)
tid range: 2011-01-01 to 2025-01-01
</table>
<table>
id: kmsta001
description: Befolkningen 1. januar efter sogn, herkomst, folkekirkemedlemsskab og tid
columns: sogn, herkomst, fkmed, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2025-01-01
</table>
<table>
id: kmsta002
description: Befolkningen 1. januar efter provsti, herkomst, folkekirkemedlemsskab og tid
columns: provsti, herkomst, fkmed, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2025-01-01
</table>
<table>
id: kmsta005
description: Befolkningen 1. januar (15 år+) efter sogn, socioøkonomisk status, folkekirkemedlemsskab og tid
columns: sogn, socio, fkmed, tid (time), indhold (unit Antal)
tid range: 2016-01-01 to 2024-01-01
</table>
<table>
id: kmsta006
description: Befolkningen 1. januar (15 år+) efter provsti, socioøkonomisk status, folkekirkemedlemsskab og tid
columns: provsti, socio, fkmed, tid (time), indhold (unit Antal)
tid range: 2016-01-01 to 2024-01-01
</table>
<table>
id: kmsta009
description: Befolkningen 1. januar (15 år+) efter sogn, folkekirkemedlemsskab, pendling og tid
columns: sogn, fkmed, pendling, tid (time), indhold (unit Antal)
tid range: 2016-01-01 to 2024-01-01
</table>
<table>
id: kmsta010
description: Befolkningen 1. januar (15 år+) efter provsti, folkekirkemedlemsskab, pendling og tid
columns: provsti, fkmed, pendling, tid (time), indhold (unit Antal)
tid range: 2016-01-01 to 2024-01-01
</table>
<table>
id: sogn1
description: Befolkningen 1. januar efter sogn, køn, alder og tid
columns: sogn, kon, alder, tid (time), indhold (unit Antal)
tid range: 2010-01-01 to 2025-01-01
</table>
<table>
id: kmst007a
description: Befolkningen 1. oktober (15 år+) efter sogn, folkekirkemedlemsskab, højest fuldførte uddannelse og tid
columns: sogn, fkmed, uddannelsef, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: kmst008a
description: Befolkningen 1. oktober (15 år+) efter provsti, folkekirkemedlemsskab, højest fuldførte uddannelse og tid
columns: provsti, fkmed, uddannelsef, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: km2
description: Ind- og udmeldelser af folkekirken efter sogn, alder, folkekirkemedlemsskab og tid
columns: sogn, alder, fkmed, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2025-04-01
</table>
<table>
id: km22
description: Ind- og udmeldelser af folkekirken efter provsti, alder, folkekirkemedlemsskab og tid
columns: provsti, alder, fkmed, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2025-04-01
</table>
<table>
id: km3
description: Levendefødte og døde efter sogn, bevægelse og tid
columns: sogn, bevaegelsev, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2025-04-01
</table>
<table>
id: km33
description: Levnedefødte og døde efter provsti, bevægelse og tid
columns: provsti, bevaegelsev, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2025-04-01
</table>
<table>
id: kmsta003
description: Befolkningens udvikling efter sogn, bevægelser og tid
columns: sogn, kirkebev, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
<table>
id: kmsta004
description: Befolkningens udvikling efter provsti, bevægelser og tid
columns: provsti, kirkebev, tid (time), indhold (unit Antal)
tid range: 2015-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Tables come in sogns/provsti pairs sharing the same structure: km1/km11, km5/km55, km2/km22, km3/km33, kmsta001/002, kmsta003/004, kmsta005/006, kmsta009/010, kmst007a/008a. Pick the geographic level first, then find the matching table.
- Three data types in this subject — choose based on the question:
  1. Membership stock (how many members at a point in time): km1/km11 (quarterly, simple), km5/km55 (annual, age+gender), km6 (annual, by kommune with dim join).
  2. Membership flows (joinings/leavings): km2/km22 (quarterly, by age). fkmed here means F=Indmeldt, U=Udmeldt — NOT membership status.
  3. Demographic context without fkmed: km3/km33 (births/deaths), kmsta003/004 (full population dynamics), sogns1 (total population by sogns for denominators).
- Geography: sogns (~2292 codes, inline) vs. provsti (111 codes, inline) vs. kommune (99, joins dim.nuts niveau 3, km6 only). Sogns is finest, provsti is a church administrative grouping not aligned with standard NUTS regions. If user asks by kommune/region, use km6 (joins dim.nuts).
- For membership rate by area: km1 or km5 (numerator fkmed='F') divided by sogns1 total (no fkmed filter) by the same sogns. Or compute directly: SUM(CASE WHEN fkmed='F' THEN indhold END)::float / SUM(indhold) within km1.
- Demographic breakdown tables (kmsta001/002 herkomst, kmsta005/006 socio, kmst007a/008a uddannelse, kmsta009/010 pendling) all cover subsets: herkomst from 2008, the rest from 2015/2016 and 15+ only.
- herkomst warning: kmsta001/002 use a 5-code scheme (1, 24, 25, 34, 35) not matching dim.herkomst. Do NOT join dim.herkomst. Labels: 1=Dansk oprindelse, 24=Indvandrere vestlige, 25=Indvandrere ikke-vestlige, 34=Efterkommere vestlige, 35=Efterkommere ikke-vestlige.
- pendling warning (kmsta009/010): pendling is a measurement SELECTOR, not an additive category. Always filter to ONE value. Use 10=Natbefolkning for standard resident-based counts.
- kirkebev warning (kmsta003/004): 17 values including derived aggregates. Never sum across them. Use B20A for stock, B11 for annual growth, individual flow codes (B02, B03, B05, B06) for primary movements.
- kmst007a/008a use 1. oktober as reference date (not 1. januar). tid is stored as yyyy-01-01 but represents October snapshot.
- All tables with fkmed (F/U) have BOTH rows for every combination — always filter or explicitly sum both. No implicit total rows.
- Exclude sogns 0='Uden placerbar adresse' and 9999='Uden fast bopæl' for geographic analysis.
- Map: All sogns-level tables (km1, km5, km2, km3, kmsta001, kmsta003, kmsta005, kmsta009, kmst007a, sogns1) support choropleth maps via /geo/sogne.parquet (merge on sogns=dim_kode). km6 supports kommune-level maps via /geo/kommuner.parquet (merge on komk=dim_kode). Provsti tables have no geo file.
