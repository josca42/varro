table: fact.indkf101
description: Familiernes indkomster efter område, enhed, ejer/lejer af bolig, indkomsttype og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [2, 3]
- enhed: values [100=Familier (Antal), 110=Indkomstbeløb (1.000 kr.), 115=Gennemsnit for alle familier (kr.), 120=Gennemsnit for alle familier med indkomsttypen (kr.)]
- boligartud: values [TOT=I alt, EJ=Beboet af ejer, LEJ=Beboet af lejer]
- indkomsttype: values [100=1 Disponibel indkomst (2+30-31-32-35), 105=2 Indkomst i alt, før skatter mv. (3+7+22+26+29), 110=3 Erhvervsindkomst (4+5+6), 115=4 Løn, 120=5 Virksomhedsoverskud ... 270=35 Betalt underholdsbidrag, 275=Ækvivaleret disponibel indkomst, 280=Ejendomsskat (grundskyld), boligejere, 285=Ejendomsskat (grundskyld), lejere, 290=Skattepligtig indkomst]
- tid: date range 2000-01-01 to 2023-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at levels 2 (landsdele) and 3 (kommuner). Filter WHERE d.niveau=... when joining.
- omrade='0' is national aggregate, not in dim.nuts.
- boligartud: TOT=I alt, EJ=ejer, LEJ=lejer. Filter to TOT for overall income, or split by tenure type.
- enhed selector (4 types). Always filter to one. Note: enhed=100 gives family count, not an income amount.
- indkomsttype is hierarchical with 35+ types — pick one specific type.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.
