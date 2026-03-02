table: fact.straf49
description: Gennemsnitlig straflængde (mdr.) for ubetingede frihedsstraffe efter køn, alder, overtrædelsens art, afgørelsestype og tid
measure: indhold (unit Antal)
columns:
- koen: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, UA=Uoplyst alder, 15=15 år, 16=16 år, 17=17 år, 18=18 år, 19=19 år, 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 60-69=60-69 år, 70-79=70-79 år, 80-=80 år og derover]
- overtraed: join dim.overtraedtype on overtraed=kode::text [approx]; levels [1, 2, 3]
- afgorelse: values [0=Afgørelsestype i alt, 111=111 Ubetinget dom alene, 112=112 Delvis betinget dom, 113=113 Delvis betinget og samfundstjeneste, 114=114 Ubetinget dom og bøde, 115=115 Udstået ved varetægt]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/overtraedtype.md

notes:
- indhold is AVERAGE sentence length in months, NOT a count. Do NOT sum — report or average as-is.
- Covers only ubetingede (unconditional) sentences. afgorelse: 0 = I alt, 111-115 = specific unconditional types (fewer than straf47's 111-118 range).
- overtraed joins dim.overtraedtype at niveaux 1, 2, 3 (same structure as straf47/48). TOT is unmatched aggregate.
- No regional breakdown (unlike straf47). No VIRKSOMHEDER in koen (only TOT/M/K).
- Pair with straf48 to compare average conditional vs unconditional sentence lengths by crime type.