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
- Unique to this table (and van8a): immigration broken down by opholdstilladelse (residence permit type). The 14 ophold categories are mutually exclusive — each immigrant appears under exactly one ophold per (statsb, koen, tid) combination.
- ophold=10 (Studie mv., Uddannelse) coexists with 101 (Au pair), 102 (Praktikanter), 103 (Øvrige grunde) — these are all distinct permit sub-types under the study umbrella, NOT an aggregate/subcategory hierarchy. Summing all 14 ophold values gives the correct total.
- statsb uses niveau 3 (~199 countries). No total row for statsb. koen has no total (1=Mænd, 2=Kvinder).
- Preliminary data (foreløbig). For final annual figures use van8a (from 1997).
- No regional or age breakdown. For those dimensions use van1kvt/van1aar.