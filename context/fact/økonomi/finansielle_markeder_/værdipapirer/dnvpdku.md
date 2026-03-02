table: fact.dnvpdku
description: Udbytter for VP-registrerede værdipapirer efter papirtype, udstedersektor og tid
measure: indhold (unit Mio. kr.)
columns:
- papir: values [11A=Aktier, i alt, 11N=Aktier, noterede, 11U=Aktier, unoterede, 30A=Investeringsforeningsbeviser, i alt, 30N=Investeringsforeningsbeviser, noterede, 30U=Investeringsforeningsbeviser, unoterede]
- udstedsektor: join dim.esa on udstedsektor=kode [approx]
- tid: date range 1999-12-01 to 2025-09-01
dim docs: /dim/esa.md

notes:
- udstedsektor uses numeric codes (0000, 1000, 1100, 1212, 122P, 122R, etc.) — these do NOT join to dim.esa (which uses S.xxx notation). 0% match rate confirmed. Treat as inline coded values; all labels are embedded in the fact doc.
- Simple table with only two dimension columns (papir, udstedsektor) plus tid. No measurement selectors — each row is one observation (udbytter in Mio. kr.).
- papir has hierarchy: 11A=aktier i alt includes 11N (noterede) and 11U (unoterede); 30A=beviser i alt includes 30N and 30U. Filter to one level only to avoid double-counting.
- This table only covers aktier and investeringsforeningsbeviser — no obligationer. It is a dividend (udbytter) table, not a holdings table.