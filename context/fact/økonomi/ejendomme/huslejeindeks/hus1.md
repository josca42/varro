table: fact.hus1
description: Huslejeindeks for boliger efter region, ejendomskategori, enhed og tid
measure: indhold (unit Indeks)
columns:
- region: join dim.nuts on region=kode; levels [1]
- ejendomskate: values [550=Boliger i alt, 552=Private boliger, 554=Almene boliger, 556=Andelsboliger]
- tal: values [100=Indeks, 210=Ændring i forhold til kvartalet før (pct.), 310=Ændring i forhold til samme kvartal året før (pct.)]
- tid: date range 2021-01-01 to 2025-07-01
dim docs: /dim/nuts.md

notes:
- `tal` is a measurement selector — every region/ejendomskate combination repeats 3 times (100=Indeks, 210=QoQ%, 310=YoY%). Always filter `tal=100` for index levels or pick one value explicitly; mixing produces meaningless sums.
- `region=0` is the national total ("Hele landet") and is NOT in dim.nuts. Regions 81–85 are the 5 standard regions (alle niveau=1 in dim.nuts). To include the national total in results, handle it separately or use a LEFT JOIN with a CASE for region=0.
- `ejendomskate=556` (Andelsboliger) only has national-level data (region=0) — no regional breakdown. Avoid filtering both region≠0 AND ejendomskate=556 or you'll get zero rows.
- Sample query — huslejeindeks by region for alle boliger: `SELECT d.titel, f.tid, f.indhold FROM fact.hus1 f JOIN dim.nuts d ON f.region=d.kode WHERE f.tal=100 AND f.ejendomskate=550 ORDER BY f.tid, d.titel;` (excludes region=0 national total, includes 5 regioner).
- Map: /geo/regioner.parquet (niveau 1) — merge on region=dim_kode. Exclude region=0.