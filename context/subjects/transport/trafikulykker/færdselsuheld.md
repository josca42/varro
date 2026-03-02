<fact tables>
<table>
id: uheld3
description: Færdselsuheld med personskade efter uheldsart, uheldssituation, by/landområde, hastighedsbegrænsning og tid
columns: uhelda, uheldsit, byland, hast, tid (time), indhold (unit Antal)
tid range: 1997-01-01 to 2024-01-01
</table>
<table>
id: uheld4
description: Færdselsuheld med personskade efter uheldsart, transportmiddel, klokkeslet, ugedag, måned og tid
columns: uhelda, transmid, klok, uge, mnd, tid (time), indhold (unit Antal)
tid range: 1997-01-01 to 2024-01-01
</table>
<table>
id: uheld5
description: Færdselsuheld med personskade efter uheldsart, uheldssituation, transportmiddel, modpart og tid
columns: uhelda, uheldsit, transmid, modpart, tid (time), indhold (unit Antal)
tid range: 2001-01-01 to 2024-01-01
</table>
<table>
id: uheld6
description: Færdselsuheld med personskade efter uheldsart, uheldssituation, transportmiddel, antal transportmidler involveret og tid
columns: uhelda, uheldsit, transmid, transinv, tid (time), indhold (unit Antal)
tid range: 2001-01-01 to 2024-01-01
</table>
<table>
id: uheldk7
description: Færdselsuheld med personskade efter uheldsart, område, by/landområde, uheldssituation og tid
columns: uhelda, omrade, byland, uheldsit, tid (time), indhold (unit Antal)
tid range: 1998-01-01 to 2024-01-01
</table>
<table>
id: uheld8
description: Tilskadekomne og dræbte i færdselsuheld efter uheldsart, personskade, transportmiddel, køn, alder, skadens type og tid
columns: uhelda, uheld, transmid, koen, alder, skade, tid (time), indhold (unit Antal)
tid range: 2001-01-01 to 2024-01-01
</table>
<table>
id: uheld9
description: Tilskadekomne og dræbte i færdselsuheld efter uheldsart, personskade, transportmiddel, personart, by/landområde, gade- eller vejtype og tid
columns: uhelda, uheld, transmid, persart, byland, gadevej, tid (time), indhold (unit Antal)
tid range: 2001-01-01 to 2024-01-01
</table>
<table>
id: uheld10
description: Tilskadekomne og dræbte i færdselsuheld efter uheldsart, uheldssituation, personskade, transportmiddel, modpart og tid
columns: uhelda, uheldsit, uheld, transmid, modpart, tid (time), indhold (unit Antal)
tid range: 2001-01-01 to 2024-01-01
</table>
<table>
id: uheld11
description: Tilskadekomne og dræbte i færdselsuheld efter uheldsart, personskade, transportmiddel, i/udenfor transportmidlet, personart, spirituspåvirkning og tid
columns: uhelda, uheld, transmid, iudenfor, persart, spirit, tid (time), indhold (unit Antal)
tid range: 2001-01-01 to 2024-01-01
</table>
<table>
id: uheldk1
description: Tilskadekomne og dræbte i færdselsuheld efter område, personskade, indblandede transportmidler, alder, køn og tid
columns: omrade, uheld, indbland, alder, kon, tid (time), indhold (unit Antal)
tid range: 1998-01-01 to 2024-01-01
</table>
<table>
id: uheldk2
description: Tilskadekomne og dræbte i spiritusuheld efter område, personskade, alder, køn og tid
columns: omrade, uheld, alder, koen, tid (time), indhold (unit Antal)
tid range: 1998-01-01 to 2024-01-01
</table>
<table>
id: uheld12
description: Førere og fodgængere efter transportmiddel, køn, alder, kørekortets alder, alkoholpromille og tid
columns: transmid, koen, alder, kalder, alco, tid (time), indhold (unit Antal)
tid range: 2001-01-01 to 2024-01-01
</table>
<table>
id: moerke
description: Personskader i færdselsuheld indberettet af politi, sygehusenes akutmodtagelse og sygehuse efter indberetter, uheldssituation, transportmiddel, køn, alder, skadens type og tid
columns: indberet, uheldsit, transmid, koen, alder, skade, tid (time), indhold (unit Antal)
tid range: 2001-01-01 to 2023-01-01
</table>
<table>
id: moerke1
description: Personskader i færdselsuheld indberettet af sygehusenes akutmodtagelse og sygehuse efter indberetter, uheldssituation, transportmiddel, køn, alder, personskade (klassificeret efter diagnose) og tid
columns: indberet, uheldsit, transmid, koen, alder, skadediag, tid (time), indhold (unit Antal)
tid range: 2009-01-01 to 2023-01-01
</table>
<table>
id: ligehi10
description: Ligestillingsindikator for tilskadekomne og dræbte i færdselsuheld efter indikator, personskade, indblandede transportmidler, alder og tid
columns: indikator, uheld, indbland, alder, tid (time), indhold (unit -)
tid range: 1998-01-01 to 2024-01-01
</table>
</fact tables>
notes:
- Two data types: accident counts (uheld3/4/5/6/k7) vs person counts (uheld8/9/10/11/k1/k2, moerke/moerke1). Choose based on whether the question is about accidents or about injured/killed persons.
- Regional breakdown: uheldk7 (accidents) and uheldk1 (persons) have kommuner (niveau 3). uheldk2 (alcohol only) has only landsdele (niveau 2). Tables without 'k' in the name have no regional dimension.
- For historical series: uheld3/4 start 1997, the k-tables start 1998, and uheld5/6/8–12/moerke start 2001. moerke/moerke1 end at 2023; all police-based tables go to 2024.
- For dark number / hospital-reported injuries (including unreported accidents): use moerke (2001–2023) or moerke1 (2009–2023, diagnosis-classified). Police-based tables (uheld8–11) undercount because they only include accidents reported to police.
- For gender equality indicators (rates per 100,000): use ligehi10. It is the only table with rate values — do not sum its indhold.
- uhelda column: ALL tables except uheld12, moerke, moerke1, and ligehi10 have uhelda where 0=Alle uheld is the aggregate of Spiritusuheld+Øvrige uheld. Always filter to one value.
- uheldsit=0 means different things: in uheld3/5/6/k7/uheld10 it means Eneuheld (single-vehicle accident, NOT a total); in moerke/moerke1 it means Uheldssituation i alt (total). Completely different coding schemes.
- transmid=0 means "I alt" (total) in all tables that have it — always filter when breaking down by vehicle type.
- alder codes '0006' and '0714' are shown with leading zeros in ColumnValues but stored as '6' and '714' in the database. Use the numeric form in SQL.
- Map: uheldk7 (accidents) and uheldk1 (persons) support kommuner/regioner choropleths (niveau 3/1). uheldk2 (alcohol injuries) supports landsdele/regioner (niveau 2/1). All use omrade=dim_kode; exclude omrade=0.
