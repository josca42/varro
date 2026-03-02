table: fact.skib23
description: Fragtskibes og krydstogtskibes anløb på større danske havne efter havn, skibstype og tid
measure: indhold (unit Antal)
columns:
- havn: values [0=HAVNE I ALT, 10=Avedøreværkets Havn, 12=Avedøre Råstofhavn, 25=Københavns Havn, 70=Stålvalseværkets Havn ... 730=Aalborg Havn, 735=Aalborg Portland Havn, 750=Frederikshavn Havn, 765=Hirtshals Havn, 785=Nordjyllandsværkets Havn]
- skibtype: values [40009=FRAGTSKIBE OG KRYDSTOGSSKIBE I ALT, 40015=Containerskibe, 40025=Bulk-carriers, 40030=Køleskibe, 40031=Tankskibe, 40056=Specialskibe, 40057=Stykgodsskibe i øvrigt, 40058=Pram/lægter til tørlast, 40062=Krydstogtskibe]
- tid: date range 1997-01-01 to 2024-01-01

notes:
- Covers only fragtskibe og krydstogtskibe — not all ship types. For all ship types (lastskibe + passagerskibe), use skib221 instead.
- havn='0' is the national total. The 32 remaining havn codes are individual harbors — no LANDSDEL aggregates (unlike skib101 and skib221). Summing all specific havns gives the national total.
- skibtype='40009' (FRAGTSKIBE OG KRYDSTOGSSKIBE I ALT) is the total of all 8 subtypes. Filter to this for national totals, or pick specific types (40015=Containerskibe, 40025=Bulk-carriers, 40031=Tankskibe, 40062=Krydstogtskibe, etc.).
- Longest time series of the harbor-level tables (from 1997), useful for trend analysis by specific harbor and cargo type.