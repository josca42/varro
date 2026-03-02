table: fact.kunst6a
description: Kunstneres indkomst efter kunstområde, væsentligste indkomstkilde, køn, prisenhed, enhed og tid
measure: indhold (unit -)
columns:
- kunstomr: values [TOTK=Kunstområde i alt, 1000=Musik, 1010=Forfattere og ord, 1020=Billedkunst og formgivere, 1030=Film og TV, 1040=Skuespil og scenekunst]
- vindkomst: values [3000=Væsentligste indkomstkilder i alt, 3010=Løn, 3020=Kombination af indkomstkilder, 3030=Offentlige ydelser og pension]
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- prisenhed: values [5=Faste priser (seneste dataårs prisniveau), 6=Nominelle priser]
- enhed: values [3040=Indkomst, før skatter - gennemsnit (kr.), 3050=Indkomst, før skatter - median (kr.), 3060=Indkomst, før skatter - nedre kvartilgrænse (kr.), 3070=Indkomst, før skatter - øvre kvartilgrænse (kr.), 3080=Indtægtskilder - gennemsnit (antal), 3090=Personer (antal)]
- tid: date range 2019-01-01 to 2023-01-01

notes:
- CRITICAL: enhed and prisenhed are measurement selectors — every dimension combination is repeated 12 times (6 enhed × 2 prisenhed). Always filter both to a single value.
- enhed selects what indhold means: 3040=mean income (kr.), 3050=median income (kr.), 3060=lower quartile (kr.), 3070=upper quartile (kr.), 3080=mean number of income sources (count), 3090=person count. These are completely different quantities — never sum across enhed values.
- prisenhed: 5=fixed prices (latest year's level), 6=nominal prices. For time series, prefer fixed prices (5). For a single year, both are identical.
- For number of artists: filter enhed=3090, prisenhed=5 (or 6; same result for counts).
- vindkomst=3000 is the total across all income sources; filter when examining specific income types.