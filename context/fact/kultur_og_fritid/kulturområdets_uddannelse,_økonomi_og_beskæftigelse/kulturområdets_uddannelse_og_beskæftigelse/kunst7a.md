table: fact.kunst7a
description: Kunstneres indkomst efter kunstområde, væsentligste indkomstkilde, aldersgruppe, prisenhed, enhed og tid
measure: indhold (unit -)
columns:
- kunstomr: values [TOTK=Kunstområde i alt, 1000=Musik, 1010=Forfattere og ord, 1020=Billedkunst og formgivere, 1030=Film og TV, 1040=Skuespil og scenekunst]
- vindkomst: values [3000=Væsentligste indkomstkilder i alt, 3010=Løn, 3020=Kombination af indkomstkilder, 3030=Offentlige ydelser og pension]
- agebygroup: values [TOT=Alder i alt, 0029=Under 30 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7099=70 år og derover]
- prisenhed: values [5=Faste priser (seneste dataårs prisniveau), 6=Nominelle priser]
- enhed: values [3040=Indkomst, før skatter - gennemsnit (kr.), 3050=Indkomst, før skatter - median (kr.), 3060=Indkomst, før skatter - nedre kvartilgrænse (kr.), 3070=Indkomst, før skatter - øvre kvartilgrænse (kr.), 3080=Indtægtskilder - gennemsnit (antal), 3090=Personer (antal)]
- tid: date range 2019-01-01 to 2023-01-01

notes:
- CRITICAL: enhed and prisenhed are measurement selectors — every combination is repeated 12 times (6 enhed × 2 prisenhed). Always filter both.
- Same enhed and prisenhed semantics as kunst6a: enhed values 3040–3090 cover mean/median/quartiles/count; prisenhed 5=fixed, 6=nominal.
- agebygroup=TOT is the total across all ages; filter when comparing age groups.