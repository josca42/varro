<fact tables>
<table>
id: turist
description: Overnatninger efter overnatningsform, område, gæstens nationalitet, periode og tid
columns: overnatf, omrade, nation1, periode, tid (time), indhold (unit Antal)
tid range: 1992-01-01 to 2025-01-01
</table>
<table>
id: turist1
description: Overnatninger efter overnatningsform, sæsonkorrigering, gæstens nationalitet og tid
columns: overnatf, saeson, nation1, tid (time), indhold (unit Antal)
tid range: 2004-01-01 to 2025-08-01
</table>
<table>
id: turist2
description: Gæster efter overnatningsform, område, gæstens nationalitet, periode og tid
columns: overnatf, omrade, nation1, periode, tid (time), indhold (unit Antal)
tid range: 2018-01-01 to 2025-01-01
</table>
<table>
id: turist4
description: Overnatninger på mindre hoteller og campingpladser efter overnatningsform, område, gæstens nationalitet og tid
columns: overnatf, omrade, nation1, tid (time), indhold (unit Antal)
tid range: 2016-01-01 to 2024-01-01
</table>
</fact tables>

notes:
- For overnight stays (overnatninger) by region/nationality/accommodation type with long history: use turist (1992–2025). Covers all accommodation types including aggregate code 100, both regions (niveau 1) and landsdele (niveau 2).
- For guest counts (gæster/arrivals, not nights): use turist2 (2018–2025). Same structure as turist but counts people not nights.
- For seasonally adjusted data or trend analysis: use turist1 (2004–2025). Simpler structure (no omrade, no periode), but ALWAYS filter saeson to either SÆSON or EJSÆSON — both appear for every row.
- For small-establishment-specific data (small hotels 10–39 beds, small campsites 10–74 units): use turist4 (2016–2024). Simplest structure, regional level only.
- SHARED PITFALL — periode column (turist + turist2): codes 1, 2, 3 are ambiguous — each maps to BOTH an aggregate period (Hele Året, År til dato, De sidste tolv måneder) AND a specific month (Januar, Februar, Marts). This causes genuine duplicate rows. Safe monthly queries should filter to periode IN (4..12) for April–December; handle months 1–3 with care.
- SHARED PITFALL — omrade (turist + turist2 + turist4): omrade=0 is the national total and is not in dim.nuts. In turist and turist2, both niveau 1 (regioner) and niveau 2 (landsdele) appear — never SUM all omrade values. Filter by niveau in the join.
- SHARED PITFALL — overnatf hierarchy (turist + turist2): code 100 contains all sub-types. Never SUM code 100 together with sub-codes 110–170 — this double-counts.
- Map: turist, turist2, and turist4 support choropleth maps via omrade. turist/turist2 have niveau 1 (regioner) + niveau 2 (landsdele); turist4 has niveau 1 only. Use context/geo/regioner.parquet or context/geo/landsdele.parquet — merge on omrade=dim_kode. Exclude omrade=0. turist1 has no geographic breakdown.