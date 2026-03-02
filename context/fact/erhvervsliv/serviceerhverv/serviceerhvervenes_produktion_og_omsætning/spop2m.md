table: fact.spop2m
description: Serviceerhvervenes produktionsindeks efter branche, sæsonkorrigering og tid
measure: indhold (unit Indeks)
columns:
- erhverv: join dim.db on erhverv=kode::text [approx: Codes like M69, I55, N77 are section+subsection concatenated; HTNXK, M_STS are custom aggregates not in db]
- saeson2: values [EJSÆSON=Ikke sæsonkorrigeret, SÆSON=Sæsonkorrigeret]
- tid: date range 2021-01-01 to 2025-08-01
dim docs: /dim/db.md

notes:
- saeson2 is a measurement selector that doubles all rows: EJSÆSON or SÆSON. Always filter to one value.
- Same erhverv join as spoo1m/spoo1k: regexp_replace(f.erhverv, '^[A-Z_]+', '') = d.kode::text AND d.niveau = 2. Single-letter section codes and custom aggregates (HTNXK, ITNXK, M_STS) have no dim.db match.
- Produktionsindeks covers 22 erhverv codes — fewer than omsætningsindeks (27). Missing: J59 (film/musik), J60 (radio/tv), J61 (telekommunikation), M74 (andre liberale ydelser), L (fast ejendom). Use ColumnValues("spop2m", "erhverv") to see exact coverage.
- M702 (Virksomhedsrådgivning) maps to niveau=3 in dim.db — same caveat as spoo1m.
- Produktionsindeks vs omsætningsindeks: both are index measures (2015=100) but production adjusts for resale/trade while turnover is gross receipts. Choose based on question.