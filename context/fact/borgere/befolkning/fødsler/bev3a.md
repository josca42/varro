table: fact.bev3a
description: Levendefødte og døde efter bevægelse og tid
measure: indhold (unit Antal)
columns:
- bevaegelsev: values [B02=Levendefødte, B03=Døde]
- tid: date range 1901-01-01 to 2025-06-01
notes:
- Simplest births/deaths table. Just 2 mutually exclusive values: B02=Levendefødte, B03=Døde. Filter bevaegelsev='B02' for births, 'B03' for deaths — never sum both.
- Longest national time series for births and deaths: 1901–2025 (monthly resolution). Use this for historical trend analysis. For regional or demographic breakdown, use other tables.
