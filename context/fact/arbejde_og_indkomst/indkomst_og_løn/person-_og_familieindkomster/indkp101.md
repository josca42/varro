table: fact.indkp101
description: Personer efter område, enhed, køn, indkomsttype og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [2, 3]
- enhed: values [101=Personer med indkomsttypen (antal), 110=Indkomstbeløb (1.000 kr.), 116=Gennemsnit for alle personer (kr.), 121=Gennemsnit for personer med indkomsttypen (kr.)]
- koen: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- indkomsttype: values [100=1 Disponibel indkomst (2+30-31-32-35), 105=2 Indkomst i alt, før skatter mv. (3+7+22+26+29), 110=3 Erhvervsindkomst (4+5+6), 115=4 Løn, 120=5 Virksomhedsoverskud ... 270=35 Betalt underholdsbidrag, 275=Ækvivaleret disponibel indkomst, 280=Ejendomsskat (grundskyld), boligejere, 285=Ejendomsskat (grundskyld), lejere, 290=Skattepligtig indkomst]
- tid: date range 1987-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at levels 2 (landsdele, ~11) and 3 (kommuner, ~98). Always add WHERE d.niveau=... when joining to pick one geographic level and avoid double-counting.
- omrade='0' is the national aggregate — not in dim.nuts. Filter WHERE omrade='0' to get the national total without joining.
- enhed is a measurement selector (4 types). Always filter to one value.
- indkomsttype is hierarchical with 35+ types. Never sum across multiple types — pick one.
- koen='MOK' is the total. Goes back to 1987 — longest regional personal income series in this subject.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.
