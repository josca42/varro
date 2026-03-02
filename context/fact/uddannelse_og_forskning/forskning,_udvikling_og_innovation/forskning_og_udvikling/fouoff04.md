table: fact.fouoff04
description: FoU-årsværk (pct.) efter formål, sektor og tid
measure: indhold (unit Pct.)
columns:
- formaaal: values [2000=Formål i alt, 3100=Landbrug, 2800=Industri, 2500=Handel, 3300=Produktion ... 3700=Sundhedsvidenskab, 2900=Jordbrug og veterinær, 3800=Samfundsvidenskab, 2600=Humanistisk videnskab, 3500=FoU som ikke kan fordeles]
- sekvid: values [1000=Sektorer i alt, 1100=Højere læreanstalter, 1200=Øvrige offentlige forskningsinstitutioner, 1300=Sektorforskningsinstitutioner, 1400=Private ikke-erhvervsdrivende institutioner]
- tid: date range 2007-01-01 to 2023-01-01
notes:
- indhold is a percentage (Pct.) — these are shares of total FoU årsværk, not counts. Never sum across formål to get a meaningful total.
- formaaal='2000' = 100% (the reference total). All other formaaal values show the percentage of FoU effort devoted to that purpose per sekvid — they sum to ~100% when all non-total formål codes are added.
- sekvid='1000' = all public sectors combined. sekvid 1100–1400 = individual sub-sectors.
- For the absolute årsværk counts behind these percentages, use fouoff03.
