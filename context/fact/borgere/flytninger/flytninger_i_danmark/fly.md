table: fact.fly
description: Samtlige flytninger efter køn, alder og tid
measure: indhold (unit Antal)
columns:
- kon: values [M=Mænd, K=Kvinder]
- alder: values [0=0 år, 1=1 år, 2=2 år, 3=3 år, 4=4 år ... 95=95 år, 96=96 år, 97=97 år, 98=98 år, 99-=99 år og derover]
- tid: date range 1980-01-01 to 2024-01-01

notes:
- No total rows: kon has only M/K and alder only 0–99. Every row is an atomic cell — no overcounting risk when summing.
- This is the longest series (back to 1980) and the only national-level table with individual single-year ages. Use it for time series or age-profile analyses that don't need geography.
- No geographic breakdown. For regional/municipal data use fly33, fly55, or fly66.