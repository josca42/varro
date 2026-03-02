table: fact.rdce05
description: Udgifter til FoU efter sektor, videnskabeligt hovedområde og tid
measure: indhold (unit Mio. kr.)
columns:
- sektor: values [10=I alt sektor, 100=Private erhverv, 110=Offentlige myndigheder/institutioner, 120=Højere læreanstalter og universitetshospitaler, 130=Private ikke profitdrevne organisationer]
- videnhoved: values [700=Naturvidenskab, 710=Teknisk videnskab, 720=Sundhedsvidenskab, 730=Jordbrugs- og veterinærvidenskab, 740=Samfundsvidenskab, 750=Humaniora]
- tid: date range 2008-01-01 to 2023-01-01
notes:
- sektor='10' = I alt sektor (total). sektor 100–130 = sub-sectors.
- videnhoved has 6 scientific field codes (700–750) with no aggregate total — sum all six for combined R&D spending by field.
- Compare with fouoff09 (vidomr, different coding) which covers externally funded public-sector FoU only. rdce05 covers all sectors and all funding.
