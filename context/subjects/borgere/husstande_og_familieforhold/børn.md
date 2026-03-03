<fact tables>
<table>
id: fam111n
description: Børn 1. januar efter område, familietype, antal personer i familien, antal børn i familien, køn, alder og tid
columns: omrade, famtyp, antpf, antbrnf, kon, alder, tid (time), indhold (unit Antal)
tid range: 1986-01-01 to 2025-01-01
</table>
<table>
id: fam133n
description: Børn 1. januar efter område, husstandstype, antal personer i husstand , antal børn i husstand, køn, alder og tid
columns: omrade, hustyp, antpersh, antbornh, kon, alder, tid (time), indhold (unit Antal)
tid range: 1986-01-01 to 2025-01-01
</table>
<table>
id: brn13
description: Børn efter område, voksne i bopælsfamilien , bopælsfamilietype, voksne i samværsfamilien  , samværsfamilietype, alder og tid
columns: omr20, voksbofam, bofamtyp, voksamfam, samfamtyp, alder, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2025-01-01
</table>
<table>
id: brn15
description: Børn fordelt på søskende de bor sammen med - antal og kombination efter område, alder, familietype, antal søskende, kombination af søskende og tid
columns: omrade, alder, famtype, antsos, kombsos, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2025-01-01
</table>
<table>
id: brn16
description: Børn fordelt på alle søskende - antal og kombination efter område, alder, familietype, antal søskende, kombination af søskende og tid
columns: omrade, alder, famtype, antsos, kombsos, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2025-01-01
</table>
<table>
id: brn9
description: Børn efter område, alder, familietype, mor status, far status og tid
columns: omrade, alder, famtyp, morstat, farstat, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2025-01-01
</table>
<table>
id: brn11
description: Børn med familieskift efter område, familieskift, familietype sidste år, familietype i år, alder og tid
columns: omrade, famskift, famtypsaa, famtypaa, alder, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2025-01-01
</table>
<table>
id: brn12
description: Børns (0-17-årige) familier efter antal børn, børnefamilietype, familietype og tid
columns: antborn, brnfam, famtyp, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2025-01-01
</table>
<table>
id: brn10
description: Børn og unge (alle 0-29-årige) 1. januar, der har mistet forældre ved dødsfald efter område, alder, mor status, far status, status på begge forældre og tid
columns: omrade, alder, morstat, farstat, forst, tid (time), indhold (unit Antal)
tid range: 2001-01-01 to 2025-01-01
</table>
<table>
id: ligefb7
description: Børn efter alder, familietype, mor status, far status og tid
columns: alder, famtyp, morstat, farstat, tid (time), indhold (unit Antal)
tid range: 1980-01-01 to 2025-01-01
</table>
<table>
id: ligefi7
description: Ligestillingsindikator for børn, der har adresse kun hos mor eller far efter indikator, alder og tid
columns: indikator, alder, tid (time), indhold (unit -)
tid range: 1980-01-01 to 2025-01-01
</table>
</fact tables>
notes:
- For children by family type with regional breakdown: fam111n (familietype) or fam133n (husstandstype), both from 1986, niveau 3 (kommune) only, ages 0–24. fam111n groups by the child's family; fam133n groups by the child's household (can span multiple families).
- For children by custody arrangement (home + samvær family): brn13 (from 2008). Unique in tracking both where the child lives and their custody/access family.
- For sibling composition: brn15 (cohabiting siblings) vs brn16 (all siblings). Both from 2008 with regional breakdown (niveau 1 and 3, plus national total code 0). kombsos uses binary positional coding.
- For children by parental status (alive/dead): brn9 (2007–, ages 0–17, region+kommune), brn10 (2001–, ages 0–29, all four nuts niveaux including landsdele, finer death-timing detail), ligefb7 (1980–, national only, has TOT rows).
- For family structure transitions: brn11 (2008–, familieskift before/after). For family counts by complexity: brn12 (2008–, national only, counts families not children).
- For gender equality indicator (% children at father vs mother address): ligefi7 (1980–, percentages only — do not sum).
- Map: All tables with omrade/omr20 support choropleth maps. fam111n and fam133n: kommune only (/geo/kommuner.parquet). brn9, brn11, brn13, brn15, brn16: kommune or region (/geo/kommuner.parquet / /geo/regioner.parquet). brn10: also landsdele (/geo/landsdele.parquet). brn12, ligefb7, ligefi7: no geographic column.
- Most brn* tables (brn9, brn10, brn11, brn13, brn15, brn16) include omrade='0' as the national total, which is not in dim.nuts. fam111n and fam133n have no national total at all (kommune level only).
- All tables covering familietype use the same codes: 0=Udeboende, 1=Begge forældre, 2=Enlig mor, 3=Mor og partner, 4=Enlig far, 5=Far og partner. None of these tables have total rows for familietype except ligefb7.
