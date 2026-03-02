table: fact.musik5
description: Registrerede musikværker efter musikværker og tid
measure: indhold (unit 1.000)
columns:
- musvaerk: values [200=Musikværker i alt, 205=Nye musikværker]
- tid: date range 2000-01-01 to 2024-01-01

notes:
- musvaerk=200 is the cumulative total of all registered works in the catalogue; musvaerk=205 is new works registered that year. These are independent measures — never sum them together.
- musvaerk=200 has data from 2000; musvaerk=205 starts from 2001.
- indhold unit is 1.000 (thousands), so multiply by 1000 for exact counts.