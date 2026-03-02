table: fact.indkp107
description: Personindkomster efter område, enhed, køn, uddannelsesniveau, indkomsttype og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [1, 2, 3]
- enhed: values [101=Personer med indkomsttypen (antal), 110=Indkomstbeløb (1.000 kr.), 116=Gennemsnit for alle personer (kr.), 121=Gennemsnit for personer med indkomsttypen (kr.)]
- koen: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- uddniv: values [10=10 GRUNDSKOLE                                               , 26=20+25 GYMNASIALE UDDANNELSER, 35=35 ERHVERVSUDDANNELSER, 40=40 KORTE VIDEREGÅENDE UDDANNELSER                           , 61=50+60 MELLEMLANGE VIDEREGÅENDE UDDANNELSER INKL. BACHELOR, 65=65 LANGE VIDEREGÅENDE UDDANNELSER                           , 9=Uoplyst]
- indkomsttype: values [100=1 Disponibel indkomst (2+30-31-32-35), 105=2 Indkomst i alt, før skatter mv. (3+7+22+26+29), 110=3 Erhvervsindkomst (4+5+6), 115=4 Løn, 120=5 Virksomhedsoverskud ... 270=35 Betalt underholdsbidrag, 275=Ækvivaleret disponibel indkomst, 280=Ejendomsskat (grundskyld), boligejere, 285=Ejendomsskat (grundskyld), lejere, 290=Skattepligtig indkomst]
- tid: date range 2004-01-01 to 2023-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at all three levels (1=5 regioner, 2=~11 landsdele, 3=~98 kommuner). Always filter WHERE d.niveau=... when joining — mixing levels silently double-counts.
- omrade='0' is national aggregate, not in dim.nuts.
- uddniv is inline (7 categories including uoplyst=9). Note the raw kode values have trailing whitespace (e.g., '10   ').
- enhed selector (4 types). Always filter to one.
- indkomsttype is hierarchical — pick one specific type.
- Only goes back to 2004 (education data limitation).
- Map: context/geo/kommuner.parquet (niveau 3), context/geo/landsdele.parquet (niveau 2), or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade=0.
