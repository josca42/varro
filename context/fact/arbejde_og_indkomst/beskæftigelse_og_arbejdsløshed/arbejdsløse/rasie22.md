table: fact.rasie22
description: Arbejdsstyrken til ledighedspct-beregning (ultimo november) efter herkomst, oprindelsesland, område og tid
measure: indhold (unit Antal)
columns:
- herkomst: values [TOT=I alt, DAN=Dansk oprindelse, IND=Indvandrere / efterkommere, UOP=Uoplyst herkomst]
- ieland: join dim.lande_uhv on ieland=kode [approx]
- omrade: join dim.nuts on omrade=kode [approx]; levels [2]
- tid: date range 2007-01-01 to 2023-01-01
dim docs: /dim/lande_uhv.md, /dim/nuts.md

notes:
- ieland does NOT join dim.lande_uhv. Same custom 39-code classification as aul03/aulk03/rasie11. Use ColumnValues("rasie22", "ieland").
- omrade joins dim.nuts at niveau=2 only (11 landsdele). Extra code 0=Hele landet not in dim.
- No alder or kon breakdown here (use rasie11 for age/gender detail). Regional workforce denominator for origin-country unemployment rates. Annual snapshots, stopped 2023.
- Map: /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.