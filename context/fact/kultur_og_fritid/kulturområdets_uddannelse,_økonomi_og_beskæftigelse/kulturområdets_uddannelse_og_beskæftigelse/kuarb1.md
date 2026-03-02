table: fact.kuarb1
description: Ansatte på kulturarbejdspladser efter køn, kulturemne, uddannelse og tid
measure: indhold (unit Antal)
columns:
- kon: values [10=Køn i alt, 1=Mænd, 2=Kvinder]
- kulturemne: join dim.kulturemner on kulturemne::text=kode [approx: Fact uses numeric codes (1,8,20,29); dimension uses alphanumeric (K09,K10). Need to map numeric to Kxx format.]; levels [1]
- uddannelse: values [KU=Kunstnerisk uddannelse, AU=Anden uddannelse, 00=I alt]
- tid: date range 2008-01-01 to 2023-01-01
dim docs: /dim/kulturemner.md

notes:
- kulturemne: numeric codes (0, 1, 8, 12, 20, 23, 29) do NOT join reliably to dim.kulturemner (which uses K-prefix codes for niveau=2). Code 1 matches niveau=1 "Idræt og fritid" but others are broad aggregate groupings not present in the dim. Use inline values from the fact doc rather than joining.
- uddannelse=00 is the total; filter when comparing KU vs AU breakdown.
- kon=10 is the total. Filter all non-target dimensions to their total to avoid overcounting.
- kulturemne=0 is national total across all cultural areas.