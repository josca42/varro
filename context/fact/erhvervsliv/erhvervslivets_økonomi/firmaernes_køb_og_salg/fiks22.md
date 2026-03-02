table: fact.fiks22
description: Firmaernes køb og salg (19-grupperingen) efter branche (DB07), beløb, sæsonkorrigering og tid
measure: indhold (unit Mio. kr.)
columns:
- branche07: join dim.db on branche07=kode::text [approx]
- belob: values [4=Salg i alt, 1=Indenlandsk salg, 3=Køb i alt, 0=Indenlandsk køb]
- saeson: values [EJSÆSON=Ikke sæsonkorrigeret, SÆSON=Sæsonkorrigeret]
- tid: date range 2009-01-01 to 2025-08-01
dim docs: /dim/db.md

notes:
- Monthly time series (same as fiks11 but branche is at the 19-grupperingen level).
- saeson is a measurement selector: always filter to one value (EJSÆSON or SÆSON) or counts double.
- belob is a measurement selector: pick exactly one per query (0/1/3/4). Never sum across.
- branche07 uses NACE section letter codes A through S (19 sections), plus TOT and X. These do NOT join to dim.db — dim.db uses numeric codes for divisions, not section letters. There is no dim table for the 19-grupperingen.
- Use ColumnValues("fiks22", "branche07") to get the 21 codes with Danish labels. X = uoplyst aktivitet (firms with unknown industry classification).
- For industry labels when querying: filter or annotate branche07 values directly using the ColumnValues lookup rather than a dim join.