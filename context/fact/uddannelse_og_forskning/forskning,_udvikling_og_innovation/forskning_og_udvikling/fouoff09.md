table: fact.fouoff09
description: Eksternt finansierede FoU-omkostninger efter sektor, fag, finansieringskilde og tid
measure: indhold (unit Mio. kr.)
columns:
- sektor: values [1000=Sektorer i alt, 1100=Højere læreanstalter, 1200=Øvrige offentlige forskningsinstitutioner, 1300=Sektorforskningsinstitutioner, 1400=Private ikke-erhvervsdrivende institutioner]
- vidomr: values [10=Naturvidenskab, 20=Teknisk videnskab, 30=Sundhedsvidenskab, 40=Jordbrugs- og veterinærvidenskab, 50=Samfundsvidenskab, 60=Humaniora]
- finanskilde: values [8000=Finansieringskilder i alt, 8100=Forskningsråd, 8200=Andre statslige midler, 8300=Andre offentlige midler, 8400=Danske virksomheder, 8500=Organisationer, fonde mv., 8600=Udenlandske virksomheder, 8700=EU, 8800=Andre udenlandske kilder]
- tid: date range 2007-01-01 to 2023-01-01
notes:
- sektor='1000' = Sektorer i alt (total). sektor 1100–1400 = individual public sub-sectors.
- vidomr has 6 field codes (10–60), no total code — sum all six for the combined figure.
- finanskilde='8000' = Finansieringskilder i alt (grand total). Codes 8100–8800 are individual external funding sources — they sum to 8000.
- This covers externally funded costs only (eksternt finansierede). For total FoU costs, use fouoff07.
