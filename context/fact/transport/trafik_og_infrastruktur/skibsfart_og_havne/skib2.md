table: fact.skib2
description: Investeringer i havne efter prisenhed, investeringstype og tid
measure: indhold (unit Mio. kr.)
columns:
- prisenhed: values [2004=Årets priser, 1990=1990-priser, 1995=1995-priser, 2000=2000-priser]
- invest: values [1000=INVESTERINGER I ALT, 1500=Anlægsinvesteringer, 2000=Bygningsinvesteringer]
- tid: date range 1992-01-01 to 2023-01-01

notes:
- prisenhed is a price-basis selector: 2004=Årets priser (current/nominal prices), plus three fixed-price bases (1990, 1995, 2000). Always filter to one prisenhed — summing across them is meaningless.
- For real (inflation-adjusted) time series comparisons, pick a fixed-price year. 2004=Årets priser gives nominal values that cannot be meaningfully compared across years.
- invest='1000' (INVESTERINGER I ALT) = 1500 (Anlægsinvesteringer) + 2000 (Bygningsinvesteringer). Filter to 1000 for totals, or pick one subtype for breakdown.
- No harbor-level breakdown — only national aggregates. Longest investment series available (back to 1992).