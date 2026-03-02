table: fact.rdce02
description: Finansiering af FoU fra udlandet efter sektor, finansieringskilde og tid
measure: indhold (unit Mio. kr.)
columns:
- sektor: values [10=I alt sektor, 100=Private erhverv, 110=Offentlige myndigheder/institutioner, 120=Højere læreanstalter og universitetshospitaler, 130=Private ikke profitdrevne organisationer]
- finanskilde: values [410=Private erhverv i udlandet, 420=Virksomheder i samme koncern i udlandet, 430=Andre virksomheder i udlandet, 440=EU-midler, 450=Andre internationale organisationer ekskl. EU, 460=Anden udenlandsk finansiering]
- tid: date range 2007-01-01 to 2023-01-01
notes:
- sektor='10' = I alt sektor (total). sektor 100–130 = sub-sectors.
- finanskilde has 6 codes (410–460) with no aggregate total — sum all six for the combined foreign financing figure.
- This covers only international financing of R&D. For all financing sources including domestic, use rdce01.
