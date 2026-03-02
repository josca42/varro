table: fact.aku540a
description: Sammensætning af AKU-ledighed efter rådighedsniveau, ydelsestype og tid
measure: indhold (unit 1.000 personer)
columns:
- raadniveau: values [TOT=Hele befolkningen (15-64-årige), BESK=Beskæftigede , IBESK=Ikke beskæftigede, SOEG=Ikke beskæftigede, der søger arbejde, EJS=Ikke beskæftigede, der ikke søger arbejde, VARS=Ikke beskæftigede, der søger arbejde og har mulighed for at starte, SEN=Ikke beskæftigede, der søger arbejde men ikke har mulighed for at starte]
- ydelsestype: values [TOT1=I alt, UDK=Modtager dagpenge eller kontanthjælp, UAKT=Aktiverede, USTUD=Studerende, UOEVR=Resten af befolkningen]
- tid: date range 2008-01-01 to 2024-01-01

notes:
- raadniveau is a hierarchy: TOT > BESK/IBESK > SOEG/EJS > VARS/SEN. Never sum across levels. For the total, use raadniveau='TOT'. To drill into the unemployed, use IBESK, then SOEG/EJS.
- ydelsestype='TOT1' (note: code is TOT1, not TOT) for the overall total. Cross-tab with ydelsestype to see how AKU-ledige distribute across benefit types.
- Annual data only (ends 2024). This is the most detailed unemployment decomposition table in the AKU series.