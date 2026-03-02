table: fact.aku550k
description: Arbejdskraftreserven efter arbejdsmarkedstilknytning, køn, enhed og tid
measure: indhold (unit 1.000 personer)
columns:
- arbknyt: values [A5=1-4 Arbejdskraftreserven, i alt, A1=1. Deltidsbeskæftigede, der ønsker flere timer , A2=2. AKU-Ledige (søger arbejde, og kan starte med det samme) , A3=3. Søger arbejde, men kan ikke starte med det samme , A4=4. Kan starte med det samme, men søger ikke arbejde, A6=5. Vil have arbejde, men søger ikke og er ikke til rådighed]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- enhed: values [2=Personer, 12=Fuldtidsækvivalerede personer]
- tid: date range 2008-01-01 to 2025-04-01

notes:
- ALWAYS filter enhed to one value: 2=Persons (1.000 persons) or 12=Full-time equivalents. Mixing both doubles your count.
- arbknyt: A5 is the total of categories A1-A4 (the "labour reserve"). A6 (vil have arbejde, men søger ikke og er ikke til rådighed) is outside the labour reserve total — A5 does NOT include A6. To get total extended underemployment, sum A5+A6 or use a separate filter.
- kon=TOT for the gender total. Quarterly data to 2025.