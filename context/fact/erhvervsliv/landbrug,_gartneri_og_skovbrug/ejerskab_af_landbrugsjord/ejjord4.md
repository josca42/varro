table: fact.ejjord4
description: Ejerskab af dansk landbrugsjord efter ejers alder, enhed, land og tid
measure: indhold (unit -)
columns:
- ejalder: values [TOT=Alder i alt, 9925=Under 25 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4044=40-44 år, 4549=45-49 år, 5054=50-54 år, 5559=55-59 år, 6064=60-64 år, 6569=65-69 år, 7000=70-74 år, 75OV=75 år og derover, 9988=Uoplyst eller ikke personligt ejerskab]
- tal: values [100=Ejerskab af landbrugsjord (antal), 110=Areal (ha)]
- land: values [0=Lande i alt, 10=Udlandet i alt, 12=EU, 15=Danmark, 20=Tyskland, 25=Nederlandene, 30=Europa uden for EU, 35=Verden udenfor Europa, 40=Asien, 45=Amerika, 50=Afrika og Oceanien, 55=Uoplyst]
- tid: date range 2022-01-01 to 2024-01-01

notes:
- tal is a measurement selector — filter to '100' (antal) or '110' (areal i ha). Never sum across both.
- ejalder=TOT is the grand total. All other values (9925, 2529, …, 75OV, 9988) are mutually exclusive and sum to TOT.
- ejalder=9988 (Uoplyst eller ikke personligt ejerskab) is a large category — ~28k of 174k ownerships (16%) in 2024. These are corporate/institutional owners (selskaber, fonde, etc.) that have no personal age. When analysing age distribution of individual owners, note that 9988 represents non-personal ownership, not missing data, and should typically be excluded or reported separately.
- land hierarchy is non-additive — land=12 (EU) includes Denmark. Use land='0' for all, land='15' for Danish owners, land='10' for foreign.
- Only available from 2022 (2 data points). For longer trends use ejjord2 (ejerform) or ejjord3 (arealstor) which go back to 2020.