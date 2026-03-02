table: fact.aku420a
description: Gennemsnitlig ugentlig arbejdstid i hovedjob efter arbejdstid, branche (DB07) og tid
measure: indhold (unit Timer)
columns:
- arbejdstid: values [2=Normal ugentlig arbejdstid, 1-95 timer, 12=Faktisk ugentlig arbejdstid, 0-95 timer (inkl. fuld fravær i referenceugen), 22=Faktisk ugentlig arbejdstid, 1-95 timer (mindst en times arbejde i referenceugen)]
- branche07: join dim.db_10 on branche07=kode::text [approx]; levels [1]
- tid: date range 2008-01-01 to 2024-01-01
dim docs: /dim/db_10.md

notes:
- branche07 joins dim.db_10 at niveau 1 (11 DB07 industry groups). Code TOT = all industries, not in dim. Join: LEFT JOIN dim.db_10 d ON f.branche07 = d.kode::text.
- arbejdstid has 3 distinct measurement types — always filter to exactly one: code 2=normal contractual hours, 12=actual hours (includes weeks with zero work due to full absence), 22=actual hours (only weeks with at least 1 hour worked). For most comparisons, code 2 (normal hours) is the most stable.
- Annual data only (tid steps yearly to 2024). Use aku410a for the same series broken down by alder/køn.