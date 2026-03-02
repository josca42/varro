table: fact.strafna3
description: Skyldige personer efter køn, alder, oprindelsesland og tid
measure: indhold (unit Antal)
columns:
- koen: values [M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 15-29=15-29 år, 30-49=30-49 år, 50-79=50-79 år]
- ieland: values [0=I alt, 5100=Danmark, 5126=Belgien, 5754=Bosnien-Hercegovina, 5128=Bulgarien ... 5468=Vietnam, 5502=Australien, 7100=Øvrige lande i alt, 7200=Øvrige lande, vestlige, 7300=Øvrige lande, ikke-vestlige]
- tid: date range 2000-01-01 to 2023-01-01
notes:
- koen has only M and K — no total row. Sum M+K for total counts.
- alder: TOT is the aggregate of the three age bands (15-29, 30-49, 50-79). Filter to TOT for overall count or to individual bands for breakdown — never mix.
- ieland is a long list (~50+ countries) plus aggregate codes: 0=I alt (all countries), 7100=Øvrige lande i alt, 7200=Øvrige lande vestlige, 7300=Øvrige lande ikke-vestlige. These aggregate codes overlap individual country codes — pick one granularity. For Denmark only: ieland=5100. For overall total: ieland=0. Use ColumnValues("strafna3", "ieland") to browse the full list.
