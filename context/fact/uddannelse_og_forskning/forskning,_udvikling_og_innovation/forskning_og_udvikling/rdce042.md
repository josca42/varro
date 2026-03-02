table: fact.rdce042
description: Udgifter til FoU efter sektor, forskningstype og tid
measure: indhold (unit Mio. kr.)
columns:
- sektor: values [10=I alt sektor, 100=Private erhverv, 110=Offentlige myndigheder/institutioner, 120=Højere læreanstalter og universitetshospitaler, 130=Private ikke profitdrevne organisationer]
- fui14: values [370=Grundforskning, 380=Anvendt forskning, 390=Eksperimentelt udviklingsarbejde]
- tid: date range 2009-01-01 to 2023-01-01
notes:
- sektor='10' = I alt sektor (total). sektor 100–130 = sub-sectors.
- fui14 has three research-type codes (370=Grundforskning, 380=Anvendt forskning, 390=Eksperimentelt udviklingsarbejde) with no aggregate total — sum all three for combined R&D spending. Note these use different codes than forsk09 (440/450/460) though they represent the same categories.
- Covers all sectors (unlike forsk09 which covers only erhvervslivet). Use rdce042 for cross-sector research-type comparisons.
