table: fact.indkf111
description: Familiernes indkomster efter område, enhed, familietype, indkomsttype og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- enhed: values [100=Familier (Antal), 110=Indkomstbeløb (1.000 kr.), 115=Gennemsnit for alle familier (kr.), 120=Gennemsnit for alle familier med indkomsttypen (kr.)]
- famtyp: values [FAIA=Familier i alt, FAUB=Familier uden børn, FAMB=Familier med børn, PAIA=Par i alt, PAUB=Par uden børn, PAMB=Par med børn, ENIA=Enlige i alt, ENUB=Enlige uden børn, ENMB=Enlige med børn, EKIA=Enlige kvinder i alt, EKUB=Enlige kvinder uden børn, EKMB=Enlige kvinder med børn, EMIA=Enlige mænd i alt, EMUB=Enlige mænd uden børn, EMMB=Enlige mænd med børn]
- indkomsttype: values [100=1 Disponibel indkomst (2+30-31-32-35), 105=2 Indkomst i alt, før skatter mv. (3+7+22+26+29), 110=3 Erhvervsindkomst (4+5+6), 115=4 Løn, 120=5 Virksomhedsoverskud ... 270=35 Betalt underholdsbidrag, 275=Ækvivaleret disponibel indkomst, 280=Ejendomsskat (grundskyld), boligejere, 285=Ejendomsskat (grundskyld), lejere, 290=Skattepligtig indkomst]
- tid: date range 1991-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at all three levels (1, 2, 3). Filter WHERE d.niveau=... when joining.
- omrade='0' is national aggregate, not in dim.nuts.
- famtyp totals: FAIA=familier i alt. Extended set includes gender-specific singles (EKIA, EMIA, etc.).
- enhed selector (4 types). Always filter to one.
- indkomsttype is hierarchical — pick one specific type.
- Goes back to 1991. Broadest family income table with geography + familietype + indkomsttype.
- Map: /geo/kommuner.parquet (niveau 3), /geo/landsdele.parquet (niveau 2), or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
