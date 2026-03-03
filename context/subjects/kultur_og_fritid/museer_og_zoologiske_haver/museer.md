<fact tables>
<table>
id: mus1
description: Aktivitet på danske museer efter museumskategori, museumstype, aktivitet og tid
columns: museer, afdling, aktivitet, tid (time), indhold (unit Antal)
tid range: 2009-01-01 to 2024-01-01
</table>
<table>
id: mus3
description: Aktivitet på danske museers besøgssteder efter område, museumskategori, museumstype, aktivitet og tid
columns: omrade, museer, afdling, aktivi, tid (time), indhold (unit Antal)
tid range: 2016-01-01 to 2024-01-01
</table>
<table>
id: mus5
description: Aktivitet uden for museets adresse efter museumskategori, museumstype, aktivitet og tid
columns: museer, afdling, aktivitet, tid (time), indhold (unit Antal)
tid range: 2022-01-01 to 2024-01-01
</table>
<table>
id: mus4
description: Besøg på museets udstilling efter museumskategori, museumstype, besøgstype og tid
columns: museer, afdling, besogstype, tid (time), indhold (unit Antal)
tid range: 2022-01-01 to 2024-01-01
</table>
<table>
id: kv2mus1
description: Besøg på museum efter museumskategori, køn, alder og tid
columns: museer, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2mus2
description: Besøg på museum efter museets placering, køn, alder og tid
columns: musplacering, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2mus3
description: Besøg på museum efter ledsager, køn, alder og tid
columns: ledsag, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2mus4
description: Brug af museers digitale tjenester efter tjeneste, køn, alder og tid
columns: tjen, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2mus5
description: Barrierer for museumsbesøg efter årsag, køn og tid
columns: aarsag, kon, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2bk1
description: Forbrug af billedkunst efter udstillingssted, køn, alder og tid
columns: udstil, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2bk2
description: Forbrug af billedkunst efter kunsttype, køn, alder og tid
columns: kunsttype, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2bk3
description: Forbrug af billedkunst efter billedkunstens placering, køn, alder og tid
columns: bilkunstplacering, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2bk4
description: Selvudøvelse af billedkunst efter udøvelsessted, køn, alder og tid
columns: udoested, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2bk5
description: Barrierer for forbrug af billedkunst efter årsag, køn og tid
columns: aarsag, kon, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- Two families of tables: administrative activity data (mus1/mus3/mus4/mus5, counts) and KV2 survey data (kv2mus1-5, kv2bk1-5, percentages from 2024 only).
- For time series on museum visits: use mus1 (2009-2024, national). For regional breakdown: mus3 (2016-2024, by region/landsdel). For visit-type detail (payment type, children vs. adults): mus4 (2022-2024). For off-site and online activities: mus5 (2022-2024).
- All mus1/mus3/mus4/mus5 share museer (TOT5=total) and afdling (TOT=total) — always filter both to avoid overcounting. Their aktivitet/aktivi/besogstype columns are measurement selectors, not additive.
- kv2mus1-5 cover museum-going behavior (which museum types, where, with whom, digital use, barriers). kv2bk1-5 cover visual art consumption (venue, art type, location, self-creation, barriers). All 2024 survey, single year only.
- All kv2 percentage tables: every category column (museer, ledsag, tjen, aarsag, udstil, kunsttype etc.) contains independent options — sums exceed 100%. Never aggregate across these columns.
- kv2mus5 and kv2bk5 share identical aarsag codes, enabling direct comparison of barriers to museum-going vs. visual art consumption.
- For kon totals in kv2 tables: kon=10. For alder totals: alder='TOT'. kv2mus5 and kv2bk5 have no alder column.
- Map: mus3 supports choropleth maps at region (niveau 1) and landsdel (niveau 2) via /geo/regioner.parquet and /geo/landsdele.parquet — merge on omrade=dim_kode, exclude omrade=0.