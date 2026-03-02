table: fact.sygind
description: Lægebesøg efter nøgletal, ydelsesart, indkomstniveau, køn, alder og tid
measure: indhold (unit -)
columns:
- bnogle: values [1000=Kontakter (gennemsnitligt antal pr. person), 1010=Personer med kontakt (pct.)]
- ydelsesart: values [120=I ALT, 130=ALMEN LÆGE I ALT, 140=Almen læge, konsultation, dagtid, 150=Almen læge, konsultation, aften mv., 151=Almen læge, besøg, dagtid ... 270=KIROPRAKTIK, 280=FYSIOTERAPI, 290=FODTERAPI, 300=PSYKOLOGHJÆLP, 320=ØVRIGE YDELSER]
- indkn: values [0KV=Alle kvartiler, 1KV=1. kvartil, 2KV=2. kvartil, 3KV=3. kvartil, 4KV=4. kvartil]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [IALT=Alder i alt, 0-9=0-9 år, 10-17=10-17 år, 18-29=18-29 år, 30-59=30-59 år, 60-=60 år og derover]
- tid: date range 2006-01-01 to 2024-01-01
notes:
- bnogle is a measurement selector (1000=average contacts per person, 1010=% with contact). Never aggregate across bnogle values.
- indkn income quartiles: 0KV=all quartiles (total), 1KV=lowest 25%, 4KV=highest 25%. These quartiles are mutually exclusive and sum to the total.
- ydelsesart is hierarchical (120=I ALT grand total). Do not sum all ydelsesart values.
- No regional breakdown. Available from 2006.
