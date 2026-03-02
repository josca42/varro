table: fact.aku520k
description: Registrerede ledige efter ydelsestype, beskæftigelsesstatus og tid
measure: indhold (unit 1.000 personer)
columns:
- ydelsestype: values [TOT=I alt, 160=Modtager dagpenge eller kontanthjælp, 166=Aktiverede]
- beskstatus: values [TOT=I ALT, BESTOT=Beskæftigede, AKUL=AKU-ledige, UARBST=Uden for arbejdsstyrken]
- tid: date range 2008-01-01 to 2025-04-01

notes:
- Both ydelsestype and beskstatus have total rows. For the overall count of registered unemployed, filter ydelsestype='TOT' AND beskstatus='TOT'.
- This table shows the AKU labour market status (employed, unemployed, outside labour force) of people who are registered as unemployed — useful for understanding how many registered unemployed are actually employed or outside the labour force by AKU definition.