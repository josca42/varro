table: fact.kv2nyh5
description: Barrierer for forbrug af nyheder efter årsag og tid
measure: indhold (unit Pct.)
columns:
- aarsag: values [40560=Det interesserer mig ikke, 40570=Jeg har ikke tid, 40580=Jeg bliver i dårligt humør af nyheder, 40590=Det er for dyrt fx at abonnere, 40600=Jeg orker ikke nyhedsstrømmen, 40610=Der er for meget ligegyldigt i nyhederne, 40620=Det er svært at skelne mellem sandt og falskt, 40630=Det er svært at følge eller forstå nyhederne, 41800=Andre årsager]
- tid: date range 2024-01-01 to 2024-01-01

notes:
- Survey data (2024 only). indhold is Pct. of people citing each reason as a barrier to news consumption.
- aarsag values are NOT mutually exclusive — a person can report multiple reasons. The 9 aarsag values sum to 190%. Never sum across aarsag.
- No koen or alder breakdown — only one row per aarsag/tid combination.
- Compare individual aarsag rows side by side to rank barriers by prevalence.