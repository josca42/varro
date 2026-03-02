table: fact.ligeli1
description: Ligestillingsindikator for løngab efter indikator og tid
measure: indhold (unit Pct.)
columns:
- indikator: values [4=Kvinders andel af mænds løn (pct.), 5=Løngab (pct.)]
- tid: date range 2004-01-01 to 2024-01-01
notes:
- indikator has 2 values that measure the same phenomenon differently: 4=kvinders andel af mænds løn (pct.) e.g. 85% means women earn 85% of men's wages; 5=løngab (pct.) e.g. 15% means a 15% gap. They are complementary (approx. 100 - val4 ≈ val5) but independent rows — never sum them. Always filter to one.
- Only 2 dimensions: indikator + tid. Annual from 2004. Very simple table for national gender pay gap trend.
