table: fact.van66
description: Opholdstilladelser (år) efter statsborgerskab, opholdstilladelse og tid
measure: indhold (unit Antal)
columns:
- statsb: join dim.lande_psd on statsb=kode; levels [3]
- ophold: values [1=Asyl, Flygtningestatus, 2=Asyl, Andet grundlag, 3A=Familiesammenføring, Ægteskab eller fast samlivsforhold, Refererer til flygtning, 3B=Familiesammenføring, Ægteskab eller fast samlivsforhold, Refererer til udlænding, men ikke flygtning, 3C=Familiesammenføring, Ægteskab eller fast samlivsforhold, Refererer til dansk/nordisk person ... 81=EU/EØS, Familiemedlemmer, 8A=EU/EØS, Øvrige grunde, 11=Det øvrige opholdsområde, Adoption, 12=Det øvrige opholdsområde, Øvrige grunde, 52=Ukraine (særlov)]
- tid: date range 1997-01-01 to 2024-01-01
dim docs: /dim/lande_psd.md

notes:
- statsb has no total code — SUM across all nationalities for total permit counts. All statsb codes are niveau=3 individual countries (~203 nationalities).
- ophold has no total code — SUM across ophold values for all-permit-type counts. Use ColumnValues("van66", "ophold") to see all permit type codes.
- tid is annual (1997–2024). This is the longest annual residence permit series (27 years). For monthly data use van77m.
- indhold = number of NEW permits granted that year. This is a flow count, not a stock.
- Use ColumnValues("lande_psd", "titel", for_table="van66") to browse nationalities.
- For gender/age breakdown use van66ka (annual, from 2014). For permanent permits only use van66p.