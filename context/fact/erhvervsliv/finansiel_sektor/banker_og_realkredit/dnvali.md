table: fact.dnvali
description: Intervention, nettokøb af valuta - dagsobservationer efter instrument og tid
measure: indhold (unit Mia. kr.)
columns:
- instrument: values [N7=Interventionskøb af valuta, netto]
- tid: date range 1999-01-04 to 2022-12-30

notes:
- Very simple table: daily net foreign exchange intervention purchases by Nationalbanken, one instrument code only.
- Data ends 2022-12-30 — no recent data.
- Positive values = net purchase of foreign currency (DKK sold); negative = net sale. Time series is very sparse — most days have no intervention (zero or NULL). Use SUM to get monthly/annual totals.