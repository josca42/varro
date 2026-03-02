table: fact.bil56
description: Brugte personbiler efter enhed, ejerforhold, drivmiddel og tid
measure: indhold (unit Antal)
columns:
- enhed: values [610=Genregistreringer, 620=Ejerskift, 656=Samlet brugtvognshandel]
- ejer: values [1000=I alt, 1005=Husholdningerne, 1010=Erhvervene]
- driv: values [20200=Drivmidler i alt, 20205=Benzin, 20210=Diesel, 20215=F-gas, 20220=N-gas, 20225=El, 20230=Petroleum, 20233=Benzinhybrid, 20234=Dieselhybrid, 20231=Brint, 20256=Metanol, 20258=Ætanol]
- tid: date range 2011-01-01 to 2025-10-01
notes:
- enhed is a measurement selector: 610=Genregistreringer, 620=Ejerskift, 656=Samlet brugtvognshandel. Verified: 656 = 610 + 620 exactly. Always filter to one enhed; same ejer×driv×tid repeats 3 times.
- ejer and driv both have total codes (ejer=1000, driv=20200). Filter appropriately.
- This is the used-car equivalent of bil51: fuel-type breakdown of used-car trade from 2011. For used-car data without fuel breakdown, bil57 goes back to 2004 and also has seasonally-adjusted series.
