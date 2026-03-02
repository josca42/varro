<fact tables>
<table>
id: bil600
description: Familiernes bilkøb (faktiske tal) efter område, købsmønster og tid
columns: omrade, koebmoens, tid (time), indhold (unit Antal)
tid range: 2006-01-01 to 2024-01-01
</table>
<table>
id: bil611
description: Familiernes bilkøb (andele og fordelinger) efter område, enhed, købsmønster og tid
columns: omrade, maengde4, koebmoens, tid (time), indhold (unit Pct.)
tid range: 2006-01-01 to 2024-01-01
</table>
<table>
id: bil62
description: Familiernes bilkøb (faktiske tal) efter købstype, familietype, købsmønster og tid
columns: koebtype, famtyp, koebmoens, tid (time), indhold (unit Antal)
tid range: 1999-01-01 to 2024-01-01
</table>
<table>
id: bil63
description: Familiernes bilkøb (andele og fordelinger) efter enhed, familietype, købsmønster og tid
columns: maengde4, famtype, koebmoens, tid (time), indhold (unit Pct.)
tid range: 1999-01-01 to 2024-01-01
</table>
<table>
id: bil64
description: Familiernes bilkøb (faktiske tal) efter købstype, uddannelse, købsmønster og tid
columns: koebtype, uddannelse, koebmoens, tid (time), indhold (unit Antal)
tid range: 1999-01-01 to 2023-01-01
</table>
<table>
id: bil65
description: Familiernes bilkøb (andele og fordelinger) efter enhed, uddannelse, købsmønster og tid
columns: maengde4, uddannelse, koebmoens, tid (time), indhold (unit Pct.)
tid range: 1999-01-01 to 2023-01-01
</table>
<table>
id: bil66
description: Familiernes bilkøb (faktiske tal) efter købstype, indkomst, købsmønster og tid
columns: koebtype, indkom, koebmoens, tid (time), indhold (unit Antal)
tid range: 1999-01-01 to 2023-01-01
</table>
<table>
id: bil67
description: Familiernes bilkøb (andele og fordelinger) efter enhed, indkomst, købsmønster og tid
columns: maengde4, indkom, koebmoens, tid (time), indhold (unit Pct.)
tid range: 1999-01-01 to 2023-01-01
</table>
<table>
id: bil68
description: Familiernes bilkøb (faktiske tal) efter købstype, boligforhold, købsmønster og tid
columns: koebtype, bol, koebmoens, tid (time), indhold (unit Antal)
tid range: 1999-01-01 to 2023-01-01
</table>
<table>
id: bil69
description: Familiernes bilkøb (andele og fordelinger) efter enhed, boligforhold, købsmønster og tid
columns: maengde4, bol, koebmoens, tid (time), indhold (unit Pct.)
tid range: 1999-01-01 to 2023-01-01
</table>
<table>
id: bil70
description: Familiernes bilkøb (faktiske tal) efter købstype, socioøkonomisk status, købsmønster og tid
columns: koebtype, socio, koebmoens, tid (time), indhold (unit Antal)
tid range: 1999-01-01 to 2023-01-01
</table>
<table>
id: bil71
description: Familiernes bilkøb (andele og fordelinger) efter enhed, socioøkonomisk status, købsmønster og tid
columns: maengde4, socio, koebmoens, tid (time), indhold (unit Pct.)
tid range: 1999-01-01 to 2023-01-01
</table>
<table>
id: bil72
description: Familiernes bilkøb (faktiske tal) efter bystørrelse, købsmønster og tid
columns: byst, koebmoens, tid (time), indhold (unit Antal)
tid range: 2016-01-01 to 2024-01-01
</table>
<table>
id: bil73
description: Familiernes bilkøb (andele og fordelinger) efter enhed, bystørrelse, købsmønster og tid
columns: maengde4, byst, koebmoens, tid (time), indhold (unit Pct.)
tid range: 2016-01-01 to 2024-01-01
</table>
</fact tables>
notes:
- Tables come in pairs: one "faktiske tal" (Antal counts, even-ish IDs: bil600/62/64/66/68/70/72) and one "andele og fordelinger" (Pct. shares, odd-ish IDs: bil611/63/65/67/69/71/73). Use faktiske tal for counts and sums; use andele for percentage breakdowns.
- All "andele" tables contain maengde4 — a MEASUREMENT SELECTOR with two values (50=Procentfordelingen, 60=Andel af det totale bilkøb) that doubles every row. Always filter to one value of maengde4 or results are doubled.
- All tables share koebmoens: a hierarchical column with 26 purchase-pattern codes. Use 10020 for "families who bought or leased a car" and 10000 for all families. The detailed sub-codes (10030–10149) describe specific combinations of bought/leased cars — they are sub-categories of 10020, not separate populations.
- Tables bil62–bil71 (by demographic breakdown) split their time series into two koebtype values due to a methodology change around 2006: bil62/63 break at 2007 (31 vs 32), bil64–71 break at 2006 (33 vs 34). Both periods are in the same table; always filter to one koebtype per year, or UNION the two periods explicitly.
- Geographic breakdown: bil600/611 use NUTS dimension (région/landsdel/kommune, back to 2006). bil72/73 use bystørrelse (city size bands, only from 2016). These are different geographic framings — pick based on question.
- Demographic breakdown tables (bil62–bil71) each cover one dimension: familietype (62/63), uddannelse (64/65), indkomst (66/67), boligforhold (68/69), socioøkonomisk status (70/71). All go back to 1999; bil64–bil71 latest data is 2023, bil62/63 go to 2024.
- indkomst tables (bil66/67): indkom has THREE parallel grouping schemes simultaneously (absolute kr-bands, deciles 1DC–10DC, quartiles 1KV–4KV). Pick one scheme — summing all triplicates the total.
- boligforhold tables (bil68/69): bol has TWO parallel schemes (boligtype: 110–610, ejerform: 620–640). Pick one scheme.
- socioøkonomisk status tables (bil70/71): socio is hierarchical — 110=Selvstændige (parent of 111+112), 130=Lønmodtagere (parent of 131–136), 515=Pensionister (parent of 520+522+525). Don't mix parent and child codes.
- Map: bil600 and bil611 support choropleth maps at all three NUTS levels — context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Remaining tables have no geographic column.
