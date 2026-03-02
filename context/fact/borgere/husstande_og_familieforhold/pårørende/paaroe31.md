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
- bnogle is a measurement selector that doubles every row: 1000 = average contacts per person, 1010 = % of persons with any contact. Always filter to one. Mixing them makes no sense.
- parorendeforhold has 4 mutually exclusive categories for adults 18+: PR810 (partner, no other relatives), PR820 (partner + other relatives), PR830 (no partner, but has other relatives), PR840 (neither partner nor other relatives). These are mutually exclusive and can be summed for totals.
- koen has 10 (i alt), 1 (mænd), 2 (kvinder). alerams has IALT plus 7 age bands (18–29, …, 80+). Filter totals to avoid double-counting.
- The partner/relative categorisation here is the same parorendeforhold scheme used in paaroe50/51, so results can be compared to home care data for adults.