table: fact.aku110k
description: Arbejdsmarkedstilknytning efter beskæftigelsesstatus, alder, køn og tid
measure: indhold (unit 1.000 personer)
columns:
- beskstatus: values [BESTOT=Beskæftigede, AKUL=AKU-ledige, UARBST=Uden for arbejdsstyrken]
- alder: values [TOT=Alder i alt, 1524=15-24 år, 2534=25-34 år, 3544=35-44 år, 4554=45-54 år, 5564=55-64 år, 6574=65-74 år]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- tid: date range 2008-01-01 to 2025-04-01