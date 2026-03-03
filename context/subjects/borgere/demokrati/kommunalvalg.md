<fact tables>
<table>
id: kvpct
description: Valg til kommunalbestyrelser efter valgresultat og tid
columns: valres, tid (time), indhold (unit Pct.)
tid range: 1970-01-01 to 2021-01-01
</table>
<table>
id: kvbpct
description: Valg til kommunalbestyrelser efter valgresultat og tid
columns: valres, tid (time), indhold (unit Antal)
tid range: 1970-01-01 to 2021-01-01
</table>
<table>
id: kvres
description: Valg til kommunalbestyrelser efter område, valgresultat og tid
columns: omrade, valres, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2021-01-01
</table>
<table>
id: laby08
description: Valg til kommunalbestyrelser efter kommunegruppe, valgresultat og tid
columns: komgrp, valres, tid (time), indhold (unit Pct.)
tid range: 2005-01-01 to 2021-01-01
</table>
<table>
id: valgk3
description: Valg til kommunalbestyrelser efter område, parti, stemmer/kandidater/køn og tid
columns: omrade, parti, stemmer, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2021-01-01
</table>
<table>
id: akva3
description: Valg til regionsråd efter område, parti, stemmer/kandidater/køn og tid
columns: omrade, parti, stemmer, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2021-01-01
</table>
<table>
id: kv21pers
description: Valgte kandidaters personlige stemmer ved kommunalvalget i 2021 efter kandidater, stemmetype og tid
columns: kandidat, stemmetype, tid (time), indhold (unit -)
tid range: 2021-01-01 to 2021-01-01
</table>
<table>
id: kv17pers
description: Valgte kandidaters personlige stemmer ved kommunalvalget i 2017 efter kandidater, stemmetype og tid
columns: kandidat, stemmetype, tid (time), indhold (unit -)
tid range: 2017-01-01 to 2017-01-01
</table>
<table>
id: kv13pers
description: Valgte kandidaters personlige stemmer ved kommunalvalget i 2013 efter kandidater, stemmetype og tid
columns: kandidat, stemmetype, tid (time), indhold (unit -)
tid range: 2013-01-01 to 2013-01-01
</table>
<table>
id: kv09pers
description: Valgte kandidaters personlige stemmer ved kommunalvalget i 2009 efter kandidater, stemmetype og tid
columns: kandidat, stemmetype, tid (time), indhold (unit -)
tid range: 2009-01-01 to 2009-01-01
</table>
<table>
id: kv05pers
description: Valgte kandidaters personlige stemmer ved kommunalvalget i 2005 efter kandidater, stemmetype og tid
columns: kandidat, stemmetype, tid (time), indhold (unit -)
tid range: 2005-01-01 to 2005-01-01
</table>
<table>
id: kv01pers
description: Valgte kandidaters personlige stemmer ved kommunalvalget i 2001 efter kandidater, stemmetype og tid
columns: kandidat, stemmetype, tid (time), indhold (unit -)
tid range: 2001-01-01 to 2001-01-01
</table>
<table>
id: kv97pers
description: Valgte kandidaters personlige stemmer ved kommunalvalget i 1997 efter kandidater, stemmetype og tid
columns: kandidat, stemmetype, tid (time), indhold (unit -)
tid range: 1997-01-01 to 1997-01-01
</table>
<table>
id: ligedb2
description: Opstillede og valgte kandidater til kommunalvalg efter kandidater, køn, alder, kommune og tid
columns: kandidat, kon, alder, komk, tid (time), indhold (unit Antal)
tid range: 2005-01-01 to 2021-01-01
</table>
<table>
id: ligedi2
description: Ligestillingsindikator for opstillede og valgte kandidater til kommunalvalg efter kandidater, indikator, alder, kommune og tid
columns: kandidat, indikator, alder, komk, tid (time), indhold (unit -)
tid range: 2005-01-01 to 2021-01-01
</table>
<table>
id: ligedi3
description: Ligestillingsindikator for opstillede og valgte kandidater til regionalvalg efter kandidater, indikator og tid
columns: kandidat, indikator, tid (time), indhold (unit -)
tid range: 2005-01-01 to 2021-01-01
</table>
</fact tables>

notes:
- **National totals only (since 1970):** kvpct (turnout %, invalid %) and kvbpct (voter counts). Simple 2–3 row tables per election year; go here first for headline figures.
- **Regional/municipal breakdown:** kvres (counts by region/kommune + party breakdown, 2005–2021), laby08 (% rates by kommunegruppe type, 2005–2021). kvres is the richest single table — it has both geographic and party-level vote counts at region and kommune granularity.
- **Party + gender + candidates:** valgk3 (kommunalbestyrelser) and akva3 (regionsråd). Both share an identical structure with the stemmer column as a measurement selector (votes / personal votes / candidates / elected by gender). Always filter stemmer to one value or counts inflate 6x. akva3 is region-level only; valgk3 goes down to kommune.
- **Individual elected candidates:** kv97pers through kv21pers — one table per election year, personal vote counts for every elected candidate. stemmetype is a measurement selector; filter to PERS for vote counts. Candidate labels encode party and municipality. kv01/kv97 have ~4600 candidates (pre-2007 kommunalreform with many more municipalities).
- **Gender equality indicators (kommunalvalg):** ligedb2 (raw counts: nominated/elected × gender × age × municipality) and ligedi2 (derived indicators: % men, % women, gender gap pp). For ready-to-use percentages use ligedi2; for custom aggregation use ligedb2.
- **Gender equality indicators (regionalvalg):** ligedi3 — same indicators as ligedi2 but for regionsråd, national level only.
- **Common gotcha:** every table with omrade/komk/komgrp joined to a dim includes code '0' (national aggregate) which is not in the dim table. JOIN to dim naturally excludes it; or filter WHERE column != '0' explicitly.
- **Measurement selector columns** are the main overcounting risk across this subject. stemmer (valgk3/akva3), stemmetype (kv*pers), valres (kvpct/kvbpct/kvres/laby08), and indikator (ligedi2/ligedi3) all cause every row to repeat multiple times — always filter to one value before summing indhold.
- **Map support:** kvres and valgk3 support choropleth at kommune (niveau 3) or region (niveau 1) via /geo/kommuner.parquet / /geo/regioner.parquet (merge on omrade=dim_kode). akva3 is region-level only. ligedb2 and ligedi2 support kommune, landsdel, and region via /geo/kommuner.parquet / /geo/landsdele.parquet / /geo/regioner.parquet (merge on komk=dim_kode). Exclude code 0 in all cases.