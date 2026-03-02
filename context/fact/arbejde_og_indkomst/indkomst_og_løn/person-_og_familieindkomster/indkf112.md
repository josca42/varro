table: fact.indkf112
description: Familiernes indkomster efter område, enhed, familietype, antal børn, indkomsttype og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- enhed: values [100=Familier (Antal), 110=Indkomstbeløb (1.000 kr.), 115=Gennemsnit for alle familier (kr.), 120=Gennemsnit for alle familier med indkomsttypen (kr.)]
- famtyp: values [FAIA=Familier i alt, PAIA=Par i alt, ENIA=Enlige i alt]
- antborn: values [TOT=I alt, 0=0 børn, 1=1 barn, 2=2 børn, 3-=3 eller flere børn]
- indkomsttype: values [100=1 Disponibel indkomst (2+30-31-32-35), 105=2 Indkomst i alt, før skatter mv. (3+7+22+26+29), 110=3 Erhvervsindkomst (4+5+6), 115=4 Løn, 120=5 Virksomhedsoverskud ... 270=35 Betalt underholdsbidrag, 275=Ækvivaleret disponibel indkomst, 280=Ejendomsskat (grundskyld), boligejere, 285=Ejendomsskat (grundskyld), lejere, 290=Skattepligtig indkomst]
- tid: date range 1993-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at all three levels (1, 2, 3). Filter WHERE d.niveau=... when joining.
- omrade='0' is national aggregate, not in dim.nuts.
- antborn: TOT=I alt, 0=ingen børn, 1=1 barn, 2=2 børn, 3-=3+. Filter antborn when summing to avoid double-counting.
- famtyp here has only 3 types (FAIA, PAIA, ENIA) — no gender breakdown of singles.
- enhed selector (4 types). Always filter to one.
- indkomsttype is hierarchical — pick one specific type.
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
