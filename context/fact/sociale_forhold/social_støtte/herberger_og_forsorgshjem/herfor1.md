table: fact.herfor1
description: Personer på herberger og forsorgshjem efter alder, overnatning, køn og tid
measure: indhold (unit Antal)
columns:
- alerams: values [1824=18-24 år, 2529=25-29 år, 3039=30-39 år, 4049=40-49 år, 5059=50-59 år, 6099=60 år og derover, 9999=Uoplyst alder]
- overnat: values [1=1 dag, 2=2-5 dage, 3=6-30 dage, 4=31-119 dage, 5=120-364 dage, 6=Hele året, 9=Uoplyst]
- kon: values [TOT=I alt, 1=Mænd, 2=Kvinder]
- tid: date range 2021-01-01 to 2024-01-01

notes:
- This table counts PEOPLE (personer), not stays. Each person appears exactly once per year in exactly one overnat and one alerams category. Confirmed: herfor1 and herfor2 produce identical person counts per age group.
- No TOT row for alerams or overnat. To get total persons: SUM(indhold) WHERE kon='TOT' (no extra filter needed — summing across all age groups and all duration bands is safe).
- kon has TOT (=1+2). Always filter kon to avoid double-counting: use kon='TOT' for totals or kon='1'/'2' for gender breakdown.
- The fact doc lists 9999=Uoplyst and overnat=9=Uoplyst but neither appears in the actual data (all rows have known age and known duration).
- Sample: 2024 total persons = 7,346. Gender breakdown: kon='1' (men) is the large majority at all age groups.