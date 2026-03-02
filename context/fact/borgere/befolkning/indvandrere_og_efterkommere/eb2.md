table: fact.eb2
description: Børn af efterkommere 1. januar efter Oprindelig herkomst, køn, alder, oprindelsesland og tid
measure: indhold (unit Antal)
columns:
- opher: values [D=Oprindelig person med dansk oprindelse, E=Oprindelig efterkommer]
- kon: values [1=Mænd, 2=Kvinder]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 121=121 år, 122=122 år, 123=123 år, 124=124 år, 125=125 år]
- ieland: values [1=Vestlige lande, 2=Ikke-vestlige lande]
- tid: date range 2007-01-01 to 2025-01-01

notes:
- Like eb1 but ieland is simplified to 1=Vestlige lande / 2=Ikke-vestlige lande (no country detail, no total code).
- alder has individual years (0–125) with no total row. SUM across alder for all-age counts.
- No total row for opher or kon. SUM across both dimensions for overall counts.
- Has individual-year alder (unlike eb1 which has 5-year bands) — useful for precise age analysis of børn af efterkommere.