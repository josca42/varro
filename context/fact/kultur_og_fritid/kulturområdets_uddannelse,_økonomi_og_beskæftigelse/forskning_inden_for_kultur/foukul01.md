table: fact.foukul01
description: Udgifter i den offentlige sektor til Forskning og Udvikling i kulturen efter fagområde, udgifter og tid
measure: indhold (unit 1.000 kr.)
columns:
- fagomr: values [1000=Kultur i alt, 1010=byplanlægning, fysisk planlægning, 1020=medier og kommunikation, 1030=historie, 1040=arkæologi, 1050=sprogvidensk., filologi, 1060=litteraturvidenskab, 1070=filosofi, idehistorie, 1080=teologi, 1090=musik, teatervidenskab, 1100=kunst- og arkitekturvidenskab, 1110=film- og medievidenskab, 1120=øvrig humanistisk videnskab]
- udgift: values [10=Udgifter til egen FoU, 20=Driftsudgifter, 30=Anlægsudgifter]
- tid: date range 2007-01-01 to 2023-01-01

notes:
- udgift=10 (Udgifter til egen FoU) is the total = udgift=20 (Driftsudgifter) + udgift=30 (Anlægsudgifter). Filter to udgift=10 for total expenditure. Summing all three values triples the count.
- fagomr=1000 (Kultur i alt) is the aggregate of all sub-fields (1010–1120). Use fagomr=1000 for overall totals, or exclude it (WHERE fagomr != 1000) when breaking down by field.
- Unit is 1.000 kr. — divide by 1000 to get millions.
- Example — total R&D expenditure in culture 2023: SELECT indhold FROM fact.foukul01 WHERE tid='2023-01-01' AND udgift=10 AND fagomr=1000