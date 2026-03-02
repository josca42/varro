table: fact.bane6
description: Jernbanetransport af intermodale lasteenheder efter transporttype, lasteenhed, enhed og tid
measure: indhold (unit -)
columns:
- transport: values [1000=KØRSEL I ALT, 1500=National kørsel, 1600=International kørsel , 4000=Fra Danmark, 5000=Til Danmark, 8000=Transit kørsel]
- last: values [0=I ALT, 40=Container/veksellad, 42=Sættevogn (uledsaget), 44=Lastvogn (ledsaget)]
- maengde4: values [2=Antal lastede enheder, 4=Antal tomme enheder, 6=TEU, lastede enheder, 8=TEU, tomme enheder, 75=1000 ton, 76=Mio. tonkm]
- tid: date range 2004-01-01 to 2024-01-01

notes:
- maengde4 has 6 incomparable measurement types — always filter to exactly one: 2=loaded unit count, 4=empty unit count, 6=TEU loaded, 8=TEU empty, 75=1000 ton, 76=Mio. tonkm. Mixing them is meaningless.
- transport: 1000=total, 1500=national, 1600=international, 4000=fra, 5000=til, 8000=transit. Same aggregate/detail pattern.
- last: 0=I ALT, 40=Container/veksellad, 42=Sættevogn (uledsaget, i.e. unaccompanied trailer), 44=Lastvogn (ledsaget, i.e. accompanied truck). Do not sum all last values — 0 is already the total of 40+42+44.
- Annual data from 2004. Use this table specifically for intermodal unit counts (TEU, trailer counts) — for total freight weight use bane1 or bane9a.