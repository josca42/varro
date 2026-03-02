table: fact.konk15
description: Erklærede konkurser efter branche (DB07), virksomhedstype og tid
measure: indhold (unit Antal)
columns:
- branche07: join dim.db on branche07=kode::text; levels [5]
- virktyp1: values [K01=Konkurser i alt, K02=Konkurser i aktive virksomheder, K03=Konkurser i nulvirksomheder]
- tid: date range 2009-01-01 to 2025-09-01
dim docs: /dim/db.md

notes:
- branche07 codes are zero-padded 6-digit strings (e.g. '011100') but dim.db stores them as 5-digit integers (e.g. 11100). The standard join ON f.branche07 = d.kode::text fails for ~8% of codes. Use: JOIN dim.db d ON LPAD(d.kode::text, 6, '0') = f.branche07 AND d.niveau = 5
- All branche07 codes are at niveau 5 (undergruppe, 736 distinct codes). To group by higher-level sectors, join dim.db multiple times up the parent_kode chain. Example for afsnit (niveau 2): JOIN dim.db d5 ON LPAD(d5.kode::text,6,'0')=f.branche07 AND d5.niveau=5, JOIN dim.db d4 ON d4.kode=d5.parent_kode, JOIN dim.db d3 ON d3.kode=d4.parent_kode, JOIN dim.db d2 ON d2.kode=d3.parent_kode AND d2.niveau=2.
- virktyp1 is a measurement selector: K01=total, K02=aktive virksomheder, K03=nulvirksomheder. K01 = K02 + K03. Always filter to one.
- Use ColumnValues("db", "titel", for_table="konk15") to browse the 736 niveau-5 codes available in this table.