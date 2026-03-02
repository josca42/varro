table: fact.best16
description: Bestyrelsesmedlemmer efter bestyrelsespost, køn, uddannelse, alder og tid
measure: indhold (unit Antal)
columns:
- bestpost: values [1=1 bestyrelsespost, 2=2 bestyrelsesposter, 3=3 bestyrelsesposter, 4=4 bestyrelsesposter, 5=5 eller flere bestyrelsesposter]
- kon: values [100=Køn i alt, 200=Mænd, 300=Kvinder, 400=Uoplyst køn]
- uddannelse: values [TOT=I alt uddannelser, H10=Grundskole, H20=Gymnasiale uddannelser mv., H30=Erhvervsfaglige uddannelser, H40=Korte videregående uddannelser, H5060=Mellemlange videregående- og bacheloruddannelser, H70=Lange videregående uddannelser mv., H90=Uoplyst]
- alder: values [IALT=Alder i alt, U20=Under 20 år, 2029=20-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 70OV=70 år og derover, UK=Ukendt alder]
- tid: date range 2023-01-01 to 2023-01-01

notes:
- Only covers 2023.
- bestpost = number of board positions held by a person (1, 2, 3, 4, 5+). These are mutually exclusive categories — summing indhold across bestpost gives the total number of board members. To get total board seats, multiply indhold by bestpost value for each row (and use 5 as a minimum for the last category).
- No "I alt" row for bestpost — the total is the sum across all 5 categories. Filter kon='100', uddannelse='TOT', alder='IALT' to get aggregate totals.