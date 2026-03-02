table: fact.van77pm
description: Permanente opholdstilladelser (månedlig) efter statsborgerskab, opholdstilladelse og tid
measure: indhold (unit Antal)
columns:
- statsb: join dim.lande_psd on statsb=kode; levels [3]
- ophold: values [1=Asyl, Flygtningestatus, 2=Asyl, Andet grundlag, 50=Asyl, 51=Brexit, 55=Studie mv., 56=EU/EØS, 57=Familiesammenføring, 5=Familiesammenføring mv., 49=Erhverv / Studie mv., 9=Erhverv, 120=Det øvrige opholdsområde]
- tid: date range 2015-01-01 to 2025-09-01
dim docs: /dim/lande_psd.md

notes:
- Monthly permanent permits only. Same coarser ophold categories as van66p (simpler than van77m).
- statsb and ophold have no total codes — SUM for totals.
- tid is monthly (2015–2025). For annual permanent permits use van66p (from 2003). For all monthly permits (not just permanent) use van77m.