table: fact.indkp109
description: Indkomster for personer over 14 år efter region/landsdel, enhed, køn, alder, herkomst, indkomsttype og tid
measure: indhold (unit -)
columns:
- regland: join dim.nuts on regland=kode; levels [1, 2]
- enhed: values [101=Personer med indkomsttypen (antal), 110=Indkomstbeløb (1.000 kr.), 116=Gennemsnit for alle personer (kr.), 121=Gennemsnit for personer med indkomsttypen (kr.)]
- koen: values [MOK=Mænd og kvinder i alt, M=Mænd, K=Kvinder]
- alder1: values [TOT=Alder i alt, UN29=Under 29 år, 3049=30-49 år, 50OV=50 år og derover]
- herkomst: join dim.herkomst on herkomst=kode::text [approx]
- indkomsttype: values [100=1 Disponibel indkomst (2+30-31-32-35), 105=2 Indkomst i alt, før skatter mv. (3+7+22+26+29), 110=3 Erhvervsindkomst (4+5+6), 115=4 Løn, 120=5 Virksomhedsoverskud ... 270=35 Betalt underholdsbidrag, 275=Ækvivaleret disponibel indkomst, 280=Ejendomsskat (grundskyld), boligejere, 285=Ejendomsskat (grundskyld), lejere, 290=Skattepligtig indkomst]
- tid: date range 2008-01-01 to 2024-01-01
dim docs: /dim/herkomst.md, /dim/nuts.md
notes:
- regland joins dim.nuts at levels 1 (5 regioner) and 2 (landsdele). Filter WHERE d.niveau=... when joining. regland='0' is national aggregate, not in dim.
- herkomst does NOT join dim.herkomst. The fact table uses text codes (ALLE, DANSK, EFT_ALLE, EFT_ANDRE, EFT_VEST, IND_ALLE, IND_ANDRE, IND_VEST) while dim.herkomst uses numeric codes (1=dansk oprindelse, 2=indvandrere, 3=efterkommere). Treat herkomst as inline: DANSK=dansk oprindelse, IND_ALLE=alle indvandrere, IND_VEST=vestlige, IND_ANDRE=ikke-vestlige, EFT_*=efterkommere equivalents.
- alder1 has only 4 coarse age groups (TOT, UN29, 3049, 50OV) — use indkp111 for 5-year age detail.
- enhed selector (4 types). Always filter to one.
- indkomsttype is hierarchical — pick one specific type.
- Only goes back to 2008.
- Map: context/geo/regioner.parquet (niveau 1) or context/geo/landsdele.parquet (niveau 2) — merge on regland=dim_kode. Exclude regland=0.
