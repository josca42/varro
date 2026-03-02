table: fact.edp5
description: Danmarks kvartalsvise ØMU-gæld efter funktion og tid
measure: indhold (unit Mia. kr.)
columns:
- funktion: values [60=Offentlig ØMU-gæld i DKK]
- tid: date range 2000-01-01 to 2025-04-01

notes:
- Single-series table: funktion=60 is the only value (always "Offentlig ØMU-gæld i DKK"). No filtering needed on funktion.
- indhold is in Mia. kr. (billions DKK). Note: edp1 reports Danish debt in Mio. kr. — edp5 values will be ~1000x smaller for the same year.
- Quarterly frequency (tid steps by quarter). Most current Danish ØMU-debt series available — runs through Q1 2025 vs edp1 which is annual through 2024.
- No dimension joins needed. A simple SELECT tid, indhold FROM fact.edp5 ORDER BY tid gives the full time series.