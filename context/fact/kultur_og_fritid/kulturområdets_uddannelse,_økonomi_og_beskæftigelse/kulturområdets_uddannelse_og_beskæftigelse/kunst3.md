table: fact.kunst3
description: Kunstnere efter kunstområde, indkomstgrundlag, aldersgruppe og tid
measure: indhold (unit Antal)
columns:
- kunstomr: values [TOTK=Kunstområde i alt, 1000=Musik, 1010=Forfattere og ord, 1020=Billedkunst og formgivere, 1030=Film og TV, 1040=Skuespil og scenekunst]
- indgrund: values [2000=75-100 pct. af indkomst fra kunstnerisk virke, 2010=25-74 pct. af indkomst fra kunstnerisk virke, 2020=1-24 pct. af indkomst fra kunstnerisk virke, 2030=Underviser i kunstneriske fag, 2040=Studerende, 2050=Øvrige]
- agebygroup: values [TOT=Alder i alt, 0029=Under 30 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6069=60-69 år, 7099=70 år og derover]
- tid: date range 2022-01-01 to 2022-01-01

notes:
- Only covers a single year (2022).
- indgrund has 6 mutually exclusive income-share categories — no total row. Summing all gives total artist count.
- kunstomr=TOTK and agebygroup=TOT are aggregate totals; filter when drilling down.