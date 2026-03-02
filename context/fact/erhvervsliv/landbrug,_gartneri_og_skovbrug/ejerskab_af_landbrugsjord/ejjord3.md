table: fact.ejjord3
description: Ejerskab af dansk landbrugsjord efter arealstørrelse, enhed, land og tid
measure: indhold (unit -)
columns:
- arealstor: values [E000=Hektar i alt, E005=Mindre end 0,5 ha, E010=0,5-0,9 ha, E015=1-1,9 ha, E020=2-4,9 ha ha, E025=5-9,9 ha, E030=10-19,9 ha, E035=20-49,9 ha, E040=50-74,9 ha, E045=75-99,9 ha, E050=Større end eller lig med100 ha]
- tal: values [100=Ejerskab af landbrugsjord (antal), 110=Areal (ha)]
- land: values [0=Lande i alt, 10=Udlandet i alt, 12=EU, 15=Danmark, 20=Tyskland, 25=Nederlandene, 30=Europa uden for EU, 35=Verden udenfor Europa, 40=Asien, 45=Amerika, 50=Afrika og Oceanien, 55=Uoplyst]
- tid: date range 2020-01-01 to 2024-01-01

notes:
- tal is a measurement selector — filter to '100' (antal ejerskaber) or '110' (areal i ha). Never sum across both.
- arealstor=E000 (Hektar i alt) is the grand total. The 10 size brackets (E005–E050) are mutually exclusive and sum exactly to E000. For a breakdown, filter arealstor != 'E000'.
- land hierarchy is non-additive — land=12 (EU) includes Denmark. Use land='0' for all, land='15' for Danish owners only, land='10' for foreign only.
- Note the label typo in E020: "2-4,9 ha ha" — the value is correct (2–4.9 ha), just the label repeats "ha".