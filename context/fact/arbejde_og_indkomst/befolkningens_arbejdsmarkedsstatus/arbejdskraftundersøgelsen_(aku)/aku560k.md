table: fact.aku560k
description: Arbejdskraftreserven efter arbejdsmarkedstilknytning, køn, enhed og tid
measure: indhold (unit Pct.)
columns:
- arbknyt: values [A5=1-4 Arbejdskraftreserven, i alt, A1=1. Deltidsbeskæftigede, der ønsker flere timer , A2=2. AKU-Ledige (søger arbejde, og kan starte med det samme) , A3=3. Søger arbejde, men kan ikke starte med det samme , A4=4. Kan starte med det samme, men søger ikke arbejde]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- enhed: values [22=Procent af arbejdsstyrken, 32=Procent af den udvidede arbejdsstyrke]
- tid: date range 2008-01-01 to 2025-04-01

notes:
- ALWAYS filter enhed to one value: 22=% of labour force (arbejdsstyrken) or 32=% of extended labour force (den udvidede arbejdsstyrke). These two percentages have different denominators.
- arbknyt: A5 is the total of A1-A4. Note A6 is absent from aku560k (only present in aku550k count table).
- For counts in thousands instead of percentages, use aku550k.