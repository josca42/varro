table: fact.hisb9
description: Dødelighedstavle (5-års tavler) efter alder, køn, dødelighedstavle og tid
measure: indhold (unit -)
columns:
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 95=95 år, 96=96 år, 97=97 år, 98=98 år, 99=99 år]
- kon: values [M=Mænd, K=Kvinder]
- tavle: values [1=Overlevende (pr. 100.000), 2=Aldersklassens dødshyppighed (pr. 100.000), 3=Middellevetid (år)]
- tid: date range 1901 to 2025

notes:
- tavle is a measurement-type selector: indhold means completely different things for each value. Always filter to a single tavle. Never aggregate across tavle values.
  - tavle=1: cumulative survivors out of 100,000 born (starts at 100,000 for alder=0)
  - tavle=2: age-specific death rate per 100,000
  - tavle=3: remaining life expectancy in years at each age
- For life expectancy at birth: WHERE tavle=3 AND alder=0. For life expectancy at age 65: WHERE tavle=3 AND alder=65.
- tid is a 5-year range (e.g. [1901,1906), [1906,1911), ...). Use lower(tid) to get the start year.
- No TOT for kon (only M and K). alder has 100 individual ages (0–99), no summary row.
- Same structure as hisb8 (2-year periods from 1981). Use hisb9 for long historical series back to 1901.
