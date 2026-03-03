table: fact.bygb12
description: Bygninger efter område, ejerforhold, anvendelse, arealintervaller og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- ejer: values [15=Privat person, I/S og privat andelsboligforening, 20=Almene boligselskaber, 30=A/S, ApS og andre selskaber, SK=Offentlig myndighed, 90=Andet, herunder moderejendomme]
- anvend: join dim.byganv on anvend=kode [approx]; levels [2, 3]
- arealint: values [99=Mindre end 99 m2, 100=100-199 m2, 200=200-499 m2, 500=500-999 m2, 1999=1000-1999 m2, 4999=2000-4999 m2, 5000=Mere end 5000 m2]
- tid: date range 2011-01-01 to 2025-01-01
dim docs: /dim/byganv.md, /dim/nuts.md

notes:
- omrade joins dim.nuts. omrade=0 is national aggregate (not in dim — dropped by INNER JOIN). Use ColumnValues("nuts", "titel", for_table="bygb12") to see available regions. niveau 1=5 regioner, niveau 2=11 landsdele, niveau 3=99 kommuner. Filter d.niveau to pick granularity.
- anvend joins dim.byganv. Some anvend codes (110, 120, 140, 150, 160, 190, 290, 390, 490, 510, ...) exist in the dim at BOTH niveau=2 and niveau=3. A join without niveau filter doubles those rows — always add WHERE d.niveau = 2 for this table. anvend=592 is a BBR subcode not yet in the dim (dropped by INNER JOIN).
- ejer, arealint: no total codes — all values are mutually exclusive categories safe to sum across. ejer has 5 owner types (15, 20, 30, SK, 90); arealint has 7 size bands.
- To count all buildings by region: filter to a single tid, join dim.nuts with d.niveau=3 for municipalities. Sum indhold across all ejer and arealint to get total building count.
- Sample query — buildings per municipality by owner type (latest period):
  SELECT d.titel, f.ejer, SUM(f.indhold)
  FROM fact.bygb12 f
  JOIN dim.nuts d ON f.omrade = d.kode AND d.niveau = 3
  WHERE f.tid = '2025-01-01'
  GROUP BY d.titel, f.ejer;
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.