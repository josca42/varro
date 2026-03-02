table: fact.rdce01
description: Udgifter til FoU efter sektor, finansieringskilde og tid
measure: indhold (unit Mio. kr.)
columns:
- sektor: values [10=I alt sektor, 100=Private erhverv, 110=Offentlige myndigheder/institutioner, 120=Højere læreanstalter og universitetshospitaler, 130=Private ikke profitdrevne organisationer]
- finans: values [20.0=Finansieringskilde i alt, 100.0=Private erhverv, 110.0=Offentlige myndigheder/institutioner, 140.0=Offentlige basismidler, 150.0=Offentlige direkte finansiering, 130.0=Private ikke profitdrevne organisationer, 160.0=Udlandet]
- tid: date range 2008-01-01 to 2023-01-01
notes:
- sektor='10' = I alt sektor (grand total). sektor 100–130 are sub-sectors.
- finans='20' = Finansieringskilde i alt (total). Codes 100, 110, 130, 160 are main financing sources summing to 20. Exception: for sektor='120' (Højere læreanstalter), codes 140 and 150 also appear (Offentlige basismidler and Offentlige direkte finansiering — sub-categories of the public funding channel specific to universities). These don't appear for other sektors.
- For the sub-components of international financing, use rdce02. For cost-type breakdown, use rdce03.
