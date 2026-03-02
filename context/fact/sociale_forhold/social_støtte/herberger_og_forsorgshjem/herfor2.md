table: fact.herfor2
description: Personer på herberger og forsorgshjem efter alder, ophold, køn og tid
measure: indhold (unit Antal)
columns:
- alerams: values [1824=18-24 år, 2529=25-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6099=60 år og derover, 9999=Uoplyst alder]
- ophold2: values [11=1 ophold, 12=2 ophold, 13=3-5 ophold, 14=6 ophold og derover]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- tid: date range 2021-01-01 to 2024-01-01

notes:
- This table counts PEOPLE (personer), not stays. Each person appears exactly once per year in exactly one ophold2 and one alerams category. Produces identical person totals to herfor1 — the two tables are different cross-tabulations of the same population.
- No TOT row for alerams or ophold2. To get total persons: SUM(indhold) WHERE kon='TOT'.
- kon has TOT (=1+2). Filter to kon='TOT' for totals or kon='1'/'2' for gender.
- ophold2 captures how many stays a person had that year: 11=1 stay, 12=2, 13=3-5, 14=6+. The categories are mutually exclusive — each person falls in exactly one bucket.