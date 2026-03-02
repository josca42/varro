<fact tables>
<table>
id: spoo1m
description: Serviceerhvervenes omsætningsindeks efter branche, sæsonkorrigering og tid
columns: erhverv, saeson2, tid (time), indhold (unit Indeks)
tid range: 2021-01-01 to 2025-08-01
</table>
<table>
id: spoo1k
description: Serviceerhvervenes omsætningsindeks efter branche, sæsonkorrigering og tid
columns: erhverv, saeson2, tid (time), indhold (unit Indeks)
tid range: 2021-01-01 to 2025-04-01
</table>
<table>
id: spop2m
description: Serviceerhvervenes produktionsindeks efter branche, sæsonkorrigering og tid
columns: erhverv, saeson2, tid (time), indhold (unit Indeks)
tid range: 2021-01-01 to 2025-08-01
</table>
<table>
id: spop2k
description: Serviceerhvervenes produktionsindeks efter branche, sæsonkorrigering og tid
columns: erhverv, saeson2, tid (time), indhold (unit Indeks)
tid range: 2021-01-01 to 2025-04-01
</table>
</fact tables>

notes:
- All four tables share identical column structure: erhverv + saeson2 + tid. Always filter saeson2 to EJSÆSON or SÆSON — it doubles every row and forgetting it silently inflates all results.
- Time granularity encoded in suffix: m=månedlig, k=kvartal. spoo1m/spop2m are monthly; spoo1k/spop2k are quarterly. The monthly tables have longer coverage (to 2025-08-01 vs 2025-04-01 for quarterly).
- Omsætningsindeks (spoo1*) = turnover index (gross receipts). Produktionsindeks (spop2*) = production index (adjusts for resale). Omsætning covers 27 erhverv codes; produktion covers 22 — it excludes J59 (film/musik), J60 (radio/tv), J61 (telekommunikation), M74 (andre liberale ydelser), L (fast ejendom).
- erhverv codes are NACE-style: single-letter section codes (H, I, J, L, M, N) are section aggregates; letter+number codes (I55, J62, N77…) are 2-digit subsectors joinable to dim.db via regexp_replace(f.erhverv, '^[A-Z_]+', '') = d.kode::text AND d.niveau = 2. HTNXK, ITNXK, M_STS are custom DST cross-section aggregates — no dim.db match.
- All four tables cover data from 2021-01-01. No long historical series — for pre-2021 service sector data, look elsewhere.