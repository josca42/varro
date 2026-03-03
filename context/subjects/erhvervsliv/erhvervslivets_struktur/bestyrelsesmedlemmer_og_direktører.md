<fact tables>
<table>
id: best11
description: Bestyrelsesmedlemmer og direktører efter type, køn, uddannelse, alder, bopælsområde og tid
columns: type, kon, uddannelse, alder, bopland, tid (time), indhold (unit Antal)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: best12
description: Bestyrelsesmedlemmer og direktører efter type, virksomhedsstørrelse, køn og tid
columns: type, virkstr, kon, tid (time), indhold (unit Antal)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: best13
description: Bestyrelsesmedlemmer og direktører efter type, virksomhedsstørrelse, uddannelse og tid
columns: type, virkstr, uddannelse, tid (time), indhold (unit Antal)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: best14
description: Bestyrelsesmedlemmer og direktører efter type, branche (DB07 19-grp), køn og tid
columns: type, branchedb0721, kon, tid (time), indhold (unit Antal)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: best15
description: Bestyrelsesmedlemmer og direktører efter type, branche (DB07 19-grp), uddannelse og tid
columns: type, branchedb0721, uddannelse, tid (time), indhold (unit Antal)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: best16
description: Bestyrelsesmedlemmer efter bestyrelsespost, køn, uddannelse, alder og tid
columns: bestpost, kon, uddannelse, alder, tid (time), indhold (unit Antal)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: best17
description: Bestyrelsesmedlemmer efter valgform, køn, virksomhedsstørrelse, branche (DB07 19-grp) og tid
columns: vform, kon, virkstr, branchedb0721, tid (time), indhold (unit Antal)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: best18
description: Bestyrelsesmedlemmer efter bestyrelsesmedlem, firmastatus, køn, virksomhedsstørrelse, branche (DB07 19-grp) og tid
columns: bestmedl, firmastat, kon, virkstr, branchedb0721, tid (time), indhold (unit Antal)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: best19
description: Bestyrelsesmedlemmer efter bestyrelsesmedlem, firmastatus, køn, virksomhedsstørrelse, branche (DB07 19-grp) og tid
columns: bestmedl, firmastat, kon, virkstr, branchedb0721, tid (time), indhold (unit Antal)
tid range: 2023-01-01 to 2023-01-01
</table>
<table>
id: ligedi11
description: Ligestillingsindikator for bestyrelsesmedlemmer og direktører efter indikator, type, uddannelse, alder og tid
columns: indikator, type, uddannelse, alder, tid (time), indhold (unit -)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: ligedi12
description: Ligestillingsindikator for bestyrelsesmedlemmer og direktører efter indikator, type, virksomhedsstørrelse og tid
columns: indikator, type, virkstr, tid (time), indhold (unit -)
tid range: 2019-01-01 to 2023-01-01
</table>
<table>
id: ligedi13
description: Ligestillingsindikator for bestyrelsesmedlemmer og direktører efter indikator, type, branche (DB07 19-grp) og tid
columns: indikator, type, branchedb0721, tid (time), indhold (unit -)
tid range: 2019-01-01 to 2023-01-01
</table>
</fact tables>

notes:
- best11–best15 cover 2019–2023 (annual). best16–best19 cover 2023 only with specialised breakdowns.
- For counts broken down by gender/education/age/region: use best11. For by firm size or industry: best12 (size × gender), best13 (size × education), best14 (industry × gender), best15 (industry × education).
- For gender-equality rates (% women/men, gender gap in procentpoint): use ligedi11 (by education/age), ligedi12 (by firm size), ligedi13 (by industry). indhold in these tables is percentages/procentpoint — never sum across the indikator column. Pick one: LA1=mænd pct, LA2=kvinder pct, LA3=forskel.
- best16: board members by number of seats held (1–5+). No "I alt" for bestpost — sum across categories. Useful for identifying serial board members.
- best17: board members by election method (generalforsamling, medarbejdervalgt, etc.). 2023 only.
- best18 vs best19: entry/exit flow tables (2023 only). best18 = who joined or continued. best19 = who left or continued. Not comparable to stock counts in best11–best15.
- branchedb0721 in all industry tables (best14, best15, best17, best18, best19, ligedi13) uses DB07 19-group letter codes (A–S, X, TOT). These do NOT join dim.db. Use ColumnValues on the fact table directly for labels.
- All count tables (best11–best19) include total rows: type='10', kon='100', virkstr='3001', uddannelse='TOT', alder='IALT'. Always filter non-target dimensions to their total to avoid overcounting.
- Map: best11 supports choropleth maps at landsdel level via /geo/landsdele.parquet — merge on bopland=dim_kode, exclude bopland IN (0, 12). Other tables have no geographic dimension.