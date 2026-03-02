table: fact.spoo1m
description: Serviceerhvervenes omsætningsindeks efter branche, sæsonkorrigering og tid
measure: indhold (unit Indeks)
columns:
- erhverv: join dim.db on erhverv=kode::text [approx: Codes like M69, I55, N77 are section+subsection concatenated; HTNXK, M_STS are custom aggregates not in db]
- saeson2: values [EJSÆSON=Ikke sæsonkorrigeret, SÆSON=Sæsonkorrigeret]
- tid: date range 2021-01-01 to 2025-08-01
dim docs: /dim/db.md

notes:
- saeson2 is a measurement selector that doubles all rows: EJSÆSON (ikke sæsonkorrigeret) or SÆSON (sæsonkorrigeret). Always filter to one value — forgetting this silently doubles every count.
- erhverv codes use NACE section letters as prefix. The dim.db join requires stripping the letter prefix: JOIN dim.db d ON regexp_replace(f.erhverv, '^[A-Z_]+', '') = d.kode::text AND d.niveau = 2. This matches codes like I55→55, J62→62, N77→77 etc. (all single-letter-prefix + 2-digit codes).
- Single-letter codes (H, I, J, L, M, N) are NACE section aggregates with no dim.db match. H=Transport, I=Hotel/restauration, J=IT/medier, L=Fast ejendom, M=Liberale erhverv, N=Administrative serviceydelser. Use them as labels without joining.
- M702 strips to kode=702 which matches dim.db at niveau=3 (Virksomhedsrådgivning), not niveau=2. Filtering d.niveau=2 will drop M702 from join results. To include it, handle separately or use COALESCE with a niveau=3 fallback.
- HTNXK, ITNXK, M_STS are custom DST aggregate codes with no dim.db entry. Use ColumnValues("spoo1m", "erhverv") to see all 27 codes with their labels.
- Sample query (omsætningsindeks per branche, sæsonkorrigeret, seneste måned): SELECT f.erhverv, COALESCE(d.titel, f.erhverv) AS branche, f.indhold FROM fact.spoo1m f LEFT JOIN dim.db d ON regexp_replace(f.erhverv, '^[A-Z_]+', '') = d.kode::text AND d.niveau = 2 WHERE f.saeson2 = 'SÆSON' AND f.tid = '2025-08-01' ORDER BY f.erhverv;