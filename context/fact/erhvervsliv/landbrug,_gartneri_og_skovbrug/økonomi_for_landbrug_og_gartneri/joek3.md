table: fact.joek3
description: Jordbrugssektorens forbrug af arbejdskraft efter produkt og tid
measure: indhold (unit 1.000 årsværk)
columns:
- produkt: values [400000=JORDBRUGETS FORBRUG AF ARBEJDSKRAFT I ALT, 410000=Ulønnet arbejdskraft, 420000=Lønnet arbejdskraft]
- tid: date range 2022-01-01 to 2024-01-01
notes:
- Simple 3-value produkt: 400000=I ALT, 410000=Ulønnet, 420000=Lønnet. I ALT = Ulønnet + Lønnet, so don't sum all three.
- Unit is 1.000 årsværk (thousands of full-time equivalents).
