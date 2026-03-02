table: fact.bygb60
description: Bygninger og deres etageareal efter område, enhed, ydrevægsmateriale, anvendelse, opførelsesår og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- maengde4: values [45=Bygninger (antal), 50=Kvadratmeter (1000 m2)]
- ydremat: values [30=Mursten (tegl, kalksandsten, cementsten), 32=Letbeton (gasbeton), 34=Fibercement plader,incl.asbest, 36=Bindingsværk, 38=Træbeklædning, 40=Betonelementer, 42=Metalplader, 44=Fibercement plader, asbestfri, 46=PVC, ydervægsmateriale, 48=Glas, ydervægsmateriale, 50=Ingen ydervægsmateriale, 52=Andet ydervægsmateriale, 54=Uoplyst eller ukendt ydervægsmateriale]
- anvend: join dim.byganv on anvend=kode [approx]; levels [2, 3]
- opforelsesar: values [-1899=Før 1900, 00-04=1900-1904, 05-09=1905-1909, 10-14=1910-1914, 15-19=1915-1919 ... 05-10=2005-2009, 11-15=2010-2014, 15-20=2015-2019, 2020-2024=2020 -, UOPL=Uoplyst]
- tid: date range 2011-01-01 to 2025-01-01
dim docs: /dim/byganv.md, /dim/nuts.md

notes:
- maengde4 is a measurement selector — same dims appear TWICE: maengde4=45 (Bygninger, antal) and maengde4=50 (Etageareal, 1.000 m2). Always filter to one value.
- omrade joins dim.nuts. omrade=0 is national aggregate (not in dim — dropped by INNER JOIN).
- anvend joins dim.byganv. Always filter WHERE d.niveau = 2. anvend=592 unmatched (dropped by INNER JOIN).
- ydremat has 13 values (no total code). Mutually exclusive wall cladding materials — safe to sum. Category 54=Uoplyst eller ukendt can be large.
- opforelsesar: century-wrapping 5-year codes. Use ColumnValues("bygb60", "opforelsesar") for labels.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.