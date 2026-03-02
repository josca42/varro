table: fact.ee3
description: Nyregistrerede dieseldrevne personbiler efter kilometer pr. liter, ejerforhold og tid
measure: indhold (unit Antal)
columns:
- km: values [0=I alt, 1120=Mindre end 5,0 km pr liter, 1125=5,1-5,3 km pr. liter, 1130=5,4-5,5 km pr. liter, 1135=5,6-5,8 km pr. liter ... 1235=22,5-24,9 km pr. liter, 1240=25,0-28,0 km pr. liter, 1245=28,1-32,0 km pr. liter, 1250=Mere end 32,1 km pr. liter, 1255=Uoplyst]
- ejer: values [1000=I alt, 1005=Husholdningerne, 1010=Erhvervene]
- tid: date range 1997-07-01 to 2024-01-01
notes:
- km encodes fuel-efficiency distribution bins for diesel cars (Antal). km=0 (I alt) is the total. Remaining bins are mutually exclusive ranges — summing them equals km=0. Diesel bins use different range boundaries than ee2 (benzin), so don't compare bin-to-bin across tables.
- ejer has total (1000=I alt) plus husholdninger + erhverv. Filter ejer=1000 for overall distribution.
- Data ends 2024-01-01. Covers only diesel cars — for petrol distribution, use ee2.
- For average fuel efficiency (not distribution), use ee1 (energi=100 for km/l).
