table: fact.van8a
description: Indvandringer (år) efter statsborgerskab, køn, opholdstilladelse og tid
measure: indhold (unit Antal)
columns:
- statsb: join dim.lande_psd on statsb=kode; levels [3]
- koen: values [1=Mænd, 2=Kvinder]
- ophold: values [13=Asyl mv., 14=Familiesammenføring til flygtning, 15=Familiesammenføring til dansk/nordisk statsborger, 16=Familiesammenføring til udenlandsk statsborger, 10=Studie mv., Uddannelse, 101=Studie mv., Au pair, 102=Studie mv., Praktikanter, 103=Studie mv., Øvrige grunde, 9=Erhverv, 7=EU/EØS, Lønarbejde, 8=EU/EØS, Uddannelse, 8A=EU/EØS, Øvrige grunde, 12=Det øvrige opholdsområde, Øvrige grunde, 52=Ukraine (særlov)]
- tid: date range 1997-01-01 to 2024-01-01
dim docs: /dim/lande_psd.md

notes:
- Annual FLOW table — counts of people who immigrated during the year. Not a stock (contrast with folk1/folk2 which count population on 1. januar).
- koen has only 1=Mænd/2=Kvinder, no total. statsb and ophold have no total codes — SUM for totals.
- Note koen column is named "koen" not "kon" (consistent with van8k).
- Goes back to 1997 — the longest immigration flow series. For quarterly (preliminary) data use van8k.
- ophold codes are arrival-purpose categories, same as van8k. Different from the permit categories in van66/van77.
- Use ColumnValues("lande_psd", "titel", for_table="van8a") to see which nationalities are present.