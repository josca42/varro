table: fact.flyv2
description: Faste investeringer i lufthavne efter investeringstype, enhed og tid
measure: indhold (unit Mio. kr.)
columns:
- invest: values [1000=INVESTERINGER I ALT, 1500=Anlægsinvesteringer, 2000=Bygningsinvesteringer]
- maengde4: values [2004=Årets priser, 1990=1990-priser, 1995=1995-priser, 2000=2000-priser]
- tid: date range 1992-01-01 to 2023-01-01

notes:
- maengde4 is a price-base selector (Årets priser=2004, 1990-priser, 1995-priser, 2000-priser). Each (invest, tid) has up to 4 rows. Always filter to a single price base — summing across them is meaningless.
- For nominal values use maengde4=2004 (Årets priser). For constant-price time series, pick one fixed base (e.g. maengde4=2000) and stay consistent.
- invest=1000 (INVESTERINGER I ALT) = 1500 (Anlægsinvesteringer) + 2000 (Bygningsinvesteringer). Filter invest to avoid double-counting.
- No lufthavn column — this table gives total investments across all Danish airports, not broken down by individual airport.
- Unit is Mio. kr. Series starts 1992 and ends 2023 (shorter than the traffic tables).