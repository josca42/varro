table: fact.bebrit07
description: Køb via internet - procent af befolkningen (16-74 år) efter type, seneste køb og tid
measure: indhold (unit Pct.)
columns:
- type: values [10=I alt, 40=Alder: 16-19 år, 50=Alder: 20-39 år, 60=Alder: 40-59 år, 70=Alder: 60-74 år ... 210=Indkomst: 0-49.999 kr., 220=Indkomst: 50.000-99.999 kr., 230=Indkomst: 100.000-199.999 kr., 240=Indkomst: 200.000-299.999 kr., 250=Indkomst: 300.000 og derover]
- senkob: values [10=Inden for de sidste 3 måneder., 20=Indenfor det sidste år (men ikke de sidste 3 måneder)., 30=For mere end et år siden., 50=Aldrig købt via internettet]
- tid: date range 2008-01-01 to 2025-01-01
notes:
- type is a demographic selector: type='10' = national total (16-74 år). Never sum across type values. Same breakdown as bebrit02 (alder, køn, beskæftigelse, uddannelse, indkomst).
- senkob categories are mutually exclusive recency buckets. To get "has bought online in past year", filter senkob IN ('10','20'). senkob='50' = never bought online.
- All values are percentages of the 16-74 year old population.
