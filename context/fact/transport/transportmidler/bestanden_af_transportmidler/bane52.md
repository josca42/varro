table: fact.bane52
description: Siddepladser og lasteevne i tog pr. 1. januar efter vogntype, enhed og tid
measure: indhold (unit Antal)
columns:
- vogn2: values [10301=VOGNE I ALT, 10420=VOGNE I TOGSÆT I ALT, 10430=Vogne i dieseldrevne togsæt i alt, 10440=Vogne i dieseldrevne togsæt hos DSB, 10450=Vogne i andre dieseldrevne togsæt, 10460=Vogne i el-drevne togsæt i alt, 10470=Vogne i S-tog, 10480=Vogne i el-drevne togsæt i øvrigt hos DSB, 10490=Vogne i Metro togsæt, 10495=Vogne i Letbane togsæt, 10500=PERSONVOGNE, 10510=GODSVOGNE]
- enhed: values [3000=Siddepladser, 1000, 3010=Lasteevne, 1000 ton]
- tid: date range 1990-01-01 to 2025-01-01

notes:
- enhed is a unit selector: 3000=Siddepladser (in thousands), 3010=Lasteevne (in 1000 ton). Both values are in thousands, not raw units. Always filter to one enhed.
- vogn2 has aggregate codes (10301=VOGNE I ALT, 10420=VOGNE I TOGSÆT I ALT) and subcategories. Filter to the specific vogn2 you need to avoid double-counting hierarchy levels.
- bane51 covers antal togenheder; bane52 covers capacity (seats/load) — they are complementary, not interchangeable.