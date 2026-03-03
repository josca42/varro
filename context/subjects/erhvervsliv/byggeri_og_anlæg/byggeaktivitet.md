<fact tables>
<table>
id: bygv11
description: Den samlede byggeaktivitet (ikke korrigeret for forsinkelser) efter område, byggefase, anvendelse, bygherreforhold og tid
columns: omrade, bygfase, anvend, bygherre, tid (time), indhold (unit M2)
tid range: 2006-01-01 to 2025-07-01
</table>
<table>
id: laby37
description: Nybyggeri (ikke korrigeret for forsinkelser) efter kommunegruppe, anvendelse og tid
columns: komgrp, anvend, tid (time), indhold (unit M2)
tid range: 2006-01-01 to 2025-04-01
</table>
<table>
id: bygv22
description: Fuldført byggeri (ikke korrigeret for forsinkelser) efter område, enhed, påbegyndelsesår, byggesagstype, anvendelse og tid
columns: omrade, tal, aar, byggesag, anvendelse, tid (time), indhold (unit -)
tid range: 2006-01-01 to 2025-07-01
</table>
<table>
id: bygv33
description: Boliger i det samlede boligbyggeri (ikke korrigeret for forsinkelser) efter område, byggefase, anvendelse, bygherreforhold og tid
columns: omrade, bygfase, anvend, bygherre, tid (time), indhold (unit Antal)
tid range: 2006-01-01 to 2025-07-01
</table>
<table>
id: bygv80
description: Det samlede etageareal (korrigeret for forsinkelser) efter byggefase, anvendelse og tid
columns: bygfase, anvendelse, tid (time), indhold (unit M2)
tid range: 1998-01-01 to 2025-06-01
</table>
<table>
id: bygv88
description: Det samlede etageareal (korrigeret for forsinkelser) efter byggefase, anvendelse, bygherreforhold, sæsonkorrigering og tid
columns: bygfase, anvendelse, bygherre, saeson, tid (time), indhold (unit M2)
tid range: 1998-01-01 to 2025-06-01
</table>
<table>
id: bygv90
description: Boliger i det samlede boligbyggeri (korrigeret for forsinkelser) efter byggefase, anvendelse og tid
columns: bygfase, anvendelse, tid (time), indhold (unit Antal)
tid range: 1998-01-01 to 2025-06-01
</table>
<table>
id: bygv99
description: Boliger i det samlede boligbyggeri (korrigeret for forsinkelser) efter byggefase, anvendelse, bygherreforhold, sæsonkorrigering og tid
columns: bygfase, anvendelse, bygherre, saeson, tid (time), indhold (unit Antal)
tid range: 1998-01-01 to 2025-06-01
</table>
<table>
id: bygvfors
description: Ændring i indberetninger fra første til seneste indberetning efter byggefase og tid
columns: bygfase, tid (time), indhold (unit Pct.)
tid range: 2006-01-01 to 2025-04-01
</table>
<table>
id: bygv01
description: Landstal for den samlede byggeaktivitet (ikke korrigeret for forsinkelser) efter byggefase, anvendelse, bygherreforhold og tid
columns: bygfase, anvend, bygherre, tid (time), indhold (unit M2)
tid range: 1982-01-01 to 2024-01-01
</table>
<table>
id: bygv02
description: Landstal for fuldført byggeri (ikke korrigeret for forsinkelser) efter påbegyndelsesår, enhed, byggesagstype, anvendelse og tid
columns: ar, tal, byggesag, anvendelse, tid (time), indhold (unit -)
tid range: 1998-01-01 to 2024-01-01
</table>
<table>
id: bygv03
description: Landstal for boliger i det samlede boligbyggeri (ikke korrigeret for forsinkelser) efter byggefase, anvendelse, bygherreforhold og tid
columns: bygfase, anvend, bygherre, tid (time), indhold (unit Antal)
tid range: 1981-01-01 to 2024-01-01
</table>
<table>
id: bygv04
description: Den samlede byggeaktivitet (historisk oversigt) efter byggefase, anvendelse og tid
columns: bygfase, anvend, tid (time), indhold (unit M2)
tid range: 1939-01-01 to 2024-01-01
</table>
<table>
id: bygv05a
description: Det samlede boligbyggeri (historisk oversigt) efter byggefase, anvendelse og tid
columns: bygfase, anvend, tid (time), indhold (unit Antal)
tid range: 1917-01-01 to 2024-01-01
</table>
<table>
id: bygv05b
description: Det samlede boligbyggeri (historisk oversigt) efter byggefase, bygherreforhold og tid
columns: bygfase, bygherre, tid (time), indhold (unit Antal)
tid range: 1917-01-01 to 2024-01-01
</table>
<table>
id: bygv06
description: Gennemsnitligt samlet areal i nyopførte boliger (historisk oversigt) efter anvendelse og tid
columns: anvend, tid (time), indhold (unit M2)
tid range: 1916-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- **Korrigeret vs. ikke-korrigeret**: Tables ending in 80/88/90/99 are delay-corrected (korrigeret for forsinkelser) — they revise figures upward to account for late reporting. Tables bygv11/bygv22/bygv33/laby37 are uncorrected. Korrigerede tables have no regional (omrade) breakdown but go back to 1998. Ukorrigerede tables have regional breakdown but only from 2006.
- **Etageareal (m2) vs. boliger (antal)**: Tables with '80'/'88'/'01'/'04' suffixes measure etageareal (m2); '33'/'90'/'99'/'03'/'05a'/'05b' measure boliger (count). bygv11 (m2) and bygv33 (antal) are parallel regional tables; bygv80/bygv90 are their corrected national counterparts.
- **For current construction activity by region**: Use bygv11 (total etageareal, m2) or bygv33 (boliger, antal) — both have nuts regions + kommuner, byggefase, anvend, bygherre, from 2006.
- **For construction by kommunegruppe**: laby37 — but only covers nybyggeri (new construction), not tilbygning/ombygning.
- **For completed construction with lag analysis**: bygv22 (regional) or bygv02 (national) — these have aar (lag from påbegyndelse to fuldførelse) and byggesagstype. Requires filtering tal (46=boliger, 51=etageareal) to avoid double-counting.
- **For seasonal adjustment**: bygv88 (etageareal) or bygv99 (boliger) — only these have saeson column. Must always filter saeson to one value. These use standalone codes for anvendelse and bygherre that do NOT join to dim tables.
- **For long historical series**: bygv04 (etageareal from 1939), bygv05a (boliger from 1917), bygv05b (boliger by bygherre from 1917), bygv06 (average m2 per dwelling from 1916). These use legacy bygfase codes (20/22/24/26 or 30/32/34/36) and old anvend/bygherre codes that don't always match the dim tables. Not suitable for regional breakdown.
- **For national totals from 1982**: bygv01 (etageareal) or bygv03 (boliger) — cleaner than the historisk tables, same dimension structure as the regional tables but national only.
- **Common pitfall**: All tables with multiple omrade/komgrp levels include aggregate rows (omrade='0' or komgrp='0' for Denmark total) that are not in the dim tables and will silently drop from inner joins. All tables with multiple bygfase values include mutually exclusive phases — always filter to one phase when aggregating.
- **bygvfors**: Not a construction volume table — it measures the percentage revision between first and latest reporting. Useful only for data quality assessment.
- **Map**: bygv11, bygv22, and bygv33 support choropleth maps via /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode, exclude omrade=0.