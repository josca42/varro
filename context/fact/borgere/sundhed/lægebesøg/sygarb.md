table: fact.sygarb
description: Lægebesøg efter nøgletal, ydelsesart, arbejdsmarkedstilknytning, køn, alder og tid
measure: indhold (unit -)
columns:
- bnogle: values [1000=Kontakter (gennemsnitligt antal pr. person), 1010=Personer med kontakt (pct.)]
- ydelsesart: values [120=I ALT, 130=ALMEN LÆGE I ALT, 140=Almen læge, konsultation, dagtid, 150=Almen læge, konsultation, aften mv., 151=Almen læge, besøg, dagtid ... 270=KIROPRAKTIK, 280=FYSIOTERAPI, 290=FODTERAPI, 300=PSYKOLOGHJÆLP, 320=ØVRIGE YDELSER]
- arbknyt: values [3000=Studerende, personer under 15 år og øvrige personer, 3005=I beskæftigelse, 3010=Arbejdsløs, 3015=Langtidssyg, revalidering m.m., 3020=Førtidspensionist, 3025=Pensionist]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [IALT=Alder i alt, 0-9=0-9 år, 10-17=10-17 år, 18-29=18-29 år, 30-59=30-59 år, 60-=60 år og derover]
- tid: date range 2021-01-01 to 2024-01-01
notes:
- bnogle is a measurement selector — each row exists twice, once per bnogle value (1000=average contacts per person, 1010=% of persons with any contact). Never aggregate across bnogle values.
- arbknyt has no total row — categories are mutually exclusive but exhaustive. Summing all gives the national total.
- ydelsesart is hierarchical (120=I ALT grand total). Do not sum all ydelsesart values.
- No regional breakdown. Only available from 2021.
