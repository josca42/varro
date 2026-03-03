<fact tables>
<table>
id: uddakt10
description: Uddannelsesaktivitet efter bopælsområde, uddannelse, alder, køn, status og tid
columns: bopomr, uddannelse, alder, kon, fstatus, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: uddakt11
description: Uddannelsesaktivitet efter institutionens beliggenhedsområde, uddannelse, alder, køn, status og tid
columns: omrade1, uddannelse, alder, kon, fstatus, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: uddakt12
description: Uddannelsesaktivitet efter uddannelse, alder, herkomst, national oprindelse, køn, status og tid
columns: uddannelse, alder, herkomst, herkomst1, kon, fstatus, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: ligeub6
description: Uddannelsesaktivitet på STEM-uddannelser efter uddannelse, køn og tid
columns: uddannelse, kon, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: ligeui6
description: Ligestillingsindikator for uddannelsesaktivitet på STEM-uddannelser efter uddannelse, indikator og tid
columns: uddannelse, indikator, tid (time), indhold (unit -)
tid range: 2005-01-01 to 2024-01-01
</table>
<table>
id: ligeui3
description: Ligestillingsindikator for uddannelsesaktivitet efter uddannelse, indikator, alder, bopælsområde og tid
columns: uddannelse, indikator1, alder, bopomr, tid (time), indhold (unit -)
tid range: 2005-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- For education activity by student residence: uddakt10 (bopomr). For education activity by school location: uddakt11 (omrade1). Both cover all education levels 2005–2024 with alder, kon, and fstatus.
- For education activity by ethnic background (herkomst/national origin): uddakt12. No geographic breakdown, national only.
- fstatus is a shared measurement selector across all uddakt tables: B=enrolled 1 October, F=completed, T=new entrants. Always filter to exactly one value — forgetting this triples counts.
- uddannelse hierarchy is the same across uddakt10/11/12: TOT → top-level (H10=Grundskole, H15=Forberedende, H20=Gymnasiale, H29=Erhvervsfaglige grundforløb, H30=Erhvervsfaglige, H35=Adgangsgivende, H40=KVU, H50=MVU, H60=Bachelor, H70=LVU, H80=Ph.d.) → sub-codes. Don't mix levels when summing.
- For STEM enrollment counts (higher ed only, with STEM/non-STEM split): ligeub6. For gender balance rates in STEM (higher ed only): ligeui6. For gender balance rates across all education types with age and regional breakdown: ligeui3.
- ligeui6 and ligeui3 hold rates/percentages — never sum indhold across rows. Use for gender analysis only, not enrollment counts.
- Map: uddakt10 (bopomr=student residence), uddakt11 (omrade1=school location), and ligeui3 (bopomr) all support choropleth maps at kommune (niveau 3) or region (niveau 1) level via /geo/kommuner.parquet or /geo/regioner.parquet.