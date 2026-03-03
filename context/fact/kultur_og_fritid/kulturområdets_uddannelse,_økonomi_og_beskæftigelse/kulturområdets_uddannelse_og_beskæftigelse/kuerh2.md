table: fact.kuerh2
description: Kulturens erhvervsstruktur efter område, aktivitet, enhed og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 3]
- aktivi: values [TOT=Alle aktiviteter, 0=Kerneaktivitet, 1=Støtteaktivitet]
- enhed: values [10=Fuldtidsbeskæftigede, 20=Arbejdssteder ultimo november]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/nuts.md

notes:
- enhed is a measurement selector: 10=Fuldtidsbeskæftigede, 20=Arbejdssteder. Always filter to one enhed value.
- CRITICAL: omrade contains BOTH niveau=1 (regioner, codes 81–85) AND niveau=3 (kommuner, codes 101+). When joining dim.nuts, always filter d.niveau to pick one granularity — otherwise you get double-counting across hierarchy levels.
- Code 0 = national total (not in dim). Codes 86 and 998 are also unmatched (likely special territories/unspecified) — exclude when joining.
- For regional analysis: WHERE d.niveau = 1. For municipal: WHERE d.niveau = 3.
- aktivi=TOT is the aggregate total; filter when comparing kerneaktivitet vs støtteaktivitet.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade IN (0, 86, 998).