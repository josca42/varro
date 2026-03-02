table: fact.strafna5
description: Skyldige personer efter oprindelsesland, afgørelsestype og tid
measure: indhold (unit Antal)
columns:
- ieland: values [0=I alt, 5100=Danmark, 5126=Belgien, 5754=Bosnien-Hercegovina, 5128=Bulgarien ... 5468=Vietnam, 5502=Australien, 7100=Øvrige lande i alt, 7200=Øvrige lande, vestlige, 7300=Øvrige lande, ikke-vestlige]
- afgorelse: values [11=11 Ubetinget frihedsstraf, 12=12 Betinget frihedsstraf, 2=2 Bødeafgørelse, 3=3 Tiltalefrafald, 4=4 Tiltale undladt, 5=5 Anden afgørelse, 511=511 Foranstaltningsdomme]
- tid: date range 2000-01-01 to 2023-01-01
notes:
- afgorelse has 7 verdict types — no total row. Sum all 7 for total convictions. Values: 11=Ubetinget frihedsstraf, 12=Betinget frihedsstraf, 2=Bødeafgørelse, 3=Tiltalefrafald, 4=Tiltale undladt, 5=Anden afgørelse, 511=Foranstaltningsdomme.
- CAUTION: strfna14 covers similar content (verdicts by statsb+herkomst) but uses a different afgorelse coding scheme (800-series codes). Do not mix code values across tables.
- ieland: 0=I alt (total), individual country codes, plus sub-aggregates 7100/7200/7300. Pick one granularity level. Use ColumnValues("strafna5", "ieland") to browse.
