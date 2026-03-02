table: fact.ee1
description: Nyregistrerede personbiler efter energieffektivitet, ejerforhold, drivmiddel og tid
measure: indhold (unit -)
columns:
- energi: values [100=Km pr. liter, 200=Liter pr. 100 km, 300=Liter pr. 1000 kg. pr. 100 km, 400=Km pr. liter ved 1000 kg]
- ejer: values [1000=I alt, 1005=Husholdningerne, 1010=Erhvervene]
- driv: values [10=I alt, 220=Diesel, 219=Benzin, 222=El, 224=Pluginhybrid]
- tid: date range 1997-07-01 to 2024-06-01
notes:
- energi is a measurement selector with 4 mutually incompatible efficiency metrics for the same car. Never sum across energi. Always filter to one: 100=km/l (most common), 200=l/100km, 300=l/1000kg/100km, 400=km/l at 1000kg.
- indhold unit varies per energi — confirmed: for ejer=1000, driv=10, tid=2023-07-01: km/l=43.29, l/100km=2.31, l/1000kg/100km=1.51, km/l@1000kg=66.43.
- driv=10 is the I alt total (different coding from other tables which use 20200). Subtypes: 219=Benzin, 220=Diesel, 222=El, 224=Pluginhybrid. Note: coding differs from bil51/bil53/bil56 which use 20205/20210/20225.
- Data ends 2024-06-01. For more recent fuel-efficiency context, use bil50 (enhed=9080, gns km/l) which extends to 2025.
- This is the primary table for average fuel efficiency of newly registered cars over time.
