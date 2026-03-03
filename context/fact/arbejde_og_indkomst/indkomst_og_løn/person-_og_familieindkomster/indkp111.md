table: fact.indkp111
description: Indkomster efter region/landsdel, enhed, køn, alder, indkomsttype og tid
measure: indhold (unit -)
columns:
- regland: join dim.nuts on regland=kode; levels [1, 2]
- enhed: values [101=Personer med indkomsttypen (antal), 110=Indkomstbeløb (1.000 kr.), 116=Gennemsnit for alle personer (kr.), 121=Gennemsnit for personer med indkomsttypen (kr.)]
- koen: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- alder1: values [00=I alt, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, 70-74=70-74 år, 74-00=Over 74 år]
- indkomsttype: values [100=1 Disponibel indkomst (2+30-31-32-35), 105=2 Indkomst i alt, før skatter mv. (3+7+22+26+29), 110=3 Erhvervsindkomst (4+5+6), 115=4 Løn, 120=5 Virksomhedsoverskud ... 270=35 Betalt underholdsbidrag, 275=Ækvivaleret disponibel indkomst, 280=Ejendomsskat (grundskyld), boligejere, 285=Ejendomsskat (grundskyld), lejere, 290=Skattepligtig indkomst]
- tid: date range 1992-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- regland joins dim.nuts at levels 1 (5 regioner) and 2 (landsdele). Filter WHERE d.niveau=... when joining. regland='0' is national aggregate, not in dim.
- alder1='00' is the total. Fine 5-year age groups from 15-19 to 74-00.
- enhed selector (4 types). Always filter to one.
- indkomsttype is hierarchical — pick one specific type.
- koen='MOK' is total. Goes back to 1992. Use this (not indkp109) when you need both region/landsdel and detailed age breakdown.
- Map: /geo/regioner.parquet (niveau 1) or /geo/landsdele.parquet (niveau 2) — merge on regland=dim_kode. Exclude regland=0.
