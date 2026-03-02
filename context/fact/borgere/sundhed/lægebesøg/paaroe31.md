table: fact.paaroe31
description: Befolkningens kontakt til praktiserende læge (18 år eller derover) efter relation, nøgletal, alder, køn og tid
measure: indhold (unit -)
columns:
- parorendeforhold: values [PR810=Har en partner og ingen andre pårørende, PR820=Har en partner og andre pårørende, PR830=Har ingen partner, men har andre pårørende, PR840=Har hverken partner eller andre pårørende]
- bnogle: values [1000=Kontakter (gennemsnitligt antal pr. person), 1010=Personer med kontakt (pct.)]
- alerams: values [IALT=Alder i alt, 1829=18-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7079=70-79 år, 8099=80 år og derover]
- koen: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- tid: date range 2021-01-01 to 2024-01-01
notes:
- For adults 18+ years. parorendeforhold describes network structure (partner+others, partner only, others only, isolated). These are mutually exclusive categories covering all adults — they sum to the total.
- bnogle is a measurement selector (1000=avg contacts per person, 1010=% with contact). Never aggregate across bnogle values.
- koen uses 10=køn i alt, 1=mænd, 2=kvinder (not TOT/M/K).
- No regional breakdown. Only from 2021.
