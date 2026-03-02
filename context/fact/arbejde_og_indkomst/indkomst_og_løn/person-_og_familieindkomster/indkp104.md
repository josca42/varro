table: fact.indkp104
description: Personindkomster efter landsdel, enhed, køn, socioøkonomisk status, indkomsttype og tid
measure: indhold (unit -)
columns:
- landdel: join dim.nuts on landdel=kode; levels [2]
- enhed: values [101=Personer med indkomsttypen (antal), 110=Indkomstbeløb (1.000 kr.), 116=Gennemsnit for alle personer (kr.), 121=Gennemsnit for personer med indkomsttypen (kr.)]
- koen: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- socio: join dim.socio on socio=kode; levels [3]
- indkomsttype: values [100=1 Disponibel indkomst (2+30-31-32-35), 105=2 Indkomst i alt, før skatter mv. (3+7+22+26+29), 110=3 Erhvervsindkomst (4+5+6), 115=4 Løn, 120=5 Virksomhedsoverskud ... 270=35 Betalt underholdsbidrag, 275=Ækvivaleret disponibel indkomst, 280=Ejendomsskat (grundskyld), boligejere, 285=Ejendomsskat (grundskyld), lejere, 290=Skattepligtig indkomst]
- tid: date range 1994-01-01 to 2023-01-01
dim docs: /dim/nuts.md, /dim/socio.md
notes:
- landdel joins dim.nuts at niveau 2 only (landsdele). landdel='0' is national aggregate, not in dim.
- socio joins dim.socio at niveau 3, but three codes are NOT in dim.socio: 100, 115, 130. These are custom aggregates added by DST (likely: 100=selvstændige inkl. medarbejdende ægtefælle, 115=selvstændige med ansatte, 130=lønmodtagere i alt). An INNER JOIN silently drops them — use LEFT JOIN or filter by kode value directly if you need them.
- enhed selector (4 types). Always filter to one.
- indkomsttype is hierarchical — pick one specific type, never sum across types.
- koen='MOK' is total.
- Map: context/geo/landsdele.parquet — merge on landdel=dim_kode. Exclude landdel=0.
