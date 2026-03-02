table: fact.ejjord5
description: Ejerskab af dansk landbrugsjord efter køn, enhed, land og tid
measure: indhold (unit -)
columns:
- kon: values [TOT=I alt, M=Mænd, K=Kvinder, UP=Uoplyst eller ikke personligt ejerskab]
- tal: values [100=Ejerskab af landbrugsjord (antal), 110=Areal (ha)]
- land: values [0=Lande i alt, 10=Udlandet i alt, 12=EU, 15=Danmark, 20=Tyskland, 25=Nederlandene, 30=Europa uden for EU, 35=Verden udenfor Europa, 40=Asien, 45=Amerika, 50=Afrika og Oceanien, 55=Uoplyst]
- tid: date range 2022-01-01 to 2024-01-01

notes:
- tal is a measurement selector — filter to '100' (antal) or '110' (areal i ha). Never sum across both.
- kon=TOT is the grand total. M + K + UP = TOT (all four values are mutually exclusive, UP is not a subset of M/K).
- kon=UP (Uoplyst eller ikke personligt ejerskab) is the same non-personal category as ejalder=9988 in ejjord4 — ~28k of 174k ownerships (16%) in 2024. These are corporate/fund/institutional owners with no gender. When comparing male vs female ownership, the correct denominator is M+K (or TOT−UP) rather than TOT.
- land hierarchy is non-additive — land=12 (EU) includes Denmark. Use land='0' for all, land='15' for Danish, land='10' for foreign.
- Only available from 2022 (2 data points). For longer trends use ejjord2 or ejjord3 which go back to 2020.