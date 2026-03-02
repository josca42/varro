table: fact.ft
description: Befolkningen (summariske tal fra folketællinger) efter hovedlandsdele og tid
measure: indhold (unit Antal)
columns:
- hoveddele: join dim.nuts on hoveddele=kode::text [approx]; levels [3]
- tid: date range 1769-01-01 to 2025-01-01
dim docs: /dim/nuts.md

notes:
- Do NOT join dim.nuts for this table. hoveddele uses a historical coding scheme that is incompatible with dim.nuts: codes like 'L11', 'L21', 'L3', 'L4' are strings that cannot be cast to smallint (the dim.nuts.kode type). Only 3 codes (101, 147, 157) happen to match numerically.
- hoveddele codes are self-contained: 000=Hele landet, L11=Hovedstaden, L21=Øerne (uden Hovedstaden), L4=Øerne, L3=Jylland, 101=København, 147=Frederiksberg, 157=Gentofte.
- Longest population series available: from 1769 (census-based counts). Very coarse geography — only 8 geographic units total.
- tid steps are irregular (census years) until recent decades when annual data begins. Not suitable for smooth time-series analysis.
- Use for very long-run historical context only. For anything post-1901 with finer geography, use befolk1/befolk2.