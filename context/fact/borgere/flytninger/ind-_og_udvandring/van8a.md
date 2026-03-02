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
- Final annual version of van8k. Same ophold structure — 14 mutually exclusive permit type categories. ophold=10 is a distinct category, not an aggregate of 101/102/103.
- statsb uses niveau 3 (~204 countries). No total rows for statsb or koen.
- Longest permit-type series: back to 1997. Use this for historical trend in immigration by permit type.
- No regional or age breakdown. For those, use van1aar.