<fact tables>
<table>
id: auks02
description: Offentligt forsørgede (fuldtidsmodtagere, sæsonkorrigeret) efter ydelsestype, køn, alder og tid
columns: ydelsestype, kon, alder, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2025-04-01
</table>
<table>
id: auks01
description: Offentligt forsørgede (fuldtidsmodtagere, sæsonkorrigeret) efter ydelsestype og tid
columns: ydelsestype, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2025-04-01
</table>
<table>
id: auk01
description: Offentligt forsørgede (fuldtidsmodtagere) efter område, ydelsestype, køn, alder og tid
columns: omrade, ydelsestype, kon, alder, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2025-04-01
</table>
<table>
id: auk02
description: Offentligt forsørgede (fuldtidsmodtagere) efter type, ydelsestype, alder, køn og tid
columns: type, ydelsestype, alder, kon, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2025-04-01
</table>
<table>
id: auk03
description: Offentligt forsørgede (aktiverede fuldtidsmodtagere) efter område, ydelsestype, køn, alder og tid
columns: omrade, ydelsestype, kon, alder, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2025-04-01
</table>
<table>
id: auk04
description: Offentligt forsørgede (fuldtidsmodtagere) efter område, ydelsestype, oprindelsesland, køn og tid
columns: omrade, ydelsestype, ieland, kon, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2025-04-01
</table>
<table>
id: auk05
description: Offentligt forsørgede (støttet beskæftigelse, fuldtidsmodtagere) efter ydelsestype, sektor, køn, alder og tid
columns: ydelsestype, sektor, kon, alder, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2025-04-01
</table>
<table>
id: auh01
description: Offentligt forsørgede (fuldtidsmodtagere) efter område, ydelsestype, køn, alder og tid
columns: omrade, ydelsestype, kon, alder, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: auh02
description: Offentligt forsørgede (fuldtidsmodtagere) efter type, ydelsestype, alder, køn og tid
columns: type, ydelsestype, alder, kon, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: auh03
description: Offentligt forsørgede (aktiverede fuldtidsmodtagere) efter område, ydelsestype, køn, alder og tid
columns: omrade, ydelsestype, kon, alder, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: auh04
description: Offentligt forsørgede (fuldtidsmodtagere) efter område, ydelsestype, oprindelsesland, køn og tid
columns: omrade, ydelsestype, ieland, kon, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: auh05
description: Offentligt forsørgede (støttet beskæftigelse, fuldtidsmodtagere) efter ydelsestype, sektor, køn, alder og tid
columns: ydelsestype, sektor, kon, alder, tid (time), indhold (unit Antal)
tid range: 2008-01-01 to 2024-01-01
</table>
<table>
id: ligeib5
description: Offentligt forsørgede efter køn, alder, ydelsestype, herkomst og tid
columns: kon, alder, ydelsestype, herkomst, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: ligeib6
description: Offentligt forsørgede efter køn, alder, ydelsestype, familietype og tid
columns: kon, alder, ydelsestype, famtyp, tid (time), indhold (unit Antal)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: ligeii5
description: Ligestillingsindikator for offentligt forsørgede efter indikator, alder, ydelsestype, herkomst og tid
columns: indikator, alder, ydelsestype, herkomst, tid (time), indhold (unit -)
tid range: 2007-01-01 to 2024-01-01
</table>
<table>
id: ligeii6
description: Ligestillingsindikator for offentligt forsørgede efter indikator, alder, ydelsestype, familietype og tid
columns: indikator, alder, ydelsestype, famtyp, tid (time), indhold (unit Pr. 100.000 personer)
tid range: 2007-01-01 to 2024-01-01
</table>
</fact tables>
notes:
- Naming convention: `auk` = quarterly (kvartal, Jan/Apr/Jul/Oct), `auh` = annual (helår, Jan only), `auks` = quarterly seasonally adjusted (sæsonkorrigeret). For each question, prefer the right time granularity. auk/auks tables are more current (to 2025-04-01); auh tables only to 2024-01-01.
- For trend analysis (avoiding seasonal noise): use auks01 (ydelsestype × tid only) or auks02 (adds kon, alder, but only 3 ydelsestype values: TOT/TOTUSU/SU).
- For regional breakdown by benefit type: auk01/auh01 (the richest table — omrade at 3 NUTS levels, 41 ydelsestype codes, kon, alder). Quarterly in auk01, annual in auh01.
- For count vs full-time equivalent comparison: auk02/auh02 — these are the only tables with a `type` column (FTM=fuldtidsmodtagere, DEL=headcount). Always filter to one type — every row is duplicated.
- For activated recipients only: auk03/auh03 (same structure as auk01/auh01 but only activation ydelsestype codes). Use these when the question is specifically about activation measures (virksomhedspraktik, løntilskud, nytteindsats, etc.).
- For origin (herkomst/land) breakdown: auk04/auh04 — regional detail at landsdele level only (niveau 2), no age breakdown. ieland has hierarchical aggregate codes (TOT, UDL, vestlige/ikke-vestlige) and individual country codes — never sum across hierarchy levels.
- For supported employment detail (fleksjob, løntilskud, skånejob) by sector: auk05/auh05. Sector breakdown not available in other tables. Starts 2008.
- For gender equality indicators (rates per 100.000) with origin: ligeii5. For same with family type: ligeii6. For raw counts: ligeib5 (origin) and ligeib6 (family type).
- ligeib5/ligeib6/ligeii5/ligeii6 are annual, use broad age groups (16-29, 30-49, 50+), and only 9 ydelsestype group codes (no leaf benefit codes).
- All tables share the same overcounting risk: ydelsestype, kon, alder, omrade, and ieland/herkomst all include aggregate total rows. Always filter non-target dimensions to their total code (TOT/IALT/0) to avoid inflated sums.
- omrade='0' = Hele landet (national total, not in dim.nuts), omrade='997' = Uoplyst (in auk01/03/auh01/03 only). Use these codes directly for national aggregates rather than joining dim.nuts.
- Map: auk01/auk03/auh01/auh03 support choropleth at alle 3 NUTS niveauer (kommuner, landsdele, regioner) via /geo/. auk04/auh04 support landsdele only. Merge on omrade=dim_kode; exclude omrade IN (0, 997).
