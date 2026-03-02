table: fact.straf47
description: Ubetingede frihedsstraffe efter område, køn, alder, overtrædelsens art, afgørelsestype, straflængde og tid
measure: indhold (unit Antal)
columns:
- omrade: join dim.nuts on omrade=kode [approx]; levels [1, 3]
- koen: values [TOT=I alt, M=Mænd, K=Kvinder, VIRKSOMHEDER=Virksomheder]
- alder: values [TOT=Alder i alt, UA=Uoplyst alder, 15=15 år, 16=16 år, 17=17 år, 18=18 år, 19=19 år, 20=20 år, 21=21 år, 22=22 år, 23=23 år, 24=24 år, 25-29=25-29 år, 30-39=30-39 år, 40-49=40-49 år, 50-59=50-59 år, 60-69=60-69 år, 70-79=70-79 år, 80-=80 år og derover]
- overtraed: join dim.overtraedtype on overtraed=kode::text [approx]; levels [1, 2, 3]
- afgorelse: values [0=Afgørelsestype i alt, 111=111 Ubetinget dom alene, 112=112 Delvis betinget dom, 113=113 Delvis betinget og samfundstjeneste, 114=114 Ubetinget dom og bøde, 115=115 Udstået ved varetægt, 116=116 Forvaring, 117=117 Ubetinget dom og samfundstjeneste, 118=118 Ungdomssanktioner]
- straflang: values [TOTUB=Ubetinget i alt, 1-14=Op til 14 dage, 15-21=15 - 21 dage, 22-30=22 - 30 dage, 31-60=31 - 60 dage ... 2161-2880=>6 - 8 år, 2881-4320=>8 - 12 år, 4321-8999=>12 år -, 9999=Livstid, 9000=Uoplyst straflængde]
- tid: date range 2007-01-01 to 2024-01-01
dim docs: /dim/nuts.md, /dim/overtraedtype.md

notes:
- Covers only ubetingede (unconditional) sentences. afgorelse restricted to 0 (I alt) and 111-118 (specific unconditional types). 9999=Livstid is a straflang value (not afgorelse).
- overtraed joins dim.overtraedtype at niveaux 1 (3 codes), 2 (4 codes), 3 (80 codes). TOT is the only unmatched code (aggregate, not in dim) — filter overtraed != 'TOT' when joining. Use ColumnValues("overtraedtype", "titel", for_table="straf47") to browse.
- straflang: TOTUB = ubetinget i alt (aggregate), bands in days (1-14 up to 4321-8999), plus 9999=Livstid and 9000=Uoplyst. Filter straflang='TOTUB' for totals.
- omrade: same as straf44/46 — niveaux 1 and 3, omrade='0' = I alt (103 distinct values in this table), '998' = Uoplyst.
- koen includes VIRKSOMHEDER (note: column is koen, not kon as in straf40/44).
- Two dim joins (omrade + overtraed) plus straflang — filter all aggregates to get leaf-level counts.
- Map: context/geo/kommuner.parquet (niveau 3) or context/geo/regioner.parquet (niveau 1) — merge on omrade=dim_kode. Exclude omrade IN ('0', '998'). Kommune data can also be aggregated to 12 politikredse via dim.politikredse (niveau 2 koder match dim.nuts niveau 3; parent_kode → politikredsgrænser in context/geo/politikredse.parquet).