table: fact.kunst9
description: Kunstneres indkomst efter kunstområde, væsentligste indkomstkilde, uddannelsesniveau, enhed og tid
measure: indhold (unit -)
columns:
- kunstomr: values [TOTK=Kunstområde i alt, 1000=Musik, 1010=Forfattere og ord, 1020=Billedkunst og formgivere, 1030=Film og TV, 1040=Skuespil og scenekunst]
- vindkomst: values [3000=Væsentligste indkomstkilder i alt, 3010=Løn, 3020=Kombination af indkomstkilder, 3030=Offentlige ydelser og pension]
- uddniv: values [10=Grundskole, 20=Gymnasiale uddannelser, 30=Erhvervsfaglige uddannelser, 40=Korte videregående uddannelser, 51=Mellemlange videregående uddannelser inkl. bacheloruddannelser, 71=Lange videregående uddannelser inkl. ph.d. uddannelser, 90=Uoplyst]
- enhed: values [3040=Indkomst, før skatter - gennemsnit (kr.), 3050=Indkomst, før skatter - median (kr.), 3060=Indkomst, før skatter - nedre kvartilgrænse (kr.), 3070=Indkomst, før skatter - øvre kvartilgrænse (kr.), 3080=Indtægtskilder - gennemsnit (antal), 3090=Personer (antal)]
- tid: date range 2022-01-01 to 2022-01-01

notes:
- Only covers a single year (2022).
- CRITICAL: enhed is a measurement selector with 6 different quantities (3040=mean income, 3050=median, 3060/3070=quartiles, 3080=income sources count, 3090=person count). Always filter to a single enhed value.
- No prisenhed column (unlike kunst6a/7a/8a) — only single price basis.
- uddniv has 7 mutually exclusive education levels, no total row.