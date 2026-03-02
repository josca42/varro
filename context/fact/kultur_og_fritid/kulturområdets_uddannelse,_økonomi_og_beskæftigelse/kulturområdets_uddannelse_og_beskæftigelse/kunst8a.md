table: fact.kunst8a
description: Kunstneres indkomst efter kunstområde, væsentligste indkomstkilde, indkomstgrundlag, prisenhed, enhed og tid
measure: indhold (unit -)
columns:
- kunstomr: values [TOTK=Kunstområde i alt, 1000=Musik, 1010=Forfattere og ord, 1020=Billedkunst og formgivere, 1030=Film og TV, 1040=Skuespil og scenekunst]
- vindkomst: values [3000=Væsentligste indkomstkilder i alt, 3010=Løn, 3020=Kombination af indkomstkilder, 3030=Offentlige ydelser og pension]
- indgrund: values [2000=75-100 pct. af indkomst fra kunstnerisk virke, 2010=25-74 pct. af indkomst fra kunstnerisk virke, 2020=1-24 pct. af indkomst fra kunstnerisk virke, 2050=Øvrige]
- prisenhed: values [5=Faste priser (seneste dataårs prisniveau), 6=Nominelle priser]
- enhed: values [3040=Indkomst, før skatter - gennemsnit (kr.), 3050=Indkomst, før skatter - median (kr.), 3060=Indkomst, før skatter - nedre kvartilgrænse (kr.), 3070=Indkomst, før skatter - øvre kvartilgrænse (kr.), 3080=Indtægtskilder - gennemsnit (antal), 3090=Personer (antal)]
- tid: date range 2019-01-01 to 2023-01-01

notes:
- CRITICAL: enhed and prisenhed are measurement selectors — every combination is repeated 12 times (6 enhed × 2 prisenhed). Always filter both.
- Same enhed and prisenhed semantics as kunst6a.
- indgrund has 4 categories (no 2030=Underviser or 2040=Studerende in this table, unlike kunst3). No total row for indgrund — sum across all for the complete artist population with each vindkomst.