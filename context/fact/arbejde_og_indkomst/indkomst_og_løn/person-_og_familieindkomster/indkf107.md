table: fact.indkf107
description: Højeste fuldførte uddannelse i familien efter område, enhed, familietype, uddannelsesniveau, indkomsttype og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- enhed: values [100=Familier (Antal), 110=Indkomstbeløb (1.000 kr.), 115=Gennemsnit for alle familier (kr.), 120=Gennemsnit for alle familier med indkomsttypen (kr.)]
- famtype: values [FAIA=Familier i alt, FAUB=Familier uden børn, FAMB=Familier med børn, PAIA=Par i alt, PAUB=Par uden børn, PAMB=Par med børn, ENIA=Enlige i alt, ENUB=Enlige uden børn, ENMB=Enlige med børn]
- uddniv: values [10=10 GRUNDSKOLE                                               , 26=20+25 GYMNASIALE UDDANNELSER, 35=35 ERHVERVSUDDANNELSER, 40=40 KORTE VIDEREGÅENDE UDDANNELSER                           , 61=50+60 MELLEMLANGE VIDEREGÅENDE UDDANNELSER INKL. BACHELOR, 65=65 LANGE VIDEREGÅENDE UDDANNELSER                           , 9=Uoplyst]
- indkomsttype: values [100=1 Disponibel indkomst (2+30-31-32-35), 105=2 Indkomst i alt, før skatter mv. (3+7+22+26+29), 110=3 Erhvervsindkomst (4+5+6), 115=4 Løn, 120=5 Virksomhedsoverskud ... 270=35 Betalt underholdsbidrag, 275=Ækvivaleret disponibel indkomst, 280=Ejendomsskat (grundskyld), boligejere, 285=Ejendomsskat (grundskyld), lejere, 290=Skattepligtig indkomst]
- tid: date range 2000-01-01 to 2023-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at all three levels (1, 2, 3). Filter WHERE d.niveau=... when joining to pick one geographic resolution.
- omrade='0' is national aggregate, not in dim.nuts.
- famtype column (note: 'famtype' not 'famtyp'). uddniv reflects highest education level in the family.
- uddniv is inline (7 education categories). Raw kode values may have trailing whitespace.
- enhed selector (4 types). Always filter to one.
- indkomsttype is hierarchical — pick one specific type.
- Only goes back to 2000 (education data).
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
