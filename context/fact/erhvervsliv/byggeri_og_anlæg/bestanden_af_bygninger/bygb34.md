table: fact.bygb34
description: Bygningsbestandens areal efter område, anvendelse, arealtype, opførelsesår og tid
measure: indhold (unit 1.000 m2)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- anvend: join dim.byganv on anvend=kode [approx]; levels [2, 3]
- arealtype: values [1=Samlet etageareal, 2=Kælderareal, 3=Erhvervsareal, 4=Boligareal]
- opforelsesar: values [-1899=Før 1900, 00-04=1900-1904, 05-09=1905-1909, 10-14=1910-1914, 15-19=1915-1919 ... 05-10=2005-2009, 11-15=2010-2014, 15-20=2015-2019, 2020-2024=2020 -, UOPL=Uoplyst]
- tid: date range 2011-01-01 to 2025-01-01
dim docs: /dim/byganv.md, /dim/nuts.md

notes:
- indhold is in 1.000 m2. Multiply by 1000 to get actual m2 or leave as-is for summary tables.
- omrade joins dim.nuts. omrade=0 is national aggregate (not in dim — dropped by INNER JOIN).
- anvend joins dim.byganv. Always filter WHERE d.niveau = 2 — some codes exist in dim at both niveau 2 and 3, doubling rows without a niveau filter. anvend=592 unmatched (dropped by INNER JOIN).
- arealtype is NOT a measurement selector in the usual sense but its categories overlap: arealtype=1 (Samlet etageareal) is the total floor area and does NOT equal the sum of arealtype 2+3+4. Always filter to the specific arealtype you want — never sum across all four. For total area use arealtype=1; for residential area use arealtype=4; for commercial area use arealtype=3.
- opforelsesar uses a confusing 5-year period coding that wraps across centuries (e.g. "05-09"=1905-1909, "05-10"=2005-2009, "20-24"=1920-1924, "20-04"=2000-2004). Use ColumnValues("bygb34", "opforelsesar") to browse the codes with labels rather than guessing from the codes themselves. No total code — safe to sum across periods.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.