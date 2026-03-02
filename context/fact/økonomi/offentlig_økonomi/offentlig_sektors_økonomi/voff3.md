table: fact.voff3
description: Versionstabel OFF3 - Offentlig forvaltning og service, udgifter og indtægter efter version, udgifter/indtægter, sektor og tid
measure: indhold (unit Mio. kr.)
columns:
- version: values [OFF2025_JUN=Juniversion 2025 (2021-2024), OFF2025_MAR=Martsversion 2025 (2024), OFF2024_JUN=Juniversion 2024 (1971-2023) Hovedrevision 2024, OFF2024_MAR=Martsversion 2024 (2023), OFF2023_SEP=Septemberversion 2023 (2022) ... OFF2015_NOV=Novemberversion 2015 (2012-2014), OFF2015_JUN=Juniversion 2015 (2014), OFF2015_MAR=Martsversion 2015 (2014), OFF2014_NOV=Novemberversion 2014 (2011-2013), OFF2014_SEP=Septemberversion 2014 (1971-2013) Hovedrevision 2014]
- ui: values [1.1=1.1. Aflønning af ansatte, 1.2=1.2. Forbrug i produktionen, 1.3=1.3. Andre produktionsskatter, 1.4=1.4. Sociale ydelser i naturalier, 1.5=1.5. Renter mv. ... 2.15.3.2=2.15.3.2. Udland i øvrigt, 2.16=2.16. Kapitalindtægter i alt (14+15), 2.17=2.17. Drifts- og kapitalindtægter i alt (13+16), 2.18=2.18. Driftsoverskud=bruttoopsparing (2.13-1.8), 2.19=2.19. Offentlig saldo=fordringserhvervelse, netto (2.17-1.17)]
- sektor: values [TOTAL=Offentlig forvaltning og service, S=Stat, F=Sociale kasser og fonde, K+R=Kommuner og regioner, R=Regioner, K=Kommuner]
- tid: date range 1971-01-01 to 2024-01-01
notes:
- version: Each version is an alternative estimate covering specific years (shown in its titel, e.g. OFF2025_JUN covers 2021–2024). For current best estimates, filter to the most recent version. Never sum across versions — they are revisions of the same years, not cumulative.
- ui and sektor are structurally identical to off3: hierarchical account codes with aggregate rows, sektor TOTAL aggregates subsectors. See off3 notes.
