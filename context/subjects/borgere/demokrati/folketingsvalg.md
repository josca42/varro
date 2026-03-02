<fact tables>
<table>
id: fvpct
description: Folketingsvalg efter valgresultat og tid
columns: valres, tid (time), indhold (unit Pct.)
tid range: 1971-01-01 to 2022-01-01
</table>
<table>
id: laby09
description: Folketingsvalg efter kommunegruppe, valgresultat og tid
columns: komgrp, valres, tid (time), indhold (unit Pct.)
tid range: 2007-01-01 to 2022-01-01
</table>
<table>
id: fvbpct
description: Folketingsvalg efter valgresultat og tid
columns: valres, tid (time), indhold (unit Antal)
tid range: 1971-01-01 to 2022-01-01
</table>
<table>
id: fvkand
description: Opstillede og valgte kandidater efter kandidater, parti og tid
columns: kandidat, parti, tid (time), indhold (unit Antal)
tid range: 1990-01-01 to 2022-01-01
</table>
<table>
id: fvkom
description: Folketingsvalg efter valgresultat, område og tid
columns: valres, omrade, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2022-01-01
</table>
<table>
id: fvpandel
description: Partiernes stemmeandel (Folketingsvalg) efter valgresultat, område og tid
columns: valres, omrade, tid (time), indhold (unit Pct.)
tid range: 2007-01-01 to 2022-01-01
</table>
<table>
id: fv22tot
description: Folketingsvalget 2022 efter valgresultat, område og tid
columns: valres, omrade, tid (time), indhold (unit Antal)
tid range: 2022-01-01 to 2022-01-01
</table>
<table>
id: fv22tota
description: Folketingsvalget 2022 efter valgresultat, område og tid
columns: valres, omrade, tid (time), indhold (unit Antal)
tid range: 2022-01-01 to 2022-01-01
</table>
<table>
id: fv22kand
description: Opstillede kandidaters personlige stemmer efter opstillede kandidater, valgresultat, parti, område og tid
columns: opkandidat, valres, parti, omrade, tid (time), indhold (unit Antal)
tid range: 2022-01-01 to 2022-01-01
</table>
<table>
id: ligedb1
description: Opstillede og valgte kandidater til folketingsvalg efter kandidater, køn, alder og tid
columns: kandidat, kon, alder, tid (time), indhold (unit Antal)
tid range: 2001-01-01 to 2022-01-01
</table>
<table>
id: ligedi0
description: Ligestillingsindikator for opstillede og valgte kandidater til folketingsvalg efter kandidater, indikator og tid
columns: kandidat, indikator, tid (time), indhold (unit -)
tid range: 1918-01-01 to 2022-01-01
</table>
<table>
id: ligedi1
description: Ligestillingsindikator for opstillede og valgte kandidater til folketingsvalg efter kandidater, indikator, alder og tid
columns: kandidat, indikator, alder, tid (time), indhold (unit -)
tid range: 2001-01-01 to 2022-01-01
</table>
<table>
id: ligedi10
description: Ligestillingsindikator for regeringer efter regeringer, indikator og tid
columns: regering, indikator, tid (time), indhold (unit -)
tid range: 2022-01-01 to 2022-01-01
</table>
</fact tables>

notes:
- For national turnout/percentages (1971–2022): fvpct (stemmeprocent, ugyldighedsprocent, brevstemmeprocent). For national absolute counts: fvbpct (vælgere, gyldige/ugyldige stemmer). Both go back to 1971.
- For municipality-level vote counts (2007–2022): fvkom (99 kommuner via dim.nuts niveau 3). For municipality-level party shares as percentages: fvpandel (same geography, same period).
- For kommunegruppe breakdown (2007–2022): laby09 (5 kommunegrupper or 98 kommuner; also has BLANKPCT and PERSPCT not in fvpct).
- For 2022 in detail: fv22tot has 4 levels of area breakdown (Hele landet, 3 valglandsdele, 10 storkredse, 92 afstemningskredse). fv22tota adds individual polling stations (1453 omrade codes). fv22kand has personal votes per candidate by storkreds.
- For gender of candidates (2001–2022): ligedb1 (counts by kon + alder), ligedi1 (pct indicators by alder). For longer series without age: ligedi0 goes back to 1918. For cabinet gender composition: ligedi10 covers all 59 governments since 1901 (one tid value = 2022 release date).
- All tables with multiple categories (valres, indikator, kon, alder) include totals. Never sum without filtering — overcounting is the main risk across this subject.
- Map support: fvkom and fvpandel → context/geo/kommuner.parquet (merge on omrade=dim_kode). fv22tot and fv22tota → context/geo/storkredse.parquet (omrade 10–19, subtract 9) or context/geo/valgkredse.parquet (omrade 20–111, subtract 19). fv22kand → context/geo/storkredse.parquet (subtract 9).
- Party codes are numeric DST IDs (e.g. 5891=A. Socialdemokratiet) consistently across fvkand, fvkom, fvpandel, fv22tot, fv22tota, fv22kand. Use ColumnValues on any of those tables to get the party list.