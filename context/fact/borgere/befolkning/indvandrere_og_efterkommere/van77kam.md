table: fact.van77kam
description: Opholdstilladelser (månedlig) efter statsborgerskab, opholdstilladelse, køn, alder og tid
measure: indhold (unit Antal)
columns:
- statsb: join dim.lande_psd on statsb=kode; levels [3]
- ophold: values [1=Asyl, Flygtningestatus, 2=Asyl, Andet grundlag, 3A=Familiesammenføring, Ægteskab eller fast samlivsforhold, Refererer til flygtning, 3B=Familiesammenføring, Ægteskab eller fast samlivsforhold, Refererer til udlænding, men ikke flygtning, 3C=Familiesammenføring, Ægteskab eller fast samlivsforhold, Refererer til dansk/nordisk person ... 81=EU/EØS, Familiemedlemmer, 8A=EU/EØS, Øvrige grunde, 11=Det øvrige opholdsområde, Adoption, 12=Det øvrige opholdsområde, Øvrige grunde, 52=Ukraine (særlov)]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- alder: values [TOT=Alder i alt, 0-4=0-4 år, 5-9=5-9 år, 10-14=10-14 år, 15-19=15-19 år, 20-24=20-24 år, 25-29=25-29 år, 30-34=30-34 år, 35-39=35-39 år, 40-44=40-44 år, 45-49=45-49 år, 50-54=50-54 år, 55-59=55-59 år, 60-64=60-64 år, 65-69=65-69 år, 70OV=70 år og derover]
- tid: date range 2014-01-01 to 2025-09-01
dim docs: /dim/lande_psd.md

notes:
- Monthly residence permits with gender/age breakdown. kon='TOT' and alder='TOT' are the aggregate codes.
- statsb and ophold have no total codes — SUM across all nationalities/permit types for totals.
- tid is monthly (2014–2025). Most granular permit data (monthly + gender + age + nationality + permit type).
- For annual data with gender/age use van66ka. For monthly without gender/age use van77m.