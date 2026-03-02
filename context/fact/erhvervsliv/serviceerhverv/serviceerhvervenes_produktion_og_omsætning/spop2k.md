table: fact.spop2k
description: Serviceerhvervenes produktionsindeks efter branche, sæsonkorrigering og tid
measure: indhold (unit Indeks)
columns:
- erhverv: join dim.db on erhverv=kode::text [approx: Codes like M69, I55, N77 are section+subsection concatenated; HTNXK, M_STS are custom aggregates not in db]
- saeson2: values [EJSÆSON=Ikke sæsonkorrigeret, SÆSON=Sæsonkorrigeret]
- tid: date range 2021-01-01 to 2025-04-01
dim docs: /dim/db.md

notes:
- saeson2 is a measurement selector that doubles all rows: EJSÆSON or SÆSON. Always filter to one value.
- Same erhverv join as spop2m: regexp_replace(f.erhverv, '^[A-Z_]+', '') = d.kode::text AND d.niveau = 2. 22 erhverv codes, same subset as spop2m (no J59, J60, J61, M74, L).
- Same structure as spop2m (monthly). Use spop2k for quarterly aggregation, spop2m for monthly detail. Both end at 2025-04-01/2025-08-01 respectively.