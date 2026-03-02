table: fact.ligedb1
description: Opstillede og valgte kandidater til folketingsvalg efter kandidater, køn, alder og tid
measure: indhold (unit Antal)
columns:
- kandidat: values [OK=Opstillede kandidater, VK=Valgte kandidater]
- kon: values [TOT=I alt, M=Mænd, K=Kvinder]
- alder: values [TOT=Alder i alt, U20=Under 20 år, 2024=20-24 år, 2529=25-29 år, 3034=30-34 år, 3539=35-39 år, 4044=40-44 år, 4549=45-49 år, 5054=50-54 år, 5559=55-59 år, 6064=60-64 år, 6569=65-69 år, 70OV=70 år og derover]
- tid: date range 2001-01-01 to 2022-01-01

notes:
- Three dimensions with aggregate totals: kandidat (OK/VK), kon (TOT/M/K), alder (TOT + 13 age groups). To get a single count, filter all to the desired combination. Example: valgte kvinder i alt: kandidat='VK', kon='K', alder='TOT'.
- Summing all kon values triples the count (TOT=M+K); summing all alder values doubles (TOT + 13 groups). Always filter exactly one value per dimension.
- alder uses coded ranges (e.g. 2024=20–24 år). There are no pre-aggregated age groups beyond TOT — combine ranges in SQL with CASE or IN() if needed.
- National-level only. For gender breakdown without age, ligedi0 (back to 1918) or the kanddat column in fvkand cover more years.
