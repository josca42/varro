table: fact.van77m
description: Opholdstilladelser (månedlig) efter statsborgerskab, opholdstilladelse og tid
measure: indhold (unit Antal)
columns:
- statsb: join dim.lande_psd on statsb=kode; levels [3]
- ophold: values [1=Asyl, Flygtningestatus, 2=Asyl, Andet grundlag, 3A=Familiesammenføring, Ægteskab eller fast samlivsforhold, Refererer til flygtning, 3B=Familiesammenføring, Ægteskab eller fast samlivsforhold, Refererer til udlænding, men ikke flygtning, 3C=Familiesammenføring, Ægteskab eller fast samlivsforhold, Refererer til dansk/nordisk person ... 81=EU/EØS, Familiemedlemmer, 8A=EU/EØS, Øvrige grunde, 11=Det øvrige opholdsområde, Adoption, 12=Det øvrige opholdsområde, Øvrige grunde, 52=Ukraine (særlov)]
- tid: date range 2014-01-01 to 2025-09-01
dim docs: /dim/lande_psd.md

notes:
- Monthly residence permits (all types). Same ophold codes as van66 (annual). statsb and ophold have no total codes — SUM for national/all-type totals.
- tid is monthly (2014–2025). Most current monthly permit data.
- For gender/age breakdown use van77kam. For permanent permits only use van77pm. For annual series going back to 1997 use van66.