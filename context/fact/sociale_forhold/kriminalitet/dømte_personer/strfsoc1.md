table: fact.strfsoc1
description: Skyldige personer efter køn, alder, socioøkonomisk status og tid
measure: indhold (unit Antal)
columns:
- koen: values [M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, 15-29=15-29 år, 30-49=30-49 år, 50-79=50-79 år]
- socio: join dim.socio on socio=kode::text [approx]; levels [3]
- tid: date range 2015-01-01 to 2023-01-01
dim docs: /dim/socio.md
notes:
- socio uses a simplified custom grouping, NOT the standard SOCIO13 hierarchy. Only 3 of 7 codes match dim.socio (111, 210, 310). Treat as inline categorical — do not join dim.socio for a full breakdown. The 7 values are: TOT=I alt, 111=Selvstændige, 200=Lønmodtagere, 210=Arbejdsløse, 310=Studerende, 315=Pensionister mv., 900=Øvrige personer.
- koen has only M and K — no total row. Sum M+K for total.
- alder TOT is the aggregate of the three age bands — filter to one level.
