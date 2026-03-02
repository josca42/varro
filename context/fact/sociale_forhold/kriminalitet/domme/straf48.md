table: fact.straf48
description: Gennemsnitlig straflængde(mdr.) for betingede frihedsstraffe efter køn, alder, overtrædelsens art, afgørelsestype og tid
measure: indhold (unit Antal)
columns:
- koen: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, UA=Uoplyst alder, 15=15 år, 16=16 år, 17=17 år, 18=18 år, 19=19 år, 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 60-69=60-69 år, 70-79=70-79 år, 80-=80 år og derover]
- overtraed: join dim.overtraedtype on overtraed=kode::text [approx]; levels [1, 2, 3]
- afgorelse: values [0=Afgørelsestype i alt, 121=121 Betinget dom alene, 122=122 Betinget dom og samfundstjeneste, 123=123 Betinget dom og bøde, 124=124 Betinget dom, bøde og samfundstjeneste]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/overtraedtype.md

notes:
- indhold is AVERAGE sentence length in months, NOT a count. Do NOT sum — aggregate using AVG or report as-is.
- Covers only betingede (conditional) sentences. afgorelse: 0 = I alt (all conditional), 121-124 = specific conditional types.
- overtraed joins dim.overtraedtype at niveaux 1, 2, 3 (same as straf47/49). TOT is the only unmatched aggregate code.
- No regional breakdown (unlike straf46). No VIRKSOMHEDER in koen (only TOT/M/K).