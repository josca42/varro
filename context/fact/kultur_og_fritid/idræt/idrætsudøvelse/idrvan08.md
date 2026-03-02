table: fact.idrvan08
description: Voksnes idrætsudøvelse efter socioøkonomisk status, deltagelse og tid
measure: indhold (unit Pct.)
columns:
- socio: values [100=I alt, BES=I beskæftigelse, LED=Ledig/orlov, STU=Studerende, PEN=Pensionist]
- deltag1: values [3=Ja deltager, 4=Ja deltager, men ikke for tiden, 5=Nej, deltager ikke]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- deltag1 values are mutually exclusive and sum to ~100%.
- socio 100 = I alt. Individual socioeconomic categories (BES, LED, STU, PEN) are mutually exclusive.
- Survey data — not annual; data points at 2007, 2011, 2016, 2020, 2024.