table: fact.smdbv001
description: Stofmisbrugsbehandling efter område, aktivitet i året og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 3]
- akti: values [ANMOD=Anmodninger, IVAERK=Iværksættelser, BEHSLUT=Afsluttede behandlinger]
- tid: date range 2015-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- omrade joins dim.nuts. Use ColumnValues("nuts", "titel", for_table="smdbv001") to see available regions/kommuner. niveau 1 = 5 regioner (kode 81-85), niveau 3 = 98 kommuner. Filter WHERE d.niveau = 1 or d.niveau = 3 to pick granularity — mixing levels double-counts.
- omrade = '0' is the national total ("Hele landet"). This code is not in dim.nuts, so it won't appear in a JOIN — use WHERE f.omrade = '0' directly if you want national figures.
- akti has 3 independent activity types: ANMOD (requests), IVAERK (treatment starts), BEHSLUT (completed treatments). These are distinct counts for the same population — filter to one akti at a time. Summing all three is meaningless.
- Sample query — treatment starts by region (2024): SELECT d.titel, f.indhold FROM fact.smdbv001 f JOIN dim.nuts d ON f.omrade = d.kode WHERE d.niveau = 1 AND f.akti = 'IVAERK' AND f.tid = '2024-01-01'
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.