table: fact.rdce03
description: Udgifter til FoU efter sektor, udgiftspost og tid
measure: indhold (unit Mio. kr.)
columns:
- sektor: values [10=I alt sektor, 100=Private erhverv, 110=Offentlige myndigheder/institutioner, 120=Højere læreanstalter og universitetshospitaler, 130=Private ikke profitdrevne organisationer]
- udgpost: values [305=Samlede udgifter til FoU i alt (2019 -), 310=Driftsudgifter til FoU i alt, 320=Lønudgifter til FoU, 330=Andre driftsudgifter til FoU, 340=Anlægsudgifter til FoU i alt, 350=Bygninger til FoU, 360=Apparatur og instrumenter til FoU]
- tid: date range 2009-01-01 to 2023-01-01
notes:
- sektor='10' = I alt sektor (total). sektor 100–130 = sub-sectors.
- udgpost hierarchy: 305=Samlede udgifter i alt (available from 2019 onwards). 310=Driftsudgifter i alt = 320 + 330. 340=Anlægsudgifter i alt = 350 + 360. For years before 2019, use 310+340 for total. Never sum 305 + 310 + 340 (double-counting).
- For breakdown by funding source, use rdce01. For breakdown by research type, use rdce042.
