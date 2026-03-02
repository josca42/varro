table: fact.sygher
description: Lægebesøg efter nøgletal, ydelsesart, herkomst, køn, alder og tid
measure: indhold (unit -)
columns:
- bnogle: values [1000=Kontakter (gennemsnitligt antal pr. person), 1010=Personer med kontakt (pct.)]
- ydelsesart: values [120=I ALT, 130=ALMEN LÆGE I ALT, 140=Almen læge, konsultation, dagtid, 150=Almen læge, konsultation, aften mv., 151=Almen læge, besøg, dagtid ... 270=KIROPRAKTIK, 280=FYSIOTERAPI, 290=FODTERAPI, 300=PSYKOLOGHJÆLP, 320=ØVRIGE YDELSER]
- herkomst: join dim.herkomst on herkomst=kode [approx]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [IALT=Alder i alt, 0-9=0-9 år, 10-17=10-17 år, 18-29=18-29 år, 30-59=30-59 år, 60-=60 år og derover]
- tid: date range 2006-01-01 to 2024-01-01
dim docs: /dim/herkomst.md
notes:
- herkomst uses a different coding scheme than dim.herkomst — the dim join will NOT work. The fact table uses: 0=I alt, 10=Dansk oprinding, 20=Indvandrere, 30=Efterkommere. dim.herkomst uses codes 1, 2, 3, 9 (×10). Query herkomst inline without a dim join.
- bnogle is a measurement selector (1000=average contacts per person, 1010=% with contact). Never aggregate across bnogle values.
- ydelsesart is hierarchical (120=I ALT grand total). Do not sum all ydelsesart values.
- No regional breakdown. Available from 2006 — the longest time series among the socioeconomic breakdown tables.
