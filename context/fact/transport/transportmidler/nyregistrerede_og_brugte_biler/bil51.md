table: fact.bil51
description: Nyregistrerede personbiler efter ejerforhold, drivmiddel og tid
measure: indhold (unit Antal)
columns:
- ejer: values [1000=I alt, 1005=Husholdningerne, 1010=Erhvervene]
- driv: values [20200=Drivmidler i alt, 20205=Benzin, 20210=Diesel, 20215=F-gas, 20220=N-gas, 20225=El, 20230=Petroleum, 20233=Benzinhybrid, 20234=Dieselhybrid, 20231=Brint, 20256=Metanol, 20258=Ætanol]
- tid: date range 2011-01-01 to 2025-09-01
notes:
- Both ejer and driv have total codes that must be filtered to avoid double-counting: ejer=1000 (I alt) includes 1005+1010; driv=20200 (Drivmidler i alt) includes all fuel types.
- For a simple count of new EV registrations: WHERE ejer='1000' AND driv='20225' (El). For EV share: divide by driv='20200'.
- This is the go-to table for fuel-type trends in new personbil registrations (benzin/diesel/el/hybrid split). Covers from 2011-01-01 — for earlier data on fuel mix, use ee2/ee3 (benzin/diesel fuel efficiency distributions).
