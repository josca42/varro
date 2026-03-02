table: fact.strfudd1
description: Skyldige personer i alderen 15-79 år efter køn, alder, uddannelse og tid
measure: indhold (unit Antal)
columns:
- koen: values [M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 15-29=15-29 år, 30-49=30-49 år, 50-79=50-79 år]
- uddannelse: values [TOT=I alt, 10=Grundskole, 20=Gymnasial uddannelse, 35=Erhvervsuddannelse, 40=Videregående uddannelse, 00=Uoplyst uddannelse]
- tid: date range 2015-01-01 to 2023-01-01
notes:
- uddannelse: TOT=I alt is the aggregate. The 5 substantive categories (Grundskole, Gymnasial, Erhvervsuddannelse, Videregående, Uoplyst) are mutually exclusive and sum to TOT. Filter to TOT for overall or to all 5 for breakdown.
- koen has only M and K — no total row. Sum M+K for total.
- alder TOT is aggregate — filter to one level.
