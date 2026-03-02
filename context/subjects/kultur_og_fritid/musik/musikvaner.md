<fact tables>
<table>
id: kv2mks1
description: Udøvelse af musik efter hyppighed, køn, alder og tid
columns: hyp, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2mks2
description: Udøvelse af musik efter måde, køn, alder og tid
columns: musm, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2mk1
description: Forbrug af musik efter adgang, køn, alder og tid
columns: adgang, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2mk2
description: Forbrug af musik efter lokation, køn, alder og tid
columns: lokation, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2mk3
description: Forbrug af musik efter genre, køn, alder og tid
columns: genre, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
<table>
id: kv2mk4
description: Forbrug af musik efter oprindelsesland, køn, alder og tid
columns: oprindland, kon, alder, tid (time), indhold (unit Pct.)
tid range: 2024-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- All 6 tables come from a single 2024 kulturvaner survey. No time series — tid is always 2024-01-01.
- All tables report percentages (Pct.). Never sum indhold values to get a count; these are rates.
- kon and alder always have total rows (kon=10 "Køn i alt", alder='TOT' "Alder i alt"). Always filter to these when you want a single population-level figure. Forgetting either inflates by 3× (kon) or 8× (alder).
- "Udøvelse" tables (kv2mks1, kv2mks2): about playing/performing music. "Forbrug" tables (kv2mk1–kv2mk4): about consuming/listening to music.
- Mutually exclusive categories (safe to read as a distribution): kv2mks1 (frequency, sums to 100) and kv2mk4 (origin preference, sums to 100).
- Multi-select categories (DO NOT sum across the category column): kv2mks2 (ways of playing, ~60 total), kv2mk1 (access methods, ~254 total), kv2mk2 (locations, ~329 total), kv2mk3 (genres, ~328 total). Each row in these tables is an independent rate.
- For "what share of Danes play music": use kv2mks1, filter WHERE hyp NOT IN (111000, 111100, 111200) to exclude non-players and non-responses, then SUM(indhold).
- For "what share of Danes listen to music at home / on streaming / to pop": pick the relevant forbrug table and read the single matching row — no summing needed.
- No dimension table joins — all category columns use inline numeric codes documented in each fact doc.