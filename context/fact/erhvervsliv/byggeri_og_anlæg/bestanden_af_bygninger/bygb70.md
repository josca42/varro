table: fact.bygb70
description: Bygninger og deres etageareal efter område, enhed, anvendelse og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- maengde4: values [45=Bygninger (antal), 50=Kvadratmeter (1000 m2)]
- anvend: join dim.byganv on anvend=kode [approx]; levels [2, 3]
- tid: date range 2021-01-01 to 2025-01-01
dim docs: /dim/byganv.md, /dim/nuts.md

notes:
- maengde4 is a measurement selector — same dims appear TWICE: maengde4=45 (Bygninger, antal) and maengde4=50 (Etageareal, 1.000 m2). Always filter to one value.
- omrade joins dim.nuts. omrade=0 is national aggregate (not in dim — dropped by INNER JOIN).
- anvend joins dim.byganv at niveau=3 (finer BBR codes: 121=Sammenbygget enfamiliehus, 131=Række- og kædehus, 132=Dobbelthus, 211=Stald til svin, ...). This is the only bygb table with niveau=3 granularity. To join dim: filter WHERE d.niveau = 3. Use ColumnValues("byganv", "titel", for_table="bygb70") to see available codes.
- CAVEAT: 13 anvend codes in bygb70 (130, 210, 220, 230, 310, 320, 330, 410, 420, 430, 440, 520, 530) only exist at niveau=2 in the dim — they have no niveau=3 sub-codes. Filtering d.niveau=3 drops these rows (~1.3M m2 for anvend=210 alone). If you need complete coverage, either drop the dim join and use anvend codes directly, or handle the 13 niveau=2-only codes separately.
- anvend codes 122, 592, 990 are unmatched in dim.byganv entirely — dropped by any INNER JOIN.
- Only covers 2021-2025; other bygb tables cover 2011-2025.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.