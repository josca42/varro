<fact tables>
<table>
id: ifor32
description: Gennemsnitlig ækvivalret disponibel indkomst efter decil gennemsnit, kommune og tid
columns: decilgen, kommunedk, tid (time), indhold (unit Gns.)
tid range: 1987-01-01 to 2023-01-01
</table>
<table>
id: ifor35
description: Gennemsnitlig ækvivalret disponibel indkomst efter decil gennemsnit, kommune, prisenhed og tid
columns: decilgen, kommunedk, prisenhed, tid (time), indhold (unit Gns.)
tid range: 1987-01-01 to 2023-01-01
</table>
<table>
id: ifor12p
description: Personer i Lavindkomst familier efter kommune, indkomstniveau og tid
columns: kommunedk, indkn, tid (time), indhold (unit Pct.)
tid range: 2000-01-01 to 2023-01-01
</table>
<table>
id: ifor10
description: Lavindkomst grænse.  Månedlige disponible indkomst efter voksne 15 år og derover, børn under 15 år, indkomstniveau og tid
columns: voksne, boern, indkn, tid (time), indhold (unit Kr. pr. familie)
tid range: 1987-01-01 to 2023-01-01
</table>
<table>
id: ifor12a
description: Personer i Lavindkomst familier efter kommune, indkomstniveau og tid
columns: kommunedk, indkn, tid (time), indhold (unit Antal)
tid range: 2000-01-01 to 2023-01-01
</table>
<table>
id: ifor11p
description: Lavindkomst familier efter indkomstniveau, socioøkonomisk status og tid
columns: indkn, socio, tid (time), indhold (unit Pct.)
tid range: 2000-01-01 to 2023-01-01
</table>
<table>
id: ifor11a
description: Personer i Lavindkomst familier efter indkomstniveau, socioøkonomisk status og tid
columns: indkn, socio, tid (time), indhold (unit Antal)
tid range: 2000-01-01 to 2023-01-01
</table>
<table>
id: laby07
description: Relativ fattigdom (andel af befolkningen) efter kommunegruppe, alder og tid
columns: komgrp, alder, tid (time), indhold (unit Pct.)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: ifor51
description: Relativ fattigdom efter alder, enhed, varighed og tid
columns: alder, enhed, kmdr, tid (time), indhold (unit -)
tid range: 2015-01-01 to 2023-01-01
</table>
<table>
id: ifor33
description: Indkomstdecilers sammensætning efter indkomstdecil, socioøkonomisk status, enhed og tid
columns: inddecil, socio, enhed, tid (time), indhold (unit -)
tid range: 2000-01-01 to 2023-01-01
</table>
<table>
id: laby06
description: Gennemsnitlig disponibel indkomst efter kommunegruppe, alder og tid
columns: komgrp, alder, tid (time), indhold (unit Kr.)
tid range: 2004-01-01 to 2023-01-01
</table>
<table>
id: ifor31
description: Gennemsnitlig ækvivalleret disponibel indkomst efter decil gennemsnit, socioøkonomisk status og tid
columns: decilgen, socio, tid (time), indhold (unit Kr.)
tid range: 2000-01-01 to 2023-01-01
</table>
<table>
id: ifor30
description: Gennemsnitlig ækvivalleret disponibel indkomst efter decil gennemsnit, socioøkonomisk status, prisenhed og tid
columns: decilgen, socio, prisenhed, tid (time), indhold (unit Kr.)
tid range: 2000-01-01 to 2023-01-01
</table>
<table>
id: ifor34
description: Indkomstdecilers sammensætning efter indkomstdecil, alder, enhed og tid
columns: inddecil, alder, enhed, tid (time), indhold (unit -)
tid range: 2000-01-01 to 2023-01-01
</table>
<table>
id: ifor41
description: Ulighedsmål målt på ækvivaleret disponibel indkomst efter ulighedsmål, kommune og tid
columns: ullig, kommunedk, tid (time), indhold (unit -)
tid range: 1987-01-01 to 2023-01-01
</table>
<table>
id: ifor22
description: Decilgrænser på ækvivaleret disponibel indkomst efter decilgrænse, kommune og tid
columns: decilgr, kommunedk, tid (time), indhold (unit Kr.)
tid range: 1987-01-01 to 2023-01-01
</table>
<table>
id: ifor25
description: Decilgrænser på ækvivaleret disponibel indkomst efter decilgrænse, kommune, prisenhed og tid
columns: decilgr, kommunedk, prisenhed, tid (time), indhold (unit Kr.)
tid range: 1987-01-01 to 2023-01-01
</table>
<table>
id: ifor21
description: Decilgrænser på ækvivaleret disponibel indkomst efter decilgrænse, socioøkonomisk status og tid
columns: decilgr, socio, tid (time), indhold (unit Kr.)
tid range: 2000-01-01 to 2023-01-01
</table>
<table>
id: ifor20
description: Decilgrænser på ækvivaleret disponibel indkomst efter decilgrænse, socioøkonomisk status, prisenhed og tid
columns: decilgr, socio, prisenhed, tid (time), indhold (unit Kr.)
tid range: 2000-01-01 to 2023-01-01
</table>
</fact tables>
notes:
- Table naming convention: tables with a "p" suffix (ifor11p, ifor12p) contain percentages (Pct.); tables with an "a" suffix (ifor11a, ifor12a) contain absolute counts (Antal). When both exist, decide based on whether the question is relative or absolute.
- The "5/6" suffix pattern (ifor35 vs ifor32, ifor25 vs ifor22, ifor20 vs ifor21, ifor30 vs ifor31): tables ending in 5/0 add a prisenhed selector (faste priser vs nominelle priser) to the corresponding "2/1" table. Use the "5/0" variant for time series analysis (filter prisenhed='5' for inflation-adjusted), the "2/1" variant for simplicity.
- For inequality indices (Gini, S80/20, P90/10) at kommune level: use ifor41. This is the only pre-computed inequality table.
- For income distribution by decil at kommune level: ifor32/ifor35 (decil averages) or ifor22/ifor25 (decil boundaries). Decil averages (ifor32) answer "how much does the average person in each decil earn?"; decil boundaries (ifor22) answer "what income threshold separates decil N from N+1?"
- For poverty (lavindkomst, <50% or <60% of median income): ifor10 (poverty thresholds in Kr. by family size), ifor12a/ifor12p (poverty counts/shares by kommune), ifor11a/ifor11p (poverty counts/shares by socioøkonomisk status).
- For relative poverty with duration (persistent poverty): ifor51 only — has kmdr column for 1/2/3/4 consecutive years in poverty. National level only.
- For relative poverty with kommunegruppe breakdown: laby07 (poverty shares, from 2015) or laby06 (average income by kommunegruppe, from 2004). Kommunegrupper = 5 types (Hovedstadskommuner, Storbykommuner, Provinsbykommuner, Oplandskommuner, Landkommuner).
- For income distribution by socioøkonomisk status: ifor31/ifor30 (decil averages) or ifor21/ifor20 (decil boundaries). ifor33 shows the socio composition within each decil; ifor34 shows the age composition within each decil.
- Shared pitfall — measurement selectors: indkn (50%/60% poverty threshold) appears in ifor10/11a/11p/12a/12p; prisenhed (faste/nominelle) in ifor20/21/25/30/35; enhed (ANT/PCT) in ifor33/34/51. Always filter to one value or you double/triple all counts.
- Shared pitfall — kommunedk aggregate: code 0 = Danmark i alt, not in dim.nuts. Use WHERE kommunedk = 0 for national totals, kommunedk != 0 for individual kommuner.
- Shared pitfall — socio aggregates: codes 100 (total) and 130 (Lønmodtagere i alt) are NOT in dim.socio. Use JOIN dim.socio d ON f.socio = d.kode WHERE d.niveau = 3 to get only the 15 detailed socio categories.
- Time coverage varies significantly: ifor32/ifor22/ifor41 back to 1987; ifor11a/11p/12a/12p/ifor33/34/31/30/21/20 from 2000; laby07/ifor51 from 2015 only.
- Map: ifor32, ifor35, ifor22, ifor25, ifor41, ifor12a, ifor12p all have kommunedk at niveau 3 — use /geo/kommuner.parquet for choropleth maps (merge on kommunedk=dim_kode, exclude kommunedk=0). Remaining tables (ifor10/11a/11p/31/30/33/34/51, laby06/07) have no geographic column.
