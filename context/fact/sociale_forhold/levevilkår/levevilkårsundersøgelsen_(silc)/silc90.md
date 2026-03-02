table: fact.silc90
description: Ugentlige timer i dagtilbud (0-12 år) efter baggrundsoplysninger, enhed og tid
measure: indhold (unit Timer)
columns:
- bagopl: values [TOT=I alt, REG81=Region Nordjylland, REG82=Region Midtjylland, REG83=Region Syddanmark, REG84=Region Hovedstaden, REG85=Region Sjælland, IND1=1. indkomstkvintil, IND2=2. indkomstkvintil, IND3=3. indkomstkvintil, IND4=4. indkomstkvintil, IND5=5. indkomstkvintil, BOL1=Ejerbolig, BOL2=Lejebolig, URB1=Tæt befolket område, URB2=Medium befolket område, URB3=Tyndt befolket område]
- enhed: values [GNS=Gennemsnit for befolkningen (16+ år), STDG=Standardfejl på gennemsnittet]
- tid: date range 2021-01-01 to 2024-01-01
notes:
- Measures average weekly hours children (0–12 år) spend in dagtilbud. enhed: GNS=Gennemsnit, STDG=Standardfejl. Always filter enhed='GNS' for the actual average.
- bagopl has 15 values covering region (REG81–85), income quintile (IND1–5), housing tenure (BOL1–2), and urbanization (URB1–3). No gender, age, or education breakdown. TOT for overall.
- Measure is average hours per week — not a percentage. Do not aggregate across bagopl.
- For national average hours in childcare by year: WHERE bagopl='TOT' AND enhed='GNS'.
