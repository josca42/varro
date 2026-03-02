table: fact.bygb40
description: Bygninger og deres opvarmede areal efter område, enhed, opvarmingsform, anvendelse, opførelsesår og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- maengde4: values [45=Bygninger (antal), 50=Kvadratmeter (1000 m2)]
- opvarm: values [1=Fjernvarme, 2=Centralvarme med oliefyr, 3=Centralvarme med naturgas, 4=Centralvarme med fast brændsel, 5=Elovne eller elpaneler, 6=Ovne med olie eller petroleum, 7=Ovne med fast brændstof, 8=Varmepumpe, 9=Anden opvarmningsform, 10=Ingen eller uoplyst opvarmning]
- anvend: join dim.byganv on anvend=kode [approx]; levels [2, 3]
- opforelsesar: values [-1899=Før 1900, 00-04=1900-1904, 05-09=1905-1909, 10-14=1910-1914, 15-19=1915-1919 ... 05-10=2005-2009, 11-15=2010-2014, 15-20=2015-2019, 2020-2024=2020 -, UOPL=Uoplyst]
- tid: date range 2011-01-01 to 2025-01-01
dim docs: /dim/byganv.md, /dim/nuts.md

notes:
- maengde4 is a measurement selector — the same combination of omrade/opvarm/anvend/opforelsesar appears TWICE: once with maengde4=45 (Bygninger, antal) and once with maengde4=50 (Kvadratmeter, 1.000 m2). Always filter to one value. Summing across both silently doubles or mixes units.
- omrade joins dim.nuts. omrade=0 is national aggregate (not in dim — dropped by INNER JOIN).
- anvend joins dim.byganv. Always filter WHERE d.niveau = 2. anvend=592 unmatched (dropped by INNER JOIN).
- opvarm has 10 values (1–10), no total code. These are mutually exclusive heating types — safe to sum.
- opforelsesar: confusing century-wrapping 5-year codes. Use ColumnValues("bygb40", "opforelsesar") to browse with labels. No total code.
- To get number of buildings by heating type nationally: filter maengde4=45, omrade=0, and choose a single tid.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.