table: fact.alko2
description: Salg af alkohol og tobak pr. indbygger efter type og tid
measure: indhold (unit Gns.)
columns:
- type: values [16=Salg af ren alkohol pr. indb. (gns. antal liter), 17=Salg af ren alkohol, pr. indb. over 18 år (gns. antal liter), 25=Salg af cigaretter, pr. indb.  (gns. antal cigaretter), 26=Salg af cigaretter, pr. indb. over 18 år (gns. antal cigaretter)]
- tid: date range 1921-01-01 to 2024-01-01

notes:
- 4 type values, each a per-capita average — never sum across types. Units: liters of pure alcohol (types 16, 17) and number of cigarettes (types 25, 26).
- Types 16 vs 17 (and 25 vs 26) differ by population denominator: whole population vs 18+ only. The 18+ figures (17, 26) are notably higher. Pick one basis and stick with it; mixing them in the same query is misleading.
- No regional or demographic breakdown — national aggregate only.