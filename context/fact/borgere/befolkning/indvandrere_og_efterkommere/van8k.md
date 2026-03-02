table: fact.van8k
description: Indvandringer (foreløbig opgørelse) (kvartal) efter statsborgerskab, køn, opholdstilladelse og tid
measure: indhold (unit Antal)
columns:
- statsb: join dim.lande_psd on statsb=kode; levels [3]
- koen: values [1=Mænd, 2=Kvinder]
- ophold: values [13=Asyl mv., 14=Familiesammenføring til flygtning, 15=Familiesammenføring til dansk/nordisk statsborger, 16=Familiesammenføring til udenlandsk statsborger, 10=Studie mv., Uddannelse, 101=Studie mv., Au pair, 102=Studie mv., Praktikanter, 103=Studie mv., Øvrige grunde, 9=Erhverv, 7=EU/EØS, Lønarbejde, 8=EU/EØS, Uddannelse, 8A=EU/EØS, Øvrige grunde, 12=Det øvrige opholdsområde, Øvrige grunde, 52=Ukraine (særlov)]
- tid: date range 2016-01-01 to 2025-04-01
dim docs: /dim/lande_psd.md

notes:
- This is a FLOW table — counts of people who immigrated during the period, not a stock/population count. (contrast with indoph1/indoph3 which are stocks on 1. januar)
- Quarterly data labeled "foreløbig opgørelse" (preliminary). koen has only 1=Mænd/2=Kvinder, no total.
- statsb and ophold have no total codes — SUM for totals. Note koen column is named "koen" not "kon".
- ophold codes here differ from the van66/van77 permit-type codes — these are arrival-purpose codes (not the permit category system).
- For annual immigration data going back to 1997 use van8a. For permit-holding stock use van66/van77.