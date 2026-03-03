table: fact.livmus04
description: Antal koncertarrangører efter arrangørtype, sektor, landsdel og tid
measure: indhold (unit Antal)
columns:
- arrangeor: values [103005=Folkekirke, 103010=Kulturhus, 103015=Landsdelsorkester, 103020=Musikfestival, 103025=Musikforening, 103030=Regionalt spillested, 103035=Spillested, 103080=Professionel koncertarrangør, 103040=Øvrig koncertarrangør]
- sektor: values [TOT=I alt, 90=Statslig, 91=Kommunal, 92=Privat, 99=Uoplyst]
- landsdel: join dim.nuts on landsdel=kode; levels [2]
- tid: date range 2018-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- landsdel joins dim.nuts at niveau=2 (11 landsdele, kode 1–11). Codes 0 (I alt/total) and 99 (Uoplyst) do not join to dim — exclude them when doing regional breakdowns: WHERE f.landsdel NOT IN ('0','99').
- Use ColumnValues("nuts", "titel", for_table="livmus04") to see the 11 regions available.
- sektor='TOT' is the total across sectors (Statslig/Kommunal/Privat/Uoplyst). Filter it out when breaking down by sector.
- arrangeor has no total code — all 9 values are individual organizer types.
- Typical query: organizer counts by region for a given year — JOIN dim.nuts ON niveau=2, filter sektor='TOT', exclude landsdel IN ('0','99').
- Map: /geo/landsdele.parquet — merge on landsdel=dim_kode. Exclude landsdel IN ('0','99').