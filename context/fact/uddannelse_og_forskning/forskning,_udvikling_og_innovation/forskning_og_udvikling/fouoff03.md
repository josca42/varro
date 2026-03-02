table: fact.fouoff03
description: FoU årsværk i den offentlige sektor efter formål, fag og tid
measure: indhold (unit Årsværk)
columns:
- formaaal: values [2000=Formål i alt, 3100=Landbrug, 2800=Industri, 2500=Handel, 3300=Produktion ... 3700=Sundhedsvidenskab, 2900=Jordbrug og veterinær, 3800=Samfundsvidenskab, 2600=Humanistisk videnskab, 3500=FoU som ikke kan fordeles]
- vidomr: values [10=Naturvidenskab, 20=Teknisk videnskab, 30=Sundhedsvidenskab, 40=Jordbrugs- og veterinærvidenskab, 50=Samfundsvidenskab, 60=Humaniora]
- tid: date range 2007-01-01 to 2023-01-01
notes:
- formaaal='2000' = Formål i alt (grand total). All other formaaal codes are sub-purposes — their codes are NOT sequential or intuitive (e.g., 2500=Handel, 2800=Industri, 3100=Landbrug). Use ColumnValues("fouoff03", "formaaal") to browse the full list.
- vidomr has 6 field codes (10–60), no total code — sum all six if you want the total across fields.
- To get total FoU årsværk by purpose: WHERE vidomr='10' ... (use one vidomr at a time) or SUM all vidomr, then filter to formaaal of interest.
- For the percentage version of this breakdown, use fouoff04.
