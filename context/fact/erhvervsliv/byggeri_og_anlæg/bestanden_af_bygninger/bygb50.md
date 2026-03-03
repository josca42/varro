table: fact.bygb50
description: Bygninger og deres bebyggede areal efter område, enhed, tagdækningsmateriale, anvendelse, opførelsesår og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- maengde4: values [45=Bygninger (antal), 50=Kvadratmeter (1000 m2)]
- tagmat: values [2=Built-up (fladt tag), 4=Tagpap (med taghældning), 6=Fibercement, inkl. asbest, 8=Cementsten, 10=Tegl, 12=Metalplader (bølgeblik, aluminium ol.), 14=Stråtag, 16=Fibercement (asbestfri), 18=PVC, tagdækningsmateriale, 20=Glas, tagdækningsmateriale, 22=Grønne Tage, 24=Ingen tagdækningsmateriale, 26=Andet tagdækningsmateriale, 28=Uoplyst eller ukendt tagdækningsmateriale]
- anvend: join dim.byganv on anvend=kode [approx]; levels [2, 3]
- opforelsesar: values [-1899=Før 1900, 00-04=1900-1904, 05-09=1905-1909, 10-14=1910-1914, 15-19=1915-1919 ... 05-10=2005-2009, 11-15=2010-2014, 15-20=2015-2019, 2020-2024=2020 -, UOPL=Uoplyst]
- tid: date range 2011-01-01 to 2025-01-01
dim docs: /dim/byganv.md, /dim/nuts.md

notes:
- maengde4 is a measurement selector — same dims appear TWICE: maengde4=45 (Bygninger, antal) and maengde4=50 (Bebygget areal, 1.000 m2). Always filter to one value; summing both silently doubles or mixes units.
- omrade joins dim.nuts. omrade=0 is national aggregate (not in dim — dropped by INNER JOIN).
- anvend joins dim.byganv. Always filter WHERE d.niveau = 2. anvend=592 unmatched (dropped by INNER JOIN).
- tagmat has 14 values (no total code). These are mutually exclusive roofing materials — safe to sum across all. Note: category 28=Uoplyst eller ukendt can be significant.
- opforelsesar: century-wrapping 5-year codes. Use ColumnValues("bygb50", "opforelsesar") for labels.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.