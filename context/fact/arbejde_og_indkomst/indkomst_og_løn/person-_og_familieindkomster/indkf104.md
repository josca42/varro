table: fact.indkf104
description: Familiernes indkomster efter område, enhed, socioøkonomisk status, indkomsttype og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [2, 3]
- enhed: values [100=Familier (Antal), 110=Indkomstbeløb (1.000 kr.), 115=Gennemsnit for alle familier (kr.), 120=Gennemsnit for alle familier med indkomsttypen (kr.)]
- socio: join dim.socio on socio=kode; levels [3]
- indkomsttype: values [100=1 Disponibel indkomst (2+30-31-32-35), 105=2 Indkomst i alt, før skatter mv. (3+7+22+26+29), 110=3 Erhvervsindkomst (4+5+6), 115=4 Løn, 120=5 Virksomhedsoverskud ... 270=35 Betalt underholdsbidrag, 275=Ækvivaleret disponibel indkomst, 280=Ejendomsskat (grundskyld), boligejere, 285=Ejendomsskat (grundskyld), lejere, 290=Skattepligtig indkomst]
- tid: date range 1993-01-01 to 2023-01-01
dim docs: /dim/nuts.md, /dim/socio.md
notes:
- omrade joins dim.nuts at levels 2 (landsdele) and 3 (kommuner). Filter WHERE d.niveau=... when joining.
- omrade='0' is national aggregate, not in dim.nuts.
- socio joins dim.socio at niveau 3, but codes 100, 115, 130 are NOT in dim.socio (same custom aggregates as indkp104). An INNER JOIN silently drops them.
- enhed selector (4 types). Always filter to one.
- indkomsttype is hierarchical — pick one specific type, never sum across types.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.
