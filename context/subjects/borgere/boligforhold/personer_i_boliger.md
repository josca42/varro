<fact tables>
<table>
id: bol201
description: Personer i boliger efter område, anvendelse, udlejningsforhold, ejerforhold, opførelsesår, alder, køn og tid
columns: amt, anvendelse, udlforh, ejer, opforelsesar, alder1, koen, tid (time), indhold (unit Antal)
tid range: 2010-01-01 to 2025-01-01
</table>
<table>
id: bol202
description: Personer efter område, anvendelse, opvarmning, toiletforhold, badeforhold, køkkenforhold, alder, køn og tid
columns: amt, anvendelse, opvarmning, toilet, bad, koekken, alder1, kon, tid (time), indhold (unit Antal)
tid range: 2010-01-01 to 2025-01-01
</table>
<table>
id: bol203
description: Personer efter område, anvendelse, udlejningsforhold, antal værelser, husstandsstørrelse, antal børn, alder, køn og tid
columns: amt, anvendelse, udlforh, antvaer, husstor, antborn, alder, kon, tid (time), indhold (unit Antal)
tid range: 2010-01-01 to 2025-01-01
</table>
<table>
id: bol204
description: Personer efter område, anvendelse, udlejningsforhold, husstandstype, antal børn, alder, køn og tid
columns: amt, anvendelse, udlforh, hustyp, antborn, alder1, kon, tid (time), indhold (unit Antal)
tid range: 2010-01-01 to 2025-01-01
</table>
<table>
id: laby45
description: Andel af befolkningen, der bor til leje efter kommunegruppe og tid
columns: komgrp, tid (time), indhold (unit Pct.)
tid range: 2010-01-01 to 2025-01-01
</table>
<table>
id: laby46
description: Gennemsnitlig boligareal pr. person efter kommunegruppe og tid
columns: komgrp, tid (time), indhold (unit M2)
tid range: 2010-01-01 to 2025-01-01
</table>
</fact tables>

notes:
- bol201–bol204 all share the same geography column (amt) with 4 mixed levels: 0=Hele landet, 81-85=5 Regioner, 1-11=11 Landsdele, 101-851=98 Kommuner. Always filter to one level to avoid overcounting. No dim join needed.
- None of the bol20x tables have total/IALT rows in any column — all values are categories. To get a total, SUM across all values of the columns you're not interested in.
- Choose table by topic: bol201=ejerforhold+opførelsesår, bol202=boligkvalitet (toilet/bad/køkken/opvarmning), bol203=antal værelser+husstandsstørrelse+antal børn, bol204=husstandstype (enlig/par/familie).
- laby45 (pct. lejer) and laby46 (m2 pr. person) are summary tables by kommunegruppe only — no regional/kommune breakdown, no person characteristics. Use them for quick national/kommunegruppe comparisons, not for detailed analysis.
- komgrp=0 in laby45/laby46 is "Hele landet" and is not in dim.kommunegrupper — skip it when joining the dim, or use it directly for the national figure.
- laby45/laby46 values are rates/averages — never SUM them across kommunegrupper.
- Map: bol201–bol204 support choropleth at kommune (amt 101–851), landsdel (amt 1–11), or region (amt 81–85) level — filter amt to one level and merge on amt=dim_kode using the corresponding geo file (kommuner/landsdele/regioner.parquet). laby45/laby46 have no geo support.