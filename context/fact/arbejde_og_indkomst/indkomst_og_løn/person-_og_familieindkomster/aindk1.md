table: fact.aindk1
description: A-indkomst efter område, enhed, køn, indkomsttype og tid
measure: indhold (unit -)
columns:
- omrade: join dim.nuts on omrade=kode; levels [2, 3]
- enhed: values [101=Personer med indkomsttypen (antal), 110=Indkomstbeløb (1.000 kr.), 116=Gennemsnit for alle personer (kr.), 121=Gennemsnit for personer med indkomsttypen (kr.)]
- koen: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- indkomsttype: values [11000=1 A-skattepligtig indkomst i alt  (2+5+11+17+18), 11025=2 Samlet løn, 11050=3 Privat- og arbejdsmarkedspensioner (14+15+16), 11075=4 Offentlige overførsler i alt (5+12+13), 11100=5 Dagpenge og kontanthjælp i alt (6+7+8+9+10) ... 11400=17 Stipendier (SU), 11425=18 Anden A-indkomst, 11450=19 A-skat, 11475=20 Arbejdsmarkedsbidrag, 11500=21 Udbetalt A-indkomst(1-19-20)]
- tid: date range 2012-01-01 to 2024-01-01
dim docs: /dim/nuts.md
notes:
- omrade joins dim.nuts at levels 2 (landsdele) and 3 (kommuner). Filter WHERE d.niveau=... when joining.
- omrade='0' is national aggregate, not in dim.nuts.
- indkomsttype here uses a completely different coding scheme (11000-11500 series, not the 100-290 series in indkp/indkf tables). It is still hierarchical — e.g. 11000=A-skattepligtig indkomst i alt (=2+5+11+17+18). Never sum across types.
- enhed selector (4 types). Always filter to one.
- koen='MOK' is total. Only from 2012 — covers only A-indkomst (employer-reported income to SKAT), not all income types.
- aindk3 covers udbetalt A-indkomst (after A-skat and arbejdsmarkedsbidrag) — same structure as aindk1.
- Map: /geo/kommuner.parquet (niveau 3) or /geo/landsdele.parquet (niveau 2) — merge on omrade=dim_kode. Exclude omrade=0.
