table: fact.straf46
description: Betingede frihedsstraffe efter område, køn, alder, overtrædelsens art, afgørelsestype, straflængde og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 3]
- koen: values [TOT=I alt, M=Mænd, K=Kvinder, VIRKSOMHEDER=Virksomheder]
- alder: values [TOT=Alder i alt, UA=Uoplyst alder, 15=15 år, 16=16 år, 17=17 år, 18=18 år, 19=19 år, 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 60-69=60-69 år, 70-79=70-79 år, 80-=80 år og derover]
- overtraed: values [TOT=Overtrædelsens art i alt, 1=Straffelov i alt, 1000=Uoplyst straffelov, 11=Seksualforbrydelser i alt, 1110=Blodskam mv. ... 3845=Love vedrørende forsvaret o.l., 3850=Love vedrørende offentlige forsyninger, 3855=Love vedrørende spil, bevilling, næring, 3865=Særlovgivning i øvrigt, 3870=Uoplyst særlovgivning]
- afgorelse: values [0=Afgørelsestype i alt, 121=121 Betinget dom alene, 122=122 Betinget dom og samfundstjeneste, 123=123 Betinget dom og bøde, 124=124 Betinget dom, bøde og samfundstjeneste]
- straflang: values [TOTB=Betinget i alt, 1-14=Op til 14 dage, 15-21=15 - 21 dage, 22-30=22 - 30 dage, 31-60=31 - 60 dage, 61-90=>2 - 3 måneder, 91-120=>3 - 4 måneder, 121-180=>4 - 6 måneder, 181-270=>6 - 9 måneder, 271-360=>9 - 12 måneder, 361-450=>12 - 15 måneder, 451-540=>15 - 18 måneder, 541-720=>18 - 24 måneder, 721-1080=>2- 3 år, 1081-8999=> 3 år +, 9001=Straffastsættelse udsat, 9000=Uoplyst straflængde]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md

notes:
- Covers only betingede (conditional) sentences. afgorelse is restricted: 0 = I alt (all conditional), 121-124 = specific conditional types (betinget dom alene, +samfundstjeneste, +bøde, +bøde+samfundstjeneste). No other verdict types appear.
- straflang: TOTB = betinget i alt (aggregate), then bands in days (1-14, 15-21, ..., 1081-8999). 9001 = straffastsættelse udsat, 9000 = uoplyst. Filter straflang='TOTB' for totals.
- omrade: same as straf44 — niveaux 1 and 3, omrade='0' = I alt, '998' = Uoplyst.
- koen includes VIRKSOMHEDER. Note the column is called koen here (not kon as in straf40/44).
- Map: /geo/kommuner.parquet (niveau 3) or /geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade IN ('0', '998'). Kommune data can also be aggregated to 12 politikredse via dim.politikredse (niveau 2 koder match dim.nuts niveau 3; parent_kode → politikredsgrænser in /geo/politikredse.parquet).