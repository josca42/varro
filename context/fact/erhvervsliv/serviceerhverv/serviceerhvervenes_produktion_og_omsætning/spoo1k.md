table: fact.spoo1k
description: Serviceerhvervenes omsætningsindeks efter branche, sæsonkorrigering og tid
measure: indhold (unit Indeks)
columns:
- erhverv: join dim.db on erhverv=kode::text [approx: Codes like M69, I55, N77 are section+subsection concatenated; HTNXK, M_STS are custom aggregates not in db]
- saeson2: values [EJSÆSON=Ikke sæsonkorrigeret, SÆSON=Sæsonkorrigeret]
- tid: date range 2021-01-01 to 2025-04-01
dim docs: /dim/db.md

notes:
- saeson2 is a measurement selector that doubles all rows: EJSÆSON (ikke sæsonkorrigeret) or SÆSON (sæsonkorrigeret). Always filter to one value — forgetting this silently doubles every count.
- erhverv codes use NACE section letters as prefix. The dim.db join requires stripping the letter prefix: JOIN dim.db d ON regexp_replace(f.erhverv, '^[A-Z_]+', '') = d.kode::text AND d.niveau = 2. This matches codes like I55→55, J62→62, N77→77 etc.
- Single-letter codes (H, I, J, L, M, N) are NACE section aggregates with no dim.db match. H=Transport, I=Hotel/restauration, J=IT/medier, L=Fast ejendom, M=Liberale erhverv, N=Administrative serviceydelser. Use them as labels without joining.
- M702 strips to kode=702 at niveau=3 (Virksomhedsrådgivning), not niveau=2. Filtering d.niveau=2 will drop M702 from join results.
- HTNXK, ITNXK, M_STS are custom DST aggregate codes with no dim.db entry. Same 27 codes as spoo1m but quarterly range ends 2025-04-01.
- Same structure as spoo1m (monthly). Use spoo1k for quarterly aggregation, spoo1m for monthly detail.