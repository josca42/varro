table: fact.hisb8
description: Dødelighedstavle (2-års tavler) efter alder, køn, dødelighedstavle og tid
measure: indhold (unit -)
columns:
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 95=95 år, 96=96 år, 97=97 år, 98=98 år, 99=99 år]
- kon: values [M=Mænd, K=Kvinder]
- tavle: values [1=Overlevende (pr. 100.000), 2=Aldersklassens dødshyppighed (pr. 100.000), 3=Middellevetid (år)]
- tid: date range 1981 to 2025

notes:
- tavle is a measurement-type selector: indhold means completely different things for each value. Always filter to a single tavle. Never aggregate across tavle values.
  - tavle=1: cumulative survivors out of 100,000 born (starts at 100,000 for alder=0)
  - tavle=2: age-specific death rate per 100,000
  - tavle=3: remaining life expectancy in years at each age
- For life expectancy at birth: WHERE tavle=3 AND alder=0. For life expectancy at age 65: WHERE tavle=3 AND alder=65.
- tid is a 2-year rolling range (e.g. [1981,1983), [1982,1984), ...). Use lower(tid) to get the start year.
- No TOT for kon (only M and K), so no overcounting risk there. But alder has 100 individual ages (0–99) with no summary row — aggregate in SQL if needed.
- hisb9 has the same structure but with 5-year periods back to 1901. Use hisb8 for recent trends, hisb9 for long historical series.
