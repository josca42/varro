table: fact.ejjord2
description: Ejerskab af dansk landbrugsjord efter ejerform, enhed, land og tid
measure: indhold (unit -)
columns:
- ejerform: values [200=Alle ejerformer, 205=Privatpersoner, 210=Enkeltmandsvirksomheder, 215=Interessentskaber (I/S), 220=Selskaber, 225=Fonde, 230=Andre Ejerformer]
- tal: values [100=Ejerskab af landbrugsjord (antal), 110=Areal (ha)]
- land: values [0=Lande i alt, 10=Udlandet i alt, 12=EU, 15=Danmark, 20=Tyskland, 25=Nederlandene, 30=Europa uden for EU, 35=Verden udenfor Europa, 40=Asien, 45=Amerika, 50=Afrika og Oceanien, 55=Uoplyst]
- tid: date range 2020-01-01 to 2024-01-01

notes:
- tal is a measurement selector — filter to '100' (antal ejerskaber) or '110' (areal i ha). Never sum across both.
- ejerform=200 (Alle ejerformer) is the grand total. The remaining six categories (205–230) are mutually exclusive and sum to 200. For a breakdown, filter ejerform != '200'.
- land hierarchy is non-additive — see ejjord1 notes. land=12 (EU) includes Denmark. Use land='0' for all, land='15' for Danish owners only, land='10' for foreign owners only.
- Privatpersoner (205) dominate: ~158k of 174k total ownerships. Selskaber (220) own ~363k ha vs ~2.25M ha for privatpersoner — corporate owners hold land in fewer but larger parcels.