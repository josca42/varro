table: fact.alko5
description: Salg af alkohol og tobak efter type og tid
measure: indhold (unit Indeks)
columns:
- type: values [200=Pilsnerækvivalenter, 205=Vin, 210=Spiritus, 215=Cigaretter, 220=Cigarer og cigarillos, 225=Røgtobak]
- tid: date range 1955-01-01 to 2024-01-01

notes:
- indhold is an index value (Indeks), not a raw quantity. Values represent relative change over time, not absolute volumes or amounts. Do not sum across types or across years.
- All 6 types start from 1955 with a consistent base. Good for comparing trends across product categories on a common scale — but the underlying absolute volumes (and their units) differ, so the index makes them comparable in relative terms only.
- Use this table when the question is about relative growth/decline trends. Use alko6 for actual quantities.