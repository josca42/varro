table: fact.frgnsk25
description: Befolkningens udvikling efter bevægelsesart, alder, køn og tid
measure: indhold (unit Antal)
columns:
- bevaegelse: values [B01A=Befolkningen ultimo forrige år, B02=Levendefødte, B03=Døde, B08A=Indvandret i indeværende år, B09A=Udvandret i indeværende år, B12=Korrektioner, B20A=Befolkningen ultimo indeværende år]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- kon: values [M=Mænd, K=Kvinder]
- tid: date range 1992-01-01 to 2024-01-01