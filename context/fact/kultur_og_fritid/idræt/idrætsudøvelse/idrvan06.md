table: fact.idrvan06
description: Voksnes idrætsudøvelse efter højest fuldførte uddannelse, deltagelse og tid
measure: indhold (unit Pct.)
columns:
- uddannelsef: values [TOT=I alt, H10=H10 Grundskole, H20=H20 Gymnasiale uddannelser, H30=H30 Erhvervsfaglige uddannelser, H40=H40 Korte videregående uddannelser, KVU, H50=H50 Mellemlange videregående uddannelser, MVU, H70=H70 Lange videregående uddannelser, LVU]
- deltag1: values [3=Ja deltager, 4=Ja deltager, men ikke for tiden, 5=Nej, deltager ikke]
- tid: date range 2007-01-01 to 2024-01-01

notes:
- deltag1 values are mutually exclusive and sum to ~100% (aktiv / aktiv men ikke for tiden / ikke aktiv).
- uddannelsef TOT = I alt. Individual education levels are mutually exclusive categories. H60 (bachelor) is absent — level jumps H50→H70.
- Survey data — not annual; data points at 2007, 2011, 2016, 2020, 2024.