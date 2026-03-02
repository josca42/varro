table: fact.bil50
description: Nyregistrerede personbiler efter ejerforhold, bil segment, enhed og tid
measure: indhold (unit -)
columns:
- ejer: values [1000=I alt, 1100=I husholdningerne, 1200=I erhvervene]
- bilseg: values [0=I alt, 10=Mini, 20=Small, 30=Medium, 40=Large, 50=Executive, 60=Luxury, 70=Sport, 80=Small MPV, 90=Large MPV, 100=Small SUV, 110=Medium SUV, 115=Large SUV, 120=Andre bilsegmenter, 125=Uoplyst]
- enhed: values [9060=Ny registrerede biler (antal), 9065=Købspris (mio. kr), 9070=Gennemsnitlig købspris (kr.), 9075=Gennemsnitlig motoreffekt (kW), 9080=Gennemsnitlig km pr liter (liter), 9085=Gennemsnitlig slagvolumen (cm3)]
- tid: date range 2004-01-01 to 2025-09-01
notes:
- enhed is a critical measurement selector — indhold means completely different things per enhed: 9060=Antal, 9065=Købspris mio. kr., 9070=Gennemsnitlig pris kr., 9075=Gennemsnitlig motoreffekt kW, 9080=Gennemsnitlig km/l, 9085=Gennemsnitlig slagvolumen cm3. Always filter to one enhed. Each ejer×bilseg×tid combination appears exactly 6 times (once per enhed).
- To get average purchase price by segment: filter enhed=9070, pick ejer and bilseg. To get count: enhed=9060.
- ejer and bilseg both have totals (ejer=1000=I alt, bilseg=0=I alt). Filter appropriately to avoid double-counting when aggregating.
- This is the right table for segment-level market analysis (e.g., SUV vs MPV share, average prices by segment).
