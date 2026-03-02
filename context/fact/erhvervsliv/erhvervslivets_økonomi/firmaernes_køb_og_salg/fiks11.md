table: fact.fiks11
description: Firmaernes køb og salg efter branche (DB07), beløb, sæsonkorrigering og tid
measure: indhold (unit Mio. kr.)
columns:
- branche07: join dim.db on branche07=kode::text [approx]; levels [2, 3]
- belob: values [4=Salg i alt, 1=Indenlandsk salg, 3=Køb i alt, 0=Indenlandsk køb]
- saeson: values [EJSÆSON=Ikke sæsonkorrigeret, SÆSON=Sæsonkorrigeret]
- tid: date range 2009-01-01 to 2025-08-01
dim docs: /dim/db.md

notes:
- Monthly time series (tid steps are monthly, 2009–2025).
- saeson is a measurement selector: every row is duplicated for EJSÆSON (ikke sæsonkorrigeret) and SÆSON (sæsonkorrigeret). Always filter to one value or counts double.
- belob is a measurement selector: pick exactly one per query. 0=Indenlandsk køb, 1=Indenlandsk salg, 3=Køb i alt, 4=Salg i alt. Never sum across belob values.
- branche07 has two distinct code types that must not be mixed:
  (1) 13 numeric codes (1, 2, 3, 5-11, 45, 46, 47) = individual DB07 divisions → join dim.db ON branche07=kode::text AND niveau=2. The niveau=2 filter is required because code '11' exists at both niveau 2 (Fremstilling af drikkevarer) and niveau 3 (Dyrkning af etårige afgrøder) in dim.db — omitting it duplicates rows for branche07='11'.
  (2) 9 letter/aggregate codes (B, C, DE, G, H, I, BDE, TOT, 4) = DST section-level aggregates not in dim.db. These overlap with the numeric codes (e.g. C includes divisions 10+11). Do not sum numeric and letter codes together.
- To get a labelled series for individual divisions: JOIN dim.db d ON f.branche07=d.kode::text AND d.niveau=2, then filter WHERE f.branche07 NOT IN ('B','C','DE','G','H','I','BDE','TOT','4').
- Use ColumnValues("fiks11", "branche07") to see all 22 codes with their text labels.