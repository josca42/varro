table: fact.ee2
description: Nyregistrerede benzindrevne personbiler efter kilometer pr. liter, ejerforhold og tid
measure: indhold (unit Antal)
columns:
- km: values [0=I alt, 1000=Under 4,5 km pr. liter, 1005=4,5-4,7 km pr. liter, 1010=4,8-4,9 km pr. liter, 1015=5,0-5,2 km pr.liter ... 1100=15,4-16,6 km pr. liter, 1105=16,7-18,1 km pr. liter, 1110=18,2-19,9 km pr. liter, 1115=Mere end 20 km pr. liter, 1255=Uoplyst]
- ejer: values [1000=I alt, 1005=Husholdningerne, 1010=Erhvervene]
- tid: date range 1997-07-01 to 2024-01-01
notes:
- km encodes fuel-efficiency distribution bins for petrol cars (Antal). km=0 (I alt) is the total. Remaining bins are mutually exclusive ranges — summing them equals km=0. Good for distribution analysis (e.g., share of cars above 15 km/l).
- ejer has total (1000=I alt) plus husholdninger + erhverv. Filter ejer=1000 for overall distribution.
- Data ends 2024-01-01. Covers only benzin (petrol) cars — for diesel distribution, use ee3.
- For average fuel efficiency (not distribution), use ee1 (energi=100 for km/l) which covers all fuel types.
