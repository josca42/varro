table: fact.van66p
description: Permanente opholdstilladelser (år) efter statsborgerskab, opholdstilladelse og tid
measure: indhold (unit Antal)
columns:
- statsb: join dim.lande_psd on statsb=kode; levels [3]
- ophold: values [1=Asyl, Flygtningestatus, 2=Asyl, Andet grundlag, 50=Asyl, 51=Brexit, 55=Studie mv., 56=EU/EØS, 57=Familiesammenføring, 5=Familiesammenføring mv., 49=Erhverv / Studie mv., 9=Erhverv, 120=Det øvrige opholdsområde]
- tid: date range 2003-01-01 to 2024-01-01
dim docs: /dim/lande_psd.md

notes:
- Permanent permits only. ophold categories are simpler/fewer than van66 (fewer sub-types, coarser groupings). No total ophold code — SUM for all-type counts.
- statsb has no total code — SUM across all nationalities for totals.
- tid is annual (2003–2024). For monthly permanent permits use van77pm.
- For all permits (not just permanent) use van66 or van77m.